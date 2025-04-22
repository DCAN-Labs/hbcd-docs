# Electroencephalography (EEG)
EEG tasks are acquired during visits V03, V04, and V06. For full details on the HBCD EEG protocol, please refer to [Fox et al. 2024](https://doi.org/10.1016/j.dcn.2024.101447) published in the Developmental Cognitive Neuroscience special issue on HBCD.

![](images/EEG-Parameters.png)
*Source: [HBCD Study Protocols - EEG](https://hbcdstudy.org/wp-content/uploads/2023/06/EEG-Parameters.pdf)*

## Quality Control    
After EEG acquisition, quality control checks are performed using [EEG2BIDS Wizard](https://github.com/aces/eeg2bids), a custom MATLAB application installed at all HBCD sites. These checks are immediately provided to the user to ensure the data's integrity and usability. The process includes:

- Verifying event markers in the EEG data to confirm all required events are accurately recorded.
- Ensuring the setup for stimulus presentation and EEG data acquisition adheres to the study protocol.
- Inspecting electrode impedances to ensure they are within acceptable limits.
- Detecting multiple task runs and incomplete recordings.
- Confirming the use of correct E-Prime task versions.

Both study sites and the EEG Core team use an EEG Quality Control dashboard developed by LORIS to access and monitor incoming EEG data and QC metrics, such as retained epochs and line noise levels. Outputs from the HBCD-Maryland Analysis of Developmental EEG ([HBCD-MADE](https://github.com/DCAN-Labs/HBCD-MADE)) pipeline, which handles preprocessing and data cleaning, are also integrated into the dashboard. These outputs include key metrics like outlier statistics for specific task epochs ([Debnath et al., 2020](https://doi.org/10.1111/psyp.13580)). Regular site-specific check-ins and troubleshooting are conducted to ensure consistent protocol adherence and data quality across sites. For a detailed description of QC procedures in the HBCD Study EEG protocol, refer to [Fox et al. (2024)](https://doi.org/10.1016/j.dcn.2024.101447).

During quality control, a frequently observed issue across all tasks was the irregular application of EEG sensors. Additionally, partial task completion due to infant fussing and missing stimulus flags were commonly noted for the faces and auditory mismatch negativity tasks.

### EEG Net Placement ("Capping Quality") Ratings
EEG capping quality ratings are used to determine inclusion in the data release pool and subsequent processing. Photos are taken for each acquisition from the front, back, top, left, and right angles of the participant's head and uploaded via the BIDS Wizard application to a secure computing environment. They are then reviewed by the EEG Core at the University of Maryland to rate the quality of EEG net placement, or "capping quality," for each acquisition. EEG data determined as unusable due to capping quality are not included in the initial public data release, as noted under [Exclusion Criteria > EEG](../../datacuration/exclusions.md#electroencephalography). 

“Average”, "Poor," and "Not usable" ratings correspond to net placement shifted 1-2 cm, 2-3 cm, and >3 cm from proper placement, respectively. To be rated as "Excellent," acquisitions must meet the following criteria:

1.	Net placement is symmetrical with midline electrodes centered on the scalp
2.	Ears are within the ear holes and not covered by sensors 
3.	Reference electrode is placed on the vertex of the scalp
4.	Electrode E17 is placed on the nasion

Please refer to the [Official EEG Acquisition Manual](https://docs.google.com/document/d/1tjrFJzntHOqJOrq-SRGy2Z0LOj56MFsZ2ZocgrUogSs/edit?usp=sharing) for additional information about capping requirements.

## EEG Task Details
<p>
<div id="alert" class="alert-banner" onclick="toggleCollapse(this)">
    <span class="emoji"><i class="fas fa-exclamation-circle"></i></span>
    <span class="text">Responsible Use Warning</span>
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
</p>

<p>
<div id="eeg-warning" class="warning-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fas fa-exclamation-triangle"></i></span>
  <span class="text">Data Warning: HBCD EEG Utilities</span>
  <span class="arrow">▸</span>
</div>
<div class="warning-collapsible-content">
<p>The EEG Core of the HBCD Data Coordinating Center (HDCC) has developed some helpful tools for extracting summary statistics and trial measures from HBCD EEG release data. We encourage all users to explore these resources at the <a href="https://childdevlab-hbcd-eeg-utilities.readthedocs.io/">HBCD EEG Utilities</a> website.</p>
</div>
</p>

<div id="eeg-artifact-warning" class="warning-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fas fa-exclamation-triangle"></i></span>
  <span class="text">Data Warning: Stimtracker Artifact</span>
  <span class="arrow">▸</span>
</div>
<div class="warning-collapsible-content">
<p>The MMN, VEP, and FACE task data for one participant included in the data release was found to contain an electrical noise artifact originating from the stimtracker device used for stimulus timing. All other participants' data were checked and confirmed to be artifact-free.</p> 
<p>This artifact is most prominent in electrode E55 between the REF and COM electrodes, but is also visible in surrounding channels. It is time-locked to both stimulus onset and offset, presenting as a negative deflection at onset and a positive deflection at offset:</p>
<img src="images/Fig1.png" width="70%" height="auto" class="center">
<p>For additional details on how this artifact appears in time-frequency plots and ERP derivatives, please visit <a href="artifacts" target="_blank">this page</a>.</p>
<p>The EEG workgroup is currently developing a method of ICA correction to remove this artifact. In the meantime, <strong>it is recommended to exclude the MMN, VEP, and FACE tasks for this participant from analyses</strong>. The affected subject is flagged on the <a href="../../../data_access/lasso" target="_blank">Lasso platform</a>.</p>
</div>

### Faces Task (FACE)
The Faces task (v.11.29.23) is used to assess neural activity supporting face and object processing within the first years of life. Event-related potentials (ERPs) are recorded while infants view faces and objects using an oddball task designed to index different stages of processing including attention, perception, categorization, individuation, and memory. 

#### Task Details   
ERPs that index different stages of processing are computed as a function of repeated presentation of faces and objects. The ERP components elicited by the Faces task include P1, N290, and P400. 

<p>
<u><b>Face task schematic (Face vs. Object) & Task Details:</b></u>
<div style="display: flex; align-items: center;">
  <img src="images/eeg-facetask.png" alt="EEG Face Task" width="45%" height="auto">
  <div style="padding-left: 15px;">
The task consists of 2 blocks:
<blockquote>
  <p><strong>Block 1</strong>: 50 trials of upright faces and 50 trials of inverted faces <br />
  <strong>Block 2</strong>: 50 trials of upright faces and 50 trials of objects</p>
</blockquote>

Timing Details:
<blockquote>
  <p><strong>Stimulus duration</strong>: 500 ms <br />
  <strong>Interstimulus interval</strong>: 600-700 ms <br />
  <strong>Total trial length</strong>: 110-1200 ms</p>
</blockquote>
  </div>
</div></p>

If the child loses attention, an attention getter may be played to bring the child’s focus back to the task. There are a total of 36 unique images in the set, with women all displaying neutral expressions, included from each of the following self-identifying demographics: Indigenous, Black, White, Asian, Hispanic/Latino, and South Asian.  

See [HBCD Study Protocols - EEG](https://hbcdstudy.org/wp-content/uploads/2023/06/EEG-Parameters.pdf) for details and [Fox et al. 2024](https://doi.org/10.1016/j.dcn.2024.101447) for additional information on the rationale for task/stimulus development and ERP findings from pilot data.

### Auditory Mismatch Negativity Task (MMN)
<p>
<div id="mmn-warning" class="warning-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fas fa-exclamation-triangle"></i></span>
  <span class="text">Data Warning</span>
  <span class="arrow">▸</span>
</div>
<div class="warning-collapsible-content">
<p>Researchers should be aware that the interstimulus interval (ISI) was updated between V03 and V04/V06. Please see <a href="https://doi.org/10.1016/j.dcn.2024.101447">Fox et al. 2024</a> and <a href="https://doi.org/10.1097/00003446-200204000-00005">Morr et al. 2002</a> for details.</p> 
</div>
</p>

The Auditory Mismatch Negativity (MMN) Task (v.11.29.23) is designed to assess early speech sound processing in infants, incorporating rigorous quality control procedures to ensure data integrity and reliability. This task measures auditory evoked potentials and examines neural habituation and dishabituation by capturing differential responses to standard and deviant stimuli.

The resulting MMN difference wave, also known as the Mismatch Response (MMR), reflects auditory discrimination and the amplitude/latency has been associated with a range of developmental outcomes, including language ability ([Choudhury & Benasich, 2011](https://doi.org/10.1016/j.clinph.2010.05.035)), temperament and personality traits ([Gurrera et al., 2001](https://doi.org/10.1016/S0006-3223(00)01067-2); [Marshall et al., 2009](https://doi.org/10.1111/j.1467-7687.2008.00808.x)), internalizing problems ([Reeb-Sutherland et al., 2009](https://doi.org/10.1111/j.1469-7610.2009.02170.x)), externalizing and attention problems ([Gumenyuk et al., 2005](https://doi.org/10.1016/j.neulet.2004.10.081)), as well as neurodevelopmental conditions such as autism ([Lepistö et al., 2005](https://doi.org/10.1016/j.brainres.2005.10.052); [Schwartz et al., 2018](https://doi.org/10.1016/j.neubiorev.2018.01.008)) and reading difficulties/dyslexia ([Leppänen et al., 2010](https://doi.org/10.1016/j.cortex.2010.06.003); [Norton et al., 2021](https://doi.org/10.3389/fnhum.2021.624617)).

#### Task Details
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
<img src="images/MMN.png" width="100%" height="auto" class="center">

### Video Resting State (RS)
<p>
<div id="rs-warning" class="warning-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fas fa-exclamation-triangle"></i></span>
  <span class="text">Data Warning</span>
  <span class="arrow">▸</span>
</div>
<div class="warning-collapsible-content">
<p>Researchers should be aware that the video content for the video RS task was modified between V03 and V04/V06. Note that this is not a true resting state as there is a visual stimulus present.</p> 
</div>
</p>

The Video Resting State (RS) (v.11.29.23) task provides assessment of the development of large-scale neural networks during infancy and early childhood via information about neural oscillations measured in EEG power across the scalp. Developmental changes in oscillatory activity reflect underlying developing large-scale neural networks associated with early self-regulatory, cognitive, and affective processes and developmental outcomes ([Gabard-Durnam et al., 2019](https://doi.org/10.1038/s41467-019-12202-9); [Jones et al., 2020](https://doi.org/10.1038/s41598-020-67687-y); [Whedon et al., 2020](https://doi.org/10.1016/j.bandc.2020.105636)). The metrics derived from the resting EEG signal include power across the frequency spectrum ([Gabard-Durnam et al., 2019](https://doi.org/10.1038/s41467-019-12202-9)) and relative power between different scalp locations ([Davidson & Fox, 1982](https://doi.org/10.1126/science.7146906)). See [Fox et al. 2024](https://doi.org/10.1016/j.dcn.2024.101447) for more information about the RS.       

#### Task Details
Participants watch a silent video for the duration of the RS task. In **V03** (*left set of images below*), the video displays a variety of colorful and abstract toys and other visuals. In **V04 & V06** (*right set of images below*), the video includes a variety of marble run and construction visuals.

<img src="images/eeg-RS.png" width="100%" height="auto">

See [HBCD Study Protocols - EEG](https://hbcdstudy.org/wp-content/uploads/2023/06/EEG-Parameters.pdf) for additional details.

### Visual Evoked Potential Task (VEP)
The Visual Evoked Potential Task (v.11.29.23) measures development of visual cortex and response to stimuli, reflecting underlying cortical development. VEP amplitude and latency decreases with age during the first three years of life. The VEP has been associated with concurrent and later developmental outcomes as a function of prenatal substance exposures ([Margolis et al., 2024](https://psycnet.apa.org/record/2024-66755-001)), early visual enrichment or deprivation ([Jensen et al., 2019](https://doi.org/10.1038/s41598-019-39242-x)), vision system maturation ([Lippé et al., 2009](https://doi.org/10.3389/neuro.09.048.2009)), neurodevelopmental disorders (e.g., ASD and ADHD; [Cremone-Caira et al., 2023](https://doi.org/10.1007/s10803-023-06005-7); [Nazhvani et al., 2013](https://doi.org/10.1016/j.clineuro.2013.08.009)), and reading and learning disabilities ([Shandiz et al., 2017](https://doi.org/10.4103/jovr.jovr_106_16)). The morphology of the VEP likely reflects varying degrees of synaptic efficiency and as such, can be used as a readout of general cortical function. 

#### Task Details
<p>
<div style="display: flex; align-items: center;">
  <div style="padding-right: 15px;">
<p>A flashing black and white 20x20 checkerboard with a red circle in the center is shown for the duration of the task (trial counts of 60 Checkerboard A and 60 Checkerboard B for a total of 120). The task elicits a VEP response in the occipital area (Oz), consisting of N1 (first negative peak), P1 (first positive peak), and N2 (second negative peak) components. See <a href="https://doi.org/10.1016/j.dcn.2024.101447">Fox et al. 2024</a> for more information about the VEP task the <a href="https://hbcdstudy.org/wp-content/uploads/2023/06/EEG-Parameters.pdf">HBCD Study Protocols - EEG</a> for additional details.</p>
  </div>
    <img src="images/eeg-vep-checkerboard.png" alt="EEG Face Task" width="25%" height="auto">
</div></p>

## Resources
- [HBCD E-Prime Task Manual](https://docs.google.com/document/d/1PghQQpLbxjQavtVlHyIz7JVJxlyKcC4Do8z8j7srdaI/edit?usp=sharing)
- [Official EEG Acquisition Manual](https://zenodo.org/records/14795030)

## References
<div class="references">
    <p>Adams, E. J., Scott, M. E., Amarante, M., Ramírez, C. A., Rowley, S. J., Noble, K. G., & Troller-Renfree, S. V. (2024). Fostering inclusion in EEG measures of pediatric brain activity. <i>Npj Science of Learning</i>, 9(1), 27. <a href="https://doi.org/10.1038/s41539-024-00240-y" target="_blank">https://doi.org/10.1038/s41539-024-00240-y</a></p>
    <p>Barry-Anwar, R., Riggins, T., & Scott, L. S. (2020). Electrophysiology in developmental populations: Key methods and findings. In K. Cohen Kadosh (Ed.), <i>The Oxford Handbook of Developmental Cognitive Neuroscience</i>. Oxford University Press. <a href="https://doi.org/10.1093/oxfordhb/9780198827474.013.3" target="_blank">https://doi.org/10.1093/oxfordhb/9780198827474.013.3</a></p>  
    <p>Choudhury, N., & Benasich, A. A. (2011). Maturation of auditory evoked potentials from 6 to 48 months: Prediction to 3 and 4 year language and cognitive abilities. <i>Clinical Neurophysiology</i>, 122(2), 320–338. <a href="https://doi.org/10.1016/j.clinph.2010.05.035" target="_blank">https://doi.org/10.1016/j.clinph.2010.05.035</a></p>
    <p>Cremone-Caira, A., Braverman, Y., MacNaughton, G. A., Nikolaeva, J. I., & Faja, S. (2023). Reduced Visual Evoked Potential Amplitude in Autistic Children with Co-Occurring Features of Attention-Deficit/Hyperactivity Disorder. <em>Journal of Autism and Developmental Disorders</em>. <a href="https://doi.org/10.1007/s10803-023-06005-7" target="_blank">https://doi.org/10.1007/s10803-023-06005-7</a></p>
    <p>Davidson, R. J., & Fox, N. A. (1982). Asymmetrical Brain Activity Discriminates Between Positive and Negative Affective Stimuli in Human Infants. <em>Science</em>, 218(4578), 1235–1237. <a href="https://doi.org/10.1126/science.7146906" target="_blank">https://doi.org/10.1126/science.7146906</a></p>
    <p>Fox, N. A., Pérez-Edgar, K., Morales, S., Brito, N. H., Campbell, A. M., Cavanagh, J. F., Gabard-Durnam, L. J., Hudac, C. M., Key, A. P., Larson-Prior, L. J., Pedapati, E. V., Norton, E. S., Reetzke, R., Roberts, T. P., Rutter, T. M., Scott, L. S., Shuffrey, L. C., Antúnez, M., Boylan, M. R., … Yoder, L. (2024). The development and structure of the Healthy Brain and Child Development (HBCD) study EEG Protocol. <i>Developmental Cognitive Neuroscience</i>, 69, 101447. <a href="https://doi.org/10.1016/j.dcn.2024.101447" target="_blank">https://doi.org/10.1016/j.dcn.2024.101447</a></p> 
    <p>Gabard-Durnam, L. J., Wilkinson, C., Kapur, K., Tager-Flusberg, H., Levin, A. R., & Nelson, C. A. (2019). Longitudinal EEG power in the first postnatal year differentiates autism outcomes. <em>Nature Communications</em>, 10(1), Article 1. <a href="https://doi.org/10.1038/s41467-019-12202-9" target="_blank">https://doi.org/10.1038/s41467-019-12202-9</a></p>
    <p>Gumenyuk, V., Korzyukov, O., Escera, C., Hämäläinen, M., Huotilainen, M., Häyrinen, T., Oksanen, H., Näätänen, R., Von Wendt, L., & Alho, K. (2005). Electrophysiological evidence of enhanced distractibility in ADHD children. <i>Neuroscience Letters</i>, 374(3), 212–217. <a href="https://doi.org/10.1016/j.neulet.2004.10.081" target="_blank">https://doi.org/10.1016/j.neulet.2004.10.081</a></p>  
    <p>Gurrera, R. J., O’Donnell, B. F., Nestor, P. G., Gainski, J., & McCarley, R. W. (2001). The P3 auditory event–related brain potential indexes major personality traits. <i>Biological Psychiatry</i>, 49(11), 922–929. <a href="https://doi.org/10.1016/S0006-3223(00)01067-2" target="_blank">https://doi.org/10.1016/S0006-3223(00)01067-2</a></p> 
    <p>Jensen, S. K. G., Kumar, S., Xie, W., Tofail, F., Haque, R., Petri, W. A., & Nelson, C. A. (2019). Neural correlates of early adversity among Bangladeshi infants. <em>Scientific Reports</em>, 9(1), 3507. <a href="https://doi.org/10.1038/s41598-019-39242-x" target="_blank">https://doi.org/10.1038/s41598-019-39242-x</a></p>
    <p>Jones, E. J. H., Goodwin, A., Orekhova, E., Charman, T., Dawson, G., Webb, S. J., & Johnson, M. H. (2020). Infant EEG theta modulation predicts childhood intelligence. <em>Scientific Reports</em>, 10(1), 11232. <a href="https://doi.org/10.1038/s41598-020-67687-y" target="_blank">https://doi.org/10.1038/s41598-020-67687-y</a></p>
    <p>Lachmann, T., Berti, S., Kujala, T., & Schröger, E. (2005). Diagnostic subgroups of developmental dyslexia have different deficits in neural processing of tones and phonemes. <i>International Journal of Psychophysiology</i>, 55(2), 105–120. <a href="https://doi.org/10.1016/j.ijpsycho.2004.11.005" target="_blank">https://doi.org/10.1016/j.ijpsycho.2004.11.005</a></p>  
    <p>Lepistö, T., Kujala, T., Vanhala, R., Alku, P., Huotilainen, M., & Näätänen, R. (2005). The discrimination of and orienting to speech and non-speech sounds in children with autism. <i>Brain Research</i>, 1066(1–2), 147–157. <a href="https://doi.org/10.1016/j.brainres.2005.10.052" target="_blank">https://doi.org/10.1016/j.brainres.2005.10.052</a></p>  
    <p>Leppänen, P. H. T., Hämäläinen, J. A., Salminen, H. K., Eklund, K. M., Guttorm, T. K., Lohvansuu, K., Puolakanaho, A., & Lyytinen, H. (2010). Newborn brain event-related potentials revealing atypical processing of sound frequency and the subsequent association with later literacy skills in children with familial dyslexia. <i>Cortex</i>, 46(10), 1362–1376. <a href="https://doi.org/10.1016/j.cortex.2010.06.003" target="_blank">https://doi.org/10.1016/j.cortex.2010.06.003</a></p>
    <p>Lippé, S., Kovacevic, N., & McIntosh, A. R. (2009). Differential Maturation of Brain Signal Complexity in the Human Auditory and Visual System. <em>Frontiers in Human Neuroscience</em>, 3, 48. <a href="https://doi.org/10.3389/neuro.09.048.2009" target="_blank">https://doi.org/10.3389/neuro.09.048.2009</a></p>
    <p>Margolis, E. T., Davel, L., Bourke, N. J., Bosco, C., Zieff, M. R., Monachino, A. D., Mazubane, T., Williams, S. R., Miles, M., & Jacobs, C. A. (2024). Longitudinal effects of prenatal alcohol exposure on visual neurodevelopment over infancy. <em>Developmental Psychology</em>. <a href="https://psycnet.apa.org/record/2024-66755-001" target="_blank">https://psycnet.apa.org/record/2024-66755-001</a></p>
    <p>Markant, J., & Scott, L. S. (2018). Attention and Perceptual Learning Interact in the Development of the Other-Race Effect. <i>Current Directions in Psychological Science</i>, <i>27</i>(3), 163–169. <a href="https://doi.org/10.1177/0963721418769884" target="_blank">https://doi.org/10.1177/0963721418769884</a></p>  
    <p>Marshall, P. J., Reeb, B. C., & Fox, N. A. (2009). Electrophysiological responses to auditory novelty in temperamentally different 9-month-old infants. <i>Developmental Science</i>, 12(4), 568–582. <a href="https://doi.org/10.1111/j.1467-7687.2008.00808.x" target="_blank">https://doi.org/10.1111/j.1467-7687.2008.00808.x</a></p>
    <p>Mlandu, N., McCormick, S. A., Davel, L., Zieff, M. R., Bradford, L., Herr, D., Jacobs, C. A., Khumalo, A., Knipe, C., Madi, Z., Mazubane, T., Methola, B., Mhlakwaphalwa, T., Miles, M., Nabi, Z. G., Negota, R., Nkubungu, K., Pan, T., Samuels, R., … Gabard-Durnam, L. J. (2024). Evaluating a novel high-density EEG sensor net structure for improving inclusivity in infants with curly or tightly coiled hair. <i>Developmental Cognitive Neuroscience</i>, 67(101396), 101396. <a href="https://doi.org/10.1016/j.dcn.2024.101396" target="_blank">https://doi.org/10.1016/j.dcn.2024.101396</a></p>
    <p>Morr, M. L., Shafer, V. L., Kreuzer, J. A., & Kurtzberg, D. (2002). Maturation of mismatch negativity in typically developing infants and preschool children. <i>Ear and Hearing</i>, 23(2), 118–136. <a href="https://doi.org/10.1097/00003446-200204000-00005" target="_blank">https://doi.org/10.1097/00003446-200204000-00005</a></p>  
    <p>Nazhvani, A. D., Boostani, R., Afrasiabi, S., & Sadatnezhad, K. (2013). Classification of ADHD and BMD patients using visual evoked potential. <em>Clinical Neurology and Neurosurgery</em>, 115(11), 2329–2335. <a href="https://doi.org/10.1016/j.clineuro.2013.08.009" target="_blank">https://doi.org/10.1016/j.clineuro.2013.08.009</a></p>
    <p>Norton, E. S., Beach, S. D., Eddy, M. D., McWeeny, S., Ozernov-Palchik, O., Gaab, N., & Gabrieli, J. D. E. (2021). ERP mismatch negativity amplitude and asymmetry reflect phonological and rapid automatized naming skills in English-speaking kindergartners. <i>Frontiers in Human Neuroscience</i>, 15, 624617. <a href="https://doi.org/10.3389/fnhum.2021.624617" target="_blank">https://doi.org/10.3389/fnhum.2021.624617</a></p>  
    <p>Reeb-Sutherland, B. C., Vanderwert, R. E., Degnan, K. A., Marshall, P. J., Pérez-Edgar, K., Chronis-Tuscano, A., Pine, D. S., & Fox, N. A. (2009). Attention to novelty in behaviorally inhibited adolescents moderates risk for anxiety. <i>Journal of Child Psychology and Psychiatry</i>, 50(11), 1365–1372. <a href="https://doi.org/10.1111/j.1469-7610.2009.02170.x" target="_blank">https://doi.org/10.1111/j.1469-7610.2009.02170.x</a></p> 
    <p>Shandiz, J. H., Heyrani, M., Sobhani-Rad, D., Salehinejad, Z., Shojaei, S., Khoshsima, M. J., Azimi, A., Yekta, A. A., & Yazdi, S. H. H. (2017). Pattern Visual Evoked Potentials in Dyslexic Children. <em>Journal of Ophthalmic & Vision Research</em>, 12(4), 402–406. <a href="https://doi.org/10.4103/jovr.jovr_106_16" target="_blank">https://doi.org/10.4103/jovr.jovr_106_16</a></p> 
    <p>Scherf, K. S., & Scott, L. S. (2012). Connecting developmental trajectories: Biases in face processing from infancy to adulthood. <i>Developmental Psychobiology</i>, <i>54</i>(6), 643–663. <a href="https://doi.org/10.1002/dev.21013" target="_blank">https://doi.org/10.1002/dev.21013</a></p>  
    <p>Schwartz, S., Shinn-Cunningham, B., & Tager-Flusberg, H. (2018). Meta-analysis and systematic review of the literature characterizing auditory mismatch negativity in individuals with autism. <i>Neuroscience and Biobehavioral Reviews</i>, 87, 106–117. <a href="https://doi.org/10.1016/j.neubiorev.2018.01.008" target="_blank">https://doi.org/10.1016/j.neubiorev.2018.01.008</a></p> 
    <p>Whedon, M., Perry, N. B., & Bell, M. A. (2020). Relations between frontal EEG maturation and inhibitory control in preschool in the prediction of children’s early academic skills. <em>Brain and Cognition</em>, 145, 105636. <a href="https://doi.org/10.1016/j.bandc.2020.105636" target="_blank">https://doi.org/10.1016/j.bandc.2020.105636</a></p>
</div>
<br>

