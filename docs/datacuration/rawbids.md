# Raw BIDS Data
The `rawdata/` folder includes raw MR, EEG, and motion data converted to BIDS, organized under subject and session-specific directories. 

<pre class="folder-tree">
bids/
|__ rawdata/ 
    |__ sub-<span class="label">&lt;label&gt;</span>/
    |   |__ sub-<span class="label">&lt;label&gt;</span>_sessions.tsv
    |   |__ sub-<span class="label">&lt;label&gt;</span>_sessions.json
    |   |__ ses-<span class="label">&lt;label&gt;</span>/
    |       |__ anat/
    |       |__ dwi/
    |       |__ eeg/
    |       |__ fmap/
    |       |__ func/
    |       |__ motion/
    |       |__ mrs/
    |       |__ sub-<span class="label">&lt;label&gt;</span>_ses-<span class="label">&lt;label&gt;</span>_scans.tsv
    |       |__ sub-<span class="label">&lt;label&gt;</span>_ses-<span class="label">&lt;label&gt;</span>_scans.json
    |
    |__ dataset_description.json
    |__ participants.tsv
    |__ participants.json 
</pre>
In a large infant study, missing data is common, leading to variations in the number of folders and files available per subject and session. The HBCD acquisition spans multiple modalities, often collected at different times, with some acquisitions occurring on separate days even within the same modality. 

<p>
<div id="age" class="notification-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fa-regular fa-lightbulb"></i></span>
  <span class="text">Raw BIDS Data: Fields Reporting Age</span>
  <span class="arrow">▸</span>
</div>
<div class="collapsible-content">
<br>
<i>Age is reported with the following fields in the <code>sessions.tsv</code> and <code>scans.tsv</code> files for V02 onwards:</i>
<br>
<br>
<b>Gestational Age at Time of Scan</b> (<code>age_gestational</code>): Reported in days, gestational age is the time from the estimated date of delivery (EDD)—a proxy for conception based on the first day of the birth parent's last menstrual period (LMP)—to the scan date.
<br>
<br>
<b>Chronological Age at Time of Scan</b> (<code>age</code>): Reported in years (to three decimal places), chronological age is the time from birth (with the birthdate jittered up to 7 days to mitigate identification risks) to the scan date. It is calculated by dividing the total days elapsed (rounded down) by 365.25. Reporting in years, rather than months, ensures consistency across developmental stages (e.g., toddlerhood, childhood), while three-decimal precision compensates for birthdate adjustments, yielding values closer to actual age.
<br>
<br>
</div>
</p>

## Participant-, Session-, & Scan-Level Data
Participant-, session-, and scan-level data are stored in standardized `.tsv` files, accompanied by a `.json` sidecar file that defines the columns and describes the data fields, located in the `rawdata/` directory and its subdirectories:

- **Participant-level**: Stored in `rawdata/participants.tsv`, this file includes basic demographic and participant information (e.g., sex).
- **Session-level**: Stored in `sub-<label>_sessions.tsv` within each subject folder, this file includes session information such as collection site, the participant’s age at each session, and head size.
- **Scan-level**:  Each session folder includes a `sub-<label>_ses-<label>_scans.tsv` file with per-scan information including participant age at scan as well as all raw data QC scores (see [HBCD MR Quality Control Procedures](../measures/mri/qc.md)).

