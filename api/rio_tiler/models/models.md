# Module rio_tiler.models

rio-tiler models.

## Variables

```python3
dtype_ranges
```

## Functions

    
### masked_and_3d

```python3
def masked_and_3d(
    array: numpy.ndarray
) -> numpy.ma.core.MaskedArray
```

Makes sure we have a 3D array and mask

    
### rescale_image

```python3
def rescale_image(
    array: numpy.ma.core.MaskedArray,
    in_range: Sequence[Tuple[Union[float, int], Union[float, int]]],
    out_range: Sequence[Tuple[Union[float, int], Union[float, int]]] = ((0, 255),),
    out_dtype: Union[str, numpy.number] = 'uint8'
) -> numpy.ma.core.MaskedArray
```

Rescale image data in-place.

    
### to_coordsbbox

```python3
def to_coordsbbox(
    bbox
) -> Union[rasterio.coords.BoundingBox, NoneType]
```

Convert bbox to CoordsBbox nameTuple.

    
### to_masked

```python3
def to_masked(
    array: numpy.ndarray
) -> numpy.ma.core.MaskedArray
```

Makes sure we have a MaskedArray.

## Classes

### BandStatistics

```python3
class BandStatistics(
    __pydantic_self__,
    **data: Any
)
```

Band statistics

#### Ancestors (in MRO)

* rio_tiler.models.RioTilerBaseModel
* pydantic.main.BaseModel
* pydantic.utils.Representation

#### Class variables

```python3
Config
```

#### Static methods

    
#### construct

```python3
def construct(
    _fields_set: Union[ForwardRef('SetStr'), NoneType] = None,
    **values: Any
) -> 'Model'
```

Creates a new model setting __dict__ and __fields_set__ from trusted or pre-validated data.

Default values are respected, but no other validation is performed.
Behaves as if `Config.extra = 'allow'` was set since it adds all passed values

    
#### from_orm

```python3
def from_orm(
    obj: Any
) -> 'Model'
```

    
#### parse_file

```python3
def parse_file(
    path: Union[str, pathlib.Path],
    *,
    content_type: 'unicode' = None,
    encoding: 'unicode' = 'utf8',
    proto: pydantic.parse.Protocol = None,
    allow_pickle: bool = False
) -> 'Model'
```

    
#### parse_obj

```python3
def parse_obj(
    obj: Any
) -> 'Model'
```

    
#### parse_raw

```python3
def parse_raw(
    b: Union[str, bytes],
    *,
    content_type: 'unicode' = None,
    encoding: 'unicode' = 'utf8',
    proto: pydantic.parse.Protocol = None,
    allow_pickle: bool = False
) -> 'Model'
```

    
#### schema

```python3
def schema(
    by_alias: bool = True,
    ref_template: 'unicode' = '#/definitions/{model}'
) -> 'DictStrAny'
```

    
#### schema_json

```python3
def schema_json(
    *,
    by_alias: bool = True,
    ref_template: 'unicode' = '#/definitions/{model}',
    **dumps_kwargs: Any
) -> 'unicode'
```

    
#### update_forward_refs

```python3
def update_forward_refs(
    **localns: Any
) -> None
```

Try to update ForwardRefs on fields based on this Model, globalns and localns.

    
#### validate

```python3
def validate(
    value: Any
) -> 'Model'
```

#### Methods

    
#### copy

```python3
def copy(
    self: 'Model',
    *,
    include: Union[ForwardRef('AbstractSetIntStr'), ForwardRef('MappingIntStrAny'), NoneType] = None,
    exclude: Union[ForwardRef('AbstractSetIntStr'), ForwardRef('MappingIntStrAny'), NoneType] = None,
    update: Union[ForwardRef('DictStrAny'), NoneType] = None,
    deep: bool = False
) -> 'Model'
```

Duplicate a model, optionally choose which fields to include, exclude and change.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| include | None | fields to include in new model | None |
| exclude | None | fields to exclude from new model, as with values this takes precedence over include | None |
| update | None | values to change/add in the new model. Note: the data is not validated before creating<br>the new model: you should trust this data | None |
| deep | None | set to `True` to make a deep copy of the model | None |

