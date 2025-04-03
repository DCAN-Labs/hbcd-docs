


Within LORIS, most protocol elements are created using a naming scheme whereby the instrument name will contain the following structure for domain_source_acronym/abbreviation:

* **'domain':** General domain to which the protocol element is related. Aligns with the Workgroup’s purview under which the given element is scoped.  
* **'source':** Who the protocol element is about. In some cases this may be more broadly applied as the 'Recipient' or 'Respondent.'  
* **'acronym/abbreviation':** The acronym or abbreviation for a given protocol element.

The options for the domain and source are as follows:  
**domain:**

* bio = Biospecimens  
* mh = Behavior/Child-Caregiver Interaction  
* sed = Social/Environmental Health Determinants  
* sens = Biosensor  
* ph = Physical Health  
* ncl = Neurocognition and Language  
* nt = Novel Tech  
* sed = Social/Environmental Health Determinants  
* eeg = EEG  
* mri = MRI  


## **Info ~ source also being tracked in data dictionary**

The 'domain' and 'source' are also included in the json metadata, parsed in most cases based on the corresponding 'domain' and 'source’ sections of the instrument name. In a few cases, the data is obtained directly into fields or tables that are not set up to follow the naming scheme, so the 'domain' and 'source' are added at a later step in the Data Release process. These would be:

* BioSpecimens  
* Imaging file based data & derivatives  
* Geocoding data coming from Ripple (Not yet imported into LORIS)  
* Some session level Ripple elements (e.g. 'informantID')  
* Participant level data

For the Ripple data, some of this is being syphoned into the 'Demographics Screener' (adm_bm_screen) form, so these would have a 'domain' and 'source', but other session and participant level data is directly imported into tables in the backend and do not have these attributes.

Imaging derivatives would not have these naming schemes, but are generally understood to be under the MRI/EEG domain and strictly for the 'Child'.  
Geocoding data has two forms in LORIS:

* 'Geocoded Linkage from Home and Work Addresses' (sed_ld_hm) '  
* 'PhenX+ Neighborhood Safety/ Geocode' (sed_bm_nbhsaf).

The Geocoded Linkage is currently not being collected, and the 'PhenX+ Neighborhood Safety' is collected at V01, V02 and V05, but only collects 3 fields (I feel safe walking in my neighborhood, day or night; Violence is not a problem in my neighborhood; My neighborhood is safe from crime).

In addition, we have three fields set for import of data via ETL, for which we would get data directly from the WG, presumably from data collected in Ripple for Geocoding. These are in the 'Demographics', and are:

* address_completeness  
* address_present  
* sufficient_coverage

Currently the fields exist, but no data has been set up or imported.

## **Informant ID**

The 'informant ID' can be construed in several ways, the main being:  
**'cohort':**

* The 'cohort' field indirectly informs the alternative caregiver (ACG) and presumably the informant for the visit. This is set by ETL when the visit is being created.  
* The 'cohort' field is currently included in the 'Visit Data' (par_visit_data). 

In addition, the other fields for the informant would be as follows:  
**'informantID':**

* Provided at the instrument level  
* Options:  
  * Null  
  * Parent  
  * Other Parent (Biological, adoptive, step-)  
  * Foster parent (child welfare or foster care)  
  * Grandmother or Grandfather (or great grandparent)  
  * Other family member  
  * Non-family member (fictive kin or friend)  
  * Other

This field only exists in the backend and is set to 'Null' by default, only to be modified if requested by sites via Issue Tracker tickets.  
There are 3 backend fields related to the informant at the session level to be imported from Ripple:  
**Informant_pscid:**

* Open text

This field exists in the backend and would receive the informant's pscid from Ripple.

**Informant_identity_legal_guardian:**

* Options:  
  * Parent  
  * State/Foster care system  
  * Grandmother or Grandfather (or great grandparent)  
  * Other family member (sibling)  
  * Non-family member (fictive kin, friend of the family or friend)  
  * Other

**informant_identity_living_with_now:**

* Options:  
  * Parent  
  * Other Parent (Biological, adoptive, step-)  
  * Foster parent (child welfare or foster care)  
  * Grandmother or Grandfather (or great grandparent)  
  * Other family member  
  * Non-family member (fictive kin or friend)  
  * Other

The above 3 fields are all at the sessions level and stored in the LORIS backend. These are to be imported via ETL, with the import currently being set up.  
For the time being, the WG will take 'Other' as a general category. If later this category is too large, they may decide on some additional set descriptors for the 'Other' category, at which point, either additional options or an additional field can be added.  
