import os
from osgeo import gdal

gdal.UseExceptions()
gdal.AllRegister()

# Set parameters
input_folder = r"W:\ilmb\vic\geobc\Workarea\mgraff\objectstorage\imagefiles\oldext\ElephantHill_Imagery"  # Set your input folder here
output_folder = r"W:\ilmb\vic\geobc\Workarea\mgraff\objectstorage\imagefiles\oldext\ElephantHill_Imagery\COG"  # Set your output folder here
file_types = ["sid", "tif", "jpg"]  # File extensions to convert
#! Note: some file extensions require certain proprietary drivers ... e.g. .SID, .ECW 


# Define the function to convert files to COG
def convert_to_cog(input_path, output_path):
    # Open the input raster dataset
    input_ds = gdal.Open(input_path)
    if input_ds is None:
        print(f"Error: Could not open input file {input_path}")
        return

    # Create the output dataset
    output_ds = gdal.Translate(output_path, input_ds, options="-of COG -co COMPRESS=LAZW")
    
    # Close the datasets
    input_ds = None
    output_ds = None

    print(f"Conversion to COG successful: {output_path}")
    return output_path

# Define the function to find and convert files
def find_and_convert_files(input_folder, output_folder, file_types):
    for root, _, files in os.walk(input_folder):
        for file_name in files:
            if any(file_name.endswith(f".{file_type}") for file_type in file_types):
                file_path = os.path.join(root, file_name)

                # Maintain the folder structure three levels back
                relative_path = os.path.relpath(file_path, input_folder)
                parts = relative_path.split(os.sep)
                if len(parts) > 3:
                    relative_path = os.path.join(*parts[-4:])
                output_subfolder = os.path.join(output_folder, os.path.dirname(relative_path))
                os.makedirs(output_subfolder, exist_ok=True)

                output_path = os.path.join(output_subfolder, f"{os.path.splitext(file_name)[0]}.tif")
                convert_to_cog(file_path, output_path)
                print(f'Outputted COG: {file_name}')

# Run the conversion process
if __name__ == "__main__":
    find_and_convert_files(input_folder, output_folder, file_types)
