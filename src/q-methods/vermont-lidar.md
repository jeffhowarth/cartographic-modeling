## Introduction 

You can access lidar raster projects from VCGI one tile at a time through the [Vermont Lidar Finder][vlf]{target=_blank}. This will require a lot of clicks and post-processing (mosaic tiles).  

Recently, the folks at VCGI have developed a seamless cloud optimized geotiff (COG) product hosted that you can access through QGIS. These datasets support a much simpler workflow for accessing high resolution (70 cm) datasets that involves two steps:   

1. Add a COG to QGIS with a cloud protocol.
2. Extract data from a subregion.  

## Cloud protocols  

As of 3/30/2024, VCGI provides a hydro-flattened DEM and a DSM (from first returns) in the COG format.  

### DEMHF  

```
https://s3.us-east-2.amazonaws.com/vtopendata-prd/Elevation/STATEWIDE_2013-2017_70cm_DEMHF.tif
```

### DSM  

```
https://s3.us-east-2.amazonaws.com/vtopendata-prd/Elevation/STATEWIDE_2013-2017_70cm_DSM.tif
```

## Add COG to QGIS  

The first step involves adding the COG to QGIS with one of the cloud protocols defined above. 

---   

<iframe width="720" height="405" src="https://www.youtube.com/embed/dwylVCCqeO0?si=7WBxYUGaD8CLMmZw" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

---  

## Extract study region  

The second step involves extracting values from a subregion of the COG with a vector layer.  

---  

<iframe width="720" height="405" src="https://www.youtube.com/embed/ha6146r0mbw?si=sr_HI2FiobfF1KQm" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>  













[vlf]: https://maps.vcgi.vermont.gov/LidarFinder/