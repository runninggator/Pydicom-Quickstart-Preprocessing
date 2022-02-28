# The "os" package is for performing traditional bash commands.
# The "shutil" is for additional commands like deleting directories
import os
import shutil

from pydicom import dcmread

# Path to the dicom directory
full_path_to_dicom_dataset = \
    r"C:\Users\Acer\Documents\BME\Neuroimaging" + \
    r"\midterm_guide\data\003_S_6264_mri"

# Path to the new dataset
# This path doesn't need to already exist and will be created for you.
# Warning, this directory will be recursively deleted if it already
# exists.
full_path_to_result_dataset = \
    r"C:\Users\Acer\Documents\BME\Neuroimaging" + \
    r"\midterm_guide\data\003_S_6264_mri_normalized"

# If the normalized dataset already exist, delete it because
# this script will be remaking it. "shutil.rmtree" recursively
# deletes a directory
if (os.path.exists(full_path_to_result_dataset)):
    # The "f" in front of the string allows us to do inline string formatting.
    # Anything inside curly brackets will be evaluated and placed
    # into the string. "\n" creates a new line.
    # The "input" function is built-in to python and pauses the program to
    # get feedback from the user. Because we plan on deleting a directory, 
    # we are asking the user for permission beforehand.
    user_input = input(f"Directory {full_path_to_result_dataset} already exists.\nDelete (y/n)?: ")

    if user_input == "y":
        shutil.rmtree(full_path_to_result_dataset)
    else:
        print("Please change the result path to point to non-existing directory.")

        # You can terminate a Python script with the "quit" function.
        quit()

# Create an empty result directory
os.makedirs(full_path_to_result_dataset)

# This command gets all the filenames from the directory and stores
# the names in a list (a python array)
dicom_filenames = os.listdir(full_path_to_dicom_dataset)

# These lists are for storing each dicom files min/max pixel array values
dicom_mins = []
dicom_maxs = []

# datatype for to convert pixel array to
dtype = 'float16'

# Open each dicom file and find the min and max values.
# We need the mins and maxs to properly normalize the data.
# The for ... in ...: syntax is a "pythonic" way of looping over
# a Python list (more broadly referred to as an iterable) 
# There are other ways to loop over a list, I like
# this syntax because it is concise and easy to read.
for dicom_filename in dicom_filenames:
    # Append the filename to the path of the dicom dataset directory
    full_dicom_file_path = os.path.join(full_path_to_dicom_dataset, dicom_filename)

    dicom_data = dcmread(full_dicom_file_path)

    # "pixel_array" contains the slice image data as a numpy matrix.
    # "min" and "max" are Numpy methods for getting the min/max values
    # from the matrix. Python lists can be appended to with the "append" method
    dicom_mins.append(dicom_data.pixel_array.min().astype(dtype))
    dicom_maxs.append(dicom_data.pixel_array.max().astype(dtype))

# "min" and "max" are built-in Python functions for getting the 
# min/max values from Python lists. Don't confuse these for the 
# Numpy min/max methods, although they are very similar they work with
# different datatypes.
dataset_min = min(dicom_mins)
dataset_max = max(dicom_maxs)

# Now we are going to go through all of the dicom data again.
# This time we will modify the dicom file and copy it to our
# result directory
for dicom_filename in dicom_filenames:
    full_dicom_file_path = os.path.join(full_path_to_dicom_dataset, dicom_filename)
    dicom_data = dcmread(full_dicom_file_path)

    # To edit the pixel_array data, we must change the PixelData attribute. This
    # is just a Pydicom nuance, but by updating the PixelData, the pixel_array
    # data is automatically updated too. Because we want to convert to a float
    # datatype (range 0 to 1), we need to use the FloatPixelData attribute instead
    # and we must delete the PixelData attribute.
    dicom_data.FloatPixelData = ((dicom_data.pixel_array.copy().astype(dtype) - dataset_min) / dataset_max).tobytes()
    delattr(dicom_data, 'PixelData')

    # Also change the patient name to reflect that this is a normalized file.
    dicom_data.PatientName = f"{dicom_data.PatientName}_normalized"

    # Save the new dicom_file in the result directory. 
    # We will append "_normalized" to the filename as well. The square
    # brackets (ie. [0:-4]) is an array slicing technique used to append
    # to the filename before the file type postfix.
    # NOTE: It really doesn't make much sense to be saving dicom files in this
    # normalized format. Normally instead of creating a new dicom directory,
    # we would just create the 3d Numpy file directly from our normalized 
    # data. However this guide creates a new directory to illustrate how 
    # to modify dicom files using Pydicom.
    # PS: These normalized dicom files will no longer look anatomically correct
    # when viewed in a dicom viewer.
    result_full_filename = os.path.join(
        full_path_to_result_dataset, 
        f"{dicom_filename[0:-4]}_normalized{dicom_filename[-4:]}"
    )
    dicom_data.save_as(result_full_filename)

    # One last point: in a real world setting, you should normalize all your
    # subjects together. ie. find the overall min/max for your entire 
    # training cohort and use those values to normalize all subjects.