# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# HYDRO STARTER SCRIPT
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

out = work + "jhowarth/outputs/hydro/"

# Declare a name for our test data

dem = work + "jhowarth/outputs/elevation/dem_clipped_practice.tif"

# -----------------------------------------------------------------------

# Breach depressions. 

wbt.breach_depressions_least_cost(
    dem = dem, 
    output = out + 'hydro_01_breach.tif', 
    dist = 10,   # This affects processing time - try to keep low (think width of roads).
    max_cost=None, 
    min_dist=True, 
    flat_increment=None, 
    fill=True
)

# Flow direction 

wbt.rho8_pointer(
    dem = out + 'hydro_01_breach.tif', 
    output = out + 'hydro_02_pointer.tif', 
    esri_pntr=False
)

# Flow accumulation 

wbt.rho8_flow_accumulation(
    i = out + 'hydro_02_pointer.tif', 
    output = out + 'hydro_03_flow_acc.tif', 
    out_type="cells", 
    log=False, 
    clip=False, 
    pntr=True, 
    esri_pntr=False, 
)

# extract streams  

wbt.extract_streams(
    flow_accum = out + 'hydro_03_flow_acc.tif', 
    output = out + 'hydro_04_streams_1000.tif', 
    threshold = 1000, 
    zero_background=False, 
)

# strahler order

wbt.strahler_stream_order(
    d8_pntr = out + 'hydro_02_pointer.tif', 
    streams = out + 'hydro_04_streams_1000.tif', 
    output = out + 'hydro_05_strahler.tif', 
    esri_pntr=False, 
    zero_background=False, 
    # callback=default_callback
)

# make vector streams 

wbt.raster_streams_to_vector(
    streams= out + 'hydro_05_strahler.tif', 
    d8_pntr = out + 'hydro_02_pointer.tif', 
    output = out + 'hydro_06_stream_lines.shp', 
    esri_pntr=False, 
    # callback=default_callback
)
