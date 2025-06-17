# HBCD MR Quality Control Procedures

## Raw MR Data QC
Quality control (QC) procedures involve automated and manual methods to evaluate unprocessed or minimally processed MRI data for issues such as incorrect acquisition parameters, imaging artifacts, or corrupted files. The purpose of raw data QC is to identify and exclude data with significant artifacts, preventing their inclusion in the released raw BIDS data as well as subsequent image processing ([see details](../processing/index.md#file-selection-for-processing)). 

### Automated QC
After acquisition, data are sent to the HBCD Data Coordinating Center (HDCC), where automated QC is performed by first extracting information from DICOM headers to identify common issues and protocol deviations, such as missing files or incorrect patient orientation. Protocol compliance criteria include whether key imaging parameters, such as voxel size or repetition time, match the expected values for a given scanner. Out-of-compliance series are reviewed and sites are contacted if corrective action is required. In addition to protocol adherence, each imaging series is also automatically checked for completeness - expand the infobox below for details:
<p>
<div id="complete-session" class="table-banner" onclick="toggleCollapse(this)">
  <span class="text">Completeness Checks</span>
  <span class="arrow">▸</span>
</div>
<div class="collapsible-content">
<p>Completeness checks are run to confirm that the number of files matches what was expected for each series on each scanner. For instance, for dMRI and fMRI series, the presence or absence of corresponding echo-planar imaging (EPI) sequences (often referred to as a “field map” or “B0 map”) used for distortion correction is checked. Missing files are typically indicative of either an aborted scan or incomplete data transfer, the latter of which can usually be resolved through re-initiating the data transfer. A complete imaging session consists of the following valid series:</p>
<table style="width: 100%; border-collapse: collapse; table-layout: fixed;">
    <tbody>
    <tr>
        <td>Structural T1 Block:</td>
        <td>T1</td>
    </tr>
    <tr>
        <td>Structural T2 Block:</td>
        <td>T2</td>
    </tr>
    <tr>
        <td>Diffusion (dMRI) Block:</td>
        <td>dMRI AP <br /> dMRI PA</td>
    </tr>
    <tr>
        <td>Resting state (rsfMRI) Block:</td>
        <td>fMRI field map AP<br /> fMRI field map PA<br /> rsfMRI (run 1)<br /> rsfMRI (run 2)</td>
    </tr>
    <tr>
        <td>MRS Block</td>
        <td>SVS localizer<br /> MRS</td>
    </tr>
    <tr>
        <td>Quantitative (qMRI) Block</td>
        <td>B1 Map<br /> 3DMagic/QALAS</td>
    </tr>
</tbody>
</table>
</div>
</p>

#### Automated QC metrics for various modalities are as follows:

<table style="width: 100%; border-collapse: collapse; table-layout: fixed; font-size: 14px">
<thead>
<tr>
    <th style="width: 20%; text-align: center;">Modality</th>
    <th style="width: 80%; text-align: center;">QC Procedures</th>
</tr>
</thead>
<tbody>
<tr>
<td style="word-wrap: break-word; white-space: normal;">Structural (T1w, T2w, qMRI)</td>
<td style="word-wrap: break-word; white-space: normal;">- Deep learning model estimates motion artifacts<br />- Signal-to-noise ratio (SNR) computed</td>
</tr>
<tr>
<td style="word-wrap: break-word; white-space: normal;">dMRI</td>
<td style="word-wrap: break-word; white-space: normal;">- Framewise displacement (FD) for head motion<br />- Head motion estimated via <span class="tooltip">registration to tensor-synthesized images<span class="tooltiptext">accounts for contrast differences across orientations</span></span> (<a href="https://doi.org/10.1002/hbm.20619">Hagler et al. 2009</a>)<br />- Identification of <span class="tooltip">dark slices<span class="tooltiptext">artifacts caused by abrupt head movements</span></span> via RMS difference between raw and tensor-fitted data<br />- Total slices and frames with motion artifacts calculated<br />- Metrics for line artifacts and field-of-view (FOV) cutoff</td>
</tr>
<tr>
<td style="word-wrap: break-word; white-space: normal;">fMRI</td>
<td style="word-wrap: break-word; white-space: normal;">- FD for head motion (average FD and seconds with FD &lt; 0.2 mm, 0.3 mm, 0.4 mm) (<a href="https://doi.org/10.1016/j.neuroimage.2011.10.018">Power et al., 2012</a>)<br />- Metrics for line artifacts and FOV cutoff<br />- <span class="tooltip">FWHM<span class="tooltiptext">Full width half max () spatial smoothness</span></span> and <span class="tooltip">tSNR<span class="tooltiptext">temporal SNR</span></span> computed after motion correction (<a href="https://doi.org/10.1016/j.neuroimage.2005.01.007">Triantafyllou et al. 2005</a>)</td>
</tr>
<tr>
<td style="word-wrap: break-word; white-space: normal;">Field Maps</td>
<td style="word-wrap: break-word; white-space: normal;">- Metrics for line artifacts and FOV cutoff</td>
</tr>
<tr>
<td style="word-wrap: break-word; white-space: normal;">All Modalities</td>
<td style="word-wrap: break-word; white-space: normal;">- SNR computed where applicable</td>
</tr>
</tbody>
</table>

### Manual Review
Based on the automated metrics above, a subset of series are selected for manual review using multivariate prediction and Bayesian classifiers to identify scans that are more likely to have issues. Trained technicians use in-house software for standardized and efficient QC. For each subject, the technician inspects a display of multi-view and multi-slice image montages and enter scores. Each subject will also prompt for notes at the end of the review before confirming, repeating, or skipping the subject, further reducing room for human error. 

During review, data quality is scored according to the severity of specific artifacts, rated on a scale of 0 to 3, where 0 indicates no artifact, 1 indicates mild, 2 moderate, and 3 severe. Structural scans include review of T1w, T2w, and qMRI. Reviewers rate scans for **motion artifacts** (e.g. ripples, blurring) and document other issues such as **intensity inhomogeneity** or **ghosting** (when the slice location is outside the FOV, creating a fainter displaced copy of the head, brain, or eyes). 

Though not scored for motion, visual inspection is performed for additional scan types including B1 field maps, used for bias field correction of qMRI scans, and SVS localizer scans used to define the ROI for MRS (spectroscopy). For qMRI, QC is also performed on derived data, including parametric maps, region of interest analysis, and comparison of quantitative parametric values for 3D-QALAS. 

For dMRI, fMRI, and field maps, scored artifacts include **susceptibility artifacts**, **FOV cutoff**, and **line artifacts** (horizontal lines present in the sagittal view, including dark slice-frame and interleaved sliced offset). **Susceptibility artifacts** are spatial and/or signal distortions, including “drop-out” regions in the brain with greatly reduced or no signal, signal bunching, and/or warping. Consistent with prior infant fMRI using posterior-anterior (PA) acquisitions, signal dropout is commonly noted in the posterior occipital cortex. Fractional anisotropy, visualized as a color-coded map that shows the directional preferences for diffusion, is additionally reviewed for DTI.

Series with severe artifacts that compromise data usability are rejected (QC = 0) and excluded from subsequent processing and analysis. The post-processing team selects from remaining series based on manual ratings, notes, and automated scores (e.g., minimum of 60% diffusion encoding volumes without significant artifacts).

### Location of Raw Data QC Results in Data Release
All quality control metrics are available in the `*_scans.tsv` file provided per participant session ([see details](../../datacuration/rawbids.md/#participant-session-scan-level-data)). The main QC score field, `QC`, is the overall manual QC score and will be a value of either 1 (pass) or 0 (fail). If the scan was not flagged for manual review and only has automated QC data, the `QC` field automatically has value of 1. 

<div id="scanstsv" class="table-banner" onclick="toggleCollapse(this)">
  <span class="text-with-link">
  <span class="text">Full list of fields included in <code>scans.tsv</code> files</span>
  <a class="anchor-link" href="#scanstsv" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="table-collapsible-content">
<table style="width: 100%; border-collapse: collapse; table-layout: fixed; font-size: 14px">
<tbody>
  <thead>
    <tr>
    <th style="width: 10%;">Field</th>
    <th style="width: 60%;">Description</th>
    <th style="width: 20%; word-wrap: break-word; white-space: normal;">Relevant Scan Types if Specific to Manual QC</th>
    </tr>
    </thead>
    <tr>
        <td style="word-wrap: break-word; white-space: normal;">filename</td>
        <td style="word-wrap: break-word; white-space: normal;">Relative paths to files</td>
        <td style="word-wrap: break-word; white-space: normal;"> </td>
    </tr>
    <tr>
        <td style="word-wrap: break-word; white-space: normal;">acq_time</td>
        <td style="word-wrap: break-word; white-space: normal;">Acquisition time</td>
        <td style="word-wrap: break-word; white-space: normal;"> </td>
    </tr>
    <tr>
        <td style="word-wrap: break-word; white-space: normal;">loris_qc_status</td>
        <td style="word-wrap: break-word; white-space: normal;">Pass Fail mapping from UCSD QC JSON file</td>
        <td style="word-wrap: break-word; white-space: normal;"> </td>
    </tr>
    <tr>
        <td style="word-wrap: break-word; white-space: normal;">loris_selected</td>
        <td style="word-wrap: break-word; white-space: normal;">Whether the file is selected for further processing</td>
        <td style="word-wrap: break-word; white-space: normal;"> </td>
    </tr>
    <tr>
        <td style="word-wrap: break-word; white-space: normal;">site</td>
        <td style="word-wrap: break-word; white-space: normal;">Site where the session data was collected</td>
        <td style="word-wrap: break-word; white-space: normal;"> </td>
    </tr>
    <tr>
        <td style="word-wrap: break-word; white-space: normal;">age</td>
        <td style="word-wrap: break-word; white-space: normal;">Age (in years) of the candidate at the time of the scan</td>
        <td style="word-wrap: break-word; white-space: normal;"> </td>
    </tr>
    <tr>
        <td style="word-wrap: break-word; white-space: normal;">age_adjusted</td>
        <td style="word-wrap: break-word; white-space: normal;">Adjusted age (in days) based on the EDD</td>
        <td style="word-wrap: break-word; white-space: normal;"> </td>
    </tr>
    <tr>
        <td style="word-wrap: break-word; white-space: normal;">head_size</td>
        <td style="word-wrap: break-word; white-space: normal;">Head size at the time of the scan</td>
        <td style="word-wrap: break-word; white-space: normal;"> </td>
    </tr>
    <tr>
        <td style="word-wrap: break-word; white-space: normal;">nrev</td>
        <td style="word-wrap: break-word; white-space: normal;">Number of reviewers for manual QC</td>
        <td style="word-wrap: break-word; white-space: normal;">All</td>
    </tr>
    <tr>
        <td style="word-wrap: break-word; white-space: normal;">revdisp</td>
        <td style="word-wrap: break-word; white-space: normal;">Whether there was disparity / disagreement between reviewers</td>
        <td style="word-wrap: break-word; white-space: normal;">All</td>
    </tr>
    <tr>
        <td style="word-wrap: break-word; white-space: normal;">QC</td>
        <td style="word-wrap: break-word; white-space: normal;">Overall manual QC score of 1 (pass) or 0 (fail)</td>
        <td style="word-wrap: break-word; white-space: normal;"> </td>
    </tr>
    <tr>
        <td style="word-wrap: break-word; white-space: normal;">notes</td>
        <td style="word-wrap: break-word; white-space: normal;">Optional notes associated with manual quality control review</td>
        <td style="word-wrap: break-word; white-space: normal;">All</td>
    </tr>
    <tr>
        <td style="word-wrap: break-word; white-space: normal;">QU_motion</td>
        <td style="word-wrap: break-word; white-space: normal;">Qualitative manual QC score for motion</td>
        <td style="word-wrap: break-word; white-space: normal;">T1w, T2w, qMRI</td>
    </tr>
    <tr>
        <td style="word-wrap: break-word; white-space: normal;">QU_sus</td>
        <td style="word-wrap: break-word; white-space: normal;">Qualitative manual QC score for susceptibility artifact</td>
        <td style="word-wrap: break-word; white-space: normal;">dMRI, fMRI, field maps</td>
    </tr>
    <tr>
        <td style="word-wrap: break-word; white-space: normal;">QU_cutoff</td>
        <td style="word-wrap: break-word; white-space: normal;">Qualitative manual QC score for FOV cutoff artifact</td>
        <td style="word-wrap: break-word; white-space: normal;">dMRI, fMRI, field maps</td>
    </tr>
    <tr>
        <td style="word-wrap: break-word; white-space: normal;">QU_line</td>
        <td style="word-wrap: break-word; white-space: normal;">Qualitative manual QC score for line artifact</td>
        <td style="word-wrap: break-word; white-space: normal;">dMRI, fMRI, field maps</td>
    </tr>
    <tr>
        <td style="word-wrap: break-word; white-space: normal;">line_nframes</td>
        <td style="word-wrap: break-word; white-space: normal;">Number of frames with line artifacts</td>
        <td style="word-wrap: break-word; white-space: normal;"> </td>
    </tr>
    <tr>
        <td style="word-wrap: break-word; white-space: normal;">line_&ltmax|mean&gt_score</td>
        <td style="word-wrap: break-word; white-space: normal;">&ltMaximum|Average&gt line artifact score across frames</td>
        <td style="word-wrap: break-word; white-space: normal;"> </td>
    </tr>
    <tr>
        <td style="word-wrap: break-word; white-space: normal;">line_&ltmax|mean&gt_count</td>
        <td style="word-wrap: break-word; white-space: normal;">&ltMaximum|Average&gt line artifact count across frames</td>
        <td style="word-wrap: break-word; white-space: normal;"> </td>
    </tr>
    <tr>
        <td style="word-wrap: break-word; white-space: normal;">cutoff</td>
        <td style="word-wrap: break-word; white-space: normal;">Sum of dorsal and ventral cutoff scores</td>
        <td style="word-wrap: break-word; white-space: normal;"> </td>
    </tr>
    <tr>
        <td style="word-wrap: break-word; white-space: normal;">&ltdorsal|ventral&gt_cutoff</td>
        <td style="word-wrap: break-word; white-space: normal;">&ltDorsal|Ventral&gt cutoff score</td>
        <td style="word-wrap: break-word; white-space: normal;"> </td>
    </tr>
    <tr>
        <td style="word-wrap: break-word; white-space: normal;">brain_&ltmean|std&gt</td>
        <td style="word-wrap: break-word; white-space: normal;">&ltAverage|Standard deviation&gt image intensity within brain mask</td>
        <td style="word-wrap: break-word; white-space: normal;"> </td>
    </tr>
    <tr>
        <td style="word-wrap: break-word; white-space: normal;">brain_SNR</td>
        <td style="word-wrap: break-word; white-space: normal;">Signal-to-noise ratio (mean/stdev) of image intensity within brain mask</td>
        <td style="word-wrap: break-word; white-space: normal;"> </td>
    </tr>
    <tr>
        <td style="word-wrap: break-word; white-space: normal;">brain_&ltmin|max|median&gt</td>
        <td style="word-wrap: break-word; white-space: normal;">&ltMinimum|Maximum|Median&gt image intensity within brain mask</td>
        <td style="word-wrap: break-word; white-space: normal;"> </td>
    </tr>
    <tr>
        <td style="word-wrap: break-word; white-space: normal;">brain_tSNR_&ltmean|median|std&gt</td>
        <td style="word-wrap: break-word; white-space: normal;">&ltAverage|Median|Standard deviation&gt temporal SNR in brain mask</td>
        <td style="word-wrap: break-word; white-space: normal;"> </td>
    </tr>
    <tr>
        <td style="word-wrap: break-word; white-space: normal;">mean_&ltmotion|trans|rot&gt</td>
        <td style="word-wrap: break-word; white-space: normal;">Average framewise &ltdisplacement|translation|rotation&gt (mm)</td>
        <td style="word-wrap: break-word; white-space: normal;"> </td>
    </tr>
    <tr>
        <td style="word-wrap: break-word; white-space: normal;">max_d&ltx|y|z&gt</td>
        <td style="word-wrap: break-word; white-space: normal;">Maximum absolute &ltx|y|z&gt translation (mm)</td>
        <td style="word-wrap: break-word; white-space: normal;"> </td>
    </tr>
    <tr>
        <td style="word-wrap: break-word; white-space: normal;">max_r&ltx|y|z&gt</td>
        <td style="word-wrap: break-word; white-space: normal;">Maximum absolute &ltx|y|z&gt rotation (mm)</td>
        <td style="word-wrap: break-word; white-space: normal;"> </td>
    </tr>
    <tr>
        <td style="word-wrap: break-word; white-space: normal;">subthresh_&lt02|03|04&gt</td>
        <td style="word-wrap: break-word; white-space: normal;">Number of seconds with framewise displacement less than &lt0.2|0.3|0.4&gt mm</td>
        <td style="word-wrap: break-word; white-space: normal;"> </td>
    </tr>
    <tr>
        <td style="word-wrap: break-word; white-space: normal;">aqc_motion</td>
        <td style="word-wrap: break-word; white-space: normal;">Automated QC motion score for sMRI</td>
        <td style="word-wrap: break-word; white-space: normal;"> </td>
    </tr>
    <tr>
        <td style="word-wrap: break-word; white-space: normal;">nreps</td>
        <td style="word-wrap: break-word; white-space: normal;">Number of repetitions / frames</td>
        <td style="word-wrap: break-word; white-space: normal;"> </td>
    </tr>
    <tr>
        <td style="word-wrap: break-word; white-space: normal;">brainvol</td>
        <td style="word-wrap: break-word; white-space: normal;">Volume of brain mask (mm^3)</td>
        <td style="word-wrap: break-word; white-space: normal;"> </td>
    </tr>
    <tr>
        <td style="word-wrap: break-word; white-space: normal;">fwhm_x</td>
        <td style="word-wrap: break-word; white-space: normal;">Full width half max spatial smoothness in x-axis (left-right)</td>
        <td style="word-wrap: break-word; white-space: normal;"> </td>
    </tr>
    <tr>
        <td style="word-wrap: break-word; white-space: normal;">b0_&ltmedian|std&gt</td>
        <td style="word-wrap: break-word; white-space: normal;">&ltMedian|Standard Deviation&gt b=0 intensity in brain mask</td>
        <td style="word-wrap: break-word; white-space: normal;"> </td>
    </tr>
    <tr>
        <td style="word-wrap: break-word; white-space: normal;">DTerr_&ltmean|median|std&gt</td>
        <td style="word-wrap: break-word; white-space: normal;">&ltAverage|Median|Standard deviation&gt across frames of RMS residual error relative to RMS signal in brain voxels</td>
        <td style="word-wrap: break-word; white-space: normal;"> </td>
    </tr>
    <tr>
        <td style="word-wrap: break-word; white-space: normal;">Completed</td>
        <td style="word-wrap: break-word; white-space: normal;">Whether the series has the expected number of files</td>
        <td style="word-wrap: break-word; white-space: normal;"> </td>
    </tr>
    <tr>
        <td style="word-wrap: break-word; white-space: normal;">NumberOfFiles</td>
        <td style="word-wrap: break-word; white-space: normal;">Number of DICOM files</td>
        <td style="word-wrap: break-word; white-space: normal;"> </td>
    </tr>
    <tr>
        <td style="word-wrap: break-word; white-space: normal;">HBCD_compliant</td>
        <td style="word-wrap: break-word; white-space: normal;">Whether the series passes a minimal protocol compliance check</td>
        <td style="word-wrap: break-word; white-space: normal;"> </td>
    </tr>
    <tr>
        <td style="word-wrap: break-word; white-space: normal;">AdditionalInfo</td>
        <td style="word-wrap: break-word; white-space: normal;">Notes related to classification and protocol compliance</td>
        <td style="word-wrap: break-word; white-space: normal;"> </td>
    </tr>
    <tr>
        <td style="word-wrap: break-word; white-space: normal;">MD_std</td>
        <td style="word-wrap: break-word; white-space: normal;">Standard deviation of mean diffusivity in brain mask</td>
        <td style="word-wrap: break-word; white-space: normal;"> </td>
    </tr>
    <tr>
        <td style="word-wrap: break-word; white-space: normal;">b0_mean</td>
        <td style="word-wrap: break-word; white-space: normal;">Average b=0 intensity in brain mask</td>
        <td style="word-wrap: break-word; white-space: normal;"> </td>
    </tr>
    <tr>
        <td style="word-wrap: break-word; white-space: normal;">FA_std</td>
        <td style="word-wrap: break-word; white-space: normal;">Standard deviation of fractional anisotropy in brain mask</td>
        <td style="word-wrap: break-word; white-space: normal;"> </td>
    </tr>
    <tr>
        <td style="word-wrap: break-word; white-space: normal;">MD_&ltmean|median&gt</td>
        <td style="word-wrap: break-word; white-space: normal;">&ltAverage|Median&gt mean diffusivity in brain mask</td>
        <td style="word-wrap: break-word; white-space: normal;"> </td>
    </tr>
    <tr>
        <td style="word-wrap: break-word; white-space: normal;">max_nbad_frames_per_&ltslice|frame&gt</td>
        <td style="word-wrap: break-word; white-space: normal;">Maximum number of outlier frames per &ltslice|frame&gt</td>
        <td style="word-wrap: break-word; white-space: normal;"> </td>
    </tr>
    <tr>
        <td style="word-wrap: break-word; white-space: normal;">FA_&ltmean|median&gt</td>
        <td style="word-wrap: break-word; white-space: normal;">&ltAverage|Median&gt fractional anisotropy in brain mask</td>
        <td style="word-wrap: break-word; white-space: normal;"> </td>
    </tr>
    <tr>
        <td style="word-wrap: break-word; white-space: normal;">fwhm_z</td>
        <td style="word-wrap: break-word; white-space: normal;">Full width half max spatial smoothness in z-axis (inferior-superior)</td>
        <td style="word-wrap: break-word; white-space: normal;"> </td>
    </tr>
    <tr>
        <td style="word-wrap: break-word; white-space: normal;">nbad_frame_slices</td>
        <td style="word-wrap: break-word; white-space: normal;">Number of outlier frame-slices for dMRI</td>
    </tr>
    <td style="word-wrap: break-word; white-space: normal;"> </td>
    <tr>
        <td style="word-wrap: break-word; white-space: normal;">nbad_frames</td>
        <td style="word-wrap: break-word; white-space: normal;">Number of frames with outlier slices for dMRI</td>
        <td style="word-wrap: break-word; white-space: normal;"> </td>
    </tr>
    <tr>
        <td style="word-wrap: break-word; white-space: normal;">nbad_slices</td>
        <td style="word-wrap: break-word; white-space: normal;">Number of slices with outlier frames for dMRI</td>
        <td style="word-wrap: break-word; white-space: normal;"> </td>
    </tr>
    <tr>
        <td style="word-wrap: break-word; white-space: normal;">fwhm_y</td>
        <td style="word-wrap: break-word; white-space: normal;">Full width half max spatial smoothness in y-axis (anterior-posterior)</td>
        <td style="word-wrap: break-word; white-space: normal;"> </td>
    </tr>
    <tr>
        <td style="word-wrap: break-word; white-space: normal;">qc_status</td>
        <td style="word-wrap: break-word; white-space: normal;">Whether review is pending, complete, or has other status</td>
        <td style="word-wrap: break-word; white-space: normal;"> </td>
    </tr>
    <tr>
        <td style="word-wrap: break-word; white-space: normal;">ngood_frames</td>
        <td style="word-wrap: break-word; white-space: normal;">Number of frames without outlier slices for dMRI</td>
        <td style="word-wrap: break-word; white-space: normal;"> </td>
    </tr>
    <tr>
        <td style="word-wrap: break-word; white-space: normal;">censor_thresh</td>
        <td style="word-wrap: break-word; white-space: normal;">Threshold used for censoring outlier slices for dMRI</td>
        <td style="word-wrap: break-word; white-space: normal;"> </td>
    </tr>
    <tr>
        <td style="word-wrap: break-word; white-space: normal;">nframes_b&lt0|500|1000|2000|3000&gt</td>
        <td style="word-wrap: break-word; white-space: normal;">Number of b=&lt0|500|1000|2000|3000&gt frames</td>
        <td style="word-wrap: break-word; white-space: normal;"> </td>
    </tr>
    <tr>
        <td style="word-wrap: break-word; white-space: normal;">nbad_frame_slices_b&lt0|500|1000|2000|3000&gt</td>
        <td style="word-wrap: break-word; white-space: normal;">Number of outlier frame-slices for dMRI b=&lt0|500|1000|2000|3000&gt frames</td>
        <td style="word-wrap: break-word; white-space: normal;"> </td>
    </tr>
    <tr>
        <td style="word-wrap: break-word; white-space: normal;">nbad_frames_b&lt0|500|1000|2000|3000&gt</td>
        <td style="word-wrap: break-word; white-space: normal;">Number of frames with outlier slices for dMRI b=&lt0|500|1000|2000|3000&gt frames</td>
        <td style="word-wrap: break-word; white-space: normal;"> </td>
    </tr>
    <tr>
        <td style="word-wrap: break-word; white-space: normal;">nbad_slices_b&lt0|500|1000|2000|3000&gt</td>
        <td style="word-wrap: break-word; white-space: normal;">Number of slices with outlier frames for dMRI b=&lt0|500|1000|2000|3000&gt frames</td>
        <td style="word-wrap: break-word; white-space: normal;"> </td>
    </tr>
    <tr>
        <td style="word-wrap: break-word; white-space: normal;">ngood_frames_b&lt0|500|1000|2000|3000&gt</td>
        <td style="word-wrap: break-word; white-space: normal;">Number of frames without outlier slices for dMRI b=&lt0|500|1000|2000|3000&gt frames</td>
        <td style="word-wrap: break-word; white-space: normal;"> </td>
    </tr>
    <tr>
        <td style="word-wrap: break-word; white-space: normal;">FWHMx_b&lt0|500|1000|2000|3000&gt</td>
        <td style="word-wrap: break-word; white-space: normal;">Full width half max spatial smoothness in x-axis (left-right) for b=&lt0|500|1000|2000|3000&gt frames</td>
        <td style="word-wrap: break-word; white-space: normal;"> </td>
    </tr>
    <tr>
        <td style="word-wrap: break-word; white-space: normal;">FWHMy_b&lt0|500|1000|2000|3000&gt</td>
        <td style="word-wrap: break-word; white-space: normal;">Full width half max spatial smoothness in y-axis (anterior-posterior) for b=&lt0|500|1000|2000|3000&gt frames</td>
        <td style="word-wrap: break-word; white-space: normal;"> </td>
    </tr>
    <tr>
        <td style="word-wrap: break-word; white-space: normal;">FWHMz_b&lt0|500|1000|2000|3000&gt</td>
        <td style="word-wrap: break-word; white-space: normal;">Full width half max spatial smoothness in z-axis (inferior-superior) for b=&lt0|500|1000|2000|3000&gt frames</td>
        <td style="word-wrap: break-word; white-space: normal;"> </td>
    </tr>
    <tr>
        <td style="word-wrap: break-word; white-space: normal;">tSNR_b&lt0|500|1000|2000|3000&gt</td>
        <td style="word-wrap: break-word; white-space: normal;">Median temporal SNR in brain mask for b=&lt0|500|1000|2000|3000&gt frames</td>
        <td style="word-wrap: break-word; white-space: normal;"> </td>
    </tr>
    <tr>
        <td style="word-wrap: break-word; white-space: normal;">DTerr_rel_b&lt0|500|1000|2000|3000&gt</td>
        <td style="word-wrap: break-word; white-space: normal;">Median across brain voxels of DTI RMS residual error for b=&lt0|500|1000|2000|3000&gt frames relative to within-voxel RMS b=0 signal</td>
        <td style="word-wrap: break-word; white-space: normal;"> </td>
    </tr>
    <tr>
        <td style="word-wrap: break-word; white-space: normal;">RSIerr_rel_b&lt0|500|1000|2000|3000&gt</td>
        <td style="word-wrap: break-word; white-space: normal;">Median across brain voxels of RSI RMS residual error for b=&lt0|500|1000|2000|3000&gt frames relative to within-voxel RMS b=0 signal</td>
        <td style="word-wrap: break-word; white-space: normal;"> </td>
    </tr>
    <tr>
        <td style="word-wrap: break-word; white-space: normal;">DTerr_rel</td>
        <td style="word-wrap: break-word; white-space: normal;">Median across brain voxels of DTI RMS residual error for all frames relative to within-voxel RMS signal</td>
        <td style="word-wrap: break-word; white-space: normal;"> </td>
    </tr>
    <tr>
        <td style="word-wrap: break-word; white-space: normal;">RSIerr_rel</td>
        <td style="word-wrap: break-word; white-space: normal;">Median across brain voxels of RSI RMS residual error for all frames relative to within-voxel RMS signal</td>
        <td style="word-wrap: break-word; white-space: normal;"> </td>
    </tr>
    <tr>
        <td style="word-wrap: break-word; white-space: normal;">NumberOfFilesMissing</td>
        <td style="word-wrap: break-word; white-space: normal;">Number of DICOM files apparently missing (based on gaps in InstanceNumbers)</td>
        <td style="word-wrap: break-word; white-space: normal;"> </td>
    </tr>
    <tr>
        <td style="word-wrap: break-word; white-space: normal;">Num&ltHead|Neck|Spine&gtCoilElem</td>
        <td style="word-wrap: break-word; white-space: normal;">Number of &lthead|neck|spine&gt coil elements</td>
        <td style="word-wrap: break-word; white-space: normal;"> </td>
    </tr>
    <tr>
        <td style="word-wrap: break-word; white-space: normal;">brain_nvox_max</td>
        <td style="word-wrap: break-word; white-space: normal;">Number of voxels within brain mask at maximum image intensity</td>
        <td style="word-wrap: break-word; white-space: normal;"> </td>
    </tr>
    <tr>
        <td style="word-wrap: break-word; white-space: normal;">brain_fvox_max</td>
        <td style="word-wrap: break-word; white-space: normal;">Fraction of voxels within brain mask at maximum image intensity</td>
        <td style="word-wrap: break-word; white-space: normal;"> </td>
    </tr>
    <tr>
        <td style="word-wrap: break-word; white-space: normal;">nonbrain_&ltmean|std|snr&gt</td>
        <td style="word-wrap: break-word; white-space: normal;">&ltAverage|Standard deviation|Signal-to-noise ratio (mean/stdev)&gt image intensity outside brain mask</td>
        <td style="word-wrap: break-word; white-space: normal;"> </td>
    </tr>
    <tr>
        <td style="word-wrap: break-word; white-space: normal;">NumberOfFilesOrig</td>
        <td style="word-wrap: break-word; white-space: normal;">umber of DICOM files received (before excluding non-image, corrupt, or extra files)</td>
        <td style="word-wrap: break-word; white-space: normal;"> </td>
    </tr>
    <tr>
        <td style="word-wrap: break-word; white-space: normal;">NumberOfFilesExtra</td>
        <td style="word-wrap: break-word; white-space: normal;">Number of extra DICOM files received (non-image, corrupt, or extra files)</td>
        <td style="word-wrap: break-word; white-space: normal;"> </td>
    </tr>
</tbody>
</table>
</div>

## Data Release Eligibility Criteria

After converting MRI data to BIDS format, both the NIfTI and JSON files undergo additional verification to ensure data integrity. As part of this process, all images are checked to confirm they were acquired using a head coil before being included in the BIDS dataset.

Acquisition parameters can vary depending on the scanner vendor. For example, while the GE protocol acquires structural data at **0.8 mm isotropic resolution**, the current protocol/software version upsamples the data during reconstruction and DICOM creation, resulting in an **in-plane resolution of 0.5 × 0.5 × 0.8 mm³**. This will be adjusted in a future software upgrade.

To account for such variations, most inclusion criteria are defined as acceptable **ranges** rather than fixed values. The specific modality-based inclusion criteria are extracted directly from the image JSON files and evaluated accordingly.

<p>
<div id="acq-param-table" class="table-banner" onclick="toggleCollapse(this)">
  <span class="table-text">Acquisition Parameter Ranges for Data Release Eligibility</span>
  <span class="arrow">▸</span>
</div>
<div class="table-collapsible-content">
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

## BrainSwipes

Manual visual inspection remains the gold standard for identifying artifacts in structural and functional derivatives (e.g., from XCP-D) and diffusion derivatives (e.g., from QSIPrep). To streamline this process, derivative visual reports are integrated into [BrainSwipes](https://brainswipes.us/about), a gamified, crowdsourced QC platform built on the open-source [Swipes For Science](https://swipesforscience.org/) framework.		

BrainSwipes engages users in evaluating brain image quality through an intuitive interface designed for large-scale studies. After creating an account, users are guided through a brief [tutorial](https://brainswipes.us/tutorial-select) that teaches them how to assess derivative images and classify them as pass or fail.

<div class="img-with-text" style="width: 60%; margin: 0 auto; text-align: center;">
    <img src="../images/brainswipes.png" alt="Example quality assessment of surface delineation in BrainSwipes" style="width: 100%; height: auto;">
    <p><i>Example quality assessment of surface delineation on BrainSwipes platform (displaying brain in axial plane at level of basal ganglia/putamen).</i></p>
</div>

<p>
<div id="swipes-procedures" class="table-banner" onclick="toggleCollapse(this)">
<span class="text-with-link">
  <span class="table-text">BrainSwipes QC Procedures</span>
	<a class="anchor-link" href="#swipes-procedures" title="Copy link">
  	<i class="fa-solid fa-link"></i>
  	</a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="collapsible-content">
<p>
<p style="font-size: 1em; margin: 0 0 5px;"><b>Surface Delineation:</b></p>
For structural QA, swipers are presented with image slices in coronal, axial, and sagittal planes to assess the accuracy of T1w and T2w surface delineations in differentiating gray and white matter. Images are derived from XCP-D visual reports.
</p>
<p style="font-size: 1em; margin: 0 0 5px;"><b>Atlas Registration:</b></p>
In addition to surface delineation, structural QA also includes atlas registration quality, evaluated by overlaying delineations of the subject’s image onto the atlas, and vice versa. Swipes display nine T1w slices for visual inspection, with three slices per anatomical plane. Quality is assessed based on the alignment of the outer boundaries of the overlaid contours with those of the underlying image, ensuring minimal gaps or misalignments. Images are derived from XCP-D visual reports.
<p>
<p style="font-size: 1em; margin: 0 0 5px;"><b>Functional Registration:</b></p>
Functional registration is evaluated by overlaying outlines of functional images onto structural images and vice versa. Swipes display nine slices of the same functional image for visual inspection, with three slices per anatomical plane. Quality is assessed similarly to structural atlas registration, focusing on the alignment of the overlaid contours. Additional evaluation includes checking for artifacts such as signal dropout. Images are derived from XCP-D visual reports.
</p>
<p style="font-size: 1em; margin: 0 0 5px;"><b>Diffusion Direction Encoding (<i>to be included in future release</i>):</b></p>
Swipes display GIFs of full-resolution T2w images as a grayscale background, with the "Direction Encoded Color" (DEC) map overlaid. These GIFs sweep through a portion of the brain across the three anatomical planes. High-quality processed DWI images exhibit bands of color that closely follow the folds and contours of the grayscale background. These visuals are derived from the QSIPrep report.
<p>
<strong>Each visual report for a given modality is independently reviewed and rated as a pass or fail, which in the outputs are scored as values of 1 and 0 respectively. BrainSwipes generates a summary of these results that includes the average score as well as number of reviewers for each visual report of each modality.</strong>
</div>
</p>

### Location of BrainSwipes Results in Data Release

<p>
<div id="dwi-fyi" class="notification-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fa-regular fa-lightbulb"></i></span>
  <span class="text-with-link">
  <span class="text">Automated QC for Processed Diffusion Data</span>
  <a class="anchor-link" href="#dwi-fyi" title="Copy link">
  	<i class="fa-solid fa-link"></i>
  	</a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="notification-open-collapsible-content">
<p>The release currently includes BrainSwipes results for only structural and functional MRI. Diffusion results will be included in a later release. However, existing automated QC procedures for processed diffusion data are fairly robust compared to sMRI and fMRI. The automated QC metrics are provided within <code>SUBSES_space-ACPC_desc-image_qc.tsv</code> in the <a href="../../../datacuration/derivatives/#qsiprep-qsiprep">QSIPrep derivatives</a> - please see more information about automated QC on the <a href="https://qsiprep.readthedocs.io/en/latest/preprocessing.html#quality-control-data">QSIPrep website</a>.</p>

<p>Below are automated QC metric distributions for HBCD data from visits V02 and V03. Higher NDC (closer to 1) and CNR indicate better quality images. <strong>We recommend users use NDC as a covariate in their analyses.</strong></p>

<p><b>Left</b>: Neighboring DWI Correlation (NDC) calculated pre and post processing for each vendor on the combined AP/PA scans. Processed data is represented by a solid line, while raw data is dashed.</p>
<p><b>Right</b>: Contrast to Noise Ratio (CNR) per shell per vendor as calculated by Eddy. Distributions are likewise colored by vendor. As data included in these plots and in the beta release have already passed a preliminary QC check we do not have specific values recommended for exclusion. However, NDC and CNR are useful covariates to include when analyzing other derivatives.</p>
<img src="../images/ndc_cnr_comparison.svg" width="95%" height="auto" class="center">
<br>
</div>
</p>

BrainSwipes QC results are provided as tabulated instrument data in the `rawdata/phenotype/` folder of the data release (see details [here](../../datacuration/phenotypes.md)), including `img_brainswipes_xcpd-T2w` and `img_brainswipes_xcpd-bold` instrument files. These files contain the BrainSwipes results reporting the average QC score and number of reviewers for each individual visual report. 

The results are also combined for each subject modality to report the overall average QC score and average number of reviewers across visual reports per run. In other words, a single average QC score is provided for each session-level T2w and session-level BOLD run. Below we provide a Python helper function to read a BrainSwipes TSV file into a Pandas DataFrame and filter out all subject runs with an average overall QC score of greater than or equal to a threshold specified by the user:

<div id="helper-function" class="table-banner" onclick="toggleCollapse(this)">
  <span class="text-with-link">
  <span class="text">🐍 Python Helper Function</span>
  <a class="anchor-link" href="#helper-function" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="table-collapsible-content">
<pre class="folder-tree">
import pandas as pd

def read_and_filter_tsv(file_path, threshold):
    """
    Reads an HBCD BrainSwipes TSV file into a DataFrame and keeps subject rows where 
	the overall average QC value is greater than or equal to the specified threshold.

    Parameters:
    - file_path (str): Path to the .tsv file
    - threshold (float): Threshold value for filtering

    Returns:
    - pd.DataFrame: Filtered DataFrame
    """
    df = pd.read_csv(file_path, sep='\t')

    fourth_col = df.columns[3]
    return df[df[fourth_col] >= threshold]

# Example usage:
# Filter to keep only subjects with an average structural QC of at least 0.6 (60% pass rate)
filtered_df = read_and_filter_tsv("img_brainswipes_xcpd_T2w.tsv", 0.6)
print(filtered_df.head())
</pre>
</div>

## References
<div class="references">
    <p>Dean III, D. C., Tisdall, M. D., Wisnowski, J. L., Feczko, E., Gagoski, B., Alexander, A. L., ... &amp; HBCD MRI Working Group. (2024). Quantifying brain development in the HEALthy Brain and Child Development (HBCD) Study: The magnetic resonance imaging and spectroscopy protocol. <em>Developmental Cognitive Neuroscience</em>, 70, 101452. <a href="https://doi.org/10.1016/j.dcn.2024.101452">https://doi.org/10.1016/j.dcn.2024.101452</a></p>
    <p>Gard, A. M., Hyde, L. W., Heeringa, S. G., West, B. T., & Mitchell, C. (2023). Why weight? Analytic approaches for large-scale population neuroscience data. Developmental Cognitive Neuroscience, 59, 101196. <a href="https://doi.org/10.1016/j.dcn.2023.101196">https://doi.org/10.1016/j.dcn.2023.101196</a></p>
    <p>Hagler, D. J., Jr, Ahmadi, M. E., Kuperman, J., Holland, D., McDonald, C. R., Halgren, E., &amp; Dale, A. M. (2009). Automated white-matter tractography using a probabilistic diffusion tensor atlas: Application to temporal lobe epilepsy. Human Brain Mapping, 30(5), 1535–1547. <a href="https://doi.org/10.1002/hbm.20619">https://doi.org/10.1002/hbm.20619</a></p>
    <p>Power, J. D., Barnes, K. A., Snyder, A. Z., Schlaggar, B. L., &amp; Petersen, S. E. (2012). Spurious but systematic correlations in functional connectivity MRI networks arise from subject motion. NeuroImage, 59(3), 2142–2154. <a href="https://doi.org/10.1016/j.neuroimage.2011.10.018">https://doi.org/10.1016/j.neuroimage.2011.10.018</a></p>
    <p>Triantafyllou, C., Hoge, R. D., Krueger, G., Wiggins, C. J., Potthast, A., Wiggins, G. C., &amp; Wald, L. L. (2005). Comparison of physiological noise at 1.5 T, 3 T and 7 T and optimization of fMRI acquisition parameters. NeuroImage, 26(1), 243–250. <a href="https://doi.org/10.1016/j.neuroimage.2005.01.007">https://doi.org/10.1016/j.neuroimage.2005.01.007</a></p>
</div>
<br>
