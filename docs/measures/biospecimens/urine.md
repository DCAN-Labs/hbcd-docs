# Urine
**Full Name**: URINE		        
**Construct**: Toxicology screen, urine     
**Description**: Results of toxicology assays in urine collected at V1

<details>
<summary>Implementation & Data Collection Details</summary>
<ul>
<li><b>Method of Administration</b>: Self-collected</li>
<li><b>Respondent</b>: Pregnant person</li>
<li><b>Visits</b>: V01</li>
<li><b>Estimated length of time for completion</b>: 5 minutes</li>
</ul>
</details>

## Assay
Based on the predefined thresholds outlined in **Table 1**, a confirmatory test result for any substance analyte (e.g. *Amphetamine (c_amp_u)*) was determined to be positive, negative, or invalid (**Table 2**). Note that continuous variables should be interpreted with caution based on the threshold limits of quantification (LOQs). The class-level (*c_any_stim_u*) and sample-level (*c_any_specimen_u*) are correspondingly scored as positive (1), negative (0), and invalid (3). If all classes are negative (0), then sample-levels are negative (0). All class-level groupings by analyte screening tests and analyte confirmatory tests are shown in **Table 3**. 

<details>
  <summary>Table 1. Urine Assay Thresholds for Analytes</summary>
  <table class="docutils">
    <thead>
      <tr>
        <th>Analyte</th>
        <th>LOD<br />(ng/mL)</th>
        <th>LOQ<br />(ng/mL)</th>
        <th>Cutoff<br />(ng/mL)</th>
        <th>Detection Window</th>
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
		<td style="width: 200px; word-wrap: break-word; white-space: normal;">2-5 days for casual use; 10-14 for chronic use</td>
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
		<td>Cotinine*</td>
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
</tbody>
  <br>
  <table class="docutils" style="width: 100%;">
    <thead>
      <tr>
        <th>Analyte</th>
        <th>LOD (pg/mL)</th>
        <th>LOQ (pg/mL)</th>
        <th>Cutoff (pg/mL)</th>
        <th>Detection Window</th>
      </tr>
    </thead>
    <tbody>
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
</tbody>
</table>
<i>*Based on DRI® Cotinine assay for the qualitative and semiquantitative determination of Cotinine</i><br>
<i>LOD: limit of detection; LOQ: limit of quantification: Cutoff concentration used to categorize metabolite as positive/negative</i>
</details>

<details>
  <summary>Table 2. Sample Data Dictionary from Urine Assays</summary>
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
		<td>1: visit 1<br />2: visit 2</td>
	</tr>
	<tr>
		<td>c_any_specimen_u</td>
		<td style="width: 200px; word-wrap: break-word; white-space: normal;">Specimen level result (positive for any analyte in confirmatory tests)</td>
		<td>Categorical</td>
		<td>1: positive<br />0: negative<br />3: invalid</td>
	</tr>
	<tr>
		<td>c_any_stim_u</td>
		<td style="width: 200px; word-wrap: break-word; white-space: normal;">Any stimulants in urine (based on confirmatory results for amphetamine, methamphetamine, MDM, MDA, MDEA, benzoylecgonine)</td>
		<td>Categorical</td>
		<td>1: positive<br />0: negative<br />3: invalid</td>
	</tr>
	<tr>
		<td>s_amp_u</td>
		<td style="width: 200px; word-wrap: break-word; white-space: normal;">Screening test in urine: amphetamines (amp)</td>
		<td>Categorical</td>
		<td>1: positive<br />0: negative<br />3: invalid</td>
	</tr>
	<tr>
		<td>c_amp_u_cat</td>
		<td style="width: 200px; word-wrap: break-word; white-space: normal;">Confirmatory test in urine: amphetamine (categorical) (amp)</td>
		<td>Categorical</td>
		<td>1: positive<br />0: negative<br />3: cancelled<br />4: screen negative</td>
	</tr>
	<tr>
		<td>c_amp_u</td>
		<td style="width: 200px; word-wrap: break-word; white-space: normal;">Confirmatory test in urine: amphetamine (amp)</td>
		<td>Continuous</td>
		<td>concentration value; -999</td>
	</tr>
</tbody>
</table>
</details>

