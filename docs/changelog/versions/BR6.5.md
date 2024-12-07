# Version: BR6.5

<p style="font-size: 1.1em">Release date: November 5, 2024</p>

<ul>
<p style="font-size: 1.1em; margin-bottom: 0px;"><u>Total number of unique participants and visits included in data dump:</u></p>
<li>1,399 unique participants  </li>
<li>1,919 visits
<ul>
<li>V01 visits: 1,127 (185 participants for which only V01 visit exists)  </li>
<li>V02 visits: 666  </li>
<li>V03 visits: 126</li></ul>
</li>
</ul>

## New features

**MRI Derivative tabular data** - Included in 'Phenotype' folder (.tsv & .json)  

  * BibsNet: 2 file pairs (T1w; T2w)  
  * XCP-D: 90 file pairs  
  * OSPREY: 58 file pairs  
    * 26 Hercules  
    * 29 Unedited

## Filters

* Excluded:  
    * Informant (*‘informant’*)  
    * Validity (‘*validity’*)  
    * Duration (‘*duration’*)  
    * Window Difference (*‘window_difference’*)  
    * Line fields  
* Included:  
    * Date of Administration (*‘date_taken’*)

## Data Conversions

* Relabeled:  
    * BIDS metadata 'Description' header to 'label'  
    * All 'Visit' headers to 'session_id'  
    * BioSpecimen file header from 'Visit Label' to 'session_id'  
    * MRI Derivatives file header from 'visit' to 'session_id'

## Additional Notes

* Prepended:  
    * 'visit_data' category with 'par' (par_visit_data)  
* 'Administration' data now populating  
* Child demographic data available
