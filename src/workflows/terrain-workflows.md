# __terrain workflows__    

It is good practice to self check your work by printing new outputs to the console panel and adding new outputs as layers to the map panel. The workflow below does not prompt you to do this; you should be in the habit of doing this automatically. Please reference the [inspect properties][inspect-properties]{target=_blank} and [map layer][map-layer]{target_blank} methods as needed.

---  

## __SHADED RELIEF__  

## Define study region  

```js
// -------------------------------------------------------------
//  DEFINE STUDY REGION
//
//  Make two versions of your study region: 
//  1. a feature collection
//  2. a binary image
//
//  Then set up your map:
//  1. center on study region at zoom 13
//  2. change base map to hybrid
// -------------------------------------------------------------
```

1. [Load feature collection from address][load-fc] --> data.gov.town
2. [Filter by attribute][filter-attribute] --> 'MIDDLEBURY'
3. [Feature collection to binary image][convert-fc-binary]    

---  

## Load elevation data   

```js
// -------------------------------------------------------------
//  LOAD ELEVATION DATA: 3DEP 1m DEM
// -------------------------------------------------------------
```

1. [Load image collection from address][load-ic] --> 'USGS/3DEP/1m'  
2. [Filter by bounds][filter-bounds] --> study_region  
3. [Select image band][select-band] --> 'elevation'

---   

## Convert image collection to image

```js
// -------------------------------------------------------------
//  CONVERT IMAGE COLLECTION INTO AN IMAGE
//
//  Mosaic dem and mask by study region.
// -------------------------------------------------------------
```

1. [Mosaic image collection to image][mosaic-ic]  
2. [Mask values at locations][local-mask] --> study_region_binary  

---  

## Define viz for image  

```js
// -------------------------------------------------------------
//  DEFINE VIZ FOR DEM 
// ------------------------------------------------------------- 
```

1. [Print min and max of image][print-min-max]  
2. Define viz parameters --> use min and max that were printed to console  

---

## Make hillshade layer

```js
// -------------------------------------------------------------
//  MAKE HILLSHADE LAYER  
// ------------------------------------------------------------- 
```

1. [Make hillshade from collection][terrain-hs-ic]  
2. [Viz with gamma to influence midtones][viz-gamma]  

---  

## Add shading from another hillshade with a different azimuth  

```js
// ------------------------------------------------------------- 
//  ADD SHADING FROM ANOTHER HILLSHADE WITH A DIFFERENT AZIMUTH 
// ------------------------------------------------------------- 
```

1. [Make hillshade from collection][terrain-hs-ic] 
2. [Minimum at locations][local-min]  

---  

## Convert to feet  

```js
// ------------------------------------------------------------- 
//  CONVERT TO FEET
// ------------------------------------------------------------- 
```

1. [Mask values at locations][local-mask] --> study_region_binary  
2. [Multiply image by constant][local-multiply-constant] --> 3.28084  
3. [Print min and max of image][print-min-max]    

---  

## Classify hypsography 

```js
// ------------------------------------------------------------- 
//  CLASSIFY HYPSOGRAPHY
// ------------------------------------------------------------- 
```

1. [Classify image by equal intervals][local-classify-intervals] --> 100  
2. [Print min and max of image][print-min-max]  

```js
var hypso_palette = ['#bfd3b5', '#cbdabf', '#e2e0c3', '#efdeba', '#edd2a3', '#eaca91', '#e6c084', '#dbad70', '#ce975b', '#c68d51'];
```

---  

## Blend hypsometric tint with shaded relief  

```js
// -------------------------------------------------------------------------
//  Blend hypsometric tint with shaded relief  
// -------------------------------------------------------------------------
```

1. [Convert image to rgb][convert-image-rgb] --> hillshade  
2. [Convert image to rgb][convert-image-rgb] --> hypso  
3. [Blend two images][viz-blend]      

---  

## __SLOPE CLASS__  

---  

[map-layer]: ../methods/map-layers.md  
[inspect-properties]: ../methods/inspect-properties.md

[load-fc]: ../methods/load-data.md#feature-collection-from-address 
[load-ic]: ../methods/load-data.md#image-collection-from-address  
[load-i]: ../methods/load-data.md#image-from-address


[filter-attribute]: ../methods/filter-data.md#by-attribute  
[filter-bounds]: ../methods/filter-data.md#by-bounds  
[select-band]: ../methods/filter-data.md#select-image-band

[convert-fc-binary]: ../methods/convert-data-model.md#feature-collection-to-binary  
[mosaic-ic]: ../methods/convert-data-model.md#mosaic-image-collection-to-image  
[convert-image-rgb]: ../methods/convert-data-model.md#image-to-rgb  

[print-min-max]: ../methods/image-viz.md#print-min-max-of-an-image  

[area-fc-acres]: ../methods/area.md#acres-of-each-feature-in-collection  
[area-fc-sq-km]: ../methods/area.md#sq-km-of-each-feature-in-collection      

[pixel-area]: ../methods/area.md#make-pixel-area-image    

[buffer-feet]: ../methods/distance.md#buffer-features-in-collection-by-feet  

[terrain-hs-ic]: ../methods/terrain.md#make-hillshade-from-collection

[sum-table]: ../methods/aggregate-table.md#sum-the-values-in-a-table-column  
[dissolve-by-prop]: ../methods/aggregate-table.md#dissolve-features-in-collection-by-property  


[local-mask]: ../methods/local-two-layers.md#mask-values-at-locations  
[local-min]: ../methods/local-two-layers.md#minimum-at-locations
[local-multiply-constant]: ../methods/local-one-layer.md#multiply-image-by-constant  
[local-classify-intervals]: ../methods/local-one-layer.md#classify-image-by-equal-interval  

[zonal-sum]: ../methods/zonal-operations.md#zonal-summary-of-dough-within-cutters  

[viz-gamma]: ../methods/image-viz.md#viz-with-gamma-to-influence-midtones  
[viz-blend]: ../methods/image-viz.md#blend-two-images  