## Instrument File Naming Conventions
Geocoding data has two forms in LORIS:

* 'Geocoded Linkage from Home and Work Addresses' (sed_ld_hm) '  
* 'PhenX+ Neighborhood Safety/ Geocode' (sed_bm_nbhsaf).

The Geocoded Linkage is currently not being collected, and the 'PhenX+ Neighborhood Safety' is collected at V01, V02 and V05, but only collects 3 fields (I feel safe walking in my neighborhood, day or night; Violence is not a problem in my neighborhood; My neighborhood is safe from crime).

In addition, we have three fields set for import of data via ETL, for which we would get data directly from the WG, presumably from data collected in Ripple for Geocoding. These are in the 'Demographics', and are:

* address_completeness  
* address_present  
* sufficient_coverage

Currently the fields exist, but no data has been set up or imported.