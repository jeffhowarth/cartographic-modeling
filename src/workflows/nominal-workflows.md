# __nominal workflows__

It is good practice to self check your work by printing new outputs to console and adding new outputs as layers to the map. Try to get into the habit of pausing your progress after each step so that you can check if your output looks right before continuing.     

## __Define study site__  

1. [Load FC from address.][load-fc] --> data.cadastre.college 

### Make ag binary. 

1. [Load FC from address.][load-fc] --> data.lc.ag
2. [Convert ag FC to binary image.][convert-fc-binary]    

### Generalize base layer to make grass/shrub/bare binary  

1. Reclassify a nominal image.  

### Isolate ag land in grass/shrub/bare lands to bring into land cover. 

1. Intersect two binaries. 

### Classify grass/shrub/bare lands that are agricultural.  

1. Output max values of locations. 

---

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


[sum-table]: ../methods/aggregate-table.md#sum-the-values-in-a-table-column  
[dissolve-by-prop]: ../methods/aggregate-table.md#dissolve-features-in-collection-by-property  


[erase-local]: ../methods/local-operations.md#erase-values-at-locations-with-binary  

[zonal-sum]: ../methods/zonal-operations.md#zonal-summary-of-dough-within-cutters  