# __viewshed comparison from dem and dsm__  

## Problem  

Please write a python script that uses Whitebox tools to compare visibility computed from a DEM and DSM for a single viewpoint. Please use the "dem_clipped_practice.tif" and "dsm_clipped_practice.tif files from the [vermont lidar tutorial][vcgi-lidar-cog]{target=_blank}. Please use the 'knoll.shp' file from the shared DATA/view-points folder. 

Please note that the two surface images (DEM and DSM) have a minor difference in extent which complicates the workflow. To understand why we need to do the Resample step in this problem, please refer to the [mama raster][mama-raster] page. 

## Workflow  

<center>

``` mermaid
graph TD
  01((DEM)) ;
  03[Viewshed] ;
  02((DSM)) ;
  04[Viewshed] ;
  05[Resample] ;
  06[Multiply] ;
  07[Add] ;
  08((&#128526)) ;

  01 --> 03
  02 --> 04 
  04 --> 05
  03 --> 05  
  05 --> 06
  03 --> 07
  06 --> 07
  07 --> 08 ;

  style 01 fill:#E6DEA1,stroke-width:0px
  style 02 fill:#E6DEA1,stroke-width:0px
  style 03 fill:#C5E6A1,stroke-width:0px
  style 04 fill:#C5E6A1,stroke-width:0px
  style 05 fill:#C5E6A1,stroke-width:0px
  style 06 fill:#C5E6A1,stroke-width:0px
  style 07 fill:#C5E6A1,stroke-width:0px
  style 08 fill:#E6DEA100,stroke-width:0px


```

</center>

## Tour of outputs  

This video tours the output layers from this model in QGIS. 

_Coming soon (need a quiet space to record)._

[vcgi-lidar-cog]: ../q-methods/vermont-lidar.md  
[mama-raster]: ../wb-methods/mama-raster.md  