# Biospecimens & Omics

## Biospecimen Screens
The current data release includes the following Biospecimen toxicology screens:

<table style="width: 100%; border-collapse: collapse; table-layout: fixed;">
  <thead>
    <tr>
      <th style="border: 1px solid #ddd; padding: 8px; text-align: left;">Name of Measure</th>
      <th style="border: 1px solid #ddd; padding: 8px; text-align: left;">Short Name</th>
      <th style="border: 1px solid #ddd; padding: 8px; text-align: left;">Construct</th>
      <th style="border: 1px solid #ddd; padding: 8px; text-align: left;">Table Name</th>
    </tr>
  </thead>
<tbody>
  <tr>
    <td style="border: 1px solid #ddd; padding: 8px; text-align: left;"><a href="#nails">Maternal Nails</a></td>
    <td style="border: 1px solid #ddd; padding: 8px; text-align: left;">Nails</td>
    <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">Toxicology screen for substances & environmental exposures</td>
    <td style="border: 1px solid #ddd; padding: 8px; text-align: left;">bio_biosample_nails</td>
  </tr>
  <tr>
      <td style="border: 1px solid #ddd; padding: 8px; text-align: left;"><a href="#urine">Maternal Urine</a></td>
      <td style="border: 1px solid #ddd; padding: 8px; text-align: left;">Urine</td>
      <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">Toxicology screen for substances & environmental exposures</td>
      <td style="border: 1px solid #ddd; padding: 8px; text-align: left;">bio_biosample_urine</td>
  </tr>
</tbody>
</table>

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
    <td style="border: 1px solid #ddd; padding: 8px; text-align: left;"><a href="#nails">Maternal Nails</a></td>
    <td style="border: 1px solid #ddd; padding: 8px; text-align: left;">Self-collected under research team supervision, or collected by research team</td>
    <td style="border: 1px solid #ddd; padding: 8px; text-align: left;">V01, V02</td>
</tr>
<tr>
    <td style="border: 1px solid #ddd; padding: 8px; text-align: left;"><a href="#urine">Maternal Urine</a></td>
    <td style="border: 1px solid #ddd; padding: 8px; text-align: left;">Self-collected</td>
    <td style="border: 1px solid #ddd; padding: 8px; text-align: left;">V01</td>
</tr>
</tbody>
</table>

## Quality Control
QC procedures involved examining assay ranges and categorical versus continuous measures. No common issues were observed from QC.

## Instrument Details
<p>
<div id="biospec-warning" class="warning-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fas fa-exclamation-triangle"></i></span>
  <span class="text">Data Warning</span>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="collapsible-content">
<p>For all toxicology screens, continuous variables should be interpreted with cautiong based on the threshold limits of quantification (LOQs), or the cutoff concentration used to categorize metabolites as positive or negative. LOQs are provided in <a href="#nails-table1">Table 1. Nail Assay Thresholds</a> and <a href="#urine-table1">Table 1. Urine Assay Thresholds for Analytes</a>.</p> 
</div>
</p>

### NAILS
<p>
<div id="nails-warning" class="warning-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fas fa-exclamation-triangle"></i></span>
  <span class="text">Data Warning</span>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="collapsible-content">
<p>As of July 1, 2024, the nail processing workflow was updated to optimize specimen use and allow confirmation testing for low sample quantities. Prior to this update, remnants of ELISA extract were not used for confirmation when specimens had insufficient sample.</p> 
</div>
</p>

This dataset includes the results of toxicology assays conducted on fingernails and toenails. Specimens are sorted by weight, and those weighing at least 20 mg undergo ELISA screening, followed by LCMSMS confirmation for presumptive positives, each requiring an additional 20 mg. If insufficient specimen remains for LCMSMS, the remnant ELISA extract is used for confirmation.

<img src="../../images/biospec/Fig1_nails.png" width="100%" height="auto">


