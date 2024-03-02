# __nominal problems__

## __Introduction__    

Nominal problems concern changing the _names at locations_. Often, the names describe _kinds of things_ (categories, classes, types). There are three kinds of nominal change:   

| Task                  | Lexicon                                                                       |
| :--                   | :--                                                                           |
| __Rename__            | Output has _same_ names as input, but they occur in different locations.      |
| __Generalize__        | Output has _fewer_ names than input.                                          |
| __Specify__           | Output has _more_ names than input.                                           |

In practice, you often apply these changes surgically, altering a subset of names in a subregion of the layer.     

## __Illustration__  

To illustrate, we will use [Vermont's  Statewide High-Resolution Land Cover Dataset](https://vcgi.vermont.gov/data-release/statewide-high-resolution-vermont-land-cover-data-now-available){target=_blank} from the [Awesome Community Datasets](https://github.com/samapriya/awesome-gee-community-datasets){target=_blank} repo.  

Our goal is to specify agriculture from other grasslands in specific zones of the layer. 

## __Implementation__  

Start a new script in our repo called __nominal.js__.  

Insert a header, then load the data and task modules.   

```js
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//  Nominal problem:
//  specify different kinds of grasslands.

//  Last modified: insert date
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

var data = require('users/jhowarth/public:modules/data.js');       
print('DATA', data);

var t = require('users/jhowarth/public:modules/tasks.js');

```

Now write a script that meets the following conditions:  

1. Defines agricultural lands with data from data.lc.ag.
2. Records a new class for agriculture at any grass/shrub or bare ground location in the base layer (data.lc.base).
3. Does not alter any other class (tree canopy, water, road, etc).

If you would like a template and answers to help you check your work, then [here is a workflow][nominal01].  


---

[nominal01]: ../workflows/nominal-workflows.md  

