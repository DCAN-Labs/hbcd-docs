# Overview

The full MRI Parameters can be found on the [HBCD Study webpage](https://hbcdstudy.org/study-protocols/) under Brain Measurement Tools.

## Quality Control & Known Issues       
Quality control of the MRI images can be found in the `scans.tsv` file in the session folder. The raw QC process involves reviewing unprocessed or lightly processed MRI data to identify and exclude data with severe artifacts from further processing. An initial protocol compliance check is performed by extracting information from DICOM headers and checking for common issues and protocol deviations, such as missing files or incorrect patient orientation. Automated QC metrics are calculated from the image data. A deep learning model estimates motion artifacts for structural scans (T1w, T2w, and qMRI), while metrics related to motion, bad frames, line artifacts, and FOV (field of view) cutoff are assessed for dMRI, fMRI, and field maps. A subset of series are selected for manual review based on multivariate prediction and Bayesian classifiers using the automated metrics. During the manual review, data quality is scored based on the severity of specific artifacts. For structural scans, motion artifacts are scored based on perceived severity on a scale of 0 to 3. Scores indicate no artifact (0), mild (1), moderate (2), or severe (3). Other artifacts, such as unusual intensity inhomogeneity or ghosting are noted by the reviewer. For dMRI, fMRI, and field maps, scored artifacts include susceptibility artifacts, FOV cutoff, and line artifacts. Other artifacts may be noted. Series with severe artifacts that clearly compromise data usability are rejected (QC=0). 

After conversion to [BIDS format](../../datacuration/imaging.md), the MRI protocol was checked to further ensure the quality of the data. For example, a check to ensure that all images are acquired using a head coil was performed before including it in the BIDS dataset. Other exclusion criteria include (*click to expand*):

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

<details class="collapsible references">
  <summary class="references">References</summary>
 <ul>
<li>Dean III, D. C., Tisdall, M. D., Wisnowski, J. L., Feczko, E., Gagoski, B., Alexander, A. L., ... &amp; HBCD MRI Working Group. (2024). Quantifying brain development in the HEALthy Brain and Child Development (HBCD) Study: The magnetic resonance imaging and spectroscopy protocol. <em>Developmental Cognitive Neuroscience</em>, 70, 101452. <a href="https://doi.org/10.1016/j.dcn.2024.101452">https://doi.org/10.1016/j.dcn.2024.101452</a></li>
</ul>
</details>