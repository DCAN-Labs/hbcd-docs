
# ReproSchema
## What is ReproSchema?
Ensuring consistency in research data collection is critical, especially in large-scale and multi-site studies like HBCD. However, tracking changes in questionnaires, maintaining structured formats, and ensuring version control across different time points can be challenging.

ReproSchema is a framework designed to address these challenges by providing a structured, standardized, and version-controlled system for managing research questionnaires. It is not a standalone survey tool like Qualtrics or REDCap. Instead, it is a modular framework that integrates with data collection systems, providing a structured backbone to reduce inconsistencies in questionnaire administration, improve data traceability, and ensure reproducibility in longitudinal research. ReproSchema functions as both a **schema** and **software platform**:

**As a schema**, ReproSchema defines a common structured format for organizing questionnaires, ensuring consistency regardless of where or when they are administered:

- Questionnaires are consistently formatted across different studies and time points.  
- Each question, response option, and skip pattern is clearly defined and linked to metadata.  
- Version history is preserved so researchers can track changes over time.

**As a platform**, it provides a set of tools to store, version, and track questionnaires, allowing researchers to:

- Store and version questionnaires to prevent discrepancies in multi-site studies.  
- Track and document changes, such as wording adjustments, adding or removing questions, or updating response options.  
- Access and compare different versions of a questionnaire used at any given time to understand how changes impact data collection. 

<div id="rs-example" class="notification-banner" onclick="toggleCollapse(this)">
    <span class="emoji"><i class="fa-regular fa-lightbulb"></i></span>
    <span class="text">Practical Example: Evolution of a Sleep Quality Question Across Data Releases</span>
    <span class="arrow">▸</span>
</div>
<div class="collapsible-content">
  <ul>
  <b>Release 1.0 (Initial Version):</b>
    <li><strong>Question:</strong> "How many hours do you sleep on a typical night?"</li>
    <li><strong>Response Options:</strong> Free-text input (participants enter a number).</li>
  </ul>
  <ul>
  <b>Release 2.0 (Revised Version):</b>
    <li><strong>Question:</strong> "On average, how many hours of sleep do you get per night?"</li>
    <li><strong>Response Options:</strong> Dropdown menu:
      <ul>
        <li>Less than 5 hours</li>
        <li>5-6 hours</li>
        <li>7-8 hours</li>
        <li>More than 8 hours</li>
      </ul>
    </li>
  </ul>
  <ul>
  <b>Release 3.0 (Further Revision):</b>
    <li><strong>Question:</strong> "On average, how many hours of sleep do you get in a 24-hour period, including naps?"</li>
    <li><strong>Response Options:</strong> Same as Release 2.0.</li>
  </ul>
  <hr> <!-- A subtle separator for better readability -->
  <ul>
  <b>Implications for Data Analysis:</b>
    <li><strong>Data Consistency:</strong> The shift from free-text to predefined categories (Release 1.0 → 2.0) standardizes responses, reducing variability but limiting detail.</li>
    <li><strong>Comparability:</strong> The addition of naps (Release 2.0 → 3.0) may impact cross-release trend analysis.</li>
    <li><strong>Data Harmonization:</strong> ReproSchema’s version management ensures that each change is documented for consistent longitudinal studies.</li>
  </ul>
</div>

## ReproSchema Workflow 

<figure>
  <img src="../images/reproschema-fig1.jpg" alt="ReproSchema Figure 1">
  <figcaption style="font-size: 0.9em;"><b>Figure 1. ReproSchema workflow overview.</b> This figure presents the ReproSchema workflow, which standardizes survey data collection to enhance research reproducibility and interoperability across studies. The workflow consists of six key components: <b>(A)</b> ReproSchema supports multiple input formats, including questionnaires in PDF or DOC format (which can be converted to ReproSchema format using large language models (LLMs), such as Claude 3.7 Sonnet, as demonstrated in the supplementary material), existing assessments from the ReproSchema library, and REDCap CSV exports (which can be automatically converted using redcap2reproschema). <b>(B)</b> The reproschema-protocol-cookiecutter tool provides a structured, stepwise process for researchers to create and publish a protocol on GitHub, ensuring organized metadata and version control. This tool enables schema validation and user interface (UI) serving. <b>(C)</b> ReproSchema protocols are stored in GitHub repositories (or other Git-compatible services), where version-controlled URIs ensure persistent access to protocols, activities, and assessment items, supporting reproducibility and provenance tracking. <b>(D)</b> The ReproSchema-UI provides a browser-based interface for interactive survey deployment, allowing researchers and participants to collect structured data while maintaining schema integrity. <b>(E)</b> Survey responses are stored in JSON-LD format, with embedded URIs linking each protocol, activity, and item to their respective sources in the ReproSchema library. This structure ensures data provenance, traceability, and semantic interoperability. <b>(F)</b> The reproschema-py tools facilitate output conversion into various standardized formats, including the National Institute of Mental Health (NIMH) Common Data Elements (reproschema2cde), the Brain Imaging Data Structure (BIDS) phenotype format (reproschema2bids), and REDCap CSV format (output2redcap), ensuring compatibility with existing research workflows.</figcaption>
