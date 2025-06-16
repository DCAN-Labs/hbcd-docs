# Auditory Mismatch Negativity Task [MMN]

<div id="alert" class="alert-banner" onclick="toggleCollapse(this)">
    <span class="emoji"><i class="fas fa-exclamation-circle"></i></span>
    <span class="text-with-link">
    <span class="text">Responsible Use Warning</span>
    <a class="anchor-link" href="#alert" title="Copy link">
    <i class="fa-solid fa-link"></i>
    </a>
    </span>
  <span class="arrow">▸</span>
</div>
<div class="alert-collapsible-content">
<p>The HBCD EEG data and EEG preprocessing outputs do not contain any personally identifiable information. It is important to consider that potentially stigmatizing conclusions could emerge from the inappropriate use of the EEG data together with available demographic information or questionnaires. Furthermore, all EEG tasks are all passive at the V03 age range and therefore conclusions should not be drawn about behavioral performance.</p> 
<p>Methodologically, there are a number of best practices for responsible data use that will be included with each file. The first is selecting files that maintain a minimum trial threshold recommendation. For each task, there are three levels of quality control thresholds that can be used: (1) our QC thresholds used to provide feedback to sites on each upload, (2) a 30% trial retention threshold (which we use internally to indicate usability of an EEG recording), and (3) the reliability recommendations for each task.</p>
<p><li><b>Threshold recommendations by task:</b></li>
<li>RS - 108 trials</li>
<li>FACE - 15 trials for each condition of interest</li>
<li>MMN - 30 trials for each condition of interest</li>
<li>VEP - 36 trials.</li></p>
<p>An additional consideration for responsible use of the HBCD EEG dataset applies to disproportionate missing data. It is possible that some participant data may be systematically missing from this dataset by virtue of not meeting the QC thresholds. For instance, with infants that are inattentive and prone to fussing out during the EEG recording, more data may be removed from their datasets by our preprocessing scripts. A similar risk holds with participants  who have thick or dense hairstyling and hair texture, which may impact capping success, impedance, and data quality (<a href="https://doi.org/10.1038/s41539-024-00240-y">Adams et al., 2024</a>). The consortium has proactively worked to address this risk by using scheduling procedures that are flexible to participants hairstyling routines and by purchasing 3 long pedestal nets per site in sizes appropriate for the V03, V04, and V06 visits (<a href="https://doi.org/10.1038/s41539-024-00240-y">Adams et al., 2024</a>; <a href="https://doi.org/10.1016/j.dcn.2024.101396">Mlandu et al., 2024</a>). Preliminary analyses indicate that capping quality for visits where the long pedestal net was used have been consistent with capping quality seen for the dataset at large.</p>
<p>It is important to use these data in a manner which takes into account that physical and neurological differences between groups are not necessarily representative of intrinsic qualities of a given demographic  group. Discussions around data patterns should be sensitive to societal factors. In addition, it is important to note that variation within demographic populations is greater than variation across populations. Demographic markers are categorical proxies that cannot capture or explain the causal mechanisms that may account for evident differences.</p>
</div>

<div id="warning" class="warning-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fas fa-exclamation-triangle"></i></span>
  <span class="text-with-link">
  <span class="text">Data Warnings</span>
  <a class="anchor-link" href="#warning" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="warning-collapsible-content">
<br>
<b>HBCD EEG Utilities</b>
<p>The EEG Core of the HBCD Data Coordinating Center (HDCC) has developed some helpful tools for extracting summary statistics and trial measures from HBCD EEG release data. We encourage all users to explore these resources at the <a href="https://hbcd-eeg-utilities.readthedocs.io/">HBCD EEG Utilities</a> website.</p>
<br>
<b>Stimtracker Artifact</b>
<p>The MMN, VEP, and FACE task data for one participant included in the data release was found to contain an electrical noise artifact originating from the stimtracker device used for stimulus timing. All other participants' data were checked and confirmed to be artifact-free.</p> 
<p>This artifact is most prominent in electrode E55 between the REF and COM electrodes, but is also visible in surrounding channels. It is time-locked to both stimulus onset and offset: as highlighted in the following EEG trace (MMN auditory oddball task in E55), the artifact presents as a negative deflection at onset and a positive deflection at offset.</p>
<p><span class="emoji"><i class="fa-regular fa-lightbulb"></i></span> <i><a href="../artifacts" target="_blank">Click here</a> for information on how this artifact appears in time-frequency plots and ERP derivatives.</i></p>
<img src="../images/Fig1.png" width="70%" height="auto" class="center">
<p>The EEG workgroup is currently developing a method of ICA correction to remove this artifact. In the meantime, <strong>it is recommended to exclude the MMN, VEP, and FACE tasks for this participant from analyses</strong>. The affected subject is flagged on Lasso.</p>
<br>
<b>Task Updates Between V03 and V04/V06</b>
<p>Researchers should be aware that the interstimulus interval (ISI) changed between visits V03 and V04/V06 - see <a href="https://doi.org/10.1016/j.dcn.2024.101447">Fox et al. 2024</a> and <a href="https://doi.org/10.1097/00003446-200204000-00005">Morr et al. 2002</a> for details.</p>
</div>

