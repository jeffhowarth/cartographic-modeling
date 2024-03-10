# __terrain problems__  

## __Introduction__  

Terrain problems concern how to represent the _earth's surface_ and the age-old problem of how to represent a third spatial dimension on a flat visual plane. 

Two classic terrain problems involve:  

1. creating the illusion of a third dimension through shading from an illumination source, often called _shaded relief_;

2. classifying the degree of change in a surface as illustrated by a _slope map_.    

## __SHADED RELIEF__         

Use the [USGS 3DEP 1m National Map](https://developers.google.com/earth-engine/datasets/catalog/USGS_3DEP_1m){target=_blank} hosted by Google to make a hyposmetric shaded relief map (as shown below).

<iframe src=https://ee-edu-apps.projects.earthengine.app/view/gg0352-shaded-relief title="Shaded Relief example" height=720 width=720 allowfullscreen= true></iframe> 

Start a new script called __wk04_01_shaded_relief.js__.

Insert a header, then load the data and task modules.   

```js
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//  SHADED RELIEF  

//  Make a blended hypsometric shaded relief.  

//  Last modified: insert date
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

var data = require('users/jhowarth/public:modules/data.js');       
print('DATA', data);

var t = require('users/jhowarth/public:modules/tasks.js');

```

Now write a script that produces the layers shown in the app above.    

If you would like a template, then [here is a workflow][terrain01].

---  

## __CLASSIFIED SLOPE MAP__  

Use the [USGS 3DEP 1m National Map](https://developers.google.com/earth-engine/datasets/catalog/USGS_3DEP_1m){target=_blank} hosted by Google to make a slope map with classes defined by the [USDA][usda]{target=_blank}.  

<iframe src=https://ee-edu-apps.projects.earthengine.app/view/gg0352-slope-class title="Shaded Relief example" height=720 width=720 allowfullscreen= true></iframe>

Start a new script called __wk04_02_slope_class.js__.

Insert a header, then load the data and task modules.   

```js
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//  CLASSIFIED SLOPE MAP

//  Make a slope map with classes defined by USDA.  

//  Last modified: insert date
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

var data = require('users/jhowarth/public:modules/data.js');       
print('DATA', data);

var t = require('users/jhowarth/public:modules/tasks.js');

```

Now write a script that produces the layers shown in the app above.  

If you would like a template, then [here is a workflow][terrain02].

[usda]: https://www.nrcs.usda.gov/sites/default/files/2022-10/Basic_Soils_AK_Curriculm%20-%20UPDATED.pdf

[terrain01]: ../workflows/terrain-workflows.md#shaded-relief  
[terrain02]: ../workflows/terrain-workflows.md#classified-slope-map       



