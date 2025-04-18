# HBCD Study Design & Conventions

## Study Design Logic: Child-Centric Data Structure
The data structure in the HBCD Study, as designed by the HBCD Data Core, is intentionally organized with Child ID as the central key. Data provided by caregivers (e.g., biological mother, other caregivers) is also nested under the corresponding Child ID.

### Rationale
The primary goal of the HBCD Study is to support longitudinal analyses of child development. By anchoring all data—including caregiver-reported measures—to the Child ID:

1. **Child-focused analysis is streamlined:** Researchers can easily conduct longitudinal analyses of individual children without needing to re-map caregiver data.

2. **Multi-birth (twins, triplets etc..) participants** are handled more effectively: In cases where one caregiver reports on multiple children (e.g., twins), the data remains clearly associated with each child, eliminating the need for complex joins or disambiguation steps.

3. **Flexible informant tracking**: While the initial release (v1.0) may not include informant IDs, future versions will. The informant ID will provide additional detail at the participant/event level, enabling users to identify which caregiver provided data and to track any caregiver changes over time.

### Additional Notes

1. Each variable includes "source" metadata in the data dictionary, specifying who provided the data (e.g., “Biological Mother", "Caregiver (Responsible Adult)", "Child", etc.).

2. The standardized variable and table naming conventions also incorporate this source information. 

3. While users will (in releases after 1.0) have the option to re-organize the data by informant ID if preferred, organizing by Child ID ensures maximum utility for the most common use case: analyzing child outcomes over time.

## Instrument File Naming Conventions
Most protocol elements follow a standardized naming convention with the structure: `domain_source_acronym`. Note that imaging derivatives do not follow this naming schemes, but are generally understood to be under the MRI, EEG, etc. domain and strictly for the 'Child.' Each component represents the following:

- **domain**: The general domain or category the protocol element falls under (e.g., biospecimens, MRI, behavior).
- **source**: Indicates who the protocol element is about or, in some cases, who completed the assessment. The source can represent either the *respondent* (who provided the information) or the *subject* (who the data is about).
For example, `mri_ra_prep` refers to MRI-related data entered by a research assistant (RA), representing procedural details as opposed to direct input from a child or caregiver.
- **acronym/abbreviation**: A short form or code representing the specific protocol element.


<div id="table-banner" class="table-banner" onclick="toggleCollapse(this)">
  <span class="text">Values for 'domain' and 'source' components</span>
  <span class="arrow">▸</span>
</div>
<div class="collapsible-content">
  <div style="display: flex; gap: 40px; flex-wrap: wrap;">
    <div>
      <p><strong>Possible values for <b>domain</b>:</strong></p>
      <ul>
        <li><code>bio</code> - Biospecimens</li>
        <li><code>mh</code> - Behavior/Child-Caregiver Interaction</li>
        <li><code>sed</code> - Social/Environmental Health Determinants</li>
        <li><code>sens</code> - Biosensor</li>
        <li><code>ph</code> - Physical Health</li>
        <li><code>ncl</code> - Neurocognition and Language</li>
        <li><code>nt</code> - Novel Tech</li>
        <li><code>eeg</code> - EEG</li>
        <li><code>mri</code> - MRI</li>
      </ul>
    </div>
    <div>
      <p><strong>Possible values for <b>source</b>:</strong></p>
      <ul>
        <li><code>ch</code> - Child</li>
        <li><code>bm</code> - Biological Mother</li>
        <li><code>si</code> - Sibling</li>
        <li><code>te</code> - Teacher</li>
        <li><code>cl</code> - Clinician</li>
        <li><code>ra</code> - RA (research assistant)</li>
        <li><code>ld</code> - Linked Data</li>
        <li><code>fd</code> - Family Data</li>
      </ul>
    </div>
  </div>
</div>

<div id="demo-age" class="notification-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fa-regular fa-lightbulb"></i></span>
  <span class="text">FYI: Correspondence to JSON Metadata</span>
  <span class="arrow">▸</span>
</div>
<div class="collapsible-content">
<p>The <code>domain</code> and <code>source</code> are also included in the JSON metadata and are typically derived from the corresponding sections of the instrument name. However, in some cases, data are collected directly into fields or tables that do not follow the standard naming convention. In those instances, the domain and source values are added later during the Data Release process.</p>
<strong>This applies to:</strong>
<ul>
<li>BioSpecimens  </li>
<li>Imaging file based data &amp; derivatives  </li>
<li>Some session-level elements (e.g. <code>informantID</code>)  </li>
<li>Participant-level data</li>
</ul>
</div>