**Returns:**

| Type | Description |
|---|---|
| None | new model instance |

    
#### dict

```python3
def dict(
    self,
    *,
    include: Union[ForwardRef('AbstractSetIntStr'), ForwardRef('MappingIntStrAny'), NoneType] = None,
    exclude: Union[ForwardRef('AbstractSetIntStr'), ForwardRef('MappingIntStrAny'), NoneType] = None,
    by_alias: bool = False,
    skip_defaults: Union[bool, NoneType] = None,
    exclude_unset: bool = False,
    exclude_defaults: bool = False,
    exclude_none: bool = False
) -> 'DictStrAny'
```

Generate a dictionary representation of the model, optionally specifying which fields to include or exclude.

    
#### json

```python3
def json(
    self,
    *,
    include: Union[ForwardRef('AbstractSetIntStr'), ForwardRef('MappingIntStrAny'), NoneType] = None,
    exclude: Union[ForwardRef('AbstractSetIntStr'), ForwardRef('MappingIntStrAny'), NoneType] = None,
    by_alias: bool = False,
    skip_defaults: Union[bool, NoneType] = None,
    exclude_unset: bool = False,
    exclude_defaults: bool = False,
    exclude_none: bool = False,
    encoder: Union[Callable[[Any], Any], NoneType] = None,
    models_as_dict: bool = True,
    **dumps_kwargs: Any
) -> 'unicode'
```

Generate a JSON representation of the model, `include` and `exclude` arguments as per `dict()`.

`encoder` is an optional function to supply as `default` to json.dumps(), other arguments as per `json.dumps()`.

### Bounds

```python3
class Bounds(
    __pydantic_self__,
    **data: Any
)
```

Dataset Bounding box

#### Ancestors (in MRO)

* rio_tiler.models.RioTilerBaseModel
* pydantic.main.BaseModel
* pydantic.utils.Representation

#### Descendants

* rio_tiler.models.SpatialInfo

#### Class variables

```python3
Config
```

#### Static methods

    
#### construct

```python3
def construct(
    _fields_set: Union[ForwardRef('SetStr'), NoneType] = None,
    **values: Any
) -> 'Model'
```

Creates a new model setting __dict__ and __fields_set__ from trusted or pre-validated data.

Default values are respected, but no other validation is performed.
Behaves as if `Config.extra = 'allow'` was set since it adds all passed values

    
#### from_orm

```python3
def from_orm(
    obj: Any
) -> 'Model'
```

    
#### parse_file

```python3
def parse_file(
    path: Union[str, pathlib.Path],
    *,
    content_type: 'unicode' = None,
    encoding: 'unicode' = 'utf8',
    proto: pydantic.parse.Protocol = None,
    allow_pickle: bool = False
) -> 'Model'
```

    
#### parse_obj

```python3
def parse_obj(
    obj: Any
) -> 'Model'
```

    
#### parse_raw

```python3
def parse_raw(
    b: Union[str, bytes],
    *,
    content_type: 'unicode' = None,
    encoding: 'unicode' = 'utf8',
    proto: pydantic.parse.Protocol = None,
    allow_pickle: bool = False
) -> 'Model'
```

    
#### schema

```python3
def schema(
    by_alias: bool = True,
    ref_template: 'unicode' = '#/definitions/{model}'
) -> 'DictStrAny'
```

    
#### schema_json

```python3
def schema_json(
    *,
    by_alias: bool = True,
    ref_template: 'unicode' = '#/definitions/{model}',
    **dumps_kwargs: Any
) -> 'unicode'
```

    
#### update_forward_refs

```python3
def update_forward_refs(
    **localns: Any
) -> None
```

Try to update ForwardRefs on fields based on this Model, globalns and localns.

    
#### validate

```python3
def validate(
    value: Any
) -> 'Model'
```

#### Methods

    
#### copy

