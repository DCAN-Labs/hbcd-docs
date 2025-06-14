# Reproschema

## Quick Start Guide for Researchers
In the HBCD Study, researchers collect data using REDCap, a web application for managing surveys and databases. To share and analyze this data, they convert it into the LORIS data dictionary format used for data releases. ReproSchema enables standardized and accurate transformation from REDCap to LORIS, ensuring questionnaire consistency and preserving data integrity across platforms and study phases.

### Accessing and Using Questionnaires
After obtaining access to the data (see instructions [here](), researchers can easily access and compare questionnaires from the HBCD study by following these steps:

 - Each questionnaire includes a JSON file detailing its metadata, including version history.​ The metadata includes change logs detailing any modifications between versions.​
 - TO DO

## Tracking Change 
Need help? Open an issue on [GitHub](https://github.com/ReproNim/hbcd-loris2reproschema)


# BLOOD
## Implementation & Data Collection
The current data release includes the following toxicology screens collected from the pregnant/postpartum person (estimated time of completion 5 minutes per screen). Additional information is as follows:

<table style="width: 100%; border-collapse: collapse; table-layout: fixed;">
  <thead>
    <tr>
      <th style="border: 1px solid #ddd; padding: 8px; text-align: left;">Screen</th>
      <th style="border: 1px solid #ddd; padding: 8px; text-align: left;">Administration Method</th>
      <th style="border: 1px solid #ddd; padding: 8px; text-align: left;">Visits</th>      
    </tr>
  </thead>
<tbody>
<tr>
    <td style="border: 1px solid #ddd; padding: 8px; text-align: left;"><a href="#blood">Blood</a></td>
    <td style="border: 1px solid #ddd; padding: 8px; text-align: left;">Phlebotomist-collected venous blood, which is pipetted onto dried blood spot cards</td>
    <td style="border: 1px solid #ddd; padding: 8px; text-align: left;">V01</td>
</tr>
<tr>
    <td style="border: 1px solid #ddd; padding: 8px; text-align: left;"><a href="#nails">Nails</a></td>
    <td style="border: 1px solid #ddd; padding: 8px; text-align: left;">Self-collected under research team supervision, or collected by research team</td>
    <td style="border: 1px solid #ddd; padding: 8px; text-align: left;">V01, V02</td>
</tr>
<tr>
    <td style="border: 1px solid #ddd; padding: 8px; text-align: left;"><a href="#urine">Urine</a></td>
    <td style="border: 1px solid #ddd; padding: 8px; text-align: left;">Self-collected</td>
    <td style="border: 1px solid #ddd; padding: 8px; text-align: left;">V01</td>
</tr>
</tbody>
</table>

### BLOOD    
These data are the results of toxicology assays in dried blood spots collected at V1. Processing of Blood Spot Cards consists of preparing three 1/8” punches of dried blood spot followed by extraction using an organic solvent. Detection of PEth in the extract is accomplished with a single pass using LCMSMS (**Figure 1**):

**Figure 1. Blood Processing**
<img src="../../images/biospec/Fig1_blood.png" width="100%" height="auto">

<br>

<p>
<div id="notification-banner" class="notification-banner" onclick="toggleCollapse(this)">
  <span class="text">PEth Assay Details</span>
  <span class="notification-arrow">▸</span>
</div>
<div class="notification-collapsible-content">
<br>
<p>PEth assays are confirmation-only testing. Test results were determined to be positive (*c_peth_b_cat*), negative, or canceled according to the thresholds outlined in **Table 1** (note that continuous variables should be interpreted with caution based on the limits of quantification, LOQs). The sample-level (*c_any_specimen_b*) was correspondingly scored as positive (1), negative (0), and canceled (3) (**Table 2**). Class-level groupings by analyte screening tests and analyte confirmatory tests are shown in **Table 3**.</p>
<summary><strong>Table 1. Blood Assay Thresholds PEth</strong></summary>
  <table class="docutils">
  <br>
    <thead>
      <tr>
        <th>Analyte</th>
        <th> LOD <br>(ng/mL)</th>
        <th> LOQ <br>(ng/mL)</th>
        <th> Cutoff <br>(ng/mL)</th>
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
</p>
<p>
<summary><strong>Table 2. Sample-Data Dictionary for Blood PEth</strong></summary>
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
</p>
<p>
<summary><strong>Table 3. Mapping from Class to Screeners and Confirmatory Tests for PEth</strong></summary>
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
</p>
</div>
</p>