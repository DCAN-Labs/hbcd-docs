# Tabulated Data

## Overview

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

Tabulated data lists information for all participants in both plain text (`.tsv`) and Parquet (`.parquet`) formats (see example below). TSV files are tab-separated values files that can be easily opened in spreadsheet software or text editors, with metadata (including the names and types of each column) provided in a separate `.json` file. The Parquet files are a columnar storage format optimized for performance and efficiency, with metadata stored directly in the file. Each data file is additionally accompanied by a corresponding shadow matrix file (in `.tsv` and `.parquet` format) that mirrors the structure of the data file with the values replaced by reason for data missingness. 

<p>
<div id="instrument-age" class="notification-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fa-regular fa-lightbulb"></i></span>
    <span class="text-with-link">
    <span class="text">Instrument-Specific Fields Reporting Age</span>
    <a class="anchor-link" href="#instrument-age" title="Copy link">
    <i class="fa-solid fa-link"></i>
    </a>
    </span>
  <span class="arrow">▸</span>
</div>
<div class="notification-open-collapsible-content">
<p><i>See the <a href="../../measures/agevariables">Age Variable Definitions</a> section for a summary of all age-related variables across the release, as well as the information summarized in table format <a href="../../measures/agevariables/#tabulated-instrument-data">here</a>.</i></p>

<b>Gestational Age at Administration</b> (<code>&lt;instrument_name&gt;_gestational_age</code>): 'GAA' is the time from the first day of the birth parent’s last menstrual period (LMP), estimated as EDD minus 280 days, to the instrument administration date. GAA is given in whole weeks, rounded down, for only the V01 visit. For a given participant, GAA typically varies by no more than 4 weeks across protocol elements except in cases where protocol exceptions were granted.
<br>
<br>
<b>Chronological Age at Administration</b> (<code>&lt;instrument_name&gt;_candidate_age</code>): Reported in years (to three decimal places), chronological age is the time from birth (with the birthdate jittered up to 7 days to mitigate identification risks) to the date of instrument administration (for V02 onward). It is calculated by dividing the total days elapsed (rounded down) by 365.25. Reporting in years, rather than months, ensures consistency across developmental stages (e.g., toddlerhood, childhood), while three-decimal precision compensates for birthdate adjustments, yielding values closer to actual age.
<br>
<br>
<b>Adjusted Chronological Age at Administration</b> (<code>&lt;instrument_name&gt;_adjusted_age</code>): 'ACAA' is the time elapsed between the estimated date of delivery (EDD) and date of instrument administration (for V02 onward), reported in whole weeks rounded down to the nearest week.
<br>
<br>
</div>
</p>