```python3
def copy(
    self: 'Model',
    *,
    include: Union[ForwardRef('AbstractSetIntStr'), ForwardRef('MappingIntStrAny'), NoneType] = None,
    exclude: Union[ForwardRef('AbstractSetIntStr'), ForwardRef('MappingIntStrAny'), NoneType] = None,
    update: Union[ForwardRef('DictStrAny'), NoneType] = None,
    deep: bool = False
) -> 'Model'
```

Duplicate a model, optionally choose which fields to include, exclude and change.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| include | None | fields to include in new model | None |
| exclude | None | fields to exclude from new model, as with values this takes precedence over include | None |
| update | None | values to change/add in the new model. Note: the data is not validated before creating<br>the new model: you should trust this data | None |
| deep | None | set to `True` to make a deep copy of the model | None |

**Returns:**

| Type | Description |
|---|---|
| None | new model instance |

    
#### dict

```python3
def dict(
    self,
    *,
    include: Union[ForwardRef('AbstractSetIntStr'), ForwardRef('MappingIntStrAny'), NoneType] = None,
    exclude: Union[ForwardRef('AbstractSetIntStr'), ForwardRef('MappingIntStrAny'), NoneType] = None,
    by_alias: bool = False,
    skip_defaults: Union[bool, NoneType] = None,
    exclude_unset: bool = False,
    exclude_defaults: bool = False,
    exclude_none: bool = False
) -> 'DictStrAny'
```

Generate a dictionary representation of the model, optionally specifying which fields to include or exclude.

    
#### json

```python3
def json(
    self,
    *,
    include: Union[ForwardRef('AbstractSetIntStr'), ForwardRef('MappingIntStrAny'), NoneType] = None,
    exclude: Union[ForwardRef('AbstractSetIntStr'), ForwardRef('MappingIntStrAny'), NoneType] = None,
    by_alias: bool = False,
    skip_defaults: Union[bool, NoneType] = None,
    exclude_unset: bool = False,
    exclude_defaults: bool = False,
    exclude_none: bool = False,
    encoder: Union[Callable[[Any], Any], NoneType] = None,
    models_as_dict: bool = True,
    **dumps_kwargs: Any
) -> 'unicode'
```

Generate a JSON representation of the model, `include` and `exclude` arguments as per `dict()`.

`encoder` is an optional function to supply as `default` to json.dumps(), other arguments as per `json.dumps()`.

### ImageData

```python3
class ImageData(
    array: numpy.ndarray,
    cutline_mask: Union[numpy.ndarray, NoneType] = None,
    *,
    assets: Union[List, NoneType] = None,
    bounds=None,
    crs: Union[rasterio.crs.CRS, NoneType] = None,
    metadata: Union[Dict, NoneType] = NOTHING,
    band_names: List[str] = NOTHING,
    dataset_statistics: Union[Sequence[Tuple[float, float]], NoneType] = None
)
```

Image Data class.

#### Attributes

| Name | Type | Description | Default |
|---|---|---|---|
| array | numpy.ma.MaskedArray | image values. | None |
| assets | list | list of assets used to construct the data values. | None |
| bounds | BoundingBox | bounding box of the data. | None |
| crs | rasterio.crs.CRS | Coordinates Reference System of the bounds. | None |
| metadata | dict | Additional metadata. Defaults to `{}`. | `{}` |
| band_names | list | name of each band. Defaults to `["1", "2", "3"]` for 3 bands image. | `["1", "2", "3"]` for 3 bands image |
| dataset_statistics | list | dataset statistics `[(min, max), (min, max)]` | None |

#### Static methods

    
#### create_from_list

```python3
def create_from_list(
    data: Sequence[ForwardRef('ImageData')]
) -> 'ImageData'
```

Create ImageData from a sequence of ImageData objects.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| data | sequence | sequence of ImageData. | None |

    
#### from_array

```python3
def from_array(
    arr: numpy.ndarray
) -> 'ImageData'
```

Create ImageData from a numpy array.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| arr | numpy.ndarray | Numpy array or Numpy masked array. | None |

    
#### from_bytes

```python3
def from_bytes(
    data: bytes
) -> 'ImageData'
```

