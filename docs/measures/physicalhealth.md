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
    <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">ph_cg_phx_i_bfh</td>
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
    <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">Unknown</td>
  </tr>  
</tbody>
</table>

## Implementation & Data Collection

The Breastfeeding and Food Insecurity surveys are child-specific and filled out remotely by the primary caregiver while growth is a direct measure in-person. Surveys were translated to Spanish for HBCD by [BURG Translations](https://burgtranslations.com/our-services/). Additional information is as follows:

<table style="width: 100%; border-collapse: collapse; table-layout: fixed;">
  <thead>
    <tr>
      <th style="border: 1px solid #ddd; padding: 8px; text-align: left;">Instrument</th>
      <th style="border: 1px solid #ddd; padding: 8px; text-align: left;">Visits</th>
      <th style="border: 1px solid #ddd; padding: 8px; text-align: left;">Completion Time</th>      
    </tr>
  </thead>
<tbody>
	<tr>
		<td>PHENX BF</td>
		<td>V02, V03, V04, V06, V08 (31-45 months)**</td>
		<td>1 min</td>
	</tr>
  <tr>
		<td>2-Item Food Insecurity</td>
		<td>V02, V03</td>
		<td>1 min</td>
	</tr>
  <tr>
		<td>Growth</td>
		<td>V02, V03, V04, V06, V08 (31-45 months)</td>
		<td>5 min</td>
	</tr>  
</tbody>
</table>
<small>**Only administered if still breastfeeding at prior visit</small>

## Quality Control
The QC procedures for all three measures involved monitoring the data dashboard for variable missingness, possible coding errors, scoring verification when needed, and data consistency.

## Instrument Details
### Breastfeeding     
<p>
<div id="bf-warning" class="warning-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fas fa-exclamation-triangle"></i></span>
  <span class="text">Expert Review: Known Issues and/or Research Considerations</span>
  <span class="arrow">▸</span>
</div>
<div class="collapsible-content">
<br>
<p>Subject matter experts emphasize that, as breast feeding history is obtained via self-report, it is vulnerable to recall bias* concerning the timing of starting and/or stopping breast feeding. In addition, as the data is obtained via a survey, it is likely that missing data will need to be statistically addressed during analysis.</p> 
</div>
</p>

Breastfeeding measures initiation, exclusivity, and cessation of breast milk feedings.

### Food Insecurity
<p>
<div id="foodins-warning" class="warning-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fas fa-exclamation-triangle"></i></span>
  <span class="text">Expert Review: Known Issues and/or Research Considerations</span>
  <span class="arrow">▸</span>
</div>
<div class="collapsible-content">
<br>
<p>Researchers should be aware that the validated measure uses Yes/No answers and does not account for missing data.</p> 
</div>
</p>

Food Insecurity, based on two items assessing the availability of food, is a screening measure used across many populations indicating risk of food insecurity in the last 12 months. Each question uses the same response options. This measure was modified slightly for HBCD to use gender-neutral terms (children are referred to as “the child” in place of gendered pronouns) as well as inclusion of "Don't know" as a response option to survey questions.

### Growth   
<p>
<div id="growth-warning" class="warning-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fas fa-exclamation-triangle"></i></span>
  <span class="text">Expert Review: Known Issues and/or Research Considerations</span>
  <span class="arrow">▸</span>
</div>
<div class="collapsible-content">
<br>
<p>Please note that range checks were implemented in the database on 7/1/2024 so are not reflected in data included in the first data release. Outliers are possible.</p> 
</div>
</p>
Growth is a standard direct measure of child height or length (in cm), weight (in kg), head circumference (cm). In older children, it will also include abdominal circumference (cm).


## References
<div class="references">
    <p>Hager, E. R., Quigg, A. M., Black, M. M., Coleman, S. M., Heeren, T., Rose-Jacobs, R., Cook, J. T., Ettinger de Cuba, S. A., Casey, P. H., Chilton, M., Cutts, D. B., Meyers, A. F., &amp; Frank, D. A. (2010). Development and validity of a 2-item screen to identify families at risk for food insecurity. <em>Pediatrics</em>, 126(1), e26-32. <a href="https://doi.org/10.1542/peds.2009-3146">https://doi.org/10.1542/peds.2009-3146</a></p>
</div>
<br>

