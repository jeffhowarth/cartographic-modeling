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

---  

You can access the underlying code for this function in the [tasks module][tasks-module]{target=_blank}. 


---  


[tasks-module]: https://code.earthengine.google.com/?accept_repo=users/jhowarth/public 

[terrain-hs-ic]: ../methods/terrain.md#make-hillshade-from-collection