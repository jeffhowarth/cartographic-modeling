# __earth engine methods__  

This is a collection of recurring tasks for cartographic modeling with the javascript code editor for Google Earth Engine. In many cases, the snippets below use data and tools that are shared via my public earth engine repo. Click [__here__][myRepo]{target=_blank} to add the repository to the "Reader" section in your instance of Code Editor. This will allow you to see the underlying code.  

## __Load modules__    

### Data module 
```js
// -------------------------------------------------------------
//  LOAD DATA MODULE. 
// -------------------------------------------------------------

var data = require('users/jhowarth/public:modules/data.js');       
print('DATA', data);
```

### Tasks module    

```js
// -------------------------------------------------------------
//  LOAD TASKS MODULE. 
// -------------------------------------------------------------

var t = require('users/jhowarth/public:modules/tasks.js');

```

### Layout module  

```js
// -------------------------------------------------------------
//  LOAD LAYOUT MODULE. 
// -------------------------------------------------------------

var layout = require('users/jhowarth/public:modules/layout.js').layout;
print('LAYOUT', layout);

```

--- 

## __Load data__      

### Load FC from address  
 
```js
// -------------------------------------------------------------
//  LOAD FEATURE COLLECTION FROM ADDRESS. 

//  Replace LAYER with a key from the data repo;
//  or replace argument with EE address string. 

// -------------------------------------------------------------

var output = ee.FeatureCollection(data.LAYER.fc_address);

```

---  

### Load IC from address  
 
```js
// -------------------------------------------------------------
//  LOAD IMAGE COLLECTION FROM ADDRESS. 

//  Replace LAYER with a key from the data repo;
//  or replace argument with EE address string.  
// -------------------------------------------------------------

var output = ee.ImageCollection(data.LAYER.fc_address);

```

---  

## __Inspect properties__    

### Print first feature in FC  

```js
// -------------------------------------------------------------
//  PRINT FIRST FEATURE IN COLLECTION.  

//  Replace 'LABEL' with appropriate header.  
//  Replace fc with appropriate variable.
// -------------------------------------------------------------

print(
    "LABEL",
    fc.first()
    )
;
```

### Print unique values in FC  

```js
// -------------------------------------------------------------
//  PRINT UNIQUE VALUES OF FEATURE PROPERTY IN COLLECTION. 

//  Replace 'LABEL' with appropriate header.  
//  Replace fc with appropriate variable.
// -------------------------------------------------------------

print(
    "LABEL",
    fc.aggregate_array().distinct().sort()
    )
;
```

---  

## __Filter a collection__  

### Filter collection by attribute  

```js
// -------------------------------------------------------------
//  FILTER COLLECTION BY ATTRIBUTE. 

//  Input must be a collection.
//  Output is a collection, where each object in collection satisfies criterion.

//  Set CRITERION (see options in ee.Filter docs).
//  Set "property_name".
//  Set "value".
// -------------------------------------------------------------

var output = input
    .filter(ee.Filter.CRITERION("property_name", "value"))
;
```

### Filter collection by bounds  

```js
// -------------------------------------------------------------
//  FILTER COLLECTION BY ATTRIBUTE. 

//  Input must be a feature collection.
//  BOUNDS may be a point, line, or polygon geometry, feature, or feature collection.
//  Output is a collection, where each object intersects.


// -------------------------------------------------------------

var output = input
    .filterBounds(BOUNDS)
;
```

---  

## __Measure spatial properties in a collection__  

### Area of features (acres) in FC 

```js
// -------------------------------------------------------------
//  CALCULATE AREA (ACRES) OF FEATURES IN COLLECTION. 
// -------------------------------------------------------------

//  This CRS is good for Vermont. Replace if you work elsewhere.

var crs = "EPSG 31245";

//  Input must be a feature collection.
//  Output is a feature collection.
//  Each output feature has new property 'acres' that holds the area of feature.
//  Replace 'acres' with something else to define an alternative property name. 
//  Remember to following naming rules for properties.   

var output = input
  .map(t.howManyAcres(crs, 'acres'))
;
```

### Area of features (sq km) in FC 

```js
// -------------------------------------------------------------
//  CALCULATE AREA (SQUARE KM) OF FEATURES IN COLLECTION. 
// -------------------------------------------------------------

//  This CRS is good for Vermont. Replace if you work elsewhere.

var crs = "EPSG 31245";

//  Input must be a feature collection.
//  Output is a feature collection.
//  Each output feature has new property 'sq_km' that holds the area of feature.
//  Replace 'sq_km' with something else to define an alternative property name.  
//  Remember to following naming rules for properties (no spaces).

var output = input
  .map(t.howManyAcres(crs, 'sq_km'))
;
```

---  

## __Aggregate features in a collection__  

### Dissolve features in collection by property  

```js
// -------------------------------------------------------------
//  DISSOLVE FEATURES IN COLLECTION BY PROPERTY. 

//  Input must be a feature collection.
//  Replace 'PROPERTY' with the property name to dissolve features.  
//  Output is a feature collection (with singlepart and multipart features),
//  where each feature represents the region of a unique property value.  
// -------------------------------------------------------------


var output = t.dissolveByProperty(input, 'PROPERTY')
```

## __NAIP imagery__  

### Tag NAIP collection with date and number of bands

```js
// -------------------------------------------------------------
//  Tag filtered collection with date and number of bands. 

//  Collection must be a NAIP image collection.
// -------------------------------------------------------------

output = t.tagDateAndBands(collection)
;
```

---  

### Make mosaic image from image collection    

```js
// -------------------------------------------------------------
//  Make mosaic image from image collection
// -------------------------------------------------------------

var output = t.makeMosaic(collection, year, region);

```

---  

## __Image visualization__  

### Make a histogram to see data distribution

```js
// Make a viz dictionary.

var input_viz = {
  min: [0,0,0],                       // List of min in same order as band list.
  max: [255,255,255],                 // List of max in same order as band list.
  bands: ['R', 'G', 'B']              // In this example, R is index 0, G is index 1, and B is index 2.
};

// Make a histogram to see data distribution.  

var b = 0;                            // This targets a band number by the list index. 0 will target R.
var i = INPUT;                        // This targets an image. Replace IMAGE with image variable.
var v = input_viz;                    // This targets the viz parameters for the image.

var histogram = t.makeHistogram(
  i,                                  // Must be an image (not an image collection).
  v.bands[b],                         // Select one band at a time.
  3,                                  // Pixel resolution of image.
  v.min[b],                           // Minimum value of x-axis
  v.max[b]                            // Maximum value of x-axis.
  )
;

// Print, print, print...

print(
  "HISTOGRAM", 
  histogram
  )
;
```



[myRepo]: https://code.earthengine.google.com/?accept_repo=users/jhowarth/public