import os
from Helpers.helper_functions import measure_boulder_dimensions

# Define input and output file paths
input_vector_path = 'Input/BE3956H-511_B02_ManualyPickedBoulders.shp'
output_vector_path = 'Output/output_boulder_measurements.shp'
block_name = 'Block1'

# Call the helper function to perform the task using only the vector data
measure_boulder_dimensions(input_vector_path, None, output_vector_path, block_name)

print("Boulder measurements completed and saved to output folder.")
