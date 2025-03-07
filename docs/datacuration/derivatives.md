# Derivatives

The `derivatives/` folder contains minimally preprocessed outputs from the [processing pipelines](../processing/pipelines.md). A description of HBCD-specific processing parameters used for each pipeline is available on the [HBCD Processing](https://hbcd-cbrain-processing.readthedocs.io/latest/) webpage. The following sections outline the session-level file and folder contents for each pipeline. 

<pre class="folder-tree">
bids/
|__ derivatives/ 
    |__ bibsnet/
    |__ hbcd_motion/
    |__ freesurfer/
    |__ made/
    |__ mcribs/
    |__ mriqc/
    |__ nibabies/
    |__ osprey/
    |__ qmri_postproc/
    |__ qsiprep/
    |__ qsirecon/
    |__ qsirecon-DIPYDKI/
    |__ qsirecon-DSIStudio/
    |__ qsirecon-NODDI/
    |__ qsirecon-TORTOISE_model-MAPMRI/
    |__ qsirecon-TORTOISE_model-tensor/
    |__ symri/
    |__ xcp_d/
</pre>

<p>
<div id="visformat" class="notification-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fa-regular fa-lightbulb"></i></span>
  <span class="text">Format of File Structure Visuals</span>
  <span class="arrow">▸</span>
</div>
<div class="collapsible-content">
<br>
<li><strong>The following formatting was employed to enhance readability of the file structure visuals:</strong></li>
<ul>
<li>The BIDS entities <code>sub-&lt;label&gt;_ses-&lt;label&gt;</code> are replaced with the string <code>SUBSES</code></li>
<li>Some entities include a set of specific values, each of which is associated with a separate file: these values are either enclosed within <code>&lt;&gt;</code> as a list, separated by <code>|</code>, or listed in a <b>Label Values Legend</b></li>
<li>For brevity, sidecar JSON files may not be displayed, in which case files with corresponding JSONs are labeled with <code>(+JSON)</code> after the filename</li>
<li>Several pipelines produce an <code>.html</code> visual summary report intended to be used for quality assessment of processed outputs. These files, typically located at either the pipeline folder or session-level, source their images from a <code>figures/</code> folder found in the derivatives. For readability, the contents of the <code>figures/</code> folders are not listed</li>
</ul>
</div>
</p>

## BIBSNet (`bibsnet/`)
BIBSNet outputs brain segmentations and masks in native T1w and T2w space as well as `volumes.tsv` files with ROI volume statistics. Additional details can be found [here](https://bibsnet.readthedocs.io/en/latest/outputs/).

<pre class="folder-tree">
bibsnet/
|__ sub-<span class="label">&lt;label&gt;</span>/
    |__ ses-<span class="label">&lt;label&gt;</span>/
        |__ anat/
            |__ <span class="subses">SUBSES</span>_space-<span class="placeholder">&lt;T1w|T2w&gt;</span>_desc-aseg_dseg.nii.gz
            |__ <span class="subses">SUBSES</span>_space-<span class="placeholder">&lt;T1w|T2w&gt;</span>_desc-aseg_dseg.json
            |__ <span class="subses">SUBSES</span>_space-<span class="placeholder">&lt;T1w|T2w&gt;</span>_desc-aseg_volumes.tsv
            |__ <span class="subses">SUBSES</span>_space-<span class="placeholder">&lt;T1w|T2w&gt;</span>_desc-aseg_volumes.json            
            |__ <span class="subses">SUBSES</span>_space-<span class="placeholder">&lt;T1w|T2w&gt;</span>_desc-aseg_brain-mask.nii.gz
            |__ <span class="subses">SUBSES</span>_space-<span class="placeholder">&lt;T1w|T2w&gt;</span>_desc-aseg_brain-mask.json
</pre>


*See [Format of File Structure Visuals](#visformat) for guidance on interpreting the folder tree above.*

## HBCD-Motion (`hbcd_motion/`)
The HBCD-Motion pipeline is used to process the HBCD Axivity Ax6 sensor recordings of infant leg movements across 72 continuous hours. Please see a full description of the output files on their webpage [here](https://hbcd-motion-postproc.readthedocs.io/en/latest/outputs.html#outputs).

<pre class="folder-tree">
hbcd_motion/
|__ sub-<span class="label">&lt;label&gt;</span>/
    |__ ses-<span class="label">&lt;label&gt;</span>/
        |__ motion/
            |__ Kinematics/
            |   |__ <span class="subses">SUBSES</span>_desc-kinematics_recording-20_motion.json
            |   |__ <span class="subses">SUBSES</span>_desc-kinematics_recording-25_motion.json
            |
            |__ PA/
            |   |__ <span class="subses">SUBSES</span>_leg-<span class="placeholder">&lt;left|right&gt;</span>_desc-accelerationPA_BOUTS.tsv
            |   |__ <span class="subses">SUBSES</span>_leg-<span class="placeholder">&lt;left|right&gt;</span>_desc-accelerationPA_LOG.txt
            |   |__ <span class="subses">SUBSES</span>_leg-<span class="placeholder">&lt;left|right&gt;</span>_desc-accelerationPA_RAW.tsv
            |   |__ <span class="subses">SUBSES</span>_leg-<span class="placeholder">&lt;left|right&gt;</span>_desc-accelerationPA_SUMMARY.json
            |   |__ <span class="subses">SUBSES</span>_leg-<span class="placeholder">&lt;left|right&gt;</span>_desc-jerkPA_BOUTS.tsv
            |   |__ <span class="subses">SUBSES</span>_leg-<span class="placeholder">&lt;left|right&gt;</span>_desc-jerkPA_LOG.txt
            |   |__ <span class="subses">SUBSES</span>_leg-<span class="placeholder">&lt;left|right&gt;</span>_desc-jerkPA_RAW.tsv
            |   |__ <span class="subses">SUBSES</span>_leg-<span class="placeholder">&lt;left|right&gt;</span>_desc-jerkPA_SUMMARY.json
            |
            |__ PARAMETERS.json
            |__ <span class="subses">SUBSES</span>_leg-<span class="placeholder">&lt;left|right&gt;</span>_desc-calibrated_recording-20_motion.tsv
</pre>
*See [Format of File Structure Visuals](#visformat) for guidance on interpreting the folder structure visual.*

## HBCD-MADE (`made/`)
HBCD-MADE produces preprocessed EEG derivatives. Please see the [HBCD-MADE webpage](https://docs-hbcd-made.readthedocs.io/en/latest) for a full explanation of the derivative files displayed below.

<pre class="folder-tree">
made/
|__ sub-<span class="label">&lt;label&gt;</span>/
    |__ ses-<span class="label">&lt;label&gt;</span>/
        |__ eeg/
            |__ filtered_data/
            |   |__ <span class="subses">SUBSES</span>_task-<span class="placeholder">&lt;FACE|MMN|RS|VEP&gt;</span>_acq-eeg_desc-filtered_eeg.fdt
            |   |__ <span class="subses">SUBSES</span>_task-<span class="placeholder">&lt;FACE|MMN|RS|VEP&gt;</span>_acq-eeg_desc-filtered_eeg.set
            |
            |__ ica_data/
            |   |__ <span class="subses">SUBSES</span>_adjustReport.txt
            |   |__ <span class="subses">SUBSES</span>_desc-mergedICA_eeg.fdt
            |   |__ <span class="subses">SUBSES</span>_desc-mergedICA_eeg.set
            | 
            |__ merged_data/
            |   |__ <span class="subses">SUBSES</span>_desc-merged_eeg.fdt
            |   |__ <span class="subses">SUBSES</span>_desc-merged_eeg.json
            |   |__ <span class="subses">SUBSES</span>_desc-merged_eeg.set
            | 
            |__ processed_data/
            |   |__ sub-<span class="label">&lt;label&gt;</span>_task-FACE_desc-<span class="placeholder">&lt;FACE-JPG&gt;</span>.jpg
            |   |__ sub-<span class="label">&lt;label&gt;</span>_task-FACE_desc-<span class="placeholder">&lt;MMN-JPG&gt;</span>.jpg
            |   |__ sub-<span class="label">&lt;label&gt;</span>_task-RS_desc-<span class="placeholder">&lt;allChAvg|allCh|ROI&gt;</span>_PSD.jpg
            |   |__ sub-<span class="label">&lt;label&gt;</span>_task-RS_spectra.csv
            |   |__ sub-<span class="label">&lt;label&gt;</span>_task-RS_spectra.mat
            |   |__ <span class="subses">SUBSES</span>_task-RS_powerSummaryStats.csv
            |   |__ sub-<span class="label">&lt;label&gt;</span>_task-VEP_<span class="placeholder">&lt;desc-oz_ERP|topo&gt;</span>.jpg
            |   |__ <span class="subses">SUBSES</span>_task-<span class="placeholder">&lt;FACE|MMN|VEP&gt;</span>_acq-eeg_ERP.mat
            |   |__ <span class="subses">SUBSES</span>_task-<span class="placeholder">&lt;FACE|MMN|RS|VEP&gt;</span>_acq-eeg_desc-filteredprocessed_eeg.fdt
            |   |__ <span class="subses">SUBSES</span>_task-<span class="placeholder">&lt;FACE|MMN|RS|VEP&gt;</span>_acq-eeg_desc-filteredprocessed_eeg.set
            |   |__ <span class="subses">SUBSES</span>_task-<span class="placeholder">&lt;FACE|MMN|VEP&gt;</span>_ERPSummaryStats.csv
            |   |__ <span class="subses">SUBSES</span>_task-<span class="placeholder">&lt;FACE|MMN|VEP&gt;</span>_ERPTrialMeasures.csv
            | 
            |__ <span class="subses">SUBSES</span>_acq-eeg_preprocessingReport.csv
            |__ <span class="subses">SUBSES</span>_task-<span class="placeholder">&lt;FACE|MMN|RS|VEP&gt;</span>_acq-eeg_MADEspecification.json
</pre>

<details open>
<summary>Label Values Legend</summary>
<p style="margin-bottom: 0; padding-bottom: 0; font-size: smaller;">
  <b style="color: #0077cc;">FACE-JPG</b>: Oz_diffERP, diffInvVsUpr_topo, diffObjVsUp2_topo, inverted_topo, object_topo, oz_ERP, upright_topo, upright2_topo
</p>
<p style="margin-bottom: 0; padding-bottom: 0; font-size: smaller;">
  <b style="color: #0077cc;">MMN-JPG</b>: deviant_topo, diffDevVsSta_topo, diffDevVsPre_topo, preDeviant_topo, standard_topo, t7t8_diffERP, t7t8_ERP
</p>
</details>

*See [Format of File Structure Visuals](#visformat) for guidance on interpreting the folder tree above.*

## MRIQC (`mriqc/`)
MRIQC extracts no-reference IQMs (image quality metrics) from structural (T1w and T2w) and functional MRI (magnetic resonance imaging) data (contained in the JSON files under `anat/` and `func/`) and also generates visual `.html` report files in the root pipeline folder. Please refer to the [MRIQC webpage](https://mriqc.readthedocs.io/en/latest/about.html) to read details about the outputs displayed below.

<pre class="folder-tree">
mriqc/
|__ sub-<span class="label">&lt;label&gt;</span>/
|   |__ ses-<span class="label">&lt;label&gt;</span>/
|       |__ anat/
|       |   |__ <span class="subses">SUBSES</span>_run-<span class="label">#</span>_T1w.json
|       |   |__ <span class="subses">SUBSES</span>_run-<span class="label">#</span>_T2w.json
|       |
|       |__ func/
|           |__ <span class="subses">SUBSES</span>_task-rest_dir-PA_run-<span class="label">#</span>_bold.json
|        
|__ <span class="subses">SUBSES</span>_run-<span class="label">#</span>_T1w.html
|__ <span class="subses">SUBSES</span>_run-<span class="label">#</span>_T2w.html
|__ <span class="subses">SUBSES</span>_task-rest_dir-PA_run-<span class="label">#</span>_bold.html
</pre>
*See [Format of File Structure Visuals](#visformat) for guidance on interpreting the folder tree above.*

## Infant-fMRIPrep (`nibabies/`)
Infant-fMRIPrep (also known as NiBabies) outputs from minimal structural and functional MRI processing include visual quality assessment reports, preprocessed derivatives, and confounds to be used for denoising in subsequent processing procedures. Please see their webpage [here](https://nibabies.readthedocs.io/en/latest/outputs.html) for a detailed description of the file outputs.

<pre class="folder-tree">
nibabies/
sub-<span class="label">&lt;label&gt;</span>/
|_ figures/
|_ ses-<span class="label">&lt;label&gt;</span>/
|  |_ log/
|  |
|  |_ anat/
|  |  |_ <span class="subses">SUBSES</span>_run-<span class="label">#</span>_desc-preproc_T2w.nii.gz <span class="hashtag">(+JSON)</span>
|  |  |_ <span class="subses">SUBSES</span>_run-<span class="label">#</span>_from-<span class="placeholder">&lt;MNI152NLin6Asym_res-2|MNIInfant+1&gt;</span>_to-T2w_mode-image_xfm.h5
|  |  |_ <span class="subses">SUBSES</span>_run-<span class="label">#</span>_from-T2w_to-<span class="placeholder">&lt;MNI152NLin6Asym_res-2|MNIInfant+1&gt;</span>_mode-image_xfm.h5
|  |  |_ <span class="subses">SUBSES</span>_run-<span class="label">#</span>_from-T2w_to-fsnative_mode-image_xfm.txt
|  |  |_ <span class="subses">SUBSES</span>_run-<span class="label">#</span>_from-fsnative_to-T2w_mode-image_xfm.txt
|  |  |_ <span class="subses">SUBSES</span>_run-<span class="label">#</span>_hemi-<span class="placeholder">&lt;L|R&gt;</span>_<span class="placeholder">&lt;curv|sulc|thickness&gt;</span>.shape.gii
|  |  |_ <span class="subses">SUBSES</span>_run-<span class="label">#</span>_hemi-<span class="placeholder">&lt;L|R&gt;</span>_<span class="placeholder">&lt;inflated|midthickness|pial|sphere|white&gt;</span>.surf.gii
|  |  |_ <span class="subses">SUBSES</span>_run-<span class="label">#</span>_hemi-<span class="placeholder">&lt;L|R&gt;</span>_space-dhcpAsym_den-32k_midthickness.surf.gii
|  |  |_ <span class="subses">SUBSES</span>_run-<span class="label">#</span>_hemi-<span class="placeholder">&lt;L|R&gt;</span>_space-dhcpAsym_den-32k_pial.surf.gii
|  |  |_ <span class="subses">SUBSES</span>_run-<span class="label">#</span>_hemi-<span class="placeholder">&lt;L|R&gt;</span>_space-dhcpAsym_den-32k_white.surf.gii
|  |  |_ <span class="subses">SUBSES</span>_run-<span class="label">#</span>_hemi-<span class="placeholder">&lt;L|R&gt;</span>_space-<span class="placeholder">&lt;dhcpAsym|fsaverage&gt;</span>_den-32k_sphere.surf.gii
|  |  |_ <span class="subses">SUBSES</span>_run-<span class="label">#</span>_space-MNI152NLin6Asym_res-2_desc-brain_mask.nii.gz <span class="hashtag">(+JSON)</span>
|  |  |_ <span class="subses">SUBSES</span>_run-<span class="label">#</span>_space-MNI152NLin6Asym_res-2_desc-preproc_T2w.nii.gz <span class="hashtag">(+JSON)</span>
|  |  |_ <span class="subses">SUBSES</span>_run-<span class="label">#</span>_space-MNI152NLin6Asym_res-2_dseg.nii.gz <span class="hashtag">(+JSON)</span>
|  |  |_ <span class="subses">SUBSES</span>_run-<span class="label">#</span>_space-<span class="placeholder">&lt;MNI152NLin6Asym_res-2|T2w&gt;</span>_label-<span class="placeholder">&lt;CSF|GM|WM&gt;</span>_probseg.nii.gz
|  |  |_ <span class="subses">SUBSES</span>_run-<span class="label">#</span>_space-T2w_desc-<span class="placeholder">&lt;aparcaseg|aseg&gt;</span>_dseg.nii.gz
|  |  |_ <span class="subses">SUBSES</span>_run-<span class="label">#</span>_space-T2w_dseg.nii.gz
|  |  |_ <span class="subses">SUBSES</span>_run-<span class="label">#</span>_space-T2w_desc-ribbon_mask.nii.gz <span class="hashtag">(+JSON)</span>
|  |  |_ <span class="subses">SUBSES</span>_run-<span class="label">#</span>_space-fsLR_den-91k_<span class="placeholder">&lt;curv|sulc|thickness&gt;</span>.dscalar.nii <span class="hashtag">(+JSON)</span>
|  |
|  |_ fmap/
|  |  |_ <span class="subses">SUBSES</span>_run-<span class="label">#</span>_fmapid-auto00000<span class="label">#</span>_desc-coeff_fieldmap.nii.gz
|  |  |_ <span class="subses">SUBSES</span>_run-<span class="label">#</span>_fmapid-auto00000<span class="label">#</span>_desc-epi_fieldmap.nii.gz
|  |  |_ <span class="subses">SUBSES</span>_run-<span class="label">#</span>_fmapid-auto00000<span class="label">#</span>_desc-preproc_fieldmap.nii.gz <span class="hashtag">(+JSON)</span>
|  |
|  |_ func/ <span class="hashtag">(ALL +JSON)</span>
|     |_ <span class="subses">SUBSES</span>-task-rest_dir-PA_run-<span class="label">#</span>_desc-brain_mask.nii.gz
|     |_ <span class="subses">SUBSES</span>-task-rest_dir-PA_run-<span class="label">#</span>_desc-confounds_timeseries.tsv
|     |_ <span class="subses">SUBSES</span>-task-rest_dir-PA_run-<span class="label">#</span>_desc-coreg_boldref.nii.gz
|     |_ <span class="subses">SUBSES</span>-task-rest_dir-PA_run-<span class="label">#</span>_desc-hmc_boldref.nii.gz 
|     |_ <span class="subses">SUBSES</span>-task-rest_dir-PA_run-<span class="label">#</span>_desc-preproc_bold.nii.gz
|     |_ <span class="subses">SUBSES</span>-task-rest_dir-PA_run-<span class="label">#</span>_from-boldref_to-T2w_mode-image_desc-coreg_xfm.txt
|     |_ <span class="subses">SUBSES</span>-task-rest_dir-PA_run-<span class="label">#</span>_from-boldref_to-auto00000_mode-image_xfm.txt
|     |_ <span class="subses">SUBSES</span>-task-rest_dir-PA_run-<span class="label">#</span>_from-orig_to-boldref_mode-image_desc-hmc_xfm.txt
|     |_ <span class="subses">SUBSES</span>-task-rest_dir-PA_run-<span class="label">#</span>_hemi-<span class="placeholder">&lt;L|R&gt;</span>_space-fsnative_bold.func.gii
|     |_ <span class="subses">SUBSES</span>-task-rest_dir-PA_run-<span class="label">#</span>_space-MNI152NLin6Asym_res-2_boldref.nii.gz
|     |_ <span class="subses">SUBSES</span>-task-rest_dir-PA_run-<span class="label">#</span>_space-MNI152NLin6Asym_res-2_desc-brain_mask.nii.gz
|     |_ <span class="subses">SUBSES</span>-task-rest_dir-PA_run-<span class="label">#</span>_space-MNI152NLin6Asym_res-2_desc-preproc_bold.nii.gz
|     |_ <span class="subses">SUBSES</span>-task-rest_dir-PA_run-<span class="label">#</span>_space-T2w_boldref.nii.gz
|     |_ <span class="subses">SUBSES</span>-task-rest_dir-PA_run-<span class="label">#</span>_space-T2w_desc-brain_mask.nii.gz
|     |_ <span class="subses">SUBSES</span>-task-rest_dir-PA_run-<span class="label">#</span>_space-T2w_desc-preproc_bold.nii.gz
|     |_ <span class="subses">SUBSES</span>-task-rest_dir-PA_run-<span class="label">#</span>_space-fsLR_den-91k_bold.dtseries.nii
|
<span class="subses">SUBSES</span>.html
</pre>

*See [Format of File Structure Visuals](#visformat) for further guidance on interpreting the folder tree above.*

### M-CRIB-S & FreeSurfer Source Directories
M-CRIB-S and FreeSurfer source directories from [Infant-fMRIPrep](#infant-fmriprep-nibabies) processing are included under `derivatives/` in the data release as well. These are intermediate pipeline outputs used for surface reconstruction, organized for the release within the `mcribs/` and `freesurfer/` folders, respectively.

#### M-CRIB-S
M-CRIB-S is a surface reconstruction method developed for neonates using the surface-based Melbourne Children's Regional Infant Brain atlases ([Adamson et al. 2020](https://doi.org/10.1038/s41598-020-61326-2)). 

*Note*: The M-CRIB-S `mcribs/SUBSES/freesurfer/` folder mostly mirrors the contents of the FreeSurfer (`derivatives/freesurfer/`) folder ([see details below](#freesurfer)), except for two symlinks replacing regular files. The visual below shows only the files unique to the M-CRIB-S `freesurfer/` folder.

<div id="symlinks" class="table-banner" onclick="toggleCollapse(this)">
  <span class="table-text">Restoring Symlink Files</span>
  <span class="notification-arrow">▸</span>
</div>
<div class="notification-collapsible-content">
<p>The M-CRIB-S subfolders (<code>TissueSeg/</code> and <code>freesurfer/mri/</code>) contain a total of 4 symlink files, which serve as references to data stored elsewhere. When these files are uploaded to the release bucket, they are renamed with the suffix <code>*_symlink_s3_object</code> to distinguish them from regular files. When downloaded, these symlink files appear as text files because they contain the S3 object path instead of the actual file content. To restore them as symlinks, run one of the following commands in the terminal:</p>
<p>Option 1: This command simply prints what commands to run to restore individual symlinks and does not change anything:</p>
<div class="copy-box">
  <div class="copy-text-container">
    <span id="specific-text-code">find . -type f -name "*_symlink_s3_object" -print | while read path ; do
  symval=$(cat "$path")
  symdir=$(dirname "$path")
  symbase=$(basename "$path" _symlink_s3_object)
  echo ln -s "$symval" "$symdir/$symbase" '&&' rm -f "$path"
done
    </span>
    <button class="copy-button">Copy</button>
  </div>
</div>

<p>Option 2: This restores all symlink files within the directory and renames them without <code>*_symlink_s3_object</code> to match the original sourcedata filenames:</p>
<div class="copy-box">
  <div class="copy-text-container">
    <span id="specific-text-code">find . -type f -name "*_symlink_s3_object" -print | while read path ; do
  symval=$(cat "$path")
  symdir=$(dirname "$path")
  symbase=$(basename "$path" _symlink_s3_object)
  ln -s "$symval" "$symdir/$symbase" && rm -f "$path" || break
done</span>
    <button class="copy-button">Copy</button>
  </div>
</div>
</div>

<pre class="folder-tree">
mcribs/
sub-<span class="label">&lt;label&gt;</span>/
|_ ses-<span class="label">&lt;label&gt;</span>/
    |__ RawT2/
    |   |__ <span class="subses">SUBSES</span>.nii.gz
    |
    |__ RawT2RadiologicalIsotropic/
    |   |__ <span class="subses">SUBSES</span>.nii.gz_symlink_s3_object
    |
    |__ SurfReconDeformable/
    |   |__ <span class="subses">SUBSES</span>/
    |       |__ meshes/
    |       |   |__ <span class="placeholder">&lt;internal|pial+internal|pial|white+internal|white&gt;</span>.vtp
    |       |   |__ pial-<span class="placeholder">&lt;lh|rh&gt;</span>-reordered.vtp
    |       |   |__ pial-<span class="placeholder">&lt;lh|rh&gt;</span>.vtp
    |       |   |__ white-<span class="placeholder">&lt;lh|rh&gt;</span>.CortexMask.curv
    |       |   |__ white-<span class="placeholder">&lt;lh|rh&gt;</span>.Normals.surf
    |       |   |__ white-<span class="placeholder">&lt;lh|rh&gt;</span>.RegionId.curv
    |       |   |__ white-<span class="placeholder">&lt;lh|rh&gt;</span>.vtp
    |       |
    |       |__ recon/
    |       |   |__ cortical-hull-dmap.nii.gz
    |       |   |__ regions.nii.gz 
    |       |
    |       |__ temp/
    |           |__ <span class="placeholder">&lt;brain|cortex&gt;</span>-mask.nii.gz
    |           |__ cerebrum-<span class="placeholder">&lt;1|2|3&gt;</span>.vtp
    |           |__ cerebrum-<span class="placeholder">&lt;lh|rh&gt;</span>-<span class="placeholder">&lt;1|2|3&gt;</span>.vtp
    |           |__ cerebrum-<span class="placeholder">&lt;lh|rh&gt;</span>-2-output_<span class="placeholder">#</span>.vtp
    |           |__ cerebrum-<span class="placeholder">&lt;lh|rh&gt;</span>-dmap.nii.gz
    |           |__ cerebrum-<span class="placeholder">&lt;lh|rh&gt;</span>-hull-<span class="placeholder">#</span>.vtp
    |           |__ cerebrum-<span class="placeholder">&lt;lh|rh&gt;</span>-iso.vtp
    |           |__ cerebrum-<span class="placeholder">&lt;lh|rh&gt;</span>-mask.nii.gz
    |           |__ corpus-callosum-mask-<span class="placeholder">&lt;1|2|3&gt;</span>.nii.gz
    |           |__ deep-gray-matter-mask-<span class="placeholder">&lt;1|2&gt;</span>.nii.gz
    |           |__ gray-matter-mask-<span class="placeholder">&lt;1|2&gt;</span>.nii.gz
    |           |__ pial-<span class="placeholder">&lt;#|#-output_#&gt;</span>.vtp
    |           |__ pial-foreground.nii.gz
    |           |__ t2w-image.nii.gz_symlink_s3_object
    |           |__ ventricles-dmap.nii.gz
    |           |__ ventricles-mask-<span class="placeholder">&lt;1|2&gt;</span>.nii.gz
    |           |__ white-<span class="placeholder">&lt;#|#-output_#&gt;</span>.vtp
    |           |__ white-foreground.nii.gz
    |           |__ white-matter-mask-<span class="placeholder">&lt;1|2&gt;</span>.nii.gz
    |
    |__ TissueSeg/
    |   |__ <span class="subses">SUBSES</span>_all_labels.nii.gz
    |   |__ <span class="subses">SUBSES</span>_all_labels_manedit.nii.gz_symlink_s3_object
    |   |__ <span class="subses">SUBSES</span>_brain_mask.nii.gz
    |   |__ <span class="subses">SUBSES</span>_t2w_restore.nii.gz_symlink_s3_object
    |
    |__ TissueSegDrawEM/
    |   |__ <span class="subses">SUBSES</span>/
    |       |__ N4/
    |           |__ <span class="subses">SUBSES</span>.nii.gz_symlink_s3_object
    |
    |__ freesurfer/ <span class="hashtag"># Only files unique to M-CRIB-S freesurfer/ folder displayed below</span>
    |   |__ <span class="subses">SUBSES</span>/
    |       |__ label/
    |       |__ mri/
    |       |   |__ brain.mgz_symlink_s3_object
    |       |   |__ orig.mgz_symlink_s3_object
    |       |__ stats/
    |       |__ surf/
    |
    |__ logs/
    |   |__ <span class="subses">SUBSES</span>.log
    |
    |__ command.txt
</pre>
*See [Format of File Structure Visuals](#visformat) for further guidance on interpreting the folder tree above.*

#### FreeSurfer
M-CRIB-S converts and organizes its output into a FreeSurfer-compatible format, provided in the `freesurfer/` folder of the Data Release. The output files follow the structure of FreeSurfer’s `recon-all` results, which are documented in the [FreeSurfer Wiki](https://surfer.nmr.mgh.harvard.edu/fswiki/ReconAllOutputFiles) and explained in [FreeSurfer Tutorial #3: Recon-all](https://andysbrainbook.readthedocs.io/en/latest/FreeSurfer/FS_ShortCourse/FS_03_ReconAll.html) from Andy's Brain Book. 

*Note*: As noted above, the `freesurfer/` folder nested under M-CRIB-S mirrors the files found in the FreeSurfer folder below. The difference (in addition to the symlink files unique to the M-CRIB-S folder) is that the latter includes 3 additional files (`scripts/mcribs.log` and `surf/<l|r>h.midthickness`).

<pre class="folder-tree">
freesurfer/
sub-<span class="label">&lt;label&gt;</span>/
|_ ses-<span class="label">&lt;label&gt;</span>/
    |__ label/
    |   |__ <span class="placeholder">&lt;lh|rh&gt;</span>.aparc+DKTatlas.annot
    |   |__ <span class="placeholder">&lt;lh|rh&gt;</span>.aparc+DKTatlas.auto.nomask.annot
    |   |__ <span class="placeholder">&lt;lh|rh&gt;</span>.aparc.annot
    |   |__ <span class="placeholder">&lt;lh|rh&gt;</span>.aparc.auto.nomask.annot
    |   |__ <span class="placeholder">&lt;lh|rh&gt;</span>.cortex.label
    |
    |__ mri/
    |   |__ T2.mgz
    |   |__ aparc+<span class="placeholder">&lt;DKTatlas&gt;</span>+aseg.mgz
    |   |__ aseg.mgz
    |   |__ aseg.<span class="placeholder">&lt;internal|presurf|presurf.preunwmfix&gt;</span>.mgz
    |   |__ brain.mgz
    |   |__ brainmask.mgz
    |   |__ <span class="placeholder">&lt;lh|rh&gt;</span>.ribbon.mgz
    |   |__ norm.mgz
    |   |__ orig.mgz
    |   |__ ribbon.mgz
    |
    |__ scripts/
    |   |__ mcribs.log
    |
    |__ stats/
    |   |__aseg.stats
    |   |__brainvol.stats
    |   |__ <span class="placeholder">&lt;lh|rh&gt;</span>.aparc+DKTatlas.stats
    |   |__ <span class="placeholder">&lt;lh|rh&gt;</span>.aparc.stats
    |   |__ <span class="placeholder">&lt;lh|rh&gt;</span>.curv.stats
    |
    |__ surf/
        |__ <span class="placeholder">&lt;lh|rh&gt;</span>.<span class="placeholder">&lt;area|area.mid|area.pial&gt;</span>
        |__ <span class="placeholder">&lt;lh|rh&gt;</span>.curv
        |__ <span class="placeholder">&lt;lh|rh&gt;</span>.inflated
        |__ <span class="placeholder">&lt;lh|rh&gt;</span>.inflated.<span class="placeholder">&lt;H|K&gt;</span>
        |__ <span class="placeholder">&lt;lh|rh&gt;</span>.midthickness
        |__ <span class="placeholder">&lt;lh|rh&gt;</span>.orig
        |__ <span class="placeholder">&lt;lh|rh&gt;</span>.pial
        |__ <span class="placeholder">&lt;lh|rh&gt;</span>.smoothwm
        |__ <span class="placeholder">&lt;lh|rh&gt;</span>.smoothwm.<span class="placeholder">&lt;BE|C|FI|H|K|K1|K2|S&gt;</span>.crv
        |__ <span class="placeholder">&lt;lh|rh&gt;</span>.smoothwm.<span class="placeholder">&lt;H|K&gt;</span>
        |__ <span class="placeholder">&lt;lh|rh&gt;</span>.sphere
        |__ <span class="placeholder">&lt;lh|rh&gt;</span>.sphere.<span class="placeholder">&lt;reg|reg2&gt;</span>
        |__ <span class="placeholder">&lt;lh|rh&gt;</span>.<span class="placeholder">&lt;sulc|thickness|volume|white&gt;</span>
</pre>
*See [Format of File Structure Visuals](#visformat) for further guidance on interpreting the folder tree above.*


## OSPREY-BIDS (`osprey/`)
OSPREY-BIDS is the BIDS extension to the OSPREY pipeline used to process HBCD magnetic resonance spectroscopy (MRS) data. Only the `HERCULES/` file tree is displayed below. The `unedited/` files generally follow similar naming conventions, with some exceptions (e.g., the BIDS field `acq-shortTE` is used instead of `acq-hercules`). Please see the [OSPREY-BIDS documentation](https://osprey-bids.readthedocs.io/en/latest/index.html) for a detailed explanation of these outputs.

<pre class="folder-tree">
osprey/
|__ sub-<span class="label">&lt;label&gt;</span>/
    |__ ses-<span class="label">&lt;label&gt;</span>/
        |__ HERCULES/
        |   |__ PreOspreyLocalizerReg/
        |   |   |__ figures/
        |   |   |__ <span class="placeholder">&lt;aal|c1|c2|c3&gt;</span>reference_seg_aligned_to_localizer.nii.gz
        |   |   |__ reference_<span class="placeholder">&lt;img|seg&gt;</span>_aligned_to_localizer.nii.gz
        |   |   |__ registration_summary.json
        |   |   |__ transform_mat.npy
        |   |   |__ readme.txt
        |   |
        |   |__ QuantifyResults/ <span class="hashtag">(ALL +JSON)</span>
        |   |   |__ <span class="placeholder">&lt;diff1|diff2|sum&gt;</span>_AlphaCorrWaterScaledGroupNormed_Voxel_1_Basis_1.tsv
        |   |   |__ <span class="placeholder">&lt;diff1|diff2|sum&gt;</span>_AlphaCorrWaterScaled_Voxel_1_Basis_1.tsv
        |   |   |__ <span class="placeholder">&lt;diff1|diff2|sum&gt;</span>_CSFWaterScaled_Voxel_1_Basis_1.tsv 
        |   |   |__ <span class="placeholder">&lt;diff1|diff2|sum&gt;</span>_TissCorrWaterScaled_Voxel_1_Basis_1.tsv
        |   |   |__ <span class="placeholder">&lt;diff1|diff2|sum&gt;</span>_amplMets_Voxel_1_Basis_1.tsv
        |   |   |__ <span class="placeholder">&lt;diff1|diff2|sum&gt;</span>_rawWaterScaled_Voxel_1_Basis_1.tsv
        |   |   |__ <span class="placeholder">&lt;diff1|diff2|sum&gt;</span>_tCr_Voxel_1_Basis_1.tsv
        |   |
        |   |__ Reports/
        |   |   |__ reportFigures/
        |   |   |__ sub-<span class="label">&lt;label&gt;</span>-report.html
        |   |
        |   |__ SegMaps/
        |   |   |__ TissueFractions_Voxel_1.tsv <span class="hashtag">(+JSON)</span>
        |   |   |__ <span class="subses">SUBSES</span>_acq-hercules_svs.nii_space-scanner_Voxel-1_label-CSF.nii.gz
        |   |   |__ <span class="subses">SUBSES</span>_acq-hercules_svs.nii_space-scanner_Voxel-1_label-GM.nii.gz
        |   |   |__ <span class="subses">SUBSES</span>_acq-hercules_svs.nii_space-scanner_Voxel-1_label-Tha.nii.gz
        |   |   |__ <span class="subses">SUBSES</span>_acq-hercules_svs.nii_space-scanner_Voxel-1_label-WM.nii.gz
        |   |
        |   |__ VoxelMasks/
        |   |   |__ <span class="subses">SUBSES</span>_acq-hercules_svs_space-scanner_mask.nii.gz
        |   |
        |   |__ LogFile.txt
        |   |__ QM_processed_spectra.tsv <span class="hashtag">(+JSON)</span>
        |   |__ SummaryMRSinMRS.md
        |   |__ subject_names_and_excluded.tsv <span class="hashtag">(+JSON)</span>
        |   |__ wrapper_settings.mat <span class="hashtag">(+JSON)</span>
        |
        |__ unedited/
</pre>
*See [Format of File Structure Visuals](#visformat) for guidance on interpreting the folder tree above.*

## qMRI Postproc (`qmri_postproc/`)
This pipeline performs minimal post-processing for SyMRI synthetic images derived from QALAS acquisition. Please visit the [qMRI PostProc webpage](https://hbcd-symri-postproc.readthedocs.io/en/latest/index.html) for a description of the file outputs below.

<pre class="folder-tree">
qmri_postproc/
|__ sub-<span class="label">&lt;label&gt;</span>/
    |__ ses-<span class="label">&lt;label&gt;</span>/
        |__ anat/  
            |__ <span class="subses">SUBSES</span>_desc-AsegROIs_scalarstats.json
            |__ <span class="subses">SUBSES</span>_desc-AsegROIs_scalarstats.tsv
            |__ <span class="subses">SUBSES</span>_desc-BilateralAsegROIs_scalarstats.json
            |__ <span class="subses">SUBSES</span>_desc-BilateralAsegROIs_scalarstats.tsv
            |__ <span class="subses">SUBSES</span>_desc-RegistrationQCAid.json
            |__ <span class="subses">SUBSES</span>_desc-RegistrationQCAid.png
            |__ <span class="subses">SUBSES</span>_space-QALAS_desc-aseg_dseg.nii.gz
            |__ <span class="subses">SUBSES</span>_space-T2w_desc-QALAS_T2map.json
            |__ <span class="subses">SUBSES</span>_space-T2w_desc-QALAS_T2map.nii.gz
</pre>
*See [Format of File Structure Visuals](#visformat) for guidance on interpreting the folder tree above.*

## QSIPrep (`qsiprep/`) 
The QSIPrep pipeline is used for preprocessing the HBCD diffusion-weighted MRI (dMRI) data. Preprocessing includes head motion correction, susceptibility distortion correction, MP-PCA denoising, coregistration to T1w images, ANTS spatial normalization, and tissue segmentation. The QSIPrep derivatives are then passed to [QSIRecon](#qsirecon) for reconstruction. Please see a full description of this pipeline on their [webpage](https://qsiprep.readthedocs.io/en/latest/). 

<pre class="folder-tree">
qsiprep/
|__ sub-<span class="label">&lt;label&gt;</span>/
    |__ log/
    |__ ses-<span class="label">&lt;label&gt;</span>/
        |__ anat/
        |   |__ <span class="subses">SUBSES</span>_from-ACPC_to-anat_mode-image_xfm.mat        
        |   |__ <span class="subses">SUBSES</span>_from-ACPC_to-MNIInfant+1_mode-image_xfm.h5
        |   |__ <span class="subses">SUBSES</span>_from-anat_to-ACPC_mode-image_xfm.mat
        |   |__ <span class="subses">SUBSES</span>_from-MNIInfant+1_to-ACPC_mode-image_xfm.h5
        |   |__ <span class="subses">SUBSES</span>_from-orig_to-anat_mode-image_xfm.txt
        |   |__ <span class="subses">SUBSES</span>_space-ACPC_desc-aseg_dseg.nii.gz
        |   |__ <span class="subses">SUBSES</span>_space-ACPC_desc-brain_mask.nii.gz
        |   |__ <span class="subses">SUBSES</span>_space-ACPC_desc-preproc_T2w.json
        |   |__ <span class="subses">SUBSES</span>_space-ACPC_desc-preproc_T2w.nii.gz
        |   |__ <span class="subses">SUBSES</span>_space-ACPC_dseg.nii.gz
        |
        |__ dwi/
        |   |__ <span class="subses">SUBSES</span>_desc-confounds_timeseries.tsv
        |   |__ <span class="subses">SUBSES</span>_desc-desc-pepolar_qc.tsv
        |   |__ <span class="subses">SUBSES</span>_space-ACPC_desc-brain_mask.nii.gz
        |   |__ <span class="subses">SUBSES</span>_space-ACPC_desc-image_qc.tsv
        |   |__ <span class="subses">SUBSES</span>_space-ACPC_desc-preproc_dwi.b
        |   |__ <span class="subses">SUBSES</span>_space-ACPC_desc-preproc_dwi.b_table.txt
        |   |__ <span class="subses">SUBSES</span>_space-ACPC_desc-preproc_dwi.bval
        |   |__ <span class="subses">SUBSES</span>_space-ACPC_desc-preproc_dwi.bvec
        |   |__ <span class="subses">SUBSES</span>_space-ACPC_desc-preproc_dwi.json
        |   |__ <span class="subses">SUBSES</span>_space-ACPC_desc-preproc_dwi.nii.gz
        |   |__ <span class="subses">SUBSES</span>_space-ACPC_desc-slice_qc.json
        |   |__ <span class="subses">SUBSES</span>_space-ACPC_dwiref.nii.gz
        |   |__ <span class="subses">SUBSES</span>_space-ACPC_model-eddy_stat-cnr_dwimap.json
        |   |__ <span class="subses">SUBSES</span>_space-ACPC_model-eddy_stat-cnr_dwimap.nii.gz
        |
        |__ figures/
        |__ <span class="subses">SUBSES</span>.html
</pre>
*See [Format of File Structure Visuals](#visformat) for guidance on interpreting the folder structure visual.*

## QSIRecon 
QSIPrep derivatives are passed to QSIRecon for reconstruction, including ODF/FOD reconstruction, tractography, Fixel estimation, and regional connectivity. The data are processed using a variety of methods and models (e.g. [Dipy](https://dipy.org/), [MRTrix](https://www.mrtrix.org/), [DSI Studio](https://dsi-studio.labsolver.org/), etc). Please see the [QSIRecon webpage](https://qsirecon.readthedocs.io/en/latest/) for a details.

<pre class="folder-tree">
derivatives/ 
|__ qsirecon/
|  |__ log/
|
|__ qsirecon-*/
    |__ sub-<span class="label">&lt;label&gt;</span>/
        |__ ses-<span class="label">&lt;label&gt;</span>/
            |__ dwi/
            |__ figures/
            |__ <span class="subses">SUBSES</span>.html    
</pre>  
*See [Format of File Structure Visuals](#visformat) for guidance on interpreting the folder trees*.

### Dipy (`qsirecon-DIPYDKI/`)
<pre class="folder-tree">
dwi/
 |__ <span class="subses">SUBSES</span>_space-ACPC_bundles-DSIStudio_scalarstats.tsv
 |__ <span class="subses">SUBSES</span>_space-<span class="placeholder">&lt;ACPC|MNIInfant+1&gt;</span>_model-dki_param-<span class="placeholder">&lt;PARAM&gt;</span>_dwimap.nii.gz <span class="hashtag">(+JSON)</span>
 |__ <span class="subses">SUBSES</span>_space-<span class="placeholder">&lt;ACPC|MNIInfant+1&gt;</span>_model-tensor_param-fa_dwimap.nii.gz <span class="hashtag">(+JSON)</span>
</pre>

<details open>
<summary>Label Values Legend</summary>
<p style="margin-bottom: 0; padding-bottom: 0; font-size: smaller;">
  <b style="color: #0077cc;">PARAM</b>: ad, ak, kfa, md, mk, mkt, rd, rk
</p>
</details>

### DSI Studio (`qsirecon-DSIStudio/`)
<pre class="folder-tree">
dwi/
|__ <span class="subses">SUBSES</span>_space-ACPC_bundles-DSIStudio_scalarstats.tsv
|__ <span class="subses">SUBSES</span>_space-ACPC_bundles-DSIStudio_tdistats.tsv
|__ <span class="subses">SUBSES</span>_space-ACPC_model-gqi_bundle-Association<span class="placeholder">&lt;ASSOC&gt;</span><span class="placeholder">&lt;L|R&gt;</span>_streamlines.tck.gz
|__ <span class="subses">SUBSES</span>_space-ACPC_model-gqi_bundle-Cerebellum<span class="placeholder">&lt;CEREB&gt;</span>_streamlines.tck.gz
|__ <span class="subses">SUBSES</span>_space-ACPC_model-gqi_bundle-CommissureAnteriorCommissure_streamlines.tck.gz
|__ <span class="subses">SUBSES</span>_space-ACPC_model-gqi_bundle-CommissureCorpusCallosum_streamlines.tck.gz
|__ <span class="subses">SUBSES</span>_space-ACPC_model-gqi_bundle-ProjectionBasalGanglia<span class="placeholder">&lt;BG&gt;</span><span class="placeholder">&lt;L|R&gt;</span>_streamlines.tck.gz
|__ <span class="subses">SUBSES</span>_space-ACPC_model-gqi_bundle-ProjectionBrainstem<span class="placeholder">&lt;BRAINSTEM&gt;</span>_streamlines.tck.gz
|__ <span class="subses">SUBSES</span>_space-ACPC_model-gqi_bundlestats.csv
|__ <span class="subses">SUBSES</span>_space-ACPC_model-gqi_dwimap.fib.gz
|__ <span class="subses">SUBSES</span>_space-ACPC_model-gqi_dwimap.fib.gz.icbm152_adult.map.gz
|__ <span class="subses">SUBSES</span>_space-ACPC_model-gqi_param-<span class="placeholder">&lt;gfa|iso&gt;</span>_dwimap.nii.gz
|__ <span class="subses">SUBSES</span>_space-ACPC_model-gqi_param-qa_dwimap.nii.gz <span class="hashtag">(+JSON)</span>
|__ <span class="subses">SUBSES</span>_space-<span class="placeholder">&lt;ACPC|MNIInfant+1&gt;</span>_model-rdi_param-<span class="placeholder">&lt;rd1|rd2&gt;</span>_dwimap.nii.gz
|__ <span class="subses">SUBSES</span>_space-<span class="placeholder">&lt;ACPC|MNIInfant+1&gt;</span>_model-tensor_param-<span class="placeholder">&lt;ad|fa|ha|md|rd&gt;</span>_dwimap.nii.gz
|__ <span class="subses">SUBSES</span>_space-<span class="placeholder">&lt;ACPC|MNIInfant+1&gt;</span>_model-tensor_param-t<span class="placeholder">&lt;xx|xy|xz|yy|yz|zz&gt;</span>_dwimap.nii.gz
|__ <span class="subses">SUBSES</span>_space-MNIInfant+1_model-gqi_param-<span class="placeholder">&lt;gfa|iso|qa&gt;</span>_dwimap.nii.gz
</pre>

<details open>
<summary>Label Values Legend</summary>
<p style="margin-bottom: 0; padding-bottom: 0; font-size: smaller;">
  <b style="color: #0077cc;">ASSOC</b>: ArcuateFasciculus, Cingulum, ExtremeCapsule, FrontalAslantTract, HippocampusAlveus, InferiorFrontoOccipitalFasciculus, InferiorLongitudinalFasciculus, MiddleLongitudinalFasciculus, ParietalAslantTract, SuperiorLongitudinalFasciculus, AssociationUncinateFasciculus, VerticalOccipitalFasciculus
</p>
<p style="margin-bottom: 0; padding-bottom: 0; font-size: smaller;">
  <b style="color: #0077cc;">CEREB</b>: Cerebellum(L/R), InferiorCerebellarPeduncle (L/R), MiddleCerebellarPeduncle, SuperiorCerebellarPeduncle, Vermis
</p>
<p style="margin-bottom: 0; padding-bottom: 0; font-size: smaller;">
  <b style="color: #0077cc;">BG</b>: AcousticRadiation, AnsaLenticularis, AnsaSubthalamica, CorticostriatalTract, FasciculusLenticularis, FasciculusSubthalamicus, Fornix, OpticRadiation, ThalamicRadiation
</p>
<p style="margin-bottom: 0; padding-bottom: 0; font-size: smaller;">
  <b style="color: #0077cc;">BRAINSTEM</b>: CorticobulbarTract(L\R), CorticopontineTract(L/R), CorticospinalTract(L/R), DentatorubrothalamicTractrl, MedialForebrainBundle(L/R), MedialLemniscus(L/R), NonDecussatingDentatorubrothalamicTract(L/R), ReticularTract(L/R)
</p>
</details>

### TORTOISE (`qsirecon-TORTOISE_model-<MAPMRI|tensor>/`)
The [TORTOISE](https://github.com/QMICodeBase/TORTOISEV4) software calculates MAPMRI and Tensor fits and scalar maps, output to derivative folders `qsirecon-TORTOISE_model-MAPMRI/` and `qsirecon-TORTOISE_model-tensor/`, respectively:

<pre class="folder-tree">
qsirecon-TORTOISE_model-MAPMRI/
 |_ dwi/ 
   |_ <span class="subses">SUBSES</span>_space-ACPC_bundles-DSIStudio_scalarstats.tsv
   |_ <span class="subses">SUBSES</span>_space-<span class="placeholder">&lt;ACPC|MNIInfant+1&gt;</span>_model-mapmri_param-<span class="placeholder">&lt;MAP-PARAM&gt;</span>_dwimap.nii.gz <span class="hashtag">(+JSON)</span>
   |_ <span class="subses">SUBSES</span>_space-<span class="placeholder">&lt;ACPC|MNIInfant+1&gt;</span>_model-tensor_param-<span class="placeholder">&lt;TENSOR-PARAM&gt;</span>_dwimap.nii.gz <span class="hashtag">(+JSON)</span>

qsirecon-TORTOISE_model-tensor/
 |_ dwi/ 
    |_ <span class="subses">SUBSES</span>_space-ACPC_bundles-DSIStudio_scalarstats.tsv
    |_ <span class="subses">SUBSES</span>_space-MNIInfant+1_model-tensor_param-<span class="placeholder">&lt;TENSOR-PARAM&gt;</span>_dwimap.nii.gz <span class="hashtag">(+JSON)</span>
</pre>

<details open>
<summary>Label Values Legend</summary>
<p style="margin-bottom: 0; padding-bottom: 0; font-size: smaller;">
  <b style="color: #0077cc;">MAP-PARAM</b>: ng, ngpar, ngperp, pa, path, rtap, rtop, rtpp
</p>
<p style="margin-bottom: 0; padding-bottom: 0; font-size: smaller;">
  <b style="color: #0077cc;">TENSOR-PARAM</b>: ad, am, fa, li, rd
</p>
</details>

## SyMRI (`symri/`)
[SyMRI](https://syntheticmr.com/products/symri-neuro/) is proprietary software for quantitative MRI. For HBCD it is used to generate synthetic contrast weighted images derived from measures of the absolute properties of [QALAS](https://pubmed.ncbi.nlm.nih.gov/25526880/) brain images. These outputs are then minimally preprocessed by [qMRI Postproc](#qmri-postproc-qmri_postproc). Files include synthetic T1w and T2w images (`SUBSES_acq-QALAS_<T1w|T2w>.nii.gz`) and derived relaxometry maps (`SUBSES_acq-QALAS_T2map.nii.gz`).
<pre class="folder-tree">
symri/
|__ sub-<span class="label">&lt;label&gt;</span>/
    |__ ses-<span class="label">&lt;label&gt;</span>/
        |__ anat/
            |__ <span class="subses">SUBSES</span>_acq-QALAS_T1w.nii.gz
            |__ <span class="subses">SUBSES</span>_acq-QALAS_T1w.json
            |__ <span class="subses">SUBSES</span>_acq-QALAS_T2map.nii.gz
            |__ <span class="subses">SUBSES</span>_acq-QALAS_T2map.json
            |__ <span class="subses">SUBSES</span>_acq-QALAS_T2w.nii.gz
            |__ <span class="subses">SUBSES</span>_acq-QALAS_T2w.json
            |__ <span class="subses">SUBSES</span>_acq-QALAS_desc-SymriContainer.log
</pre>
*See [Format of File Structure Visuals](#visformat) for guidance on interpreting the folder tree above.*


## XCP-D (`xcp_d/`)
XCP-D performs functional MRI post-processing and noise regression from Infant-fMRIPrep derivatives. Please see the [XCP-D webpage](https://xcp-d.readthedocs.io/en/latest/) to learn more and read details about the output file types.


<p style="margin-bottom: 0; padding-bottom: 0; font-size: smaller;">
  <b style="color: #0077cc;">SEG</b> label values: 4S1056Parcels, 4S156Parcels, 4S256Parcels, 4S356Parcels, 4S456Parcels, 4S556Parcels, 4S656Parcels, 4S756Parcels, 4S856Parcels, 4S956Parcels, Glasser, Gordon, HCP, MIDB, MyersLabonte, Tian
</p>

<pre class="folder-tree">
xcp_d/
sub-<span class="label">&lt;label&gt;</span>/
|_ ses-<span class="label">&lt;label&gt;</span>/
|  |_ anat/
|  |  |_ <span class="subses">SUBSES</span>_run-<span class="label">#</span>_space-MNI152NLin6Asym_desc-preproc_T2w.nii.gz
|  |  |_ <span class="subses">SUBSES</span>_run-<span class="label">#</span>_space-fsLR_seg-<span class="placeholder">&lt;SEG&gt;</span>_stat-mean_desc-curv_morph.tsv
|  |  |_ <span class="subses">SUBSES</span>_run-<span class="label">#</span>_space-fsLR_seg-<span class="placeholder">&lt;SEG&gt;</span>_stat-mean_desc-sulc_morph.tsv
|  |  |_ <span class="subses">SUBSES</span>_run-<span class="label">#</span>_space-fsLR_seg-<span class="placeholder">&lt;SEG&gt;</span>_stat-mean_desc-thickness_morph.tsv
|  |  |_ <span class="subses">SUBSES</span>_run-<span class="label">#</span>_hemi-<span class="placeholder">&lt;L|R&gt;</span>_space-fsLR_den-32k_<span class="placeholder">&lt;inflated|vinflated&gt;</span>.surf.gii
|  |  |_ <span class="subses">SUBSES</span>_run-<span class="label">#</span>_hemi-<span class="placeholder">&lt;L|R&gt;</span>_space-fsLR_den-32k_<span class="placeholder">&lt;midthickness|pial|white&gt;</span>.surf.gii
|  |  |_ <span class="subses">SUBSES</span>_run-<span class="label">#</span>_space-fsLR_den-91k_<span class="placeholder">&lt;curv|sulc|thickness&gt;</span>.dscalar.nii
|  |
|  |_ func/ <span class="hashtag"># All func files have JSONs with exception of .hdf5 & *linc_qc.tsv</span>
|     |_ <span class="subses">SUBSES</span>_task-rest_desc-abcc_qc.hdf5 <span class="hashtag">(No JSON)</span>
|     |_ <span class="subses">SUBSES</span>_task-rest_<span class="placeholder">&lt;motion|outliers&gt;</span>.tsv
|     |_ <span class="subses">SUBSES</span>_task-rest_space-fsLR_den-91k_desc-denoisedSmoothed_bold.dtseries.nii
|     |_ <span class="subses">SUBSES</span>_task-rest_space-fsLR_den-91k_desc-denoised_bold.dtseries.nii
|     |_ <span class="subses">SUBSES</span>_task-rest_space-fsLR_seg-<span class="placeholder">&lt;SEG&gt;</span>_den-91k_stat-mean_timeseries.ptseries.nii
|     |_ <span class="subses">SUBSES</span>_task-rest_space-fsLR_seg-<span class="placeholder">&lt;SEG&gt;</span>_stat-mean_timeseries.tsv
|     |_ <span class="subses">SUBSES</span>_task-rest_space-fsLR_seg-<span class="placeholder">&lt;SEG&gt;</span>_stat-pearsoncorrelation_relmat.tsv
|     |_ <span class="subses">SUBSES</span>-task-rest_dir-PA_run-<span class="label">#</span>_desc-abcc_qc.hdf5 <span class="hashtag">(No JSON)</span>
|     |_ <span class="subses">SUBSES</span>-task-rest_dir-PA_run-<span class="label">#</span>_space-fsLR_den-91k_desc-linc_qc.tsv <span class="hashtag">(No JSON)</span>
|     |_ <span class="subses">SUBSES</span>-task-rest_dir-PA_run-<span class="label">#</span>_<span class="placeholder">&lt;design|motion|outliers&gt;</span>.tsv
|     |_ <span class="subses">SUBSES</span>-task-rest_dir-PA_run-<span class="label">#</span>_space-fsLR_den-91k_desc-denoisedSmoothed_bold.dtseries.nii
|     |_ <span class="subses">SUBSES</span>-task-rest_dir-PA_run-<span class="label">#</span>_space-fsLR_den-91k_desc-denoised_bold.dtseries.nii
|     |_ <span class="subses">SUBSES</span>-task-rest_dir-PA_run-<span class="label">#</span>_space-fsLR_den-91k_stat-alff_boldmap.dscalar.nii
|     |_ <span class="subses">SUBSES</span>-task-rest_dir-PA_run-<span class="label">#</span>_space-fsLR_den-91k_stat-alff_desc-smooth_boldmap.dscalar.nii
|     |_ <span class="subses">SUBSES</span>-task-rest_dir-PA_run-<span class="label">#</span>_space-fsLR_den-91k_stat-reho_boldmap.dscalar.nii
|     |_ <span class="subses">SUBSES</span>-task-rest_dir-PA_run-<span class="label">#</span>_space-fsLR_seg-<span class="placeholder">&lt;SEG&gt;</span>_den-91k_stat-coverage_boldmap.pscalar.nii
|     |_ <span class="subses">SUBSES</span>-task-rest_dir-PA_run-<span class="label">#</span>_space-fsLR_seg-<span class="placeholder">&lt;SEG&gt;</span>_den-91k_stat-mean_timeseries.ptseries.nii
|     |_ <span class="subses">SUBSES</span>-task-rest_dir-PA_run-<span class="label">#</span>_space-fsLR_seg-<span class="placeholder">&lt;SEG&gt;</span>_den-91k_stat-pearsoncorrelation_boldmap.pconn.nii
|     |_ <span class="subses">SUBSES</span>-task-rest_dir-PA_run-<span class="label">#</span>_space-fsLR_seg-<span class="placeholder">&lt;SEG&gt;</span>_stat-alff_bold.tsv
|     |_ <span class="subses">SUBSES</span>-task-rest_dir-PA_run-<span class="label">#</span>_space-fsLR_seg-<span class="placeholder">&lt;SEG&gt;</span>_stat-coverage_bold.tsv
|     |_ <span class="subses">SUBSES</span>-task-rest_dir-PA_run-<span class="label">#</span>_space-fsLR_seg-<span class="placeholder">&lt;SEG&gt;</span>_stat-mean_timeseries.tsv
|     |_ <span class="subses">SUBSES</span>-task-rest_dir-PA_run-<span class="label">#</span>_space-fsLR_seg-<span class="placeholder">&lt;SEG&gt;</span>_stat-pearsoncorrelation_relmat.tsv
|     |_ <span class="subses">SUBSES</span>-task-rest_dir-PA_run-<span class="label">#</span>_space-fsLR_seg-<span class="placeholder">&lt;SEG&gt;</span>_stat-reho_bold.tsv
|  
|_ figures/
|
<span class="subses">SUBSES</span>_executive_summary.html
sub-<span class="label">&lt;label&gt;</span>.html
</pre>