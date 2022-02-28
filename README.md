# Pydicom Quickstart Preprocessing
 A simple guide to creating a Pydicom preprocessing pipeline.

## Overview
Pydicom is a python tool for working with dicom datasets. It provides a simple framework for reading and modifying dicom files with a command-line-like interface (there is no graphical user interface). Pydicom is a Python tool, so if you’re familiar with Python or are looking to leverage the wide variety of existing Python packages into your medical imaging toolbox, then Pydicom is a great place to start. I use Pydicom in my own research and I’m excited to share with you some insights into creating a simple preprocessing pipeline.

In this guide, we will be going over the basics of Python and Pydicom. We will use Pydicom to: 
1. load dicom files from a dicom dataset
2. view the pixel array data using Matplotlib
3. copy the dataset and normalize the pixel arrays
4. extract the normalized slices into a 3d Numpy matrix

This particular pipeline is geared for submitting data into a 3-dimensional machine learning model. Let’s get started!

**For the detailed walkthrough please refer to** [this guide](https://docs.google.com/document/d/1SDfkJujvq5VAXviAgMhEDXuYmf0ie2m7fQ1raC5bmY4/edit?usp=sharing)
