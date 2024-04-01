# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# LEAST COST PATH EXAMPLE - path from MBH to Knoll
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

out = work + "jhowarth/outputs/least-cost/"

# Declare a name for our test data

od = work + "jhowarth/x0352/od/od_lcp_practice.tif"  
lc = work + "jhowarth/x0352/land_cover/base_land_cover.tif"  

# ----------------------------------------------------------------------

# Select Knoll (value = 1) as source location. 

wbt.equal_to(
    input1 = od, 
    input2 = 1, 
    output = out + "_01_origin.tif", 
    # callback=default_callback
)

# Reclassify friction values from land cover classes. 

wbt.reclass(
    i = lc, 
    output = out + "_02_friction.tif", 
    reclass_vals = "10;1;3;2;2;3;5;4;5;5;1;6;1;7;5;8", 
    assign_mode=True
)

# Calculate cost distance

wbt.cost_distance(
    source = out + "_01_origin.tif", 
    cost = out + "_02_friction.tif", 
    out_accum = out + "_03_cost_acc.tif", 
    out_backlink = out + "_04_cost_backlink.tif", 
)

# Select BiHall (value = 10) as destination.  

wbt.equal_to(
    input1 = od, 
    input2 = 10, 
    output = out + "_05_destination.tif", 
    # callback=default_callback
)

# Find least cost path. 

wbt.cost_pathway(
    destination = out + "_05_destination.tif", 
    backlink = out + "_04_cost_backlink.tif", 
    output = out + "_06_lcp.tif", 
    zero_background=False, 
    # callback=default_callback
)
