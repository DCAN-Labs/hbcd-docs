# Exclusion Criteria 

## Imaging, Spectroscopy, EEG, & Accelerometry

#### Acquisition Parameter Criteria
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

#### Electroencephalography
EEG file inclusion in the data release is based in part on EEG capping quality: acquisitions with QC ratings of "excellent", "average", and "poor" are all included and those rated as "not usable" are excluded. See details of quality control procedures under [Data Measures > EEG > EEG Net Placement ("Capping Quality") Ratings](../measures/eeg/index.md#eeg-net-placement-capping-quality-ratings). Capping ratings are made available to users in the QC [instrument files](phenotypes.md#instrument-data) provided for each EEG task in the `phenotype/` folder (`eeg_qc_task-FACE.tsv`, `eeg_qc_task-MMN.tsv`, `eeg_qc_task-RS.tsv`, and `eeg_qc_task-VEP.tsv`).

#### Processing Pipeline Criteria
With the exception of TB1 MRI and electrocardiogram (ECG) data, raw BIDS files are included in the release only if they were used in at least one processing pipeline, ensuring alignment with derived pipeline outputs. Since HBCD employs multiple pipelines — each with its own requirements — the released data represent the union of all files that meet at least one pipeline’s criteria. 

For some data categories, files are selected for processing based on pipeline-specific criteria detailed under *Quality Control Selection Information* in the [Tool Names](https://hbcd-cbrain-processing.readthedocs.io/latest/tool_details.html#tool-names) section of the HBCD Processing website. For imaging data that underwent [raw data quality control](../measures/mri/qc.md#raw-mr-data-qc), only files that pass are included in the data release and utilized for data processing. There are some exceptions: for instance, MRS localizers are not excluded from processing based on QC alone. Data curation is instead performed during OSPREY-BIDS processing, which prioritizes localizer timing over QC (see details [here](https://osprey-bids.readthedocs.io/en/2.4.3/processing_pipeline_details.html)). All quality control information is stored in the `sub-<label>_ses-<label>_scans.tsv` file located in each BIDS session folder. 

When additional QC criteria apply, filtering typically occurs in two stages: first, using both manual and automated QC fields, and second, using only automated fields. For example, only the highest-quality T1w and T2w are selected for structural MRI processing when multiple scans passing QC are present. In this first release, all high-resolution T1w and T2w scans — and most QALAS acquisitions — were selected using `QU_Motion`, a manual assessment of motion artifacts.

## Tabulated Instrument Data

### General Rules Applied to All Data
- For all participants with only one active V01 visit, sex is changed from "Male/Female" to “Other”
- All empty strings (“”) or missing values are replaced with the default ReproSchema-compliant string “n/a”
- Some fields can have out-of-range values considered “extreme” that are changed to “n/a." Filtered fields are listed under [Filtered Out-Of-Range Field Values](#filtered-values).
  
### Static Element Exclusions
Static elements are precisely identified hard-coded elements such as participants, instruments, and instrument fields. The current data release excludes participants with a 'Postnatal Recruitment' visit as well as Multiple Birth Participants (to be included in the [interim release](../changelog/pending.md#release-11-release-date-tba)). Excluded instruments and instrument fields are as follows:

<div id="static-exclusions-dropdown" class="table-banner" onclick="toggleCollapse(this)">
    <span class="table-text">Excluded Instruments</span>
  <span class="notification-arrow">▸</span>
</div>
<div class="notification-collapsible-content">
<ul>
    <li>Biosensor Receipt Form ('sens_ch_rcpt')</li>
    <li>EEG Acquisition Checklists
    <ul>
        <li>Form ('eeg_ch_chkl')</li>
        <li>Form Reattempt - 1 ('eeg_ch_chkl_1')</li>
        <li>Form Reattempt - 2 ('eeg_ch_chkl_2')</li>
    </ul>
    <li>GABI Setup/Receipt
        <ul>
        <li>'nt_pa_gabi_setup'  </li>
        <li>'nt_pa_gabi_rcpt'  </li>
        </ul>
    </li>
    <li>ERICA forms
        <ul>
        <li>'mh_cg_erica_3_7m'  </li>
        <li>'mh_cg_erica_7_9m'  </li>
        <li>'mh_cg_erica_fcm_adm_3_7m'  </li>
        <li>'mh_cg_erica_fcm_adm_7_9m'  </li>
        </ul>
    </li>
    <li>MRI Checklists
        <ul>
        <li>Data Summary Form ('mri_ra_chkl_data')  </li>
        <li>Scan Session Summary Form ('mri_ra_chkl_scan')  </li>
        </ul>
    </li>
    <li>MRI Pre/Post Scan Prep ('mri_ra_prep')</li>
    <li>NIH Baby ToolBox ('ncl_ch_nbtb')</li>
    <li>Participant Feedback Form ('adm_cg_fb')</li>
    <li>RA Feedback ('adm_ra_fb')</li>
    <li>Participant Alerts ('admin_alert')</li>
    <li>TLFB (Timeline Follow Back) Summary Parser ('pex_ch_tlfb')</li>
    <li>Visit Level Data ('adm_fd_visitdata')</li>
    <li>Visit start ('visit_start')</li>
    <li>Urgent Events ('adm_fd_urgent')</li>
    <li>Transitions in Care Questionnaire ('sed_cg_tic')</li>
</ul>
</div>

<div id="static-exclusions-fields" class="table-banner" onclick="toggleCollapse(this)">
    <span class="table-text">Excluded Instrument Fields</span>
  <span class="notification-arrow">▸</span>
</div>
<div class="notification-collapsible-content">
<ul>
    <li>Examiner ('Examiner’)  </li>
    <li>Date of Birth (‘DOB’)  </li>
    <li>Informant (‘informant’)  </li>
    <li>Validity (‘validity’)  </li>
    <li>Duration (‘duration’)  </li>
    <li>Window Difference (‘window_difference’)  </li>
    <li>Start timestamp (‘timestamp_start’)  </li>
    <li>Stop timestamp (‘timestamp_stop’)  </li>
    <li>REDCap timestamp (‘timestamp_redcap_locked’)  </li>
    <li>Visit Data ('visit_stage' removed from the 'visit_data' category)  </li>
    <li>'Height/Weight/Head Circumference' ('ph_ch_anthro') - BMI-related fields removed  </li>
    <li>Breast Feeding History ('ph_cg_phx_i_bfh') - All fields except '001' excluded  </li>
    <li>Clinical Alerts  </li>
    <li>REDCap Complete status ('complete')  </li>
    <li>Scannable codes (BioSamples codes, tracking Nos, etc...)  </li>
    <li>Line fields</li>
</ul>
</div>

<div id="filtered-values" class="table-banner" onclick="toggleCollapse(this)">
    <span class="table-text">Filtered Out-Of-Range Field Values</span>
  <span class="notification-arrow">▸</span>
</div>
<div class="notification-collapsible-content">
<p>Some fields can have out-of-range values considered “extreme.” Values outside of the valid ranges listed for the instruments below were filtered, i.e. changed to "n/a."</p>
<table style="width: 100%; border-collapse: collapse; table-layout: fixed;">
  <thead>
    <tr>
      <th style="border: 1px solid #ddd; padding: 8px; text-align: left;">Instrument</th>
      <th style="border: 1px solid #ddd; padding: 8px; text-align: left;">Field</th>
      <th style="border: 1px solid #ddd; padding: 8px; text-align: left;">Valid Range</th>
    </tr>
  </thead>
<tbody>        
<td colspan="1" rowspan="4" style="word-wrap: break-word; white-space: normal;">Growth (<code>ph_ch_anthro</code>)</td>
    <tr>
        <td>Length (<code>len_001_i_03</code>)</td>
        <td>30 to 130 cm</td>
    </tr>     
    <tr>
        <td>Head Circumference (<code>head_001_i_03</code>)</td>
        <td>25 to 55 cm</td>
    </tr>          
    <tr>
        <td>Weight (<code>wei_001_i_03</code>)</td>
        <td>0.5 to 30 kg</td>
    </tr>         
<td colspan="1" rowspan="5" style="word-wrap: break-word; white-space: normal;">Healthv2 Inf (<code>pex_bm_healthv2_inf</code>)</td>
    <tr>
        <td><code>001_i_01</code></td>
        <td>≤ 16</td>
    </tr>     
    <tr>
        <td><code>001_i_02</code></td>
        <td>≤ 66</td>
    </tr>     
    <tr>
        <td><code>002</code></td>
        <td>12 - 51</td>
    </tr>     
    <tr>
        <td><code>002_i_01</code></td>
        <td>30 - 130</td>
    </tr>     
</tbody>
</table>
</div>
<br>

### Dynamic Element Exclusions
<div id="dynamic-exclusions-dropdown" class="table-banner" onclick="toggleCollapse(this)">
    <span class="table-text">Dynamic Element Exclusions</span>
  <span class="notification-arrow">▸</span>
</div>
<div class="notification-collapsible-content">
<ul>
<b>Participant Filters:</b>
    <li>No brain rating or brain rating noted “abnormal” are not selected</li>
    <li>Only active participants and sessions are selected</li>
    <li>Participants from Data Coordination Center (DCC) and University of Florida (UFL) sites are not selected</li>
    <li>Only participants with PSCIDs starting with “CH” are selected (excluding all test participants e.g. QI, YI, XI, PI)</li>
</ul>
<ul><b>Visit Filters:</b> Only visits whose 'LaunchPad Complete' Status was set to 'Complete' before July 1st, 2024 are included</ul>
<ul>
<b>Domain Filters:</b>
    <li>BioSpecimens</li>
    <li>Geocoding data</li>
    <li>Transition in Care</li>
    <li>REDCap surveys filled out directly in LORIS (Identified based on LORIS 'Examiner' field not set to 'REDCap')</li>
</ul>
</div>

