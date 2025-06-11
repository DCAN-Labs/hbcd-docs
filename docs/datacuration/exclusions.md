# Exclusion Criteria

## Imaging Acquisition Parameter Criteria
After converting MRI data to BIDS format, both the NIfTI and JSON files undergo additional verification to ensure data integrity. As part of this process, all images are checked to confirm they were acquired using a head coil before being included in the BIDS dataset.

Acquisition parameters can vary depending on the scanner vendor. For example, while the GE protocol acquires structural data at **0.8 mm isotropic resolution**, the current protocol/software version upsamples the data during reconstruction and DICOM creation, resulting in an **in-plane resolution of 0.5 × 0.5 × 0.8 mm³**. This will be adjusted in a future software upgrade.

To account for such variations, most inclusion criteria are defined as acceptable **ranges** rather than fixed values. The specific modality-based inclusion criteria are extracted directly from the image JSON files and evaluated accordingly.

<p>
<div id="acq-param-table" class="table-banner" onclick="toggleCollapse(this)">
  <span class="table-text">Acquisition Parameter Ranges for Data Release Eligibility</span>
  <span class="table-arrow">▸</span>
</div>
<div class="table-open-collapsible-content">
<table style="width: 100%; border-collapse: collapse; table-layout: fixed;">
  <thead>
    <tr>
      <th style="width: 100%; border-collapse: collapse; table-layout: fixed;">File</th>
      <th style="width: 100%; border-collapse: collapse; table-layout: fixed;">TR</th>   
      <th style="width: 100%; border-collapse: collapse; table-layout: fixed;">TE</th>        
      <th style="width: 100%; border-collapse: collapse; table-layout: fixed;">TI</th>    
      <th style="width: 100%; border-collapse: collapse; table-layout: fixed;">Slice Thickness</th>  
      <th style="width: 100%; border-collapse: collapse; table-layout: fixed;">Volume #</th>  
    </tr>
  </thead>
<tbody>
	<tr>
		<td>T1w</td>
		<td>2.3-2.41</td>
    <td>0.002-0.0035</td>
		<td>1.06-1.1</td>    
    <td>0.8</td>    
    <td>NA</td>    
	</tr>
	<tr>
		<td>T2w</td>
		<td>2.5-4.5</td>
    <td>0.09-0.15</td>
		<td>0.29-0.33</td>    
    <td>0.563-0.565</td>    
    <td>NA</td>
	</tr>  
	<tr>
		<td>MRS Localizer</td>
		<td>2.5-4.5</td>
    <td>0.09-0.15</td>
		<td>0.29-0.33</td>    
    <td>0.563-0.565</td>    
    <td>NA</td>
	</tr>   
	<tr>
		<td>Diffusion</td>
		<td>4.8</td>
    <td>0.0880-0.0980</td>
		<td>NA</td>    
    <td>1.7</td>    
    <td style="word-wrap: break-word; white-space: normal;">≥ 90 (AP + PA)</td>  
	</tr>  
	<tr>
		<td>EPI Fieldmap</td>
		<td>8.4-9.2</td>
    <td>0.064-0.0661</td>
		<td>2</td>    
    <td>0.563-0.565</td>    
    <td>NA</td>
	</tr>  
	<tr>
		<td>Functional</td>
		<td>1.725</td>
    <td>0.0369-0.0371</td>
		<td>NA</td>    
    <td>2</td>  
    <td>≥ 87 (~2.5 min)</td>   
	</tr>  
</tbody>
</table>
</div>
</p>

## Electroencephalography
EEG file inclusion in the data release is based in part on EEG capping quality: acquisitions with QC ratings of "excellent", "average", and "poor" are all included and those rated as "not usable" are excluded. See details of quality control procedures under [Data Measures > EEG > EEG Net Placement ("Capping Quality") Ratings](../measures/eeg/index.md#eeg-net-placement-capping-quality-ratings). Capping ratings are made available to users in the QC [instrument files](phenotypes.md) provided for each EEG task in the `phenotype/` folder (`eeg_qc_task-FACE.tsv`, `eeg_qc_task-MMN.tsv`, `eeg_qc_task-RS.tsv`, and `eeg_qc_task-VEP.tsv`).

## Processing Pipeline Criteria
With the exception of TB1 MRI and electrocardiogram (ECG) data, raw BIDS files are included in the release only if they were used in at least one processing pipeline, ensuring alignment with derived pipeline outputs. Since HBCD employs multiple pipelines — each with its own requirements — the released data represent the union of all files that meet at least one pipeline’s criteria. 

For some data categories, files are selected for processing based on pipeline-specific criteria detailed under *Quality Control Selection Information* in the [Tool Names](https://hbcd-cbrain-processing.readthedocs.io/latest/tool_details.html#tool-names) section of the HBCD Processing website. For imaging data that underwent [raw data quality control](../measures/mri/qc.md#raw-mr-data-qc), only files that pass are included in the data release and utilized for data processing. All quality control information is stored in the `sub-<label>_ses-<label>_scans.tsv` file located in each BIDS session folder. This file is queried prior to processing to determine which files to include/exclude (e.g. based on thresholds for `QU_motion`, `acq_motion`, `brain_SNR`, etc.). 

There are some exceptions: for instance, MRS localizers are not excluded from processing based on QC alone. Data curation is instead performed during OSPREY-BIDS processing, which prioritizes localizer timing over QC (see details [here](https://osprey-bids.readthedocs.io/en/2.4.3/processing_pipeline_details.html)). 

When additional QC criteria apply, filtering typically occurs in two stages: first, using both manual and automated QC fields, and second, using only automated fields. For example, only the highest-quality T1w and T2w are selected for structural MRI processing when multiple scans passing QC are present. In this first release, all high-resolution T1w and T2w scans — and most QALAS acquisitions — were selected using `QU_Motion`, a manual assessment of motion artifacts.


