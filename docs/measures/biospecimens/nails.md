# Nails
**Full Name**: NAILS		       
**Construct**: Toxicology screen, fingernails and toenails     
**Description**: Results of toxicology assays in nails collected at V1 and V2

The nail processing workflow was re-developed and implemented on July 1, 2024 to consider the amount of specimen available and offer the opportunity for additional confirmation tests in case of low sample quantity. Specimens are sorted by weight and screened following the workflow outlined in **Figure 1**. Specimens that contain at least 20 mg of nail are screened using ELISA with subsequent LCMSMS confirmation for presumptive positives, each confirmation of which requires an additional 20 mg. In the updated workflow, if additional specimen is not available for LCMSMS confirmation, the remnant of ELISA extract is instead used for confirmation. Nail weights and test ordered (custom 14 panel test; EtG only; cancelled) are noted in the sample-data dictionary below (**Table 2**).

##### Figure 1. Schematic for nail processing
<img src="../Fig1_nails.png" width="100%" height="auto">

<details>
<summary>Implementation & Data Collection Details</summary>
<ul>
<li><b>Method of Administration</b>: Self-collected under research team supervision, or collected by research team</li>
<li><b>Respondent</b>: Pregnant/Postpartum person</li>
<li><b>Visits</b>: V01, V02</li>
<li><b>Estimated length of time for completion</b>: 5 minutes</li>
</ul>
</details>

## USDTL Assay
Based on the predefined threshold outlined in **Table 1**, a confirmatory test result for any substance analyte (e.g. *Amphetamine (c_amp_u)*) was determined to be positive, negative, or invalid (*QNS* i.e. *quantity not sufficient*) (**Table 2**). Note that continuous variables should be interpreted with caution based on the threshold limits of quantification (LOQs). The class-level (e.g. *c_nictotine_u*) and sample-level (e.g. *c_any_specimen_n*) are correspondingly scored as positive (1), negative (0), and invalid (3). If all classes are negative (0), then sample-levels are negative (0). All class-level groupings by analyte screening tests and analyte confirmatory tests are shown in **Table 3**. 