## Imaging & Spectroscopy
### Anatomical (anat/)
Anatomical files include T1- and T2-weighted MRI images, MRS localizer files (`acq-mrsLocAx` and `acq-mrsLocCor` indicate axial and coronal localizers, respectively), and Quantitative MRI QALAS files. 
<pre class="folder-tree">
anat/
|__ sub-<span class="label">&lt;label&gt;</span>_ses-<span class="label">&lt;label&gt;</span>_run-<span class="label">&lt;label&gt;</span>_T1w.nii.gz 
|__ sub-<span class="label">&lt;label&gt;</span>_ses-<span class="label">&lt;label&gt;</span>_run-<span class="label">&lt;label&gt;</span>_T1w.json
|__ sub-<span class="label">&lt;label&gt;</span>_ses-<span class="label">&lt;label&gt;</span>_run-<span class="label">&lt;label&gt;</span>_T2w.nii.gz
|__ sub-<span class="label">&lt;label&gt;</span>_ses-<span class="label">&lt;label&gt;</span>_run-<span class="label">&lt;label&gt;</span>_T2w.json
|__ sub-<span class="label">&lt;label&gt;</span>_ses-<span class="label">&lt;label&gt;</span>_acq-sub-<span class="placeholder">&lt;mrsLocAx|mrsLocCor&gt;</span>_run-<span class="label">&lt;label&gt;</span>_T2w.nii.gz 
|__ sub-<span class="label">&lt;label&gt;</span>_ses-<span class="label">&lt;label&gt;</span>_acq-sub-<span class="placeholder">&lt;mrsLocAx|mrsLocCor&gt;</span>_run-<span class="label">&lt;label&gt;</span>_T2w.json
|__ sub-<span class="label">&lt;label&gt;</span>_ses-<span class="label">&lt;label&gt;</span>_run-<span class="label">&lt;label&gt;</span>_inv-sub-<span class="placeholder">&lt;0|1|2|3|4&gt;</span>_QALAS.nii.gz
|__ sub-<span class="label">&lt;label&gt;</span>_ses-<span class="label">&lt;label&gt;</span>_run-<span class="label">&lt;label&gt;</span>_inv-sub-<span class="placeholder">&lt;0|1|2|3|4&gt;</span>_QALAS.json
</pre>
*Please see information about hardcoded fields for Philips and GE [here](overview.md/#hardcoded-fields-for-philips-ge) and post-BIDS conversion modifications made for QALAS [here](overview.md/#qalas-post-conversion-modifications).*

### Diffusion (dwi/)
Diffusion files include DWI runs (`*_dwi.nii.gz`) along with `bval` and `bvec` files, which provide the magnitudes and orientations of the diffusion gradients for each volume, respectively. Single-band reference files (`*_sbref.nii.gz`) are also included in the release. All images were acquired in both AP (`dir-AP`) and PA (`dir-PA`) phase encoding directions.
<pre class="folder-tree">
dwi/
|__ sub-<span class="label">&lt;label&gt;</span>_ses-<span class="label">&lt;label&gt;</span>_dir-<span class="placeholder">&lt;AP|PA&gt;</span>_run-<span class="label">&lt;label&gt;</span>_dwi.bval
|__ sub-<span class="label">&lt;label&gt;</span>_ses-<span class="label">&lt;label&gt;</span>_dir-<span class="placeholder">&lt;AP|PA&gt;</span>_run-<span class="label">&lt;label&gt;</span>_dwi.bvec
|__ sub-<span class="label">&lt;label&gt;</span>_ses-<span class="label">&lt;label&gt;</span>_dir-<span class="placeholder">&lt;AP|PA&gt;</span>_run-<span class="label">&lt;label&gt;</span>_dwi.nii.gz
|__ sub-<span class="label">&lt;label&gt;</span>_ses-<span class="label">&lt;label&gt;</span>_dir-<span class="placeholder">&lt;AP|PA&gt;</span>_run-<span class="label">&lt;label&gt;</span>_dwi.json
|__ sub-<span class="label">&lt;label&gt;</span>_ses-<span class="label">&lt;label&gt;</span>_dir-<span class="placeholder">&lt;AP|PA&gt;</span>_run-<span class="label">&lt;label&gt;</span>_sbref.json
|__ sub-<span class="label">&lt;label&gt;</span>_ses-<span class="label">&lt;label&gt;</span>_dir-<span class="placeholder">&lt;AP|PA&gt;</span>_run-<span class="label">&lt;label&gt;</span>_sbref.nii.gz
</pre>
*NOTE: Please see information about hardcoded fields for Philips and GE [here](overview.md/#hardcoded-fields-for-philips-ge).*

### Functional (func/) and Fieldmaps (fmap/) 
Functional files include BOLD functional resting state images under `func/`. Each functional acquisition has an associated pair of EPI fieldmaps acquired to use for distortion correction under `fmap/`, with AP (`dir-AP`) and PA (`dir-PA`) phase encoding directions. 

**Siemens, GE, and Philips additionally include B1 fieldmaps.** For Siemens, `acq-<anat|fmap>` denotes the anatomical (like) image and scaled flip angle map whereas for GE and Philips, `acq-tr<1|2>` denotes the first and second TR image (*see BIDS specification for quantitative MRI: [TB1TFL and TB1RFM](https://bids-specification.readthedocs.io/en/stable/appendices/qmri.html#tb1tfl-and-tb1rfm-specific-notes) and [TB1AFI](https://bids-specification.readthedocs.io/en/stable/appendices/qmri.html#tb1afi-specific-notes)*):

<pre class="folder-tree">
|__ func/
|   |__ sub-<span class="label">&lt;label&gt;</span>_ses-<span class="label">&lt;label&gt;</span>_task-rest_dir-PA_run-<span class="label">&lt;label&gt;</span>_bold.nii.gz
|   |__ sub-<span class="label">&lt;label&gt;</span>_ses-<span class="label">&lt;label&gt;</span>_task-rest_dir-PA_run-<span class="label">&lt;label&gt;</span>_bold.json
|
|__ fmap/
    |__ sub-<span class="label">&lt;label&gt;</span>_ses-<span class="label">&lt;label&gt;</span>_dir-AP_run-<span class="label">&lt;label&gt;</span>_epi.nii.gz
    |__ sub-<span class="label">&lt;label&gt;</span>_ses-<span class="label">&lt;label&gt;</span>_dir-AP_run-<span class="label">&lt;label&gt;</span>_epi.json
    |__ sub-<span class="label">&lt;label&gt;</span>_ses-<span class="label">&lt;label&gt;</span>_dir-PA_run-<span class="label">&lt;label&gt;</span>_epi.nii.gz
    |__ sub-<span class="label">&lt;label&gt;</span>_ses-<span class="label">&lt;label&gt;</span>_dir-PA_run-<span class="label">&lt;label&gt;</span>_epi.json
	|
	| <span class="hashtag"># SIEMENS ONLY:</span>
    |__ sub-<span class="label">&lt;label&gt;</span>_ses-<span class="label">&lt;label&gt;</span>_acq-anat_run-<span class="label">&lt;label&gt;</span>_TB1TFL.nii.gz
    |__ sub-<span class="label">&lt;label&gt;</span>_ses-<span class="label">&lt;label&gt;</span>_acq-anat_run-<span class="label">&lt;label&gt;</span>_TB1TFL.json
    |__ sub-<span class="label">&lt;label&gt;</span>_ses-<span class="label">&lt;label&gt;</span>_acq-fmap_run-<span class="label">&lt;label&gt;</span>_TB1TFL.nii.gz
    |__ sub-<span class="label">&lt;label&gt;</span>_ses-<span class="label">&lt;label&gt;</span>_acq-fmap_run-<span class="label">&lt;label&gt;</span>_TB1TFL.json
	|
	| <span class="hashtag"># GE AND PHILIPS ONLY:</span>
    |__ sub-<span class="label">&lt;label&gt;</span>_ses-<span class="label">&lt;label&gt;</span>_acq-tr1_run-<span class="label">&lt;label&gt;</span>_TB1AFI.nii.gz 
    |__ sub-<span class="label">&lt;label&gt;</span>_ses-<span class="label">&lt;label&gt;</span>_acq-tr1_run-<span class="label">&lt;label&gt;</span>_TB1AFI.json 
    |__ sub-<span class="label">&lt;label&gt;</span>_ses-<span class="label">&lt;label&gt;</span>_acq-tr2_run-<span class="label">&lt;label&gt;</span>_TB1AFI.nii.gz
    |__ sub-<span class="label">&lt;label&gt;</span>_ses-<span class="label">&lt;label&gt;</span>_acq-tr2_run-<span class="label">&lt;label&gt;</span>_TB1AFI.json
</pre>

*NOTE: Please see information about hardcoded fields for Philips and GE [here](overview.md/#hardcoded-fields-for-philips-ge).*

### MR Spectroscopy (mrs/)
MRS files include metabolite and water reference (`*_<svs|ref>.nii.gz`) data aqcuired via short-echo-time (TE = 35 ms) and HERCULES (spectral-edited, TE = 80 ms) (`acq-<shortTE|hercules>`). The JSON sidecar files include the dimensions of the NIfTI-MRS data array, holding different coil elements in dimension 5 and different transients in dimension 6.
<pre class="folder-tree">
mrs/
|__ sub-<span class="label">&lt;label&gt;</span>_ses-<span class="label">&lt;label&gt;</span>_acq-shortTE_run-<span class="label">&lt;label&gt;</span>_svs.nii.gz
|__ sub-<span class="label">&lt;label&gt;</span>_ses-<span class="label">&lt;label&gt;</span>_acq-shortTE_run-<span class="label">&lt;label&gt;</span>_svs.json
|__ sub-<span class="label">&lt;label&gt;</span>_ses-<span class="label">&lt;label&gt;</span>_acq-shortTE_run-<span class="label">&lt;label&gt;</span>_ref.nii.gz
|__ sub-<span class="label">&lt;label&gt;</span>_ses-<span class="label">&lt;label&gt;</span>_acq-shortTE_run-<span class="label">&lt;label&gt;</span>_ref.json
|__ sub-<span class="label">&lt;label&gt;</span>_ses-<span class="label">&lt;label&gt;</span>_acq-hercules_run-<span class="label">&lt;label&gt;</span>_svs.nii.gz
|__ sub-<span class="label">&lt;label&gt;</span>_ses-<span class="label">&lt;label&gt;</span>_acq-hercules_run-<span class="label">&lt;label&gt;</span>_svs.json
|__ sub-<span class="label">&lt;label&gt;</span>_ses-<span class="label">&lt;label&gt;</span>_acq-hercules_run-<span class="label">&lt;label&gt;</span>_ref.nii.gz
|__ sub-<span class="label">&lt;label&gt;</span>_ses-<span class="label">&lt;label&gt;</span>_acq-hercules_run-<span class="label">&lt;label&gt;</span>_ref.json
</pre>

## EEG
For EEG BIDS data, the specific **location of electrodes**, placed on either the head (`acq-eeg`) or chest (`acq-ecg`), is specified in the `*_electrodes.tsv` files following cartesian coordinates provided by the accompanying `*_coordsystem.json` file. For **task acquisitions**, the task is specified by `task-<label>`, with task options of `FACE`, `MMN`, `RS`, and `VEP` (see task details [here](../measures/eeg/index.md)).

<pre class="folder-tree">
eeg/
| <span class="hashtag"># LOCATION OF ELECTRODES:</span>
|__sub-<span class="label">&lt;label&gt;</span>_ses-<span class="label">&lt;label&gt;</span>_acq-ecg_space-CapTrak_electrodes.tsv
|__sub-<span class="label">&lt;label&gt;</span>_ses-<span class="label">&lt;label&gt;</span>_acq-ecg_space-CapTrak_coordsystem.json
|__sub-<span class="label">&lt;label&gt;</span>_ses-<span class="label">&lt;label&gt;</span>_acq-eeg_space-<span class="placeholder">&lt;CapTrak|CTF&gt;</span>_electrodes.tsv
|__sub-<span class="label">&lt;label&gt;</span>_ses-<span class="label">&lt;label&gt;</span>_acq-eeg_space-<span class="placeholder">&lt;CapTrak|CTF&gt;</span>_coordsystem.json
|
| <span class="hashtag"># TASK ACQUISITIONS:</span>
|__sub-<span class="label">&lt;label&gt;</span>_ses-<span class="label">&lt;label&gt;</span>_task-<span class="placeholder">&lt;FACE|MMN|RS|VEP&gt;</span>_acq-<span class="placeholder">&lt;eeg|ecg&gt;</span>_channels.tsv
|__sub-<span class="label">&lt;label&gt;</span>_ses-<span class="label">&lt;label&gt;</span>_task-<span class="placeholder">&lt;FACE|MMN|RS|VEP&gt;</span>_acq-<span class="placeholder">&lt;eeg|ecg&gt;</span>_eeg.json
|__sub-<span class="label">&lt;label&gt;</span>_ses-<span class="label">&lt;label&gt;</span>_task-<span class="placeholder">&lt;FACE|MMN|RS|VEP&gt;</span>_acq-<span class="placeholder">&lt;eeg|ecg&gt;</span>_eeg.set
|__sub-<span class="label">&lt;label&gt;</span>_ses-<span class="label">&lt;label&gt;</span>_task-<span class="placeholder">&lt;FACE|MMN|RS|VEP&gt;</span>_acq-<span class="placeholder">&lt;eeg|ecg&gt;</span>_events.tsv
|__sub-<span class="label">&lt;label&gt;</span>_ses-<span class="label">&lt;label&gt;</span>_task-<span class="placeholder">&lt;FACE|MMN|RS|VEP&gt;</span>_acq-<span class="placeholder">&lt;eeg|ecg&gt;</span>_events.json
|
|__ sourcedata/
    |__ sub-<span class="label">&lt;label&gt;</span>_ses-<span class="label">&lt;label&gt;</span>_task-<span class="placeholder">&lt;FACE|MMN|RS|VEP&gt;</span>_acq-eeg_flags.json
    |__ sub-<span class="label">&lt;label&gt;</span>_ses-<span class="label">&lt;label&gt;</span>_task-<span class="placeholder">&lt;FACE|MMN|RS|VEP&gt;</span>_acq-eeg_impedances.json
    |__ sub-<span class="label">&lt;label&gt;</span>_ses-<span class="label">&lt;label&gt;</span>_task-<span class="placeholder">&lt;FACE|MMN|RS|VEP&gt;</span>_acq-eeg_eventlogs.txt
</pre>

<ul>
The accompanying <code>sourcedata/</code> files include:
<li>Information about quality control flags and acquisition (<code>*_flags.json</code>- see QC details <a href="../../measures/eeg/#quality-control">here</a>)</li>
<li>Impedance values used to ensure good electrode contact (<code>*_impedence.json</code>)</li>
<li>Task stimuli presentations (<code>*_eventlogs.txt</code>)</li>
</ul>


## Motion
Axivity AX6 sensor data provided in the data release include `_motion.tsv` sensor recordings with corresponding `*_channels.tsv` files that describe each column of of the motion file. The acquisition (`acq-`) label for the calibration files is `calibration` while the label for the 72-hr data files is `primary`. The `task` label will be either `LeftLegMovement` or `RightLegMovement` for sensors placed on the left or right leg. Each `.tsv` file is accompanied by a JSON sidecar containing recording-related metadata: 

<pre class="folder-tree">
motion/  
|__ sub-<span class="label">&lt;label&gt;</span>_ses-<span class="label">&lt;label&gt;</span>_task-<span class="label">&lt;label&gt;</span>_tracksys-imu_acq-<span class="label">&lt;label&gt;</span>_motion.tsv  
|__ sub-<span class="label">&lt;label&gt;</span>_ses-<span class="label">&lt;label&gt;</span>_task-<span class="label">&lt;label&gt;</span>_tracksys-imu_acq-<span class="label">&lt;label&gt;</span>_motion.json
|__ sub-<span class="label">&lt;label&gt;</span>_ses-<span class="label">&lt;label&gt;</span>_task-<span class="label">&lt;label&gt;</span>_tracksys-imu_acq-<span class="label">&lt;label&gt;</span>_channels.tsv  
|__ sub-<span class="label">&lt;label&gt;</span>_ses-<span class="label">&lt;label&gt;</span>_task-<span class="label">&lt;label&gt;</span>_tracksys-imu_acq-<span class="label">&lt;label&gt;</span>_channels.json
</pre>