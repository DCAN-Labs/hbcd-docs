# Recommended Programs & Utilities

## Tabulated Data
Tabulated data within the `phenotype/` folder includes demographic, toxicology, and behavioral data provided as `.tsv` and `.parquet` files (see details [here](../../datacuration/phenotypes.md)). To work with these files, we recommend the following programs:

<i class="fas fa-database"></i> **NBDCtools** [COMING SOON]   
This R package can be used to parse the columns or tables you want to use as a data frame in R. The package will automatically determine the appropriate file to pull from and how to format the data based on the data dictionary. This allows for easy manipulation and analysis of the data without having to manually parse the files or worry about formatting issues.   
[Download page for NBDCtools <i class="fa fa-download"></i>]() 

## Brain Imaging Data
#### Interactive Visualization of Volumetric NIfTI (`.nii.gz`) files (e.g. T1w, T2w, DTI, etc.)
<i class="fa-solid fa-eye"></i></i> **[ITK-Snap](http://www.itksnap.org/pmwiki/pmwiki.php)**    
A free, open-source software application used to visualize and segment 3D and 4D medical images. See an overview of ITK-Snap on Andy's Brain Blog [here](https://andysbrainbook.readthedocs.io/en/latest/ITK-Snap/ITK-Snap_Overview.html#itk-snap-overview) for a primer.      
[Download page for ITK-Snap <i class="fa fa-download"></i>](http://www.itksnap.org/pmwiki/pmwiki.php?n=Downloads.SNAP4)

<i class="fa-solid fa-eye"></i></i> **[FSLeyes](https://fsl.fmrib.ox.ac.uk/fsl/docs/#/utilities/fsleyes)**    
A free, open-source image viewer for medical images, particularly MRI data. Part of the FSL software suite.    
[Download page for FSLeyes <i class="fa fa-download"></i>](https://fsl.fmrib.ox.ac.uk/fsl/docs/#/utilities/fsleyes)

#### Interactive Visualization & Processing of Surface Data
**[Connectome Workbench](https://www.humanconnectome.org/software/connectome-workbench)** is a free, open-source software package particularly useful for visualizing connectivity data, surface-based analyses, and more. It is recommended for viewing and processing surface data (`.gii` files), volume data (`.nii/.nii.gz` files), and CIFTI data (dlabel, dscalar, dtseries, pconn, etc. files) - check out this [blog post](https://mvpa.blogspot.com/2014/03/nifti-cifti-gifti-in-hcp-and-workbench.html) for a helpful primer on the difference between these various file formats. Useful Workbench tools include wb_view and wb_command.    
[Download page for Connectome Workbench <i class="fa fa-download"></i>](https://humanconnectome.org/software/get-connectome-workbench)

<i class="fa-solid fa-eye"></i></i> **wb_view**       
<span style="display: inline-block; background-color: #f0f8ff; color: #333; border-radius: 12px; padding: 1px 5px; font-size: 0.9em; border: 1px solid #d0e7ff;">
  <i class="fa-regular fa-lightbulb" style="margin-right: 6px; color:rgb(13, 148, 8);"></i>
  <strong>Good for:</strong> interactive visualization (volumetric & surface data)
</span>     
An interactive GUI used for inspecting images, particularly useful for visualizing surface-based data. It allows users to view and manipulate 3D brain images, including the ability to rotate, zoom, and pan the images. It also provides tools for overlaying different types of data, such as functional and structural images, and for visualizing connectivity data.  

<i class="fas fa-cogs"></i> **wb_command**          
<span style="display: inline-block; background-color: #f0f8ff; color: #333; border-radius: 12px; padding: 1px 5px; font-size: 0.9em; border: 1px solid #d0e7ff;">
  <i class="fa-regular fa-lightbulb" style="margin-right: 6px; color:rgb(13, 148, 8);"></i>
  <strong>Good for:</strong> processing & analysis
</span>     
A command-line tool that provides a variety of functions for processing and analyzing neuroimaging data. It can be used to perform a wide range of tasks, including image registration, surface generation, and statistical analysis. The command-line interface allows for batch processing of data and can be integrated into scripts for automated analysis.

## Programming Languages

<i class="fas fa-laptop-code"></i> **[MATLAB](https://www.mathworks.com/products/matlab.html)**   
  MATLAB has a variety of built-in functions and toolboxes for neuroimaging data. Note that it is proprietary, but may be provided at no-cost through your institution or department. See Andy's Brain Blog [Matlab for Neuroimagers](https://andysbrainbook.readthedocs.io/en/latest/Matlab/Matlab_Overview.html#matlab-for-neuroimagers) for a primer.

<i class="fas fa-laptop-code"></i> **Python**   
  Python is also commonly used in the field of neuroimaging: useful Python modules for neuroimaging include NiBabel, Nilearn, Nipype, PyNIfTI, PySurfer, PyTorch, and others. See Andy's Brain Blog [Python for Neuroimagers](https://andysbrainbook.readthedocs.io/en/latest/PythonForNeuroimagers/PythonForNeuroimagers_Overview.html) for a primer. 

<i class="fas fa-laptop-code"></i> **R/RStudio**    
  Especially strong for statistical plots, often used in conjunction with analysis results.       
  [Download page for R/RStudio <i class="fa fa-download"></i>](https://posit.co/download/rstudio-desktop/)


## Electroencaphalography (EEG) Data
The EEG Core of the HBCD Data Coordinating Center (HDCC) has a [GitHub repository](https://github.com/ChildDevLab/HBCD-data-release-notes) with file notes and scripts for working with the first HBCD EEG data release. We recommend all users to review this page for important resources. Users can contact us with any questions about working with the EEG data or using the GitHub repository at eegdata@umd.edu.