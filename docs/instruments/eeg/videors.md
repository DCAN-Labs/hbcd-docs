# Video Resting State Task

**Full Name**: Video Resting State      
**Acronym**: RS         
**Table Name**: **TO DO**     

<div id="resp-use-warning" class="alert-banner" onclick="toggleCollapse(this)">
    <span class="emoji"><i class="fas fa-exclamation-circle"></i></span>
    <span class="text-with-link">
    <span class="text">Responsible Use Warning</span>
    <a class="anchor-link" href="#resp-use-warning" title="Copy link">
    <i class="fa-solid fa-link"></i>
    </a>
    </span>
  <span class="notification-arrow">▸</span>
</div>
<div class="closed-collapsible-content">
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

<div id="data-warning" class="warning-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fas fa-exclamation-triangle"></i></span>
  <span class="text-with-link">
  <span class="text">Data Warnings</span>
  <a class="anchor-link" href="#data-warning" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="notification-arrow">▸</span>
</div>
<div class="closed-collapsible-content">
<br>
<b>HBCD EEG Utilities</b>
<p>The EEG Core of the HBCD Data Coordinating Center (HDCC) has developed some helpful tools for extracting summary statistics and trial measures from HBCD EEG release data. We encourage all users to explore these resources at the <a href="https://hbcd-eeg-utilities.readthedocs.io/">HBCD EEG Utilities</a> website.</p>
<br>
<b>Stimtracker Artifact</b>
<p>The MMN, VEP, and FACE task data for one participant included in the data release was found to contain an electrical noise artifact originating from the stimtracker device used for stimulus timing. All other participants' data were checked and confirmed to be artifact-free.</p> 
<p>This artifact is most prominent in electrode E55 between the REF and COM electrodes, but is also visible in surrounding channels. It is time-locked to both stimulus onset and offset: as highlighted in the following EEG trace (MMN auditory oddball task in E55), the artifact presents as a negative deflection at onset and a positive deflection at offset. Please visit <a href="artifacts" target="_blank">this page</a> to see how this artifact appears in time-frequency plots and ERP derivatives.</p>
<img src="../images/Fig1.png" width="70%" height="auto" class="center">
<p>The EEG workgroup is currently developing a method of ICA correction to remove this artifact. In the meantime, <strong>it is recommended to exclude the MMN, VEP, and FACE tasks for this participant from analyses</strong>. The affected subject is flagged on the <a href="../../../data_access/lasso" target="_blank">Lasso platform</a>.</p>
</div>

The Video Resting State (RS) (v.11.29.23) task provides assessment of the development of large-scale neural networks during infancy and early childhood via information about neural oscillations measured in EEG power across the scalp. Developmental changes in oscillatory activity reflect underlying developing large-scale neural networks associated with early self-regulatory, cognitive, and affective processes and developmental outcomes ([Gabard-Durnam et al., 2019](https://doi.org/10.1038/s41467-019-12202-9); [Jones et al., 2020](https://doi.org/10.1038/s41598-020-67687-y); [Whedon et al., 2020](https://doi.org/10.1016/j.bandc.2020.105636)). The metrics derived from the resting EEG signal include power across the frequency spectrum ([Gabard-Durnam et al., 2019](https://doi.org/10.1038/s41467-019-12202-9)) and relative power between different scalp locations ([Davidson & Fox, 1982](https://doi.org/10.1126/science.7146906)). See [Fox et al. 2024](https://doi.org/10.1016/j.dcn.2024.101447) for more information about the RS.       

### Task Details

<p>
<div id="demo-fyi" class="notification-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fa-regular fa-lightbulb"></i></span>
    <span class="text">See the <a href="..">EEG Overview</a> for a summary of EEG protocols, quality control information, etc.</span>
</div>
</p>

Participants watch a silent video for the duration of the RS task. In **V03** (*left set of images below*), the video displays a variety of colorful and abstract toys and other visuals. In **V04 & V06** (*right set of images below*), the video includes a variety of marble run and construction visuals. See [HBCD Study Protocols - EEG](https://hbcdstudy.org/wp-content/uploads/2023/06/EEG-Parameters.pdf) for additional details.

<img src="../images/eeg-RS.png" width="100%" height="auto">

## Resources
- [HBCD EEG Utilities](https://hbcd-eeg-utilities.readthedocs.io/)
- [HBCD E-Prime Task Manual](https://docs.google.com/document/d/1PghQQpLbxjQavtVlHyIz7JVJxlyKcC4Do8z8j7srdaI/edit?usp=sharing)
- [HBCD EEG Acquisition Protocol](https://zenodo.org/records/14795030)

## References
<div class="references">
    <p>Davidson, R. J., & Fox, N. A. (1982). Asymmetrical Brain Activity Discriminates Between Positive and Negative Affective Stimuli in Human Infants. <em>Science</em>, 218(4578), 1235–1237. <a href="https://doi.org/10.1126/science.7146906" target="_blank">https://doi.org/10.1126/science.7146906</a></p>
    <p>Fox, N. A., Pérez-Edgar, K., Morales, S., Brito, N. H., Campbell, A. M., Cavanagh, J. F., Gabard-Durnam, L. J., Hudac, C. M., Key, A. P., Larson-Prior, L. J., Pedapati, E. V., Norton, E. S., Reetzke, R., Roberts, T. P., Rutter, T. M., Scott, L. S., Shuffrey, L. C., Antúnez, M., Boylan, M. R., … Yoder, L. (2024). The development and structure of the Healthy Brain and Child Development (HBCD) study EEG Protocol. <i>Developmental Cognitive Neuroscience</i>, 69, 101447. <a href="https://doi.org/10.1016/j.dcn.2024.101447" target="_blank">https://doi.org/10.1016/j.dcn.2024.101447</a></p> 
    <p>Gabard-Durnam, L. J., Wilkinson, C., Kapur, K., Tager-Flusberg, H., Levin, A. R., & Nelson, C. A. (2019). Longitudinal EEG power in the first postnatal year differentiates autism outcomes. <em>Nature Communications</em>, 10(1), Article 1. <a href="https://doi.org/10.1038/s41467-019-12202-9" target="_blank">https://doi.org/10.1038/s41467-019-12202-9</a></p>
    <p>Jones, E. J. H., Goodwin, A., Orekhova, E., Charman, T., Dawson, G., Webb, S. J., & Johnson, M. H. (2020). Infant EEG theta modulation predicts childhood intelligence. <em>Scientific Reports</em>, 10(1), 11232. <a href="https://doi.org/10.1038/s41598-020-67687-y" target="_blank">https://doi.org/10.1038/s41598-020-67687-y</a></p>
    <p>Whedon, M., Perry, N. B., & Bell, M. A. (2020). Relations between frontal EEG maturation and inhibitory control in preschool in the prediction of children’s early academic skills. <em>Brain and Cognition</em>, 145, 105636. <a href="https://doi.org/10.1016/j.bandc.2020.105636" target="_blank">https://doi.org/10.1016/j.bandc.2020.105636</a></p>
</div>
<br>

