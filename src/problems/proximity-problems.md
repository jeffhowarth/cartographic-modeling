# __proximity problems__  

## __Introduction__  

Proximity problems deal with _relative distance_, or how far a location is from another location. 

A classic proximity problem involves classifying a threshold distance from a feature or collection of features. Often this zone of influence is called a _buffer_.   

## __Illustration__      

To illustrate, we will use an ancillary dataset from [Vermont's  Statewide High-Resolution Land Cover Dataset](https://vcgi.vermont.gov/data-release/statewide-high-resolution-vermont-land-cover-data-now-available){target=_blank} hosted on my data repo. 

Your goal is to use the "3D Building Roofprint' collection to specify a zone that is 100 feet to the nearest human structure.   

## __Implementation__  

Start a new script called __proximity_problem.js__.

Insert a header, then load the data and task modules.   

```js
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//  PROXIMITY PROBLEM
//  Specify a zone based on distance to nearest human structure. 

//  Last modified: insert date
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

var data = require('users/jhowarth/public:modules/data.js');       
print('DATA', data);

var t = require('users/jhowarth/public:modules/tasks.js');

```

Now write a script that produces a binary raster layer of all locations within 100 feet of a human structure (from data.lc.buildings).  

If you would like a template and answers to help you check your work, then [here is a workflow][prox01].

---

[prox01]: ../workflows/proximity-workflows.md  






