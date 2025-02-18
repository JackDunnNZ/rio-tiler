"""test IO and Warp resampling."""
import os

import pytest

from rio_tiler.io import Reader

PREFIX = os.path.join(os.path.dirname(__file__), "fixtures")
COGEO = os.path.join(PREFIX, "cog.tif")

# RasterIO() resampling method.
# ref: https://gdal.org/api/raster_c_api.html#_CPPv418GDALRIOResampleAlg
io = [
    "nearest",
    "bilinear",
    "cubic",
    "cubic_spline",
    "lanczos",
    "average",
    "mode",
    "gauss",
    "rms",
]

# WarpKernel resampling method.
# ref: https://gdal.org/api/gdalwarp_cpp.html#_CPPv4N14GDALWarpKernel9eResampleE
warp = [
    "nearest",
    "bilinear",
    "cubic",
    "cubic_spline",
    "lanczos",
    "average",
    "mode",
    "sum",
    "rms",
]


@pytest.mark.parametrize("resampling", io)
def test_read_resampling(resampling):
    """Test read with all resampling."""
    with Reader(COGEO) as src:
        im = src.preview(max_size=64, resampling_method=resampling)
        assert im.data.any()


@pytest.mark.parametrize("resampling", warp)
def test_warp_resampling(resampling):
    """Test warp with all resampling."""
    with Reader(COGEO) as src:
        im = src.preview(max_size=64, reproject_method=resampling, dst_crs="epsg:4326")
        assert im.data.any()
