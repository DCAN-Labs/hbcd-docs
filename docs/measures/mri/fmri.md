# Functional MRI (fMRI)
<p>
<div id="alert" class="alert-banner" onclick="toggleCollapse(this)">
    <span class="emoji"><i class="fas fa-exclamation-circle"></i></span>
    <span class="text">Responsible Use Warning</span>
  <span class="arrow">▸</span>
</div>
<div class="collapsible-content">
<br>
<p><b><i>The text below is sourced directly from the ABCD Wiki <a href="https://data.abcdstudy.org/reports/wiki-release6/data-doc/imaging/resting-state-fmri.html#use-rsfmri">Responsible Use Warning: Head Motion</a>. While it specifically references ABCD, the same principles apply equally to HBCD.</i></b></p>
<blockquote>
<p>Head motion is a serious issue for neuroimaging, and especially for resting state fMRI. It creates brain-wide artifactual effects including elevated short-distance connectivity and attenuated long-distance connectivity (Power et al. 2012). In order to guard against artifactual effects due to head motion, researchers typically implement a variety of strategies that operate at multiple points of the data collection and processing pipeline, with guidance regularly evolving over time (Power et al. 2014; 2015; Satterthwaite et al. 2013; Siegel et al. 2017; Gratton et al. 2020). Some of these strategies include discarding entire runs of data that exceed certain motion thresholds and discarding individual functional imaging frames that are proximal to motion events (i.e., “motion censoring”). These strategies in particular typically lead to the exclusion of some participants from further analysis for lack of sufficient data.</p>
<p>Levels of head motion differ according to demographic factors such as sex, race/ethnicity, and SES (Cosgrove et al., 2022). Therefore, strategies to deal with head motion may introduce questions of fairness and may lead to differential exclusions across demographic groups. In addition, motion censoring causes sessions to vary by the amount of data remaining. Such variability may continue to inflate findings especially in the presence of conditions that may correlate with the motion artifact like autism or ADHD (Eggebrecht, 2017). The amount of data remaining influences the variation in the connectivity calculations by affecting the degrees of freedom. Therefore, even after motion censoring, issues concerning fairness may persist when examining factors that might be affected by motion like sex, race/ethnicity, SES, and BMI (Cosgrove et al., 2022). One strategy that avoids this confound is to strictly control the degrees of freedom, where functional connectivity measures are calculated with the exact same amount of data. Researchers should assess whether control of artifactual effects of head motion effects can be achieved by alternative means that mitigate this impact. Examples of such strategies could include data augmentation approaches such as sampling from other datasets beyond ABCD, data processing strategies like the include use of ICA-based denoising (Pruim et al., 2015a; 2015b), use of bootstrap aggregation (Ramduny et al., 2024), or the creation of “pseudo-rest” by removing task signals from the task data (Fair et al. 2007), or post-hoc approaches like propensity weighting. To aid researchers in exploring this impact further, the ABCD study has released 5 minute- and 10 minute-trimmed and untrimmed functional connectivity datasets. Researchers interested in examining brain-behavior associations or multivariate predictions should follow strategies such as those in Eggebrecht 2017: 1) assess how missing data impacts dependent, independent variables and covariates, 2) examine the association between the degrees of freedom and non-FC variables, 3) use trimmed FC measures when needed to mitigate artifacts due to data quality.</p>
</blockquote>
</div>
</p>

<p>
<div id="warning" class="warning-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fas fa-exclamation-triangle"></i></span>
  <span class="text">Data Warning</span>
  <span class="arrow">▸</span>
</div>
<div class="collapsible-content">
<br>
<p>An issue with signal intensity clipping has been identified in a portion of Philips fMRI scans. Due to a scaling error in real-time reconstruction, high-intensity values are capped at 4095, creating hyperintense regions that drown out the signal of gray and white matter in that region. This affects derived measures such as ROI-ROI correlations.</p>
<p>Initially detected during manual QC, the issue was rare early in the study and has since been addressed with a protocol patch applied at most Philips sites. However, sites VAN and CCH experienced more severe cases, as the patch was only implemented there in October 2024. Since then, no new severe cases have been observed. Overall, 20% of scans from VAN and CCH show varying levels of clipping, with 6.3% classified as severe and failing QC. In the future, real-time reconstruction will be updated in order to salvage this data, but in the interim, impacted scans are excluded from the release.</p> 
<p>Severe cases typically fail manual QC (QC=0), but less severe cases often pass (QC=1) as they may not be visually apparent. The severity of intensity clipping artifacts can be approximated from the ratio of the median to maximum image intensity and fraction of voxels at maximum intensity within the brain mask (available in the <a href="../../../datacuration/rawbids/#participant-session-scan-level-data"><code>scans.tsv</code> file</a>): </p> 
<ul>
<li>Severe clipping: brain_median / brain_max > 0.8 AND brain_fvox_max > 0.001</li> 
<li>Potential clipping: brain_median / brain_max > 0.5 AND brain_fvox_max > 0.001</li> 
</ul>
</div>
</p>