<details>
  <summary>Table 1. Nail Assay Thresholds </summary>
  <table class="docutils">
  <br>
    <thead>
      <tr>
		<th style="width: 180px; word-wrap: break-word; white-space: normal;">Analyte</th>
        <th>LOD<br />(pg/mL)</th>
        <th>LOQ<br />(pg/mL)</th>
        <th>Cutoff<br />(pg/mL)</th>
        <th>Detection Window (months)</th>
      </tr>
    </thead>
    <tbody>
	<tr>
		<td>Amphetamine</td>
		<td>20</td>
		<td>40</td>
		<td>100</td>
		<td>Finger 3-6 & Toe 10-14</td>
	</tr>
	<tr>
		<td>Methamphetamine</td>
		<td>20</td>
		<td>40</td>
		<td>100</td>
		<td>Finger 3-6 & Toe 10-14</td>
	</tr>
	<tr>
		<td>MDA</td>
		<td>20</td>
		<td>40</td>
		<td>100</td>
		<td>Finger 3-6 & Toe 10-14</td>
	</tr>
	<tr>
		<td>MDMA</td>
		<td>20</td>
		<td>40</td>
		<td>100</td>
		<td>Finger 3-6 & Toe 10-14</td>
	</tr>
	<tr>
		<td>MDEA</td>
		<td>20</td>
		<td>40</td>
		<td>100</td>
		<td>Finger 3-6 & Toe 10-14</td>
	</tr>
	<tr>
		<td>Carboxy-delta-9-THC</td>
		<td>0.01</td>
		<td>0.02</td>
		<td>0.05</td>
		<td>Finger 3-6 & Toe 10-14</td>
	</tr>
	<tr>
		<td>Cocaine</td>
		<td>20</td>
		<td>40</td>
		<td>100</td>
		<td>Finger 3-6 & Toe 10-14</td>
	</tr>
	<tr>
		<td>Cocaethylene</td>
		<td>10</td>
		<td>20</td>
		<td>50</td>
		<td>Finger 3-6 & Toe 10-14</td>
	</tr>
	<tr>
		<td>Benzoylecgonine</td>
		<td>10</td>
		<td>20</td>
		<td>50</td>
		<td>Finger 3-6 & Toe 10-14</td>
	</tr>
	<tr>
		<td>Norcocaine</td>
		<td>10</td>
		<td>20</td>
		<td>50</td>
		<td>Finger 3-6 & Toe 10-14</td>
	</tr>
	<tr>
		<td>6-MAM</td>
		<td>20</td>
		<td>40</td>
		<td>100</td>
		<td>Finger 3-6 & Toe 10-14</td>
	</tr>
	<tr>
		<td>Codeine</td>
		<td>20</td>
		<td>40</td>
		<td>100</td>
		<td>Finger 3-6 & Toe 10-14</td>
	</tr>
	<tr>
		<td>Hydrocodone</td>
		<td>20</td>
		<td>40</td>
		<td>100</td>
		<td>Finger 3-6 & Toe 10-14</td>
	</tr>
	<tr>
		<td>Hydromorphone</td>
		<td>20</td>
		<td>40</td>
		<td>100</td>
		<td>Finger 3-6 & Toe 10-14</td>
	</tr>
	<tr>
		<td>Morphine</td>
		<td>20</td>
		<td>40</td>
		<td>100</td>
		<td>Finger 3-6 & Toe 10-14</td>
	</tr>
	<tr>
		<td>Norhydrocodone</td>
		<td>8</td>
		<td>16</td>
		<td>40</td>
		<td>Finger 3-6 & Toe 10-14</td>
	</tr>
	<tr>
		<td>Oxycodone</td>
		<td>20</td>
		<td>40</td>
		<td>100</td>
		<td>Finger 3-6 & Toe 10-14</td>
	</tr>
	<tr>
		<td>Oxymorphone</td>
		<td>20</td>
		<td>40</td>
		<td>100</td>
		<td>Finger 3-6 & Toe 10-14</td>
	</tr>
	<tr>
		<td>Noroxycodone</td>
		<td>8</td>
		<td>16</td>
		<td>40</td>
		<td>Finger 3-6 & Toe 10-14</td>
	</tr>
	<tr>
		<td>Methadone</td>
		<td>20</td>
		<td>40</td>
		<td>100</td>
		<td>Finger 3-6 & Toe 10-14</td>
	</tr>
	<tr>
		<td>EDDP</td>
		<td>20</td>
		<td>40</td>
		<td>100</td>
		<td>Finger 3-6 & Toe 10-14</td>
	</tr>
	<tr>
		<td>Amobarbital</td>
		<td>80</td>
		<td>80</td>
		<td>200</td>
		<td>Finger 3-6 & Toe 10-14</td>
	</tr>
	<tr>
		<td>Butalbital</td>
		<td>80</td>
		<td>80</td>
		<td>200</td>
		<td>Finger 3-6 & Toe 10-14</td>
	</tr>
	<tr>
		<td>Pentobarbital</td>
		<td>80</td>
		<td>80</td>
		<td>200</td>
		<td>Finger 3-6 & Toe 10-14</td>
	</tr>
	<tr>
		<td>Phenobarbital</td>
		<td>80</td>
		<td>80</td>
		<td>200</td>
		<td>Finger 3-6 & Toe 10-14</td>
	</tr>
	<tr>
		<td>Secobarbital</td>
		<td>80</td>
		<td>80</td>
		<td>200</td>
		<td>Finger 3-6 & Toe 10-14</td>
	</tr>
	<tr>
		<td>Alprazolam</td>
		<td>20</td>
		<td>40</td>
		<td>100</td>
		<td>Finger 3-6 & Toe 10-14</td>
	</tr>
	<tr>
		<td>Diazepam</td>
		<td>20</td>
		<td>40</td>
		<td>100</td>
		<td>Finger 3-6 & Toe 10-14</td>
	</tr>
	<tr>
		<td>Midazolam</td>
		<td>20</td>
		<td>40</td>
		<td>100</td>
		<td>Finger 3-6 & Toe 10-14</td>
	</tr>
	<tr>
		<td>Nordiazepam</td>
		<td>20</td>
		<td>40</td>
		<td>100</td>
		<td>Finger 3-6 & Toe 10-14</td>
	</tr>
	<tr>
		<td>Oxazepam</td>
		<td>20</td>
		<td>40</td>
		<td>100</td>
		<td>Finger 3-6 & Toe 10-14</td>
	</tr>
	<tr>
		<td>Temazepam</td>
		<td>20</td>
		<td>40</td>
		<td>100</td>
		<td>Finger 3-6 & Toe 10-14</td>
	</tr>
	<tr>
		<td>Ketamine</td>
		<td>20</td>
		<td>40</td>
		<td>100</td>
		<td>Finger 3-6 & Toe 10-14</td>
	</tr>
	<tr>
		<td>Norketamine</td>
		<td>20</td>
		<td>40</td>
		<td>100</td>
		<td>Finger 3-6 & Toe 10-14</td>
	</tr>
	<tr>
		<td>Tramadol</td>
		<td>200</td>
		<td>400</td>
		<td>500</td>
		<td>Finger 3-6 & Toe 10-14</td>
	</tr>
	<tr>
		<td>Fentanyl</td>
		<td>2</td>
		<td>4</td>
		<td>10</td>
		<td>Finger 3-6 & Toe 10-14</td>
	</tr>
	<tr>
		<td>Norfentanyl</td>
		<td>2</td>
		<td>4</td>
		<td>10</td>
		<td>Finger 3-6 & Toe 10-14</td>
	</tr>
	<tr>
		<td>Alfentanil</td>
		<td>2</td>
		<td>4</td>
		<td>10</td>
		<td>Finger 3-6 & Toe 10-14</td>
	</tr>
	<tr>
		<td>Acetyl Fentanyl</td>
		<td>2</td>
		<td>4</td>
		<td>10</td>
		<td>Finger 3-6 & Toe 10-14</td>
	</tr>
	<tr>
		<td>Acetyl Norfentanyl</td>
		<td>2</td>
		<td>4</td>
		<td>10</td>
		<td>Finger 3-6 & Toe 10-14</td>
	</tr>
	<tr>
		<td>Sufentanil</td>
		<td>1</td>
		<td>2</td>
		<td>5</td>
		<td>Finger 3-6 & Toe 10-14</td>
	</tr>
	<tr>
		<td>Norsufentanil</td>
		<td>2</td>
		<td>2</td>
		<td>5</td>
		<td>Finger 3-6 & Toe 10-14</td>
	</tr>
	<tr>
		<td>Buprenorphine</td>
		<td>4</td>
		<td>8</td>
		<td>20</td>
		<td>Finger 3-6 & Toe 10-14</td>
	</tr>
	<tr>
		<td>Norbuprenorphine</td>
		<td>4</td>
		<td>8</td>
		<td>20</td>
		<td>Finger 3-6 & Toe 10-14</td>
	</tr>
	<tr>
		<td>Ethyl glucuronide</td>
		<td>4</td>
		<td>8</td>
		<td>20</td>
		<td>Finger 3 months <br /> Toe no consensus</td>
	</tr>
	<tr>
		<td>Nicotine</td>
		<td>20</td>
		<td>40</td>
		<td>100</td>
		<td>Finger 3-6 & Toe 10-14</td>
	</tr>
	<tr>
		<td>Cotinine</td>
		<td>20</td>
		<td>40</td>
		<td>100</td>
		<td>Finger 3-6 & Toe 10-14</td>
