## Instrument File Naming Conventions


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
|   |__ phenotype/ <span class="hashtag"># Demographics, visit info, behavioral & other data measures</span>
|   |   |__ bio_biosample_<span class="placeholder">&lt;nails|urine&gt;</span>.* 
|   |   |__ par_visit_data.*
|   |   |__ sed_basic_demographics.* 
|   |   |__ <span class="placeholder">&lt;instrument_name&gt;</span>./
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




Geocoding data has two forms in LORIS:

* 'Geocoded Linkage from Home and Work Addresses' (sed_ld_hm) '  
* 'PhenX+ Neighborhood Safety/ Geocode' (sed_bm_nbhsaf).

The Geocoded Linkage is currently not being collected, and the 'PhenX+ Neighborhood Safety' is collected at V01, V02 and V05, but only collects 3 fields (I feel safe walking in my neighborhood, day or night; Violence is not a problem in my neighborhood; My neighborhood is safe from crime).

In addition, we have three fields set for import of data via ETL, for which we would get data directly from the WG, presumably from data collected in Ripple for Geocoding. These are in the 'Demographics', and are:

* address_completeness  
* address_present  
* sufficient_coverage

Currently the fields exist, but no data has been set up or imported.