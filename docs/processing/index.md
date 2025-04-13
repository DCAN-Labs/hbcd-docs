# HBCD Processing Pipelines
<p>
<div id="faq-qcrec" class="notification-banner" onclick="toggleCollapse(this)">
    <span class="emoji"><i class="fa-regular fa-lightbulb"></i></span>
    <span class="text">For full documentation on how each pipeline was used for HBCD processing, please visit the external <a href="https://hbcd-cbrain-processing.readthedocs.io/latest/">HBCD Processing</a> page</span>
</div>
</p>

## Overview
The **HBCD processing pipelines** are a collection of modular tools used to process data from the HBCD study. These pipelines are not exclusive to HBCD, but are general-purpose tools for analyzing a variety of data modalities, including magnetic resonance imaging (MRI), electroencephalography (EEG), magnetic resonance spectroscopy (MRS), and biosensor data. The pipelines are designed to be modular and flexible, allowing for customization to meet the specific needs of the HBCD study.

## Pipeline Standards & Design
All pipelines used for HBCD data processing must adhere to [HBCD Processing & Analytic Software Standards](standards.md), which require, among other things:

- NMIND peer review and DOI publication for reproducibility.
- Compliance with the Brain Imaging Data Structure (BIDS) standard.
- Implementation as BIDS Apps ([Gorgolewski et al.,2017](https://doi.org/10.1371/journal.pcbi.1005209)), ensuring containerized, standardized processing.

### Why BIDS & BIDS Apps?
BIDS is a community-driven standard for organizing neuroimaging and behavioral data, making datasets **structured**, **shareable**, and **reproducible**. BIDS Apps are containerized applications that run on any system supporting [Docker](https://docs.docker.com/get-started/get-docker/) or [Apptainer](https://apptainer.org/docs/user/main/quick_start.html) (Singularity).

**Benefits of Containerization:**        
<i class="fa fa-check-square"></i> Ensures all software dependencies are included.      
<i class="fa fa-check-square"></i> Guarantees consistent processing environments across systems.        
<i class="fa fa-check-square"></i> Simplifies reproducibility and collaboration.        

## Running an HBCD Processing Pipeline
To process HBCD study data using one of these pipelines, follow the installation and usage instructions on the specific pipeline's documentation page (links below).

**Choosing a Container System:**            
**Singularity/Apptainer** → Recommended for university-affiliated HPC clusters, where users lack administrative privileges.         
**Docker** → Preferred for personal computers due to its ease of installation (may require extra setup for HPC use).

All processing containers are available on [Docker Hub](https://hub.docker.com/).

## Data Processing Pipelines
The following is a list of the processing pipelines used for the HBCD study:

### Magnetic Resonance Imaging (MRI)
<ul style="list-style-type: none; padding: 0; font-family: Arial, sans-serif;">
  <li style="margin-bottom: 10px;">
    <a href="https://mriqc.readthedocs.io/en/latest/" style="color: #2a7ae2; text-decoration: none; font-weight: bold;">
      MRIQC
    </a>: automated extraction of image quality metrics from structural and functional MRI data
  </li>
  <li style="margin-bottom: 10px;">
    <a href="https://bibsnet.readthedocs.io/en/latest/" style="color: #2a7ae2; text-decoration: none; font-weight: bold;">
      BIBSNet
    </a>: deep learning model for brain segmentation
  </li>
  <li style="margin-bottom: 10px;">
    <a href="https://nibabies.readthedocs.io/en/latest/" style="color: #2a7ae2; text-decoration: none; font-weight: bold;">
      infant-fMRIPrep
    </a>: structural and functional MRI preprocessing pipeline
  </li>
  <li style="margin-bottom: 10px;">
    <a href="https://xcp-d.readthedocs.io/en/latest/" style="color: #2a7ae2; text-decoration: none; font-weight: bold;">
      XCP-D
    </a>: functional MRI post-processing and noise regression pipeline
  </li>
  <li style="margin-bottom: 10px;">
    <a href="https://qsiprep.readthedocs.io/en/latest/" style="color: #2a7ae2; text-decoration: none; font-weight: bold;">
      QSIPrep
    </a> and 
    <a href="https://qsirecon.readthedocs.io/en/latest/" style="color: #2a7ae2; text-decoration: none; font-weight: bold;">
      QSIRecon
    </a>: diffusion-weighted MRI (dMRI) data processing pipelines
  </li>
  <li style="margin-bottom: 10px;">
    <a href="https://hbcd-symri-postproc.readthedocs.io/en/latest/index.html" style="color: #2a7ae2; text-decoration: none; font-weight: bold;">
      qMRI Postproc 
    </a>: minimal post-processing for SyMRI synthetic images derived from QALAS acquisition
  </li>
</ul>

### Electroencephalography (EEG)
<p style="list-style-type: none; padding: 0; font-family: Arial, sans-serif;">
    <a href="https://docs-hbcd-made.readthedocs.io/en/latest/" style="color: #2a7ae2; text-decoration: none; font-weight: bold;">
      HBCD-MADE
    </a>: Maryland Analysis of Developmental EEG (MADE) pipeline adapted for HBCD
</p>

### Magnetic Resonance Spectroscopy (MRS)       
<p style="list-style-type: none; padding: 0; font-family: Arial, sans-serif;">
    <a href="https://osprey-bids.readthedocs.io/en/latest/index.html" style="color: #2a7ae2; text-decoration: none; font-weight: bold;">
      OSPREY-BIDS
    </a>: MRS data processing pipeline
</p>

### Biosensor Data      
<p style="list-style-type: none; padding: 0; font-family: Arial, sans-serif;">
    <a href="https://hbcd-motion-postproc.readthedocs.io/en/latest/" style="color: #2a7ae2; text-decoration: none; font-weight: bold;">
      HBCD-Motion
    </a>: leg movement sensor data processing
</p>
