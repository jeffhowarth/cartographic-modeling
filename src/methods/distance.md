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

[buffer-feet]: ../methods/distance.md#buffer-features-in-collection-by-feet  