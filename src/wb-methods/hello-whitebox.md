## directory structure  

You will need to set up a workspace as shown below.    

1. Make a project folder (in example I called this __GEOG0352__).
2. Place __WBT__ folder in the project folder.
3. Create __hello-whitebox.py__ file in the project folder (above the WBT).  

![whitebox-directory-setup](https://geography.middlebury.edu/howarth/ee_edu/wb/wb-directory.png)

## write a header

```py
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#   Hello Whitebox
#   
#   To test my whitebox configuration.
#   Date
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  
```

## load modules  

```py
# import tools from WBT module

from WBT.whitebox_tools import WhiteboxTools

# declare a name for the tools

wbt = WhiteboxTools()

```

## set up your working directory 

```py
# Set your working directory - where you will read and write files. 
# NOTE: You will need to customize the path name below. 

work =  "/Users/jhowarth/Library/CloudStorage/GoogleDrive-jhowarth@middlebury.edu/Shared drives/GEOG0352-S24/"

wbt.work_dir = work
```

## declare names for output directory and starter data

```py
# Declare a directory for our outputs  

out = work + "jhowarth/outputs/"

# Declare a name for our test data

dsm = work + "DATA/_test_dsm.tif"

```

## call a whitebox operation  

```py
# Call the slope tool and define parameters

wbt.slope(
    dem = dsm,
    output = out + "_test_slope.tif",
    zfactor=None,
    units="degrees"
)

```

## visualize output with QGIS  

1. Open QGIS  
2. Save new project as 'wb_viewer' in your cloud project directory and at the same level as your outputs folder. 
3. Add data to QGIS project from outputs folder. 

## use whitebox manual to call other operations  

[Whitebox Tools manual][wbt-man]{target=_blank}

```py
# Threshold the slope output: less than or equal to 10 degrees.  

# BASIC SYNTAX
# after argument: =
# before file names: out +  
# include filename extension: .tif 
# delete callback

```

## challenge

```py
# Calculate surface height (not elevation)

```

[wbt-man]: https://www.whiteboxgeo.com/manual/wbt_book/intro.html