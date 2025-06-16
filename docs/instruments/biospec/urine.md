# Urine

**Full Name**: Maternal Urine       
**Table Name**: `bio_biosample_urine`       
**Construct**: Toxicology screen for substances & environmental exposures

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
<p>For all toxicology screens, continuous variables should be interpreted with cautiong based on the threshold limits of quantification (LOQs), or the cutoff concentration used to categorize metabolites as positive or negative. LOQs are provided in <a href="#urine-table1">Table 1. Urine Assay Thresholds for Analytes</a>.</p> 

<b>Urinary Concentration Corrections</b>
<p>Urine concentrations vary by participant. Urinary concentration corrections can be made by creatine or specific gravity. There is a <a href="../../changelog/knownissues/#urine-incorrect-specific-gravity-variable">known issue</a> with the specific gravity values and they are not meaningful in the current data release; therefore, only the initial creatinine results from sample validation should be used for urinary concentration corrections. Creatinine values are provided for researchers who wish to adjust/correct for urinary concentration in continuous measures or apply different thresholds.</p> 
</div>


## Administration & Quality Control

<table style="width: 100%; border-collapse: collapse; table-layout: fixed; font-size: 16px;">
<tbody>
<tr><td><b>Respondent</b></td>
<td>Pregnant/postpartum person</td></tr>
<tr><td><b>Administration</b></td>
<td>Self-collected</td></tr>
<tr><td><b>Visits</b></td>
<td>V01</td></tr>
<tr><td><b>Completion Time</b></td>
<td>5 min</td></tr>
<tr><td><b>Quality Control</b></td>
<td>Examine assay ranges and categorical versus continuous measures.</td></tr>
</tbody>
</table>


## Instrument Details

These data are the results of urine toxicology assays. Test results for substances were determined to be positive or negative based on predefined thresholds, or invalid (for specimens identified as dilute, substituted, adulterated, or otherwise insufficient based on validation).
<img src="../images/Fig1_biospec_urine.png" width="80%" height="auto" class="center">

### Validation
Validation is based on creatinine, pH, and nitrite measurements. Specimens with low creatinine (<20 mg/dL) are confirmed using specific gravity via refractometer (decision grid below), and the creatinine analysis is repeated to rule out issues with the first analysis (e.g. sample mix-ups, air bubble in a line on the instrument, etc.):
<img src="../images/Table1_biospec_urine.png" width="80%" height="auto" class="center">

### Assay Details
Based on predefined thresholds ([Table 1](#urine-table1)), a confirmatory test result for any substance analyte (e.g. *Amphetamine (c_amp_u)*) is determined to be positive, negative, or invalid ([Table 2](#urine-table2)). The class-level (*c_any_X_u*) and screen-level (*s_X_u*) are correspondingly scored as positive (1), negative (0), and invalid (3). The confirmatory tests (*c_X_u*) are scored as (1) positive, (0) negative, 3 (cancelled), and 4 (screen negative). If all classes are negative (0), then sample-levels are negative (0). All class-level groupings by analyte screening tests and analyte confirmatory tests are shown in [Table 3](#urine-table3).

<div id="urine-table1" class="table-banner" onclick="toggleCollapse(this)">
  <span class="table-text">Table 1. Urine Assay Thresholds for Analytes</span>
  <span class="arrow">▸</span>
</div>
<div class="table-collapsible-content">
<table style="width: 100%; border-collapse: collapse; table-layout: fixed;">
<thead>
      <tr>
        <th style="width: 30%;">Analyte</th>
        <th style="width: 20%;"><span class="tooltip tooltip-bottom">LOD<span class="tooltiptext">Limit of detection</span></span> (ng/mL)</th>
        <th style="width: 10%;"><span class="tooltip tooltip-bottom">LOQ<span class="tooltiptext">Limit of quantification</span></span> (ng/mL)</th>
        <th style="width: 10%;">Cutoff (ng/mL)</th>
        <th style="width: 40%;">Detection Window</th>
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
        <td><span class="tooltip tooltip-right">Cotinine<span class="tooltiptext"> Based on DRI® Cotinine assay for the qualitative and semiquantitative determination of Cotinine</span></span></td>
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
  <span class="arrow">▸</span>
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
        <td><span class="tooltip tooltip-right">c_amp_u_cat<span class="tooltiptext">Categorical confirmatory test variable for nicotine follows a different convention and is ‘c_nicotine_u'</span></span></td>
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

<div id="urine-table3" class="table-banner" onclick="toggleCollapse(this)">
  <span class="table-text">Table 3. Mapping From Class to Screening Tests and Confirmatory Tests</span>
  <span class="arrow">▸</span>
</div>
<div class="table-collapsible-content">
<table style="width: 100%; border-collapse: collapse; table-layout: fixed;">
    <thead>
      <tr>
        <th style="width: 50%;">Class</th>
        <th style="width: 20%;">Screening Test</th>
        <th style="width: 30%;">Confirmatory Test (positive screen reflex)</th>
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
        <td colspan="1" rowspan="3">
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
        <td colspan="1" rowspan="11">
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
        <td colspan="1" rowspan="19">
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
        <td>mep (s_mep_u)</td>
        <td>Normeperidine (c_nmep_u)</td>
    </tr>
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
        <td>Buprenorphine (c_bup_u)</td></tr>
    <tr><td>Norbuprenorpine (c_nbup_u)</td></tr>
    <tr>
        <td colspan="1" rowspan="2">
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
        <td>EthylGluc-0100 (c_ethglu_u)</td>
    </tr>
    <tr><td>EthylSul-100 (c_ethsyl_u)</td></tr>
    <tr>
        <td colspan="1" rowspan="2">
            <div>sedative (c_sedative_u)</div>
        </td>
        <td colspan="1" rowspan="2">
            <div>zol (s_zol_u)</div>
        </td>
        <td>Zolpidem (c_zol_u)</td>
    </tr>
    <tr>
        <td>Zolpidem CA (c_zolc_u)</td>
    </tr>
    <tr>
        <td colspan="1" rowspan="3"><div>dissociative anesthetic (c_disanesth_u)</div></td>
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
<br>