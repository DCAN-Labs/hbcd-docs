# demotable

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
        <th style="width: 20%; text-align: center; word-wrap: break-word; white-space: normal;">Source (<span class="tooltip">Admin Records<span class="tooltiptext">Recorded by Research Assistant within administrative data once the child was born, as reported by parent.</span></span> or V01 Demographics)</th>
        <th style="width: 50%; text-align: center; word-wrap: break-word; white-space: normal;">Description</th>
      </tr>
    </thead>
    <tbody>
<tr>
<td style="word-wrap: break-word; white-space: normal;">Child sex</td>
<td style="word-wrap: break-word; white-space: normal;"><code>sex</code></td>
<td style="word-wrap: break-word; white-space: normal;">Admin records</td>
<td style="word-wrap: break-word; white-space: normal;"><span class="tooltip tooltip-left"><i>Visit V02 onward</i><span class="tooltiptext">Data are not collected prior to birth, i.e. at the prenatal V01 visit, and will be available starting at visit V02</span></span></td>
</tr>
<tr>
<td style="word-wrap: break-word; white-space: normal;">Child ethnicity</td>
<td style="word-wrap: break-word; white-space: normal;"><code>child_ethnicity</code></td>
<td style="word-wrap: break-word; white-space: normal;">Admin records</td>
<td style="word-wrap: break-word; white-space: normal;"><a href="https://www.census.gov/programs-surveys/acs.html">ACS</a>-standard ethnicity item. <span class="tooltip tooltip-left"><i>Visit V02 onward</i><span class="tooltiptext">Data are not collected prior to birth, i.e. at the prenatal V01 visit, and will be available starting at visit V02</span></span><i></i></td>
</tr>
<tr>
<td style="word-wrap: break-word; white-space: normal;">Child race</td>
<td style="word-wrap: break-word; white-space: normal;"><code>child_race</code></td>
<td style="word-wrap: break-word; white-space: normal;">Admin records</td>
<td style="word-wrap: break-word; white-space: normal;"><a href="https://www.census.gov/programs-surveys/acs.html">ACS</a>-standard race item. <span class="tooltip"><i>Visit V02 onward</i><span class="tooltiptext">Data are not collected prior to birth, i.e. at the prenatal V01 visit, and will be available starting at visit V02</span></span><i></i></td>
</tr>
<tr>
<td style="word-wrap: break-word; white-space: normal;">Child race and ethnicity combined - multiracial aggregation by Hispanic and non-Hispanic distinction</td>
<td style="word-break: break-all; white-space: normal;"><code>child_ethnoracial_acs_by_multi_ethnicity</code></td>
<td style="word-wrap: break-word; white-space: normal;">?</td>
<td style="word-wrap: break-word; white-space: normal;">Constructed from <code>child_race</code> and <code>child_ethnicity</code> following <span class="tooltip">current federal standards<span class="tooltiptext">i.e., if a child is identified as Hispanic or Latino based on the response to the ethnicity item, they will be categorized as such, regardless of their race</span></span>. Children with multiple races endorsed are classified as "multiracial" and split into Hispanic and non-Hispanic subgroups. <span class="tooltip"><i>Visit V02 onward</i><span class="tooltiptext">Data are not collected prior to birth, i.e. at the prenatal V01 visit, and will be available starting at visit V02</span></span><i></i></td>
</tr>
<tr>
<td style="word-wrap: break-word; white-space: normal;">Child race and ethnicity combined - multiracial aggregation by Black and non-Black distinction</td>
<td style="word-break: break-all; white-space: normal;"><code>child_ethnoracial_acs_by_multi_race</code></td>
<td style="word-wrap: break-word; white-space: normal;">?</td>
<td style="word-wrap: break-word; white-space: normal;">Constructed from <code>child_race</code> and <code>child_ethnicity</code> following <span class="tooltip">current federal standards<span class="tooltiptext">i.e., if a child is identified as Hispanic or Latino based on the response to the ethnicity item, they will be categorized as such, regardless of their race</span></span>. Children with multiple races endorsed are classified as "multiracial" and split into those who do and do not include Black/African American as an identity. <span class="tooltip"><i>Visit V02 onward</i><span class="tooltiptext">Data are not collected prior to birth, i.e. at the prenatal V01 visit, and will be available starting at visit V02</span></span><i></i></td>
</tr>
<tr>
<td style="word-wrap: break-word; white-space: normal;">Mother combined race and ethnicity - multiracial category split into Hispanic and non-Hispanic groups</td>
<td style="word-break: break-all; white-space: normal"><code>screen_mother_ethnoracial_acs_by_multi_ethnicity</code></td>
<td style="word-wrap: break-word; white-space: normal;">V01 Demographics</td>
<td style="word-wrap: break-word; white-space: normal;">Derived from screening responses to separate race and ethnicity questions. Individuals are assigned a single category, with subcategories for multiracial individuals based on <span class="tooltip">Hispanic or Latino ethnicity<span class="tooltiptext">Participants who select multiple races are grouped as multiracial, split into subcategories for those who do and do not indicate Hispanic or Latino ethnicity as one of their selected identities.</span></span></td>
</tr>
<tr>
<td style="word-wrap: break-word; white-space: normal;">Mother combined race and ethnicity - multiracial category split into Black and non-Black groups</td>
<td style="word-break: break-all; white-space: normal;"><code>screen_mother_ethnoracial_acs_by_multi_race</code></td>
<td style="word-wrap: break-word; white-space: normal;">V01 Demographics</td>
<td style="word-wrap: break-word; white-space: normal;">Derived from screening responses to separate race and ethnicity questions. Individuals are assigned a single category, with subcategories for multiracial individuals based on <span class="tooltip">Black/African American identity<span class="tooltiptext">Participants who select multiple races are grouped as multiracial, split into subcategories for those who do and do not indicate Black/African American as one of their selected identities.</span></span></td>
</tr>
<tr>
<td style="word-wrap: break-word; white-space: normal;">Mother race and ethnicity</td>
<td style="word-break: break-all; white-space: normal;"><code>rc_mother_ethnoracial_aou_race_ethnicity</code></td>
<td style="word-wrap: break-word; white-space: normal;">V01 Demographics</td>
<td style="word-wrap: break-word; white-space: normal;">Derived from single race and ethnicity item (Source: <a class="in-cell-link" href="https://support.researchallofus.org/hc/en-us/articles/360039299632-Race-and-ethnicity-generalizations" target="_blank">All of Us</a>) and scored following <span class="tooltip">OMB standards<span class="tooltiptext">Anyone identifying as Hispanic/Latino (alone or with another group) is categorized as Hispanic/Latino; all others as non-Hispanic</span>.</span></td>
</tr>
<tr>
<td style="word-wrap: break-word; white-space: normal;">Mother ethnicity</td>
<td style="word-wrap: break-word; white-space: normal;"><code>screen_mother_ethnicity</code></td>
<td style="word-wrap: break-word; white-space: normal;">Admin records</td>
<td style="word-wrap: break-word; white-space: normal;">Participant response to <a href="https://www.census.gov/programs-surveys/acs.html">ACS</a> item about ethnic identity collected during screening. <i>See <a href="../../changelog/knownissues/#mother-ethnicity">Known Issue</a>.</i></td>
</tr>
<tr>
<td style="word-wrap: break-word; white-space: normal;">Mother race, multi-categorical</td>
<td style="word-wrap: break-word; white-space: normal;"><code>screen_mother_race</code></td>
<td style="word-wrap: break-word; white-space: normal;">Admin records</td>
<td style="word-wrap: break-word; white-space: normal;">Participant response to <a href="https://www.census.gov/programs-surveys/acs.html">ACS</a> item/question about racial identity collected during screening.  <i>See <a href="../../changelog/knownissues/#duplicate-options-for-mother-race-variable">Known Issue</a>.</i></td>
</tr>
<tr>
<td style="word-wrap: break-word; white-space: normal;">Mother race, indicator variables from screening</td>
<td style="word-break: break-all; white-space: normal;"><code>screen_mother_race_multi___{0 - 5}</code></td>
<td style="word-wrap: break-word; white-space: normal;">Admin records</td>
<td style="word-wrap: break-word; white-space: normal;">Indicator variables from ACS race question:<br>
0 = White<br>
1 = Black or African American<br>
2 = American Indian or Alaskan Native<br>
3 = Asian<br>
4 = Native Hawaiian or other Pacific Islander<br>
5 = Other race</td>
</tr>
<tr>
<td style="word-wrap: break-word; white-space: normal;">Mother race, indicator variables from survey item</td>
<td style="word-wrap: break-word; white-space: normal;"><code>rc_mother_race___{0 - 7}</code></td>
<td style="word-wrap: break-word; white-space: normal;">?</td>
<td style="word-wrap: break-word; white-space: normal;">Indicator variables for responses to <a class="in-cell-link" href="https://support.researchallofus.org/hc/en-us/articles/360039299632-Race-and-ethnicity-generalizations" target="_blank">All of Us</a> combined race and ethnicity question part of the Demographic survey during screening:<br>
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
<td style="word-wrap: break-word; white-space: normal;">Mother education</td>
<td style="word-wrap: break-word; white-space: normal;"><code>rc_mother_education</code></td>
<td style="word-wrap: break-word; white-space: normal;">V01 Demographics</td>
<td style="word-wrap: break-word; white-space: normal;"><code>sed_bm_demo_edu_001</code></td>
</tr>
<tr>
<td style="word-wrap: break-word; white-space: normal;">Total combined household income</td>
<td style="word-wrap: break-word; white-space: normal;"><code>rc_mother_income</code></td>
<td style="word-wrap: break-word; white-space: normal;">V01 Demographics</td>
<td style="word-wrap: break-word; white-space: normal;"><code>sed_bm_demo_income_002</code></td>
</tr>
<tr>
<td style="word-wrap: break-word; white-space: normal;">Recruitment site</td>
<td style="word-wrap: break-word; white-space: normal;"><code>recruitment_site</code></td>
<td style="word-wrap: break-word; white-space: normal;">???</td>
<td style="word-wrap: break-word; white-space: normal;">De-identified value reflecting recruitment sites</td>
</tr>
</tbody>
</table>
</div>