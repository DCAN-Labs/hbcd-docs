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

### Functional Connectivity as Data Quality Improves (Left -> Right)

##### Average Gordon Connectivity Matrices for V02 at Varying QC Thresholds

<figure>
  <img src="../images/mriqc/mri_qc.png" style="width: 100%;" class="center">
  <figcaption style="font-size: 0.9em;"><p>Average functional connectivity matrices were generated from the Gordon parcellation available in the <a href="../../../datacuration/derivatives/#xcp-d-xcp_d">XCP-D derivatives</a> for all V02 sessions included in the release using varying QC thresholds for the BrainSwipes QC results (<code>img_brainswipes_xcpd-bold</code>) - <a href="../qc/#brainswipes">see details</a>. Functional connectivity is not significantly impacted when including a greater amount of data with lower average QC scoring.</p></figcaption>
</figure>

