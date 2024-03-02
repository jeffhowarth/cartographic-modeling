## viz for raster 

```js
// -------------------------------------------------------------
//  VIZ PARAMETERS FOR RASTER DATA

//  Replace VIZ with custom name.
//  Adjust BAND_NAME to define band or list of bands to display. 
//  Adjust min value to minimum value displayed with color.
//  Adjust max value to maximum value displayed with color.
//  Adjust gamma to brighten or darken midtones.
//  Min, max, gamma can be custom for each band from list order.

```
```js
// -------------------------------------------------------------

var VIZ = 
    {
        bands: ['BAND_NAME'],
        min: [0],
        max: [255],
        gamma: [1]
    }
;

// -------------------------------------------------------------

```

---   

## simple viz for vector 

```js
// -------------------------------------------------------------
//  SIMPLE VIZ PARAMETERS FOR VECTOR DATA

//  Replace VIZ with custom name.
//  Adjust COLOR with HTML color name or hex code.

//  RESOURCE: https://htmlcolorcodes.com/color-names/

```
```js
// -------------------------------------------------------------

var VIZ = 
    {
        color: 'Orchid'
    }
;

// -------------------------------------------------------------

```

---   

## add layer

```js
// -------------------------------------------------------------
//  ADD LAYER TO MAP

//  Replace DATA with name of collection, image, geometry.
//  Replace VIZ with parameters for vector or raster data.  
//  Replace LAYER_NAME with name as a string.
//  Change FALSE to true to show by default.
//  Change 1 to decimal between 0 and 1 to adjust opacity.
```
```js
// -------------------------------------------------------------

Map.addLayer(
    DATA,
    VIZ,
    LAYER_NAME,
    false,
    1
)

// -------------------------------------------------------------

```

---

## casing and fill viz for vector 

```js
// -------------------------------------------------------------
//  CASING AND FILL VIZ FOR VECTOR DATA

//  This allows you to control display of both casing and fill.
//  OUTPUT is a single-band image. 

//  STEP 1: DEFINE VIZ PARAMETERS

//  Replace VIZ with custom name.
//  Casing color --> Adjust HTML color name or hex code.
//  Casing size --> Adjust WEIGHT.
//  Fill color --> Adjust HTML hex code; last two characters control opacity. 

//  STEP 2: STYLE VECTOR WITH VIZ PARAMETERS

//  INPUT is vector data to display.
//  VIZ is style parameters.
//  OUTPUT is image data with styled casing and fill.

//  STEP 3: ADD STYLED DATA TO MAP.

//  OUTPUT is from step 2. 
//  Viz parameter slot must be {} placeholder.
//  Adjust 'LAYER NAME'. 
//  Adjust boolean show argument.   

//  RESOURCES: 

//  https://htmlcolorcodes.com/color-names/
//  https://gist.github.com/lopspower/03fb1cc0ac9f32ef38f4
//  


```
```js
// -------------------------------------------------------------

var VIZ = 
    {
        color: '#DA70D6'
        weight: 2 
        fillColor: '#DA70D600'
    }
;

var OUTPUT = INPUT.style(VIZ);

Map.addLayer(OUTPUT, {}, "LAYER NAME", false);

// -------------------------------------------------------------

```

[viz-raster]: ../methods/map-layers.md#viz-for-raster
[simple-viz-vector]: ../methods/map-layers.md#simple-viz-for-vector  
[add-layer]: ../methods/map-layers.md#add-layer  
[case-fill]: ../methods/map-layers.md#casing-and-fill-viz-for-vector  