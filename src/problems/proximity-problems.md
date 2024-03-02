# __proximity problems__  

## __Introduction__  

Proximity problems deal with _relative distance_, or how far a location is from another location. 

A classic proximity problem involves classifying a threshold distance from a feature or collection of features.  

## __Illustration__      

To illustrate, we will use [Vermont's  Statewide High-Resolution Land Cover Dataset](https://vcgi.vermont.gov/data-release/statewide-high-resolution-vermont-land-cover-data-now-available){target=_blank}.

Your goal is to specify a zone based on distance to nearest human structures.   

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

Now write a script that produces a binary raster layer of all locations within 50 meters of a human structure (from data.cadastre.college).  

If you would like a template and answers to help you check your work, then [here is a workflow][prox01].

---

[prox01]: ../workflows/proximity-workflows.md  






