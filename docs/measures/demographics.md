# Demographics & Visit Information

## Basic Demographics

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
<p><b>Participant-Reported Challenges</b><br>
Some participants reported challenges in answering certain questions, such as those related to race and ethnicity (e.g. options did not capture identity) and occupation (i.e. imperfect option for job type and number of hours).</p> 
<p><b>Withheld Variables/Variable Data</b><br>
Some variables with small cell sizes were withheld from the data release to minimize any risk of disclosure of identifying information. In addition, there are some variables that do not contain any data in the current data release (e.g., response options allowed for more household members and more jobs during pregnancy than were reported by the respondents who completed V01 to date). These variables are currently being retained because this could change as data collection proceeds.</p> 
<p><b>Branching Logic</b><br>
There are several items with branching logic; please consult the RedCAP questionnaire to see question flow and data dictionaries for information on skip patterns. Topics with branching logic include: <i>Household roster</i>, <i>Nativity</i>, <i>Jobs / work environment</i>, and items on <i>other biological parent</i> (responses opt in to answer this set of questions).</p>
<p><b>V01 Candidate Age</b><br>
Note that candidate age (<code>candidate_age</code>) refers to the infant that will be enrolled in HBCD; this variable does not have values in V01 Demographics, as this questionnaire is completed before the child is born.</p>
</div>
</p>