Create ImageData from bytes.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| data | bytes | raster dataset as bytes. | None |

#### Instance variables

```python3
count
```

Number of band.

```python3
data
```

Return data part of the masked array.

```python3
height
```

Height of the data array.

```python3
mask
```

Return Mask in form of rasterio dataset mask.

```python3
transform
```

Returns the affine transform.

```python3
width
```

Width of the data array.

#### Methods

    
#### apply_color_formula

```python3
def apply_color_formula(
    self,
    color_formula: Union[str, NoneType]
)
```

Apply color-operations formula in place.

    
#### apply_colormap

```python3
def apply_colormap(
    self,
    colormap: Union[Dict[int, Tuple[int, int, int, int]], Sequence[Tuple[Tuple[Union[float, int], Union[float, int]], Tuple[int, int, int, int]]]]
) -> 'ImageData'
```

Apply colormap to the image data.

    
#### apply_expression

```python3
def apply_expression(
    self,
    expression: str
) -> 'ImageData'
```

Apply expression to the image data.

    
#### as_masked

```python3
def as_masked(
    self
) -> numpy.ma.core.MaskedArray
```

return a numpy masked array.

    
#### clip

```python3
def clip(
    self,
    bbox: Tuple[float, float, float, float]
) -> 'ImageData'
```

Clip data and mask to a bbox.

    
#### data_as_image

```python3
def data_as_image(
    self
) -> numpy.ndarray
```

Return the data array reshaped into an image processing/visualization software friendly order.

(bands, rows, columns) -> (rows, columns, bands).

    
#### post_process

```python3
def post_process(
    self,
    in_range: Union[Sequence[Tuple[Union[float, int], Union[float, int]]], NoneType] = None,
    out_dtype: Union[str, numpy.number] = 'uint8',
    color_formula: Union[str, NoneType] = None,
    **kwargs: Any
) -> 'ImageData'
```

