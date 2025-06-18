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


## MRI QC

🚧 UNDER CONSTRUCTION 🚧

### Surface Morphometrics & BrainSwipes QC Summaries

##### Cumulative BrainSwipes Plot Shows Most of the Data Passes Visual Inspection
<img src="../images/mriqc/brainswipes-T2-QC.png" style="width: 70%;" class="center">


##### Surface Morphometrics

<div id="surf" class="table-banner" onclick="toggleCollapse(this)">
  <span class="text-with-link">
  <span class="text">Thickness, Curvature, and Sulcal Depth Across Networks</span>
  <a class="anchor-link" href="#surf" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="table-collapsible-content">
<img src="../images/mriqc/thickness.jpeg" style="width: 90%;" class="center">
<img src="../images/mriqc/curv.jpeg" style="width: 90%;" class="center">
<img src="../images/mriqc/sulc.jpeg" style="width: 90%;" class="center">
</div>






### Functional Connectivity as Data Quality Improves (Left -> Right)

<p>
<div class="notification-banner static-banner">
  <span class="emoji"><i class="fa-regular fa-lightbulb"></i></span>
  <span class="text">
    BrainSwipes Quality Control (QC) Scoring
  </span>
</div>
<div class="notification-static-content">
<p>QC scores range from 0 to 1, where 0 indicates a "Fail" and 1 indicates a "Pass." Scores are averaged across reviewers. For example, an average QC score of 0.6 means that 60% of reviewers rated the image as a pass. Therefore, a threshold of > 0.1 includes data that received passing scores from more than 10% of reviewers.</p>
</div>
</p>


##### Average Gordon Connectivity Matrices for V02 at Varying QC Thresholds

<figure>
  <img src="../images/mriqc/mri_qc.png" style="width: 100%;" class="center">
  <figcaption style="font-size: 0.9em;"><p>Average functional connectivity matrices were computed using the Gordon parcellation from <a href="../../../datacuration/derivatives/#xcp-d-xcp_d">XCP-D derivatives</a> for V02 sessions with data inclusion based on various thresholds of BrainSwipes QC results (<code>img_brainswipes_xcpd-bold</code>; <a href="../qc/#brainswipes">see details</a>). Functional connectivity patterns remained consistent even when incorporating data with lower QC scores, suggesting robustness to mild quality variations.
 </p></figcaption>
</figure>