<details>
  <summary>Table 3. Mapping From Class to Screening Tests and Confirmatory Tests</summary>
  <table class="docutils" style="width: 100%;">
  <br>
    <thead>
      <tr>
        <th>Class</th>
        <th>Screening Test</th>
        <th>Confirmatory Test (positive screen reflex)</th>
      </tr>
    </thead>
    <tbody>
	<tr>
		<td colspan="1" rowspan="6">
			<div>stimulant<br /> (c_any_stim_u)</div>
		</td>
		<td colspan="1" rowspan="2">
			<div>amp<br /> (s_amp_u)</div>
		</td>
		<td>Amphetamine (c_amp_u)</td>
	</tr>
	<tr>
		<td>Methamphetamine (c_meth_u)</td>
	</tr>
	<tr>
		<td colspan="1" rowspan="3">
			<div>mdma<br /> (s_mdma_u)</div>
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
		<td>coc <br /> (s_coc_u)</td>
		<td>Benzoylecgonine (c_ben_u)</td>
	</tr>
	<tr>
		<td colspan="1" rowspan="3">
			<div>cannabinoid<br /> (c_any_cannabinoid_u)</div>
		</td>
		<td colspan="1" rowspan="3">
			<div>thc<br /> (s_thc_u)</div>
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
			<div>barbiturate<br /> (c_any_barb_u)</div>
		</td>
		<td colspan="1" rowspan="5">
			<div>bar <br /> (s_bar_u)</div>
		</td>
		<td>Amobarbital (c_amobarb_u)</td>
	</tr>
	<tr>
		<td>Secobarbital (c_secobarb_u)</td>
	</tr>
	<tr>
		<td>Pentobarbital (c_pentobarb_u)</td>
	</tr>
	<tr>
		<td>Phenobarbital (c_phenobarb_u)</td>
	</tr>
	<tr>
		<td>Butalbital (c_butalbital_u)</td>
	</tr>
	<tr>
		<td colspan="1" rowspan="11">
			<div>benzodiazepine<br /> (c_any_benzo_u)</div>
		</td>
		<td colspan="1" rowspan="11">
			<div>benz <br /> (s_benz_u)</div>
		</td>
		<td>Oxazepam (c_oxaz_u)</td>
	</tr>
	<tr>
		<td>Nordiazepam (c_nord_u)</td>
	</tr>
	<tr>
		<td>Temazepam (c_tema_u)</td>
	</tr>
	<tr>
		<td>Hydroxymidazolam (c_homi_u)</td>
	</tr>
	<tr>
		<td>Alphahydroxyalprazolam (c_aha_u)</td>
	</tr>
	<tr>
		<td>2hydroxyethylflurazepam (c_2hef_u)</td>
	</tr>
	<tr>
		<td>7Aminoclonazepam (c_7ac_u)</td>
	</tr>
	<tr>
		<td>7Aminoflunitrazepam (c_7af_u)</td>
	</tr>
	<tr>
		<td>7Aminonitrazepam (c_7an_u)</td>
	</tr>
	<tr>
		<td>Alphahydroxytriazolam (c_aht_u)</td>
	</tr>
	<tr>
		<td>Lorazepam (c_lor_u)</td>
	</tr>
	<tr>
		<td colspan="1" rowspan="20">
			<div>opioids<br /> (c_any_opioid_u)</div>
		</td>
		<td colspan="1" rowspan="5">
			<div>opi <br /> (s_opi_u)</div>
		</td>
		<td>Codeine (c_cod_u)</td>
	</tr>
	<tr>
		<td>Morphine (c_mor_u)</td>
	</tr>
	<tr>
		<td>MAM (c_mam_u)</td>
	</tr>
	<tr>
		<td>Hydrocodone (c_hydroc_u)</td>
	</tr>
	<tr>
		<td>Hydromorphone (c_hydrom_u)</td>
	</tr>
	<tr>
		<td colspan="1" rowspan="2">
			<div>mtd <br /> (s_mtd_u)</div>
		</td>
		<td>Methadone (c_mtd_u)</td>
	</tr>
	<tr>
		<td>EDDP (c_eddp_u)</td>
	</tr>
	<tr>
		<td>ppx <br /> (s_ppx_u)</td>
		<td>Norpropoxyphene (c_nppx_u)</td>
	</tr>
	<tr>
		<td colspan="1" rowspan="2">
			<div>oxyc <br /> (s_oxyc_u)</div>
		</td>
		<td>Oxycodone (c_oxyc_u)</td>
	</tr>
	<tr>
		<td>Oxymorphone (c_oxym_u)</td>
	</tr>
	<tr>
		<td colspan="1" rowspan="2">
			<div>mep <br /> (s_mep_u)</div>
		</td>
		<td>Meperidinem (c_mep_u)</td>
	</tr>
	<tr>
		<td>Normeperidine (c_nmep_u)</td>
	</tr>
	<tr>
		<td>tram <br /> (s_tram_u)</td>
		<td>Tramadol (c_tram_u)</td>
	</tr>
	<tr>
		<td colspan="1" rowspan="3">
			<div>fent <br /> (s_fent_u)</div>
		</td>
		<td>Fentanyl (c_fent_u)</td>
	</tr>
	<tr>
		<td>Norfentanyl (c_nfent_u)</td>
	</tr>
	<tr>
		<td>Alfentanil (c_afent_u)</td>
	</tr>
	<tr>
		<td colspan="1" rowspan="2">
			<div>suf <br /> (s_suf_u)</div>
		</td>
		<td>Norsufentanil (c_nsuf_u)</td>
	</tr>
	<tr>
		<td>Sufentanil (c_suf_u)</td>
	</tr>
	<tr>
		<td colspan="1" rowspan="2">
			<div>bup <br /> (s_bup_u)</div>
		</td>
		<td>Buprenorphine (c_bup_u)</td>
	</tr>
	<tr>
		<td>Norbuprenorpine (c_nbup_u)</td>
	</tr>
	<tr>
		<td colspan="1" rowspan="2">
			<div>muscle relaxant<br />(c_any_mscrlx_u)</div>
		</td>
		<td colspan="1" rowspan="2">
			<div>crs <br /> (s_crs_u)</div>
		</td>
		<td>Carisoprodol (c_crs_u)</td>
	</tr>
	<tr>
		<td>Meprobamate (c_mepb_u)</td>
	</tr>
	<tr>
		<td colspan="1" rowspan="2">
			<div>ethanol <br /> (c_ethanol_u)</div>
		</td>
		<td colspan="1" rowspan="2">
			<div>etgeia <br /> (s_etgeia_u)</div>
		</td>
		<td>EthylGluc-0100 (c_ethglu_u0)</td>
	</tr>
	<tr>
		<td>EthylSul-100 (c_ethsyl_u)</td>
	</tr>
	<tr>
		<td colspan="1" rowspan="2">
			<div>sedative <br /> (c_sedative_u)</div>
		</td>
		<td colspan="1" rowspan="2">
			<div>zol <br /> (s_zol_u)</div>
		</td>
		<td>Zolpidem (c_zol_u0)</td>
	</tr>
	<tr>
		<td>Zolpidem CA (c_zolc_u)</td>
	</tr>
	<tr>
		<td colspan="1" rowspan="3">
			<div>dissociative anesthetic<br />(c_disanesth_u)</div>
		</td>
		<td colspan="1" rowspan="2">
			<div>ket <br /> (s_ket_u)</div>
		</td>
		<td>Ketamine (c_ket_u)</td>
	</tr>
	<tr>
		<td>Norketamine (c_nket_u)</td>
	</tr>
	<tr>
		<td>pcp <br /> (s_pcp_u)</td>
		<td>Phencyclidine (c_pcp_u)</td>
	</tr>
	<tr>
		<td>nicotine (c_nicotine_u)</td>
		<td>&nbsp;</td>
		<td>Cotinine (c_cot_u)</td>
	</tr>
</tbody>
</table>
</details>


## Quality Control & Known Issues
QC procedures involved examining assay ranges and categorical versus continuous measures. No common issues were identified from QC.

Subject matter experts have highlighted one potential issue regarding creatinine results included in the data release. For context, urine specimen validation is determined based on creatinine, pH, and nitrite measurements (**Figure 1**). Specimens with low creatinine (<20 mg/dL) are confirmed using specific gravity via refractometer, and the creatinine analysis is repeated to rule out issues with the first analysis (e.g. sample mix-ups, air bubble in a line on the instrument, etc.) (**Table 4**). All assays are marked as invalid for specimens identified as dilute, substituted, adulterated, or otherwise insufficient. However, for data release, only the initial creatinine results are reported. Creatinine and specific gravity values are therefore provided for researchers who wish to adjust for urinary concentration in continuous measures or apply different thresholds.

**Figure 1. Urine Processing Schematic**
<img src="../Fig1_biospec_urine.png" width="90%" height="auto">

<br>

**Table 4. Urine Validity (Creatinine/Specific Gravity) Decision Grid**
<img src="../Table1_biospec_urine.png" width="90%" height="auto">

<br>