</figure>

For more information about reproschema, please visit [https://www.repronim.org/reproschema/](https://www.repronim.org/reproschema/) or read [Chen et al., 2024](https://preprints.jmir.org/preprint/63343). 

## Overview of Version Management
In longitudinal studies like HBCD, where data is collected over extended periods, tracking every change in data collection instruments is vital. ReproSchema's systematic documentation allows researchers to:

- **Maintain Data Consistency**: By having a clear record of all modifications, researchers can ensure that data remains comparable across different time points.  
- **Enhance Data Reliability**: Understanding the history of changes helps in assessing the reliability of the data, as it provides context for any variations observed in the responses.  
- **Facilitate Transparent Reporting**: Comprehensive documentation supports transparent reporting of methodologies, which is essential for reproducibility and credibility in scientific research.

**Here's an overview of how ReproSchema handles various modifications:**

**Fixing Typographical Errors** – Ensures corrected versions are used in future data collection and allows for tracking the impact of the error on past data.    
**Adjusting Answer Choices** – Documents changes in options to ensure variations are considered during data analysis.    
**Modifying Question Order** – Tracks reordering to assess potential effects on responses, as the  sequence of questions can influence how respondents perceive and answer them.   
**Adding or Removing Questions** – Ensures structural changes are documented for accurate longitudinal analysis and data comparability.

## How ReproSchema Organizes Questionnaires
ReproSchema structures research questionnaires into three levels, making it easy to track, update, and maintain consistency in data collection over time.  

<figure>
  <img src="../images/reproschema-fig2.jpg" alt="ReproSchema Figure 1">
  <figcaption style="font-size: 0.9em;"><b>Figure 2. Mapping a research protocol to ReproSchema.</b> This figure illustrates how an assessment is structured and represented in ReproSchema, as well as how it appears in the user interface. The entire assessment (outlined in red) is an Activity. Each individual question (green) is an Item, and the available answer choices (purple) are ResponseOptions. When a participant selects an answer (orange), that selection is recorded as a Response. One protocol can have multiple activities. The right panel demonstrates how different Activities within a protocol are organized in the UI, allowing users to navigate between different activities.</figcaption>
</figure>

**Protocol Level: The Big Picture**  
At the highest level, a protocol represents the entire study’s questionnaire framework. It includes all assessments and surveys used in the research. Each protocol is tied to a specific data release, ensuring everything is version-controlled and well-documented. This structure helps researchers keep surveys consistent across different phases of a study.

**Activity Level: The Questionnaires**  
Within each protocol, the activity level includes individual questionnaires or assessments, such as the PHQ-9 (depression scale) or GAD-7 (anxiety scale). ReproSchema tracks changes at this level, including when assessments are added, removed, or modified. This tracking ensures that researchers can compare data across time while maintaining accuracy.

**Item Level: The Questions**  
The smallest unit in ReproSchema is an item, which refers to individual questions within a questionnaire. Each question is carefully tracked, including:

- Question Text: The exact wording of the question.  
- Response Options: The answer choices given to participants.  
- Skip Patterns: If certain answers lead to different follow-up questions.

Tracking these elements allows researchers to see when and how questions change, which is critical in studies that collect data over multiple years.

## Quick Start Guide for Researchers
In the HBCD Study, researchers collect data using REDCap, a web application for managing surveys and databases. To share and analyze this data, they convert it into the LORIS data dictionary format used for data releases. ReproSchema enables standardized and accurate transformation from REDCap to LORIS, ensuring questionnaire consistency and preserving data integrity across platforms and study phases.

### Accessing and Using Questionnaires
After obtaining access to the data (see instructions [here](../data_access/index.md)), researchers can easily access and compare questionnaires from the HBCD study by following these steps:

 - Each questionnaire includes a JSON file detailing its metadata, including version history.​ The metadata includes change logs detailing any modifications between versions.​
 - TO DO

## Tracking Change 
Need help? Open an issue on [GitHub](https://github.com/ReproNim/hbcd-loris2reproschema)

## References
<div class="references">
	<p>Chen Y, Jarecka D, Abraham SA, Gau R, Ng E, Low DM, Bevers I, Johnson A, Keshavan A, Klein A, Clucas J, Rosli Z, Hodge SM, Linkersdörfer J, Bartsch H, Das S, Fair D, Kennedy D, Ghosh SS. ReproSchema: Enhancing Research Reproducibility through Standardized Survey Data Collection. JMIR Preprints. 21/06/2024:63343. DOI: 10.2196/preprints.63343. URL: <a href="https://preprints.jmir.org/preprint/63343">https://preprints.jmir.org/preprint/63343</a></p> 
</div>
<br>