Whole-brain functional activity as measured by functional magnetic resonance imaging (fMRI). The blood oxygen level dependent (BOLD) signal is measured at each voxel in 2mm isotropic space with a repetition time (TR) of 1725 ms and multi-band (MB) factor of 4. 

A minimum of two resting state (rs) fMRI runs are acquired during sleep (for infants <30 months old) lasting 7.5 minutes each (**Figure 1A**). [FIRMM software](https://firmm.readthedocs.io/) (Dosenbach et al. 2017) is used to monitor motion, as quantified by framewise displacement (FD), in real time and additional runs are acquired as needed to obtain a minimum total of 7.5 minutes of low-motion (FD <0.3 mm) data across runs (**Figure 1B**). 

Each rsfMRI run is additionally preceded by acquisition of single shot spin-echo (SE) EPI images with same and reversed polarity phase encoding gradients with which to perform distortion correction (**Figure 1C**). Additional details are available at [Dean et al. 2024](https://doi.org/10.1016/j.dcn.2024.101452). 

<div style="text-align: center;">
  <p style="font-size: 1.1em; margin-bottom: 0px;"><strong>Figure 1.</strong> HBCD fMRI Acquisition Protocol (<i>Courtesy of <a href="https://doi.org/10.1016/j.dcn.2024.101452">Dean et al. 2024</a></i>)</p>
  <img src="../images/Deanetal2024_fMRI.jpg" width="83%" height="auto">
</div>

<br>

Functional MRI data is processed through [infant-fMRIPrep](https://nibabies.readthedocs.io/en/latest/) and subsequently [XCP-D](https://xcp-d.readthedocs.io/en/latest/usage.html) as described in detail on the [HBCD Processing webpage](https://hbcd-cbrain-processing.readthedocs.io/latest/tool_details.html#tool-names). In brief, infant-fMRIPrep produces minimally pre-processed outputs including confound files (with motion parameters, average signals for ROIs like CSF, etc.) and motion-corrected data in age-specific MNI volumetric atlas as well as fs_LR32k surface space. From these outputs, the XCP-D pipeline runs nuisance regression/denoising, parcellates the fMRI data, and computes summary measures.

Volumetric and surface-based time series will be made available for each subject. The data release also includes dense and parcellated time series with at least 2.5 minutes of low-motion data (FD>0.3), functional connectivity matrices, regional homogeneity values, and amplitude of low-frequency fluctuation values. All parcellated derivatives are generated from a variety of parcellation schemes. 

## References
<div class="references">
   <p>Cosgrove KT, McDermott TJ, White EJ, Mosconi MW, Thompson WK, Paulus MP, Cardenas-Iniguez C, Aupperle RL. Limits to the generalizability of resting-state functional magnetic resonance imaging studies of youth: An examination of ABCD Study® baseline data. <i>Brain Imaging Behav</i> 16, 1919-1925, 2022. <a href="https://doi.org/10.1007/s11682-022-00665-2" target="_blank">doi: 10.1007/s11682-022-00665-2</a></p>
  <p>Dean III, D. C., Tisdall, M. D., Wisnowski, J. L., Feczko, E., Gagoski, B., Alexander, A. L., ... &amp; HBCD MRI Working Group. (2024). Quantifying brain development in the HEALthy Brain and Child Development (HBCD) Study: The magnetic resonance imaging and spectroscopy protocol. <em>Developmental Cognitive Neuroscience</em>, 70, 101452. <a href="https://doi.org/10.1016/j.dcn.2024.101452">10.1016/j.dcn.2024.101452</a></p>
  <p>Dosenbach, N. U. F., Koller, J. M., Earl, E. A., Miranda-Dominguez, O., Klein, R. L., Van, A. N., Snyder, A. Z., Nagel, B. J., Nigg, J. T., Nguyen, A. L., Wesevich, V., Greene, D. J., & Fair, D. A. (2017). Real-time motion analytics during brain MRI improve data quality and reduce costs. <em>NeuroImage</em>, 161, 80-93. <a href="https://doi.org/10.1016/j.neuroimage.2017.08.025">https://doi.org/10.1016/j.neuroimage.2017.08.025</a></p>
  <p>Eggebrecht, A. T., Elison, J. T., Feczko, E., Todorov, A., Wolff, J. J., Kandala, S., Adams, C. M., Snyder, A. Z., Lewis, J. D., Estes, A. M., Zwaigenbaum, L., Botteron, K. N., McKinstry, R. C., Constantino, J. N., Evans, A., Hazlett, H. C., Dager, S., Paterson, S. J., Schultz, R. T., … Pruett, J. R., Jr. (2017). Joint attention and brain functional connectivity in infants and toddlers. <i>Cerebral Cortex (New York, N.Y.: 1991)</i>, 27(3), 1709–1720. <a href="https://doi.org/10.1093/cercor/bhw403" target="_blank">doi: 10.1093/cercor/bhw403</a></p>
  <p>Fair, D. A., Schlaggar, B. L., Cohen, A. L., Miezin, F. M., Dosenbach, N. U. F., Wenger, K. K., Fox, M. D., Snyder, A. Z., Raichle, M. E., & Petersen, S. E. (2007). A method for using blocked and event-related fMRI data to study “resting state” functional connectivity. <i>NeuroImage</i>, 35(1), 396–405. <a href="https://doi.org/10.1016/j.neuroimage.2006.11.051" target="_blank">doi: 10.1016/j.neuroimage.2006.11.051</a></p>
  <p>Gratton, C., Dworetsky, A., Coalson, R. S., Adeyemo, B., Laumann, T. O., Wig, G. S., Kong, T. S., Gratton, G., Fabiani, M., Barch, D. M., Tranel, D., Miranda-Dominguez, O., Fair, D. A., Dosenbach, N. U. F., Snyder, A. Z., Perlmutter, J. S., Petersen, S. E., & Campbell, M. C. (2020). Removal of high frequency contamination from motion estimates in single-band fMRI saves data without biasing functional connectivity. <i>NeuroImage</i>, 217(116866), 116866. <a href="https://doi.org/10.1016/j.neuroimage.2020.116866" target="_blank">doi: 10.1016/j.neuroimage.2020.116866</a></p>
  <p>Power, J. D., Barnes, K. A., Snyder, A. Z., Schlaggar, B. L., & Petersen, S. E. (2012). Spurious but systematic correlations in functional connectivity MRI networks arise from subject motion. <i>NeuroImage</i>, 59(3), 2142–2154. <a href="https://doi.org/10.1016/j.neuroimage.2011.10.018" target="_blank">doi: 10.1016/j.neuroimage.2011.10.018</a></p>
  <p>Power, J. D., Mitra, A., Laumann, T. O., Snyder, A. Z., Schlaggar, B. L., & Petersen, S. E. (2014). Methods to detect, characterize, and remove motion artifact in resting state fMRI. <i>NeuroImage</i>, 84, 320–341. <a href="https://doi.org/10.1016/j.neuroimage.2013.08.048" target="_blank">doi: 10.1016/j.neuroimage.2013.08.048</a></p>
  <p>Power, J. D., Schlaggar, B. L., & Petersen, S. E. (2015). Recent progress and outstanding issues in motion correction in resting state fMRI. <i>NeuroImage</i>, 105, 536–551. <a href="https://doi.org/10.1016/j.neuroimage.2014.10.044" target="_blank">doi: 10.1016/j.neuroimage.2014.10.044</a></p>
  <p>Pruim RHR, Mennes M, van Rooij D, Llera A, Buitelaar JK, Beckmann CF. ICA-AROMA: A robust ICA-based strategy for removing motion artifacts from fMRI data. <i>Neuroimage</i> 112, 267-277, 2015a. <a href="https://doi.org/10.1016/j.neuroimage.2015.02.064" target="_blank">doi: 10.1016/j.neuroimage.2015.02.064</a></p>
  <p>Pruim RHR, Mennes M, Buitelaar JK, Beckmann CF. Evaluation of ICA-AROMA and alternative strategies for motion artifact removal in resting state fMRI. <i>Neuroimage</i> 112, 278-287, 2015b. <a href="https://doi.org/10.1016/j.neuroimage.2015.02.063" target="_blank">doi: 10.1016/j.neuroimage.2015.02.063</a></p>
  <p>Ramduny, J., Uddin, L. Q., Vanderwal, T., Feczko, E., Fair, D. A., Kelly, C., & Baskin-Sommers, A. (2024). Increasing the representation of minoritized youth for inclusive and reproducible brain-behavior associations. <i>bioRxiv</i>. <a href="https://doi.org/10.1101/2024.06.22.600221" target="_blank">doi: 10.1101/2024.06.22.600221</a></p>
  <p>Satterthwaite TD, Elliott MA, Gerraty RT, Ruparel K, Loughead J, Calkins ME, Eickhoff SB, Hakonarson H, Gur RC, Gur RE, Wolf DH. An improved framework for confound regression and filtering for control of motion artifact in the preprocessing of resting-state functional connectivity data. <i>Neuroimage</i> 64, 240-256, 2013. <a href="https://doi.org/10.1016/j.neuroimage.2012.08.052" target="_blank">doi: 10.1016/j.neuroimage.2012.08.052</a></p>
  <p>Siegel JS, Mitra A, Laumann TO, Seitzman BA, Raichle M, Corbetta M, Snyder AZ. Data Quality Influences Observed Links Between Functional Connectivity and Behavior. <i>Cereb Cortex</i> 27, 4492-4502, 2017. <a href="https://doi.org/10.1093/cercor/bhw253" target="_blank">doi: 10.1093/cercor/bhw253</a></p>
</div>
<br>
