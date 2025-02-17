# Pending & Upcoming Updates

## Pending Field Filters

* Brain Rating associated fields  
* Open text fields (Custom per instrument. Check on a case by case basis)  
* Fields in 'HBCD_Include_vs_not_Include' tab of the [Internal Facing](https://docs.google.com/spreadsheets/d/1qKuhIvogkOCVg-lDk30WKd5tfF0xuy-ChubOBSqOYNQ/edit?gid=1013027810#gid=1013027810) document

## Upcoming - BR15

* Data Dictionary:  
    * Unexpected value for 'type_var' ('score' and 'admin') - Review  
    * Checkbox fields with no 'value' for 'levels'  
* ‘Parquet’ files - Parquet files for TLFB  
* Add ‘Unit’ information - Audit of 'Unit' fields & include 'Unit' information (Ongoing - case by case basis review)
* Remove 'user_completion' from TLFB (precise name: 'ph_ch_tlfb_tlfb_user_completion') 
* BR14 [Issue #1 - Incorrect Data: Height/Weight/Head Circumference (`ph_ch_anthro`)](versions/BR14.md#1-incorrect-data-heightweighthead-circumference-ph_ch_anthro) - is expected to be resolved 

### Pregnancy & Exposure
Instruments to be added:

- `pex_bm_psych`
- `sed_bm_bfy`

### EEG  
 * Exclude additional BIDS and derivative data for subjects flagged by EEG team

## Upcoming - Post-Release

* Shadow Matrix:  
  * Add logic to populate Shadow Matrix for:   
    * 'Blank' fields related to 'QC Flagged' cases (fields with validations)  
    * Blank' fields related to other 'QC Flagged' cases  
* Demographics:   
    * New bins for ‘levels’ for REDCap ‘Demographics’ (sed_bm_demo) fields (‘Education’ and ‘Income’)  
    * Child demographics - Multi Race options  
* BrainSwipes  
* Geocoding