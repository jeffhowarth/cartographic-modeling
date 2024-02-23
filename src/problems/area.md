# __area problems__  

Please work through this problem set and then give you best shot at the challenge problem. I will post a form to the course calendar where you can submit links to your scripts.  

Please note that for the first four solutions, I provide the answers so that you can check your work.  

To get started, create a folder in your working repository named __area__.

---  

## __How much?__    

We can start with a basic question: how much area does a feature collection contain?  

For example:  

_How much land does Middlebury College own in Vermont?_    

We can answer this question with either a vector or raster solution.  

The solutions below all reference code blocks from the [ee methods](../methods/ee.md){target=_blank} page.

---  

### __Vector solution__      

Start a new script in your __area__ folder called __01_basic_vector.js__.

Insert a code snippet like this as a header:   

```js
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//  BASIC VECTOR SOLUTION
//  Example: How much land does Middlebury College own?

//  Last modified: insert date
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
```

Work through the steps below.  

1. Load the data module.
2. Load the tasks module.
3. Define a SUBJECT. 
    1. Load feature collection from address.
    2. Use the address for parcels owned by college (data.college.fc_address).  
    3. Inspect the properties of the feature collection.
        1. Print the number of objects in the collection. (A)  
4. Calculate area of each SUBJECT feature.  
    1. Area of features (acres) in FC. 
5. Print results:
    1. Print number of objects in the SUBJECT collection. (B)
    1. Summarize the total area of all features in the zs collection.
        1. Sum the values in a table column (FC property). (C)

<details closed>
<summary>Check your answers for vector solution.</summary>
<br>
(A) Number of parcels owned by the college: <b>286</b> 
<br> 
(B) Number of objects in the SUBJECT collection: <b>286</b> 
<br> 
(C) Total acres of college-owned parcels: <b>7009</b>  
</details>

---  

### __Raster solution__      

In earth engine, a raster solution employs a ZONAL operation.     

Start a new script in your __area__ folder called __02_basic_raster.js__.

Insert a code snippet like this as a header:    

```js
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//  BASIC RASTER SOLUTION
//  Example: How much land does Middlebury College own?

//  Last modified: insert date
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
```

Work through the steps below.  

1. Load the data module.
2. Define CUTTERS:  
    1. Load feature collection from address.
    2. Use the address for parcels owned by college (data.college.fc_address).  
    3. Inspect the properties of the feature collection.
        1. Print the number of objects in the collection. (A)  
3. Define the DOUGH:  
    1. Make pixel area image. 
4. Compute Zonal Summary (zs):  
    1. Zonal summary of dough within cutters. 
5. Print results:
    1. Print number of objects in the zs collection. (B)
    1. Summarize the total area of all features in the zs collection.
        1. Sum the values in a table column (FC property). (C)

<details closed>
<summary>Check your answers for raster solution.</summary>
<br>
(A) Number of parcels owned by the college: <b>286</b> 
<br>
(B) Number of objects in zs collection: <b>286</b> 
<br> 
(C) Total acres of college-owned parcels: <b>7009</b>  
</details>

---  

### __Reflection__  

Think about the following:  

1. Compare your answers from the two solutions: how close are they?  
2. How sensitive is the raster solution to your choice of scale?  

---  

## __Of a theme within regions?__    

The first two solutions gave us how much area within each and all regions, where a feature collection represents a set of regions.   

The next problem looks to measure the amount of a theme _within_ a set of regions.  

The basic question is: _how much area of a particular theme occurs within a region or set of regions?_  

For example:

_How many acres of rare or significant natural communities does the College own?_  

This type of problem can be easily solved with a raster overlay operation that builds on the basic solution solved previously.     

---  

### __Raster solution__  

Start a new script in your __area__ folder called __03_theme_in_regions.js__.

Insert a code snippet like this as a header:    

```js
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//  THEME IN REGIONS  
//  Example: How many acres of rare or significant natural 
//  communities does Middlebury College own?  

//  Last modified: insert date
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
```

Work through the steps below.  

1. Load the data module.
2. Load the task module.
3. Define CUTTERS:  
    1. Load feature collection from address.
    2. Use the address for parcels owned by college (data.college.fc_address).  
    3. Inspect the properties of the feature collection.
        1. Print the number of objects in the collection. (A)  
4. Define THEME:  
    1. Load feature collection from address.
    2. Use the address for rare natural communities (data.rarity.vt.nc.fc_address). 
    3. Inspect the properties of the feature collection.
        1. Print first feature in FC.
        2. Print unique values in FC.
            1. Explore 'S_RANK'.
            2. Explore 'S_NAME'.  
    4. Convert FC to binary image.
        1. Use THEME as input.
3. Define the DOUGH:  
    1. Make pixel area image. 
    2. Erase values at locations without a mask.  
        1. Multiply the pixel area image by the theme binary. 
4. Compute Zonal Summary (zs):  
    1. Zonal summary of dough within cutters. 
5. Print results:
    1. Print number of objects in the zs collection. (B)
    1. Summarize the total area of all features in the zs collection.
        1. Sum the values in a table column (FC property). (C)

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

## __Of a theme within sites across regions?__  

