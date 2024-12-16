# Phenotypes Data Curation & BIDS Conversion

## Data Structure & File Contents

The data structure of the phenotypic data is as follows:
```
assembly_bids/ 
|__ participants.tsv
|__ participants.json 
|__ sub-<label>/
|   |__ sub-<label>_sessions.tsv
|   |__ sub-<label>_sessions.json
|   |__ ses-<label>/
|       |__ phenotype/
|       |   |__ biosample_urine.tsv
|       |   |__ biosample_urine.json
|       |   |__ sed_basic_demographics.tsv
|       |   |__ sed_basic_demographics.json
|       |   |__ visit_data.tsv
|       |   |__ visit_data.json
|       |   |__ <instrument_name>.tsv (repeat for all selected instruments)
|       |   |__ <instrument_name>.json (repeat for all selected instruments)
```

**USDTL urine results files** (`biosample_urine.tsv|json`): include BioSpecimen results fields such as DCCID, Visit Label, and Scannable code.

**Instrument files** (`<instrument_name>.tsv|json`): each instrument has a `.tsv` Data Table containing all instrument values for the participants and a `.json` Data Dictionary describing all instrument fields (except those in the exclusion lists provided below). 

**Visit data** (`visit_data.tsv|json`): include visit information fields (e.g. Label, Stage, Date, and if the visit was missed or participant withdrew and the reason), Project, Cohort, and Site. These files also contain Substance Use (SU) flags from three locations ([TLFB](../measures/pregexp/substanceuse_all.md), [Health V2](../measures/pregexp/infanthealth.md), and [Biosample Urine](../measures/biospecimens/urine.md))

**Demographics files** (`sed_basic_demographics.tsv|json`): include demographics of the infant/child (gestational age at birth, sex, recruitment site, race, ethnicity) and mother (race, ethnicity, education, income, language spoken at home). These files also contain information about substance abuse. This includes flags raised for SU (from self-reported use (TLFB) and/or biospecimen results) and the Health-V2 instrument *pex_bm_healthv2_inf* (field “007”) if option 1 (NOWS - Neonatal Opioid Withdrawal Syndrome) or 5 (FAS - Fetal Alcohol Syndrome) was selected.


## Excluded Elements & General Rules
Below is a list of static elements (i.e. precisely identified hard-coded elements such as participants, instruments, and instrument fields) and dynamic elements excluded during the data release process as well as general rules applied to all data:


<p>
<div id="notification-banner" class="notification-banner" onclick="toggleCollapse(this)">
    <span class="text">Static Element Exclusions</span>
  <span class="notification-arrow">▸</span>
</div>
<div class="notification-collapsible-content">
<br>
<b>Participant Filters:</b>
<ul>
    <li>Participants with a 'Postnatal Recruitment' visit  </li>
    <li>Multiple Birth Participants</li>
</ul>

<b>Excluded Instruments:</b>
<ul>
    <li>Biosensor Receipt Form ('sens_ch_rcpt')</li>
    <li>EEG Acquisition Checklists
    <ul>
        <li>Form ('eeg_ch_chkl')</li>
        <li>Form Reattempt - 1 ('eeg_ch_chkl_1')</li>
        <li>Form Reattempt - 2 ('eeg_ch_chkl_2')</li>
    </ul>
    <li>GABI Setup/Receipt
        <ul>
        <li>'nt_pa_gabi_setup'  </li>
        <li>'nt_pa_gabi_rcpt'  </li>
        </ul>
    </li>
    <li>ERICA forms
        <ul>
        <li>'mh_cg_erica_3_7m'  </li>
        <li>'mh_cg_erica_7_9m'  </li>
        <li>'mh_cg_erica_fcm_adm_3_7m'  </li>
        <li>'mh_cg_erica_fcm_adm_7_9m'  </li>
        </ul>
    </li>
    <li>MRI Checklists
        <ul>
        <li>Data Summary Form ('mri_ra_chkl_data')  </li>
        <li>Scan Session Summary Form ('mri_ra_chkl_scan')  </li>
        </ul>
    </li>
    <li>MRI Pre/Post Scan Prep ('mri_ra_prep')</li>
    <li>NIH Baby ToolBox ('ncl_ch_nbtb')</li>
    <li>Participant Feedback Form ('adm_cg_fb')</li>
    <li>RA Feedback ('adm_ra_fb')</li>
    <li>Participant Alerts ('admin_alert')</li>
    <li>TLFB (Timeline Follow Back) Summary Parser ('pex_ch_tlfb')</li>
    <li>Visit Level Data ('adm_fd_visitdata')</li>
    <li>Visit start ('visit_start')</li>
    <li>Urgent Events ('adm_fd_urgent')</li>
    <li>Transitions in Care Questionnaire ('sed_cg_tic')</li>
