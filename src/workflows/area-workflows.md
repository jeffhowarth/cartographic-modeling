# __area workflows__  

This page outlines workflows to solve the [area problems][area-problems] with earth engine methods defined on the [methods pages][ee-methods].  

---  

## __Vector approach__  

Here is a workflow to solve the [vector-based approach][area01] to the area problem.

### Load modules. 

1. [Load the data module.][load-data-module]  
2. [Load the tasks module.][load-task-module]

### Define a SUBJECT. 

1. [Load feature collection from address][load-fc] --> data.cadastre.college.fc_address 
2. [Print the number of objects in the collection.][print-size] --> Answer A below  

### Calculate area of each SUBJECT feature.  
    
1. [Area of features (acres) in FC.][area-fc-acres]

### Print results. 

1. [Print size of collection.][print-size] --> Answer B below
2. [Sum the values in a table column.][sum-table] --> Answer C below

<details closed>
<summary>Check your answers for vector solution.</summary>
<br>
(A) Number of parcels owned by the college: <b>286</b> 
<br>
(B) Number of objects in SUBJECT collection: <b>286</b> 
<br> 
(C) Total acres of college-owned parcels: <b>7009</b>  
</details>

---  

## __Raster approach__  

Work through the steps below to solve the [raster-based approach][area02] to the area problem.  

### Load modules.   

1. [Load the data module.][load-data-module]  
2. [Load the tasks module.][load-task-module]  

### Define CUTTERS.    
    
1. [Load feature collection from address][load-fc] --> data.cadastre.college.fc_address 
2. [Print size collection.][print-size] --> Answer A below  

### Define the DOUGH.    
    
1. [Make pixel area image.][pixel-area]   

### Compute Zonal Summary (zs).  
    
1. [Zonal summary of dough within cutters.][zonal-sum] 

### Print results.   
    
1. [Print size of collection.][print-size] --> Answer B below
2. [Sum the values in a table column (FC property).][sum-table] --> Answer C below

<details closed>
<summary>Check your answers for raster-based solution.</summary>
<br>
(A) Number of parcels owned by the college: <b>286</b> 
<br>
(B) Number of objects in zs collection: <b>286</b> 
<br> 
(C) Total acres of college-owned parcels: <b>7009</b>  
</details>

---  

## __Theme within regions__  

Work through the steps below to solve the [theme within regions][area03] area problem.  

### Load modules.   

1. [Load the data module.][load-data-module]  
2. [Load the tasks module.][load-task-module]  

### Define CUTTERS.    

1. [Load feature collection from address][load-fc] --> data.cadastre.college.fc_address 
2. [Print size collection.][print-size] --> Answer A below  

### Define binary THEME.  

1. [Load feature collection from address.][load-fc] --> data.rarity.vt.nc.fc_address 
2. Inspect the properties of the feature collection.
    1. [Print first feature in FC.][print-first]
    2. [Print unique values in FC.][print-unique]
        1. Explore 'S_RANK'.
        2. Explore 'S_NAME'.  
    3. [Convert FC to binary image.][convert-fc-binary] --> THEME as input

### Define the DOUGH.  

1. [Make pixel area image.][pixel-area]   
2. [Erase values at locations with binary.][erase-local] --> pixel area and theme binary 

### Compute Zonal Summary (zs).  

1. [Zonal summary of dough within cutters.][zonal-sum] 

### Print results.

1. [Print size of collection.][print-size] --> Answer B below
2. [Sum the values in a table column.][sum-table] --> Answer C below


<details closed>
<summary>Check your answers for THEME IN REGIONS raster solution.</summary>
<br>
(A) Number of parcels owned by the college: <b>286</b> 
<br>
(B) Number of objects in zs collection: <b>286</b> 
<br> 
(C) Total acres of rare natural communities on college-owned parcels: <b>1284</b>  
</details>  

---   

## __Theme within sites across regions__    

Work through the steps below to solve the [theme within sites across regions][area04] area problem.

### Load modules.

1. [Load the data module.][load-data-module]  
2. [Load the tasks module.][load-task-module]  

### Define SITES.

1. [Load feature collection from address][load-fc] --> data.cadastre.college.fc_address 
2. [Print size of collection.][print-size] --> Answer A below     
3. [Convert FC to binary image.][convert-fc-binary] --> Use SITES as input.

### Define REGIONS.

1. [Load feature collection from address][load-fc] --> data.gov.town.fc_address    
2. [Filter collection by bounds.][filter-bounds] --> towns that intersect college parcels
3. [Print the number of objects in the collection.][print-size] --> Answer ABbelow 

### Define THEME.

1. [Load feature collection from address.][load-fc] --> data.rarity.vt.nc.fc_address 
2. Inspect the properties of the feature collection.
    1. [Print first feature in FC.][print-first]
    2. [Print unique values in FC.][print-unique]
        1. Explore 'S_RANK'.
        2. Explore 'S_NAME'.  
3. [Convert FC to binary image.][convert-fc-binary] --> THEME as input  

### Define the DOUGH. 

1. [Make pixel area image.][pixel-area]   
2. [Erase values at locations with binary.][erase-local] --> pixel area and theme binary and sites binary

### Compute Zonal Summary (zs). 

1. [Zonal summary of dough within cutters.][zonal-sum] --> REGIONS as cutters!

### Print results.  

1. [Print size of collection.][print-size] --> Answer C below
2. [Sum the values in a table column.][sum-table] --> Answer D below  

<details closed>
<summary>Check your answers for THEME IN SITES ACROSS REGIONS raster solution.</summary>
<br>
(A) Number of parcels owned by the college: <b>286</b> 
<br>
(B) Number of towns that intersect college lands: <b>9</b> 
<br> 
(C) Number of REGIONS in the zs output: <b>9</b> 
<br> 
(D) Total acres of rare natural communities on college-owned parcels: <b>1301</b>  
</details>  

## __Challenge problem__    

Here are some clues to solve the [area challenge problem][area05].  

* Your dough will need two bands.
    1. One of pixel areas for locations that are THEME and SITE.
    2. Another of pixel areas for locations that are THEME.  

```js
var dough = dough_theme_sites.addBands(dough_theme);
```

* You will need to alter some parameters in the Chart to reflect that you are charting two series:  
    1. yProperties  
    2. .setSeriesNames  
    3. colors   

---   
[area-problems]: ../problems/area-problems.md  
[ee-methods]: ../methods/intro.md  

[area01]: ../problems/area-problems.md#vector-approach  
[area02]: ../problems/area-problems.md#raster-approach  
[area03]: ../problems/area-problems.md#theme-within-regions  
[area04]: ../problems/area-problems.md#theme-within-sites-across-regions  
[area05]: ../problems/area-problems.md#challenge-problem


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


[erase-local]: ../methods/local-two-layers.md#erase-values-at-locations-with-binary

[zonal-sum]: ../methods/zonal-operations.md#zonal-summary-of-dough-within-cutters  