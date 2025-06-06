# Demo table alt option

[![HBCD_EEG_Utilities](https://img.shields.io/badge/NMIND-17%2F42-orange?logo=data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgMjQgMjQiIGZpbGw9IiNDRDdGMzIiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+CiAgPHBhdGggZD0iTTMuMzc3NTIgNS4wODI0MUMzIDUuNjIwMjggMyA3LjIxOTA3IDMgMTAuNDE2N1YxMS45OTE0QzMgMTcuNjI5NCA3LjIzODk2IDIwLjM2NTUgOS44OTg1NiAyMS41MjczQzEwLjYyIDIxLjg0MjQgMTAuOTgwNyAyMiAxMiAyMkMxMy4wMTkzIDIyIDEzLjM4IDIxLjg0MjQgMTQuMTAxNCAyMS41MjczQzE2Ljc2MSAyMC4zNjU1IDIxIDE3LjYyOTQgMjEgMTEuOTkxNFYxMC40MTY3QzIxIDcuMjE5MDcgMjEgNS42MjAyOCAyMC42MjI1IDUuMDgyNDFDMjAuMjQ1IDQuNTQ0NTQgMTguNzQxNyA0LjAyOTk2IDE1LjczNTEgMy4wMDA3OUwxNS4xNjIzIDIuODA0NzJDMTMuNTk1IDIuMjY4MjQgMTIuODExNCAyIDEyIDJDMTEuMTg4NiAyIDEwLjQwNSAyLjI2ODI0IDguODM3NzIgMi44MDQ3Mkw4LjI2NDkxIDMuMDAwNzlDNS4yNTgzMiA0LjAyOTk2IDMuNzU1MDMgNC41NDQ1NCAzLjM3NzUyIDUuMDgyNDFaIi8+Cjwvc3ZnPgo=)](https://www.nmind.org/proceedings/hbcd-eeg-utilities/)


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
        <th style="width: 30%; border: 1px solid #ddd; padding: 12px; text-align: center; word-wrap: break-word; white-space: normal;">Construct</th>
        <th style="width: 10%; border: 1px solid #ddd; padding: 12px; text-align: center; word-wrap: break-word; white-space: normal;">Variable Name</th>
        <th style="width: 60%; border: 1px solid #ddd; padding: 12px; text-align: center; word-wrap: break-word; white-space: normal;">Description</th>
      </tr>
    </thead>
    <tbody>
<tr>
<td style="border: 1px solid #ddd; padding: 4px; word-wrap: break-word; white-space: normal;">Child sex</td>
<td style="border: 1px solid #ddd; padding: 4px; word-wrap: break-word; white-space: normal;"><code>sex</code></td>
<td style="border: 1px solid #ddd; padding: 4px; word-wrap: break-word; white-space: normal;">Obtained from <span class="tooltip">administrative records<span class="tooltiptext">Recorded by Research Assistant within administrative data once the child was born, as reported by parent.</span>.</span> <i>Available for visit V02 onward.<i></td>
</tr>
<tr>
<td style="border: 1px solid #ddd; padding: 4px; word-wrap: break-word; white-space: normal;">Child ethnicity</td>
<td style="border: 1px solid #ddd; padding: 4px; word-wrap: break-word; white-space: normal;"><code>child_ethnicity</code></td>
<td style="border: 1px solid #ddd; padding: 4px; word-wrap: break-word; white-space: normal;"><a href="https://www.census.gov/programs-surveys/acs.html">ACS</a>-standard ethnicity item in <span class="tooltip">administrative records<span class="tooltiptext">Recorded by Research Assistant within administrative data once the child was born, as reported by parent.</span></span>. <i>Available for visit V02 onward.<i></td>
</tr>
<tr>
<td style="border: 1px solid #ddd; padding: 4px; word-wrap: break-word; white-space: normal;">Child race</td>
<td style="border: 1px solid #ddd; padding: 4px; word-wrap: break-word; white-space: normal;"><code>child_race</code></td>
<td style="border: 1px solid #ddd; padding: 4px; word-wrap: break-word; white-space: normal;"><a href="https://www.census.gov/programs-surveys/acs.html">ACS</a>-standard race item in <span class="tooltip">administrative records<span class="tooltiptext">Recorded by Research Assistant within administrative data once the child was born, as reported by parent.</span></span>. <i>Available for visit V02 onward.<i></td>
</tr>
<tr>
<td style="border: 1px solid #ddd; padding: 4px; word-wrap: break-word; white-space: normal;">Child race and ethnicity combined - multiracial aggregation by Hispanic and non-Hispanic distinction</td>
<td style="border: 1px solid #ddd; padding: 4px; word-break: break-all; white-space: normal;"><code>child_ethnoracial_acs_by_multi_ethnicity</code></td>
<td style="border: 1px solid #ddd; padding: 4px; word-wrap: break-word; white-space: normal;">Constructed from <code>child_race</code> and <code>child_ethnicity</code> following <span class="tooltip">current federal standards<span class="tooltiptext">i.e., if a child is identified as Hispanic or Latino based on the response to the ethnicity item, they will be categorized as such, regardless of their race</span></span>. Children with multiple races endorsed are classified as "multiracial" and split into Hispanic and non-Hispanic subgroups. <i>Available for visit V02 onward.<i></td>
</tr>
<tr>
<td style="border: 1px solid #ddd; padding: 4px; word-wrap: break-word; white-space: normal;">Child race and ethnicity combined - multiracial aggregation by Black and non-Black distinction</td>
<td style="border: 1px solid #ddd; padding: 4px; word-wrap: break-word; white-space: normal;"><code>child_ethnoracial_acs_by_multi_race</code></td>
<td style="border: 1px solid #ddd; padding: 4px; word-wrap: break-word; white-space: normal;">Constructed from <code>child_race</code> and <code>child_ethnicity</code> following <span class="tooltip">current federal standards<span class="tooltiptext">i.e., if a child is identified as Hispanic or Latino based on the response to the ethnicity item, they will be categorized as such, regardless of their race</span></span>. Children with multiple races endorsed are classified as "multiracial" and split into those who do and do not include Black/African American as an identity. <i>Available for visit V02 onward.<i></td>
</tr>
<tr>
<td style="border: 1px solid #ddd; padding: 4px; word-wrap: break-word; white-space: normal;">Mother combined race and ethnicity - multiracial category split into Hispanic and non-Hispanic groups</td>
<td style="border: 1px solid #ddd; padding: 4px; word-break: break-all; white-space: normal;">
  <code>screen_mother_ethnoracial_acs_by_multi_ethnicity</code>
</td>
<td style="border: 1px solid #ddd; padding: 4px; word-wrap: break-word; white-space: normal;">Derived from screening responses to separate race and ethnicity questions. Individuals are assigned a single category; those selecting multiple races are grouped as multiracial, split into subcategories for those who do and do not indicate Hispanic or Latino ethnicity as one of their selected identities.</td>
</tr>
<tr>
<td style="border: 1px solid #ddd; padding: 4px; word-wrap: break-word; white-space: normal;">Mother combined race and ethnicity - multiracial category split into Black and non-Black groups</td>
<td style="border: 1px solid #ddd; padding: 4px; word-break: break-all; white-space: normal;"><code>screen_mother_ethnoracial_acs_by_multi_race</code></td>
<td style="border: 1px solid #ddd; padding: 4px; word-wrap: break-word; white-space: normal;">Derived from screening responses to separate race and ethnicity questions. Individuals are assigned a single category; those selecting multiple races are grouped as multiracial, split into subcategories for those who do and do not indicate Black/African American as one of their selected identities.</td>
</tr>
<tr>
<td style="border: 1px solid #ddd; padding: 4px; word-wrap: break-word; white-space: normal;">Mother race and ethnicity</td>
<td style="border: 1px solid #ddd; padding: 4px; word-break: break-all; white-space: normal;"><code>rc_mother_ethnoracial_aou_race_ethnicity</code></td>
<td style="border: 1px solid #ddd; padding: 4px; word-wrap: break-word; white-space: normal;">Derived from V01 Demographics Survey single race and ethnicity item (Source: <a class="in-cell-link" href="https://support.researchallofus.org/hc/en-us/articles/360039299632-Race-and-ethnicity-generalizations" target="_blank">All of Us</a>) and scored following <span class="tooltip">OMB standards<span class="tooltiptext">Anyone identifying as Hispanic/Latino (alone or with another group) is categorized as Hispanic/Latino; all others as non-Hispanic</span>.</span></td>
</tr>
<tr>
<td style="border: 1px solid #ddd; padding: 4px; word-wrap: break-word; white-space: normal;">Mother ethnicity</td>
<td style="border: 1px solid #ddd; padding: 4px; word-wrap: break-word; white-space: normal;"><code>screen_mother_ethnicity</code></td>
<td style="border: 1px solid #ddd; padding: 4px; word-wrap: break-word; white-space: normal;">Participant response to <a href="https://www.census.gov/programs-surveys/acs.html">ACS</a> item/question about ethnic identity collected during screening. <i>See <a href="../../changelog/knownissues/#mother-ethnicity">Known Issue</a>.</i></td>
</tr>
<tr>
<td style="border: 1px solid #ddd; padding: 4px; word-wrap: break-word; white-space: normal;">Mother race, multi-categorical</td>
<td style="border: 1px solid #ddd; padding: 4px; word-wrap: break-word; white-space: normal;"><code>screen_mother_race</code></td>
<td style="border: 1px solid #ddd; padding: 4px; word-wrap: break-word; white-space: normal;">Participant response from screening to <a href="https://www.census.gov/programs-surveys/acs.html">ACS</a> item/question about racial identity collected during screening.  <i>See <a href="../../changelog/knownissues/#duplicate-options-for-mother-race-variable">Known Issue</a>.</i></td>
</tr>
<tr>
<td style="border: 1px solid #ddd; padding: 4px; word-wrap: break-word; white-space: normal;">Mother race, indicator variables from screening</td>
<td style="border: 1px solid #ddd; padding: 4px; word-break: break-all; white-space: normal;"><code>screen_mother_race_multi___{0 - 5}</code></td>
<td style="border: 1px solid #ddd; padding: 4px; word-wrap: break-word; white-space: normal;">Indicator variables from ACS race screening question:<br>
___0 = White<br>
___1 = Black or African American<br>
___2 = American Indian or Alaskan Native<br>
___3 = Asian<br>
___4 = Native Hawaiian or other Pacific Islander<br>
___5 = Other race</td>
</tr>
<tr>
<td style="border: 1px solid #ddd; padding: 4px; word-wrap: break-word; white-space: normal;">Mother race, indicator variables from survey item</td>
<td style="border: 1px solid #ddd; padding: 4px; word-break: break-all; white-space: normal;"><code>rc_mother_race___{0 - 7}</code></td>
<td style="border: 1px solid #ddd; padding: 4px; word-wrap: break-word; white-space: normal;">Indicator variables for responses to <a class="in-cell-link" href="https://support.researchallofus.org/hc/en-us/articles/360039299632-Race-and-ethnicity-generalizations" target="_blank">All of Us</a> combined race and ethnicity question part of the Demographic survey during screening:<br>
___0 = American Indian or Alaskan Native<br>
___1 = Asian<br>
___2 = Black, African American, or African<br>
___3 = Hispanic, Latino, or Spanish<br>
___4 = Middle Eastern or North African<br>
___5 = Native Hawaiian or other Pacific Islander<br>
___6 = White<br>
___7 = None of these fully describe me</td>
</tr>
<tr>
<td style="border: 1px solid #ddd; padding: 4px; word-wrap: break-word; white-space: normal;">Mother education</td>
<td style="border: 1px solid #ddd; padding: 4px; word-wrap: break-word; white-space: normal;"><code>rc_mother_education</code></td>
<td style="border: 1px solid #ddd; padding: 4px; word-wrap: break-word; white-space: normal;">V01 Demographics survey variable <code>sed_bm_demo_edu_001</code></td>
</tr>
<tr>
<td style="border: 1px solid #ddd; padding: 4px; word-wrap: break-word; white-space: normal;">Total combined household income</td>
<td style="border: 1px solid #ddd; padding: 4px; word-wrap: break-word; white-space: normal;"><code>rc_mother_income</code></td>
<td style="border: 1px solid #ddd; padding: 4px; word-wrap: break-word; white-space: normal;">V01 Demographics survey variable <code>sed_bm_demo_income_002</code></td>
</tr>
<tr>
<td style="border: 1px solid #ddd; padding: 4px; word-wrap: break-word; white-space: normal;">Recruitment site</td>
<td style="border: 1px solid #ddd; padding: 4px; word-wrap: break-word; white-space: normal;"><code>recruitment_site</code></td>
<td style="border: 1px solid #ddd; padding: 4px; word-wrap: break-word; white-space: normal;">De-identified value reflecting recruitment sites</td>
</tr>
</tbody>
</table>
</div>
