## maximum at locations       

```js
// -------------------------------------------------------------
//  MAXIMUM AT LOCATIONS

//  This operation does pairwise comparisons of pixel values between
//  two images (i1, i2); the output stores the maximum of each pair. 
```

```js
// -------------------------------------------------------------

var output = i1.max(i2);

```

---  

## intersect two binaries    

```js
// -------------------------------------------------------------
//  INTERSECT TWO BINARIES.

//  i1 and i2 are both binary images {0,1}.
//  output is a binary image {0,1}.
```

```js
// -------------------------------------------------------------

var output = i1.and(i2);

```

---  

## erase values at locations with binary   

```js
// -------------------------------------------------------------
//  ERASE VALUES AT LOCATIONS WITH BINARY.

//  INPUT is an image with values to erase.
//  BINARY is a binary image {0,1}.
//  OE (output erased) is an image. 
```

```js
// -------------------------------------------------------------

var oe = input
  .multiply(binary)
;

print(
  "ERASED",
  oe
  )
;
```

---

[local-erase]: ../methods/local-two-layers.md#erase-values-at-locations-with-binary 
[local-intersection]: ../methods/local-two-layers.md#intersect-two-binaries  
[local-max]: ../methods/local-two-layers.md#maximum-at-locations
