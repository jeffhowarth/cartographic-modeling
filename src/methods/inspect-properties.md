## print first feature in FC  

```js
// -------------------------------------------------------------
//  PRINT FIRST FEATURE IN COLLECTION.  

//  Replace 'LABEL' with appropriate header.  
//  Replace fc with appropriate variable.
```

```js
// -------------------------------------------------------------

print(
    "LABEL",
    fc.first()
    )
;
```

---  

## print unique values in FC  

```js
// -------------------------------------------------------------
//  PRINT UNIQUE VALUES OF FEATURE PROPERTY IN COLLECTION. 

//  Replace 'LABEL' with appropriate header.  
//  Replace fc with appropriate variable.
```

```js
// -------------------------------------------------------------

print(
    "LABEL",
    fc.aggregate_array().distinct().sort()
    )
;
```

---  

## print size of collection  

```js
// -------------------------------------------------------------
//  PRINT SIZE OF COLLECTION. 

//  Replace 'LABEL' with appropriate header.  
//  Replace collection with appropriate variable.
```

```js  
// -------------------------------------------------------------

print(
    "LABEL",
    collection.size()
    )
;
```

---  

[print-first]: ../methods/inspect-properties.md#print-first-feature-in-fc
[print-unique]: ../methods/inspect-properties.md#print-unique-values-in-fc  
[print-size]: ../methods/inspect-properties.md#print-size-of-collection