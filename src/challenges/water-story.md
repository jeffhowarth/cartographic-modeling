# __water story__  

## Introduction  

This problem introduces a workflow to map nominal values in vector tables with different colors and with casings and fills (borders and interiors). Unfortunately, this is surprisingly difficult to do in earth engine, which is troublesome because a lot of conservation data gets delivered as feature collections (vector tables). So for practical reasons, I would like you to learn some methods to deal with this problem.  

This problem is also motivated by a personal pet peeve: I am bothered by maps that do not distinguish between ditches (built by people in the last 100 years to drain wetlands for agriculture) and streams (built through fluvial processes over millennia). I think cartographers have an ethical responsibility to not participate in the erasure of the past and to instead help people remember the past and recognize how recent history has transformed the landscapes we now inhabit. For me, using the same color for streams and ditches does not feel ethically responsible, at best.  

## Goal  

Please do the following:  

1. Make a copy of your shaded relief script (called it wk04_03_water_story_challenge.md).
2. Copy the starter script below and paste it into the new script after the shaded relief part.    
3. Read through the script and play with it to try to understand how the wetlands section works. 
4. Try to finish styling the stream, ditch, and pond data by completing the last section where I leave you hanging. 
5. Ideally, your script should produce the layers shown in the app below.

<iframe src=https://ee-edu-apps.projects.earthengine.app/view/gg0352-shaded-relief-with-water-features title="Shaded Relief with water features" height=720 width=720 allowfullscreen= true></iframe> 


## Starter script

```js
// -------------------------------------------------------------------------
//  PART II: WATER STORY CHALLENGE
// -------------------------------------------------------------------------

// -+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-
//  A. WETLANDS
// -+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-

//  Load wetland data and filter by region.  

var wet_class = ee.FeatureCollection(data.wetlands.vswi_class.fc_address)
  .filterBounds(study_region)
;

//  Print to see what you are working with.  

print(
  "WETLANDS",
  wet_class.first(),
  wet_class.aggregate_array('CLASS').distinct().sort()
  )
;

//  Load soils, filter by study region, and filter for hydric soils. 

var hydric = ee.FeatureCollection(data.soils.addison.fc_address)
  .filterBounds(study_region)
  .filter(ee.Filter.eq('HYDRIC', 'Y'))
;

//  Print so you can see what ya got.  

print(
  'HYDRIC',
  hydric.first(),
  hydric.aggregate_array('HYDRIC').distinct().sort()
  )
;

// Define a style dictionary for nominal classes. 

var wet_styles = ee.Dictionary({
    "class1": {color: '#7F4D84CC', fillColor: '#D7BFD9CC', width: 1},
    "class2": {color: '#5C4D85CC', fillColor: '#C6BFD9CC', width: 1},
    "hydric": {color: '#4D857780', fillColor: '#BFD9D380', width: 1}
    
});

//  Make a distinct feature collection for each class 
//  and tag each feature in the layer with a name that matches a key in the dictionary. 

var class1 = t.tag2style(wet_class, 'CLASS', 1, 'class1');
var class2 = t.tag2style(wet_class, 'CLASS', 2, 'class2');
var hydric = t.tag2style(hydric, 'HYDRIC', 'Y', 'hydric');

//  Merge the three tagged collections into a single feature collection.  

var wetlands = hydric
  .merge(class2)
  .merge(class1)
  ;

//  Print this out so that you can see what the last step did. 

print(
  "WETLANDS",
  wetlands 
  )
;

//  Map the style dictionary to each feature in the collection.
//  This makes the style parameters a property of each feature in the collection.  

var wetlands_with_styles = wetlands
  .map(t.fStyle(wet_styles, "tag"))
;

//  Print this out so that you can compare with wetlands and see what the last step did. 

print(
  "With styles",
  wetlands_with_styles.first()
);

// Apply the styles to make an RGB image. 

var wetlands_styles_applied = wetlands_with_styles
  .style({styleProperty: 'style'})
  .updateMask(study_region_binary)
;

//  Display the RGB image.  Notice how the result now has casings and fills.  

Map.addLayer(wetlands_styles_applied, {}, "Wetlands - styles applied" );

// -+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-
//  B. SURFACE WATERS 
// -+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+- 

// Load stream area data and filter by region. 

var stream_area = ee.FeatureCollection("projects/sat-io/open-datasets/NHD/NHD_VT/NHDArea")
  .filterBounds(study_region)
;

Map.addLayer(stream_area, {color: 'cyan'}, "Stream area", false);

// Load stream line data and filte by region. 

var stream_line = ee.FeatureCollection("projects/sat-io/open-datasets/NHD/NHD_VT/NHDFlowline")
  .filterBounds(study_region)
;

Map.addLayer(stream_line, {color: 'cyan'}, "Stream line", false);

//  Load waterbody data and filter by region.  

var waterbody = ee.FeatureCollection("projects/sat-io/open-datasets/NHD/NHD_VT/NHDWaterbody")
  .filterBounds(study_region)
;

Map.addLayer(waterbody, {color: 'cyan'}, "Waterbody", false);  

//  Print to compare and contrast tables.  

print(
  "NHD features",
  stream_area.first(),
  stream_line.first(),
  waterbody.first()
  )
;

//  Here is a cheat sheet for the fcodes in our dataset (standard for the national hydrology dataset)
//  and a strategy to display them on the map. 

//  The goal is to distinguish ditches from other water features;
//  because ditches were created to drain wetland soils.

var fcodes = {
  39004: ["Lake/Pond", 'natural'],
  33600: ["Canal/Ditch", 'ditch'],
  46006: ["Stream/River perennial", 'natural'],
  55800: ["Artificial path", 'ignore']
};

//  Here is the style dictionary for natural vs ditch channels. 

var nhd_styles = ee.Dictionary({
  "natural": {color: '#688A91', fillColor: '#ACDCE6', width: 2},
  "ditch": {color: '#CC8866', fillColor: '#E6C7B8', width: 2},
  })
;

// -+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-
//  TRY TO COMPLETE THE REMAINDER OF THIS SCRIPT 
//  TO DISPLAY THE WATER FEATURES AS SHOWN IN THE APP.
// -+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-
```
