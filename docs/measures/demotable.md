# demo table

**NOTE**: Within the table and the variable names below, “child” refers to the child enrolled in HBCD and “mother” refers to the person carrying the child (i.e., pregnant with the child) at the time of V01.


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
    <thead>
      <tr>
        <th style="width: 30%; border: 1px solid #ddd; padding: 12px; text-align: center; word-wrap: break-word; white-space: normal;">Construct<br>[<code>Variable Name</code>]</th>
        <th style="width: 10%; border: 1px solid #ddd; padding: 12px; text-align: center; word-wrap: break-word; white-space: normal;">Source</th>
        <th style="width: 70%; border: 1px solid #ddd; padding: 12px; text-align: center; word-wrap: break-word; white-space: normal;">Description/Details</th>
      </tr>
    </thead>
    <tbody>
<tr>
<td style="border: 1px solid #ddd; padding: 4px; word-wrap: break-word; white-space: normal;">Child sex<br>[<code>sex</code>]</td>
<td style="border: 1px solid #ddd; padding: 4px; word-wrap: break-word; white-space: normal;"><span class="tooltip">Administrative data<span class="tooltiptext">Recorded by Research Assistant within administrative data once the child was born, as reported by parent.</span></span></td>
<td style="border: 1px solid #ddd; padding: 4px; word-wrap: break-word; white-space: normal;"><i>Available starting at visit V02.<i></td>
</tr>
<tr>
<td style="border: 1px solid #ddd; padding: 4px; word-wrap: break-word; white-space: normal;">Child ethnicity<br>[<code>child_ethnicity</code>]</td>
<td style="border: 1px solid #ddd; padding: 4px; word-wrap: break-word; white-space: normal;"><span class="tooltip">Administrative data<span class="tooltiptext">Recorded by Research Assistant within administrative data once the child was born, as reported by parent.</span></span></td>
<td style="border: 1px solid #ddd; padding: 4px; word-wrap: break-word; white-space: normal;">Standard item on ethnicity from the American Community Survey.<br><i>Available starting at visit V02.<i></td>
</tr>
<tr>
<td style="border: 1px solid #ddd; padding: 4px; word-wrap: break-word; white-space: normal;">Child race<br>[<code>child_race</code>]</td>
<td style="border: 1px solid #ddd; padding: 4px; word-wrap: break-word; white-space: normal;"><span class="tooltip">Administrative data<span class="tooltiptext">Recorded by Research Assistant within administrative data once the child was born, as reported by parent.</span></span></td>
<td style="border: 1px solid #ddd; padding: 4px; word-wrap: break-word; white-space: normal;">Standard item on race from the American Community Survey.<br><i>Available starting at visit V02.<i></td>
</tr>
<tr>
<td style="border: 1px solid #ddd; padding: 4px; word-wrap: break-word; white-space: normal;">Child race and ethnicity combined - multiracial aggregation by Hispanic and non-Hispanic distinction<br>[<code>child_ethnoracial_acs_by_multi_ethnicity</code>]</td>
<td style="border: 1px solid #ddd; padding: 4px; word-wrap: break-word; white-space: normal;"><span class="tooltip">Administrative data<span class="tooltiptext">Recorded by Research Assistant within administrative data once the child was born, as reported by parent.</span></span></td>
<td style="border: 1px solid #ddd; padding: 4px; word-wrap: break-word; white-space: normal;">Constructed from <code>child_race</code> and <code>child_ethnicity</code> following <span class="tooltip">current federal standards<span class="tooltiptext">i.e., if a child is identified as Hispanic or Latino based on the response to the ethnicity item, they will be categorized as such, regardless of their race</span></span>. Children with multiple races endorsed are classified as "multiracial" and split into Hispanic and non-Hispanic subgroups.<br><i>Available starting visit V02.<i></td>
</tr>
<tr>
<td style="border: 1px solid #ddd; padding: 4px; word-wrap: break-word; white-space: normal;">Child race and ethnicity combined - multiracial aggregation by Black and non-Black distinction<br>[<code>child_ethnoracial_acs_by_multi_race</code>]</td>
<td style="border: 1px solid #ddd; padding: 4px; word-wrap: break-word; white-space: normal;"><span class="tooltip">Administrative data<span class="tooltiptext">Recorded by Research Assistant within administrative data once the child was born, as reported by parent.</span></span></td>
<td style="border: 1px solid #ddd; padding: 4px; word-wrap: break-word; white-space: normal;">Constructed from <code>child_race</code> and <code>child_ethnicity</code> following <span class="tooltip">current federal standards<span class="tooltiptext">i.e., if a child is identified as Hispanic or Latino based on the response to the ethnicity item, they will be categorized as such, regardless of their race</span></span>. 
Children with multiple races endorsed are classified as "multiracial" and split those who do and do not include Black/African American as an identity.<br><i>Available starting visit V02.<i></td>
</tr>
<tr>
<td style="border: 1px solid #ddd; padding: 4px; word-wrap: break-word; white-space: normal;">Maternal age at V01<br>[<code>mother_age_v01</code>]</td>
<td style="border: 1px solid #ddd; padding: 4px; word-wrap: break-word; white-space: normal;">Constructed</td>
<td style="border: 1px solid #ddd; padding: 4px; word-wrap: break-word; white-space: normal;">'MAV01' is a constructed variable that represents the birth parent's age, obtained from the scheduled date of the V01 visit. The age is reported in years to two decimal places, with fractional years calculated by dividing the number of whole months (rounded down) by 12. This variable is static and does not change over time.
</td>
</tr>
<tr>
<td style="border: 1px solid #ddd; padding: 4px; word-wrap: break-word; white-space: normal;">Maternal Age at Delivery<br>[<code>mother_age_delivery</code>]</td>
<td style="border: 1px solid #ddd; padding: 4px; word-wrap: break-word; white-space: normal;">Constructed</td>
<td style="border: 1px solid #ddd; padding: 4px; word-wrap: break-word; white-space: normal;">'MAD' is a constructed variable that represents the birth parent’s age at the time of their child's delivery (date of birth). It is reported in years to two decimal places, with fractional years calculated by dividing the total whole months (rounded down) by 12. This variable is static and does not change over time. <br />These data will be missing from V01 Basic Demographics, and available starting at V02.</td>
</tr>
<tr>
<td style="border: 1px solid #ddd; padding: 4px; word-wrap: break-word; white-space: normal;">Gestational Age at Delivery<br>[<code>gestational_age_delivery</code>]</td>
<td style="border: 1px solid #ddd; padding: 4px; word-wrap: break-word; white-space: normal;">Constructed</td>
<td style="border: 1px solid #ddd; padding: 4px; word-wrap: break-word; white-space: normal;">'GAD' is a constructed variable that represents the time elapsed between the first day of the birth parent’s last menstrual period (LMP), derived from the estimated date of delivery (EDD) minus 280 days, and the child's date of birth. It is reported in whole weeks, rounded down to the nearest week. This variable is static and does not change over time. <br />These data will be missing from V01 Basic Demographics, and available starting at V02.</td>
</tr>
<tr>
<td style="border: 1px solid #ddd; padding: 4px; word-wrap: break-word; white-space: normal;">Mother combined race and ethnicity at screening into study - multiracial category split into Hispanic and non-Hispanic groups<br>[<code>screen_mother_ethnoracial_acs_by_multi_ethnicity</code>]</td>
<td style="border: 1px solid #ddd; padding: 4px; word-wrap: break-word; white-space: normal;">Constructed from participant responses to separate questions of race and ethnicity collected during screening</td>
<td style="border: 1px solid #ddd; padding: 4px; word-wrap: break-word; white-space: normal;">This is a constructed race and ethnicity variable where individuals are placed into a single category. Individuals that select more than one response for race are placed into a multiracial group, which is split into subcategories for those who do and do not indicate Hispanic or Latino ethnicity as one of their select identities.</td>
</tr>
<tr>
<td style="border: 1px solid #ddd; padding: 4px; word-wrap: break-word; white-space: normal;">Mother combined race and ethnicity at screening into study &ndash; multiracial category split into Black and non-Black groups<br>[<code>screen_mother_ethnoracial_acs_by_multi_ethnicity</code>]</td>
<td style="border: 1px solid #ddd; padding: 4px; word-wrap: break-word; white-space: normal;">Constructed from participant responses to separate questions of race and ethnicity collected during screening</td>
<td style="border: 1px solid #ddd; padding: 4px; word-wrap: break-word; white-space: normal;">This is a constructed race and ethnicity variable where individuals are placed into a single category. Individuals that select more than one response for race are placed into a multiracial group, which is split into subcategories for those who do and do not indicate Black/African American as one of their selected identities.</td>
</tr>
<tr>
<td style="border: 1px solid #ddd; padding: 4px; word-wrap: break-word; white-space: normal;">Mother race and ethnicity<br>[<code>rc_mother_ethnoracial_aou_race_ethnicity</code>]</td>
<td style="border: 1px solid #ddd; padding: 4px; word-wrap: break-word; white-space: normal;">V01 Demographics Survey single race and ethnicity item (Source: <a class="in-cell-link" href="https://support.researchallofus.org/hc/en-us/articles/360039299632-Race-and-ethnicity-generalizations" target="_blank">All of Us</a>)</td>
<td style="border: 1px solid #ddd; padding: 4px; word-wrap: break-word; white-space: normal;">Scoring follows OMB standards: anyone identifying as Hispanic/Latino (alone or with another group) is categorized as Hispanic/Latino; all others as non-Hispanic.</td>
</tr>
<tr>
<td style="border: 1px solid #ddd; padding: 4px; word-wrap: break-word; white-space: normal;">Mother ethnicity<br>[<code>Screen_mother_ethnicity</code>]</td>
<td style="border: 1px solid #ddd; padding: 4px; word-wrap: break-word; white-space: normal;">Screening</td>
<td style="border: 1px solid #ddd; padding: 4px; word-wrap: break-word; white-space: normal;">Participant response to a single item/question from the American Community Survey about ethnic identity collected during screening. See <a href="../../changelog/knownissues/#mother-ethnicity">Known Issue</a></td>
</tr>
<tr>
<td style="border: 1px solid #ddd; padding: 4px; word-wrap: break-word; white-space: normal;">Mother race, multi-categorical variable from screening<br>[<code>screen_mother_race</code>]</td>
<td style="border: 1px solid #ddd; padding: 4px; word-wrap: break-word; white-space: normal;">Screening</td>
<td style="border: 1px solid #ddd; padding: 4px; word-wrap: break-word; white-space: normal;">Participant response to a single item/question from the American Community Survey about racial identity collected during screening.</td>
</tr>
<tr>
<td style="border: 1px solid #ddd; padding: 4px; word-wrap: break-word; white-space: normal;">Mother race, indicator variables from screening item<br>[<code>screen_mother_race_multi___{0 - 5}</code>]</td>
<td style="border: 1px solid #ddd; padding: 4px; word-wrap: break-word; white-space: normal;">Screening</td>
<td style="border: 1px solid #ddd; padding: 4px; word-wrap: break-word; white-space: normal;">Indicator variables for responses to ACS race question:<br>
___0=White; ___1=Black or African American; ___2=American Indian or Alaskan Native; ___3=Asian; ___4=Native Hawaiian or other Pacific Islander; ___5="Other race"</td>
</tr>
<tr>
<td style="border: 1px solid #ddd; padding: 4px; word-wrap: break-word; white-space: normal;">Mother race, indicator variables from survey item<br>[<code>rc_mother_race___{0 - 7}</code>]</td>
<td style="border: 1px solid #ddd; padding: 4px; word-wrap: break-word; white-space: normal;">Screening</td>
<td style="border: 1px solid #ddd; padding: 4px; word-wrap: break-word; white-space: normal;">Indicator variables for responses to <a class="in-cell-link" href="https://support.researchallofus.org/hc/en-us/articles/360039299632-Race-and-ethnicity-generalizations" target="_blank">All of Us</a> combined race and ethnicity question that is part of the Demographic survey:<br>
___0=American Indian or Alaskan Native; ___1=Asian; ___2=Black, African American, or African; ___3=Hispanic, Latino, or Spanish; ___4=Middle Eastern or North African; ___5=Native Hawaiian or other Pacific Islander; ___6=White; 7=None of these fully describe me.</td>
</tr>
<tr>
<td style="border: 1px solid #ddd; padding: 4px; word-wrap: break-word; white-space: normal;">Mother education<br>[<code>rc_mother_education</code>]</td>
<td style="border: 1px solid #ddd; padding: 4px; word-wrap: break-word; white-space: normal;">V01 Demographics survey <code>sed_bm_demo_edu_001</code></td>
<td style="border: 1px solid #ddd; padding: 4px; word-wrap: break-word; white-space: normal;"> </td>
</tr>
<tr>
<td style="border: 1px solid #ddd; padding: 4px; word-wrap: break-word; white-space: normal;">Total combined household income<br>[<code>rc_mother_income</code>]</td>
<td style="border: 1px solid #ddd; padding: 4px; word-wrap: break-word; white-space: normal;">V01 Demographics survey <code>sed_bm_demo_income_002</code></td>
<td style="border: 1px solid #ddd; padding: 4px; word-wrap: break-word; white-space: normal;"> </td>
</tr>
<tr>
<td style="border: 1px solid #ddd; padding: 4px; word-wrap: break-word; white-space: normal;">Recruitment site<br>[<code>recruitment_site</code>]</td>
<td style="border: 1px solid #ddd; padding: 4px; word-wrap: break-word; white-space: normal;">Recruitment site</code></td>
<td style="border: 1px solid #ddd; padding: 4px; word-wrap: break-word; white-space: normal;">De-identified value</td>
</tr>
</tbody>
</table>
</div>