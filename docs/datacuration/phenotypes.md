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

Tabulated data lists information for all participants in both plain text (`.tsv`) and Parquet (`.parquet`) formats (see example below). TSV files are tab-separated values files that can be easily opened in spreadsheet software or text editors, with metadata (including the names and types of each column) provided in a separate `.json` file. The Parquet files are a columnar storage format optimized for performance and efficiency, with metadata stored directly in the file. Each data file is additionally accompanied by a corresponding shadow matrix file (in `.tsv` and `.parquet` format) that mirrors the structure of the data file with the values replaced by reason for data missingness. Please see the page [Data Formats & Tools > Tabulated Data](../dataformats/tabulated.md) for details on these file types and how to work with them.

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

