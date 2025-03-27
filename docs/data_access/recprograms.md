# Recommended Programs

## Brain Imaging Data
### Interactive Visualization - Volumetric Data
The following programs are recommended for visualizing volumetric data (e.g. T1w, T2w, DTI, etc.):

**[ITK-Snap](http://www.itksnap.org/pmwiki/pmwiki.php)**        
<span style="display: inline-block; background-color: #f0f8ff; color: #333; border-radius: 12px; padding: 1px 5px; font-size: 0.9em; border: 1px solid #d0e7ff;">
  <i class="fa-regular fa-lightbulb" style="margin-right: 6px; color:rgb(13, 148, 8);"></i>
  <strong>Good for:</strong> interactive visualization (volumetric data)
</span>     
A free, open-source software application used to visualize and segment 3D and 4D medical images. It is particularly useful for brain imaging files such as NIfTI (`.nii.gz`) MRI files (e.g. T1w, T2w, brain segmentations, etc.). See an overview of ITK-Snap on Andy's Brain Blog [here](https://andysbrainbook.readthedocs.io/en/latest/ITK-Snap/ITK-Snap_Overview.html#itk-snap-overview) for a primer.      
[Download page for ITK-Snap <i class="fa fa-download"></i>](http://www.itksnap.org/pmwiki/pmwiki.php?n=Downloads.SNAP4)

**[FSLeyes](https://fsl.fmrib.ox.ac.uk/fsl/docs/#/utilities/fsleyes)**      
<span style="display: inline-block; background-color: #f0f8ff; color: #333; border-radius: 12px; padding: 1px 5px; font-size: 0.9em; border: 1px solid #d0e7ff;">
  <i class="fa-regular fa-lightbulb" style="margin-right: 6px; color:rgb(13, 148, 8);"></i>
  <strong>Good for:</strong> interactive visualization (volumetric data)
</span>   
A free, open-source image viewer for medical images, particularly MRI data. It is part of the FSL software suite and provides a user-friendly interface for visualizing and analyzing neuroimaging data.       
[Download page for FSLeyes <i class="fa fa-download"></i>](https://fsl.fmrib.ox.ac.uk/fsl/docs/#/utilities/fsleyes)

### Interactive Visualization & Processing - Surface Data
**[Connectome Workbench](https://www.humanconnectome.org/software/connectome-workbench)** is a free, open-source software package particularly useful for visualizing connectivity data, surface-based analyses, and more. It is recommended for viewing and processing surface data (`.gii` files), volume data (`.nii/.nii.gz` files), and CIFTI data (dlabel, dscalar, dtseries, pconn, etc. files) - check out this [blog post](https://mvpa.blogspot.com/2014/03/cifti-primer.html) for a helpful primer on the difference between these various file formats. Useful Workbench tools include:

**wb_view**       
<span style="display: inline-block; background-color: #f0f8ff; color: #333; border-radius: 12px; padding: 1px 5px; font-size: 0.9em; border: 1px solid #d0e7ff;">
  <i class="fa-regular fa-lightbulb" style="margin-right: 6px; color:rgb(13, 148, 8);"></i>
  <strong>Good for:</strong> interactive visualization (volumetric & surface data)
</span>     
An interactive GUI used for inspecting images, particularly useful for visualizing surface-based data. It allows users to view and manipulate 3D brain images, including the ability to rotate, zoom, and pan the images. It also provides tools for overlaying different types of data, such as functional and structural images, and for visualizing connectivity data.  

**wb_command**          
<span style="display: inline-block; background-color: #f0f8ff; color: #333; border-radius: 12px; padding: 1px 5px; font-size: 0.9em; border: 1px solid #d0e7ff;">
  <i class="fa-regular fa-lightbulb" style="margin-right: 6px; color:rgb(13, 148, 8);"></i>
  <strong>Good for:</strong> processing & analysis
</span>     
A command-line tool that provides a variety of functions for processing and analyzing neuroimaging data. It can be used to perform a wide range of tasks, including image registration, surface generation, and statistical analysis. The command-line interface allows for batch processing of data and can be integrated into scripts for automated analysis.

[Download page for Connectome Workbench <i class="fa fa-download"></i>](https://humanconnectome.org/software/get-connectome-workbench)

### Programming Languages

**[MATLAB](https://www.mathworks.com/products/matlab.html)**        
<span style="display: inline-block; background-color: #f0f8ff; color: #333; border-radius: 12px; padding: 1px 5px; font-size: 0.9em; border: 1px solid #d0e7ff;">
  <i class="fa-regular fa-lightbulb" style="margin-right: 6px; color:rgb(13, 148, 8);"></i>
  <strong>Good for:</strong> analysis and data visualization
</span>          
MATLAB has a variety of built-in functions and toolboxes for neuroimaging data. Note that it is proprietary, but may be provided at no-cost through your institution or department. See Andy's Brain Blog [Matlab for Neuroimagers](https://andysbrainbook.readthedocs.io/en/latest/Matlab/Matlab_Overview.html#matlab-for-neuroimagers) for a primer.

**Python**      
<span style="display: inline-block; background-color: #f0f8ff; color: #333; border-radius: 12px; padding: 1px 5px; font-size: 0.9em; border: 1px solid #d0e7ff;">
  <i class="fa-regular fa-lightbulb" style="margin-right: 6px; color:rgb(13, 148, 8);"></i>
  <strong>Good for:</strong> analysis and data visualization
</span>   
Python is also commonly used in the field of neuroimaging: useful Python modules for neuroimaging include NiBabel, Nilearn, Nipype, PyNIfTI, PySurfer, PyTorch, and others. See Andy's Brain Blog [Python for Neuroimagers](https://andysbrainbook.readthedocs.io/en/latest/PythonForNeuroimagers/PythonForNeuroimagers_Overview.html) for a primer. 

**R/RStudio**   
<span style="display: inline-block; background-color: #f0f8ff; color: #333; border-radius: 12px; padding: 1px 5px; font-size: 0.9em; border: 1px solid #d0e7ff;">
  <i class="fa-regular fa-lightbulb" style="margin-right: 6px; color:rgb(13, 148, 8);"></i>
  <strong>Good for:</strong> data visualization
</span>   
Especially strong for statistical plots, often used in conjunction with analysis results.       
[Download page for R/RStudio <i class="fa fa-download"></i>](https://posit.co/download/rstudio-desktop/)


## Electroencaphalography (EEG) Data
The EEG Core of the HBCD Data Coordinating Center (HDCC) has a [GitHub repository](https://github.com/ChildDevLab/HBCD-data-release-notes) with file notes and scripts for working with the first HBCD EEG data release. We recommend all users to review this page for important resources. Users can contact us with any questions about working with the EEG data or using the GitHub repository at eegdata@umd.edu.