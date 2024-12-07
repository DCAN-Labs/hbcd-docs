# Version: BR6

<p style="font-size: 1.1em">Release date: October 30, 2024</p>

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

* Derived 'SU' flag variable has been populated in the 'Basic Demographics' category with a 'Yes'/'No' output based on meeting any of the following criteria:  
    * Self reported substance use (any SU flag on the TLFB)  
    * BioSpecimen results (any positive BioSpecimen result on the USDTL Urine results table)  
    * NOWS or FAS fields (Any positive response for these fields in the 'Health V2' form)  
* 'Child Demographics' - The following two placeholder entries included in the ‘basic_demographics’ category (Data should populate in future iterations once the data starts flowing into the LORIS database):  
    * 'child_race'  
    * 'child_ethnicity'   
* BioSpecimens: USDTL Urine BioSpecimen file included.   
    * Prepended with the 'bio' domain   
    * 'Visit label' added  
    * 111 entries excluded as no DCCID found for ‘specimen ID’

