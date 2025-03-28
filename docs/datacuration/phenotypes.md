# Phenotype BIDS Data
The data provided within the `phenotype/` folder contains tabulated data, including demographic, toxicology, and behavior. It also includes data associated with magnetic resonance imaging (MRI), spectroscopy (MRS), electroencephalography (EEG), and motion/accelerometry data (from [wearable sensor](../measures/sensors.md) recordings for leg motion). See the full list of included instruments and measures in the [Data Measures](../measures/index.md#data-measure-release-notes) overview of the Release Notes.

Tabulated data is provided in both `.tsv` and `.parquet` formats and contain information for all participants. The `.parquet` files are a columnar storage format that is optimized for performance and efficiency, while the `.tsv` files are tab-separated values files that can be easily opened in spreadsheet software or text editors. Each set of files is additionally accompanied by a `.json` file that describes the structure of the data, including the names and types of each column, as well as any additional metadata.

<pre class="folder-tree">
bids/
|__ phenotype/
    |
    | <span class="hashtag"># BioSpecimen Data</span>
    |__ bio_biosample_nails.tsv
    |__ bio_biosample_nails.json
    |__ bio_biosample_urine.tsv
    |__ bio_biosample_urine.json
    |  
    | <span class="hashtag"># Visit Data</span>
    |__ par_visit_data.tsv
    |__ par_visit_data.json
    |
    | <span class="hashtag"># Demographics Data</span>
    |__ sed_basic_demographics.tsv
    |__ sed_basic_demographics.json
    |__ sed_bm_demo.tsv
    |__ sed_bm_demo.json
    |
    | <span class="hashtag"># Instruments</span>
    |__ <span class="placeholder">&lt;instrument_name&gt;</span>.tsv
    |__ <span class="placeholder">&lt;instrument_name&gt;</span>.json
</pre>

## Demographics Data
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

<p style="margin: 0 0 5px;">The <code>sed_basic_demographics</code> file provide demographic information for each participant that is useful for understanding their phenotypic data in context. This includes:</p>
<ul>
<li>Gestational Age at Delivery</li>
<li>Sex</li>
<li>Recruitment site</li>
<li>Child demographics: race, ethnicity</li>
<li>Birth parent's demographics: race, ethnicity, education, language at home</li>
<li>Substance Use (SU) flags raised by any of the following (<a href="#visit-data">Visit Data</a> contains details per visit):
    <ul>
    <li>Self-reported use (<a href="../../measures/pregexp/substanceuse/#tlfb">TLFB</a>)</li>
    <li><a href="../../measures/biospec">Biospecimen results</a></li>
    <li><a href="../../measures/pregexp/preghealth/#instruments">Health-V2 instrument</a> (<code>pex_bm_healthv2_inf</code>) Field <em>007</em> if option 1 (NOWS - Neonatal Opioid Withdrawal Syndrome) or 5 (FAS - Fetal Alcohol Syndrome) was selected</li>
    </ul>
</li>
</ul>

<p>The <code>sed_bm_demo</code> file contains additional demographic information pertaining to the birth parent collected as part of <a href="../../measures/socenvdet/">Social & Environmental Determinants</a> measures.</p>

Cohort types included in the data release are as follows, with Types E-F indicating [Caregiver Type](#CGtype):

- HBCD Main Child
- HBCD Main Child - Postnatal Recruitment
- HBCD Main Child - Type E-F
- HBCD Multiple Birth - Main Child
- HBCD Multiple Birth - Postnatal Recruitment
- HBCD Multiple Birth - Postnatal Recruitment - Sibling
- HBCD Multiple Birth - Type E-F

<div id="CGtype" class="table-banner" onclick="toggleCollapse(this)">
  <span class="table-text">Caregiver Type Definitions</span>
  <span class="table-arrow">▸</span>
</div>
<div class="table-collapsible-content">
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

## Visit Data
<p style="margin: 0 0 5px;">The <code>par_visit_data</code> file contains all participant visit data, including:</p>
<ul>
<li>Visit information (Label, Stage, Date, and if the visit was missed and the reason)</li>
<li>Project, Cohort, and Site</li>
<li>Withdrawal (if the participant withdrew from the study, the reason, and date) and Protocol violation (if there was a protocol exception and the date) information</li>
<li>Substance Use (SU) flags from three locations:
    <ul>
    <li>Self-reported use (<a href="../../measures/pregexp/substanceuse/#tlfb">TLFB</a>)</li>
    <li><a href="../../measures/pregexp/preghealth/#instrument-details">Health-V2</a></li>
    <li><a href="../../measures/biospec/#urine">Biosample Urine</a></li>
    </ul>
</li>
</ul>

## BioSpecimens
All BioSpecimen file are prepended with `bio_`. The `bio_biosample_urine` urine files include BioSpecimen USDTL Urine and DCCID, Visit Label, and Scannable code. See details of BioSpecimen screens [here](../measures/biospec.md).

## Instrument Data
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

Each instrument has a `<instrument_name>.tsv` Data Table containing instrument values and a `<instrument_name>.json` Data Dictionary describing instrument fields for all participants. For a full list of instrument files included in the release, see the overview section under [Data Measures Release Notes](../measures/index.md#data-measure-release-notes) overview.

