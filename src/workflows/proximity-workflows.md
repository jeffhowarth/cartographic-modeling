# __proximity workflows__  

It is good practice to self check your work by printing new outputs to console and adding new outputs as layers to the map. Try to get into the habit of pausing your progress after each step so that you can check if your output looks right before continuing. 

## Load building footprint layer

1. [Load feature collection][load-fc] --> data.lc.buildings. 

## Buffer buildings to identify 50 meter zones of influence.   

1. Buffer each feature in a collection. 

## Create binary proximity zone

1. [Convert fc to binary image.][convert-fc-binary]


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