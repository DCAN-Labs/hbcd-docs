# Imaging Data Curation & BIDS Conversion
## BIDS Conversion
With the exception of [MRS](#mr-spectroscopy), raw image files are converted to BIDS standard formatting using an [HBCD-customized version](https://github.com/rordenlab/dcm2niix/tree/c5caaa9f858b704b61d3ff4a7989282922dd712e) of the [dcm2niix](https://github.com/rordenlab/dcm2niix) tool. The resulting data structure relevant to imaging data is as follows. Below we expand on the file contents of each modality folder within the session folder: 

```
assembly_bids/ 
|__ participants.tsv
|__ participants.json 
|__ sub-<label>/
|   |__ sub-<label>_sessions.tsv
|   |__ sub-<label>_sessions.json
|   |__ ses-<label>/
|       |__ anat/
|       |__ dwi/
|       |__ fmap/
|       |__ func/
|       |__ sub-<label>_ses-<label>_scans.tsv
|       |__ sub-<label>_ses-<label>_scans.json
```

### Anatomical
Anatomical files include T1- and T2-weighted MRI images, MRS localizer files (`acq-mrsLocAx` and `acq-mrsLocCor` indicate axial and coronal localizers, respectively), and Quantitative MRI QALAS files:
```
...
|   |__ ses-<label>/
|       |__ anat/
|       |   |__ sub-<label>_ses-<label>_run-<label>_T1w.nii.gz 
|       |   |__ sub-<label>_ses-<label>_run-<label>_T1w.json
|       |   |__ sub-<label>_ses-<label>_run-<label>_T2w.nii.gz
|       |   |__ sub-<label>_ses-<label>_run-<label>_T2w.json
|       |   |__ sub-<label>_ses-<label>_acq-<mrsLocAx/mrsLocCor>_run-<label>_T2w.nii.gz 
|       |   |__ sub-<label>_ses-<label>_acq-<mrsLocAx/mrsLocCor>_run-<label>_T2w.json
|       |   |__ sub-<label>_ses-<label>_run-<label>_inv-<label>_QALAS.nii.gz
|       |   |__ sub-<label>_ses-<label>_run-<label>_inv-<label>_QALAS.json
```

### Diffusion

Diffusion files include DWI runs (`*_dwi.nii.gz`) along with `bval` and `bvec` files, which provide the magnitudes and orientations of the diffusion gradients for each volume, respectively. Single-band reference files (`*_sbref.nii.gz`) are also included in the release. All images were acquired in both AP (`dir-AP`) and PA (`dir-PA`) phase encoding directions.
```
...
|   |__ ses-<label>/
|       |__ dwi/
|       |   |__ sub-<label>_ses-<label>_dir-<AP/PA>_run-<label>_dwi.bval
|       |   |__ sub-<label>_ses-<label>_dir-<AP/PA>_run-<label>_dwi.bvec
|       |   |__ sub-<label>_ses-<label>_dir-<AP/PA>_run-<label>_dwi.nii.gz
|       |   |__ sub-<label>_ses-<label>_dir-<AP/PA>_run-<label>_dwi.json
|       |   |__ sub-<label>_ses-<label>_dir-<AP/PA>_run-<label>_sbref.json
|       |   |__ sub-<label>_ses-<label>_dir-<AP/PA>_run-<label>_sbref.nii.gz
```

### Functional & EPI Fieldmaps
Functional files include BOLD functional resting state images under `func/` and EPI fieldmaps acquired acquired in AP (`dir-AP`) and PA (`dir-PA`) phase encoding directions under `fmap/`:
```
...
|   |__ ses-<label>/
|       |__ fmap/
|       |   |__ sub-<label>_ses-<label>_dir-AP_run-<label>_epi.nii.gz
|       |   |__ sub-<label>_ses-<label>_dir-AP_run-<label>_epi.json
|       |   |__ sub-<label>_ses-<label>_dir-PA_run-<label>_epi.nii.gz
|       |   |__ sub-<label>_ses-<label>_dir-PA_run-<label>_epi.json
|       |
|       |__ func/
|       |   |__ sub-<label>_ses-<label>_task-rest_dir-PA_run-<label>_bold.nii.gz
|       |   |__ sub-<label>_ses-<label>_task-rest_dir-PA_run-<label>_bold.json
```

### Additional B1 Fieldmaps for Siemens, GE, and Philips
Siemens, GE, and Philips will include additional files under `fmap/` due to acquisition of B1 fieldmaps, which were converted following the BIDS specification for quantitative MRI (see BIDS specific notes for [TB1TFL and TB1RFM](https://bids-specification.readthedocs.io/en/stable/appendices/qmri.html#tb1tfl-and-tb1rfm-specific-notes) and [TB1AFI](https://bids-specification.readthedocs.io/en/stable/appendices/qmri.html#tb1afi-specific-notes)). 

**Siemens** (`acq-<anat/fmap>` denotes the anatomical (like) image and scaled flip angle map):
```
...
|   |__ ses-<label>/
|       |__ fmap/
|           |__ sub-<label>_ses-<label>_acq-anat_run-<label>_TB1TFL.nii.gz
|           |__ sub-<label>_ses-<label>_acq-anat_run-<label>_TB1TFL.json
|           |__ sub-<label>_ses-<label>_acq-fmap_run-<label>_TB1TFL.nii.gz
|           |__ sub-<label>_ses-<label>_acq-fmap_run-<label>_TB1TFL.json
```
<br>
**GE and Philips** (`acq-tr<1/2>` denotes the first and second TR image):
```
...
|   |__ ses-<label>/
|       |__ fmap/
|     GE/PHILIPS ONLY:
|           |__ sub-<label>_ses-<label>_acq-tr1_run-<label>_TB1AFI.nii.gz 
|           |__ sub-<label>_ses-<label>_acq-tr1_run-<label>_TB1AFI.json 
|           |__ sub-<label>_ses-<label>_acq-tr2_run-<label>_TB1AFI.nii.gz
|           |__ sub-<label>_ses-<label>_acq-tr2_run-<label>_TB1AFI.json
```

### MR Spectroscopy
For MRS, vendor-specific raw data formats (Siemens `.dat`; Philips data/list; GE P-file) were converted to BIDS using [spec2nii v0.7.0](https://github.com/wtclarke/spec2nii). Output files include metabolite and water reference (`*_<svs/ref>.nii.gz`) data aqcuired via short-echo-time (TE = 35 ms) and HERCULES (spectral-edited, TE = 80 ms) (`acq-<shortTE/hercules>`). The JSON sidecar files include the dimensions of the NIfTI-MRS data array, holding different coil elements in dimension 5 and different transients in dimension 6.
```
...
|       |__ mrs/
|       |   |__ sub-<label>_ses-<label>_acq-shortTE_run-<label>_svs.nii.gz
|       |   |__ sub-<label>_ses-<label>_acq-shortTE_run-<label>_svs.json
|       |   |__ sub-<label>_ses-<label>_acq-shortTE_run-<label>_ref.nii.gz
|       |   |__ sub-<label>_ses-<label>_acq-shortTE_run-<label>_ref.json
|       |   |__ sub-<label>_ses-<label>_acq-hercules_run-<label>_svs.nii.gz
|       |   |__ sub-<label>_ses-<label>_acq-hercules_run-<label>_svs.json
|       |   |__ sub-<label>_ses-<label>_acq-hercules_run-<label>_ref.nii.gz
|       |   |__ sub-<label>_ses-<label>_acq-hercules_run-<label>_ref.json
```

## Post-Conversion Modifications
<p>
<details>
<summary><b>Hard-coded fields for missing/incorrect header information</b></summary>
<br>
In some cases, <i>dcm2niix</i> conversion led to missing or incorrectly configured NIfTI/JSON metadata. To address these issues, the headers for the file types listed below were hard-coded after conversion. These hard-coded values are also documented in the <i>HardCodedValues</i> field of the corresponding JSON sidecar file.
<br>
<br>
<ul>
<b>Philips</b>
	<li>T1W: <i>RepetitionTime</i></li>
	<li>DWI: <i>PhaseEncodingDirection</i>, <i>TotalReadoutTime</i>, & <i>SliceTiming</i> (<i>SmallDelta</i> & <i>LargeDelta</i> also added)</li>
	<li>EPI: <i>PhaseEncodingDirection</i> & <i>TotalReadoutTime</i></li>
	<li>BOLD:	<i>PhaseEncodingDirection</i>, <i>TotalReadoutTime</i>, & <i>SliceTiming</i></li>
<br>
<b>GE</b>
	<li>T1W: <i>RepetitionTime</i></li>
</ul>
</details>
</p>

<details>
<summary><b>Quantitative MRI</b></summary><br>
Depending on the scanner manufacturer, <i>dcm2niix</i> conversion for QALAS produced either five 3D NIfTI files or a single 4D NIfTI file with five volumes (as well as missing JSON header information). To standardize the output, all <i>dcm2niix</i>-derived QALAS series were converted into five separate NIfTI files, each corresponding to a different inversion time (labeled using the <i>inv-&lt;label&gt;</i> BIDS entity). The associated JSON sidecar was then updated with the following:

<br>
<br>

1.  <i>T2Prep</i> field of <i>inv-0</i> QALAS file hard-coded to 0.10 (Siemens), 0.09 (GE), and 0.10 (Philips)

<br>
<br>

<p>2.  <i>InversionTime</i> values (sec) for QALAS files hard-coded as follows for each manufacturer:</b></p>

<table>
  <tr>
  <th width="100">QALAS file</th>
  <th width="100">Siemens</th>
  <th width="100">GE</th>
  <th>Philips</th>
  </tr>
  <tbody>
    <tr>
    <td>inv-0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    </tr>
    <tr>
    <td>inv-1</td>
    <td>0.1</td>
    <td>0.119300</td>
    <td>0.115000</td>
    </tr>
    <tr>
    <td>inv-2</td>
    <td>1</td>
    <td>1.0191834</td>
    <td>1.010522</td>
    </tr>
    <tr>
    <td>inv-3</td>
    <td>1.9</td>
    <td>1.919068</td>
    <td>1.906045</td>
    </tr>
    <tr>
    <td>inv-4</td>
    <td>2.8</td>
    <td>2.818952</td>
    <td>2.801567</td>
    </tr>
  </tbody>
</table>
</details><br>