</ul>

<br><b>Excluded Instrument Fields:</b>
<ul>
    <li>Examiner ('Examiner’)  </li>
    <li>Date of Birth (‘DOB’)  </li>
    <li>Informant (‘informant’)  </li>
    <li>Validity (‘validity’)  </li>
    <li>Duration (‘duration’)  </li>
    <li>Window Difference (‘window_difference’)  </li>
    <li>Start timestamp (‘timestamp_start’)  </li>
    <li>Stop timestamp (‘timestamp_stop’)  </li>
    <li>REDCap timestamp (‘timestamp_redcap_locked’)  </li>
    <li>Visit Data ('visit_stage' removed from the 'visit_data' category)  </li>
    <li>'Height/Weight/Head Circumference' ('ph_ch_anthro')
        <ul>
        <li>BMI-related fields removed  </li>
        </ul>
    </li>
    <li>Breast Feeding History ('ph_cg_phx_i_bfh')
        <ul>
        <li>All fields except '001' excluded  </li>
        </ul>
    </li>
    <li>Filter out extreme values for 'Height/Weight/Head Circumference' ('ph_ch_anthro')
        <ul>
        <li>Length ('len_001_i_03'): Min => 30 / Max => 130  </li>
        <li>Weight ('wei_001_i_03'): Min => 0.5 / Max => 30  </li>
        <li>Head Circumference ('head_001_i_03'): Min => 25 / Max => 55  </li>
        </ul>
    </li>
    <li>Clinical Alerts  </li>
    <li>REDCap Complete status ('complete')  </li>
    <li>Scannable codes (BioSamples codes, tracking Nos, etc...)  </li>
    <li>Line fields</li>
</ul>
</div>
</p>



<p>
<div id="notification-banner" class="notification-banner" onclick="toggleCollapse(this)">
    <span class="text">Dynamic Element Exclusions</span>
  <span class="notification-arrow">▸</span>
</div>
<div class="notification-collapsible-content">
</p>
<b>Participant Filters:</b>
<ul>
    <li>No brain rating or brain rating noted “abnormal” are not selected</li>
    <li>Only active participants and sessions are selected</li>
    <li>Participants from Data Coordination Center (DCC) and University of Florida (UFL) sites are not selected</li>
    <li>Only participants with PSCIDs starting with “CH” are selected (excluding all test participants e.g. QI, YI, XI, PI)</li>
</ul>

<b>Visit Filters:</b>
<ul>
    <li>Only visits whose 'LaunchPad Complete' Status was set to 'Complete' before July 1st, 2024 are included</li>
</ul>

<b>Domain Filters:</b>
<ul>
    <li>BioSpecimens</li>
    <li>Geocoding data</li>
    <li>Transition in Care</li>
    <li>REDCap surveys filled out directly in LORIS (Identified based on LORIS 'Examiner' field not set to 'REDCap')</li>
</ul>
</div>
</p>

<div id="notification-banner" class="notification-banner" onclick="toggleCollapse(this)">
    <span class="text">General Rules Applied to All Data</span>
  <span class="notification-arrow">▸</span>
</div>
<div class="notification-collapsible-content">
<p>
<ul>
    <li>All participants having only one active visit that is V01 will have their sex changed to “Other” instead of “Male” or “Female”</li>
    <li>All empty string “” or missing values will be replaced with the default ReproSchema-compliant string “n/a”</li>
    <li>For V01, all “Candidate_Age” values are replaced with “n/a”</li>
    <li>For other visits, “Candidate_Age” will be computed in years</li>
    <li>Some fields can have out of range values. They are considered “extreme” values and are changed to “n/a”. Filters apply to:
        <ul>
            <li>Pex Bm Healthv2 Inf (‘pex_bm_healthv2_inf’) instrument:
                <ul>
                    <li>Field “001_i_01”: higher than 16</li>
                    <li>Field “001_i_02”: higher than 66</li>
                    <li>Field “002”: outside of range 12-51</li>
                    <li>Field “002_i_01”: outside of range 30-130</li>
                </ul>
            </li>
        </ul>
    </li>
</ul>
</p>
</div><br>
