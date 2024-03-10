## feature collection from address  
 
```js
// -------------------------------------------------------------
//  LOAD FEATURE COLLECTION FROM ADDRESS. 

//  Replace LAYER with a key from the data repo;
//  or replace argument with EE address string. 
// -------------------------------------------------------------
```

```js

var output = ee.FeatureCollection(data.LAYER.fc_address);

// -------------------------------------------------------------

```

---  

## image collection from address  
 
```js
// -------------------------------------------------------------
//  LOAD IMAGE COLLECTION FROM ADDRESS. 

//  Replace LAYER with a key from the data repo;
//  or replace argument with EE address string.
// -------------------------------------------------------------  
```

```js

var output = ee.ImageCollection(data.LAYER.ic);

// -------------------------------------------------------------

```

---  

## image from address  
 
```js
// -------------------------------------------------------------
//  LOAD IMAGE FROM ADDRESS. 

//  Replace LAYER with a key from the data repo;
//  or replace argument with EE address string.
// -------------------------------------------------------------  
```

```js  

var output = ee.Image(data.LAYER.i);

// -------------------------------------------------------------

```

---  

[load-fc]: ../methods/load-data.md#feature-collection-from-address 
[load-ic]: ../methods/load-data.md#image-collection-from-address  
[load-i]: ../methods/load-data.md#image-from-address