# __nominal workflows__  

It is good practice to self check your work by printing new outputs to console and adding new outputs as layers to the map. Try to get into the habit of pausing your progress after each step so that you can check if your output looks right before continuing.     

---

### Define study site  

```js
// -------------------------------------------------------------
//  DEFINE STUDY SITE. 
// -------------------------------------------------------------
```

1. [Load FC from address.][load-fc] --> data.cadastre.college 

--- 

### Make binary 

```js
// -------------------------------------------------------------
//  MAKE BINARY OF AG. 
// -------------------------------------------------------------
```

1. [Load FC from address.][load-fc] --> data.lc.ag
2. [Convert ag FC to binary image.][convert-fc-binary]    

---

### Generalize layer   

```js
// -------------------------------------------------------------
//  GENERALIZE LC LAYER.
// -------------------------------------------------------------
```

1. [Reclassify a nominal image.][local-reclass]  

---  

### Isolate subregion 

```js
// -------------------------------------------------------------
//  ISOLATE LC SUBREGION.
// -------------------------------------------------------------
```

1. [Intersect two binaries.][local-intersection]   

---  

### Specify new LC names  

```js
// -------------------------------------------------------------
//  SPECIFY NEW LC NAMES.
// -------------------------------------------------------------
```

1. [Multiply image by constant][local-multiply-constant]  
2. [Maximum at locations.][local-max] 

---

[load-data-module]: ../methods/load-modules.md#data-module 
[load-task-module]: ../methods/load-modules.md#tasks-module

[load-fc]: ../methods/load-data.md#feature-collection-from-address 
[load-ic]: ../methods/load-data.md#image-collection-from-address  
[load-i]: ../methods/load-data.md#image-from-address

[print-first]: ../methods/inspect-properties.md#print-first-feature-in-fc
[print-unique]: ../methods/inspect-properties.md#print-unique-values-in-fc  
[print-size]: ../methods/inspect-properties.md#print-size-of-collection


[filter-attribute]: ../methods/filter-data.md#by-attribute  
[filter-bounds]: ../methods/filter-data.md#by-bounds  

[convert-fc-binary]: ../methods/convert-data-model.md#feature-collection-to-binary  

[area-fc-acres]: ../methods/area.md#acres-of-each-feature-in-collection  
[area-fc-sq-km]: ../methods/area.md#sq-km-of-each-feature-in-collection      

[pixel-area]: ../methods/area.md#make-pixel-area-image    


[sum-table]: ../methods/aggregate-table.md#sum-the-values-in-a-table-column  
[dissolve-by-prop]: ../methods/aggregate-table.md#dissolve-features-in-collection-by-property  

[local-reclass]: ../methods/local-one-layer.md#reclassify-nominal-values 
[local-multiply-constant]: ../methods/local-one-layer.md#multiply-image-by-constant

[local-erase]: ../methods/local-two-layers.md#erase-values-at-locations-with-binary  
[local-intersection]: ../methods/local-two-layers.md#intersect-two-binaries
[local-max]: ../methods/local-two-layers.md#maximum-at-locations  

[zonal-sum]: ../methods/zonal-operations.md#zonal-summary-of-dough-within-cutters  