#### USDTL Assay Details
Based on the predefined threshold outlined in [Table 1](#nails-table1), a confirmatory test result for any substance analyte (e.g. *Amphetamine (c_amp_u)*) was determined to be positive, negative, or invalid (*QNS* i.e. *quantity not sufficient*) ([Table 2](#nails-table2)).

<p><b class="blue-text">LOD</b> / <b class="blue-text">LOQ</b> = limit of detection / quantification</p>

<div id="nails-table1" class="table-banner" onclick="toggleCollapse(this)">
  <span class="table-text">Table 1. Nail Assay Thresholds</span>
  <span class="table-arrow">▸</span>
</div>
<div class="table-collapsible-content">
<table style="width: 100%; border-collapse: collapse; table-layout: fixed;">
<thead>
    <tr>
    <th style="border: 1px solid #ddd; padding: 10px;">Analyte</th>
    <th style="border: 1px solid #ddd; padding: 10px;">LOD (pg/mL)</th>
    <th style="border: 1px solid #ddd; padding: 10px;">LOQ (pg/mL)</th>
    <th style="border: 1px solid #ddd; padding: 9px;">Cutoff (pg/mL)</th>
    <th style="border: 1px solid #ddd; padding: 10px; word-wrap: break-word; white-space: normal;">Detection Window (months)</th>
    </tr>
</thead>
<tbody>
    <tr>
        <td>Amphetamine</td>
        <td>20</td>
        <td>40</td>
        <td>100</td>
        <td>Finger 3-6; Toe 10-14</td>
    </tr>
    <tr>
        <td>Methamphetamine</td>
        <td>20</td>
        <td>40</td>
        <td>100</td>
        <td>Finger 3-6; Toe 10-14</td>
    </tr>
    <tr>
        <td>MDA</td>
        <td>20</td>
        <td>40</td>
        <td>100</td>
        <td>Finger 3-6; Toe 10-14</td>
    </tr>
    <tr>
        <td>MDMA</td>
        <td>20</td>
        <td>40</td>
        <td>100</td>
        <td>Finger 3-6; Toe 10-14</td>
    </tr>
    <tr>
        <td>MDEA</td>
        <td>20</td>
        <td>40</td>
        <td>100</td>
        <td>Finger 3-6; Toe 10-14</td>
    </tr>
    <tr>
        <td>Carboxy-delta-9-THC</td>
        <td>0.01</td>
        <td>0.02</td>
        <td>0.05</td>
        <td>Finger 3-6; Toe 10-14</td>
    </tr>
    <tr>
        <td>Cocaine</td>
        <td>20</td>
        <td>40</td>
        <td>100</td>
        <td>Finger 3-6; Toe 10-14</td>
    </tr>
    <tr>
        <td>Cocaethylene</td>
        <td>10</td>
        <td>20</td>
        <td>50</td>
        <td>Finger 3-6; Toe 10-14</td>
    </tr>
    <tr>
        <td>Benzoylecgonine</td>
        <td>10</td>
        <td>20</td>
        <td>50</td>
        <td>Finger 3-6; Toe 10-14</td>
    </tr>
    <tr>
        <td>Norcocaine</td>
        <td>10</td>
        <td>20</td>
        <td>50</td>
        <td>Finger 3-6; Toe 10-14</td>
    </tr>
    <tr>
        <td>6-MAM</td>
        <td>20</td>
        <td>40</td>
        <td>100</td>
        <td>Finger 3-6; Toe 10-14</td>
    </tr>
    <tr>
        <td>Codeine</td>
        <td>20</td>
        <td>40</td>
        <td>100</td>
        <td>Finger 3-6; Toe 10-14</td>
    </tr>
    <tr>
        <td>Hydrocodone</td>
        <td>20</td>
        <td>40</td>
        <td>100</td>
        <td>Finger 3-6; Toe 10-14</td>
    </tr>
    <tr>
        <td>Hydromorphone</td>
        <td>20</td>
        <td>40</td>
        <td>100</td>
        <td>Finger 3-6; Toe 10-14</td>
    </tr>
    <tr>
        <td>Morphine</td>
        <td>20</td>
        <td>40</td>
        <td>100</td>
        <td>Finger 3-6; Toe 10-14</td>
    </tr>
    <tr>
        <td>Norhydrocodone</td>
        <td>8</td>
        <td>16</td>
        <td>40</td>
        <td>Finger 3-6; Toe 10-14</td>
    </tr>
    <tr>
        <td>Oxycodone</td>
        <td>20</td>
        <td>40</td>
        <td>100</td>
        <td>Finger 3-6; Toe 10-14</td>
    </tr>
    <tr>
        <td>Oxymorphone</td>
        <td>20</td>
        <td>40</td>
        <td>100</td>
        <td>Finger 3-6; Toe 10-14</td>
    </tr>
    <tr>
        <td>Noroxycodone</td>
        <td>8</td>
        <td>16</td>
        <td>40</td>
        <td>Finger 3-6; Toe 10-14</td>
    </tr>
    <tr>
        <td>Methadone</td>
        <td>20</td>
        <td>40</td>
        <td>100</td>
        <td>Finger 3-6; Toe 10-14</td>
    </tr>
    <tr>
        <td>EDDP</td>
        <td>20</td>
        <td>40</td>
        <td>100</td>
        <td>Finger 3-6; Toe 10-14</td>
    </tr>
    <tr>
        <td>Amobarbital</td>
        <td>80</td>
        <td>80</td>
        <td>200</td>
        <td>Finger 3-6; Toe 10-14</td>
    </tr>
    <tr>
        <td>Butalbital</td>
        <td>80</td>
        <td>80</td>
        <td>200</td>
        <td>Finger 3-6; Toe 10-14</td>
    </tr>
    <tr>
        <td>Pentobarbital</td>
        <td>80</td>
        <td>80</td>
        <td>200</td>
        <td>Finger 3-6; Toe 10-14</td>
    </tr>
    <tr>
        <td>Phenobarbital</td>
        <td>80</td>
        <td>80</td>
        <td>200</td>
        <td>Finger 3-6; Toe 10-14</td>
    </tr>
    <tr>
        <td>Secobarbital</td>
        <td>80</td>
        <td>80</td>
        <td>200</td>
        <td>Finger 3-6; Toe 10-14</td>
    </tr>
    <tr>
        <td>Alprazolam</td>
        <td>20</td>
        <td>40</td>
        <td>100</td>
        <td>Finger 3-6; Toe 10-14</td>
    </tr>
    <tr>
        <td>Diazepam</td>
        <td>20</td>
        <td>40</td>
        <td>100</td>
        <td>Finger 3-6; Toe 10-14</td>
    </tr>
    <tr>
        <td>Midazolam</td>
        <td>20</td>
        <td>40</td>
        <td>100</td>
        <td>Finger 3-6; Toe 10-14</td>
    </tr>
    <tr>
        <td>Nordiazepam</td>
        <td>20</td>
        <td>40</td>
        <td>100</td>
        <td>Finger 3-6; Toe 10-14</td>
    </tr>
    <tr>
        <td>Oxazepam</td>
        <td>20</td>
        <td>40</td>
        <td>100</td>
        <td>Finger 3-6; Toe 10-14</td>
    </tr>
    <tr>
        <td>Temazepam</td>
        <td>20</td>
        <td>40</td>
        <td>100</td>
        <td>Finger 3-6; Toe 10-14</td>
    </tr>
    <tr>
        <td>Ketamine</td>
        <td>20</td>
        <td>40</td>
        <td>100</td>
        <td>Finger 3-6; Toe 10-14</td>
    </tr>
    <tr>
        <td>Norketamine</td>
        <td>20</td>
        <td>40</td>
        <td>100</td>
        <td>Finger 3-6; Toe 10-14</td>
    </tr>
    <tr>
        <td>Tramadol</td>
        <td>200</td>
        <td>400</td>
        <td>500</td>
        <td>Finger 3-6; Toe 10-14</td>
    </tr>
    <tr>
        <td>Fentanyl</td>
        <td>2</td>
        <td>4</td>
        <td>10</td>
        <td>Finger 3-6; Toe 10-14</td>
    </tr>
    <tr>
        <td>Norfentanyl</td>
        <td>2</td>
        <td>4</td>
        <td>10</td>
        <td>Finger 3-6; Toe 10-14</td>
    </tr>
    <tr>
        <td>Alfentanil</td>
        <td>2</td>
        <td>4</td>
        <td>10</td>
        <td>Finger 3-6; Toe 10-14</td>
    </tr>
    <tr>
        <td>Acetyl Fentanyl</td>
        <td>2</td>
        <td>4</td>
        <td>10</td>
        <td>Finger 3-6; Toe 10-14</td>
    </tr>
    <tr>
        <td>Acetyl Norfentanyl</td>
        <td>2</td>
        <td>4</td>
        <td>10</td>
        <td>Finger 3-6; Toe 10-14</td>
    </tr>
    <tr>
        <td>Sufentanil</td>
        <td>1</td>
        <td>2</td>
        <td>5</td>
        <td>Finger 3-6; Toe 10-14</td>
    </tr>
    <tr>
        <td>Norsufentanil</td>
        <td>2</td>
        <td>2</td>
        <td>5</td>
        <td>Finger 3-6; Toe 10-14</td>
    </tr>
    <tr>
        <td>Buprenorphine</td>
        <td>4</td>
        <td>8</td>
        <td>20</td>
        <td>Finger 3-6; Toe 10-14</td>
    </tr>
    <tr>
        <td>Norbuprenorphine</td>
        <td>4</td>
        <td>8</td>
        <td>20</td>
        <td>Finger 3-6; Toe 10-14</td>
    </tr>
    <tr>
        <td>Ethyl glucuronide</td>
        <td>4</td>
        <td>8</td>
        <td>20</td>
        <td>Finger 3; Toe no consensus</td>
    </tr>
    <tr>
        <td>Nicotine</td>
        <td>20</td>
        <td>40</td>
        <td>100</td>
        <td>Finger 3-6; Toe 10-14</td>
    </tr>
    <tr>
        <td>Cotinine</td>
        <td>20</td>
        <td>40</td>
        <td>100</td>
        <td>Finger 3-6; Toe 10-14</td>
    </tr>
</tbody>
</table>
</div>

<div id="nails-table2" class="table-banner" onclick="toggleCollapse(this)">
  <span class="table-text">Table 2. Sample-Data Dictionary Nail Assays</span>
  <span class="table-arrow">▸</span>
</div>
<div class="table-collapsible-content">
<table style="width: 100%; border-collapse: collapse; table-layout: fixed;">
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
        <td>Nail_weight</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">Weight of nails available to assay</td>
        <td>Continuous</td>
        <td>nail weight (grams)</td>
    </tr>
    <tr>
        <td>Nail_type</td>
        <td>Type of nails assayed</td>
        <td>Categorical</td>
        <td>1: fingernail<br />2: toenail<br />3: both<br />4: unknown</td>
    </tr>
    <tr>
        <td>test_ordered_n</td>
        <td>Test ordered</td>
        <td>Categorical</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">1: custom 14 panel test<br />2: Only enough to run EtG<br />3: Canceled because we could not run anything (no results generated)</td>
    </tr>
    <tr>
        <td>c_any_specimen_n</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">Specimen level result (positive for any analyte in confirmatory tests)</td>
        <td>Categorical</td>
        <td>1: positive<br />0: negative<br />3: QNS</td>
    </tr>
    <tr>
        <td>c_any_stim_n</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">Any stimulants in nails (based on confirmatory results for amphetamine, methamptheamine, MDM, MDA, MDEA)</td>
        <td>Categorical</td>
        <td>1: positive<br />0: negative<br />3: QNS</td>
    </tr>
    <tr>
        <td>s_amp_n</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">Screening test in nails: amphetamine/MDA dual test (amp/mamp)</td>
        <td>Categorical</td>
        <td>1: positive<br />0: negative<br />3: QNS</td>
    </tr>
    <tr>
        <td>s_mamp_n</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">Screening test in nails: methamphetamine/MDMA dual test (amp/mamp)</td>
        <td>Categorical</td>
        <td>1: positive<br />0: negative<br />3: QNS</td>
    </tr>
    <tr>
        <td>c_amp_n_cat</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">>Confirmatory test in nails: amphetamine (categorical) (amp/mamp)</td>
        <td>Categorical</td>
        <td>1: positive<br />0: negative<br />3: QNS<br />4: screen negative</td>
    </tr>
    <tr>
        <td>c_amp_n</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">Confirmatory test in nails: amphetamine (amp/mamp)</td>
        <td>Continuous</td>
        <td>concentration value -999</td>
    </tr>
</tbody>
</table>
</div>
</p>

Based on the confirmatory test (i.e. reflexes from positive screening test) result for any substance, the class-level (e.g. *c_nictotine_u*) and sample-level (e.g. *c_any_specimen_n*) are correspondingly scored as positive (1), negative (0), and invalid (3). If all classes are negative (0), then sample-levels are negative (0). All class-level groupings by analyte screening tests and analyte confirmatory tests are shown in [Table 3](#nails-table3).

<div id="nails-table3" class="table-banner" onclick="toggleCollapse(this)">
  <span class="table-text">Table 3. Mapping from Class to Screening Tests and Confirmatory Tests for Nails</span>
  <span class="table-arrow">▸</span>
</div>
<div class="table-collapsible-content">
<table class="docutils">
<thead>
<tr>
    <th>Class</th>
    <th>Screening test</th>
    <th>Confirmatory Test</th>      
</tr>
</thead>
<tbody>
<tr>
    <td colspan="1" rowspan="9" style="word-wrap: break-word; white-space: normal;">Stimulant (c_any_stim_n)</td>
    <td colspan="1" rowspan="5" style="word-wrap: break-word; white-space: normal;">amp/mamp (s_amp_n, s_mamp_n)</td>
    <td>Amphetamine (c_amp_n)</td>
</tr>
    <tr><td>Methamphetamine (c_meth_n)</td></tr>
    <tr><td>MDMA (c_mdma_n)</td></tr>
    <tr><td>MDA (c_mda_n)</td></tr>
    <tr><td>MDEA (c_mdea_n)</td></tr>
<tr>
    <td colspan="1" rowspan="4">coc (s_coc_n)</td>
    <td>Cocaine (c_coc_n)</td>
</tr>
    <tr><td>Cocaethylene (c_cocae_n)</td></tr>
    <tr><td>Benzoylecgonine (c_ben_n)</td></tr>
    <tr><td>Norcocaine (c_ncoc_n)</td></tr>
<tr>
    <td style="word-wrap: break-word; white-space: normal;">Cannabinoid (c_any_cannabinoid_n)</td>
    <td>thc (s_thc_n)</td>
    <td style="word-wrap: break-word; white-space: normal;">Carboxy-delta-9-THC (c_delta-9-THC_n)</td>
</tr>
<tr>
    <td colspan="1" rowspan="5">Barbiturate (c_any_barb_n)</td>
    <td colspan="1" rowspan="5">bar (s_bar_n)</td>
    <td>Amobarbital (c_amobarb_n)</td>
</tr>
    <tr><td>Secobarbital (c_secobarb_n)</td></tr>
    <tr><td>Pentobarbital (c_pentobarb_n)</td></tr>
    <tr><td>Phenobarbital (c_phenobarb_n)</td></tr>
    <tr><td>Butalbital (c_butalbital_n)</td>
</tr> 
<tr>
    <td colspan="1" rowspan="6" style="word-wrap: break-word; white-space: normal;">Benzodiazepine (c_any_benzo_n)</td>
    <td colspan="1" rowspan="6">benz (s_benz_n)</td>
    <td>Diazepam (c_diaz_n)</td></tr>
    <tr><td>Oxazepam (c_oxaz_n)</td></tr>
    <tr><td>Nordiazepam (c_nord_n)</td></tr>
    <tr><td>Temazepam (c_tema_n)</td></tr>
    <tr><td>Midazolam (c_mida_n)</td></tr>
    <tr><td>Alprazolam (c_alpa_n)</td>
</tr>
<tr>
    <td colspan="1" rowspan="21">Opioids (c_any_opioid_n)</td>
    <td colspan="1" rowspan="6">opi (s_opi_n)</td>
    <td>Codeine (c_cod_n)</td></tr>
    <tr><td>Morphine (c_mor_n)</td></tr>
    <tr><td>MAM (c_mam_n)</td></tr>
    <tr><td>Hydrocodone (c_hydroc_n)</td></tr>
    <tr><td>Norhydrocodone (c_norh_n)</td></tr>
    <tr><td>Hydromorphone (c_hydrom_n)</td>
</tr>
<tr>
    <td colspan="1" rowspan="2">mtd (s_mtd_n)</td>
    <td>Methadone (c_mtd_n)</td></tr>
    <tr><td>EDDP (c_eddp_n)</td>
</tr>
<tr>
    <td colspan="1" rowspan="3">oxyc (s_oxyc_n)</td>
    <td>Oxycodone (c_oxyc_n)</td></tr>
    <tr><td>Noroxycodone (c_noxyc_n)</td></tr>
    <tr><td>Oxymorphone (c_oxym_n)</td>
</tr>
<tr>    
    <td>tram (s_tram_n)</td>
    <td>Tramadol (c_tram_n)</td>
</tr>
<tr>
    <td colspan="1" rowspan="4">fent (s_fent_n)</td>
    <td>Fentanyl (c_fent_n)</td></tr>
    <tr><td>Norfentanyl (c_nfent_n)</td></tr>
    <tr><td>Acetylfentanyl (c_acfent_n)</td></tr>
    <tr><td>ActlNorfentanyl (c_acnfent_n)</td>
</tr>
<tr>
    <td colspan="1" rowspan="3">suf (s_suf_n)</td>
    <td>Alfentanil (c_afent_n)</td></tr>
    <tr><td>Sufentanil (c_suf_u)</td></tr>
    <tr><td>Norsufentanil (c_nsuf_n)</td>
</tr>
<tr>
    <td colspan="1" rowspan="2">bup (s_bup_n)</td>
    <td>Buprenorphine (c_bup_n)</td></tr>
    <tr><td>Norbuprenorpine (c_nbup_n)</td>
</tr>
<tr>
    <td colspan="1" rowspan="2" style="word-wrap: break-word; white-space: normal;">dissociative anesthetic (c_disanesth_n)</td>
    <td colspan="1" rowspan="2">ket (s_ket_n)</td>
    <td>Ketamine (c_ket_n)</td>
    </tr><tr><td>Norketamine (c_nket_n)</td>
</tr>
<tr>
    <td colspan="1" rowspan="2">Nicotine (c_nicotine_n)</td>
    <td colspan="1" rowspan="2">cot (s_cot_n)</td>
    <td>Nicotine (c_nic_n)</td></tr>
    <tr><td>Cotinine (c_cot_n)</td>
</tr>
<tr>
    <td>Ethanol (c_ethanol_n)</td>
    <td>&nbsp;</td>
    <td>ethyl glucuronide (c_etoh_n)</td>
</tr>
</tbody>
</table> 
</div>
</p>  


### URINE
<p>
<div id="urine-warning" class="warning-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fas fa-exclamation-triangle"></i></span>
  <span class="text">Data Warning</span>
  <span class="arrow">▸</span>
</div>
<div class="collapsible-content">
<p>Only the initial creatinine results from sample validation are included in the data release: creatinine and specific gravity values are therefore provided for researchers who wish to adjust for urinary concentration in continuous measures or apply different thresholds.</p> 
</div>
</p>

These data are the results of urine toxicology assays. Test results for substances were determined to be positive or negative based on predefined thresholds, or invalid (for specimens identified as dilute, substituted, adulterated, or otherwise insufficient based on validation).
<img src="../../images/biospec/Fig1_biospec_urine.png" width="90%" height="auto">

Validation is based on creatinine, pH, and nitrite measurements. Specimens with low creatinine (<20 mg/dL) are confirmed using specific gravity via refractometer (decision grid below), and the creatinine analysis is repeated to rule out issues with the first analysis (e.g. sample mix-ups, air bubble in a line on the instrument, etc.):
<img src="../../images/biospec/Table1_biospec_urine.png" width="90%" height="auto">

#### Assay Details
Based on predefined thresholds ([Table 1](#urine-table1)), a confirmatory test result for any substance analyte (e.g. *Amphetamine (c_amp_u)*) is determined to be positive, negative, or invalid ([Table 2](#urine-table2)). 

<p><b class="blue-text">LOD</b> / <b class="blue-text">LOQ</b> = limit of detection / quantification</p>

<div id="urine-table1" class="table-banner" onclick="toggleCollapse(this)">
  <span class="table-text">Table 1. Urine Assay Thresholds for Analytes</span>
  <span class="table-arrow">▸</span>
</div>
<div class="table-collapsible-content">
<table style="width: 100%; border-collapse: collapse; table-layout: fixed;">
<tfoot><tr><td colspan="5"><i><b>**</b> Based on DRI® Cotinine assay for the qualitative and semiquantitative determination of Cotinine</i></td></tr></tfoot>
<thead>
      <tr>
        <th style="border: 1px solid #ddd; padding: 8px; text-align: left;">Analyte</th>
        <th style="border: 1px solid #ddd; padding: 8px; text-align: left;">LOD (ng/mL)</th>
        <th style="border: 1px solid #ddd; padding: 8px; text-align: left;">LOQ (ng/mL)</th>
        <th style="border: 1px solid #ddd; padding: 8px; text-align: left;">Cutoff (ng/mL)</th>
        <th style="border: 1px solid #ddd; padding: 8px; text-align: left;">Detection Window</th>
      </tr>
</thead>
<tbody>
    <tr>
        <td>Amphetamine</td>
        <td>50</td>
        <td>100</td>
        <td>250</td>
        <td>2-3 days</td>
    </tr>
    <tr>
        <td>Methamphetamine</td>
        <td>50</td>
        <td>100</td>
        <td>250</td>
        <td>2-3 days</td>
    </tr>
    <tr>
        <td>MDA</td>
        <td>50</td>
        <td>100</td>
        <td>250</td>
        <td>2-3 days</td>
    </tr>
    <tr>
        <td>MDMA</td>
        <td>50</td>
        <td>100</td>
        <td>250</td>
        <td>2-3 days</td>
    </tr>
    <tr>
        <td>MDEA</td>
        <td>50</td>
        <td>100</td>
        <td>250</td>
        <td>2-3 days</td>
    </tr>
    <tr>
        <td>Carboxy-delta-9-THC</td>
        <td>3</td>
        <td>7.5</td>
        <td>15</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">2-5 days for casual use; 10-14 for chronic use</td>
    </tr>
    <tr>
        <td>Carboxy-delta-8-THC</td>
        <td>3</td>
        <td>7.5</td>
        <td>15</td>
        <td>No consensus</td>
    </tr>
    <tr>
        <td>Carboxy-cannabidiol</td>
        <td>10</td>
        <td>25</td>
        <td>50</td>
        <td>No consensus</td>
    </tr>
        <tr>
        <td>Cotinine<b>**</b></td>
        <td>34</td>
        <td>34</td>
        <td>500</td>
        <td>Up to 7 days</td>
    </tr>
    <tr>
        <td>Benzoylecgonine</td>
        <td>20</td>
        <td>50</td>
        <td>100</td>
        <td>2-3 days</td>
    </tr>
    <tr>
        <td>6-MAM</td>
        <td>2</td>
        <td>4</td>
        <td>10</td>
        <td>8 hours</td>
    </tr>
    <tr>
        <td>Codeine</td>
        <td>10</td>
        <td>50</td>
        <td>100</td>
        <td>2-3 days</td>
    </tr>
    <tr>
        <td>Hydrocodone</td>
        <td>10</td>
        <td>50</td>
        <td>100</td>
        <td>2-3 days</td>
    </tr>
    <tr>
        <td>Hydromorphone</td>
        <td>10</td>
        <td>50</td>
        <td>100</td>
        <td>2-3 days</td>
    </tr>
    <tr>
        <td>Morphine</td>
        <td>10</td>
        <td>50</td>
        <td>100</td>
        <td>2-3 days</td>
    </tr>
    <tr>
        <td>Oxycodone</td>
        <td>60</td>
        <td>120</td>
        <td>300</td>
        <td>2-3 days</td>
    </tr>
    <tr>
        <td>Oxymorphone</td>
        <td>60</td>
        <td>120</td>
        <td>300</td>
        <td>2-3 days</td>
    </tr>
    <tr>
        <td>Phencyclidine</td>
        <td>5</td>
        <td>12.5</td>
        <td>25</td>
        <td>2-3 days</td>
    </tr>
    <tr>
        <td>Methadone</td>
        <td>60</td>
        <td>120</td>
        <td>300</td>
        <td>2-3 days</td>
    </tr>
    <tr>
        <td>EDDP</td>
        <td>60</td>
        <td>120</td>
        <td>300</td>
        <td>2-3 days</td>
    </tr>
    <tr>
        <td>Amobarbital</td>
        <td>40</td>
        <td>100</td>
        <td>200</td>
        <td>2-4 days</td>
    </tr>
    <tr>
        <td>Butalbital</td>
        <td>40</td>
        <td>100</td>
        <td>200</td>
        <td>2-4 days</td>
    </tr>
    <tr>
        <td>Pentobarbital</td>
        <td>40</td>
        <td>100</td>
        <td>200</td>
        <td>1-2 days</td>
    </tr>
    <tr>
        <td>Phenobarbital</td>
        <td>40</td>
        <td>100</td>
        <td>200</td>
        <td>2 weeks</td>
    </tr>
    <tr>
        <td>Secobarbital</td>
        <td>40</td>
        <td>100</td>
        <td>200</td>
        <td>1-2 days</td>
    </tr>
    <tr>
        <td>&alpha;-Hydroxyalprazolam</td>
        <td>20</td>
        <td>40</td>
        <td>100</td>
        <td>1-4 days</td>
    </tr>
    <tr>
        <td>&alpha; -Hydroxytirazolam</td>
        <td>20</td>
        <td>40</td>
        <td>100</td>
        <td>1-4 days</td>
    </tr>
    <tr>
        <td>&alpha; -Hydroxymidazolam</td>
        <td>20</td>
        <td>40</td>
        <td>100</td>
        <td>1-4 days</td>
    </tr>
    <tr>
        <td>2-Hydroxyethylflurazepam</td>
        <td>20</td>
        <td>40</td>
        <td>100</td>
        <td>1-4 days</td>
    </tr>
    <tr>
        <td>7-Aminoflunitrazepam</td>
        <td>20</td>
        <td>40</td>
        <td>100</td>
        <td>1-4 days</td>
    </tr>
    <tr>
        <td>7-Aminoclonazepam</td>
        <td>20</td>
        <td>40</td>
        <td>100</td>
        <td>1-4 days</td>
    </tr>
    <tr>
        <td>7-Aminonitrazepam</td>
        <td>20</td>
        <td>40</td>
        <td>100</td>
        <td>1-4 days</td>
    </tr>
    <tr>
        <td>Lorazepam</td>
        <td>20</td>
        <td>40</td>
        <td>100</td>
        <td>1-4 days</td>
    </tr>
    <tr>
        <td>Nordiazepam</td>
        <td>20</td>
        <td>40</td>
        <td>100</td>
        <td>1-4 days</td>
    </tr>
    <tr>
        <td>Oxazepam</td>
        <td>20</td>
        <td>40</td>
        <td>100</td>
        <td>1-4 days</td>
    </tr>
    <tr>
        <td>Temazepam</td>
        <td>20</td>
        <td>40</td>
        <td>100</td>
        <td>1-4 days</td>
    </tr>
    <tr>
        <td>Norpropoxyphene</td>
        <td>10</td>
        <td>50</td>
        <td>100</td>
        <td>2-3 days</td>
    </tr>
    <tr>
        <td>Ketamine</td>
        <td>10</td>
        <td>50</td>
        <td>100</td>
        <td>2-3 days</td>
    </tr>
    <tr>
        <td>Norketamine</td>
        <td>10</td>
        <td>50</td>
        <td>100</td>
        <td>2-3 days</td>
    </tr>
    <tr>
        <td>Normeperidine</td>
        <td>40</td>
        <td>100</td>
        <td>200</td>
        <td>2-3 days</td>
    </tr>
    <tr>
        <td>Tramadol</td>
        <td>40</td>
        <td>80</td>
        <td>200</td>
        <td>2-3 days</td>
    </tr>
    <tr>
        <td>Buprenorphine</td>
        <td>1</td>
        <td>2</td>
        <td>5</td>
        <td>2-3 days</td>
    </tr>
    <tr>
        <td>Norbuprenorphine</td>
        <td>1</td>
        <td>2</td>
        <td>5</td>
        <td>2-3 days</td>
    </tr>
    <tr>
        <td>Ethyl glucuronide</td>
        <td>50</td>
        <td>100</td>
        <td>100</td>
        <td>2-3 days</td>
    </tr>
    <tr>
        <td>Ethyl sulfate</td>
        <td>12.5</td>
        <td>25</td>
        <td>25</td>
        <td>2-3 days</td>
    </tr>
    <tr>
        <td>Zolpidem</td>
        <td>4</td>
        <td>8</td>
        <td>20</td>
        <td>2-3 days</td>
    </tr>
    <tr>
        <td>Zolpidem Carboxylic Acid</td>
        <td>4</td>
        <td>8</td>
        <td>20</td>
        <td>2-3 days</td>
    </tr>
    <tr>
        <td>Carisoprodol</td>
        <td>10</td>
        <td>20</td>
        <td>50</td>
        <td>2-3 days</td>
    </tr>
    <tr>
        <td>Meprobamate</td>
        <td>10</td>
        <td>20</td>
        <td>50</td>
        <td>2-3 days</td>
    </tr>
    <tr>
    <td colspan="5"></td>
</tr>  
</tbody>
<thead>
      <tr>
        <th style="border: 1px solid #ddd; padding: 8px; text-align: left;">Analyte</th>
        <th style="border: 1px solid #ddd; padding: 8px; text-align: left;">LOD (pg/mL)</th>
        <th style="border: 1px solid #ddd; padding: 8px; text-align: left;">LOQ (pg/mL)</th>
        <th style="border: 1px solid #ddd; padding: 8px; text-align: left;">Cutoff (pg/mL)</th>
        <th style="border: 1px solid #ddd; padding: 8px; text-align: left;">Detection Window</th>
      </tr>
</thead>
    <tr>
        <td>Fentanyl</td>
        <td>40</td>
        <td>40</td>
        <td>100</td>
        <td>2-3 days</td>
    </tr>
    <tr>
        <td>Norfentanyl</td>
        <td>40</td>
        <td>40</td>
        <td>100</td>
        <td>2-3 days</td>
    </tr>
    <tr>
        <td>Alfentanil</td>
        <td>40</td>
        <td>40</td>
        <td>100</td>
        <td>2-3 days</td>
    </tr>
    <tr>
        <td>Sufentanil</td>
        <td>40</td>
        <td>40</td>
        <td>100</td>
        <td>2-3 days</td>
    </tr>
    <tr>
        <td>Norsufentanil</td>
        <td>40</td>
        <td>40</td>
        <td>100</td>
        <td>2-3 days</td>
    </tr>
</table>
</div>


<div id="urine-table2" class="table-banner" onclick="toggleCollapse(this)">
  <span class="table-text">Table 2. Sample Data Dictionary from Urine Assays</span>
  <span class="table-arrow">▸</span>
</div>
<div class="table-collapsible-content">
<table style="width: 100%; border-collapse: collapse; table-layout: fixed;">
    <thead>
      <tr>
        <th style="border: 1px solid #ddd; padding: 8px; text-align: left;">Variable</th>
        <th style="border: 1px solid #ddd; padding: 8px; text-align: left;">Description</th>
        <th style="border: 1px solid #ddd; padding: 8px; text-align: left;">Form</th>
        <th style="border: 1px solid #ddd; padding: 8px; text-align: left;">Options</th>
       </tr>
    </thead>
    <tbody>
    <tr>
        <td>Specimen_ID</td>
        <td>Specimen ID</td>
        <td>String</td>
        <td>string</td>
    </tr>
    <tr>
        <td>PSCID</td>
        <td>Participant ID</td>
        <td>String</td>
        <td>string</td>
    </tr>
    <tr>
        <td>Visit_time_point</td>
        <td>Visit time point</td>
        <td>Categorical</td>
        <td>1: visit 1</li>
        <li>2: visit 2</li></td>
    </tr>
    <tr>
        <td>c_any_specimen_u</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">Specimen level result (positive for any analyte in confirmatory tests)</td>
        <td>Categorical</td>
        <td><li>1: positive</li>
        <li>0: negative</li>
        <li>3: invalid</li></td>
    </tr>
    <tr>
        <td>c_any_stim_u</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">Any stimulants in urine (based on confirmatory results for amphetamine, methamphetamine, MDM, MDA, MDEA, benzoylecgonine)</td>
        <td>Categorical</td>
        <td><li>1: positive</li>
        <li>0: negative</li>
        <li>3: invalid</li></td>
    </tr>
    <tr>
        <td>s_amp_u</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">Screening test in urine: amphetamines (amp)</td>
        <td>Categorical</td>
        <td><li>1: positive</li>
        <li>0: negative</li>
        <li>3: invalid</li></td>
    </tr>
    <tr>
        <td>c_amp_u_cat</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">Confirmatory test in urine: amphetamine (categorical) (amp)</td>
        <td>Categorical</td>
        <td><li>1: positive</li>
        <li>0: negative</li>
        <li>3: cancelled</li>
        <li>4: screen negative</li></td>
    </tr>
    <tr>
        <td>c_amp_u</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">Confirmatory test in urine: amphetamine (amp)</td>
        <td>Continuous</td>
        <td>concentration value; -999</td>
    </tr>
</tbody>
</table>
</div>

The class-level (*c_any_stim_u*) and sample-level (*c_any_specimen_u*) are correspondingly scored as positive (1), negative (0), and invalid (3). If all classes are negative (0), then sample-levels are negative (0). All class-level groupings by analyte screening tests and analyte confirmatory tests are shown in [Table 3](#urine-table3).

<div id="urine-table3" class="table-banner" onclick="toggleCollapse(this)">
  <span class="table-text">Table 3. Mapping From Class to Screening Tests and Confirmatory Tests</span>
  <span class="table-arrow">▸</span>
</div>
<div class="table-collapsible-content">
<table style="width: 100%; border-collapse: collapse; table-layout: fixed;">
    <thead>
      <tr>
        <th style="border: 1px solid #ddd; padding: 8px; text-align: left;">Class</th>
        <th style="border: 1px solid #ddd; padding: 8px; text-align: left;">Screening Test</th>
        <th style="border: 1px solid #ddd; padding: 8px; text-align: left;">Confirmatory Test (positive screen reflex)</th>
      </tr>
    </thead>
    <tbody>
    <tr>
        <td colspan="1" rowspan="6">
            <div>stimulant (c_any_stim_u)</div>
        </td>
        <td colspan="1" rowspan="2">
            <div>amp (s_amp_u)</div>
        </td>
        <td>Amphetamine (c_amp_u)</td>
    </tr>
    <tr>
        <td>Methamphetamine (c_meth_u)</td>
    </tr>
    <tr>
        <td colspan="1" rowspan="3">
            <div>mdma (s_mdma_u)</div>
        </td>
        <td>MDM (c_mdm_u)</td>
    </tr>
    <tr>
        <td>MDA (c_mda_u)</td>
    </tr>
    <tr>
        <td>MDEA (c_mdea_u)</td>
    </tr>
    <tr>
        <td>coc (s_coc_u)</td>
        <td>Benzoylecgonine (c_ben_u)</td>
    </tr>
    <tr>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;" colspan="1" rowspan="3">
            <div>cannabinoid (c_any_cannabinoid_u)</div>
        </td>
        <td colspan="1" rowspan="3">
            <div>thc (s_thc_u)</div>
        </td>
        <td>Carboxy-delta-9-THC (c_delta-9-THC_u)</td>
    </tr>
    <tr>
        <td>Carboxy-Cannabidiol (c_cannabidiol_u)</td>
    </tr>
    <tr>
        <td>Carboxy-delta-8-THC (c_delta-8-THC_u)</td>
    </tr>
    <tr>
        <td colspan="1" rowspan="5">
            <div>barbiturate (c_any_barb_u)</div>
        </td>
        <td colspan="1" rowspan="5">
            <div>bar (s_bar_u)</div>
        </td>
        <td>Amobarbital (c_amobarb_u)</td>
    </tr>
    <tr><td>Secobarbital (c_secobarb_u)</td></tr>
    <tr><td>Pentobarbital (c_pentobarb_u)</td></tr>
    <tr><td>Phenobarbital (c_phenobarb_u)</td></tr>
    <tr><td>Butalbital (c_butalbital_u)</td></tr>
    <tr>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;" colspan="1" rowspan="11">
            <div>benzodiazepine (c_any_benzo_u)</div>
        </td>
        <td colspan="1" rowspan="11">
            <div>benz (s_benz_u)</div>
        </td>
        <td>Oxazepam (c_oxaz_u)</td>
    </tr>
    <tr><td>Nordiazepam (c_nord_u)</td></tr>
    <tr><td>Temazepam (c_tema_u)</td></tr>
    <tr><td>Hydroxymidazolam (c_homi_u)</td></tr>
    <tr><td>Alphahydroxyalprazolam (c_aha_u)</td></tr>
    <tr><td>2hydroxyethylflurazepam (c_2hef_u)</td></tr>
    <tr><td>7Aminoclonazepam (c_7ac_u)</td></tr>
    <tr><td>7Aminoflunitrazepam (c_7af_u)</td></tr>
    <tr><td>7Aminonitrazepam (c_7an_u)</td></tr>
    <tr><td>Alphahydroxytriazolam (c_aht_u)</td></tr>
    <tr><td>Lorazepam (c_lor_u)</td></tr>
    <tr>
        <td colspan="1" rowspan="20">
            <div>opioids (c_any_opioid_u)</div>
        </td>
        <td colspan="1" rowspan="5">
            <div>opi (s_opi_u)</div>
        </td>
        <td>Codeine (c_cod_u)</td></tr>
    <tr><td>Morphine (c_mor_u)</td></tr>
    <tr><td>MAM (c_mam_u)</td></tr>
    <tr><td>Hydrocodone (c_hydroc_u)</td></tr>
    <tr><td>Hydromorphone (c_hydrom_u)</td></tr>
    <tr>
        <td colspan="1" rowspan="2"><div>mtd (s_mtd_u)</div></td>
        <td>Methadone (c_mtd_u)</td></tr>
    <tr>
    <td>EDDP (c_eddp_u)</td></tr>
    <tr>
        <td>ppx (s_ppx_u)</td>
        <td>Norpropoxyphene (c_nppx_u)</td>
    </tr>
    <tr>
        <td colspan="1" rowspan="2">
            <div>oxyc (s_oxyc_u)</div>
        </td>
        <td>Oxycodone (c_oxyc_u)</td>
    </tr>
    <tr>
        <td>Oxymorphone (c_oxym_u)</td>
    </tr>
    <tr>
        <td colspan="1" rowspan="2">
            <div>mep (s_mep_u)</div>
        </td>
        <td>Meperidinem (c_mep_u)</td>
    </tr>
    <tr><td>Normeperidine (c_nmep_u)</td></tr>
    <tr>
        <td>tram (s_tram_u)</td>
        <td>Tramadol (c_tram_u)</td>
    </tr>
    <tr>
        <td colspan="1" rowspan="3"><div>fent (s_fent_u)</div></td>
        <td>Fentanyl (c_fent_u)</td>
    </tr>
    <tr>
        <td>Norfentanyl (c_nfent_u)</td></tr>
    <tr><td>Alfentanil (c_afent_u)</td></tr>
    <tr>
        <td colspan="1" rowspan="2"><div>suf (s_suf_u)</div></td>
        <td>Norsufentanil (c_nsuf_u)</td>
    </tr>
    <tr><td>Sufentanil (c_suf_u)</td></tr>
    <tr>
        <td colspan="1" rowspan="2">
            <div>bup (s_bup_u)</div>
        </td>
        <td>Buprenorphine (c_bup_u)</td>
    </tr>
    <tr><td>Norbuprenorpine (c_nbup_u)</td></tr>
    <tr>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;" colspan="1" rowspan="2">
            <div>muscle relaxant (c_any_mscrlx_u)</div>
        </td>
        <td colspan="1" rowspan="2">
            <div>crs (s_crs_u)</div>
        </td>
        <td>Carisoprodol (c_crs_u)</td>
    </tr>
    <tr><td>Meprobamate (c_mepb_u)</td></tr>
    <tr>
        <td colspan="1" rowspan="2"><div>ethanol (c_ethanol_u)</div></td>
        <td colspan="1" rowspan="2">
            <div>etgeia (s_etgeia_u)</div>
        </td>
        <td>EthylGluc-0100 (c_ethglu_u0)</td>
    </tr>
    <tr><td>EthylSul-100 (c_ethsyl_u)</td></tr>
    <tr>
        <td colspan="1" rowspan="2">
            <div>sedative (c_sedative_u)</div>
        </td>
        <td colspan="1" rowspan="2">
            <div>zol (s_zol_u)</div>
        </td>
        <td>Zolpidem (c_zol_u0)</td>
    </tr>
    <tr>
        <td>Zolpidem CA (c_zolc_u)</td>
    </tr>
    <tr>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;" colspan="1" rowspan="3"><div>dissociative anesthetic (c_disanesth_u)</div></td>
        <td colspan="1" rowspan="2"><div>ket (s_ket_u)</div></td>
        <td>Ketamine (c_ket_u)</td>
    </tr>
    <tr><td>Norketamine (c_nket_u)</td></tr>
    <tr><td>pcp (s_pcp_u)</td>
    <td>Phencyclidine (c_pcp_u)</td></tr>
    <tr><td>nicotine (c_nicotine_u)</td>
        <td>&nbsp;</td>
        <td>Cotinine (c_cot_u)</td>
    </tr>
</tbody>
</table>
</div>

## References
<div class="references">
    <p>Bandoli, G., Anunziata, F., Bogdan, R., Zilverstand, A., Chaiyachati, B. H., Gurka, K. K., Sullivan, E., Croff, J., & Bakhireva, L. N. (2024). Assessment of substance exposures in nail clipping samples: A systematic review. <i>Drug and Alcohol Dependence</i>, 254, 111038. <a href="https://doi.org/10.1016/j.drugalcdep.2023.111038" target="_blank">https://doi.org/10.1016/j.drugalcdep.2023.111038</a></p>
</div>
<br>
