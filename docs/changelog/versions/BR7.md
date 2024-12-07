# Version: BR7

<p style="font-size: 1.1em">Release date: November 12, 2024</p>

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

## New Features
<ul>
<b>MRI Derivative tabular data:</b> Included in 'Phenotype' folder (.tsv & .json)  
<li>'MADE: 5 file pairs (5 .stv & 5.json)  </li>
</ul>

## Filters

  * Visit Data  
    * 'visit_stage' removed from the 'visit_data' category  
  * 'Height/Weight/Head Circumference' (ph_ch_anthro)  
    * BMI related fields removed  
  * Breast Feeding History (ph_cg_phx_i_bfh)  
    * All fields except '001' excluded  
  * Filter out extreme values for 'Height/Weight/Head Circumference' (ph_ch_anthro)  
    * Length ('len_001_i_03')  
      * Min => 30 / Max => 130  
    * Weight ('wei_001_i_03')  
      * Min => 0.5 / Max => 30  
    * Head Circumference ('head_001_i_03')  
      * Min => 25 / Max => 55

## Data Conversions

* Label adjustments:  
    * All fieldnames forced to lower case  
* Typo fix:   
    * 'protocole' changed to 'protocol' in Data Dictionary  
* Replacement:  
    * Converted for field names and Data Dictionary 'LongName'  
        * All _i_ to __  
        * All leading i_ to leading _

## Other Features
* Added an exclusion mechanism for fieldnames on specific instruments