In the previous problems, we allowed the extent of a feature collection define the extent of our analysis.  

The next problem looks to make comparisons of THEMES in SITES across COMPARISON REGIONS.  

Perhaps you can suggest better terms to describe the general case for this after you work through the problem, but here is the concrete example:  

_How many acres of rare or significant natural communities does the College own in each town?_  

In this example, the THEME is rare or significant natural communities, the SITES are college parcels, and the REGIONS are towns in Vermont.  

This type of problem can again be easily solved with a raster overlay operation that builds on the previous solution.  

### __Raster solution__  

Start a new script in your __area__ folder called __04_theme_in_sites_across_regions.js__.

Insert a code snippet like this as a header:    

```js
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//  THEME IN SITES ACROSS REGIONS  
//  Example: How many acres of rare or significant natural 
//  communities does Middlebury College own in each town?  

//  Last modified: insert date
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
```

Work through the steps below.  

1. Load the data module.
2. Load the task module.
3. Define SITES:  
    1. Load feature collection from address.
    2. Use the address for parcels owned by college (data.college.fc_address).  
    3. Inspect the properties of the feature collection.
        1. Print the number of objects in the collection. (A)  
    4. Convert FC to binary image.
        1. Use SITES as input.
4. Define REGIONS. 
    1. Load feature collection from address.
    2. Use the address for parcels owned by college (data.gov.town.fc_address).  
    3. Filter collection by bounds.
        1. Filter for towns that intersect college parcels. 
    4. Inspect the properties of the feature collection.
        1. Print the number of objects in the collection. (B)  
4. Define THEME:  
    1. Load feature collection from address.
    2. Use the address for rare natural communities (data.rarity.vt.nc.fc_address). 
    3. Inspect the properties of the feature collection.
        1. Print first feature in FC.
        2. Print unique values in FC.
            1. Explore 'S_RANK'.
            2. Explore 'COMM_TYPE'.  
    4. Convert FC to binary image.
        1. Use THEME as input.
3. Define the DOUGH:  
    1. Make pixel area image. 
    2. Erase values at locations without a mask.  
        1. Multiply the pixel area image by the theme binary.
        2. Also multiply the pixel area image by the cutter binary.  
4. Compute Zonal Summary (zs):  
    1. Zonal summary of dough within cutters. 
        1. Use REGIONS as your cutters!
5. Print results:
    1. Print number of objects in the zs collection. (C)
    1. Summarize the total area of all features in the zs collection.
        1. Sum the values in a table column (FC property). (D)

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

---  

### __Reflection__  

Please think about these two questions:  

1. How many cutters do we have in this solution?  
2. How does the total area reported in this solution compare to previous?
3. Why might they differ?  

---  

### Map 

You can adapt this snippet to map the layers.

```js
// ------------------------------------------------------------------------------------------------------
//  MAP
// ------------------------------------------------------------------------------------------------------

var palettes = {
  cutters: '#78b3e0',
  theme: '#7A995C'
  }
;

Map.centerObject(regions, 10);
Map.setOptions('hybrid');

var regions_style = {color: '#ffffff', width: 6, fillColor: 'ffffff00'};

Map.addLayer(regions.style(regions_style), {}, "Regions");
Map.addLayer(sites, {color: palettes.cutters}, "Sites", true, 0.75);
Map.addLayer(theme, {color: palettes.theme}, "Theme");
```

---  

### Chart

You can adapt this script to chart your results.  

```js
// ------------------------------------------------------------------------------------------------------
//  Charts  
// ------------------------------------------------------------------------------------------------------

// Make a bar chart for the total acreage per town.

var chart = ui.Chart.feature.byFeature(
  {
    features: zs.sort("sum", false), 
    xProperty: 'TOWNNAME', 
    yProperties: ['sum']
  })
  .setSeriesNames(['Rare Nat Communities'])
  .setChartType('ColumnChart')
  .setOptions({
    title: 'Town Comparison',
    hAxis: {title: 'Town'},
    vAxis: {title: 'Acres'},
    colors: [palettes.theme]
  });

print(chart);

```

## Challenge Problem

The last problem reports the amount of area of a THEME within SITES across REGIONS. Can you modify this solution to make a chart that looks like this?

![Week 2 Challenge Problem](https://geography.middlebury.edu/howarth/cart_modeling/images/wk02_cp.png)

Start a new script in your __area__ folder called __05_theme_in_sites_across_regions_challenge.js__.

Insert a code snippet like this as a header:    

```js
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//  THEME IN SITES ACROSS REGIONS 

//  Challenge Problem 

//  Compare total area of THEME to total area of SUBJECT. 

//  Last modified: insert date
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
```

You should be able to recyle the majority of your last solution. You just need to do a little surgery. Here are some clues:  

* Your dough will need to bands.
    1. One of pixel areas with locations that are not THEME AND SITE erased.
    2. Another of pixel areas with locations that are not THEME erased.  

```js
var dough = dough_theme_sites.addBands(dough_theme);
```

* You will need to alter some parameters in the Chart to reflect that you are charting two series:  
    1. yProperties  
    2. .setSeriesNames  
    3. colors   


No pressure. Please let me know if you have questions.  