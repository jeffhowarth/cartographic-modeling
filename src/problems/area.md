# __area problems__  

Create a folder in your working repository named __area__.

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
2. Define a CUTTER:  
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
Total acres of college-owned parcels: <b>7009</b>  
</details>

### Reflection  

Think about the following:  

1. Compare your answers from the two solutions: how close are they?  
2. How sensitive is the raster solution to your choice of scale?  
