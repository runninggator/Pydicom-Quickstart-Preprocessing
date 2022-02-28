# Numpy is a popular Python library for working with matrices.
import numpy as np

import os
from pydicom import dcmread

# Path to the normalized dataset
# This directory should have been created and populated
# in the previous preprocessing step.
full_path_to_normalized_dataset = \
    r"C:\Users\Acer\Documents\BME\Neuroimaging" + \
    r"\midterm_guide\data\003_S_6264_mri_normalized"

dicom_filenames = os.listdir(full_path_to_normalized_dataset)

# Save the filenames and slice locations, this will be used
# for ensuring the slices are in the correct order
file_and_slice_locations = []

# Loop over dicom data and save the slice locations
for dicom_filename in dicom_filenames:
    full_dicom_file_path = os.path.join(full_path_to_normalized_dataset, dicom_filename)
    dicom_data = dcmread(full_dicom_file_path)

    slice_location = float(dicom_data.SliceLocation)

    # Here we are appending dictionary key-value pair objects
    # to the list
    file_and_slice_locations.append({
        'file_name': dicom_filename,
        'slice_location': slice_location
    })

# Sort by slice location. The "sort" function sorts a Python list according to
# a lambda function.
file_and_slice_locations.sort(key=lambda inst: inst['slice_location'], reverse=True)
dicom_filenames = [dicom_data['file_name'] for dicom_data in file_and_slice_locations]

# This variable will hold our Numpy 3d data.
# It will be initialized during the first loop iteration 
# to be the proper shape (height, width, depth)
data_3d = None

for slice_num, dicom_filename in enumerate(dicom_filenames):
    full_dicom_file_path = os.path.join(full_path_to_normalized_dataset, dicom_filename)
    dicom_data = dcmread(full_dicom_file_path)

    if (data_3d is None):
        # Initialize the 3d data. This will only
        # happen on the first iteration.
        # This line might be confusing but essentially it creates a 
        # 3d numpy matrix with the same shape of the dataset and with the data
        # type of the original pixel_array. 
        # Advanced note: The "shape" attribute returns a Python list with the 
        # Numpy shape ie. [height, width]. 
        # The unpacking operator (*) unpacks an array into
        # individual parameters. "np.zeros" creates a numpy array with all zeroes
        # with the given shape.
        data_3d = np.zeros((len(dicom_filenames), *dicom_data.pixel_array.shape)).astype(dicom_data.pixel_array.dtype)

    # Add this slice to the numpy array. Array indexing allows us to overwrite
    # individual slices.
    data_3d[slice_num,:,:] = dicom_data.pixel_array

# Now save the numpy 3d data to your current directory
np.save('data_3d_normalized.npy', data_3d)

# Let's print out the min, max and mean of the 3d data as
# a quick validation test
print('min:', data_3d.min(), 'max:', data_3d.max(), 'mean:', data_3d.mean())