# HBCD Processing Pipelines
<p>
<div id="faq-qcrec" class="notification-banner" onclick="toggleCollapse(this)">
    <span class="emoji"><i class="fa-regular fa-lightbulb"></i></span>
    <span class="text">For full documentation on how each pipeline was used for HBCD processing, please visit the external <a href="https://hbcd-cbrain-processing.readthedocs.io/latest/">HBCD Processing</a> page</span>
</div>
</p>

## Overview
The HBCD Processing Pipelines are a collection of tools used to process and analyze data from the Healthy Brain Cognitive Development (HBCD) study. The pipelines are designed to process data from a variety of modalities, including magnetic resonance imaging (MRI), electroencephalogram (EEG), magnetic resonance spectroscopy (MRS), and biosensor data. The pipelines are designed to be modular and flexible, allowing for customization to meet the specific needs of the HBCD study.

Per the [HBCD Processing & Analytic Software Standards](standards.md), all pipelines must undergo NMIND peer review and be published with a DOI. The pipelines must also be containerized and compatible with the Brain Imaging Data Structure (BIDS) standard input data. **ADD MORE ABOUT CONTAINERS HERE**

Several of the processing pipelines query the `scans.tsv` (see [Scan-Level Data](../datacuration/rawbids.md#scan-level-data)) to determine which files to include/exclude for processing. The criteria used are listed under the 'Quality Control Selection Information' under [Tool Names](https://hbcd-cbrain-processing.readthedocs.io/latest/tool_details.html#tool-names) on the HBCD Processing page. Please visit the [HBCD Processing](https://hbcd-cbrain-processing.readthedocs.io/latest/) webpage for full documentation on how each of the following pipelines was used for HBCD processing.

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

### Electroencephalogram (EEG)
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
