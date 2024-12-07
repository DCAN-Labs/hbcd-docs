# Blood
**Full Name**: BLOOD		              
**Construct**: Toxicology screen, blood        
**Description**:  Results of toxicology assays in dried blood spots collected at V1

Processing of Blood Spot Cards consists of preparing three 1/8” punches of dried blood spot followed by extraction using an organic solvent. Detection of PETH in the extract is accomplished with a single pass using LCMSMS (**Figure 1**):

**Figure 1. Blood Processing**
<img src="Fig1_blood.png" width="100%" height="auto">

<br>

<details>
<summary>Implementation & Data Collection Details</summary>
<ul>
<li><b>Method of Administration</b>: Phlebotomist-collected venous blood, which is pipetted onto dried blood spot cards</li>
<li><b>Respondent</b>: Pregnant person</li>
<li><b>Visits</b>: V01</li>
<li><b>Estimated length of time for completion</b>: 5 minutes</li>
</ul>
</details>


## PEth Assay
PEth assays are confirmation-only testing. Test results were determined to be positive (*c_peth_b_cat*), negative, or canceled according to the thresholds outlined in **Table 1** (note that continuous variables should be interpreted with caution based on the limits of quantification, LOQs). The sample-level (*c_any_specimen_b*) was correspondingly scored as positive (1), negative (0), and canceled (3) (**Table 2**). Class-level groupings by analyte screening tests and analyte confirmatory tests are shown in **Table 3**.

<details>
  <summary>Table 1. Blood Assay Thresholds PEth</summary>
  <table class="docutils">
  <br>
    <thead>
      <tr>
        <th>Analyte</th>
        <th>LOD (ng/mL)</th>
        <th>LOQ (ng/mL)</th>
        <th>Cutoff (ng/mL)</th>
        <th>Detection Window</th>
      </tr>
    </thead>
    <tbody>
		<td>Phosphatidylethanol</td>
		<td>4</td>
		<td>8</td>
		<td>20</td>
		<td>2-4 weeks</td>
	</tr>
</tbody>
</table>
</details>

<details>
  <summary>Table 2. Sample-Data Dictionary for Blood PEth</summary>
  <table class="docutils">
  <br>
    <thead>
      <tr>
        <th>Variable</th>
        <th>Description</th>
        <th>Form</th>
        <th>Options</th>
      </tr>
    </thead>
    <tbody>
	<tr>
		<td>Specimen_ID</td>
		<td>Specimen ID</td>
		<td>String</td>
		<td>String</td>
	</tr>
	<tr>
		<td>PSCID</td>
		<td>Participant ID</td>
		<td>String</td>
		<td>String</td>
	</tr>
	<tr>
		<td>Visit_time_point</td>
		<td>Visit time point</td>
		<td>Categorical</td>
		<td>1: visit 1<br />2: visit 2</td>
	</tr>
	<tr>
		<td>c_ethanol_b</td>
		<td>Specimen level result<br />(direct confirmation)</td>
		<td>Categorical</td>
		<td>1: positive<br />0: negative<br />3: cancelled</td>
	</tr>
	<tr>
		<td>c_peth_b_cat</td>
		<td>Confirmatory only test in blood:<br />etoh metabolite<br />(categorical) (peth)</td>
		<td>Categorical</td>
		<td>1: positive<br />0: negative<br />3: cancelled</td>
	</tr>
	<tr>
		<td>c_peth_b</td>
		<td>Confirmatory test in blood:<br />etoh metabolite (peth)</td>
		<td>Continuous</td>
		<td>concentration value</td>
	</tr>
	<tr>
		<td>c_peth_unit_b</td>
		<td>Units</td>
		<td>String</td>
		<td>Units of measure</td>
	</tr>
</tbody>
</table>
</details>


<details>
  <summary>Table 3. Mapping from Class to Screeners and Confirmatory Tests for PEth</summary>
  <table class="docutils"><colgroup><col width="25%"/><col width="50%"/></colgroup>
  <br>
    <thead>
      <tr>
        <th>Class</th>
        <th>Confirmatory (only) Test</th>
      </tr>
    </thead>
    <tbody>
	<tr>
		<td>Ethanol (c_ethanol_b)</td>
		<td>20phsphtdetbsp (c_peth_b_cat)</td>
	</tr>
</tbody>
</table>
</details>


## Quality Control & Known Issues
QC procedures involved examining assay ranges and categorical versus continuous measures. No common issues were identified from QC. No potential issues were flagged by subject matter experts.
