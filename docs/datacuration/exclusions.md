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

## Pipeline Criteria
 
Please see the criteria for file selection when processing [here](../instruments/processing/index.md#file-selection-for-processing).



