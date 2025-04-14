# Stimtracker Artifact

## Background
Two subjects in the data release were found to have an electrical noise artifact originating from the stimtracker device used for stimuli timing. The artifact is especially apparent in the E55 electrode between the REF and COM electrodes, but does appear in a few surrounding channels as well. This artifact is time-locked to the stimulus onset and offset. This artifact appears in the data for the VEP, FACE, and MMN tasks for one subject and in the MMN task only for the other subject. It does not appear in the resting state data. No other participants show this artifact at channel E55.

<figure>
  <img src="../images/Fig1.png" alt="Figure 1">
  <figcaption style="font-size: 0.9em;"><b>Figure 1. Example of the electrical artifact detected in the MMN auditory oddball task in E55. The artifact is characterized by the negative deflection of the signal at the stimulus onset and the positive deflection of the signal at offset.</figcaption>
</figure>

## Time-Frequency Plots
<figure>
  <img src="../images/Fig2.png" alt="Figure 2">
  <figcaption style="font-size: 0.9em;"><b>Figure 2. Time-frequency plots (1-30 Hz) of all data release subjects at E55.</figcaption>
</figure>

<figure>
  <img src="../images/Fig3.png" alt="Figure 3">
  <figcaption style="font-size: 0.9em;"><b>Figure 3. Time-frequency plots overlaid by electrode position for subject data with artifact. Note that there is an influence of this artifact in the electrodes surrounding E55.</figcaption>
</figure>

<figure>
  <img src="../images/Fig4.png" alt="Figure 4">
  <figcaption style="font-size: 0.9em;"><b>Figure 4. Average time-frequency across all subjects at E55 including subject data with artifact on the left and excluding it on the right.</figcaption>
</figure>

<figure>
  <img src="../images/Fig5.png" alt="Figure 5">
  <figcaption style="font-size: 0.9em;"><b>Figure 5. Time-frequency of all data of other release subjects, excluding subject data with artifact, at E55. None of these participants show the artifact at E55.</figcaption>
</figure>

## Effects On ERP Derivatives 
While the artifact is present at channel E55, it does not appear in the regions of interest (ROIs) for the VEP and FACE tasks.

<figure>
  <img src="../images/Fig6.png" alt="Figure 6">
  <figcaption style="font-size: 0.9em;"><b>Figure 6. VEP data for the Oz ROI for subject data with artifact. The artifact does not appear in this ROI.</figcaption>
</figure>

<figure>
  <img src="../images/Fig7.png" alt="Figure 7">
  <figcaption style="font-size: 0.9em;"><b>Figure 7. FACE data from the Oz ROI for subject data with artifact. The artifact does not appear in this ROI.</figcaption>
</figure>

For the MMN task, channel E55 is not used in the T7/T8 ROI, and the artifact does not appear in this region. However, the FCz cluster includes electrodes E12 and E112 which may be affected by the artifact.

<figure>
  <img src="../images/Fig8.png" alt="Figure 8">
  <figcaption style="font-size: 0.9em;"><b>Figure 8. MMN data from the T7/T8 ROI for subject data with artifact. The artifact does not appear in this region.</figcaption>
</figure>

<figure>
  <img src="../images/Fig9.png" alt="Figure 9">
  <figcaption style="font-size: 0.9em;"><b>Figure 9. MMN data from the FCz ROI for subject data with artifact. The artifact may appear in this data.</figcaption>
</figure>


## Recommendations For Use
Due to the presence of this artifact, the EEG working group recommends that one subject be excluded from any analyses using the MMN task and a second subject be excluded from any analyses using VEP, FACE, and MMN tasks.

## Note For Future Data Releases
The EEG working group is currently developing a method of ICA correction to remove this artifact.
