# Quality Control Output Summaries

## Automated QC for Processed Diffusion Data

The release currently includes BrainSwipes results for only structural and functional MRI. Diffusion results will be included in a later release. However, existing automated QC procedures for processed diffusion data are fairly robust compared to sMRI and fMRI. The automated QC metrics are provided within <code>SUBSES_space-ACPC_desc-image_qc.tsv</code> in the <a href="../../../datacuration/derivatives/#qsiprep-qsiprep">QSIPrep derivatives</a> - please see more information about automated QC on the <a href="https://qsiprep.readthedocs.io/en/latest/preprocessing.html#quality-control-data">QSIPrep website</a>.

<p>Below are automated QC metric distributions for HBCD data from visits V02 and V03. Higher NDC (closer to 1) and CNR indicate better quality images. <strong>We recommend users use NDC as a covariate in their analyses.</strong></p>

<p><b>Left</b>: Neighboring DWI Correlation (NDC) calculated pre and post processing for each vendor on the combined AP/PA scans. Processed data is represented by a solid line, while raw data is dashed.</p>
<p><b>Right</b>: Contrast to Noise Ratio (CNR) per shell per vendor as calculated by Eddy. Distributions are likewise colored by vendor. As data included in these plots and in the beta release have already passed a preliminary QC check we do not have specific values recommended for exclusion. However, NDC and CNR are useful covariates to include when analyzing other derivatives.</p>
<img src="../images/ndc_cnr_comparison.svg" width="85%" height="auto" class="center">

<div id="dwi-fyi" class="notification-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fa-regular fa-lightbulb"></i></span>
  <span class="text-with-link">
  <span class="text">Automated QC for Processed Diffusion Data (REMOVE)</span>
  <a class="anchor-link" href="#dwi-fyi" title="Copy link">
    <i class="fa-solid fa-link"></i>
    </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="notification-collapsible-content">
<p>The release currently includes BrainSwipes results for only structural and functional MRI. Diffusion results will be included in a later release. However, existing automated QC procedures for processed diffusion data are fairly robust compared to sMRI and fMRI. The automated QC metrics are provided within <code>SUBSES_space-ACPC_desc-image_qc.tsv</code> in the <a href="../../../datacuration/derivatives/#qsiprep-qsiprep">QSIPrep derivatives</a> - please see more information about automated QC on the <a href="https://qsiprep.readthedocs.io/en/latest/preprocessing.html#quality-control-data">QSIPrep website</a>.</p>

<p>Below are automated QC metric distributions for HBCD data from visits V02 and V03. Higher NDC (closer to 1) and CNR indicate better quality images. <strong>We recommend users use NDC as a covariate in their analyses.</strong></p>

<p><b>Left</b>: Neighboring DWI Correlation (NDC) calculated pre and post processing for each vendor on the combined AP/PA scans. Processed data is represented by a solid line, while raw data is dashed.</p>
<p><b>Right</b>: Contrast to Noise Ratio (CNR) per shell per vendor as calculated by Eddy. Distributions are likewise colored by vendor. As data included in these plots and in the beta release have already passed a preliminary QC check we do not have specific values recommended for exclusion. However, NDC and CNR are useful covariates to include when analyzing other derivatives.</p>
<img src="../images/ndc_cnr_comparison.svg" width="95%" height="auto" class="center">
</div>



🚧 UNDER CONSTRUCTION 🚧 - 

## MRI QC

<p>
<div class="notification-banner static-banner">
  <span class="emoji"><i class="fa-regular fa-lightbulb"></i></span>
  <span class="text">
    BrainSwipes Quality Control (QC) Scoring
  </span>
</div>
<div class="notification-static-content">
<p>QC scores range from 0 to 1, where 0 indicates a "Fail" and 1 indicates a "Pass." Scores are averaged across reviewers. For example, an average QC score of 0.6 means that 60% of reviewers rated the image as a pass. Therefore, for example, a threshold of > 0.1 includes data that received passing scores from more than 10% of reviewers.</p>
</div>
</p>

### Structural BrainSwipes QC & Surface Morphometrics 

##### T2w BrainSwipes QC Summary

The following cumulative BrainSwipes plot shows that the majority of T2w images passed visual inspection:
<img src="../images/mriqc/brainswipes-T2-QC.png" style="width: 70%;" class="center">


### Surface Morphometrics With and Without QC Threshold

Click to expand each section below to view surface morphometric summaries for (1) all V02 data included in the release and (2) only V02 data with an average structural QC score of 0.7 (i.e. rated as a Pass by 70% of reviewers)

<div id="surf" class="notification-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fa-regular fa-lightbulb"></i></span>
  <span class="text-with-link">
  <span class="text">Thickness</i></span>
  <a class="anchor-link" href="#surf" title="Copy link">
    <i class="fa-solid fa-link"></i>
    </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="notification-collapsible-content">
<img src="../images/mriqc/thickness.jpeg" style="width: 100%;" class="center">
<img src="../images/mriqc/thickness-qcthresh.jpeg" style="width: 100%;" class="center">
</div>

<div id="surf" class="notification-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fa-regular fa-lightbulb"></i></span>
  <span class="text-with-link">
  <span class="text">Curvature</i></span>
  <a class="anchor-link" href="#surf" title="Copy link">
    <i class="fa-solid fa-link"></i>
    </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="notification-collapsible-content">
<img src="../images/mriqc/curv.jpeg" style="width: 100%;" class="center">
<br>
<b>ADD 70% FIGURE</b>
</div>

<div id="surf" class="notification-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fa-regular fa-lightbulb"></i></span>
  <span class="text-with-link">
  <span class="text">Sulcal Depth</i></span>
  <a class="anchor-link" href="#surf" title="Copy link">
    <i class="fa-solid fa-link"></i>
    </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="notification-collapsible-content">
<img src="../images/mriqc/sulc.jpeg" style="width: 100%;" class="center">
<br>
<b>ADD 70% FIGURE</b>
</div>

### Functional Connectivity as Data Quality Improves (Left -> Right)

##### Average Gordon Connectivity Matrices for V02 at Varying QC Thresholds

<p>Average functional connectivity matrices were computed using the Gordon parcellation from <a href="../../../datacuration/derivatives/#xcp-d-xcp_d">XCP-D derivatives</a> for V02 sessions with data inclusion based on various thresholds of BrainSwipes QC results (<code>img_brainswipes_xcpd-bold</code>; <a href="../qc/#brainswipes">see details</a>). Functional connectivity patterns remained consistent even when incorporating data with lower QC scores, suggesting robustness to mild quality variations.
 </p>

<img src="../images/mriqc/mri_qc.png" style="width: 100%;" class="center">

