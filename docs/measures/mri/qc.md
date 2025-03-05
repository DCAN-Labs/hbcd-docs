# HBCD MR Quality Control Procedures
<p>
<div id="qc-alert" class="alert-banner" onclick="toggleCollapse(this)">
    <span class="emoji"><i class="fas fa-exclamation-circle"></i></span>
    <span class="text">Responsible Use Warning</span>
  <span class="arrow">▸</span>
</div>
<div class="collapsible-content">
<br>
<p><b><i>The text below is sourced directly from the ABCD Wiki <a href="https://data.abcdstudy.org/reports/wiki-release6/data-doc/imaging/quality-control.html#use-qc">Responsible Use Warning: Quality Control</a>. While it specifically references ABCD, the same principles apply equally to HBCD.</i></b></p>
<p>Researchers conducting analyses of neuroimaging data must consider the responsible use of variables related to race and ethnicity. Comparisons of neuroimaging data among participants who are grouped by race and/or ethnicity can be interpreted as evidence of biomarkers to explain neurobiological mechanisms through which some communities experience lower rates of achievement and poorer life outcomes compared to their White counterparts. To discourage continuation of this biological deficits framework, data analysts must recognize that ethical conduct in research includes ensuring that their analyses prevent further stigmatization, marginalization, and injustice toward individuals because race and ethnicity. Potential stigmatization may also be relevant to certain clinical diagnoses or outcomes. Prior to any data analysis or interpretation, researchers must consider the psychological, social, economic, and any other potentially harmful impacts their research could have on individuals, communities, and society.</p> 
<p>Data analyses centered around comparisons of participant groups when the groupings are based on race and ethnicity alone (i.e., independent variables in isolation) are discouraged. Instead, researchers should consider factors that may perpetuate stigma in research and commit to the additional work that is needed to ensure that statistical models and analytic findings are fully contextualized, particularly with respect to variables related to social determinants of health.</p>

<p style="margin-bottom: 5px; padding-bottom: 5px; border-bottom: 1px solid #6b6b6b66;"><strong>Missingness Issues</strong></p>
<p>Participants in the ABCD Study may not have usable data for a variety of reasons. They may have withdrawn from the study, or they may have missed assessments or sessions. In other cases, data may have been collected but it is inappropriate for inclusion in an analysis. For example, neuroimaging data may be inappropriate for analysis due to excessive head motion (see the discussion of head motion in Resting-State MRI Data Documentation).</p> 
<p>Importantly, factors that predict the absence of usable data tend to be correlated with demographic factors such as sex, race/ethnicity, and socioeconomic status. Thus, researchers should investigate how patterns of missingness and their correlates may impact the conclusions they draw. In addition, they should consider strategies to address patterns of missingness, such as imputation or population weighting (Gard et al., 2023), that may allow more data to be retained and/or improve generalizability to real-world communities.</p>
</div>
</p>

## Raw MR Data QC
Quality control (QC) procedures involve automated and manual methods to evaluate unprocessed or minimally processed MRI data for issues such as incorrect acquisition parameters, imaging artifacts, or corrupted files. The purpose of raw data QC is to identify and exclude data with significant artifacts, preventing their inclusion in the released raw BIDS data as well as subsequent image processing. 

