# HBCD Processing Pipelines
<p>
<div id="faq-qcrec" class="notification-banner" onclick="toggleCollapse(this)">
    <span class="emoji"><i class="fa-regular fa-lightbulb"></i></span>
    <span class="text">For full documentation on how each pipeline was used for HBCD processing, please visit the external <a href="https://hbcd-cbrain-processing.readthedocs.io/latest/">HBCD Processing</a> page</span>
</div>
</p>

## Overview
The **HBCD processing pipelines** are a collection of modular tools used to process data from the HBCD study. These pipelines are not exclusive to HBCD, but are general-purpose tools for analyzing a variety of data modalities, including magnetic resonance imaging (**MRI**), electroencephalography (**EEG**), magnetic resonance spectroscopy (**MRS**), and **biosensor data**. The pipelines are designed to be modular and flexible, allowing for customization to meet the specific needs of the HBCD study.

**The following processing pipelines were used for the HBCD study:**

<table style="width: 100%; border-collapse: collapse; table-layout: fixed; font-size: 15px">
  <thead>
    <tr>
      <th style="width: 10%; text-align: center;">Modality</th>
      <th style="width: 10%; text-align: center;">Processing Pipeline</th>
      <th style="width: 60%; text-align: center;">Pipeline Description</th>
    </tr>
  </thead>
  <tbody>
<tr>
<td colspan="1" rowspan="6">
<div>MRI</div>
</td>
<td><a href="https://mriqc.readthedocs.io/en/latest/">MRIQC</a></td>
<td style="word-wrap: break-word; white-space: normal;">Automated extraction of image quality metrics from structural and functional MRI data</td>
</tr>
<tr>
<td><a href="https://bibsnet.readthedocs.io/en/latest/">BIBSNet</a></td>
<td>Deep learning model for brain segmentation</td>
</tr>
<tr>
<td><a href="https://nibabies.readthedocs.io/en/latest/">infant-fMRIPrep</a></td>
<td style="word-wrap: break-word; white-space: normal;">Structural and functional MRI preprocessing pipeline</td>
</tr>
<tr>
<td><a href="https://xcp-d.readthedocs.io/en/latest/">XCP-D</a></td>
<td style="word-wrap: break-word; white-space: normal;">Functional MRI post-processing and noise regression pipeline</td>
</tr>
<tr>
<td><a href="https://qsiprep.readthedocs.io/en/latest/">QSIPrep</a> and <a href="https://qsirecon.readthedocs.io/en/latest/">QSIRecon</a></td>
<td style="word-wrap: break-word; white-space: normal;">Diffusion-weighted MRI (dMRI) data processing pipelines</td>
</tr>
<tr>
<td><a href="https://hbcd-symri-postproc.readthedocs.io/en/latest/index.html">qMRI Postproc</a></td>
<td style="word-wrap: break-word; white-space: normal;">Minimal post-processing for SyMRI synthetic images derived from QALAS acquisition</td>
</tr>
<tr>
<td>EEG</td>
<td><a href="https://docs-hbcd-made.readthedocs.io/en/latest/">HBCD-MADE</a></td>
<td style="word-wrap: break-word; white-space: normal;">Maryland Analysis of Developmental EEG (MADE) pipeline adapted for HBCD</td>
</tr>
<tr>
<td>MRS</td>
<td><a href="https://osprey-bids.readthedocs.io/en/latest/index.html">OSPREY-BIDS</a></td>
<td style="word-wrap: break-word; white-space: normal;">MRS data processing pipeline</td>
</tr>
<tr>
<td>Biosensor Data</td>
<td><a href="https://hbcd-motion-postproc.readthedocs.io/en/latest/">HBCD-Motion</a></td>
<td style="word-wrap: break-word; white-space: normal;">Leg movement sensor data processing</td>
</tr>
</tbody>
</table>

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

### Running an HBCD Processing Pipeline
To process HBCD study data using one of these pipelines, follow the installation and usage instructions on the specific pipeline's documentation page (links below).

**Choosing a Container System:**            
**Singularity/Apptainer** → Recommended for university-affiliated HPC clusters, where users lack administrative privileges.         
**Docker** → Preferred for personal computers due to its ease of installation (may require extra setup for HPC use).

All processing containers are available on [Docker Hub](https://hub.docker.com/).

## File Selection for Processing

With the exception of TB1 MRI and electrocardiogram (ECG) data, raw BIDS files are included in the release only if they were used in at least one processing pipeline, ensuring alignment with derived pipeline outputs. Since HBCD employs multiple pipelines — each with its own requirements — the released data represent the union of all files that meet at least one pipeline’s criteria. 

For some data categories, files are selected for processing based on pipeline-specific criteria detailed under *Quality Control Selection Information* in the [Tool Names](https://hbcd-cbrain-processing.readthedocs.io/latest/tool_details.html#tool-names) section of the HBCD Processing website. For imaging data that underwent [raw data quality control](../mri/qc.md#raw-mr-data-qc), only files that pass are included in the data release and utilized for data processing. All quality control information is stored in the `sub-<label>_ses-<label>_scans.tsv` file located in each BIDS session folder. This file is queried prior to processing to determine which files to include/exclude (e.g. based on thresholds for `QU_motion`, `acq_motion`, `brain_SNR`, etc.). 

There are some exceptions: for instance, MRS localizers are not excluded from processing based on QC alone. Data curation is instead performed during OSPREY-BIDS processing, which prioritizes localizer timing over QC (see details [here](https://osprey-bids.readthedocs.io/en/2.4.3/processing_pipeline_details.html)). 

When additional QC criteria apply, filtering typically occurs in two stages: first, using both manual and automated QC fields, and second, using only automated fields. For example, only the highest-quality T1w and T2w are selected for structural MRI processing when multiple scans passing QC are present. In this first release, all high-resolution T1w and T2w scans — and most QALAS acquisitions — were selected using `QU_Motion`, a manual assessment of motion artifacts.
