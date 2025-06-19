# Basic Demographics
   
**Table Name**: `sed_basic_demographics`    

<p>
<div id="faq-access" class="notification-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fa-regular fa-lightbulb"></i></span>
    <span class="text">Basic Demographics is a <i>derived measure</i> computed from multiple sources. For more extensive demographics information, please see <a href="../../SED/v01-demo">V01 Demographics</a>.</span>
</div>
</p>


Basic Demographics is derived information computed from: 

- A subset of **V01 Demographics** (`sed_bm_demo`) Social & Environmental Determinants domain instrument variables 
- **Administrative screening records** collected by HBCD Study staff, as reported by the birth parent, during the enrolment/screening process (e.g. the age and race/ethnicity of the pregnant study participant)

Basic Demographics are **global, visit-agnostic variables** that do not change over time and should be present and consistent across all Visits (V01, V02, etc.). *However*, if only V01 data for a given participant is included in the release (due to ongoing enrollment, participant withdrawal, etc.), then items about the child will be missing, as the child is not born until after the V01 visit (all variables about the child are available beginning with V02).


<div id="alert" class="alert-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fas fa-exclamation-circle"></i></span>
  <span class="text-with-link">
  <span class="text">Responsible Use Warning</span>
  <a class="anchor-link" href="#alert" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="alert-collapsible-content">
<p>When using HBCD data, all data users must agree to responsible use as described in the DUC. When conceptualizing studies, analyzing data, and communicating findings from studies that use variables such as race, ethnicity, country of origin, and socioeconomic data, it is critical to consider strategies to avoid stigmatization of any groups and perpetuating harmful biases.</p> 
<p>Race and ethnicity are collected as a part of the HBCD protocol to reflect social experiences (i.e., representing social constructs), and should not be conceptualized as biological, natural, intrinsic, or fixed categories of people. In addition, researchers sometimes use race/ethnicity variables as a proxy for unmeasured social experiences or environmental exposures. HBCD measures a wide variety of social experiences and environmental exposures. In analyzing HBCD data, race/ethnicity should not be used as a proxy for measured variables.</p>
</div>

<div id="warning" class="warning-banner" onclick="toggleCollapse(this)">
    <span class="emoji"><i class="fas fa-exclamation-triangle"></i></span>
  <span class="text-with-link">
  <span class="text">Data Warning</i></span>
  <a class="anchor-link" href="#warning" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="warning-collapsible-content">
