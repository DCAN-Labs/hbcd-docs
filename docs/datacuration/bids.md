# Overview: Data Curation & BIDS Standardization

## Brain Imaging Data Structure
As much as possible, HBCD processing utilizes the [Brain Imaging Data Structure](https://bids-specification.readthedocs.io/en/stable/) (BIDS) standard for data organization. At a high level, the HBCD BIDS structure will appear as follows:

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
|       |__ eeg/
|       |__ fmap/
|       |__ func/
|       |__ motion/
|       |__ mrs/
|       |__ sub-<label>_ses-<label>_scans.tsv
|       |__ sub-<label>_ses-<label>_scans.json
```
In a large infant study, missing data is common, leading to variations in the number of folders and files available per subject and session. The HBCD acquisition spans multiple modalities, often collected at different times, with some acquisitions occurring on separate days even within the same modality. Participant-, session-, and scan-level data is captured by `participants.tsv`, `sessions.tsv`, and `scans.tsv` files respectively, each accompanied by JSON files with column descriptions and field definitions.

## Data Curation & Exclusion Criteria
Quality control metrics for raw MRI images, generated according to the procedures outlined [here](../measures/mri/overview.md), are provided in the `scans.tsv` file within the session folder. Following conversion to BIDS format, the MRI NIfTI and JSON files undergo additional quality checks to ensure data integrity. For instance, all images were verified to be acquired using a head coil before inclusion in the BIDS dataset. Additional exclusion criteria for each imaging modality are detailed below.

<p>
<details>
<summary>Exclusion Criteria</summary>
<br>

<ul>
<u>T1w:</u>
  <li>TR outside of range 2.3-2.41</li>
  <li>TE outside of range 0.002-0.0035</li>
  <li>TI outside of range 1.06-1.1</li>
  <li>Slice thickness not being 0.8</li>
  <br>

<u>T2w and MRS Localizer:</u>
  <li>TR outside of range 2.5-4.5</li>
  <li>TE outside of range 0.09-0.15</li>
  <li>TI outside of range 0.29-0.33</li>
  <li>Slice thickness outside of range 0.563-0.565</li>
  <br>

<u>Diffusion:</u>
  <li>TR not being set to 4.8</li>
  <li>TE outside of range 0.0880-0.0980</li>
  <li>Slice thickness not being set to 1.7</li>
  <li>The total number of volumes between DWI AP and DWI PA is below 90 volumes</li>
  <br>

<u>EPI Fieldmap:</u>
  <li>TR outside of range 8.4-9.2</li>
  <li>TE outside of range 0.064-0.0661</li>
  <li>TI not being set to 2</li>
  <li>Slice thickness outside of range 0.563-0.565</li>
  <br>

<u>Functional:</u>
  <li>TR not being set to 1.725</li>
  <li>TE outside of range 0.0369-0.0371</li>
  <li>Slice thickness not being set to 2</li>
  <li>fMRI is shorter than 87 volumes (approximately less than 2.5 minutes long)</li>
</ul>
</details>
</p>