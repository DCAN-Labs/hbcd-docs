# Brain Imaging Data Structure (BIDS)
As much as possible, HBCD processing utilizes the [Brain Imaging Data Structure](https://bids-specification.readthedocs.io/en/stable/) (BIDS) standard for data organization. At a high level, HBCD BIDS data has the folder structure displayed below, with all data nested under `hbcd/`. The three main folders of interest are as follows: see linked sections for further details on the contents and folder structure of each.

- [Raw BIDS Data](rawbids.md) (`rawdata/sub-<label>/`): raw imaging, EEG, and motion data converted to BIDS for processing through BIDS App pipelines (see details [here](../processing/index.md))
- [Phenotype BIDS Data](phenotypes.md) (`rawdata/phenotype/`): tabulated demographic, biospecimen, and instrument data  
- [Derivatives](derivatives.md) (`derivatives/`): pre-processed imaging, EEG, and motion data derived from processing pipelines

<pre class="folder-tree">

hbcd/
|__ rawdata/ 
|   |__ sub-<span class="label">&lt;label&gt;</span>/
|   |   |__ sub-<span class="label">&lt;label&gt;</span>_sessions.tsv
|   |   |__ sub-<span class="label">&lt;label&gt;</span>_sessions.json
|   |   |__ ses-<span class="label">&lt;label&gt;</span>/
|   |       |__ anat/
|   |       |__ dwi/
|   |       |__ eeg/
|   |       |__ fmap/
|   |       |__ func/
|   |       |__ motion/
|   |       |__ mrs/
|   |       |__ sub-<span class="label">&lt;label&gt;</span>_ses-<span class="label">&lt;label&gt;</span>_scans.tsv
|   |       |__ sub-<span class="label">&lt;label&gt;</span>_ses-<span class="label">&lt;label&gt;</span>_scans.json
|   |
|   |__ phenotype/
|   |   |__ bio_biosample_<span class="placeholder">&lt;nails|urine&gt;</span>.*
|   |   |__ par_visit_data.*
|   |   |__ sed_basic_demographics.*
|   |   |__ sed_bm_demo.*
|   |   |__ <span class="placeholder">&lt;instrument_name&gt;</span>.*
|   |
|   |__ dataset_description.json
|   |__ participants.tsv
|   |__ participants.json 
|
|__ derivatives/ 
    |__ bibsnet/
    |__ hbcd_motion/
    |__ made/
    |__ mriqc/
    |__ nibabies/
    |__ osprey/
    |__ qmri_postproc/
    |__ qsiprep/
    |__ qsirecon/
    |__ symri/
    |__ xcp_d/
</pre>


