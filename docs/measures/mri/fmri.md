# Functional MRI (fMRI)

Whole-brain functional activity as measured by functional magnetic resonance imaging (fMRI). The blood oxygen level dependent (BOLD) signal is measured at each voxel in 2mm isotropic space with a repetition time (TR) of 1725 ms and multi-band (MB) factor of 4. 

A minimum of two resting state (rs) fMRI runs are acquired during sleep (for infants <30 months old) lasting 7.5 minutes each (**Figure 1A**). [FIRMM software](https://firmm.readthedocs.io/) (Dosenbach et al. 2017) is used to monitor motion, as quantified by framewise displacement (FD), in real time and additional runs are acquired as needed to obtain a minimum total of 7.5 minutes of low-motion (FD <0.3 mm) data across runs (**Figure 1B**). 

Each rsfMRI run is additionally preceded by acquisition of single shot spin-echo (SE) EPI images with same and reversed polarity phase encoding gradients with which to perform distortion correction (**Figure 1C**). Additional details are available at [Dean et al. 2024](https://doi.org/10.1016/j.dcn.2024.101452). 

<div style="text-align: center;">
  <p style="font-size: 1.1em; margin-bottom: 0px;"><strong>Figure 1.</strong> HBCD fMRI Acquisition Protocol (<i>Courtesy of <a href="https://doi.org/10.1016/j.dcn.2024.101452">Dean et al. 2024</a></i>)</p>
  <img src="Deanetal2024_fMRI.jpg" width="83%" height="auto">
</div>

<br>

Functional MRI data is processed through [infant-fMRIPrep](https://nibabies.readthedocs.io/en/latest/) and subsequently [XCP-D](https://xcp-d.readthedocs.io/en/latest/usage.html) as described in detail on the [HBCD Processing webpage](https://hbcd-cbrain-processing.readthedocs.io/latest/tool_details.html#tool-names). In brief, infant-fMRIPrep produces minimally pre-processed outputs including confound files (with motion parameters, average signals for ROIs like CSF, etc.) and motion-corrected data in age-specific MNI volumetric atlas as well as fs_LR32k surface space. From these outputs, the XCP-D pipeline runs nuisance regression/denoising, parcellates the fMRI data, and computes summary measures.

Volumetric and surface-based time series will be made available for each subject. The data release also includes dense and parcellated time series with at least 2.5 minutes of low-motion data (FD>0.3), functional connectivity matrices, regional homogeneity values, and amplitude of low-frequency fluctuation values. All parcellated derivatives are generated from a variety of parcellation schemes. 

<details class="collapsible references">
  <summary class="references">References</summary>
 <ul>
<li><p>Dean III, D. C., Tisdall, M. D., Wisnowski, J. L., Feczko, E., Gagoski, B., Alexander, A. L., ... &amp; HBCD MRI Working Group. (2024). Quantifying brain development in the HEALthy Brain and Child Development (HBCD) Study: The magnetic resonance imaging and spectroscopy protocol. <em>Developmental Cognitive Neuroscience</em>, 70, 101452. <a href="https://doi.org/10.1016/j.dcn.2024.101452">10.1016/j.dcn.2024.101452</a></p></li>

<li><p>Dosenbach, N. U. F., Koller, J. M., Earl, E. A., Miranda-Dominguez, O., Klein, R. L., Van, A. N., Snyder, A. Z., Nagel, B. J., Nigg, J. T., Nguyen, A. L., Wesevich, V., Greene, D. J., & Fair, D. A. (2017). Real-time motion analytics during brain MRI improve data quality and reduce costs. <em>NeuroImage</em>, 161, 80-93. <a href="https://doi.org/10.1016/j.neuroimage.2017.08.025">https://doi.org/10.1016/j.neuroimage.2017.08.025</a></p></li>
</ul>
</details>