## Task Details

<p>
<div id="demo-fyi" class="notification-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fa-regular fa-lightbulb"></i></span>
    <span class="text">See <a href="..">Overview</a> for a summary of EEG protocols and quality control information.</span>
</div>
</p>

Standard ("ba") and deviant ("da") auditory stimuli are presented while a video is played on an iPad to serve as a visual distractor (brightness set to maximum, in airplane mode, and unplugged). The task may be paused if breaks are needed. The `.wav` files for the auditory stimuli are 196 ms long for the “ba” stimulus and 198 ms long for the “da” stimulus.

<ul>
<strong>Trial Count:</strong>
<li>Standard condition: 569</li>
<li>Deviant condition: 98 </li>
<li>Total: 667</li>
</ul>

<ul>
<strong>Timing Details:</strong>
<li>Stimulus duration: 200 ms</li>
<li>InterStimulus interval: 820 ms (V03), 600 ms (V04/V06)</li>
<li>Total trial length: 1020 ms (V03), 800 ms (V04/V06)</li>
</ul>

A schematic of the trial progression for Visit 3 is below. See [HBCD Study Protocols - EEG](https://hbcdstudy.org/wp-content/uploads/2023/06/EEG-Parameters.pdf) for additional details.
<img src="../images/MMN.png" width="100%" height="auto" class="center">

## Resources
- [HBCD EEG Utilities](https://hbcd-eeg-utilities.readthedocs.io/)
- [HBCD E-Prime Task Manual](https://docs.google.com/document/d/1PghQQpLbxjQavtVlHyIz7JVJxlyKcC4Do8z8j7srdaI/edit?usp=sharing)
- [HBCD EEG Acquisition Protocol](https://zenodo.org/records/14795030)


### References

<div class="references">
    <p>Adams, E. J., Scott, M. E., Amarante, M., Ramírez, C. A., Rowley, S. J., Noble, K. G., & Troller-Renfree, S. V. (2024). Fostering inclusion in EEG measures of pediatric brain activity. <i>Npj Science of Learning</i>, 9(1), 27. <a href="https://doi.org/10.1038/s41539-024-00240-y" target="_blank">https://doi.org/10.1038/s41539-024-00240-y</a></p>
    <p>Fox, N. A., Pérez-Edgar, K., Morales, S., Brito, N. H., Campbell, A. M., Cavanagh, J. F., Gabard-Durnam, L. J., Hudac, C. M., Key, A. P., Larson-Prior, L. J., Pedapati, E. V., Norton, E. S., Reetzke, R., Roberts, T. P., Rutter, T. M., Scott, L. S., Shuffrey, L. C., Antúnez, M., Boylan, M. R., … Yoder, L. (2024). The development and structure of the Healthy Brain and Child Development (HBCD) study EEG Protocol. <i>Developmental Cognitive Neuroscience</i>, 69, 101447. <a href="https://doi.org/10.1016/j.dcn.2024.101447" target="_blank">https://doi.org/10.1016/j.dcn.2024.101447</a></p> 
    <p>Mlandu, N., McCormick, S. A., Davel, L., Zieff, M. R., Bradford, L., Herr, D., Jacobs, C. A., Khumalo, A., Knipe, C., Madi, Z., Mazubane, T., Methola, B., Mhlakwaphalwa, T., Miles, M., Nabi, Z. G., Negota, R., Nkubungu, K., Pan, T., Samuels, R., … Gabard-Durnam, L. J. (2024). Evaluating a novel high-density EEG sensor net structure for improving inclusivity in infants with curly or tightly coiled hair. <i>Developmental Cognitive Neuroscience</i>, 67(101396), 101396. <a href="https://doi.org/10.1016/j.dcn.2024.101396" target="_blank">https://doi.org/10.1016/j.dcn.2024.101396</a></p>
</div>
<br>