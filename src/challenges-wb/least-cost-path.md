# __least cost path practice__  

## Problem  

Please write a python script that uses whitebox tools to find the least cost path from BiHall to the Knoll. 

Please use the base_land_cover.tif from the [GEE export example][eex] for the land cover input. And use the "od_lcp_practice.tif" on the shared [DATA/od/][od]{target=_blank} directory for the origin-destination input.  

You will need to derive the friction values for the land cover reclass on your own. Try to assign values so that the least cost path that results resembles the one that you would take if you were to walk from the back of BiHall to the Knoll. Please know that all pixels must have some cost that accumulates (so make the lowest friction 1 rather than 0). Also remember that the whitebox reclass operation requires a string of "new value;old value" pairs. So you will need to adapt the string below by replacing the 'x#' with a cost associated with the following land cover class:  

```
"x1;1;x2;2;x3;3;x4;4;x5;5;x6;6;x7;7;x8;8"
```

## Workflow  

<center>

``` mermaid
graph TD

  00((origin-destination)) ;
  01[EqualTo] ;
  02[EqualTo] ;
  03((land-cover)) ;
  04[Reclass] ;
  05[CostDistance] ;
  06[CostPathway] ;
  07((&#128526)) ;

  00 --> 01 ;
  00 --> 02 ;
  03 --> 04 ;
  01 --> 05 ;
  04 --> 05 ;
  02 --> 06 ;
  05 --> 06 ;
  06 --> 07 ; 


  style 00 fill:#C5E6A1,stroke-width:0px
  style 01 fill:#C5E6A1,stroke-width:0px
  style 02 fill:#C5E6A1,stroke-width:0px
  style 03 fill:#C5E6A1,stroke-width:0px
  style 04 fill:#C5E6A1,stroke-width:0px
  style 05 fill:#C5E6A1,stroke-width:0px
  style 06 fill:#C5E6A1,stroke-width:0px
  style 07 fill:#E6DEA100,stroke-width:0px


```

</center>

## Tour of outputs  

The video tours the output layers from this model in QGIS.  

_forthcoming_  

---  

[eex]: ../methods/export.md#export-nominal-raster
[od]: https://drive.google.com/drive/folders/14cNeBnCgU2Huk18968AdDdLNGh6hZQIm?usp=drive_link  
