# __area problems__  

Please work through this problem set and then give your best shot at the challenge problem.  

Please note that for the first four problems, I provide links to workflows and answers that you may use to help guide and check your work. Your task is to write scripts that generate the answers.     

To get started, create a folder in your working repository named __area__.

---  

## __How much?__    

We can start with a basic question: how much area does a feature collection contain?  

For example:  

_How much land does Middlebury College own in Vermont?_    

We can answer this question with either a vector or raster solution.  

---  

### __Vector approach__      

Start a new script in your __area__ folder called __01_basic_vector.js__.

Insert a code snippet like this as a header:   

```js
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//  BASIC VECTOR SOLUTION
//  Example: How much land does Middlebury College own?

//  Last modified: insert date
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
```

Now write a script that computes the total acreage of parcels owned by the college (from data.cadastre.college).  

If you would like a template and answers to help you check your work, then [here is a workflow][area01].  

---  

### __Raster approach__        

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

Now write a script that computes the total acreage of parcels owned by the college (from data.cadastre.college) using a ZONAL operation with a raster input.  

If you would like a template and answers to help you check your work, then [here is workflow][area02].  

---  

### __Reflection__  

Please think about the following:  

1. Compare your answers from the two solutions: how close are they?  
2. How sensitive is the raster solution to your choice of scale?  

---  

## __Theme within regions__    

The first two solutions gave us how much area within each and all regions, where a feature collection represents a set of regions.   

The next problem looks to measure the amount of a theme _within_ a set of regions.  

The basic question is:  

_How much area of a particular theme occurs within a region or set of regions?_  

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

Now write a script that computes the total acreage of rare and significant natural communities (data.rarity.vt.nc) that occur within college-owned parcels (data.cadastre.college) that builds on the previous raster-based solution.  

If you would like a template and answers to help you check your work, then [here is a workflow][area03].  

---  

## __Theme within sites across regions__  

In the previous problems, we allowed the extent of a feature collection to define the extent of our analysis.  

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

Now build on the previous solutions and write a script that computes the total acreage of rare and significant natural communities (data.rarity.vt.nc) that occur within college-owned parcels (data.cadastre.college) in each town that contains college-owned parcels.  

If you would like a template and answers to help you check your work, then [here is a workflow][area04].  

---  

### __Reflection__  

Please think about these three questions:  

1. How many cutters do we have in this solution?  
2. How does the total area reported in this solution compare to previous?
3. Why might they differ?  

---  

### __Map__   

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

### __Chart__  

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

## __Challenge Problem__  

Your challenge problem is to report the amount of a THEME within SITES across REGIONS _and_ the amount of the THEME across REGIONS in a single chart like this:  

![Week 2 Challenge Problem](https://geography.middlebury.edu/howarth/cart_modeling/images/wk02_cp.png)

Start a new script in your __area__ folder called __05_theme_in_sites_across_regions_challenge.js__.

Insert a code snippet like this as a header:    

```js
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//  THEME IN SITES ACROSS REGIONS CHALLENGE

//  Compare total area of THEME to total area of SUBJECT. 

//  Last modified: insert date
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

```

You should be able to recycle the majority of your last solution. You just need to do a little surgery. 

Click [here][area05] if you would like some clues.  

No pressure. Please let me know if you have questions.  


---  

[area01]: ../workflows/area-workflows.md#vector-approach  
[area02]: ../workflows/area-workflows.md#raster-approach  
[area03]: ../workflows/area-workflows.md#theme-within-regions  
[area04]: ../workflows/area-workflows.md#theme-within-sites-across-regions    
[area05]: ../workflows/area-workflows.md#challenge-problem  
