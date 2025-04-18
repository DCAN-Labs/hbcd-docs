# HBCD Study Design

## Study Design Logic: Child-Centric Data Structure
The data structure in the HBCD Study, as designed by the HBCD Data Core, is intentionally organized with Child ID as the central key. Data provided by caregivers (e.g., biological mother, other caregivers) is also nested under the corresponding Child ID.

### Rationale
The primary goal of the HBCD Study is to support longitudinal analyses of child development. By anchoring all data, including caregiver-reported measures, to the Child ID:

1. **Child-focused analysis is streamlined:** Researchers can easily conduct longitudinal analyses of individual children without needing to re-map caregiver data.

2. **Multi-birth (twins, triplets etc..) participants** are handled more effectively: In cases where one caregiver reports on multiple children (e.g., twins), the data remains clearly associated with each child, eliminating the need for complex joins or disambiguation steps.

3. **Flexible informant tracking**: While the initial release (r1.0) may not include informant IDs, future versions will. The informant ID will provide additional detail at the participant/event level, enabling users to identify which caregiver provided data and to track any caregiver changes over time.

### Additional Notes

1. Each variable includes "source" metadata in the data dictionary, specifying who provided the data (e.g., “Biological Mother", "Caregiver (Responsible Adult)", "Child", etc.) - see [Instrument File Naming Conventions](../../datacuration/phenotypes/#instrument-file-naming-conventions) for details.

2. The standardized variable and table naming conventions also incorporate this source information. 

3. While users will (in releases after 1.0) have the option to re-organize the data by informant ID if preferred, organizing by Child ID ensures maximum utility for the most common use case: analyzing child outcomes over time.