<p><b>⚠️ <a href="../../../changelog/knownissues"><u>Known Issues</u></a> To Be Resolved in Future Release</b><br>
<p><strong>'Mother Race' (<code>screen_mother_race</code>)</strong>: contains duplicate options for the selection of 'Black African American' (option #3). This option is not used for data entry, and instead the 'Black_or African American' option (option #5) should be used. No other variables are affected by this.</p>
<p><strong>Mother Ethnicity (<code>screen_mother_ethnicity</code>)</strong>: should be a 2-level variable, but is currently noted as a 4-level variable in the data dictionary. Levels of 0 and 1 (in the data dictionary) are included in error, they do not appear in the dataset; all participants with valid data have a value of 2 (Hispanic) or 3 (non-Hispanic).</p>
<p><b>Participant-Reported Challenges</b><br>
Some participants reported challenges in answering certain questions, such as those related to race and ethnicity (e.g. options did not capture identity) and occupation (i.e. imperfect option for job type and number of hours).</p> 
</div>

## Variable Logic & Definitions

<div id="bdemo-fyi" class="notification-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fa-regular fa-lightbulb"></i></span>
  <span class="text-with-link">
  <span class="text">Variable Logic</span>
  <a class="anchor-link" href="#bdemo-fyi" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="notification-collapsible-content">
<p><b>Fields Reporting Age</b><br>
Basic Demographics includes a unique set of fields reporting age compared to instrument data, including Maternal Age at V01 (MAV01), Maternal Age at Delivery (MAD), and Gestational Age at Delivery (GAD) of the child (defined in the table below). See the <a href="../../agevariables">Age Variable Definitions</a> section for a summary of all age-related variables across the release.</p>

<p><b>Combined Race and Ethnicity Variable Logic</b><br>
With the exception of <code>rc_mother_ethnoracial_aou_race_ethnicity</code> (only constructed for the birth parent, following <a href="https://www.federalregister.gov/documents/2023/01/27/2023-01635/initial-proposals-for-updating-ombs-race-and-ethnicity-statistical-standards">OMB</a> standards as described in the table below), variables that combine race and ethnicity are constructed from separate race and ethnicity variables following current federal standards: if an individual is identified as Hispanic or Latino based on the response to the ethnicity item, they will be categorized as such, regardless of their race. In addition, individuals who select more than one race are categorized as "multiracial."</p>
<p><b>Multiracial Individuals: Aggregation By Ethnicity Vs Race</b><br>
There are two combined race and ethnicity variables that aggregate multiracial individuals into subcategories by ethnicity (<code>*_acs_by_multi_ethnicity</code>) vs race (<code>*_acs_by_multi_race</code>). For aggregation by ethnicity, individuals are subcategorized into those who do and do not select Hispanic as one of their identities. For race, individuals are subcategorized into those who do and do not select Black/African American as one of their identities.</p>
</div>

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
<td style="padding: 8px; word-wrap: break-word; white-space: normal;">Maternal Age at V01 (MAV01)</td>
<td style="padding: 8px; word-wrap: break-word; white-space: normal;"><code>mother_age_v01</code></td>
<td style="padding: 8px; word-wrap: break-word; white-space: normal;">Admin</td>
<td style="padding: 8px; word-wrap: break-word; white-space: normal;">Birth parent's age, obtained from the scheduled date of the V01 visit. Reported in years to two decimal places, with fractional years calculated by dividing the number of whole months (rounded down) by 12.</td>
</tr>
<tr>
<td style="padding: 8px; word-wrap: break-word; white-space: normal;">Maternal Age at Delivery (MAD)</td>
<td style="padding: 8px; word-wrap: break-word; white-space: normal;"><code>mother_age_delivery</code></td>
<td style="padding: 8px; word-wrap: break-word; white-space: normal;">Admin</td>
<td style="padding: 8px; word-wrap: break-word; white-space: normal;">Birth parent's age at the time of their child's delivery (date of birth). Reported in years to two decimal places, with fractional years calculated by dividing the total whole months (rounded down) by 12.</td>
</tr>
<tr>
<td style="padding: 8px; word-wrap: break-word; white-space: normal;">Gestational Age at Delivery (GAD)</td>
<td style="padding: 8px; word-wrap: break-word; white-space: normal;"><code>gestational_age_delivery</code></td>
<td style="padding: 8px; word-wrap: break-word; white-space: normal;">Admin</td>
<td style="padding: 8px; word-wrap: break-word; white-space: normal;">Age of the child at delivery calculated as the time elapsed between the first day of the birth parent’s <span class="tooltip">LMP<span class="tooltiptext">last menstrual period</span></span> and the child's date of birth. Reported in whole weeks, rounded down to the nearest week.</td>
</tr>
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
<td style="padding: 8px; word-wrap: break-word; white-space: normal;">Participant response to <a href="https://www.census.gov/programs-surveys/acs.html">ACS</a> item about ethnic identity collected during screening. <i>See <a href="../../../changelog/knownissues/#mother-ethnicity">Known Issue</a>.</i></td>
</tr>
<tr>
<td style="padding: 8px; word-wrap: break-word; white-space: normal;">Mother race, multi-categorical</td>
<td style="padding: 8px; word-wrap: break-word; white-space: normal;"><code>screen_mother_race</code></td>
<td style="padding: 8px; word-wrap: break-word; white-space: normal;">Admin</td>
<td style="padding: 8px; word-wrap: break-word; white-space: normal;">Participant response to <a href="https://www.census.gov/programs-surveys/acs.html">ACS</a> item/question about racial identity collected during screening.  <i>See <a href="../../../changelog/knownissues/#duplicate-options-for-mother-race-variable">Known Issue</a>.</i></td>
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



