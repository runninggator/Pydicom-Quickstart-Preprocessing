# Matplotlib is a graphic utility. We want the pyplot
# tool to show the slice data.
import matplotlib.pyplot as plt
from pydicom import dcmread

# Full path to the dicom file
full_path_to_dicom_file = \
    r"C:\Users\Acer\Documents\BME\Neuroimaging" + \
    r"\midterm_guide\data\003_S_6264_mri" + \
    r"\ADNI_003_S_6264_MR_Accelerated_Sagittal_MPRAGE__br_raw_20190916165655131_99_S873488_I1227039.dcm"

# Load the dicom file. Print the patient name to the console.
dicom_file_data = dcmread(full_path_to_dicom_file)
print(dicom_file_data.PatientName)

# Using Matplotlib, create a figure with the dicom pixel_array data.
# The pixel_array attribute contains the grayscale image values for
# that slice. Also, tell Matplotlib that this image is in the grayscale
# colorspace. The "show" function is called to display the figure 
# in a new window.
plt.imshow(dicom_file_data.pixel_array, cmap=plt.cm.gray)
plt.show()