</tr>
</tbody>
</table>
<i>LOD: limit of detection; LOQ: limit of quantification: Cutoff concentration used to categorize metabolite as positive/negative</i>
</details>

<details>
  <summary>Table 2. Sample-Data Dictionary Nail Assays</summary>
  <br>
  <table class="docutils">
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
		<td style="width: 180px; word-wrap: break-word; white-space: normal;">Weight of nails available to assay</td>
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
		<td style="width: 180px; word-wrap: break-word; white-space: normal;">1: custom 14 panel test<br />2: Only enough to run EtG<br />3: Canceled because we could not run anything (no results generated)</td>
	</tr>
	<tr>
		<td>c_any_specimen_n</td>
		<td style="width: 180px; word-wrap: break-word; white-space: normal;">Specimen level result (positive for any analyte in confirmatory tests)</td>
		<td>Categorical</td>
		<td>1: positive<br />0: negative<br />3: QNS</td>
	</tr>
	<tr>
		<td>c_any_stim_n</td>
		<td style="width: 180px; word-wrap: break-word; white-space: normal;">Any stimulants in nails (based on confirmatory results for amphetamine, methamptheamine, MDM, MDA, MDEA)</td>
		<td>Categorical</td>
		<td>1: positive<br />0: negative<br />3: QNS</td>
	</tr>
	<tr>
		<td>s_amp_n</td>
		<td style="width: 180px; word-wrap: break-word; white-space: normal;">Screening test in nails: amphetamine/MDA dual test (amp/mamp)</td>
		<td>Categorical</td>
		<td>1: positive<br />0: negative<br />3: QNS</td>
	</tr>
	<tr>
		<td>s_mamp_n</td>
		<td style="width: 180px; word-wrap: break-word; white-space: normal;">Screening test in nails: methamphetamine/MDMA dual test (amp/mamp)</td>
		<td>Categorical</td>
		<td>1: positive<br />0: negative<br />3: QNS</td>
	</tr>
	<tr>
		<td>c_amp_n_cat</td>
		<td style="width: 180px; word-wrap: break-word; white-space: normal;">Confirmatory test in nails: amphetamine (categorical) (amp/mamp)</td>
		<td>Categorical</td>
		<td>1: positive<br />0: negative<br />3: QNS<br />4: screen negative</td>
	</tr>
	<tr>
		<td>c_amp_n</td>
		<td style="width: 180px; word-wrap: break-word; white-space: normal;">Confirmatory test in nails: amphetamine (amp/mamp)</td>
		<td>Continuous</td>
		<td>concentration value; -999</td>
	</tr>
