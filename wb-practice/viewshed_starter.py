# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# VIEWSHED STARTER SCRIPT
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  

# import tools from WBT module

import sys
sys.path.insert(1, '/Users/jhowarth/tools')     # path points to my WBT directory
from WBT.whitebox_tools import WhiteboxTools

# declare a name for the tools

wbt = WhiteboxTools()

# Set the Whitebox working directory
# You will need to change this to your local path name

work =  "/Users/jhowarth/Library/CloudStorage/GoogleDrive-jhowarth@middlebury.edu/Shared drives/GEOG0352-S24/"

wbt.work_dir = work

# Declare a director for our outputs  

out = work + "jhowarth/outputs/viewsheds/"



# Declare a name for our test data

dsm = work + "data/elevation/dsm_clip_practice.tif"
dem = work + "data/elevation/dem_clip_practice.tif"
view_point = work + "data/practice_supplements/view_point.shp"

# -----------------------------------------------------------------------

wbt.viewshed(
    dem = dsm, 
    stations = view_point, 
    output = out + "_01_test_shed_dsm.tif", 
    height=1.8, 
    # callback=default_callback
)

wbt.viewshed(
    dem = dem, 
    stations = view_point, 
    output = out + "_02_test_shed_dem.tif", 
    height=1.8, 
    # callback=default_callback
)

wbt.multiply(
    input1 = out + "_02_test_shed_dem.tif", 
    input2 = 10, 
    output = out + "_03_test_shed_dem_10.tif", 
    # callback=default_callback
)

wbt.add(
    input1 = out + "_01_test_shed_dsm.tif", 
    input2 = out + "_03_test_shed_dem_10.tif", 
    output = out + "_04_test_shed_comparison.tif", 
    # callback=default_callback
)
