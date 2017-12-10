"""rio_tiler.cbers: cbers processing."""

from functools import partial
from concurrent import futures

import numpy as np
from cachetools.func import lru_cache

import mercantile
import rasterio
from rasterio.warp import transform_bounds

from rio_tiler import utils
from rio_tiler.errors import TileOutsideBounds

CBERS_BUCKET = 's3://cbers-pds'


@lru_cache()
def bounds(sceneid):
    """Retrieve image bounds.

    Attributes
    ----------

    sceneid : str
        CBERS sceneid.

    Returns
    -------
    out : dict
        dictionary with image bounds.
    """

    scene_params = utils.cbers_parse_scene_id(sceneid)
    cbers_address = '{}/{}'.format(CBERS_BUCKET, scene_params['key'])

    with rasterio.open('{}/{}_BAND5.tif'.format(cbers_address, sceneid)) as src:
        wgs_bounds = transform_bounds(
            *[src.crs, 'epsg:4326'] + list(src.bounds), densify_pts=21)

    info = {'sceneid': sceneid}
    info['bounds'] = list(wgs_bounds)

    return info


@lru_cache()
def metadata(sceneid, pmin=2, pmax=98):
    """Retrieve image bounds and histogram info.

    Attributes
    ----------

    sceneid : str
        CBERS sceneid.
    pmin : int, optional, (default: 2)
        Histogram minimum cut.
    pmax : int, optional, (default: 98)
        Histogram maximum cut.

    Returns
    -------
    out : dict
        dictionary with image bounds and bands histogram cuts.
    """

    scene_params = utils.cbersl_parse_scene_id(sceneid)
    cbers_address = '{}/{}'.format(CBERS_BUCKET, scene_params['key'])

    with rasterio.open('{}/preview.jp2'.format(cbers_address)) as src:
        wgs_bounds = transform_bounds(
            *[src.crs, 'epsg:4326'] + list(src.bounds), densify_pts=21)

    info = {'sceneid': sceneid, 'bounds': list(wgs_bounds)}

    bands = ['5', '6', '6', '8']
    addresses = ['{}/{}_BAND{}.tif'.format(cbers_address, sceneid, band) for band in bands]
    _min_max_worker = partial(utils.sentinel_min_max_worker, pmin=pmin, pmax=pmax)
    with futures.ThreadPoolExecutor(max_workers=2) as executor:
        responses = list(executor.map(_min_max_worker, addresses))
        info['rgbMinMax'] = dict(zip(bands, responses))

    return info


@lru_cache()
def tile(sceneid, tile_x, tile_y, tile_z, rgb=('5', '6', '7'), tilesize=256):
    """Create mercator tile from CBERS data.

    Attributes
    ----------

    sceneid : str
        CBERS sceneid.
    tile_x : int
        Mercator tile X index.
    tile_y : int
        Mercator tile Y index.
    tile_z : int
        Mercator tile ZOOM level.
    rgb : tuple, int, optional (default: ('5', '6', '7'))
        Bands index for the RGB combination.
    tilesize : int, optional (default: 256)
        Output image size.

    Returns
    -------
    out : numpy ndarray
    """

    if isinstance(rgb, str):
        rgb = tuple((rgb, ))

    scene_params = utils.cbers_parse_scene_id(sceneid)
    cbers_address = '{}/{}'.format(CBERS_BUCKET, scene_params['key'])

    with rasterio.open('{}/{}_BAND5.tif'.format(cbers_address, sceneid)) as src:
        wgs_bounds = transform_bounds(
            *[src.crs, 'epsg:4326'] + list(src.bounds), densify_pts=21)

    if not utils.tile_exists(wgs_bounds, tile_z, tile_x, tile_y):
        raise TileOutsideBounds('Tile {}/{}/{} is outside image bounds'.format(
            tile_z, tile_x, tile_y))

    mercator_tile = mercantile.Tile(x=tile_x, y=tile_y, z=tile_z)
    tile_bounds = mercantile.xy_bounds(mercator_tile)

    addresses = ['{}/{}_BAND{}.tif'.format(cbers_address, sceneid, band) for band in rgb]

    _tiler = partial(utils.tile_band_worker, bounds=tile_bounds, tilesize=tilesize)
    with futures.ThreadPoolExecutor(max_workers=3) as executor:
        out = np.stack(executor.map(_tiler, addresses))

    return out
