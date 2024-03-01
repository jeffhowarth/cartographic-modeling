# __nominal problems__

## __The case of Vermont's Land Cover dataset__ 

[Statewide High-Resolution Land Cover Dataset](https://vcgi.vermont.gov/data-release/statewide-high-resolution-vermont-land-cover-data-now-available){target=_blank}  

[Hosted by Awesome Community Dataset](https://github.com/samapriya/awesome-gee-community-datasets){target=_blank}  

### __Problem__   

Improve base layer to:  

1. Distinguish agricultural lands from grass/shrub and bare classes;  
2. Distinguish tree canopy, grass/shrub of yards and human landscaping from places with greater potential for natural communities.  

### __Goal__  





## Get started  

1. Add a header.  
2. Load data and task modules.  
3. Load study site (college lands).
4. Set up map.  

## Ag problem  

### Load land cover base layer  

1. Initialize lc variable.
2. Print to console. 
3. Add base layer to map.  

### Make grassland binary. 

1. Load agricultural layer. 
2. Add layer to map (to inspect).  
3. Convert ag FC to binary image.  
4. Add binary layer to map.  

### Generalize base layer to make grass/shrub/bare binary  

1. Reclassify land cover base to binary.  
2. Add layer to map (to inspect).

### Isolate ag land in grass/shrub/bare lands to bring into land cover. 

1. Intersect two binaries. 
2. Add layer to map.  

### Classify grass/shrub/bare lands that are agricultural.  

1. Add agricultural class to base image. 
2. Create new viz dictionary for layer. 
3. Create new class list for layer. 
4. Add layer to map.  

## Proximity problem  

### Load building footprint layer

1. Load building feature collection. 
2. Add layer to map.  

### Buffer buildings by influence zone.   

1. Write a function to buffer each building by 50 meters. 
2. Apply function to feature collection. 
3. Add layer to map.   
4. Convert building influence to binary. 
5. Add layer to map. 

### Add building influence to lc with ag cimage. 

1. Incorporate the binary image in the lc with ag image.
2. Create new viz dictionary for layer. 
3. Create new class list for layer.
6. Add layer to map  