All quality control metrics are available in the `scans.tsv` file, described [here](../../datacuration/rawbids.md/#participant-session-scan-level-data), provided per participant session. Processing pipelines query the `scans.tsv` file to determine which files to include/exclude for processing (e.g. query to exclude files based on thresholds for `QU_motion`, `acq_motion`, `brain_SNR`, etc.). The criteria used for each pipeline are listed under the 'Quality Control Selection Information' under [Tool Names](https://hbcd-cbrain-processing.readthedocs.io/latest/tool_details.html#tool-names) on the HBCD Processing page. Please visit the [HBCD Processing](https://hbcd-cbrain-processing.readthedocs.io/latest/) webpage for full documentation on how each of  the following pipelines was used for HBCD processing.

### Automated QC
After acquisition, data are sent to the HBCD Data Coordinating Center (HDCC), where automated QC is performed by first extracting information from DICOM headers to identify common issues and protocol deviations, such as missing files or incorrect patient orientation. Protocol compliance criteria include whether key imaging parameters, such as voxel size or repetition time, match the expected values for a given scanner. Out-of-compliance series are reviewed and sites are contacted if corrective action is required. For dMRI and fMRI series, the presence or absence of corresponding echo-planar imaging (EPI) sequences (often referred to as a “field map” or “B0 map”) used for distortion correction is checked. 

In addition to protocol adherence, each imaging series is also automatically checked for completeness to confirm that the number of files matches what was expected for each series on each scanner. Missing files are typically indicative of either an aborted scan or incomplete data transfer, the latter of which can usually be resolved through re-initiating the data transfer.

A complete imaging session consists of the following valid series:
<table dir="ltr" border="1" cellspacing="0" cellpadding="0" data-sheets-root="1" data-sheets-baot="1"><colgroup><col width="200" /><col width="250" /></colgroup>
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

Automated QC metrics such as signal-to-noise ratio (SNR) and head motion statistics are computed from the image data. For structural scans (T1w, T2w, and quantitative MRI), a deep learning model estimates motion artifacts. For dMRI, fMRI, and field maps, metrics are generated to assess for line artifacts and field-of-view (FOV) cutoff. In addition, head motion is quantified for dMRI and fMRI by frame-to-frame displacement, known as framewise displacement (FD). For fMRI, this includes average FD and the number of seconds with FD less than 0.2 mm, 0.3 mm, and 0.4 mm (Power et al. 2012). SNR is also assessed via full width half max spatial smoothness (FWHM) and temporal SNR (tSNR), computed after motion correction (Triantafyllou et al. 2005). 

For dMRI series, head motion is estimated by registering each frame to a corresponding image synthesized from a tensor fit, accounting for variation in image contrast across diffusion orientations (Hagler et al. 2009). Dark slices, artifacts caused by abrupt head movements, are identified as outliers based on the root mean squared (RMS) difference between the original data and the tensor-fitted data. The total number of slices and frames affected by these motion artifacts are calculated for each dMRI series.

### Manual Review
Based on the automated metrics above, a subset of series are selected for manual review using multivariate prediction and Bayesian classifiers to identify scans that are more likely to have issues. Trained technicians use in-house software for standardized and efficient QC. For each subject, the technician inspects a display of multi-view and multi-slice image montages and enter scores. Each subject will also prompt for notes at the end of the review before confirming, repeating, or skipping the subject, further reducing room for human error. 

During review, data quality is scored according to the severity of specific artifacts, rated on a scale of 0 to 3, where 0 indicates no artifact, 1 indicates mild, 2 moderate, and 3 severe. Structural scans include review of T1w, T2w, and qMRI. Reviewers rate scans for **motion artifacts** (e.g. ripples, blurring) and document other issues such as **intensity inhomogeneity** or **ghosting** (when the slice location is outside the FOV, creating a fainter displaced copy of the head, brain, or eyes). 

Though not scored for motion, visual inspection is performed for additional scan types including B1 field maps, used for bias field correction of qMRI scans, and SVS localizer scans used to define the ROI for MRS (spectroscopy). For qMRI, QC is also performed on derived data, including parametric maps, region of interest analysis, and comparison of quantitative parametric values for 3D-QALAS. 

For dMRI, fMRI, and field maps, scored artifacts include **susceptibility artifacts**, **FOV cutoff**, and **line artifacts** (horizontal lines present in the sagittal view, including dark slice-frame and interleaved sliced offset). **Susceptibility artifacts** are spatial and/or signal distortions, including “drop-out” regions in the brain with greatly reduced or no signal, signal bunching, and/or warping. Consistent with prior infant fMRI using posterior-anterior (PA) acquisitions, signal dropout is commonly noted in the posterior occipital cortex. Fractional anisotropy, visualized as a color-coded map that shows the directional preferences for diffusion, is additionally reviewed for DTI.

Series with severe artifacts that compromise data usability are rejected (QC = 0) and excluded from subsequent processing and analysis. The post-processing team selects from remaining series based on manual ratings, notes, and automated scores (e.g., minimum of 60% diffusion encoding volumes without significant artifacts).


## BrainSwipes
Quality control procedures for various pipeline outputs—such as structural and functional derivatives from XCP-D and diffusion derivatives from QSIPrep-rely on manual visual inspection (the current gold standard for image QC) to identify image artifacts. To streamline this process, the visual reports included in these derivatives are integrated into [BrainSwipes](https://brainswipes.us/about), a gamified platform built off of the open-source [Swipes For Science](https://swipesforscience.org/) project.

BrainSwipes harnesses the power of crowdsourcing to address the time-intensive task of evaluating MRI brain scan quality through visual inspection, particularly for large-scale studies. Users are guided through a simple [tutorial](https://brainswipes.us/tutorial-select) that teaches them how to navigate the platform and assess derivative files, enabling them to confidently classify images as either pass or fail. For a comprehensive guide to using BrainSwipes, visit the [BrainSwipes ReadTheDocs](https://brainswipes.readthedocs.io/).

<div class="img-with-text" style="width: 80%; margin: 0 auto; text-align: center;">
    <img src="../images/brainswipes.png" alt="Example quality assessment of surface delineation in BrainSwipes" style="width: 100%; height: auto;">
    <p><i>Example quality assessment of surface delineation on BrainSwipes platform (displaying brain in axial plane at level of basal ganglia/putamen).</i></p>
</div>

<p>
<div id="swipes-procedures" class="table-banner" onclick="toggleCollapse(this)">
  <span class="table-text">BrainSwipes QC Procedures</span>
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

<p style="font-size: 1em; margin: 0 0 5px;"><b>Diffusion Direction Encoding:</b></p>
Swipes display GIFs of full-resolution T2w images as a grayscale background, with the "Direction Encoded Color" (DEC) map overlaid. These GIFs sweep through a portion of the brain across the three anatomical planes. High-quality processed DWI images exhibit bands of color that closely follow the folds and contours of the grayscale background. These visuals are derived from the QSIPrep report.
<p>
</div>
</p>

#### How are final QC scores determined for a given modality? 
Final QC scores are based on the evaluation of visual reports associated with each [QC procedure](#swipes-procedures) described above. Each report is independently reviewed, and the results are combined to calculate an overall QC score.

For example, **T1w/T2w image quality** is assessed through:

- **Atlas registration quality**: Rated using 2 visual reports (atlas overlaid on T1w/T2w and T1w/T2w overlaid on the atlas).
- **Surface delineation:** Rated using 7 visual reports showing different brain regions in coronal, axial, and sagittal planes.

Each of these 9 reports must be reviewed by at least 10 independent reviewers (or it's marked as incomplete). Reviewers assign a score of 1 (Pass) or 0 (Fail) for each report. For a report to receive an overall Pass, the average QC score across reviewers must be at least 0.7. 

To achieve an overall QC Pass for T1w/T2w images, **all 9 reports** must meet the passing threshold.
Summary QC scores for BOLD and DWI are generated in the same fashion, based on visual reports evaluating functional registration and diffusion direction encoding, respectively.

## References
<div class="references">
    <p>Dean III, D. C., Tisdall, M. D., Wisnowski, J. L., Feczko, E., Gagoski, B., Alexander, A. L., ... &amp; HBCD MRI Working Group. (2024). Quantifying brain development in the HEALthy Brain and Child Development (HBCD) Study: The magnetic resonance imaging and spectroscopy protocol. <em>Developmental Cognitive Neuroscience</em>, 70, 101452. <a href="https://doi.org/10.1016/j.dcn.2024.101452">https://doi.org/10.1016/j.dcn.2024.101452</a></p>
    <p>Gard, A. M., Hyde, L. W., Heeringa, S. G., West, B. T., & Mitchell, C. (2023). Why weight? Analytic approaches for large-scale population neuroscience data. Developmental Cognitive Neuroscience, 59, 101196. <a href="https://doi.org/10.1016/j.dcn.2023.101196">https://doi.org/10.1016/j.dcn.2023.101196</a></p>
    <p>Hagler, D. J., Jr, Ahmadi, M. E., Kuperman, J., Holland, D., McDonald, C. R., Halgren, E., &amp; Dale, A. M. (2009). Automated white-matter tractography using a probabilistic diffusion tensor atlas: Application to temporal lobe epilepsy. Human Brain Mapping, 30(5), 1535–1547. <a href="https://doi.org/10.1002/hbm.20619">https://doi.org/10.1002/hbm.20619</a></p>
    <p>Power, J. D., Barnes, K. A., Snyder, A. Z., Schlaggar, B. L., &amp; Petersen, S. E. (2012). Spurious but systematic correlations in functional connectivity MRI networks arise from subject motion. NeuroImage, 59(3), 2142–2154. <a href="https://doi.org/10.1016/j.neuroimage.2011.10.018">https://doi.org/10.1016/j.neuroimage.2011.10.018</a></p>
    <p>Triantafyllou, C., Hoge, R. D., Krueger, G., Wiggins, C. J., Potthast, A., Wiggins, G. C., &amp; Wald, L. L. (2005). Comparison of physiological noise at 1.5 T, 3 T and 7 T and optimization of fMRI acquisition parameters. NeuroImage, 26(1), 243–250. <a href="https://doi.org/10.1016/j.neuroimage.2005.01.007">https://doi.org/10.1016/j.neuroimage.2005.01.007</a></p>
</div>
<br>
