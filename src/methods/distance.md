## Buffer features in collection by feet  

```js
// -------------------------------------------------------------
//  BUFFER FEATURES IN COLLECTION BY FEET.

//  INPUT is a feature collection. 
//  DISTANCE is a number in units feet.
//  OUTPUT is a single part feature collection of polygons.  
```

```js  
// -------------------------------------------------------------

var OUTPUT = INPUT.map(t.bufferFeet(DISTANCE));
```

---  

## Euclidean distance image    
```js
// -----------------------------------------------------------------------------
//  EUCLIDEAN DISTANCE
//
//  euc_distance output represents the euclidean distance to the nearest non-zero pixel of input.
//  Input must be image with 0 as background value.
// -----------------------------------------------------------------------------

var crs = "EPSG:32145";
var kr = 100;                   // Diameter of kernel, or zone to compute distance over. 

var euc_distance = input
  .distance(ee.Kernel.euclidean({radius: kr, units: 'meters'}))
  .reproject({crs: crs})                                         
  .rename('distance')
  ;

// Fun palette for distance images. 

var inferno = ["#000004", "#320A5A", "#781B6C", "#BB3654", "#EC6824", "#FBB41A", "#FCFFA4"].reverse();

// Add layer to map with fun palette. 

Map.addLayer(euc_distance,  {min:0, max: 100, palette: inferno}, "Euclidean distance image", false);

```


---  

[buffer-feet]: ../methods/distance.md#buffer-features-in-collection-by-feet  
[distance-euc]: ../methods/distance.md#euclidean-distance-image  