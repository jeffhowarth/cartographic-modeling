# __extract streams from dem__  

## Problem  

Please write a python script that uses whitebox tools to extract streams from a DEM. Please use the "dem_clipped_practice.tif" from the [vermont lidar tutorial][vcgi-lidar-cog]{target=_blank}.  

## Workflow  

<center>

``` mermaid
graph TD

  00((DEM)) ;
  01[BreachDepressionsLeastCost] ;
  02[Rho8Pointer] ;
  03[Rho8FlowAccumulation] ;
  04[ExtractStreams] ;
  05[StrahlerStreamOrder] ;
  06[RasterStreamsToVector] ;
  07((&#128526)) ;

  00 --> 01
  01 --> 02 
  02 --> 03  
  03 --> 04
  04 --> 05
  02 --> 05
  05 --> 06
  02 --> 06
  06 --> 07 


  style 00 fill:#C5E6A1,stroke-width:0px
  style 01 fill:#C5E6A1,stroke-width:0px
  style 02 fill:#C5E6A1,stroke-width:0px
  style 03 fill:#C5E6A1,stroke-width:0px
  style 04 fill:#C5E6A1,stroke-width:0px
  style 05 fill:#C5E6A1,stroke-width:0px
  style 06 fill:#E1C3E6,stroke-width:0px
  style 07 fill:#E6DEA100,stroke-width:0px


```

</center>

## Tour of outputs  

The video tours the output layers from this model in QGIS.  

<iframe width="720" height="405" src="https://www.youtube.com/embed/8lHMGAJ8RLs?si=gX8cLT8rUHuRxieo" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

[vcgi-lidar-cog]: ../q-methods/vermont-lidar.md  