## File Types
Tabulated data is available in both tab-separated values (TSV) and [Apache Parquet](https://parquet.apache.org/) formats. Both formats are provided to support a range of tools and user preferences. However, **we recommend using Parquet for NBDC tabulated data to ensure correctly specified data types, faster loading speeds, and lower memory usage.**

### Plain Text vs. Parquet Files
#### Plain Text (TSV/CSV)
Plain text formats (TSV/CSV) are widely compatible and easy to inspect, but less efficient for large datasets. They don't support selective column loading or preserve metadata, such as data type specification; the metadata is instead available via the sidecar JSON files for plan text files. As a result, tools like Python or R must guess data types during import, often incorrectly. For example, categorical values like "0"/"1" for "Yes"/"No" (commonly used in NBDC datasets) may be interpreted as numeric, and columns with mostly missing values may be treated as empty if the first few rows lack data.

To avoid such issues, it's recommended to manually define column types using the accompanying data dictionaries included in the sidecar JSON metadata files during the import. The `NBDCtools` R package offers a helper function, `read_dsv_formatted()`, to automate this process (see [Recommended Programs](recprograms.md#tabulated-data) for details).

#### Parquet
<div id="parquetbids" class="notification-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fa-regular fa-lightbulb"></i></span>
  <span class="text">Note: Parquet Not Currently Supported by BIDS</span>
  <span class="arrow">▸</span>
</div>
<div class="notification-open-collapsible-content">
<p>Please note that Parquet files are currently not officially supported by the <a href="https://bids-specification.readthedocs.io/en/stable/">BIDS specification</a>. For NBDC datasets, we decided to add Parquet as an alternative file format to the BIDS standard TSV to allow users to take advantage of the features of this modern and efficient open source format that is commonly used in the data science community.</p>
</div>

[Apache Parquet](https://parquet.apache.org/) is a modern, compressed, columnar format optimized for large-scale data. In contrast to TSV files, Parquet supports selective column loading and smaller file sizes. This improves loading speed and memory usage and enhances performance for analytical workflows. Crucially, parqet can store metadata (including column types, variable/value labels, and categorical coding) directly in the file, enabling accurate import without manual setup. See details for how Parquet export is handled in [Lasso](../download/lasso.md) and [DEAP](../download/DEAP.md).

<p style="margin-bottom: 0; padding-bottom: 0;"><b>Example: Loading Parquet file in Python (using <a href="https://docs.pola.rs/">polars</a> or <a href="https://pandas.pydata.org/docs/getting_started/index.html">pandas</a> modules)</b></p>

```bash
# Using `polars` module [RECOMMENDED]:
import polars as pl
parquet_df = pl.read_parquet("path/to/file.parquet")

# Using `pandas` module:
import pandas as pd
parquet_df = pd.read_parquet("path/to/file.parquet")
```

<p style="margin-bottom: 0; padding-bottom: 0;"><b>Example: Loading Parquet file in R (<a href="https://arrow.apache.org/docs/r/">arrow</a> package):</b></p>

```bash 
# Using `arrow` package:
library(arrow)
parquet_df <- read_parquet("path/to/file.parquet")
```

### Shadow Matrices
Each TSV and Parquet ***data file*** in the BIDS `/rawdata/phenotype/` directory has a corresponding ***shadow matrix file*** in the same format (TSV or Parquet). These shadow matrix files mirror the structure and column names of the original data files. Shadow matrices can be exported as CSV files via Lasso when running a query (see details [here](../download/lasso.md#step-5-query-the-associated-data)) or downloaded in a chosen file format via [DEAP](../download/DEAP.md).

In the data files, missing values are represented as blank cells. Shadow matrices provide essential context by indicating the reason a value is missing (e.g., “don’t know,” “declined to answer,” “missed visit”). Each cell in a shadow matrix corresponds to the same cell in the associated data file:

- If a data cell contains a value, the corresponding shadow matrix cell is blank.
- If a data cell is missing, the corresponding shadow matrix cell includes a code or description indicating the reason the data is missing, as illustrated below by the <mark style="background-color: #f9cb9b; font-weight: normal;">highlighted cells</mark> in the data file (*left*) vs. the corresponding shadow matrix (*right*).

![](../images/shadowmatrix.png)

In HBCD, some participant responses like “Don’t know” or “Decline to answer” (which are typically considered non-responses) are deliberately converted to missing values in the data file, with the original response converted to a missingness reason stored in the shadow matrix. This prevents analytical errors such as inadvertently treating placeholder codes (like `777` or `999`, common in other datasets) as valid numeric values during analysis and ensures consistency in data types across all entries (e.g. text notes in numeric fields are avoided).

<div id="shadowFYI" class="notification-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fa-regular fa-lightbulb"></i></span>
  <span class="text">When should I use shadow matrices?</span>
  <span class="arrow">▸</span>
</div>
<div class="notification-open-collapsible-content">
<p>While the approach of storing missingness reasons in a shadow matrix file supports cleaner analyses, there are situations where non-responses are themselves meaningful. For example, a researcher might be interested in how often participants do not understand a given question and how this relates to other variables. In such cases, users can re-integrate the non-responses from the shadow matrix back into the data.</p>
</div>

#### Working with Shadow Matrices in R and Python 
Here we describe how researchers can use shadow matrix files in combination with the data files to, for example, explore and understand patterns of missing data or integrate missingness reasons (e.g., `Decline to Answer`, `Logic Skipped`, etc.) into your analysis. 

For working in **R**, we recommend using the `NBDCtools` package - see details [here](recprograms.md#tabulated-data). For **Python**, the following helper function joins the tabulated data file with its corresponding shadow matrix file so data columns are combined with columns providing the reasons for missingness in the same data frame. This function works with both TSV and CSV file formats, but can be updated for Parquet files using the loading logic shown under the section on Parquet files above ([here](#parquet)).

##### 🐍 Python Helper Function
```
import pandas as pd
import os

def load_data_with_shadow(data_path, shadow_path):  
    """  
    Loads a data file (CSV or TSV) and its corresponding shadow matrix  
    (CSV or TSV) and adds '_missing_reason' columns for missing values.
    """  

    # Detect delimiter from file extension and load data
    def get_delimiter(path):
        ext = os.path.splitext(path)[1].lower()
        return "\t" if ext == ".tsv" else ","

    data = pd.read_csv(data_path, delimiter=get_delimiter(data_path))  
    shadow = pd.read_csv(shadow_path, delimiter=get_delimiter(shadow_path))

    # Annotate data with non-empty missingness reason columns (excluding participant_id 
    # and session_id) in shadow matrix 
    for col in data.columns[2:]:  
        if col in shadow.columns:
            if not shadow[col].isna().all() and not (shadow[col] == '').all():
                data[f"{col}_missing_reason"] = shadow[col]

    return data

# Example usage:
df = load_data_with_shadow("data.tsv", "shadow_matrix.tsv")

# Example: View reasons for missing data for a given column/variable in the data file 
df[df["<COLUMN NAME>"].isna()][["<COLUMN NAME>_missing_reason"]]  
```

## File Naming Conventions

Most protocol elements follow a standardized naming convention with the structure: `domain_source_acronym`. Note that imaging derivatives do not follow this naming scheme, but are generally understood to be under the MRI, EEG, etc. domain and strictly for the 'Child.' Each component represents the following:

- **domain**: The general domain or category the protocol element falls under (e.g., biospecimens, MRI, behavior).
- **source**: Indicates who the protocol element is about or, in some cases, who completed the assessment. The source can represent either the *respondent* (who provided the information) or the *subject* (who the data is about).
For example, `mri_ra_prep` refers to MRI-related data entered by a research assistant (RA), representing procedural details as opposed to direct input from a child or caregiver.
- **acronym/abbreviation**: A short form or code representing the specific protocol element.

<div id="table-banner" class="table-banner" onclick="toggleCollapse(this)">
  <span class="text">Values for 'domain' and 'source' components</span>
  <span class="arrow">▸</span>
</div>
<div class="collapsible-content">
  <div style="display: flex; gap: 40px; flex-wrap: wrap;">
    <div>
      <p><strong>Possible values for <b>domain</b>:</strong></p>
      <ul>
        <li><code>bio</code> - Biospecimens</li>
        <li><code>mh</code> - Behavior/Child-Caregiver Interaction</li>
        <li><code>sed</code> - Social/Environmental Health Determinants</li>
        <li><code>sens</code> - Biosensor</li>
        <li><code>ph</code> - Physical Health</li>
        <li><code>ncl</code> - Neurocognition and Language</li>
        <li><code>nt</code> - Novel Tech</li>
        <li><code>eeg</code> - EEG</li>
        <li><code>mri</code> - MRI</li>
      </ul>
    </div>
    <div>
      <p><strong>Possible values for <b>source</b>:</strong></p>
      <ul>
        <li><code>ch</code> - Child</li>
        <li><code>bm</code> - Biological Mother</li>
        <li><code>si</code> - Sibling</li>
        <li><code>te</code> - Teacher</li>
        <li><code>cl</code> - Clinician</li>
        <li><code>ra</code> - RA (research assistant)</li>
        <li><code>ld</code> - Linked Data</li>
        <li><code>fd</code> - Family Data</li>
      </ul>
    </div>
  </div>
</div>

<div id="json-metadata" class="notification-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fa-regular fa-lightbulb"></i></span>
  <span class="text">FYI: Correspondence to JSON Metadata</span>
  <span class="arrow">▸</span>
</div>
<div class="notification-open-collapsible-content">
<p>The <code>domain</code> and <code>source</code> are also included in the JSON metadata and are typically derived from the corresponding sections of the instrument name. However, in some cases, data are collected directly into fields or tables that do not follow the standard naming convention. In those instances, the domain and source values are added later during the Data Release process.</p>
<strong>This applies to:</strong>
<ul>
<li>BioSpecimens  </li>
<li>Imaging file based data &amp; derivatives  </li>
<li>Some session-level elements (e.g. <code>informantID</code>)  </li>
<li>Participant-level data</li>
</ul>
</div>

## Exclusion Criteria

### General Rules Applied to All Data
- For all participants with only one active V01 visit, sex is changed from "Male/Female" to “Other”
- All empty strings (“”) or missing values are replaced with the default ReproSchema-compliant string “n/a”
- Some fields can have out-of-range values considered “extreme” that are changed to “n/a." Filtered fields are listed under [Filtered Out-Of-Range Field Values](#filtered-values).
  
### Static Element Exclusions
Static elements are precisely identified hard-coded elements such as participants, instruments, and instrument fields. The current data release excludes participants with a 'Postnatal Recruitment' visit as well as Multiple Birth Participants (to be included in the [interim release](../changelog/pending.md#release-11-release-date-tba)). Excluded instruments and instrument fields are as follows:

<div id="static-exclusions-dropdown" class="table-banner" onclick="toggleCollapse(this)">
    <span class="table-text">Excluded Instruments</span>
  <span class="notification-arrow">▸</span>
</div>
<div class="closed-collapsible-content">
<ul>
    <li>Biosensor Receipt Form ('sens_ch_rcpt')</li>
    <li>EEG Acquisition Checklists
    <ul>
        <li>Form ('eeg_ch_chkl')</li>
        <li>Form Reattempt - 1 ('eeg_ch_chkl_1')</li>
        <li>Form Reattempt - 2 ('eeg_ch_chkl_2')</li>
    </ul>
    <li>GABI Setup/Receipt
        <ul>
        <li>'nt_pa_gabi_setup'  </li>
        <li>'nt_pa_gabi_rcpt'  </li>
        </ul>
    </li>
    <li>ERICA forms
        <ul>
        <li>'mh_cg_erica_3_7m'  </li>
        <li>'mh_cg_erica_7_9m'  </li>
        <li>'mh_cg_erica_fcm_adm_3_7m'  </li>
        <li>'mh_cg_erica_fcm_adm_7_9m'  </li>
        </ul>
    </li>
    <li>MRI Checklists
        <ul>
        <li>Data Summary Form ('mri_ra_chkl_data')  </li>
        <li>Scan Session Summary Form ('mri_ra_chkl_scan')  </li>
        </ul>
    </li>
    <li>MRI Pre/Post Scan Prep ('mri_ra_prep')</li>
    <li>NIH Baby ToolBox ('ncl_ch_nbtb')</li>
    <li>Participant Feedback Form ('adm_cg_fb')</li>
    <li>RA Feedback ('adm_ra_fb')</li>
    <li>Participant Alerts ('admin_alert')</li>
    <li>TLFB (Timeline Follow Back) Summary Parser ('pex_ch_tlfb')</li>
    <li>Visit Level Data ('adm_fd_visitdata')</li>
    <li>Visit start ('visit_start')</li>
    <li>Urgent Events ('adm_fd_urgent')</li>
    <li>Transitions in Care Questionnaire ('sed_cg_tic')</li>
</ul>
</div>

<div id="static-exclusions-fields" class="table-banner" onclick="toggleCollapse(this)">
    <span class="table-text">Excluded Instrument Fields</span>
  <span class="notification-arrow">▸</span>
</div>
<div class="closed-collapsible-content">
<ul>
    <li>Examiner ('Examiner’)  </li>
    <li>Date of Birth (‘DOB’)  </li>
    <li>Informant (‘informant’)  </li>
    <li>Validity (‘validity’)  </li>
    <li>Duration (‘duration’)  </li>
    <li>Window Difference (‘window_difference’)  </li>
    <li>Start timestamp (‘timestamp_start’)  </li>
    <li>Stop timestamp (‘timestamp_stop’)  </li>
    <li>REDCap timestamp (‘timestamp_redcap_locked’)  </li>
    <li>Visit Data ('visit_stage' removed from the 'visit_data' category)  </li>
    <li>'Height/Weight/Head Circumference' ('ph_ch_anthro') - BMI-related fields removed  </li>
    <li>Breast Feeding History ('ph_cg_phx_i_bfh') - All fields except '001' excluded  </li>
    <li>Clinical Alerts  </li>
    <li>REDCap Complete status ('complete')  </li>
    <li>Scannable codes (BioSamples codes, tracking Nos, etc...)  </li>
    <li>Line fields</li>
</ul>
</div>

<div id="filtered-values" class="table-banner" onclick="toggleCollapse(this)">
    <span class="table-text">Filtered Out-Of-Range Field Values</span>
  <span class="notification-arrow">▸</span>
</div>
<div class="closed-collapsible-content">
<p>Some fields can have out-of-range values considered “extreme.” Values outside of the valid ranges listed for the instruments below were filtered, i.e. changed to "n/a."</p>
<table style="width: 100%; border-collapse: collapse; table-layout: fixed;">
  <thead>
    <tr>
      <th style="border: 1px solid #ddd; padding: 8px; text-align: left;">Instrument</th>
      <th style="border: 1px solid #ddd; padding: 8px; text-align: left;">Field</th>
      <th style="border: 1px solid #ddd; padding: 8px; text-align: left;">Valid Range</th>
    </tr>
  </thead>
<tbody>        
<td colspan="1" rowspan="4" style="word-wrap: break-word; white-space: normal;">Growth (<code>ph_ch_anthro</code>)</td>
    <tr>
        <td>Length (<code>len_001_i_03</code>)</td>
        <td>30 to 130 cm</td>
    </tr>     
    <tr>
        <td>Head Circumference (<code>head_001_i_03</code>)</td>
        <td>25 to 55 cm</td>
    </tr>          
    <tr>
        <td>Weight (<code>wei_001_i_03</code>)</td>
        <td>0.5 to 30 kg</td>
    </tr>         
<td colspan="1" rowspan="5" style="word-wrap: break-word; white-space: normal;">Healthv2 Inf (<code>pex_bm_healthv2_inf</code>)</td>
    <tr>
        <td><code>001_i_01</code></td>
        <td>≤ 16</td>
    </tr>     
    <tr>
        <td><code>001_i_02</code></td>
        <td>≤ 66</td>
    </tr>     
    <tr>
        <td><code>002</code></td>
        <td>12 - 51</td>
    </tr>     
    <tr>
        <td><code>002_i_01</code></td>
        <td>30 - 130</td>
    </tr>     
</tbody>
</table>
</div>
<br>

### Dynamic Element Exclusions
<div id="dynamic-exclusions-dropdown" class="table-banner" onclick="toggleCollapse(this)">
    <span class="table-text">Dynamic Element Exclusions</span>
  <span class="notification-arrow">▸</span>
</div>
<div class="closed-collapsible-content">
<ul>
<b>Participant Filters:</b>
    <li>No brain rating or brain rating noted “abnormal” are not selected</li>
    <li>Only active participants and sessions are selected</li>
    <li>Participants from Data Coordination Center (DCC) and University of Florida (UFL) sites are not selected</li>
    <li>Only participants with PSCIDs starting with “CH” are selected (excluding all test participants e.g. QI, YI, XI, PI)</li>
</ul>
<ul><b>Visit Filters:</b> Only visits whose 'LaunchPad Complete' Status was set to 'Complete' before July 1st, 2024 are included</ul>
<ul>
<b>Domain Filters:</b>
    <li>BioSpecimens</li>
    <li>Geocoding data</li>
    <li>Transition in Care</li>
    <li>REDCap surveys filled out directly in LORIS (Identified based on LORIS 'Examiner' field not set to 'REDCap')</li>
</ul>
</div>