</tbody>
</table>
</details>

<details>
  <summary>Table 3. Mapping from Class to Screening Tests and Confirmatory Tests for Nails</summary>
  <br>
  <table class="docutils">
    <thead>
      <tr>
		<th>Class</th>
		<th>Screening test</th>
		<th>Confirmatory Test<br />(reflexes from positive screening test)</th>
	   </tr>
	</thead>
	<tbody>
	<tr>
	<tr>
		<td colspan="1" rowspan="9">
			<div>Stimulant <br /> (c_any_stim_n)</div>
		</td>
		<td colspan="1" rowspan="5">
			<div>amp/mamp <br /> (s_amp_n, s_mamp_n)</div>
		</td>
		<td>Amphetamine (c_amp_n)</td>
	</tr>
	<tr>
		<td>Methamphetamine (c_meth_n)</td>
	</tr>
	<tr>
		<td>MDMA (c_mdma_n)</td>
	</tr>
	<tr>
		<td>MDA (c_mda_n)</td>
	</tr>
	<tr>
		<td>MDEA (c_mdea_n)</td>
	</tr>
	<tr>
		<td colspan="1" rowspan="4">
			<div>coc <br /> (s_coc_n)</div>
		</td>
		<td>Cocaine (c_coc_n)</td>
	</tr>
	<tr>
		<td>Cocaethylene (c_cocae_n)</td>
	</tr>
	<tr>
		<td>Benzoylecgonine (c_ben_n)</td>
	</tr>
	<tr>
		<td>Norcocaine (c_ncoc_n)</td>
	</tr>
	<tr>
		<td>Cannabinoid<br />(c_any_cannabinoid_n)</td>
		<td>thc <br /> (s_thc_n)</td>
		<td>Carboxy-delta-9-THC (c_delta-9-THC_n)</td>
	</tr>
	<tr>
		<td colspan="1" rowspan="5">
			<div>Barbiturate <br /> (c_any_barb_n)</div>
		</td>
		<td colspan="1" rowspan="5">
			<div>bar <br /> (s_bar_n)</div>
		</td>
		<td>Amobarbital (c_amobarb_n)</td>
	</tr>
	<tr>
		<td>Secobarbital (c_secobarb_n)</td>
	</tr>
	<tr>
		<td>Pentobarbital (c_pentobarb_n)</td>
	</tr>
	<tr>
		<td>Phenobarbital (c_phenobarb_n)</td>
	</tr>
	<tr>
		<td>Butalbital (c_butalbital_n)</td>
	</tr>
	<tr>
		<td colspan="1" rowspan="6">
			<div>Benzodiazepine<br />(c_any_benzo_n)</div>
		</td>
		<td colspan="1" rowspan="6">
			<div>benz <br /> (s_benz_n)</div>
		</td>
		<td>Diazepam (c_diaz_n)</td>
	</tr>
	<tr>
		<td>Oxazepam (c_oxaz_n)</td>
	</tr>
	<tr>
		<td>Nordiazepam (c_nord_n)</td>
	</tr>
	<tr>
		<td>Temazepam (c_tema_n)</td>
	</tr>
	<tr>
		<td>Midazolam (c_mida_n)</td>
	</tr>
	<tr>
		<td>Alprazolam (c_alpa_n)</td>
	</tr>
	<tr>
		<td colspan="1" rowspan="21">
			<div>Opioids<br /> (c_any_opioid_n)</div>
		</td>
		<td colspan="1" rowspan="6">
			<div>opi <br /> (s_opi_n)</div>
		</td>
		<td>Codeine (c_cod_n)</td>
	</tr>
	<tr>
		<td>Morphine (c_mor_n)</td>
	</tr>
	<tr>
		<td>MAM (c_mam_n)</td>
	</tr>
	<tr>
		<td>Hydrocodone (c_hydroc_n)</td>
	</tr>
	<tr>
		<td>Norhydrocodone (c_norh_n)</td>
	</tr>
	<tr>
		<td>Hydromorphone (c_hydrom_n)</td>
	</tr>
	<tr>
		<td colspan="1" rowspan="2">
			<div>mtd <br /> (s_mtd_n)</div>
		</td>
		<td>Methadone (c_mtd_n)</td>
	</tr>
	<tr>
		<td>EDDP (c_eddp_n)</td>
	</tr>
	<tr>
		<td colspan="1" rowspan="3">
			<div>oxyc <br /> (s_oxyc_n)</div>
		</td>
		<td>Oxycodone (c_oxyc_n)</td>
	</tr>
	<tr>
		<td>Noroxycodone (c_noxyc_n)</td>
	</tr>
	<tr>
		<td>Oxymorphone (c_oxym_n)</td>
	</tr>
	<tr>
		<td>tram <br /> (s_tram_n)</td>
		<td>Tramadol (c_tram_n)</td>
	</tr>
	<tr>
		<td colspan="1" rowspan="4">
			<div>fent <br /> (s_fent_n)</div>
		</td>
		<td>Fentanyl (c_fent_n)</td>
	</tr>
	<tr>
		<td>Norfentanyl (c_nfent_n)</td>
	</tr>
	<tr>
		<td>Acetylfentanyl (c_acfent_n)</td>
	</tr>
	<tr>
		<td>ActlNorfentanyl (c_acnfent_n)</td>
	</tr>
	<tr>
		<td colspan="1" rowspan="3">
			<div>suf <br /> (s_suf_n)</div>
		</td>
		<td>Alfentanil (c_afent_n)</td>
	</tr>
	<tr>
		<td>Sufentanil (c_suf_u)</td>
	</tr>
	<tr>
		<td>Norsufentanil (c_nsuf_n)</td>
	</tr>
	<tr>
		<td colspan="1" rowspan="2">
			<div>bup <br /> (s_bup_n)</div>
		</td>
		<td>Buprenorphine (c_bup_n)</td>
	</tr>
	<tr>
		<td>Norbuprenorpine (c_nbup_n)</td>
	</tr>
	<tr>
		<td colspan="1" rowspan="2">
			<div>dissociative anesthetic<br />(c_disanesth_n)</div>
		</td>
		<td colspan="1" rowspan="2">
			<div>ket <br /> (s_ket_n)</div>
		</td>
		<td>Ketamine (c_ket_n)</td>
	</tr>
	<tr>
		<td>Norketamine (c_nket_n)</td>
	</tr>
	<tr>
		<td colspan="1" rowspan="2">
			<div>Nicotine <br /> (c_nicotine_n)</div>
		</td>
		<td colspan="1" rowspan="2">
			<div>cot <br /> (s_cot_n)</div>
		</td>
		<td>Nicotine (c_nic_n)</td>
	</tr>
	<tr>
		<td>Cotinine (c_cot_n)</td>
	</tr>
	<tr>
		<td>Ethanol <br /> (c_ethanol_n)</td>
		<td>&nbsp;</td>
		<td>ethyl glucuronide (c_etoh_n)</td>
	</tr>
</tbody>
</table>
</details>

## Quality Control & Known Issues
QC procedures involved examining assay ranges and categorical versus continuous measures. No common issues were identified from QC.

One potential issue flagged by subject matter experts is that the nail processing workflow was re-developed and implemented on July 1, 2024 and thus data collected before that point will does not use the remnant of ELISA extract for confirmation for specimens with too little sample.

<details class="collapsible references">
  <summary class="references">References</summary>
 <ul>
    <p>Bandoli, G., Anunziata, F., Bogdan, R., Zilverstand, A., Chaiyachati, B. H., Gurka, K. K., Sullivan, E., Croff, J., & Bakhireva, L. N. (2024). Assessment of substance exposures in nail clipping samples: A systematic review. <i>Drug and Alcohol Dependence</i>, 254, 111038. <a href="https://doi.org/10.1016/j.drugalcdep.2023.111038" target="_blank">https://doi.org/10.1016/j.drugalcdep.2023.111038</a></p>
  </ul>
</details>


 

