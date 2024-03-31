# __mama raster__  

## Overview  

In most (if not all) cases, Whitebox will panic if you try to compare two layers that do not align perfectly. As a result, for any local or zonal operation that requires two inputs, you will need to make sure that each input image has the same pixel resolution and the same extent (number of rows and columns). 

For this problem, I generally assign one image to serve as a __mama raster__, or a raster with a cell size and extent that will be inherited by all other rasters in the module. 

## Choosing a mama  

In general, your choice of which image to assign as mama should usually prioritize __down-sampling__ (reducing resolution) over up-sampling (increasing resolution).

| Cell Size | Extent    | Strategy  | 
| :---      | :---      | :---      |  
| Same      | Differ    | Either raster could serve as mama.    | 
| Differ    | Same      | Lower resolution should be mama.      | 
| Differ    | Differ    | Lower resolution should be mama.      |

In some cases, the two rasters will have the same resolution, but may have minor or major misalignments in the extent. Either raster could serve as the mama. 

In other cases, the two rasters will have different resolutions. It is often better to down-sample and assign the lower resolution raster as mama.  

## Operation  

In Whitebox, the __Resample__ tool can be used to change the resolution and extent of an image to match a mama image. The key is to use the __base__ parameter rather than the _scale_ parameter. This will assign both the cell size and the extent of the base raster to the output raster.  

Please note that the __method__ parameter is also very important. It should be "nn" for discrete data (nominal, ordinal, interval) and either "bilinear" or "cc" for continuous data (ratio).    

```py

# Align with mama.    

wbt.resample(
    inputs = input1, 
    output = output1, 
    cell_size=None, 
    base=mama, 
    method="nn",    # "nn" for discrete; "bilinear" or "cc" for continuous 
    # callback=default_callback
)

```