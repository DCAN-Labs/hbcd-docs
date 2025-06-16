# Known Issues
The following issues have been identified in the current HBCD data release. **We are actively working to address them and will include fixes in either the patch (Release 1.1) or next Release 2.0 unless stated otherwise**. This page will be updated as new issues are discovered. If you have questions or would like to report an issue, please submit a ticket through the [Lasso Help Center](https://nbdc-datashare.lassoinformatics.com/help-center).

## General

##### ⚠️ Instruction Metadata - Caution, Please Read Carefully

Instruction text in the form's metadata is extracted programmatically from the most recent instruction field in the REDCap Data Dictionary for each form, based on field order. This means:

*   If an instruction spans multiple fields, only the last portion will be captured, resulting in partial instructions.
*   Because the instruction is provided for all fields up to the next set of instructions, some fields may display text intended for a previous section.
*   Manual curation of instruction metadata is planned for future releases. For the most accurate information, always refer to the original form.       

**Expected Fix:** Release 1.1  


## Basic Demographics
##### ⚠️ Duplicate Options for 'Mother Race' Variable
The variable 'Mother Race' (`sed_basic_demographics_screen_mother_race`) has duplicate options for the selection of 'Black African American' (option #3). This option is not used for data entry, and instead the 'Black_or African American' option (option #5) should be used. No other variables are affected by this.       
**Expected Fix:** Release 1.1    

##### ⚠️ Mother Ethnicity
The variable `screen_mother_ethnicity` should be a 2-level variable, however it is currently noted as a 4-level variable in the data dictionary. Levels of 0 and 1 (in the data dictionary) are included in error, they do not appear in the dataset; all participants with valid data have a value of 2 (Hispanic) or 3 (non-Hispanic).        
**Expected Fix:** Release 1.1    

## Biospecimens

##### ⚠️ Nails & Urine: Collection & Analysis Dates Currently Missing
Collection dates and analysis dates for Nails and Urine are not provided in the current release and will be provided in the future.            
**Expected Fix:** Release 1.1

##### ⚠️ Urine: Incorrect Specific Gravity Variable
The urine specific gravity variable is incorrect (`bio_bm_biosample_urine_bio_spg_u`); do not analyze this variable. There are several participants with “1”. This variable should be expressed in the thousands and will be corrected in the next release.     
**Expected Fix:** Release 1.1

##### ⚠️ Urine Toxicology (Cotinine)
There may be negative values for urinary toxicology results (e.g. `bio_bm_biosample_urine_bio_bm_biosample_urine_bio_c_cot_u`). Please note that negative values for these variables are not biologically plausible. We recommend users convert these values to 0 prior to analyzing their data.        
**Expected Fix:** Release 1.1

##### ⚠️ Negative Gestational Ages 
There are two participants with negative gestational ages in the urine biosample dataset due to inaccurate collection dates of the biosample. Please do not include these two observations in your analysis.        
**Expected Fix:** Release 1.1

## Electroencephalography (EEG)
##### ⚠️ HBCD-MADE Resting-State Derivatives
The HBCD-MADE summary statistics for resting-state EEG data contained in the derivative file `processed_data/*_task-RS_powerSummaryStats.csv` (see HBCD-MADE derivatives structure [here](../datacuration/derivatives.md#hbcd-made-made) for details) are incorrect due to a former bug in the pipeline and should not be used for analysis. Users should instead generate these files themselves using scripts provided via [HBCD EEG Utilities](https://hbcd-eeg-utilities.readthedocs.io/en/stable/) for extracting summary statistics.      
**Expected Fix:** Release 1.1

## Neurocognition & Language
##### ⚠️ SPM-2 T-Scores
The t-scores are currently not provided, as the original conversion from raw score to t-score was incorrect. The t-scores will be corrected and provided in a future data release.      
**Expected Fix:** Release 1.1

## Pregnancy & Exposure, Including Substance Use
##### ⚠️ Pregnancy Exposures, Including Substances (APA Level 2)
Individual items for Level 1 and Level 2 domains are provided, but summary scores and corresponding t-scores are not provided for Level 1 Sleep or any Level 2 domains. This will be corrected in a future release. In the meantime, users can calculate their own summary scores and convert them to t-scores based on the user [documentation](../instruments/pregexp/mh/apa12.md) provided for this measure.        
**Expected Fix:** Release 1.1

##### ⚠️ ICD Code Names/Labels Inconsistently Provided (Pregnancy & Infant Health)
In cases where ICD codes are provided, corresponding names/labels are sometimes not provided. This is a known issue to be fixed in future releases. In the meantime, users can consider existing packages to merge ICD labels in [Stata](https://www.stata.com/features/overview/icd/), [SAS](https://hcup-us.ahrq.gov/toolssoftware/ccsr/dxccsr.jsp), or [R](https://www.rdocumentation.org/packages/icd/versions/3.3).        
**Expected Fix:** Release 1.1

##### ⚠️ Infant Health Check 

The following fields are 'Descriptive' fields and should have been excluded. They will be removed in a future release:

- `pex_bm_healthv2_inf_001__00`
- `pex_bm_healthv2_inf_002__00`
- `pex_bm_healthv2_inf_003__00`
- `pex_bm_healthv2_inf_004__00`
- `pex_bm_healthv2_inf_005__00`

**Expected Fix:** Release 1.1

##### ⚠️ PEX (TLFB Substance Use Flags)
The TLFB Substance Use Flags are intended to indicate whether a participant had **ever met the substance-specific use criteria** during or after pregnancy across visits V01 and V02 at the time of survey administration. Currently, **only the alcohol use flag** correctly follows this logic. All other substance use flags are incorrect and will be corrected in a future release. In the meantime, users can derive their own substance use flag variables by applying “or” logic to determine whether the participant met the substance-specific criteria in **either** V01 or V02.     
**Expected Fix:** Release 1.1


##### ⚠️ Edinburgh Postnatal Depression Scale (EPDS)
Users should be aware that each item for the EPDS is duplicated (for example, `epds_001` and `epds_001_01`); these duplicate columns contain the same data. Duplicate data will be removed in the future.           
**Expected fix:** Release 1.1

## Social & Environmental Determinants
##### ⚠️ Blank Cells in PhenX Discrimination Survey
For the PhenX+ Discrimination survey, one of the multi-select questions (column `sed_bm_phx__discr.006`: *"What do you think is the main reason for these experiences? If more than one main reason, check all that apply."*) is blank for some participants.       
**Expected Fix:** Release 1.1

## Visit Information
##### ⚠️ Invalid Participant Withdrawal Dates for Participants Who Did Not Withdraw
Participants who have “no” for `par_visit_data_participant_withdrawal` systematically have a withdrawal date of 12/26/1999 for 
`par_visit_data_participant_withdrawal_date`. Participants who have “yes” for `par_visit_data_participant_withdrawal` have a valid date and are unimpacted.     
**Expected Fix:** Release 1.1

##### ⚠️ Missing Substance Use Flags 
The substance use flags found in the Visit Information data are single summary variables to reflect substance use status (yes/no) based on any positive reports from the (1) Timeline Follow Back (self-report), (2) Healthy History (V02) (self-report), or (3) USDTL urine toxicology results. Nail toxicology results were not used in the creation of these substance use flags. Further, the substance use flag variable is missing for alcohol, opioid, cannabis, and nicotine, and will be integrated in future data releases. In the meantime, users can generate their own substance use flag summary variables using the individual components found in the “pregnancy exposures, including substances” and “biospecimens” domains.       
**Expected Fix:** Release 1.1
