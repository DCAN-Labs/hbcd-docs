# Nails

**Full Name**: Maternal Nails       
**Table Name**: `bio_biosample_nails`       
**Construct**: Toxicology screen for substances & environmental exposures conducted on fingernails and toenails

<p>
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
<br>
<b>Continuous Variables</b>
<p>For all toxicology screens, continuous variables should be interpreted with cautiong based on the threshold limits of quantification (LOQs), or the cutoff concentration used to categorize metabolites as positive or negative. LOQs are provided in <a href="#nails-table1">Table 1. Nail Assay Thresholds</a>.</p> 
<b>Updated Workflow</b>
<p>As of July 1, 2024, the nail processing workflow was updated to optimize specimen use and allow confirmation testing for low sample quantities. Prior to this update, remnants of ELISA extract were not used for confirmation when specimens had insufficient sample.</p> 
</div>
</p>


## Administration & Quality Control

<table style="width: 100%; border-collapse: collapse; table-layout: fixed; font-size: 16px;">
<tbody>
<tr><td><b>Respondent</b></td>
<td>Pregnant/postpartum person</td></tr>
<tr><td><b>Administration</b></td>
<td>Self-collected under research team supervision, or collected by research team</td></tr>
<tr><td><b>Visits</b></td>
<td>V01, V02</td></tr>
<tr><td><b>Completion Time</b></td>
<td>5 min</td></tr>
<tr><td><b>Quality Control</b></td>
<td>Examine assay ranges and categorical versus continuous measures.</td></tr>
</tbody>
</table>

## Instrument Details - USDTL Assay
Fingernail and toenail specimens are sorted by weight, and those weighing at least 20 mg undergo ELISA screening, followed by LCMSMS confirmation for presumptive positives, each requiring an additional 20 mg. If insufficient specimen remains for LCMSMS, the remnant ELISA extract is used for confirmation.

<img src="../images/Fig1_nails.png" width="70%" height="auto" class="center">

Based on the predefined threshold outlined in [Table 1](#nails-table1), a confirmatory test result for any substance analyte (e.g. *Amphetamine (c_amp_u)*) is determined to be positive, negative, or invalid (*QNS* i.e. *quantity not sufficient*) ([Table 2](#nails-table2)).

Based on the confirmatory test (i.e. reflexes from positive screening test) result for any substance, the class-level (e.g. *c_any_X_n*) and screening-level (e.g. *s_X_n*) are correspondingly scored as positive (1), negative (0), and quantity not sufficient (QNS) (3). The confirmatory tests (*c_X_n*) are scored as (1) positive, (0) negative, 3 (QNS), and 4 (screen negative). If all classes are negative (0), then sample-levels are negative (0). All class-level groupings by analyte screening tests and analyte confirmatory tests are shown in [Table 3](#nails-table3).

<div id="nails-table1" class="table-banner" onclick="toggleCollapse(this)">
  <span class="text-with-link">
  <span class="text">Table 1. Nail Assay Thresholds</span>
  <a class="anchor-link" href="#nails-table1" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="table-collapsible-content">
<table style="width: 100%; border-collapse: collapse; table-layout: fixed;">
<thead>
    <tr>
    <th style="width: 30%;">Analyte</th>
    <th style="width: 20%;"><span class="tooltip tooltip-bottom">LOD
                <span class="tooltiptext">Limit of detection</span>
            </span> (pg/mL)</th>
    <th style="width: 10%;"><span class="tooltip tooltip-bottom">LOQ
                <span class="tooltiptext">Limit of quantification</span>
            </span> (pg/mL)</th>
    <th style="width: 10%;">Cutoff (pg/mL)</th>
    <th style="width: 40%;">Detection Window (months)</th>
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
  <span class="text-with-link">
  <span class="text">Table 2. Sample-Data Dictionary Nail Assays</span>
  <a class="anchor-link" href="#nails-table2" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
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
        <td><span class="tooltip tooltip-right">c_amp_n_cat
                <span class="tooltiptext" style="font-size: 0.8em;">Categorical confirmatory test variable for alcohol follows a different convention and is ‘c_ethanol_n’</span>
            </span></td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">Confirmatory test in nails: amphetamine (categorical) (<i>amp/mamp</i>)</td>
        <td>Categorical</td>
        <td>1: positive<br />0: negative<br />3: QNS<br />4: screen negative</td>
    </tr>
    <tr>
        <td>c_amp_n</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">Confirmatory test in nails: amphetamine (<i>amp/mamp</i>)</td>
        <td>Continuous</td>
        <td>concentration value<br>-999</td>
    </tr>
</tbody>
</table>
</div>




<div id="nails-table3" class="table-banner" onclick="toggleCollapse(this)">
  <span class="text-with-link">
  <span class="text">Table 3. Mapping from Class to Screening Tests and Confirmatory Tests for Nails</span>
  <a class="anchor-link" href="#nails-table3" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="table-collapsible-content">
<table style="width: 100%; border-collapse: collapse; table-layout: fixed;">
<thead>
<tr>
    <th>Class</th>
    <th>Screening test</th>
    <th>Confirmatory Test</th>      
</tr>
</thead>
<tbody>
<tr>
    <td colspan="1" rowspan="9">Stimulant (c_any_stim_n)</td>
    <td colspan="1" rowspan="5">amp/mamp (s_amp_n, s_mamp_n)</td>
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
    <td>Cannabinoid (c_any_cannabinoid_n)</td>
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
    <tr><td>Sufentanil (c_suf_n)</td></tr>
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

### References
<div class="references">
    <p>Bandoli, G., Anunziata, F., Bogdan, R., Zilverstand, A., Chaiyachati, B. H., Gurka, K. K., Sullivan, E., Croff, J., & Bakhireva, L. N. (2024). Assessment of substance exposures in nail clipping samples: A systematic review. <i>Drug and Alcohol Dependence</i>, 254, 111038. <a href="https://doi.org/10.1016/j.drugalcdep.2023.111038" target="_blank">https://doi.org/10.1016/j.drugalcdep.2023.111038</a></p>
</div>
<br>
