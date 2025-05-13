# Known Issues

### ⚠️ Blank Cells in PhenX Discrimination Survey
For the PhenX+ Discrimination survey, one of the multi-select questions (column `sed_bm_phx__discr.006`: *"What do you think is the main reason for these experiences? If more than one main reason, check all that apply."*) is blank for some participants. 

### ⚠️ Discrepancy Between Parquet & CSV Files
Empty string appears where there should be nulls.

### ⚠️ ICD Code Names/Labels Inconsistently Provided (Pregnancy & Infant Health)

In cases where ICD codes are provided, corresponding names/labels are sometimes not provided. This is a known issue to be fixed in future releases. In the meantime, users can consider existing packages to merge ICD labels in [Stata](https://www.stata.com/features/overview/icd/), [SAS](https://hcup-us.ahrq.gov/toolssoftware/ccsr/dxccsr.jsp), or [R](https://www.rdocumentation.org/packages/icd/versions/3.3).