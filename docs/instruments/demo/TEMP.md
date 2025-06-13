# Demographics

## Basic Demographics

<p>
<div id="demo-fyi" class="notification-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fa-regular fa-lightbulb"></i></span>
    <span class="text">Please see the section on the <a href="../socenvdet/#hbcd-demographics-v01">HBCD Demographics V01</a> instrument for more detailed demographics information variables from which Basic Demographics was in part derived.</span>
</div>
</p>

<div id="demo-alert" class="alert-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fas fa-exclamation-circle"></i></span>
  <span class="text-with-link">
  <span class="text">Responsible Use Warning</span>
  <a class="anchor-link" href="#demo-alert" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="alert-collapsible-content">
<p>When using HBCD data, all data users must agree to responsible use as described in the DUC. When conceptualizing studies, analyzing data, and communicating findings from studies that use variables such as race, ethnicity, country of origin, and socioeconomic data, it is critical to consider strategies to avoid stigmatization of any groups and perpetuating harmful biases.</p> 
<p>Race and ethnicity are collected as a part of the HBCD protocol to reflect social experiences (i.e., representing social constructs), and should not be conceptualized as as biological, natural, intrinsic, or fixed categories of people. In addition, researchers sometimes use race/ethnicity variables as a proxy for unmeasured social experiences or environmental exposures. HBCD measures a wide variety of social experiences and environmental exposures. In analyzing HBCD data, race/ethnicity should not be used as a proxy for measured variables.</p>
</div>

<p>
<div id="demo-warning" class="warning-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fas fa-exclamation-triangle"></i></span>
  <span class="text-with-link">
  <span class="text">Data Warnings</span>
  <a class="anchor-link" href="#demo-warning" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="warning-collapsible-content">

