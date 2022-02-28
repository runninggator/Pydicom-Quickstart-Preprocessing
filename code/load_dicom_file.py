# Import dcmread from Pydicom. This function
# will read in a dicom file and store its contents 
# in an object.
from pydicom import dcmread

# Path to a dicom file. If running this yourself, make sure to
# change this path to point to your own file. 
# The backslashes at the end of each line "\"
# are python line-breaks that allow for a multi-line command 
# (for readability). The "r" in front of the strings tells python
# to interpret the strings as a raw string and ignore special characters
# like the backslash characters inside each string.
full_path_to_dicom_file = \
    r"C:\Users\Acer\Documents\BME\Neuroimaging" + \
    r"\midterm_guide\data\003_S_6264_mri" + \
    r"\ADNI_003_S_6264_MR_Accelerated_Sagittal_MPRAGE__br_raw_20190916165345336_183_S873488_I1227039.dcm"

# Read the dicom file and store its contents in the variable
# "dicom_file_data"
dicom_file_data = dcmread(full_path_to_dicom_file)

# Print the dicom file data object
print(str(dicom_file_data))