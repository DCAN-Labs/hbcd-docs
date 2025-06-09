# Brain Imaging Data Structure (BIDS)
HBCD Study data included in the release are formatted and organized according to the [Brain Imaging Data Structure](https://bids-specification.readthedocs.io/en/stable/) (BIDS) standard. All release data, including [**tabulated data**](#tabulated-data) (demographics and visit information, toxicology, behavior, and tabulated data associated with file-based data) and [**file-based data**](#file-based-data) (raw and processed MRI, MRS, EEG, and motion/accelerometry data), are organized within this folder structure:

<pre class="folder-tree">
hbcd/
|__ rawdata/ 
|   |__ phenotype/     <span class="hashtag"># Tabulated Data (demographics, visit info, behavior, etc.)</span>
|   |
|   |__ sub-<span class="label">&lt;label&gt;</span>/   <span class="hashtag"># Raw File-Based Data (MRI, EEG, etc.)</span>
|       |__ ses-<span class="label">&lt;label&gt;</span>/
|           |__ <span class="placeholder">&lt;data modality&gt;</span>/
|
|__ derivatives/       <span class="hashtag"># Processed File-Based Data (MRI, EEG, etc.)</span>
    |__ <span class="placeholder">&lt;processing pipeline&gt;</span>/
</pre>


## Tabulated Data
Tabulated data, located under `rawdata/phenotype/`, refers to data from measures and instruments listed under [Data Measure Release Notes](../measures/index.md#tabulated-data). This includes behavior, demographics, visit data, toxicology results, and tabulated data associated with brain imaging and other file-based data:

<pre class="folder-tree">
hbcd/
|__ rawdata/ 
    |__ phenotype/ 
        |__ sed_basic_demographics.*        <span class="hashtag"># Basic Demographics</span>
        |__ par_visit_data.*                <span class="hashtag"># Visit Information</span>
        |__ bio_biosample_<span class="placeholder">&lt;nails|urine&gt;</span>.*   <span class="hashtag"># Toxicology</span>
        |__ <span class="placeholder">&lt;instrument_name&gt;</span>.*             <span class="hashtag"># Instrument Data</span>
</pre>

Tabulated data lists information for all participants in both plain text (`.tsv`) and Parquet (`.parquet`) formats (see example below). TSV files are tab-separated values files that can be easily opened in spreadsheet software or text editors, with metadata (including the names and types of each column) provided in a separate `.json` file. The Parquet files are a columnar storage format optimized for performance and efficiency, with metadata stored directly in the file. Each data file is additionally accompanied by a corresponding shadow matrix file (in `.tsv` and `.parquet` format) that mirrors the structure of the data file with the values replaced by reason for data missingness. Please see the page [Data Formats & Tools > Tabulated Data](../dataformats/tabulated.md) for details on these file types and how to work with them.

## File-Based Data
File-based data refers to **raw** (`rawdata/sub-<label>/`) and **processed "derivative"** (`derivatives/`) data for magnetic resonance imaging (MRI), spectroscopy (MRS), electroencephalography (EEG), and motion/accelerometry, formatted to adhere to the Brain Imaging Data Structure (BIDS) standard. See [**Raw BIDS Data**](rawbids.md) and [**Derivatives**](derivatives.md) for a detailed description of the file contents and organization of these folders.

<pre class="folder-tree">
hbcd/
|__ rawdata/ 
|   |__ sub-<span class="label">&lt;label&gt;</span>/   <span class="hashtag"># Raw File-Based Data (MRI, EEG, etc.)</span>
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
|   |__ dataset_description.json
|   |__ participants.tsv
|   |__ participants.json 
|
|__ derivatives/    <span class="hashtag"># Processed File-Based Data (MRI, EEG, etc.)</span>
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









