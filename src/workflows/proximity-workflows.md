# __proximity workflows__  

It is good practice to self check your work by printing new outputs to the console panel and adding new outputs as layers to the map panel. The workflow below does not prompt you to do this; you should be in the habit of doing this automatically. Please reference the [inspect properties][inspect-properties]{target=_blank} and [map layer][map-layer]{target_blank} methods as needed.

---  

## Define college lands study sites.

```js
// -------------------------------------------------------------
//  1. DEFINE STUDY SITE. 
// -------------------------------------------------------------
```

1. [Load feature collection][load-fc] --> data.cadastre.college 
2. Set up your map to center on study site and show hybrid base layer. 

---  

## Load building roofprints on college lands.

```js
// -------------------------------------------------------------
//  2. LOAD BUILDING ROOFPRINTS ON COLLEGE LANDS. 
// -------------------------------------------------------------
```

1. [Load feature collection][load-fc] --> data.lc.buildings 
2. [Filter collection by region][filter-bounds] --> buildings on college parcels.

---  

## Map 100 foot zones of influence for each building on college lands.   

```js
// -------------------------------------------------------------
//  3. MAP 100 FT ZOI FOR EACH BUILDING ON COLLEGE LANDS.  
// -------------------------------------------------------------
```

1. [Buffer each feature in a collection.][buffer-feet]   

---  

## Map binary proximity zone

```js
// -------------------------------------------------------------
//  4. MAP BINARY PROXIMITY ZONE.  
// -------------------------------------------------------------
```

1. [Convert fc to binary image.][convert-fc-binary]

---  

## Challenge Problems   

1. Could you solve step 3 with a raster solution (where you do not use the f.buffer method to map proximity)?
2. Could you solve step 4 with a vector solution (what you do not convert fc to binary image)?  

---  

## Reflections  

1. What are pros and cons of vector solution to define proximity zones compared to raster solution?    
2. What are pros and cons of raster solution to make binary image versus the vector solution of dissolving features?    

---  

[map-layer]: ../methods/map-layers.md  
[inspect-properties]: ../methods/inspect-properties.md

[load-data-module]: ../methods/load-modules.md#data-module 
[load-task-module]: ../methods/load-modules.md#tasks-module

[load-fc]: ../methods/load-data.md#feature-collection-from-address 
[load-ic]: ../methods/load-data.md#image-collection-from-address  
[load-i]: ../methods/load-data.md#image-from-address

[print-first]: ../methods/inspect-properties.md#print-first-feature-in-fc
[print-unique]: ../methods/inspect-properties.md#print-unique-values-in-fc  
[print-size]: ../methods/inspect-properties.md#print-size-of-collection


[filter-collection]: ../methods/filter-collection.md#by-attribute  
[filter-bounds]: ../methods/filter-collection.md#by-bounds  

[convert-fc-binary]: ../methods/convert-data-model.md#feature-collection-to-binary  

[area-fc-acres]: ../methods/area.md#acres-of-each-feature-in-collection  
[area-fc-sq-km]: ../methods/area.md#sq-km-of-each-feature-in-collection      

[pixel-area]: ../methods/area.md#make-pixel-area-image    

[buffer-feet]: ../methods/distance.md#buffer-features-in-collection-by-feet  


[sum-table]: ../methods/aggregate-table.md#sum-the-values-in-a-table-column  
[dissolve-by-prop]: ../methods/aggregate-table.md#dissolve-features-in-collection-by-property  


[erase-local]: ../methods/local-operations.md#erase-values-at-locations-with-binary  

[zonal-sum]: ../methods/zonal-operations.md#zonal-summary-of-dough-within-cutters  