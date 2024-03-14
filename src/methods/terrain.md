## make hillshade from collection

```js
// -------------------------------------------------------------
//  MAKE HILLSHADE FROM COLLECTION
//  
//  DEM_IC is a collection of DEM images.
//  AZIMUTH is the position of the sun on the horizon; should be 315 +/- 45.
//  ZENITH is the vertical position of the sun (above the horizon).
//  Z-factor is exaggeration factor; >1 increases contrast.
// -------------------------------------------------------------
```

```js
var z = 1.2;            // Adjust based on terrain characteristics. 

// Make hillshades from collection. 

var hs = dem_ic
  .map(t.hsCollection(320, 35, z))             // Adjust for your terrain.
  .mosaic()                                    
  .rename('hillshade')
;
```

You can access the underlying code for this function in the [tasks module][tasks-module]{target=_blank}. 

---  

## calculate slope as percent from collection  

```js
// -------------------------------------------------------------
//  CALCULATE SLOPE AS PERCENT FROM COLLECTION  
//  
//  INPUT is a collection of DEM images.  
//  OUTPUT is a an image where each pixel reports slope as percent.
// -------------------------------------------------------------
```

```js
var output = input.map(t.percentSlopeCollection)
  .mosaic()
;
```

You can access the underlying code for this function in the [tasks module][tasks-module]{target=_blank}. 

---

## classify slope with usda criteria  

```js
// -------------------------------------------------------------
//  CLASSIFY SLOPE WITH USDA CRITERIA  
//  
//  INPUT is a slope image in units PERCENT.  
//  OUTPUT is a dictionary with four keys:
//    i: nominal image based on USDA slope classes,
//    layer_name: 'USDA slope classification'  
//    class_names: names of each class,
//    viz: viz parameters for the image.  
// -------------------------------------------------------------
```

```js
var output = t.classSlopeUSDA(input);
```  

You can access the underlying code for this function in the [tasks module][tasks-module]{target=_blank}. 

---  


[tasks-module]: https://code.earthengine.google.com/?accept_repo=users/jhowarth/public 

[terrain-hs-ic]: ../methods/terrain.md#make-hillshade-from-collection
[terrain-percent-slope-ic]: ../methods/terrain.md#calculate-slope-as-percent-from-collection
[terrain-usda-class]: ../methods/terrain.md#classify-slope-with-usda-criteria