**Basic Demographics** (`sed_basic_demographics`) includes data compiled from multiple sources, primarily the [HBCD Demographics V01](../socenvdet/#hbcd-demographics) instrument (`sed_bm_demo`) collected under the Social & Environmental Determinants domain. Additional demographic information was obtained from administrative records at the time of consent (including the age and race/ethnicity of the pregnant study participant) and during scheduling of the V02 visit — the first study visit after the child’s birth (including the child’s sex and race/ethnicity).

<p>
<div id="demo-table" class="table-banner" onclick="toggleCollapse(this)">
  <span class="text-with-link">
  <span class="text">Basic Demographics Pre-processed Key Variables</span>
  <a class="anchor-link" href="#demo-table" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="table-open-collapsible-content">
<table style="width: 100%; border-collapse: collapse; table-layout: fixed; font-size: 13px;">
<tfoot>
  <tr>
    <td colspan="3" style="white-space: normal; word-wrap: break-word; word-break: break-word; max-width: 600px;">
      <i>NOTE: within this table and the variable names, “child” refers to the child enrolled in HBCD; “mother” refers to the person carrying the child (i.e., pregnant with the child) at the time of V01.</i>
    </td>
  </tr>
</tfoot>
    <thead>
      <tr>
        <th style="width: 30%; border: 1px solid #ddd; padding: 12px; text-align: center; word-wrap: break-word; white-space: normal;">Construct<br>[<code>Variable Name</code>]</th>
        <th style="width: 70%; border: 1px solid #ddd; padding: 12px; text-align: center; word-wrap: break-word; white-space: normal;">Description</th>
      </tr>
    </thead>
    <tbody>
<tr>
<td style="border: 1px solid #ddd; padding: 4px; word-wrap: break-word; white-space: normal;">Child sex<br>[<code>sex</code>]</td>
<td style="border: 1px solid #ddd; padding: 4px; word-wrap: break-word; white-space: normal;">Recorded by Research Assistant within administrative data once the child was born, as reported by parent. These data will be missing from V01 Basic Demographics, and available starting at V02.</td>
</tr>
<tr>
<td style="border: 1px solid #ddd; padding: 4px; word-wrap: break-word; white-space: normal;">Child ethnicity<br>[<code>child_ethnicity</code>]</td>
<td style="border: 1px solid #ddd; padding: 4px; word-wrap: break-word; white-space: normal;">Recorded by Research Assistant within administrative data once the child was born, as reported by parent. Information was collected using a standard item on ethnicity from the American Community Survey. <br />These data will be missing from V01 Basic Demographics, and available starting at V02.</td>
</tr>
<tr>
<td style="border: 1px solid #ddd; padding: 4px; word-wrap: break-word; white-space: normal;">Child race<br>[<code>child_race</code>]</td>
<td style="border: 1px solid #ddd; padding: 4px; word-wrap: break-word; white-space: normal;">Recorded by Research Assistant within administrative data once the child was born, as reported by parent. Information was collected using a standard item asking about race from the American Community Survey. <br />These data will be missing from V01 Basic Demographics, and available starting at V02.</td>
</tr>
<tr>
<td style="border: 1px solid #ddd; padding: 4px; word-wrap: break-word; white-space: normal;">Child race and ethnicity combined &ndash; multiracial aggregation by Hispanic and non-Hispanic distinction<br>[<code>child_ethnoracial_acs_by_multi_ethnicity</code>]</td>
<td style="border: 1px solid #ddd; padding: 4px; word-wrap: break-word; white-space: normal;">Recorded by Research Assistant within administrative data once the child was born, as reported by parent. <br />Constructed using the separate items on child race and child ethnicity (above) following current federal standards (i.e., if a child is identified as Hispanic or Latino based on the response to the ethnicity item, they will be categorized as such, regardless of their race). <br />If the child has two or more racial categories endorsed, they are categorized as &ldquo;multiracial&rdquo; and the multiracial category is split into those who are Hispanic and those who are not.<br />These data will be missing from V01 Basic Demographics, and available starting at V02.</td>
</tr>
<tr>
<td style="border: 1px solid #ddd; padding: 4px; word-wrap: break-word; white-space: normal;">Child race and ethnicity combined &ndash; multiracial aggregation by Black and non-Black distinction<br>[<code>child_ethnoracial_acs_by_multi_race</code>]</td>
<td style="border: 1px solid #ddd; padding: 4px; word-wrap: break-word; white-space: normal;">Recorded by Research Assistant within administrative data once the child was born, as reported by parent. Constructed using the separate items on child race and child ethnicity (above) following current federal standards (i.e., if a child is identified as Hispanic or Latino based on the response to the ethnicity item, they will be categorized as such, regardless of their race). <br /><br /><br />If the child has two or more racial categories endorsed, they are categorized as &ldquo;multiracial&rdquo; and the multiracial category is split into those that include Black/African American as an identity and those who do not.<br />These data will be missing from V01 Basic Demographics, and available starting at V02.</td>
</tr>
<tr>
<td style="border: 1px solid #ddd; padding: 4px; word-wrap: break-word; white-space: normal;">Maternal age at V01<br>[<code>mother_age_v01</code>]</td>
<td style="border: 1px solid #ddd; padding: 4px; word-wrap: break-word; white-space: normal;">'MAV01' is a constructed variable that represents the birth parent's age, obtained from the scheduled date of the V01 visit. The age is reported in years to two decimal places, with fractional years calculated by dividing the number of whole months (rounded down) by 12. This variable is static and does not change over time.
</td>
</tr>
<tr>
<td style="border: 1px solid #ddd; padding: 4px; word-wrap: break-word; white-space: normal;">Maternal Age at Delivery<br>[<code>mother_age_delivery</code>]</td>
<td style="border: 1px solid #ddd; padding: 4px; word-wrap: break-word; white-space: normal;">'MAD' is a constructed variable that represents the birth parent’s age at the time of their child's delivery (date of birth). It is reported in years to two decimal places, with fractional years calculated by dividing the total whole months (rounded down) by 12. This variable is static and does not change over time. <br />These data will be missing from V01 Basic Demographics, and available starting at V02.</td>
</tr>
<tr>
<td style="border: 1px solid #ddd; padding: 4px; word-wrap: break-word; white-space: normal;">Gestational Age at Delivery<br>[<code>gestational_age_delivery</code>]</td>
<td style="border: 1px solid #ddd; padding: 4px; word-wrap: break-word; white-space: normal;">'GAD' is a constructed variable that represents the time elapsed between the first day of the birth parent’s last menstrual period (LMP), derived from the estimated date of delivery (EDD) minus 280 days, and the child's date of birth. It is reported in whole weeks, rounded down to the nearest week. This variable is static and does not change over time. <br />These data will be missing from V01 Basic Demographics, and available starting at V02.</td>
</tr>
<tr>
<td style="border: 1px solid #ddd; padding: 4px; word-wrap: break-word; white-space: normal;">Mother combined race and ethnicity at screening into study&ndash; multiracial category split into Hispanic and non-Hispanic groups<br>[<code>screen_mother_ethnoracial_acs_by_multi_ethnicity</code>]</td>
<td style="border: 1px solid #ddd; padding: 4px; word-wrap: break-word; white-space: normal;">Using participant responses to separate questions of race and ethnicity collected during screening, we constructed a race and ethnicity variable where individuals are placed into a single category.<br />If an individual selected more than one response for race, they were placed into a multiracial group; this multiracial group was split into multiracial individuals who indicated Hispanic or Latino ethnicity as one of their select identities, and those who selected other combinations of more than one response.</td>
</tr>
<tr>
<td style="border: 1px solid #ddd; padding: 4px; word-wrap: break-word; white-space: normal;">Mother combined race and ethnicity at screening into study &ndash; multiracial category split into Black and non-Black groups<br>[<code>screen_mother_ethnoracial_acs_by_multi_ethnicity</code>]</td>
<td style="border: 1px solid #ddd; padding: 4px; word-wrap: break-word; white-space: normal;">Using participant responses to separate questions of race and ethnicity collected during screening, we constructed a race and ethnicity variable where individuals are placed into a single category.<br />If an individual selected more than one response for race, they were placed into a multiracial group; this multiracial group was split into multiracial individuals who indicated Black/African American as one of their selected identities, and those who selected other combinations of more than one response.</td>
</tr>
<tr>
<td style="border: 1px solid #ddd; padding: 4px; word-wrap: break-word; white-space: normal;">Mother race and ethnicity<br>[<code>rc_mother_ethnoracial_aou_race_ethnicity</code>]</td>
<td style="border: 1px solid #ddd; padding: 4px; word-wrap: break-word; white-space: normal;">Responses to a single race and ethnicity item administered as part of the V01 Demographics survey (Source: <a class="in-cell-link" href="https://support.researchallofus.org/hc/en-us/articles/360039299632-Race-and-ethnicity-generalizations" target="_blank">All of Us</a> race and ethnicity item, and scoring followed OMB standards where individuals who identified as Hispanic/Latino alone, or in combination with some other category, were categorized as Hispanic/Latino) &ndash; all other groups are &rdquo;non-Hispanic&rdquo;.</td>
</tr>
<tr>
<td style="border: 1px solid #ddd; padding: 4px; word-wrap: break-word; white-space: normal;">Mother ethnicity<br>[<code>Screen_mother_ethnicity</code>]</td>
<td style="border: 1px solid #ddd; padding: 4px; word-wrap: break-word; white-space: normal;">Participant response to a single question about ethnic identity, collected during screening using an item from the American Community Survey.<br />DATA NOTE: There is a known formatting error with this 2-level variable. Levels of 0 and 1 are included in error and are blank &ndash; all participants with valid data have a value of either &ldquo;2&rdquo; or &ldquo;3&rdquo;, with 2=Hispanic and 3=non-Hispanic. This issue will be corrected in a future data release.</td>
</tr>
<tr>
<td style="border: 1px solid #ddd; padding: 4px; word-wrap: break-word; white-space: normal;">Mother race, multi-categorical variable from screening<br>[<code>screen_mother_race</code>]</td>
<td style="border: 1px solid #ddd; padding: 4px; word-wrap: break-word; white-space: normal;">Participant response to a single question about racial identity, collected during screening using an item from the American Community Survey.</td>
</tr>
<tr>
<td style="border: 1px solid #ddd; padding: 4px; word-wrap: break-word; white-space: normal;">Mother race, indicator variables from screening item<br>[<code>screen_mother_race_multi___0</code> <br />&hellip;to&hellip; <code>screen_mother_race_multi___5</code>]</td>
<td style="border: 1px solid #ddd; padding: 4px; word-wrap: break-word; white-space: normal;">Indicator variables for responses to ACS race question at screening; ___0=White; ___1=Black or African American; ___2=American Indian or Alaskan Native; ___3=Asian; ___4=Native Hawaiian or other Pacific Islander; ___5=&rdquo;Other race&rdquo;</td>
</tr>
<tr>
<td style="border: 1px solid #ddd; padding: 4px; word-wrap: break-word; white-space: normal;">Mother race, indicator variables from survey item<br>[<code>rc_mother_race___0</code> &hellip;to&hellip; <code>rc_mother_race___7</code>]</td>
<td style="border: 1px solid #ddd; padding: 4px; word-wrap: break-word; white-space: normal;">Indicator variables for responses to <a class="in-cell-link" href="https://support.researchallofus.org/hc/en-us/articles/360039299632-Race-and-ethnicity-generalizations" target="_blank">All of Us</a> combined race and ethnicity question that is part of the Demographic survey; ___0=American Indian or Alaskan Native; ___1=Asian; ___2=Black, African American, or African; ___3=Hispanic, Latino, or Spanish; ___4=Middle Eastern or North African; ___5=Native Hawaiian or other Pacific Islander; ___6=White; 7=None of these fully describe me.</td>
</tr>
<tr>
<td style="border: 1px solid #ddd; padding: 4px; word-wrap: break-word; white-space: normal;">Mother education<br>[<code>rc_mother_education</code>]</td>
<td style="border: 1px solid #ddd; padding: 4px; word-wrap: break-word; white-space: normal;">This item comes from the V01 Demographics survey &ldquo;sed_bm_demo_edu_001&rdquo;</td>
</tr>
<tr>
<td style="border: 1px solid #ddd; padding: 4px; word-wrap: break-word; white-space: normal;">Total combined household income<br>[<code>rc_mother_income</code>]</td>
<td style="border: 1px solid #ddd; padding: 4px; word-wrap: break-word; white-space: normal;">This item comes from the V01 Demographics survey &ldquo;sed_bm_demo_income_002&rdquo;</td>
</tr>
<tr>
<td style="border: 1px solid #ddd; padding: 4px; word-wrap: break-word; white-space: normal;">Recruitment site<br>[<code>recruitment_site</code>]</td>
<td style="border: 1px solid #ddd; padding: 4px; word-wrap: break-word; white-space: normal;">De-identified value reflecting recruitment sites.</td>
</tr>
</tbody>
</table>
</div>
</p>


## Visit Data
<p style="margin: 0 0 5px;">Visit Level Data (<code>par_visit_data</code>) contains all participant visit data, including:</p>
<ul>
<li>Visit information: Label, Stage, Date, if the visit was missed, and the reason if visit was missed</li>
<li>Project, <a href="#cohorts">Cohort</a>, and Site</li>
<li>Withdrawal information: if the participant withdrew from the study, the reason, and date</li>
<li>Protocol violation information: if there was a protocol exception and the date</li>
<li>Visit details for SU flags raised by TLFB, Biospecimen, or Health-V2 as described above (<a href="#basic-emographics-data">Basic Demographics Data</a>)</li>
</ul>

**Note that `cohort` and `site` are not currently described in the data dictionary, but are included in dataset downloads from Lasso and are equivalent to the columns `par_visit_data_cohort` and `par_visit_data_site` (see details [here](../download/lasso.md#additional-columns-cohort-site-not-defined-in-data-dictionary)).**


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

