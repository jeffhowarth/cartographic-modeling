## feature collection to binary image  

```js
// -------------------------------------------------------------
//  CONVERT FEATURE COLLECTION TO BINARY IMAGE. 

//  INPUT must be a feature collection.
//  OUTPUT will be a binary raster.  
// -------------------------------------------------------------
```

```js

var output = t.fc2Binary(input);

// -------------------------------------------------------------



```

You can access the underlying code for this function in the [tasks module][tasks-module]{target=_blank}. 

---  

## mosaic image collection to image    

```js
// -------------------------------------------------------------
//  MOSAIC IMAGE COLLECTION   

//  INPUT must be an image collection with a 'quilt patch' structure.
//  OUTPUT will be a image with a 'quilted' structure.  
// -------------------------------------------------------------
```

```js

var output = input.mosaic();

// -------------------------------------------------------------
```

---  

## image to rgb   

```js
// -------------------------------------------------------------------------
//  IMAGE TO RGB  

//  INPUT is an image.
//  min, max, gamma, etc are should call viz parameters
//  OUTPUT is three band (RGB) image. 
// -------------------------------------------------------------------------
```

```js

var output_rgb = input.visualize({
  min: viz.min, 
  max: viz.max, 
  gamma: viz.gamma,
  forceRgbOutput: true
});

```

---   

[convert-fc-binary]: ../methods/convert-data-model.md#feature-collection-to-binary-image  

[mosaic-ic]: ../methods/convert-data-model.md#mosaic-image-collection-to-image   
[convert-image-rgb]: ../methods/convert-data-model.md#image-to-rgb  


[tasks-module]: https://code.earthengine.google.com/?accept_repo=users/jhowarth/public  