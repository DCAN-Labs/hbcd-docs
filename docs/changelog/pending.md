# Pending & Upcoming Updates

## Pending Field Filters
* Brain Rating associated fields  
* Open text fields (Custom per instrument. Check on a case by case basis)  
* Fields in 'HBCD_Include_vs_not_Include' tab of the '[Internal Facing](https://docs.google.com/spreadsheets/d/1qKuhIvogkOCVg-lDk30WKd5tfF0xuy-ChubOBSqOYNQ/edit?gid=1013027810#gid=1013027810)' document  
* Implementation of the ‘Shadow Matrix’

## Upcoming Updates

**Upcoming - BR9:**

* Basic Demographics:  
    * Child Demographics (collected at V02 from Ripple) to be added to Basic Demographics  
    * ACS scoring for Maternal demographics (Screener from Ripple)  
    * All of Us scoring for Maternal demographics (REDCap surveys)  
    * Remove ‘rc_mother_ethnicity’ (Mother ethnicity field from REDCap)  
* ‘Parquet’ files - Set up for generation of Parquet files as additional output  
* Add ‘Unit’ information - Audit of 'Unit' fields & include 'Unit' information (Ongoing - case by case basis review)  
* BioSpecimen:   
    * Implement Data Dictionary elements into json metadata for USDTL results  
    * Include 'Nail Type'  
* EEG:  
    * Age in *sessions.tsv* computed based on ‘Visit Date’  
    * Age computed from custom ‘acq_time’ (extracted from the mff files) will be in *scans.tsv* (associated to each task file)
