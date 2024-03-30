# __workflow diagrams__  

Workflow diagrams show how each step in a solution connects to other steps. The color represents the format of the result (or output) of each step as shown below.  

<center>

``` mermaid
graph TD
  raster[raster] ;
  vector[vector] ;

style raster fill:#C5E6A1,stroke-width:0px
style vector fill:#E1C3E6,stroke-width:0px
```

</center>

Links between steps show how the output of one step serves as the input to another.      

<center>

``` mermaid
graph LR
  step01[Step 1] ;
  step02[Step 2] ;

  step01 --> step02 

  style step01 fill:#C5E6A1,stroke-width:0px
  style step02 fill:#E1C3E6,stroke-width:0px

  
```