# Physical Health

## Instruments
The current data release includes the following Physical Health Measures instruments:

<table style="width: 100%; border-collapse: collapse; table-layout: fixed;">
  <thead>
    <tr>
      <th style="border: 1px solid #ddd; padding: 8px; text-align: left;">Name of Instrument</th>
      <th style="border: 1px solid #ddd; padding: 8px; text-align: left;">Acronym</th>
      <th style="border: 1px solid #ddd; padding: 8px; text-align: left;">Construct</th>
      <th style="border: 1px solid #ddd; padding: 8px; text-align: left;">Table Name</th>
    </tr>
  </thead>
<tbody>
  <tr>
    <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;"><a href="#breastfeeding">Breast Feeding History</a></td>
    <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">PHENX BF</td>
    <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">Nutrition</td>
    <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">ph_cg_phx__bfh</td>
  </tr>
  <tr>
    <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;"><a href="#food-insecurity">2-item Food Insecurity</a></td>
    <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">USDA short form</td>
    <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">Food insecurity</td>
    <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">sed_cg_foodins</td>
  </tr>
  <tr>
    <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;"><a href="#growth">Height/Weight/Head Circumference</a></td>
    <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">Growth</td>
    <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">Growth</td>
    <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">ph_ch_anthro</td>
  </tr>  
</tbody>
</table>

## Implementation & Data Collection

All metrics are child-specific. Surveys were translated to Spanish for HBCD by [BURG Translations](https://burgtranslations.com/our-services/). Additional information is as follows:

<table style="width: 100%; border-collapse: collapse; table-layout: fixed;">
<tfoot><tr><td colspan="4"><small><b>**</b> V08 (31-45 months) only administered if still breastfeeding at prior visit</small></td></tr></tfoot>
  <thead>
    <tr>
      <th style="border: 1px solid #ddd; padding: 8px; text-align: left;">Instrument</th>
      <th style="border: 1px solid #ddd; padding: 8px; text-align: left;">Visits</th>
      <th style="border: 1px solid #ddd; padding: 8px; text-align: left;">Administration</th>
      <th style="border: 1px solid #ddd; padding: 8px; text-align: left;">Completion Time</th>      
    </tr>
  </thead>
<tbody>
	<tr>
		<td>PHENX BF</td>
		<td>V02, V03, V04, V06, V08<b>**</b></td>
    <td>Remote (by Caregiver)</td>
		<td>1 min</td>
	</tr>
  <tr>
		<td>2-Item Food Insecurity</td>
		<td>V02, V03</td>
    <td>Remote (by Caregiver)</td>
		<td>1 min</td>
	</tr>
  <tr>
		<td>Growth</td>
		<td>V02, V03, V04, V06, V08</td>
    <td>In Person</td>
		<td>5 min</td>
	</tr>  
</tbody>
</table>

## Quality Control
The QC procedures for all three measures involved monitoring the data dashboard for variable missingness, possible coding errors, scoring verification when needed, and data consistency.

## Instrument Details
### Breastfeeding     
<p>
<div id="bf-warning" class="warning-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fas fa-exclamation-triangle"></i></span>
  <span class="text">Data Warning</span>
  <span class="arrow">▸</span>
</div>
<div class="warning-collapsible-content">
<p>Breast feeding history is obtained via self-report, so is vulnerable to recall bias concerning the timing of starting and/or stopping breast feeding. In addition, as the data is obtained via a survey, it is likely that missing data will need to be statistically addressed during analysis.</p> 
</div>
</p>

Breastfeeding measures initiation, exclusivity, and cessation of breast milk feedings.

### Food Insecurity
<p>
<div id="foodins-warning" class="warning-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fas fa-exclamation-triangle"></i></span>
  <span class="text">Data Warning</span>
  <span class="arrow">▸</span>
</div>
<div class="warning-collapsible-content">
<p>Researchers should be aware that the validated measure uses Yes/No answers and does not account for missing data.</p> 
</div>
</p>

Food Insecurity, based on two items assessing the availability of food, is a screening measure used across many populations indicating risk of food insecurity in the last 12 months. Each question uses the same response options. This measure was modified slightly for HBCD to use gender-neutral terms (children are referred to as “the child” in place of gendered pronouns) as well as inclusion of "Don't know" as a response option to survey questions.

### Growth   
<p>
<div id="growth-warning" class="warning-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fas fa-exclamation-triangle"></i></span>
  <span class="text">Data Warning</span>
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
</p>
Growth is a standard direct measure of child growth, including height or length (in cm), weight (in kg), and head circumference (cm). In older children, it will also include abdominal circumference (cm).

## References
<div class="references">
    <p>Hager, E. R., Quigg, A. M., Black, M. M., Coleman, S. M., Heeren, T., Rose-Jacobs, R., Cook, J. T., Ettinger de Cuba, S. A., Casey, P. H., Chilton, M., Cutts, D. B., Meyers, A. F., &amp; Frank, D. A. (2010). Development and validity of a 2-item screen to identify families at risk for food insecurity. <em>Pediatrics</em>, 126(1), e26-32. <a href="https://doi.org/10.1542/peds.2009-3146">https://doi.org/10.1542/peds.2009-3146</a></p>
</div>
<br>