<p><b>⚠️ <a href="../../changelog/knownissues"><u>Known Issues</u></a> To Be Resolved in Future Release</b><br>
<p><strong>'Mother Race' (<code>screen_mother_race</code>)</strong>: contains duplicate options for the selection of 'Black African American' (option #3). This option is not used for data entry, and instead the 'Black_or African American' option (option #5) should be used. No other variables are affected by this.</p>

<p><strong>Mother Ethnicity (<code>screen_mother_ethnicity</code>)</strong>: should be a 2-level variable, but is currently noted as a 4-level variable in the data dictionary. Levels of 0 and 1 (in the data dictionary) are included in error, they do not appear in the dataset; all participants with valid data have a value of 2 (Hispanic) or 3 (non-Hispanic).</p>

<p><b>Participant-Reported Challenges</b><br>
Some participants reported challenges in answering certain questions, such as those related to race and ethnicity (e.g. options did not capture identity) and occupation (i.e. imperfect option for job type and number of hours).</p> 
</div>
</p>

**Basic Demographics** (`sed_basic_demographics`) is a derived table that includes data derived or computed from two sources:

1. [**HBCD Demographics V01**](socenvdet.md#hbcd-demographics-v01) instrument (`sed_bm_demo`) collected under the Social & Environmental Determinants domain 
2. **Administrative screening records** collected by a research assistant, as reported by the birth parent, during the enrolment/screening process (e.g. the age and race/ethnicity of the pregnant study participant)

Additional details on Basic Demographics variables are provided below. 

<p>
<div id="bdemo-fyi" class="notification-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fa-regular fa-lightbulb"></i></span>
  <span class="text-with-link">
  <span class="text">Variable Logic & Definitions</span>
  <a class="anchor-link" href="#bdemo-fyi" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="notification-open-collapsible-content">
<p><b>Basic Demographics are global, visit-agnostic variables</b><br>
Basic Demographics are single-point, static variables (i.e. they do not change over time) that should be present and consistent across all Visits (V01, V02, etc.). <strong>However</strong>, if only V01 data for a given participant is included in the release (due to ongoing enrollment, participant withdrawal, etc.), then items about the child will be missing, as the child is not born until after the V01 visit (all variables about the child are available beginning with V02).</p>

<p><b>Child vs Mother Variables</b><br>
Within the table and the variable names, <strong><code>child</code></strong> refers to the child enrolled in HBCD and <strong><code>mother</code></strong> refers to the person carrying the child (i.e., pregnant with the child) at the time of V01.</p>

<p><b>Combined Race and Ethnicity Variable Logic</b><br>
With the exception of <code>rc_mother_ethnoracial_aou_race_ethnicity</code> (only constructed for the birth parent, following <a href="https://www.federalregister.gov/documents/2023/01/27/2023-01635/initial-proposals-for-updating-ombs-race-and-ethnicity-statistical-standards">OMB</a> standards as described in the table below), variables that combine race and ethnicity are constructed from separate race and ethnicity variables following current federal standards: if an individual is identified as Hispanic or Latino based on the response to the ethnicity item, they will be categorized as such, regardless of their race. In addition, individuals who select more than one race are categorized as "multiracial."</p>

<p><b>Multiracial Individuals: Aggregation By Ethnicity Vs Race</b><br>
There are two combined race and ethnicity variables that aggregate multiracial individuals into subcategories by ethnicity (<code>*_acs_by_multi_ethnicity</code>) vs race (<code>*_acs_by_multi_race</code>). For aggregation by ethnicity, individuals are subcategorized into those who do and do not select Hispanic as one of their identities. For race, individuals are subcategorized into those who do and do not select Black/African American as one of their identities.</p>
</div>
</p>

<div id="demo-table" class="table-banner" onclick="toggleCollapse(this)">
  <span class="text-with-link">
  <span class="text">Basic Demographics (Key Derived Variables)</span>
  <a class="anchor-link" href="#demo-table" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="table-open-collapsible-content">
<table style="width: 100%; border-collapse: collapse; table-layout: fixed; font-size: 13px;">
    <thead>
      <tr>
        <th style="width: 25%; text-align: center; word-wrap: break-word; white-space: normal;">Construct</th>
        <th style="width: 20%; text-align: center; word-wrap: break-word; white-space: normal;">Variable Name</th>
        <th style="width: 10%; text-align: center; word-wrap: break-word; white-space: normal;"><span class="tooltip tooltip-bottom">Source<span class="tooltiptext">Administrative Records or V01 Demographics instrument</span></span></th>
        <th style="width: 40%; text-align: center; word-wrap: break-word; white-space: normal;">Description</th>
      </tr>
    </thead>
    <tbody>
<tr>
<td style="padding: 8px; word-wrap: break-word; white-space: normal;">Child sex</td>
<td style="padding: 8px; word-wrap: break-word; white-space: normal;"><code>sex</code></td>
<td style="padding: 8px; word-wrap: break-word; white-space: normal;">Admin</td>
<td style="padding: 8px; word-wrap: break-word; white-space: normal;"><span class="tooltip tooltip-left"><i>Visit V02 onward</i><span class="tooltiptext">Data are not collected prior to birth, i.e. at the prenatal V01 visit, and will be available starting at visit V02</span></span></td>
</tr>
<tr>
<td style="padding: 8px; word-wrap: break-word; white-space: normal;">Child ethnicity</td>
<td style="padding: 8px; word-wrap: break-word; white-space: normal;"><code>child_ethnicity</code></td>
<td style="padding: 8px; word-wrap: break-word; white-space: normal;">Admin</td>
<td style="padding: 8px; word-wrap: break-word; white-space: normal;"><a href="https://www.census.gov/programs-surveys/acs.html">ACS</a>-standard ethnicity item. <span class="tooltip tooltip-left"><i>Visit V02 onward</i><span class="tooltiptext">Data are not collected prior to birth, i.e. at the prenatal V01 visit, and will be available starting at visit V02</span></span><i></i></td>
</tr>
<tr>
<td style="padding: 8px; word-wrap: break-word; white-space: normal;">Child race</td>
<td style="padding: 8px; word-wrap: break-word; white-space: normal;"><code>child_race</code></td>
<td style="padding: 8px; word-wrap: break-word; white-space: normal;">Admin</td>
<td style="padding: 8px; word-wrap: break-word; white-space: normal;"><a href="https://www.census.gov/programs-surveys/acs.html">ACS</a>-standard race item. <span class="tooltip"><i>Visit V02 onward</i><span class="tooltiptext">Data are not collected prior to birth, i.e. at the prenatal V01 visit, and will be available starting at visit V02</span></span></td>
</tr>
<tr>
<td style="padding: 8px; word-wrap: break-word; white-space: normal;">Child race and ethnicity combined - multiracial aggregation by Hispanic and non-Hispanic distinction</td>
<td style="word-break: break-all; white-space: normal;"><code>child_ethnoracial_acs_by_multi_ethnicity</code></td>
<td style="padding: 8px; word-wrap: break-word; white-space: normal;">Admin</td>
<td style="padding: 8px; word-wrap: break-word; white-space: normal;">Individuals are assigned a single category, constructed from <code>child_race</code> and <code>child_ethnicity</code>, with subcategories for multiracial individuals based on ethnicity following the logic described in the <a href="#bdemo-fyi">Variable Logic & Definitions</a> above. <span class="tooltip"><i>Visit V02 onward</i><span class="tooltiptext">Data are not collected prior to birth, i.e. at the prenatal V01 visit, and will be available starting at visit V02</span></span><i></i></td>
</tr>
<tr>
<td style="padding: 8px; word-wrap: break-word; white-space: normal;">Child race and ethnicity combined - multiracial aggregation by Black and non-Black distinction</td>
<td style="word-break: break-all; white-space: normal;"><code>child_ethnoracial_acs_by_multi_race</code></td>
<td style="padding: 8px; word-wrap: break-word; white-space: normal;">Admin</td>
<td style="padding: 8px; word-wrap: break-word; white-space: normal;">Individuals are assigned a single category, constructed from <code>child_race</code> and <code>child_ethnicity</code>, with subcategories for multiracial individuals based on race following the logic described in the <a href="#bdemo-fyi">Variable Logic & Definitions</a> above. <span class="tooltip"><i>Visit V02 onward</i><span class="tooltiptext">Data are not collected prior to birth, i.e. at the prenatal V01 visit, and will be available starting at visit V02</span></span><i></i></td>
</tr>
<tr>
<td style="padding: 8px; word-wrap: break-word; white-space: normal;">Mother combined race and ethnicity - multiracial category split into Hispanic and non-Hispanic groups</td>
<td style="word-break: break-all; white-space: normal"><code>screen_mother_ethnoracial_acs_by_multi_ethnicity</code></td>
<td style="padding: 8px; word-wrap: break-word; white-space: normal;">Admin</td>
<td style="padding: 8px; word-wrap: break-word; white-space: normal;">Individuals are assigned a single category, constructed from screening responses to separate race and ethnicity questions, with subcategories for multiracial individuals based on ethnicity following the logic described in the <a href="#bdemo-fyi">Variable Logic & Definitions</a> above.</td>
</tr>
<tr>
<td style="padding: 8px; word-wrap: break-word; white-space: normal;">Mother combined race and ethnicity - multiracial category split into Black and non-Black groups</td>
<td style="word-break: break-all; white-space: normal;"><code>screen_mother_ethnoracial_acs_by_multi_race</code></td>
<td style="padding: 8px; word-wrap: break-word; white-space: normal;">Admin</td>
<td style="padding: 8px; word-wrap: break-word; white-space: normal;">Individuals are assigned a single category, constructed from screening responses to separate race and ethnicity questions, with subcategories for multiracial individuals based on race following the logic described in the <a href="#bdemo-fyi">Variable Logic & Definitions</a> above.</td>
</tr>
<tr>
<td style="padding: 8px; word-wrap: break-word; white-space: normal;">Mother race and ethnicity</td>
<td style="word-break: break-all; white-space: normal;"><code>rc_mother_ethnoracial_aou_race_ethnicity</code></td>
<td style="padding: 8px; word-wrap: break-word; white-space: normal;">V01 Demo</td>
<td style="padding: 8px; word-wrap: break-word; white-space: normal;">Derived from single <a class="in-cell-link" href="https://support.researchallofus.org/hc/en-us/articles/360039299632-Race-and-ethnicity-generalizations" target="_blank">All of Us</a> race and ethnicity item scored following <span class="tooltip"><a href="https://www.federalregister.gov/documents/2023/01/27/2023-01635/initial-proposals-for-updating-ombs-race-and-ethnicity-statistical-standards">OMB</a> standards<span class="tooltiptext">Anyone identifying as Hispanic/Latino (alone or with another group) is categorized as Hispanic/Latino; all others as non-Hispanic</span>.</span></td>
</tr>
<tr>
<td style="padding: 8px; word-wrap: break-word; white-space: normal;">Mother ethnicity</td>
<td style="padding: 8px; word-wrap: break-word; white-space: normal;"><code>screen_mother_ethnicity</code></td>
<td style="padding: 8px; word-wrap: break-word; white-space: normal;">Admin</td>
<td style="padding: 8px; word-wrap: break-word; white-space: normal;">Participant response to <a href="https://www.census.gov/programs-surveys/acs.html">ACS</a> item about ethnic identity collected during screening. <i>See <a href="../../changelog/knownissues/#mother-ethnicity">Known Issue</a>.</i></td>
</tr>
<tr>
<td style="padding: 8px; word-wrap: break-word; white-space: normal;">Mother race, multi-categorical</td>
<td style="padding: 8px; word-wrap: break-word; white-space: normal;"><code>screen_mother_race</code></td>
<td style="padding: 8px; word-wrap: break-word; white-space: normal;">Admin</td>
<td style="padding: 8px; word-wrap: break-word; white-space: normal;">Participant response to <a href="https://www.census.gov/programs-surveys/acs.html">ACS</a> item/question about racial identity collected during screening.  <i>See <a href="../../changelog/knownissues/#duplicate-options-for-mother-race-variable">Known Issue</a>.</i></td>
</tr>
<tr>
<td style="padding: 8px; word-wrap: break-word; white-space: normal;">Mother race, indicator variables from screening</td>
<td style="word-break: break-all; white-space: normal;"><code>screen_mother_race_multi___{0 - 5}</code></td>
<td style="padding: 8px; word-wrap: break-word; white-space: normal;">Admin</td>
<td style="padding: 8px; word-wrap: break-word; white-space: normal;">Indicator variables from ACS race question:<br>
0 = White<br>
1 = Black or African American<br>
2 = American Indian or Alaskan Native<br>
3 = Asian<br>
4 = Native Hawaiian or other Pacific Islander<br>
5 = Other race</td>
</tr>
<tr>
<td style="padding: 8px; word-wrap: break-word; white-space: normal;">Mother race, indicator variables from survey item</td>
<td style="padding: 8px; word-wrap: break-word; white-space: normal;"><code>rc_mother_race___{0 - 7}</code></td>
<td style="padding: 8px; word-wrap: break-word; white-space: normal;">V01 Demo</td>
<td style="padding: 8px; word-wrap: break-word; white-space: normal;">Indicator variables for responses to <a class="in-cell-link" href="https://support.researchallofus.org/hc/en-us/articles/360039299632-Race-and-ethnicity-generalizations" target="_blank">All of Us</a> combined race and ethnicity question:<br>
0 = American Indian or Alaskan Native<br>
1 = Asian<br>
2 = Black, African American, or African<br>
3 = Hispanic, Latino, or Spanish<br>
4 = Middle Eastern or North African<br>
5 = Native Hawaiian or other Pacific Islander<br>
6 = White<br>
7 = None of these fully describe me</td>
</tr>
<tr>
<td style="padding: 8px; word-wrap: break-word; white-space: normal;">Mother education</td>
<td style="padding: 8px; word-wrap: break-word; white-space: normal;"><code>rc_mother_education</code></td>
<td style="padding: 8px; word-wrap: break-word; white-space: normal;">V01 Demo</td>
<td style="padding: 8px; word-wrap: break-word; white-space: normal;">Derived from <code>sed_bm_demo_edu_001</code></td>
</tr>
<tr>
<td style="padding: 8px; word-wrap: break-word; white-space: normal;">Total combined household income</td>
<td style="padding: 8px; word-wrap: break-word; white-space: normal;"><code>rc_mother_income</code></td>
<td style="padding: 8px; word-wrap: break-word; white-space: normal;">V01 Demo</td>
<td style="padding: 8px; word-wrap: break-word; white-space: normal;">Derived from <code>sed_bm_demo_income_002</code></td>
</tr>
<tr>
<td style="padding: 8px; word-wrap: break-word; white-space: normal;">Recruitment site</td>
<td style="padding: 8px; word-wrap: break-word; white-space: normal;"><code>recruitment_site</code></td>
<td style="padding: 8px; word-wrap: break-word; white-space: normal;">Admin</td>
<td style="padding: 8px; word-wrap: break-word; white-space: normal;">De-identified value reflecting recruitment sites</td>
</tr>
</tbody>
</table>
</div>

Note that, compared to tabulated instrument data (see [Tabulated Instrument Data](../measures/agevariables.md/#tabulated-instrument-data)), Basic Demographics includes a unique set of fields reporting age: 

<p>
<div id="demo-age" class="notification-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fa-regular fa-lightbulb"></i></span>
    <span class="text-with-link">
    <span class="text">Demographics: Fields Reporting Age</span>
    <a class="anchor-link" href="#demo-age" title="Copy link">
    <i class="fa-solid fa-link"></i>
    </a>
    </span>
  <span class="arrow">▸</span>
</div>
<div class="notification-open-collapsible-content">
<br>
<i>See the <a href="../agevariables">Age Variable Definitions</a> section for a summary of all age-related variables across the release, as well as the information summarized in table format <a href="../agevariables/#basic-demographics">here</a>.</i>
<br>
<br>
<b>Maternal Age at V01 </b> (<code>mother_age_v01</code>): 'MAV01' is the birth parent's age, obtained from the scheduled date of the V01 visit. Reported in years to two decimal places, with fractional years calculated by dividing the number of whole months (rounded down) by 12.
<br>
<br>
<b>Maternal Age at Delivery</b> (<code>mother_age_delivery</code>): 'MAD' is the birth parent’s age at the time of their child's delivery (date of birth). Reported in years to two decimal places, with fractional years calculated by dividing the total whole months (rounded down) by 12.
<br>
<br>
<b>Gestational Age at Delivery</b> (<code>gestational_age_delivery</code>): 'GAD' is the time elapsed between the first day of the birth parent’s last menstrual period (LMP) and the child's date of birth. Reported in whole weeks, rounded down to the nearest week.<br>
<br>
</div>
</p>

## HBCD V01 Demographics
See instrument details under [Social & Environmental Determinants](socenvdet.md#hbcd-demographics-v01).

## Visit Information
<p style="margin: 0 0 5px;">Visit Level Data (<code>par_visit_data</code>) contains all participant visit data, including:</p>
<ul>
<li>Visit information: Label, Stage, Date, if the visit was missed, and the reason if visit was missed</li>
<li>Project, <a href="#cohorts">Cohort</a>, and Site</li>
<li>Withdrawal information: if the participant withdrew from the study, the reason, and date</li>
<li>Protocol violation information: if there was a protocol exception and the date</li>
<li>Substance use flags raised by any of the following:
<ul>
<li><a href="../../measures/pregexp/substanceuse#tlfb">TLFB</a> (Self-reported use)
<li><a href="../../measures/biospec">Biospecimen results</a>
<li><a href="../../measures/pregexp/preghealth#instruments">Infant health- V2</a> (<code>pex_bm_healthv2_inf</code>) Field <code>007</code> when option 1 (NOWS - Neonatal Opioid Withdrawal Syndrome) or 5 (FAS - Fetal Alcohol Syndrome) was selected</li>
</ul>
</ul>

**Note that `cohort` and `site` are not currently described in the data dictionary, but are included in dataset downloads from Lasso and are equivalent to the columns `par_visit_data_cohort` and `par_visit_data_site` (see details [here](../access/download/#add-columns)).**


<div id="cohorts" class="notification-banner" onclick="toggleCollapse(this)">
  <span class="text">Cohort & Caregiver Types</span>
  <span class="arrow">▸</span>
</div>
<div class="notification-open-collapsible-content">
<p>Cohort types included in the data release are as follows, with each listed item indicating a specific subtype or Caregiver Type (e.g., "HBCD Main Child - Postnatal Recruitment"):</p>
<ul>
<li><strong>HBCD Main Child -</strong> <em>Postnatal Recruitment</em>, <em>Type A-F</em></li>
<li><strong>HBCD Multiple Birth -</strong> <em>Main Child</em>, <em>Postnatal Recruitment</em>, <em>Postnatal Recruitment - Sibling</em>, <em>Type A-F</em></li>
</ul>
<b>Caregiver Type A-F Definitions</b>
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

