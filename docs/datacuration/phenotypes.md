# Phenotype BIDS Data
The data provided within the `phenotype/` folder contains tabulated data from measures and instruments listed under [Data Measure Release Notes](../measures/index.md#tabulated-data). This includes behavior, demographics, visit data, toxicology results, and tabulated data associated with brain imaging and other [file-based data types](../measures/index.md#file-based-data).

Tabulated data lists information for all participants in both `.tsv` and `.parquet` format. The `.parquet` files are a columnar storage format that is optimized for performance and efficiency, while the `.tsv` files are tab-separated values files that can be easily opened in spreadsheet software or text editors. Each set of files is additionally accompanied by a `.json` metadata file that describes the structure of the data, including the names and types of each column.

<pre class="folder-tree">
bids/
|__ phenotype/
    |
    | <span class="hashtag"># BioSpecimen Data (prepended with 'bio_')</span>
    |__ bio_biosample_<span class="placeholder">&lt;nails|urine&gt;</span>.tsv
    |__ bio_biosample_<span class="placeholder">&lt;nails|urine&gt;</span>.parquet
    |__ bio_biosample_<span class="placeholder">&lt;nails|urine&gt;</span>.json
    |  
    | <span class="hashtag"># Visit Data</span>
    |__ par_visit_data.tsv
    |__ par_visit_data.parquet
    |__ par_visit_data.json
    |
    | <span class="hashtag"># Demographics Data</span>
    |__ sed_<span class="placeholder">&lt;basic_demographics|bm_demo&gt;</span>.tsv
    |__ sed_<span class="placeholder">&lt;basic_demographics|bm_demo&gt;</span>.parquet
    |__ sed_<span class="placeholder">&lt;basic_demographics|bm_demo&gt;</span>.json
    |
    | <span class="hashtag"># Instruments</span>
    |__ <span class="placeholder">&lt;instrument_name&gt;</span>.tsv
    |__ <span class="placeholder">&lt;instrument_name&gt;</span>.parquet
    |__ <span class="placeholder">&lt;instrument_name&gt;</span>.json
</pre>


## Instrument File Naming Conventions
Most protocol elements follow a standardized naming convention with the structure: `domain_source_acronym`. Note that imaging derivatives do not follow this naming schemes, but are generally understood to be under the MRI, EEG, etc. domain and strictly for the 'Child.' Each component represents the following:

- **domain**: The general domain or category the protocol element falls under (e.g., biospecimens, MRI, behavior).
- **source**: Indicates who the protocol element is about or, in some cases, who completed the assessment. The source can represent either the *respondent* (who provided the information) or the *subject* (who the data is about).
For example, `mri_ra_prep` refers to MRI-related data entered by a research assistant (RA), representing procedural details as opposed to not direct input from a child or caregiver.
- **acronym/abbreviation**: A short form or code representing the specific protocol element.


<div id="table-banner" class="table-banner" onclick="toggleCollapse(this)">
  <span class="text">Potential Values For Domain and Source</span>
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

<div id="demo-age" class="notification-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fa-regular fa-lightbulb"></i></span>
  <span class="text">FYI: Correspondance to JSON Metadata</span>
  <span class="arrow">▸</span>
</div>
<div class="collapsible-content">
<p>The <code>domain</code> and <code>source</code> are also included in the JSON metadata and are typically derived from the corresponding sections of the instrument name. However, in some cases, data are collected directly into fields or tables that do not follow the standard naming convention. In those instances, the domain and source values are added later during the Data Release process.</p>
<strong>This applies to:</strong>
<ul>
<li>BioSpecimens  </li>
<li>Imaging file based data &amp; derivatives  </li>
<li>Some session-level elements (e.g. <code>informantID</code>)  </li>
<li>Participant-level data</li>
</ul>
</div>

## Demographics Data 
<p style="margin: 0 0 5px;">Demographic (<code>sed_basic_demographics.tsv</code>) information provided for each participant includes:</p>
<ul>
<li>Gestational age at delivery</li>
<li>Sex</li>
<li>Recruitment site</li>
<li>Child demographics (race, ethnicity)</li>
<li>Birth parent's demographics (race, ethnicity, education, language at home)</li>
</ul> 

<p style="margin: 0 0 5px;">This file also includes <strong>substance use (SU) flags</strong> raised by any of the following (with details per visit provided in <a href="#visit-data">Visit Data</a>):</p>
<ul>
<li><a href="../../measures/pregexp/substanceuse#tlfb">TLFB</a> Self-reported use</li>
<li><a href="../../measures/biospec">Biospecimen results</a></li>
<li><a href="../../measures/pregexp/preghealth#instruments">Health-V2 instrument</a> (<code>pex_bm_healthv2_inf</code>) Field <code>007</code> if option 1 (NOWS - Neonatal Opioid Withdrawal Syndrome) or 5 (FAS - Fetal Alcohol Syndrome) was selected</li>
</ul>

## Visit Data
<p style="margin: 0 0 5px;">Visit data (<code>par_visit_data.tsv</code>) contains all participant visit data, including:</p>
<ul>
<li>Visit information: Label, Stage, Date, if the visit was missed, and the reason if visit was missed</li>
<li>Project, Cohort, and Site</li>
<li>Withdrawal information: if the participant withdrew from the study, the reason, and date</li>
<li>Protocol violation information: if there was a protocol exception and the date</li>
<li>Visit details for SU flags raised by TLFB, Biospecimen, or Health-V2 as described above (<a href="#demographics-data">Demographics Data</a>)</li>
</ul>

## Cohort & Caregiver Types
Cohort types included in the data release are as follows, with each listed item indicating a specific subtype or [Caregiver Type](#CGtype) (e.g., "HBCD Main Child - Postnatal Recruitment"):

- **HBCD Main Child -** *Postnatal Recruitment*, *Type A-F*
- **HBCD Multiple Birth -** *Main Child*, *Postnatal Recruitment*, *Postnatal Recruitment - Sibling*, *Type A-F*

<div id="CGtype" class="table-banner" onclick="toggleCollapse(this)">
  <span class="text">Caregiver Type A-F Definitions</span>
  <span class="arrow">▸</span>
</div>
<div class="table-open-collapsible-content">
<table style="width: 100%; border-collapse: collapse; table-layout: fixed;">
<tbody>
	<tr>
		<td>Type A</td>
		<td>Temporary Alternative Caregiver</td>
	</tr>
	<tr>
		<td>Type B</td>
		<td style="word-wrap: break-word; white-space: normal;">Change in Primary Caregiver (Placement Only) Without Change in Legal Custody (But Birth Parent Unable to Complete Visit)</td>
	</tr>
	<tr>
		<td>Type C</td>
		<td>Change in Joint Custody</td>
	</tr>
	<tr>
		<td>Type D</td>
		<td style="word-wrap: break-word; white-space: normal;">Child Removed From Birth Parent and Placed in Foster Care (Change in Placement)</td>
	</tr>
	<tr>
		<td>Type E</td>
		<td>Change in Legal Custody and Placement (e.g. adoption)</td>
	</tr>
	<tr>
		<td>Type F</td>
		<td>Original Consented Parent</td>
	</tr>            
</tbody>
</table>
</div>

## Fields Reporting Age
<p>
<div id="instrument-age" class="notification-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fa-regular fa-lightbulb"></i></span>
  <span class="text">Instrument-Specific Fields Reporting Age</span>
  <span class="arrow">▸</span>
</div>
<div class="collapsible-content">
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

<p>
<div id="demo-age" class="notification-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fa-regular fa-lightbulb"></i></span>
  <span class="text">Demographics: Fields Reporting Age</span>
  <span class="arrow">▸</span>
</div>
<div class="collapsible-content">
<br>
<i>Note that all of the following are single-point and static values.</i>
<br>
<br>
<b>Maternal Age at V01 </b> (<code>mother_age_v01</code>): 'MAV01' is the birth parent's age, obtained from the scheduled date of the V01 visit. The age is reported in years to two decimal places, with fractional years calculated by dividing the number of whole months (rounded down) by 12.
<br>
<br>
<b>Maternal Age at Delivery</b> (<code>mother_age_delivery</code>): 'MAD' is the birth parent’s age at their child’s birth. The age is reported in years to two decimal places, with fractional years calculated by dividing whole months (rounded down) by 12.
<br>
<br>
<b>Gestational Age at Delivery</b> (<code>gestational_age_delivery</code>): 'GAD' is the time from the first day of the birth parent’s last menstrual period (LMP), derived from the estimated date of delivery (EDD) minus 280 days, to the child’s birth. Reported in whole weeks, rounded down.
<br>
<br>
</div>
</p>
