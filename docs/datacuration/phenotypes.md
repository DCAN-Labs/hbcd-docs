# Phenotype BIDS Data
The data provided within the `rawdata/phenotype/` folder contains tabulated data from measures and instruments listed under [Data Measure Release Notes](../measures/index.md#tabulated-data). This includes behavior, demographics, visit data, toxicology results, and tabulated data associated with brain imaging and other [file-based data types](../measures/index.md#file-based-data).

Tabulated data lists information for all participants in both plain text (`.tsv`) and Parquet (`.parquet`) format. The TSV files are tab-separated values files that can be easily opened in spreadsheet software or text editors, with metadata (including the names and types of each column) provided in a separate `.json` file. The Parquet files are a columnar storage format optimized for performance and efficiency, with metadata stored directly in the file. Each data file is additionally accompanied by a corresponding shadow matrix file (in `.tsv` and `.parquet` format) that mirrors the structure of the data file with the values replaced by reason for data missingness. Please see the page [Data Formats & Tools > Tabulated Data](../dataformats/tabulated.md) for details on these file types and how to work with them.

<pre class="folder-tree">
r1.0/
|__ hbcd/
    |__ rawdata/ 
        |__ phenotype/
            | <span class="hashtag"># Visit Data</span>
            |__ par_visit_data.tsv
            |__ par_visit_data.json
            |__ par_visit_data_shadow.tsv
            |__ par_visit_data.parquet
            |__ par_visit_data_shadow.parquet
            |
            | <span class="hashtag"># Demographics Data</span>
            |__ sed_basic_demographics.tsv
            |__ sed_basic_demographics.json
            |__ sed_basic_demographics_shadow.tsv
            |__ sed_basic_demographics.parquet
            |__ sed_basic_demographics_shadow.parquet
            |
            | <span class="hashtag"># Instruments</span>
            |__ <span class="placeholder">&lt;instrument_name&gt;</span>.tsv
            |__ <span class="placeholder">&lt;instrument_name&gt;</span>.json
            |__ <span class="placeholder">&lt;instrument_name&gt;</span>_shadow.tsv
            |__ <span class="placeholder">&lt;instrument_name&gt;</span>.parquet
            |__ <span class="placeholder">&lt;instrument_name&gt;</span>_shadow.parquet
</pre>


## File Naming Conventions
Most protocol elements follow a standardized naming convention with the structure: `domain_source_acronym`. Note that imaging derivatives do not follow this naming schemes, but are generally understood to be under the MRI, EEG, etc. domain and strictly for the 'Child.' Each component represents the following:

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


## Fields Reporting Age

Note that Basic Demographics data (<code>sed_basic_demographics.tsv</code>) includes an additional set of fields reporting age - please see 

the following fields that report age at the time of instrument administration:
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
<br>
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

