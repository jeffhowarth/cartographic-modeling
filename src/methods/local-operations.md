### erase values at locations with binary   

```js
// -------------------------------------------------------------
//  ERASE VALUES AT LOCATIONS WITH BINARY.

//  INPUT is an image with values to erase.
//  BINARY is a binary image {0,1}.
//  OE (output erased) is an image. 
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

[erase-wo-mask]: ../methods/local-operations.md#erase-values-at-locations-with-binary  