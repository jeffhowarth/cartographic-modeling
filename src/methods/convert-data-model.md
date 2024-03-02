### feature collection to binary image.  

```js
// -------------------------------------------------------------
//  CONVERT FEATURE COLLECTION TO BINARY IMAGE. 

//  INPUT must be a feature collection. 
//  BINARY will be an image with a single band named 'THEME'.
//  Alter THEME to give the band a custom name.  
//  Follow naming conventions for bands (no spaces). 
```

```js
// -------------------------------------------------------------

var binary = input
  .map(function(f){return f.set('tag', 1)})
  .reduceToImage(
    {
      properties: ['tag'], 
      reducer: ee.Reducer.max()
    }
  )
  .unmask()
  .rename(['THEME'])
;

print(
  "BINARY",
  binary
  )
;
```

---  

[convert-fc-binary]: ../methods/convert-data-model.md#convert-fc-to-binary-image  