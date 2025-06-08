# Known Issues
The following issues have been identified in the current HBCD data release. **We are actively working to address them and will include fixes in the next release unless stated otherwise**. This page will be updated as new issues are discovered.

If you have questions or would like to report an issue, please submit a ticket through the Lasso Help Center by following the steps described in the [Report Issues](../reportissue.md) section.

## General
##### ⚠️ Discrepancy Between Parquet & CSV Files
Empty string appears where there should be nulls.

## Basic Demographics
##### ⚠️ Duplicate Options for 'Mother Race' Variable
The variable 'Mother Race' (`sed_basic_demographics_screen_mother_race`) has duplicate options for the selection of 'Black African American' (option #3). This option is not used for data entry, and instead the 'Black_or African American' option (option #5) should be used. No other variables are affected by this.

##### ⚠️ Mother Ethnicity
The variable `screen_mother_ethnicity` should be a 2-level variable, however it is currently noted as a 4-level variable in the data dictionary. Levels of 0 and 1 (in the data dictionary) are included in error, they do not appear in the dataset; all participants with valid data have a value of 2 (Hispanic) or 3 (non-Hispanic). 

## Biospecimens

##### ⚠️ Urine: Incorrect Specific Gravity Variable
The urine specific gravity variable is incorrect (`bio_bm_biosample_urine_bio_spg_u`); do not analyze this variable. There are several participants with “1”. This variable should be expressed in the thousands and will be corrected in the next release.


##### ⚠️ Urine Toxicology (Cotinine)

There may be negative values for urinary toxicology results (e.g. `bio_bm_biosample_urine_bio_bm_biosample_urine_bio_c_cot_u`). Please note that negative values for these variables are not biologically plausible. We recommend users convert these values to 0 prior to analyzing their data.


##### ⚠️ Negative Gestational Ages 
 
There are two participants with negative gestational ages in the urine biosample dataset due to inaccurate collection dates of the biosample. Please do not include these two observations in your analysis. 


## Electroencephalography (EEG)
##### ⚠️ HBCD-MADE Resting-State Derivatives
The HBCD-MADE summary statistics for resting-state EEG data contained in the derivative file `processed_data/*_task-RS_powerSummaryStats.csv` (see HBCD-MADE derivatives structure [here](../datacuration/derivatives.md#hbcd-made-made) for details) are incorrect due to a former bug in the pipeline and should not be used for analysis. Users should instead generate these files themselves using scripts provided via [HBCD EEG Utilities](https://hbcd-eeg-utilities.readthedocs.io/en/stable/) for extracting summary statistics. 

## Neurocognition & Language
##### ⚠️ SPM-2 T-Scores
The t-scores are currently not provided, as the original conversion from raw score to t-score was incorrect. The t-scores will be corrected and provided in a future data release.


## Pregnancy & Exposure, Including Substance Use
##### ⚠️ APA Score Fields
TO DO

##### ⚠️ ICD Code Names/Labels Inconsistently Provided (Pregnancy & Infant Health)
In cases where ICD codes are provided, corresponding names/labels are sometimes not provided. This is a known issue to be fixed in future releases. In the meantime, users can consider existing packages to merge ICD labels in [Stata](https://www.stata.com/features/overview/icd/), [SAS](https://hcup-us.ahrq.gov/toolssoftware/ccsr/dxccsr.jsp), or [R](https://www.rdocumentation.org/packages/icd/versions/3.3).

##### ⚠️ Infant Health Check 
 TO DO


## Social & Environmental Determinants
##### ⚠️ Blank Cells in PhenX Discrimination Survey
For the PhenX+ Discrimination survey, one of the multi-select questions (column `sed_bm_phx__discr.006`: *"What do you think is the main reason for these experiences? If more than one main reason, check all that apply."*) is blank for some participants. 

## Tabulated MRI Data

##### ⚠️ BrainSwipes

There are 8 participant sessions with existing processed structural/functional outputs present in the XCP-D derivatives of the release data without corresponding [BrainSwipes](../measures/mri/qc.md#brainswipes) QC results include in the `img_brainswipes_xcpd-T2w` and `img_brainswipes_xcpd-bold` tables. These participants will be included in the next release in addition to BrainSwipes QC results for newly processed sessions. Users may perform visual inspection of the visual reports themselves to determine whether to include these data in their analyses by inspecting the `sub-<label>_ses-<label>_executive_summary.html` XCP-D derivatives file (see details [here](../datacuration/derivatives.md#xcp-d-xcp_d)). For guidance on how to perform visual inspection, create an account at [BrainSwipes](https://brainswipes.us) and review the tutorials provided for [surface delineation](https://brainswipes.us/tutorial/anat), [atlas registration](https://brainswipes.us/tutorial/atlas), and [functional registration](https://brainswipes.us/tutorial/func).

## Visit Information
##### ⚠️ Invalid Participant Withdrawal Dates for Participants Who Did Not Withdraw
Participants who have “no” for `par_visit_data_participant_withdrawal` systematically have a withdrawal date of 12/26/1999 for 
`par_visit_data_participant_withdrawal_date`. Participants who have “yes” for `par_visit_data_participant_withdrawal` have a valid date and are unimpacted.

##### ⚠️ Missing Substance Use Flags 
The substance use flags found in the Visit Information data are single summary variables to reflect substance use status (yes/no) based on any positive reports from the (1) Timeline Follow Back (self-report), (2) Healthy History (V02) (self-report), or (3) USDTL urine toxicology results. Nail toxicology results were not used in the creation of these substance use flags. Further, the substance use flag variable is missing for alcohol, opioid, cannabis, and nicotine, and will be integrated in future data releases. In the meantime, users can generate their own substance use flag summary variables using the individual components found in the “pregnancy exposures, including substances” and “biospecimens” domains.