Post-process image data.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| in_range | tuple | input min/max bounds value to rescale from. | None |
| out_dtype | str | output datatype after rescaling. Defaults to `uint8`. | `uint8` |
| color_formula | str | color-ops formula (see: https://github.com/vincentsarago/color-ops). | None |
| kwargs | optional | keyword arguments to forward to `rio_tiler.utils.linear_rescale`. | None |

**Returns:**

| Type | Description |
|---|---|
| ImageData | new ImageData object with the updated data. |

    
#### render

```python3
def render(
    self,
    add_mask: bool = True,
    img_format: str = 'PNG',
    colormap: Union[Dict[int, Tuple[int, int, int, int]], Sequence[Tuple[Tuple[Union[float, int], Union[float, int]], Tuple[int, int, int, int]]], NoneType] = None,
    **kwargs
) -> bytes
```

Render data to image blob.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| add_mask | bool | add mask to output image. Defaults to `True`. | `True` |
| img_format | str | output image format. Defaults to `PNG`. | `PNG` |
| colormap | dict or sequence | RGBA Color Table dictionary or sequence. | None |
| kwargs | optional | keyword arguments to forward to `rio_tiler.utils.render`. | None |

**Returns:**

| Type | Description |
|---|---|
| bytes | image. |

    
#### rescale

```python3
def rescale(
    self,
    in_range: Sequence[Tuple[Union[float, int], Union[float, int]]],
    out_range: Sequence[Tuple[Union[float, int], Union[float, int]]] = ((0, 255),),
    out_dtype: Union[str, numpy.number] = 'uint8'
)
```

Rescale data in place.

    
#### resize

```python3
def resize(
    self,
    height: int,
    width: int,
    resampling_method: Literal['nearest', 'bilinear', 'cubic', 'cubic_spline', 'lanczos', 'average', 'mode', 'gauss', 'rms'] = 'nearest'
) -> 'ImageData'
```

Resize data and mask.

    
#### statistics

```python3
def statistics(
    self,
    categorical: bool = False,
    categories: Union[List[float], NoneType] = None,
    percentiles: Union[List[int], NoneType] = None,
    hist_options: Union[Dict, NoneType] = None
) -> Dict[str, rio_tiler.models.BandStatistics]
```

Return statistics from ImageData.

### Info

```python3
class Info(
    __pydantic_self__,
    **data: Any
)
```

Dataset Info.

#### Ancestors (in MRO)

* rio_tiler.models.SpatialInfo
* rio_tiler.models.Bounds
* rio_tiler.models.RioTilerBaseModel
* pydantic.main.BaseModel
* pydantic.utils.Representation

#### Class variables

```python3
Config
```

#### Static methods

    
#### construct

```python3
def construct(
    _fields_set: Union[ForwardRef('SetStr'), NoneType] = None,
    **values: Any
) -> 'Model'
```

Creates a new model setting __dict__ and __fields_set__ from trusted or pre-validated data.

Default values are respected, but no other validation is performed.
Behaves as if `Config.extra = 'allow'` was set since it adds all passed values

    
#### from_orm

```python3
def from_orm(
    obj: Any
) -> 'Model'
```

    
#### parse_file

```python3
def parse_file(
    path: Union[str, pathlib.Path],
    *,
    content_type: 'unicode' = None,
    encoding: 'unicode' = 'utf8',
    proto: pydantic.parse.Protocol = None,
    allow_pickle: bool = False
) -> 'Model'
```

    
#### parse_obj

```python3
def parse_obj(
    obj: Any
) -> 'Model'
```

    
#### parse_raw

```python3
def parse_raw(
    b: Union[str, bytes],
    *,
    content_type: 'unicode' = None,
    encoding: 'unicode' = 'utf8',
    proto: pydantic.parse.Protocol = None,
    allow_pickle: bool = False
) -> 'Model'
```

    
#### schema

```python3
def schema(
    by_alias: bool = True,
    ref_template: 'unicode' = '#/definitions/{model}'
) -> 'DictStrAny'
```

    
#### schema_json

```python3
def schema_json(
    *,
    by_alias: bool = True,
    ref_template: 'unicode' = '#/definitions/{model}',
    **dumps_kwargs: Any
) -> 'unicode'
```

    
#### update_forward_refs

```python3
def update_forward_refs(
    **localns: Any
) -> None
```

Try to update ForwardRefs on fields based on this Model, globalns and localns.

    
#### validate

```python3
def validate(
    value: Any
) -> 'Model'
```

#### Methods

    
#### copy

```python3
def copy(
    self: 'Model',
    *,
    include: Union[ForwardRef('AbstractSetIntStr'), ForwardRef('MappingIntStrAny'), NoneType] = None,
    exclude: Union[ForwardRef('AbstractSetIntStr'), ForwardRef('MappingIntStrAny'), NoneType] = None,
    update: Union[ForwardRef('DictStrAny'), NoneType] = None,
    deep: bool = False
) -> 'Model'
```

Duplicate a model, optionally choose which fields to include, exclude and change.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| include | None | fields to include in new model | None |
| exclude | None | fields to exclude from new model, as with values this takes precedence over include | None |
| update | None | values to change/add in the new model. Note: the data is not validated before creating<br>the new model: you should trust this data | None |
| deep | None | set to `True` to make a deep copy of the model | None |

**Returns:**

| Type | Description |
|---|---|
| None | new model instance |

    
#### dict

```python3
def dict(
    self,
    *,
    include: Union[ForwardRef('AbstractSetIntStr'), ForwardRef('MappingIntStrAny'), NoneType] = None,
    exclude: Union[ForwardRef('AbstractSetIntStr'), ForwardRef('MappingIntStrAny'), NoneType] = None,
    by_alias: bool = False,
    skip_defaults: Union[bool, NoneType] = None,
    exclude_unset: bool = False,
    exclude_defaults: bool = False,
    exclude_none: bool = False
) -> 'DictStrAny'
```

Generate a dictionary representation of the model, optionally specifying which fields to include or exclude.

    
#### json

```python3
def json(
    self,
    *,
    include: Union[ForwardRef('AbstractSetIntStr'), ForwardRef('MappingIntStrAny'), NoneType] = None,
    exclude: Union[ForwardRef('AbstractSetIntStr'), ForwardRef('MappingIntStrAny'), NoneType] = None,
    by_alias: bool = False,
    skip_defaults: Union[bool, NoneType] = None,
    exclude_unset: bool = False,
    exclude_defaults: bool = False,
    exclude_none: bool = False,
    encoder: Union[Callable[[Any], Any], NoneType] = None,
    models_as_dict: bool = True,
    **dumps_kwargs: Any
) -> 'unicode'
```

Generate a JSON representation of the model, `include` and `exclude` arguments as per `dict()`.

`encoder` is an optional function to supply as `default` to json.dumps(), other arguments as per `json.dumps()`.

### NodataTypes

```python3
class NodataTypes(
    /,
    *args,
    **kwargs
)
```

rio-tiler Nodata types.

#### Ancestors (in MRO)

* builtins.str
* enum.Enum

#### Class variables

```python3
Alpha
```

```python3
Empty
```

```python3
Internal
```

```python3
Mask
```

```python3
Nodata
```

```python3
name
```

```python3
value
```

### PointData

```python3
class PointData(
    array: numpy.ndarray,
    *,
    band_names: List[str] = NOTHING,
    coordinates: Union[Tuple[float, float], NoneType] = None,
    crs: Union[rasterio.crs.CRS, NoneType] = None,
    assets: Union[List, NoneType] = None,
    metadata: Union[Dict, NoneType] = NOTHING
)
```

Point Data class.

#### Attributes

| Name | Type | Description | Default |
|---|---|---|---|
| array | numpy.ma.MaskedArray | pixel values. | None |
| band_names | list | name of each band. Defaults to `["1", "2", "3"]` for 3 bands image. | `["1", "2", "3"]` for 3 bands image |
| coordinates | tuple | Point's coordinates. | None |
| crs | rasterio.crs.CRS | Coordinates Reference System of the bounds. | None |
| assets | list | list of assets used to construct the data values. | None |
| metadata | dict | Additional metadata. Defaults to `{}`. | `{}` |

#### Static methods

    
#### create_from_list

```python3
def create_from_list(
    data: Sequence[ForwardRef('PointData')]
)
```

Create PointData from a sequence of PointsData objects.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| data | sequence | sequence of PointData. | None |

#### Instance variables

```python3
count
```

Number of band.

```python3
data
```

Return data part of the masked array.

```python3
mask
```

Return Mask in form of rasterio dataset mask.

#### Methods

    
#### apply_expression

```python3
def apply_expression(
    self,
    expression: str
) -> 'PointData'
```

Apply expression to the image data.

    
#### as_masked

```python3
def as_masked(
    self
) -> numpy.ma.core.MaskedArray
```

return a numpy masked array.

### RioTilerBaseModel

```python3
class RioTilerBaseModel(
    __pydantic_self__,
    **data: Any
)
```

Base Model for rio-tiler models.

#### Ancestors (in MRO)

* pydantic.main.BaseModel
* pydantic.utils.Representation

#### Descendants

* rio_tiler.models.Bounds
* rio_tiler.models.BandStatistics

#### Class variables

```python3
Config
```

#### Static methods

    
#### construct

```python3
def construct(
    _fields_set: Union[ForwardRef('SetStr'), NoneType] = None,
    **values: Any
) -> 'Model'
```

Creates a new model setting __dict__ and __fields_set__ from trusted or pre-validated data.

Default values are respected, but no other validation is performed.
Behaves as if `Config.extra = 'allow'` was set since it adds all passed values

    
#### from_orm

```python3
def from_orm(
    obj: Any
) -> 'Model'
```

    
#### parse_file

```python3
def parse_file(
    path: Union[str, pathlib.Path],
    *,
    content_type: 'unicode' = None,
    encoding: 'unicode' = 'utf8',
    proto: pydantic.parse.Protocol = None,
    allow_pickle: bool = False
) -> 'Model'
```

    
#### parse_obj

```python3
def parse_obj(
    obj: Any
) -> 'Model'
```

    
#### parse_raw

```python3
def parse_raw(
    b: Union[str, bytes],
    *,
    content_type: 'unicode' = None,
    encoding: 'unicode' = 'utf8',
    proto: pydantic.parse.Protocol = None,
    allow_pickle: bool = False
) -> 'Model'
```

    
#### schema

```python3
def schema(
    by_alias: bool = True,
    ref_template: 'unicode' = '#/definitions/{model}'
) -> 'DictStrAny'
```

    
#### schema_json

```python3
def schema_json(
    *,
    by_alias: bool = True,
    ref_template: 'unicode' = '#/definitions/{model}',
    **dumps_kwargs: Any
) -> 'unicode'
```

    
#### update_forward_refs

```python3
def update_forward_refs(
    **localns: Any
) -> None
```

Try to update ForwardRefs on fields based on this Model, globalns and localns.

    
#### validate

```python3
def validate(
    value: Any
) -> 'Model'
```

#### Methods

    
#### copy

```python3
def copy(
    self: 'Model',
    *,
    include: Union[ForwardRef('AbstractSetIntStr'), ForwardRef('MappingIntStrAny'), NoneType] = None,
    exclude: Union[ForwardRef('AbstractSetIntStr'), ForwardRef('MappingIntStrAny'), NoneType] = None,
    update: Union[ForwardRef('DictStrAny'), NoneType] = None,
    deep: bool = False
) -> 'Model'
```

Duplicate a model, optionally choose which fields to include, exclude and change.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| include | None | fields to include in new model | None |
| exclude | None | fields to exclude from new model, as with values this takes precedence over include | None |
| update | None | values to change/add in the new model. Note: the data is not validated before creating<br>the new model: you should trust this data | None |
| deep | None | set to `True` to make a deep copy of the model | None |

**Returns:**

| Type | Description |
|---|---|
| None | new model instance |

    
#### dict

```python3
def dict(
    self,
    *,
    include: Union[ForwardRef('AbstractSetIntStr'), ForwardRef('MappingIntStrAny'), NoneType] = None,
    exclude: Union[ForwardRef('AbstractSetIntStr'), ForwardRef('MappingIntStrAny'), NoneType] = None,
    by_alias: bool = False,
    skip_defaults: Union[bool, NoneType] = None,
    exclude_unset: bool = False,
    exclude_defaults: bool = False,
    exclude_none: bool = False
) -> 'DictStrAny'
```

Generate a dictionary representation of the model, optionally specifying which fields to include or exclude.

    
#### json

```python3
def json(
    self,
    *,
    include: Union[ForwardRef('AbstractSetIntStr'), ForwardRef('MappingIntStrAny'), NoneType] = None,
    exclude: Union[ForwardRef('AbstractSetIntStr'), ForwardRef('MappingIntStrAny'), NoneType] = None,
    by_alias: bool = False,
    skip_defaults: Union[bool, NoneType] = None,
    exclude_unset: bool = False,
    exclude_defaults: bool = False,
    exclude_none: bool = False,
    encoder: Union[Callable[[Any], Any], NoneType] = None,
    models_as_dict: bool = True,
    **dumps_kwargs: Any
) -> 'unicode'
```

Generate a JSON representation of the model, `include` and `exclude` arguments as per `dict()`.

`encoder` is an optional function to supply as `default` to json.dumps(), other arguments as per `json.dumps()`.

### SpatialInfo

```python3
class SpatialInfo(
    __pydantic_self__,
    **data: Any
)
```

Dataset SpatialInfo

#### Ancestors (in MRO)

* rio_tiler.models.Bounds
* rio_tiler.models.RioTilerBaseModel
* pydantic.main.BaseModel
* pydantic.utils.Representation

#### Descendants

* rio_tiler.models.Info

#### Class variables

```python3
Config
```

#### Static methods

    
#### construct

```python3
def construct(
    _fields_set: Union[ForwardRef('SetStr'), NoneType] = None,
    **values: Any
) -> 'Model'
```

Creates a new model setting __dict__ and __fields_set__ from trusted or pre-validated data.

Default values are respected, but no other validation is performed.
Behaves as if `Config.extra = 'allow'` was set since it adds all passed values

    
#### from_orm

```python3
def from_orm(
    obj: Any
) -> 'Model'
```

    
#### parse_file

```python3
def parse_file(
    path: Union[str, pathlib.Path],
    *,
    content_type: 'unicode' = None,
    encoding: 'unicode' = 'utf8',
    proto: pydantic.parse.Protocol = None,
    allow_pickle: bool = False
) -> 'Model'
```

    
#### parse_obj

```python3
def parse_obj(
    obj: Any
) -> 'Model'
```

    
#### parse_raw

```python3
def parse_raw(
    b: Union[str, bytes],
    *,
    content_type: 'unicode' = None,
    encoding: 'unicode' = 'utf8',
    proto: pydantic.parse.Protocol = None,
    allow_pickle: bool = False
) -> 'Model'
```

    
#### schema

```python3
def schema(
    by_alias: bool = True,
    ref_template: 'unicode' = '#/definitions/{model}'
) -> 'DictStrAny'
```

    
#### schema_json

```python3
def schema_json(
    *,
    by_alias: bool = True,
    ref_template: 'unicode' = '#/definitions/{model}',
    **dumps_kwargs: Any
) -> 'unicode'
```

    
#### update_forward_refs

```python3
def update_forward_refs(
    **localns: Any
) -> None
```

Try to update ForwardRefs on fields based on this Model, globalns and localns.

    
#### validate

```python3
def validate(
    value: Any
) -> 'Model'
```

#### Methods

    
#### copy

```python3
def copy(
    self: 'Model',
    *,
    include: Union[ForwardRef('AbstractSetIntStr'), ForwardRef('MappingIntStrAny'), NoneType] = None,
    exclude: Union[ForwardRef('AbstractSetIntStr'), ForwardRef('MappingIntStrAny'), NoneType] = None,
    update: Union[ForwardRef('DictStrAny'), NoneType] = None,
    deep: bool = False
) -> 'Model'
```

Duplicate a model, optionally choose which fields to include, exclude and change.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| include | None | fields to include in new model | None |
| exclude | None | fields to exclude from new model, as with values this takes precedence over include | None |
| update | None | values to change/add in the new model. Note: the data is not validated before creating<br>the new model: you should trust this data | None |
| deep | None | set to `True` to make a deep copy of the model | None |

**Returns:**

| Type | Description |
|---|---|
| None | new model instance |

    
#### dict

```python3
def dict(
    self,
    *,
    include: Union[ForwardRef('AbstractSetIntStr'), ForwardRef('MappingIntStrAny'), NoneType] = None,
    exclude: Union[ForwardRef('AbstractSetIntStr'), ForwardRef('MappingIntStrAny'), NoneType] = None,
    by_alias: bool = False,
    skip_defaults: Union[bool, NoneType] = None,
    exclude_unset: bool = False,
    exclude_defaults: bool = False,
    exclude_none: bool = False
) -> 'DictStrAny'
```

Generate a dictionary representation of the model, optionally specifying which fields to include or exclude.

    
#### json

```python3
def json(
    self,
    *,
    include: Union[ForwardRef('AbstractSetIntStr'), ForwardRef('MappingIntStrAny'), NoneType] = None,
    exclude: Union[ForwardRef('AbstractSetIntStr'), ForwardRef('MappingIntStrAny'), NoneType] = None,
    by_alias: bool = False,
    skip_defaults: Union[bool, NoneType] = None,
    exclude_unset: bool = False,
    exclude_defaults: bool = False,
    exclude_none: bool = False,
    encoder: Union[Callable[[Any], Any], NoneType] = None,
    models_as_dict: bool = True,
    **dumps_kwargs: Any
) -> 'unicode'
```

Generate a JSON representation of the model, `include` and `exclude` arguments as per `dict()`.

`encoder` is an optional function to supply as `default` to json.dumps(), other arguments as per `json.dumps()`.