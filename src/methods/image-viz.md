## make histogram of image values 

```js
// Make a viz dictionary.

var input_viz = {
  min: [0,0,0],                       // List of min in same order as band list.
  max: [255,255,255],                 // List of max in same order as band list.
  bands: ['R', 'G', 'B']              // In this example, R is index 0, G is index 1, and B is index 2.
};

// Make a histogram to see data distribution.  

var b = 0;                            // This targets a band number by the list index. 0 will target R.
var i = INPUT;                        // This targets an image. Replace IMAGE with image variable.
var v = input_viz;                    // This targets the viz parameters for the image.

var histogram = t.makeHistogram(
  i,                                  // Must be an image (not an image collection).
  v.bands[b],                         // Select one band at a time.
  3,                                  // Pixel resolution of image.
  v.min[b],                           // Minimum value of x-axis
  v.max[b]                            // Maximum value of x-axis.
  )
;

// Print, print, print...

print(
  "HISTOGRAM", 
  histogram
  )
;
```

---

[make-histogram]: ../methods/image-viz.md#make-histogram-of-image-vales 
