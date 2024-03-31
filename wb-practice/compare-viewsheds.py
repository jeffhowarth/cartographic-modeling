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

dsm = work + "jhowarth/outputs/elevation/dsm_clipped_practice.tif"
dem = work + "jhowarth/outputs/elevation/dem_clipped_practice.tif"
view_point = work + "jhowarth/x0352/view_point/knoll.shp"

# -----------------------------------------------------------------------

wbt.viewshed(
    dem = dsm, 
    stations = view_point, 
    output = out + "_01_test_shed_dsm.tif", 
    height = 1.7, 
    # callback=default_callback
)

wbt.viewshed(
    dem = dem, 
    stations = view_point, 
    output = out + "_02_test_shed_dem.tif", 
    height = 1.7, 
    # callback=default_callback
)

wbt.resample(
    inputs = out + "_02_test_shed_dem.tif", 
    output = out + "_03_test_shed_dem_2mama.tif", 
    cell_size=None, 
    base=out + "_01_test_shed_dsm.tif", 
    method="nn", 
    # callback=default_callback
)


wbt.multiply(
    input1 = out + "_03_test_shed_dem_2mama.tif", 
    input2 = 10, 
    output = out + "_04_test_shed_dem_2mama_10.tif", 
    # callback=default_callback
)

wbt.add(
    input1 = out + "_01_test_shed_dsm.tif", 
    input2 = out + "_04_test_shed_dem_2mama_10.tif", 
    output = out + "_05_test_compare_sheds.tif", 
    # callback=default_callback
)
