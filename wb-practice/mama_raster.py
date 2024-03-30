# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# MAMA RASTER SCRIPT
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

# Declare a directory for our outputs.
# You will need to first make this directory in finder or explorer.  

out = work + "jhowarth/outputs/mama/"

# Declare a name for our test data

dem = work + "data/elevation/dem_clip_practice.tif"
mama = work + "jhowarth/x0352/lc/base_land_cover.tif"  

# -----------------------------------------------------------------------

# Resample higher resolution image(s) to match resolution and extent of mama image. 
# All images must be in the same CRS. 

wbt.resample(
    inputs = dem, 
    output = "_01_dem_from_mama.tif", 
    cell_size=None, 
    base = mama, 
    method = "cc",                  # 'nn' for nominal; 'bilinear' or 'cc' for continuous.
    # callback=default_callback
)
