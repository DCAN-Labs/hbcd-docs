# Processing & Analytic Software Standards

![](nmind.png)

HBCD pipeline developers, Workgroups, and community contributors who wish to integrate their tools into the HBCD release environment are expected to follow these guidelines to ensure standardization of HBCD software and documentation. These guidelines are rooted in principles and utilities developed by [NMIND](https://www.nmind.org/about) aimed at promoting reproducibility and standardization in neuroimaging tools ([Kiar et. al 2023](https://www.nature.com/articles/s41562-023-01647-0)). Among these is the [NMIND Coding Standards Checklist](https://www.nmind.org/standards-checklist/), a comprehensive framework for evaluating the quality of a tool's documentation, infrastructure, and testing capabilities against open, community-developed, scientific software-development standards. Badge ratings for all tools that complete this review process can be viewed at [Evaluated Tools](https://www.nmind.org/proceedings/). 

Software utilized for the HBCD release must undergo NMIND peer review and be published with a DOI. To initiate editorial review, developers complete the checklist and submit a pull request to the [proceedings repository](https://github.com/nmind/proceedings), including the tool's exported JSON file for external review. Any issues or feature requests related to this utility should be reported as issues in the NMIND [GitHub repository](https://github.com/nmind/standards-checklist). 

At a minimum, tools must meet the standards equivalent to the Bronze badge in the rating system. Developers may bypass checklist items that are not applicable—for example, listing software dependencies is less critical since all HBCD software must be containerized.

## Documentation 
### NMIND Documentation Checklist (Bronze Badge)
<input type="checkbox"> Landing page provides a link to documentation and brief description of what program does<br>
<input type="checkbox"> Documentation is up to date with version of software (*see [Obtaining a DOI](#obtaining-a-doi) for details*)<br>
<input type="checkbox"> Typical intended usage is described<br>
<input type="checkbox"> An example of its usage is shown<br>
<input type="checkbox"> Document functions intended for users (i.e., public function docstring/help coverage ≥ 10%)<br>
<input type="checkbox"> Reasonable description of required inputs (i.e., "NIfTI of brain mask in MNI" vs. "An image file")<br>
<input type="checkbox"> Description of output(s)<br>
<input type="checkbox"> User installation instructions available<br>
<input type="checkbox"> Dependencies listed (i.e. external and within-language requirements)<br>

### HBCD-Specific Requirement: Webpage For Documentation
In addition to the general guidelines outlined in the checklist, we require that HBCD pipelines maintain living documentation accessible through a dedicated webpage. This ensures the information remains up-to-date, offering a more dynamic and easily navigable resource compared to static publications or standard GitHub README files. Given the complexity and depth of information typically required for image processing pipelines, a webpage provides a more effective platform for organizing and presenting the documentation. Developers can refer to the [fMRIPrep ReadtheDocs](https://fmriprep.org/en/stable/) as a guide for overall organization and what level of detail each section should ideally include. 

## Infrastructure
### NMIND Infrastructure Checklist (Bronze Badge)
<input type="checkbox"> Code is open source<br>
<input type="checkbox"> Package is under version control (*see [Version Control](#version-control) for details*)<br>
<input type="checkbox"> Readme is present<br>
<input type="checkbox"> License is present (*see [Licensing](#licensing) for details*)<br>
<input type="checkbox"> Issues tracking is enabled (i.e., either through GitHub or external site)<br>
<input type="checkbox"> Digital Object Identifier (DOI) points to latest version (*see [Obtaining a DOI](#obtaining-a-doi) for details*)<br>
<input type="checkbox"> All documented installation instructions can be successfully followed<br>

### Obtaining a DOI
HBCD software must include a DOI for publication that points to the latest software version. We recommend that developers obtain a DOI by self-publishing on [Zenodo](https://cdnis-brain.readthedocs.io/zenodo/), which generates a top-level DOI as well as a per-version DOI attached to each release. Note that this should be done even if you have published a scientific article about your tool so that the software version can be properly cited. The pipeline webpage should include a description of how to properly cite the pipeline (see [example](https://fmriprep.org/en/stable/#citation)). 

**NOTE:** Remember to add the Zenodo DOI badge to the landing page of your website. This will additionally fulfill the Documentation checklist item *"Documentation is up to date with version of software*." See an example of Zenodo badge and associated Zenodo publication on the [Nibabies webpage](https://nibabies.readthedocs.io/en/latest/).

### Licensing
Per the checklist above, we require HBCD pipeline software to include a license. Remember that source code for HBCD pipelines are required to be open source; common permissive license options include [Apache-2.0 License 2.0](https://github.com/DCAN-Labs/hbcd-docs/community/license/new?branch=main&filename=LICENSE&template=apache-2.0), [MIT License](https://github.com/DCAN-Labs/hbcd-docs/community/license/new?branch=main&filename=LICENSE&template=mit), and the [BSD-3-Clause license](https://github.com/DCAN-Labs/hbcd-docs/community/license/new?branch=main&filename=LICENSE&template=bsd-3-clause). Visit GitHub's documentation on [Licensing a Repository](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/licensing-a-repository) and [Adding a License To a Repository](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/adding-a-license-to-a-repository) for more information. 

### Version Control
In addition to basic version control on GitHub, developers should tag new releases when significant updates or multiple changes are made. Each tagged release must include a changelog detailing the differences from the previous version. Developers are encouraged to establish a standard release cycle and define criteria for special releases, such as urgent bug fixes. Documentation should specify which versions will receive long-term support, which will be deprecated, and the timeline for deprecation.

### HBCD-Specific Requirement: Containerization & BIDS Compatibility 
To ensure data processing and analytic reproducibility, all HBCD pipelines must follow general [BIDS-App guidelines](https://bids-apps.neuroimaging.io/). This includes being containerized as well as compatibility with BIDS standard input data, i.e. the latest HBCD derivatives provided in the current release. 

## Testing Ability

### NMIND Testing Checklist (Bronze Badge)
<input type="checkbox"> Provide/generate/point to test data**<br>
<input type="checkbox"> Provide instructions for users to run tests and evaluate for correct behavior

<i>**Standards for testing may not be applicable for all HBCD processing pipelines. For example, depending on how specialized a given application is for HBCD, openly sharing representative test data for the workflow may not be feasible.</i>

## Current HBCD Pipeline Evaluations

A full list of tools evaluated through the [NMIND Coding Standards Checklist](https://www.nmind.org/standards-checklist/) can be found on their webpage under [Evaluated Tools](https://www.nmind.org/proceedings/). Below are the badge rating details for pipelines integrated into the HBCD release environment:

- [MRIQC](https://www.nmind.org/proceedings/mriqc/)
- BIBSNet
- [infant-fMRIPrep](https://www.nmind.org/proceedings/nibabies/) 
- [XCP-D](https://www.nmind.org/proceedings/xcpd/)
- [QSIPrep](https://www.nmind.org/proceedings/qsiprep/) 
- [QSIRecon](https://www.nmind.org/proceedings/qsirecon/)
- [qMRI Postproc](https://www.nmind.org/proceedings/hbcd_qmri_postproc/)
- [HBCD-MADE](https://www.nmind.org/proceedings/hbcdmade/)
- [OSPREY-BIDS](https://www.nmind.org/proceedings/osprey_bids/)
- [HBCD-Motion](https://www.nmind.org/proceedings/hbcd_motion_postproc/)