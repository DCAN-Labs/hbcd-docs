# Growth

**Full Name**: Height/Weight/Head Circumference              
**Acronym**: Growth                  
**Table Name**: `ph_ch_anthro`       
**Construct**: Growth is a standard direct measure of child growth, including height or length (in cm), weight (in kg), and head circumference (cm). In older children, it will also include abdominal circumference (cm).

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
<p>Please note that range checks for Growth (<code>ph_ch_anthro</code>) were implemented in the database on 7/1/2024 and so are not reflected in data included in the first data release. Extreme out-of-range values were excluded (converted to 'n/a'), but some outliers are possible. Valid values for Growth fields are documented in the section on Exclusion Criteria (see <a href="../../datacuration/exclusions#filtered-values">Filtered Out-Of-Range Field Values</a>) and provided below for quick reference:</p>
<ul>
  <li>Length (<code>len_001_i_03</code>): min 30 / max 130 (cm) </li>
  <li>Weight (<code>wei_001_i_03</code>): min 0.5 / max 30  (kg)</li>
  <li>Head Circumference (<code>head_001_i_03</code>): min 25 / max 55 (cm)</li>
</ul>
<p>In addition, because dates of birth are jittered and calculated chronologic and adjusted ages are ±6 days, we do not provide z-scores in the current data release. Further, we do NOT recommend calculating Z-scores using V02 data. Caution is recommended when calculating Z-scores using data from subsequent visits.</p>
</div>

## Administration & Quality Control

<table style="width: 100%; border-collapse: collapse; table-layout: fixed; font-size: 16px;">
<tbody>
<tr><td><b>Child Specific</b></td>
<td>Yes</td></tr>
<tr><td><b>Respondent</b></td>
<td>Parent</td></tr>
<tr><td><b>Administration</b></td>
<td style="word-wrap: break-word; white-space: normal;">HBCD Study Staff, in person. Surveys were translated to Spanish for HBCD by <a href="https://burgtranslations.com/our-services/">BURG Translations</a>.</td></tr>
<tr><td><b>Visits</b></td>
<td>V02, V03, V04, V06, V08</td></tr>
<tr><td><b>Completion Time</b></td>
<td>5 min</td></tr>
<tr><td><b>Quality Control</b></td>
<td style="word-wrap: break-word; white-space: normal;">Monitor data dashboard for variable missingness, possible coding errors, scoring verification when needed, and data consistency.</td></tr>
</tbody>
</table>




