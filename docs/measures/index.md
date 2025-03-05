# Data Measure Release Notes
The current release includes data from Visits 1, 2, and 3 (V01, V02, and V03). In this section we provide a brief overview of each data measure provided in the data release, including, where applicable, details of implementation and data collection, scoring procedures, quality control procedures, known issues, and references.
![](../images/timeline-img.png)
<p>
<div class="notification-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fa-regular fa-lightbulb"></i></span>
  <span class="text">Visit numbers are labeled as Visit X or V0X in the release notes (e.g., V01 = Visit 1)</span>
</div>
</p>

Below is a summary of measures included in Release 1.0. Note that the HBCD Data Release Docs only cover the measures currently available, with additional documentation to follow in future updates as additional measure data are released. For details on upcoming additions in Release 1.1, see [Pending & Upcoming Updates](../changelog/pending.md). Full study protocols are available on the [HBCD Study site](https://hbcdstudy.org/study-protocols/).

## File-Based Data
The data release includes raw (`rawdata/`) and processed "derivative" (`derivatives/`) data for MRI, MRS, EEG, and motion/accelerometry, formatted to adhere to the Brain Imaging Data Structure (BIDS) standard. See [Raw BIDS Data](../datacuration/rawbids.md) and [Derivatives](../datacuration/derivatives.md) under the [HBCD BIDS Data](../datacuration/overview.md) section of the Release Notes for details.

## Tabulated Data
The data provided within the `phenotype/` folder includes demographic, toxicology, behavior, and tabulated data associated with magnetic resonance imaging (MRI), spectroscopy (MRS), electroencephalography (EEG), and motion/accelerometry (i.e. [wearable sensor](sensors.md) recordings for leg motion) - see [Phenotype BIDS Data](../datacuration/phenotypes.md) under the [HBCD BIDS Data](../datacuration/overview.md) section of the Release Notes for details. 

<button id="toggle-all-btn">Expand All Sections ↕️</button>


<div id="behCGinteraction" class="table-banner" onclick="toggleCollapse(this)">
  <span class="table-text">Behavior & Caregiver-Child Interaction</span>
  <span class="table-arrow">▸</span>
</div>
<div class="table-collapsible-content">
<table style="width: 100%; border-collapse: collapse; table-layout: fixed; font-size: 14px;">
  <thead>
  </tr>
  <tr>
    <tr>
      <th style="width: 40%; border: 1px solid #ddd; padding: 6px; text-align: center; font-size: 12px;">Name of Instrument</th>
      <th style="width: 15%; border: 1px solid #ddd; padding: 6px; text-align: center; font-size: 12px;">Acronym</th>
      <th style="width: 30%; border: 1px solid #ddd; padding: 6px; text-align: center; font-size: 12px;">Construct</th>
      <th style="width: 15%; border: 1px solid #ddd; padding: 6px; text-align: center; font-size: 12px;">Table Name</th>
    </tr>
  </thead>
  <tbody>
  <tr>
    <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;"><a href="../measures/behCGinteraction/#ecpromis-child-caregiver-interaction">Early Childhood Patient-Reported Outcome Measurement Information System Child/Caregiver Relationship Scale</a></td>
    <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">ecPROMIS</td>
    <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">Relationships</td>
    <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">mh_cg_pms__cc__inf</td>
  </tr>
  <tr>
    <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;"><a href="../measures/behCGinteraction/#ibq-r-very-short-form-behavioral-inhibition">Infant Behavior Questionnaire &ndash; Revised Very Short Form + Behavior Inhibition</a></td>
    <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">IBQ-R (VSF)+BI</td>
    <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">Temperamental Surgency/Extraversion, Negative Affectivity, Effortful Control, and Behavioral Inhibition</td>
    <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">mh_cg_ibqr</td>
  </tr>
  <tr>
    <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;"><a href="../measures/behCGinteraction/#maps-tl">Multidimensional Assessment Profiles - Temper Loss scale</a></td>
    <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">MAPS-TL</td>
    <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">Irritability</td>
    <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">mh_cg_mapdb__inf</td>
  </tr>
  </tbody>
  </table>
</div>

<div id="biospec" class="table-banner" onclick="toggleCollapse(this)">
  <span class="table-text">Biospecimen & Omics</span>
  <span class="table-arrow">▸</span>
</div>
<div class="table-collapsible-content">
  <table style="width: 100%; border-collapse: collapse; table-layout: fixed; font-size: 14px;">
  <thead>
  <tr>
    <th style="width: 40%; border: 1px solid #ddd; padding: 6px; text-align: center; font-size: 12px;">Name of Instrument</th>
    <th style="width: 15%; border: 1px solid #ddd; padding: 6px; text-align: center; font-size: 12px;">Acronym</th>
    <th style="width: 30%; border: 1px solid #ddd; padding: 6px; text-align: center; font-size: 12px;">Construct</th>
    <th style="width: 15%; border: 1px solid #ddd; padding: 6px; text-align: center; font-size: 12px;">Table Name</th>
  </tr>
  </thead>
  <tbody>
    <tr>
    <td style="border: 1px solid #ddd; padding: 8px; text-align: left;"><a href="../measures/biospec/#nails">Nails Toxicology Screen</a></td>
    <td style="border: 1px solid #ddd; padding: 8px; text-align: left;">Nails</td>
    <td style="border: 1px solid #ddd; padding: 8px; text-align: left;">Toxicology Screen</td>
    <td style="border: 1px solid #ddd; padding: 8px; text-align: left;">bio_biosample_nails</td>
  </tr>
  <tr>
      <td style="border: 1px solid #ddd; padding: 8px; text-align: left;"><a href="../measures/biospec/#urine">Urine Toxicology Screen</a></td>
      <td style="border: 1px solid #ddd; padding: 8px; text-align: left;">Urine</td>
      <td style="border: 1px solid #ddd; padding: 8px; text-align: left;">Toxicology Screen</td>
      <td style="border: 1px solid #ddd; padding: 8px; text-align: left;">bio_biosample_urine</td>
  </tr>
  </tbody>
  </table>
</div>

<div id="demographics" class="table-banner" onclick="toggleCollapse(this)">
  <span class="table-text">Demographics</span>
  <span class="table-arrow">▸</span>
</div>
<div class="table-collapsible-content">
<table style="width: 100%; border-collapse: collapse; table-layout: fixed; font-size: 14px;">
  <thead>
  </tr>
  <tr>
    <tr>
      <th style="width: 10%; border: 1px solid #ddd; padding: 6px; text-align: center; font-size: 12px;">Name of Instrument</th>
      <th style="width: 10%; border: 1px solid #ddd; padding: 6px; text-align: center; font-size: 12px;">Acronym</th>
      <th style="width: 30%; border: 1px solid #ddd; padding: 6px; text-align: center; font-size: 12px;">Construct</th>
      <th style="width: 15%; border: 1px solid #ddd; padding: 6px; text-align: center; font-size: 12px;">Table Name</th>
    </tr>
  </thead>
  <tbody>
  <tr>
      <td style="border: 1px solid #ddd; padding: 8px; text-align: left;"><a href="../measures/demographics">HBCD Demographics V01</a></td>
      <td style="border: 1px solid #ddd; padding: 8px; text-align: left;">Demographics</td>
      <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">Basic social characteristics related to the birthing parent, the other biological parent, and their household</td>
      <td style="border: 1px solid #ddd; padding: 8px; text-align: left;">sed_basic_demographics</td>
  </tr>
  </tbody>
  </table>
</div>

<div id="neurocog" class="table-banner" onclick="toggleCollapse(this)">
  <span class="table-text">Neurocognition & Language</span>
  <span class="table-arrow">▸</span>
</div>
<div class="table-collapsible-content">
<table style="width: 100%; border-collapse: collapse; table-layout: fixed; font-size: 14px;">
  <thead>
  </tr>
  <tr>
    <tr>
      <th style="width: 40%; border: 1px solid #ddd; padding: 6px; text-align: center; font-size: 12px;">Name of Instrument</th>
      <th style="width: 15%; border: 1px solid #ddd; padding: 6px; text-align: center; font-size: 12px;">Acronym</th>
      <th style="width: 30%; border: 1px solid #ddd; padding: 6px; text-align: center; font-size: 12px;">Construct</th>
      <th style="width: 15%; border: 1px solid #ddd; padding: 6px; text-align: center; font-size: 12px;">Table Name</th>
    </tr>
  </thead>
  <tbody>
  <tr>
      <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;"><a href="../measures/neurocog/#mlds">Multilingual Language Development Screener</a></td>
      <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">MLDS</td>
      <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">Multilingual exposure</td>
      <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">ncl_ch_mlds</td>
  </tr>
  <tr>
      <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;"><a href="../measures/neurocog/#spm-2">Sensory Processing Measure – Infant/Toddler</a></td>
      <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">SPM-2</td>
      <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">Sensory processing</td>
      <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">ncl_cg_spm2__inf</td>
  </tr>
  </tbody>
  </table>
</div>

<div id="sensors" class="table-banner" onclick="toggleCollapse(this)">
  <span class="table-text">Novel Technologies & Wearable Sensors</span>
  <span class="table-arrow">▸</span>
</div>
<div class="table-collapsible-content">
  <table style="width: 100%; border-collapse: collapse; table-layout: fixed; font-size: 14px;">
    <thead>
    </tr>
    <tr>
      <tr>
        <th style="width: 40%; border: 1px solid #ddd; padding: 6px; text-align: center; font-size: 12px;">Name of Instrument</th>
        <th style="width: 15%; border: 1px solid #ddd; padding: 6px; text-align: center; font-size: 12px;">Acronym</th>
        <th style="width: 30%; border: 1px solid #ddd; padding: 6px; text-align: center; font-size: 12px;">Construct</th>
        <th style="width: 15%; border: 1px solid #ddd; padding: 6px; text-align: center; font-size: 12px;">Table Name</th>
      </tr>
    </thead>
    <tbody>
  <tr>
    <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;"><a href="../measures/sensors/#wearable-sensors">Wearable Sensors</a></td>
    <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">Channel setup</td>
    <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">N/A</td>
    <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">sens_ch_setup</td>
  </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;"><a href="../measures/sensors/#infant-sensor-questionnaire">Infant Sensor Questionnaire</a></td>
      <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">N/A</td>
      <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">Motor behavior, physical activity, sleep</td>
      <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">nt_ch_sens__qtn_1</td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;"><a href="../measures/sensors/#infant-sensor-questionnaire">Infant Sensor Questionnaire</a></td>
      <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">N/A</td>
      <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">Motor behavior, physical activity, sleep</td>
      <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">nt_ch_sens__qtn_2</td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;"><a href="../measures/sensors/#infant-sensor-questionnaire">Infant Sensor Questionnaire</a></td>
      <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">N/A</td>
      <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">Motor behavior, physical activity, sleep</td>
      <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">nt_ch_sens__qtn_3</td>
    </tr>  
    </tbody>
    </table>
</div>

<div id="physicalhealth" class="table-banner" onclick="toggleCollapse(this)">
  <span class="table-text">Physical Health</span>
  <span class="table-arrow">▸</span>
</div>
<div class="table-collapsible-content">
<table style="width: 100%; border-collapse: collapse; table-layout: fixed; font-size: 14px;">
  <thead>
  </tr>
  <tr>
    <tr>
      <th style="width: 30%; border: 1px solid #ddd; padding: 6px; text-align: center; font-size: 12px;">Name of Instrument</th>
      <th style="width: 15%; border: 1px solid #ddd; padding: 6px; text-align: center; font-size: 12px;">Acronym</th>
      <th style="width: 30%; border: 1px solid #ddd; padding: 6px; text-align: center; font-size: 12px;">Construct</th>
      <th style="width: 15%; border: 1px solid #ddd; padding: 6px; text-align: center; font-size: 12px;">Table Name</th>
    </tr>
  </thead>
  <tbody>
  <tr>
    <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;"><a href="../measures/physicalhealth/#breastfeeding">Breast Feeding History</a></td>
    <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">PHENX BF</td>
    <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">Nutrition</td>
    <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">ph_cg_phx__bfh</td>
  </tr>
  <tr>
    <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;"><a href="../measures/physicalhealth/#food-insecurity">2-item Food Insecurity</a></td>
    <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">USDA short form</td>
    <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">Food insecurity</td>
    <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">sed_cg_foodins</td>
  </tr>
  <tr>
    <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;"><a href="../measures/physicalhealth/#growth">Height/Weight/Head Circumference</a></td>
    <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">Growth</td>
    <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">Growth</td>
    <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">ph_ch_anthro</td>
  </tr>  
  </tbody>
  </table>
</div>

<div id="pregexp" class="table-banner" onclick="toggleCollapse(this)">
  <span class="table-text">Pregnancy & Exposure, Including Substance Use</span>
  <span class="table-arrow">▸</span>
</div>
<div class="table-collapsible-content">
<p style="margin-bottom: 0; padding-bottom: 0; font-size: 1em">
  <a href="pregexp/preghealth" style="color: #00008B; text-decoration: none;">&nbsp; Pregnancy & Infant Health</a>
</p>
<table style="width: 100%; border-collapse: collapse; table-layout: fixed; font-size: 14px;">
  <thead>
  </tr>
  <tr>
    <tr>
      <th style="width: 30%; border: 1px solid #ddd; padding: 6px; text-align: center; font-size: 12px;">Name of Instrument</th>
      <th style="width: 10%; border: 1px solid #ddd; padding: 6px; text-align: center; font-size: 12px;">Acronym</th>
      <th style="width: 30%; border: 1px solid #ddd; padding: 6px; text-align: center; font-size: 12px;">Construct</th>
      <th style="width: 15%; border: 1px solid #ddd; padding: 6px; text-align: center; font-size: 12px;">Table Name</th>
    </tr>
  </thead>
  <tbody>
   <tr>
      <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;"><a href="../measures/pregexp/preghealth#instrument-details">Pregnancy Health</a></td>
      <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">Healthhx</td>
      <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">Pre-pregnancy and pregnancy health</td>
      <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">pex_bm_health_preg__healthhx</td>
    </tr>          
    <tr>
    <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;"><a href="../measures/pregexp/preghealth#instrument-details">Pregnancy Health-Exposures and Vaccines</a></td>
    <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">Vacc</td>
    <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">Vaccines in pregnancy</td>
    <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">pex_bm_health_preg__exp__vacc</td>
  </tr>    
  <tr>
    <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;"><a href="../measures/pregexp/preghealth#instrument-details">Pregnancy Health-Chronic Conditions</a></td>
    <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">Exp I chroncond</td>
    <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">Chronic conditions and sexually transmitted infections in pregnancy</td>
    <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">pex_bm_health_preg__chroncond</td>
  </tr>  
  <tr>
    <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;"><a href="../measures/pregexp/preghealth#instrument-details">Pregnancy Health-Illness</a></td>
    <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">Exp I illness</td>
    <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">Illness in pregnancy</td>
    <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">pex_bm_health_preg__illness</td>
  </tr>     
  <tr>
    <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;"><a href="../measures/pregexp/preghealth#instrument-details">Pregnancy Health-ER/Hospitalizations</a></td>
    <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">Exp I ERhosp</td>
    <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">ER visit or hospitalization in pregnancy</td>
    <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">pex_bm_health_preg__erhosp</td>
  </tr>  
  <tr>
    <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;"><a href="../measures/pregexp/preghealth#instrument-details">Pregnancy Health-Medications</a></td>
    <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">Exp I Meds</td>
    <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">Prescription and over the counter medications in pregnancy</td>
    <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">pex_bm_health_preg__meds</td>
  </tr>  
  <tr>
    <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;"><a href="../measures/pregexp/preghealth#instrument-details">Pregnancy Health-V2 (End of Pregnancy)</a></td>
    <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">Healthv2 Preg</td>
    <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">Updates information between enrollment and delivery</td>
    <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">pex_bm_healthv2_preg</td>
  </tr>     
  <tr>
    <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;"><a href="../measures/pregexp/preghealth#instrument-details">Infant health- V2</a></td>
    <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">Healthv2 Inf</td>
    <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">Delivery and birth outcomes</td>
    <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">pex_bm_healthv2_inf</td>
  </tr>    
</tbody>
</table>

<p style="margin-bottom: 0; padding-bottom: 0; font-size: 1em">
  <a href="pregexp/substanceuse" style="color: #00008B; text-decoration: none;">&nbsp; Substance Use</a>
</p>
<table style="width: 100%; border-collapse: collapse; table-layout: fixed; font-size: 14px;">
  <thead>
  </tr>
  <tr>
    <tr>
      <th style="width: 30%; border: 1px solid #ddd; padding: 6px; text-align: center; font-size: 12px;">Name of Instrument</th>
      <th style="width: 10%; border: 1px solid #ddd; padding: 6px; text-align: center; font-size: 12px;">Acronym</th>
      <th style="width: 30%; border: 1px solid #ddd; padding: 6px; text-align: center; font-size: 12px;">Construct</th>
      <th style="width: 15%; border: 1px solid #ddd; padding: 6px; text-align: center; font-size: 12px;">Table Name</th>
    </tr>
  </thead>
  <tbody>
  <tr>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;"><a href="../measures/pregexp/substanceuse/#assist-v1v2v3">Alcohol, Smoking and Substance Involvement Screening Test V1.0</a></td>
        <td>Assist V1</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">Substance use and problematic use before and during pregnancy</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">pex_bm_assistv1</td>
    </tr>    
    <tr>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;"><a href="../measures/pregexp/substanceuse/#assist-v1v2v3">Alcohol, Smoking and Substance Involvement Screening Test V2.0</a></td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">Assist V2</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">Substance use during end of pregnancy ( between V1 and delivery) and postnatal (weeks 0-4, between delivery and V2)</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">pex_bm_assistv2</td>
    </tr>    
    <tr>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;"><a href="../measures/pregexp/substanceuse/#assist-v1v2v3">Alcohol, Smoking and Substance Involvement Screening Test V3.0</a></td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">Assist V3</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">Substance use after pregnancy</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">pex_bm_assistv3</td>
    </tr>   
    <tr>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;"><a href="../measures/pregexp/substanceuse/#tlfb">Timeline Follow Back</a></td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">TLFB</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">Substance use before and during pregnancy</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">pex_ch_tlfb</td>
    </tr>   
  </tbody>
  </table>

<p style="margin-bottom: 0; padding-bottom: 0; font-size: 1em">
  <a href="pregexp/mentalhealth" style="color: #00008B; text-decoration: none;">&nbsp; Mental Health</a>
</p>
<table style="width: 100%; border-collapse: collapse; table-layout: fixed; font-size: 14px;">
  <thead>
  </tr>
  <tr>
    <tr>
      <th style="width: 30%; border: 1px solid #ddd; padding: 6px; text-align: center; font-size: 12px;">Name of Instrument</th>
      <th style="width: 10%; border: 1px solid #ddd; padding: 6px; text-align: center; font-size: 12px;">Acronym</th>
      <th style="width: 30%; border: 1px solid #ddd; padding: 6px; text-align: center; font-size: 12px;">Construct</th>
      <th style="width: 15%; border: 1px solid #ddd; padding: 6px; text-align: center; font-size: 12px;">Table Name</th>
    </tr>
  </thead>
  <tbody>
  <tr>
    <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;"><a href="../measures/pregexp/mentalhealth/#personal-family-psychiatric-history">Personal and family psychiatric history</a></td>
    <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">FAM MH</td>
    <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">Personal and family mental health</td>
    <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">pex_bm_psych</td>
  </tr>            
  <tr>
    <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;"><a href="../measures/pregexp/mentalhealth/#apa-12">DSM-5 Self-Rated Level 1 and Level 2 (version 8a) Cross-Cutting Symptom Measure—Adult</a></td>
    <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">APA 1/2</td>
    <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">Mental Health</td>
    <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">pex_bm_apa</td>
  </tr>  
  <tr>
    <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;"><a href="../measures/pregexp/mentalhealth/#dsm5-ptsdacute-stress-short-scale">National Stressful Events Survey- PTSD Short Scale/Acute Stress Disorder</a></td>
    <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">NSESSS—PTSD/Acute Stress Disorder</td>
    <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">PTSD/acute stress disorder symptom severity</td>
    <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">pex_bm_str__ptsd</td>
  </tr>      
  <tr>
    <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;"><a href="../measures/pregexp/mentalhealth/#epds">Edinburgh Postnatal Depression Scale</a></td>
    <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">EPDS</td>
    <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">Postnatal depression</td>
    <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">pex_bm_epds</td>
  </tr>      
</tbody>
</table>
</div>

<div id="socenvdet" class="table-banner" onclick="toggleCollapse(this)">
  <span class="table-text">Social & Environmental Determinants</span>
  <span class="table-arrow">▸</span>
</div>
<div class="table-collapsible-content">
<table style="width: 100%; border-collapse: collapse; table-layout: fixed; font-size: 14px;">
  <thead>
  </tr>
  <tr>
    <tr>
      <th style="width: 10%; border: 1px solid #ddd; padding: 6px; text-align: center; font-size: 12px;">Name of Instrument</th>
      <th style="width: 10%; border: 1px solid #ddd; padding: 6px; text-align: center; font-size: 12px;">Acronym</th>
      <th style="width: 30%; border: 1px solid #ddd; padding: 6px; text-align: center; font-size: 12px;">Construct</th>
      <th style="width: 15%; border: 1px solid #ddd; padding: 6px; text-align: center; font-size: 12px;">Table Name</th>
    </tr>
  </thead>
  <tbody>
</tr>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;"><a href="../measures/socenvdet/#babys-first-years">Baby’s First Years – Benefits/Services/Economic Stress</a></td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">BFY</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">Benefits/Services/Economic Stress</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">sed_bm_bfy</td>
    </tr>
    <tr>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;"><a href="../measures/socenvdet/#discrimination">PhenX+ Toolkit Discrimination</a></td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">PhenX+ Discrimination</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">Discrimination</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">sed_bm_phx__discr</td>
    </tr>   
    <tr>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;"><a href="../measures/socenvdet/#ehits">Extended – Hurt, Insult, Threaten, Scream</a></td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">eHITS</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">Intimate Partner Violence</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">sed_bm_ehits</td>
    </tr>        
    <tr>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;"><a href="../measures/socenvdet/#neighborhood-safety">PhenX+ Toolkit Neighborhood Safety</a></td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">Neighborhood Safety</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">Social Determinants of Health</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">sed_bm_nbhsaf</td>
    </tr>          
    <tr>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;"><a href="../measures/socenvdet/#paces">Protective and Compensatory Experience</a></td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">PACES</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">Protective Factors</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">sed_bm_paces</td>
    </tr>   
    <tr>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;"><a href="../measures/socenvdet/#perceived-stresssocial-support">Patient-Reported Outcome Measurement Information System</a></td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">PROMIS</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">Perceived Stress/Social Support</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">sed_bm_strsup</td>
    </tr>   
</tbody>
</table>
</div>

<div id="eeg" class="table-banner" onclick="toggleCollapse(this)">
  <span class="table-text">EEG</span>
  <span class="table-arrow">▸</span>
</div>
<div class="table-collapsible-content">
<table style="width: 100%; border-collapse: collapse; table-layout: fixed; font-size: 14px;">
  <thead>
  </tr>
  <tr>
    <tr>
      <th style="width: 30%; border: 1px solid #ddd; padding: 6px; text-align: center; font-size: 12px;">Name of Instrument</th>
      <th style="width: 10%; border: 1px solid #ddd; padding: 6px; text-align: center; font-size: 12px;">Acronym</th>
      <th style="width: 15%; border: 1px solid #ddd; padding: 6px; text-align: center; font-size: 12px;">Table Name(s)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
    <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;"><a href="../measures/eeg/#faces-task">Faces Task</a></td>
    <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">Face</td>
    <td colspan="2" rowspan="1" style="word-wrap: break-word; white-space: normal;">eeg_made_task-FACE_acq-eeg_MADE_preprocessing_report<br>eeg_qc_task-FACE</td>
  </tr>
  <tr>
    <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;"><a href="../measures/eeg/#auditory-mismatch-negativity-task-mmn">Auditory Mismatch Negativity Task</a></td>
    <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">MMN</td>
    <td colspan="2" rowspan="1" style="word-wrap: break-word; white-space: normal;">eeg_made_task-MMN_acq-eeg_MADE_preprocessing_report<br>eeg_qc_task-MMN</td>
  </tr>
  <tr>
    <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;"><a href="../measures/eeg/#video-resting-state-rs">Video Resting State Task</a></td>
    <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">RS</td>
    <td colspan="2" rowspan="1" style="word-wrap: break-word; white-space: normal;">eeg_made_task-RS_acq-eeg_MADE_preprocessing_report<br>eeg_qc_task-RS</td>
  </tr>
  <tr>
    <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;"><a href="../measures/eeg/#visual-evoked-potential-task-vep">Visual Evoked Potential Task</a></td>
    <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">VEP</td>
    <td colspan="2" rowspan="1" style="word-wrap: break-word; white-space: normal;">eeg_made_task-RS_acq-eeg_VEP_preprocessing_report<br>eeg_qc_task-VEP<br>eeg_made_task-VEP_ERP-summaryStats</td>
  </tr>
  <tr>
</tbody>
</table>
</div>

<div id="mri" class="table-banner" onclick="toggleCollapse(this)">
  <span class="table-text">MRI & MRS</span>
  <span class="table-arrow">▸</span>
</div>
<div class="table-collapsible-content">
<table style="width: 100%; border-collapse: collapse; table-layout: fixed; font-size: 14px;">
<tfoot><tr>
<td colspan="3" style="word-wrap: break-word; white-space: normal;">
    <li><b class="blue-text">&lt;SEG&gt;</b> label: 4S1056Parcels, 4S156Parcels, 4S256Parcels, 4S356Parcels, 4S456Parcels, 4S556Parcels, 4S656Parcels, 4S756Parcels, 4S856Parcels, 4S956Parcels, HCP, Glasser, Gordon, MIDB, MyersLabonte, Tian</li>
    <br>
    <li><b class="blue-text">&lt;PROC&gt;</b> labels: HERCULES_diff1, HERCULES_diff2, HERCULES_sum, unedited_A</li>
</td></tr>
</tfoot>
  <thead>
  </tr>
  <tr>
    <tr>
      <th style="width: 30%; border: 1px solid #ddd; padding: 6px; text-align: center; font-size: 12px;">Name of Instrument</th>
      <th style="width: 10%; border: 1px solid #ddd; padding: 6px; text-align: center; font-size: 12px;">Acronym</th>
      <th style="width: 15%; border: 1px solid #ddd; padding: 6px; text-align: center; font-size: 12px;">Table Name(s)</th>
    </tr>
  </thead>
  <tbody>
  <tr>
    <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;"><a href="../measures/mri/smri">Structural MRI</a></td>
    <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">sMRI</td>
    <td colspan="2" rowspan="1" style="word-wrap: break-word; white-space: normal;">
    img_brainswipes_xcpd-T1w<br>img_brainswipes_xcpd-T2w<br>img_mriqc_T1w<br>img_mriqc_T2w<br>
    img_bibsnet_space-T1w_desc-aseg_volumes<br>
    img_bibsnet_space-T2w_desc-aseg_volumes<br>
    </td>
  </tr>
  <tr>
    <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;"><a href="../measures/mri/fmri">Functional MRI</a></td>
    <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">fMRI</td>
    <td colspan="2" rowspan="1" style="word-wrap: break-word; white-space: normal;">img_brainswipes_xcpd-bold<br>img_mriqc_bold<br>
    <li>img_xcpd_space-fsLR_seg-<span class="blue-text">&lt;SEG&gt;</span>_stat-alff_bold  </li>
    <li>img_xcpd_space-fsLR_seg-<span class="blue-text">&lt;SEG&gt;</span>_stat-coverage_bold  </li>
    <li>img_xcpd_space-fsLR_seg-<span class="blue-text">&lt;SEG&gt;</span>_stat-mean_desc-curv_morph  </li>
    <li>img_xcpd_space-fsLR_seg-<span class="blue-text">&lt;SEG&gt;</span>_stat-mean_desc-sulc_morph  </li>
    <li>img_xcpd_space-fsLR_seg-<span class="blue-text">&lt;SEG&gt;</span>_stat-mean_desc-thickness_morph  </li>
    <li>img_xcpd_space-fsLR_seg-<span class="blue-text">&lt;SEG&gt;</span>_stat-reho_bold  </li></td>
  </tr>
  <tr>
    <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;"><a href="../measures/mri/dmri">Diffusion MRI</a></td>
    <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">dMRI</td>
    <td>img_brainswipes_qsiprep-dwi</td>
  </tr>
    <tr>
    <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;"><a href="../measures/mri/qmri">Quantitative MRI</a></td>
    <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">qMRI</td>
    <td>N/A</td>
  </tr>
  <tr>
    <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;"><a href="../measures/mri/mrs">Magnetic Resonance Spectroscopy</a></td>
    <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">MRS</td>
    <td colspan="2" rowspan="1" style="word-wrap: break-word; white-space: normal;">
      <li>img_osprey_<span class="blue-text">&lt;PROC&gt;</span>_AlphaCorrWaterScaledGroupNormed_Voxel_1_Basis_1  </li>
      <li>img_osprey_<span class="blue-text">&lt;PROC&gt;</span>_AlphaCorrWaterScaled_Voxel_1_Basis_1</li>
      <li>img_osprey_<span class="blue-text">&lt;PROC&gt;</span>_CSFWaterScaled_Voxel_1_Basis_1</li>
      <li>img_osprey_<span class="blue-text">&lt;PROC&gt;</span>_TissCorrWaterScaled_Voxel_1_Basis_1</li>
      <li>img_osprey_<span class="blue-text">&lt;PROC&gt;</span>_rawWaterScaled_Voxel_1_Basis_1</li>
      <li>img_osprey_<span class="blue-text">&lt;PROC&gt;</span>_amplMets_Voxel_1_Basis_1  </li>
      <li>img_osprey_<span class="blue-text">&lt;PROC&gt;</span>_tCr_Voxel_1_Basis_1  </li>
      <li>img_osprey_HERCULES_qm_processed_spectra</li>
      <li>img_osprey_unedited_qm_processed_spectra</li></td>
  </tr>
</tbody>
</table>
</div>
<br>