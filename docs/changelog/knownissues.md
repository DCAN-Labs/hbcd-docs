# Known Issues

*The following issues will be corrected in a future data release:*

## General

### ⚠️ Discrepancy Between Parquet & CSV Files
Empty string appears where there should be nulls.


## Basic Demographics

### ⚠️ Duplicate Options for 'Mother Race' Variable
The variable 'Mother Race' (`sed_basic_demographics_screen_mother_race`) has duplicate options for the selection of 'Black African American' (option #3). This option is not used for data entry, and instead the 'Black_or African American' option (option #5) should be used. No other variables are affected by this.

### ⚠️ Mother Ethnicity
The variable `screen_mother_ethnicity` should be a 2-level variable, however it is currently noted as a 4-level variable in the data dictionary. Levels of 0 and 1 (in the data dictionary) are included in error, they do not appear in the dataset; all participants with valid data have a value of 2 (Hispanic) or 3 (non-Hispanic). 


## Electroencephalography (EEG)
### ⚠️ MADE Resting-State Derivatives
The summary statistics for the MADE resting-state EEG data contained in the file `sub-<label>_ses-<label>_task-RS_powerSummaryStats.csv` are currently incorrect due to a bug in the pipeline.


## Neurocognition & Language
### ⚠️ SPM-2 T-Scores
The t-scores are currently missing as the original conversion from raw score to t-score was incorrect. The t-scores will be corrected in a future data release. In the meantime, users can calculate their own t-scores using the raw scores and the SPM-2 manual, which is available [here](https://www.mhs.com/MHS-Assessment?prodname=spm2).



## Pregnancy & Exposure, Including Substance Use
### ⚠️ APA Score Fields
TO DO

### ⚠️ ICD Code Names/Labels Inconsistently Provided (Pregnancy & Infant Health)
In cases where ICD codes are provided, corresponding names/labels are sometimes not provided. This is a known issue to be fixed in future releases. In the meantime, users can consider existing packages to merge ICD labels in [Stata](https://www.stata.com/features/overview/icd/), [SAS](https://hcup-us.ahrq.gov/toolssoftware/ccsr/dxccsr.jsp), or [R](https://www.rdocumentation.org/packages/icd/versions/3.3).


## Social & Environmental Determinants
### ⚠️ Blank Cells in PhenX Discrimination Survey
For the PhenX+ Discrimination survey, one of the multi-select questions (column `sed_bm_phx__discr.006`: *"What do you think is the main reason for these experiences? If more than one main reason, check all that apply."*) is blank for some participants. 


## Visit Information

### ⚠️ Invalid Participant Withdrawal Dates for Participants Who Did Not Withdraw
Particpants who have “no” for `par_visit_data_participant_withdrawal` systematically have a withdrawal date of 12/26/1999 for 
`par_visit_data_participant_withdrawal_date`. Participants who have “yes” for `par_visit_data_participant_withdrawal` have a valid date and are unimpacted.


### ⚠️ Missing Substance Use Flags 
The substance use flags found in the Visit Information data are single summary variables to reflect substance use status (yes/no) based on any positive reports from the (1) Timeline Follow Back (self-report), (2) Healthy History (V02) (self-report), or (3) USDTL urine toxicology results. Nail toxicology results were not used in the creation of these substance use flags. Further, the substance use flag variable is missing for alcohol, opioid, cannabis, and nicotine, and will be integrated in future data releases. In the meantime, users can generate their own substance use flag summary variables using the individual components found in the “pregnancy exposures, including substances” and “biospecimens” domains.
