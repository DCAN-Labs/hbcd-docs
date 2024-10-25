# Pipelines & Software Standards

## Processing Pipelines
**The following pipelines were used for HBCD data processing: for more details, visit the pipeline webpages linked below as well as the [Tool Details Overview](https://hbcd-cbrain-processing.readthedocs.io/latest/tool_details.html) section of the [HBCD Processing webpage](https://hbcd-cbrain-processing.readthedocs.io/latest/index.html).**

**Magnetic Resonance Imaging (MRI)**    
- [MRIQC](https://mriqc.readthedocs.io/en/latest/): automated extraction of image quality metrics from structural (T1w and T2w) and functional MRI data  
- [BIBSNet](https://bibsnet.readthedocs.io/en/latest/): deep learning model for brain segmentation
- [infant-fMRIPrep/fMRIPrep](https://nibabies.readthedocs.io/en/latest/): structural and functional MRI preprocessing pipeline   
- [XCP-D](https://xcp-d.readthedocs.io/en/latest/): functional MRI post-processing and noise regression pipeline  
- [QSIPrep](https://qsiprep.readthedocs.io/en/latest/) and [QSIRecon](https://qsirecon.readthedocs.io/en/latest/): diffusion-weighted MRI (dMRI) data processing pipelines  
-  [SyMRI](https://hbcd-symri-postproc.readthedocs.io/en/latest/index.html): minimal post-processing for synthetic images generated from SyMRI tools using QALAS acquisition

**Electroencephalogram (EEG)**
- [HBCD-MADE](https://docs-hbcd-made.readthedocs.io/en/latest/): Maryland Analysis of Developmental EEG (MADE) pipeline adapted for HBCD data

**Magnetic Resonance Spectroscopy (MRS)**
- [OSPREY](https://osprey-bids.readthedocs.io/en/latest/index.html): MRS data processing pipeline

**Biosensor Data**
- [AXIVITY](https://hbcd-motion-postproc.readthedocs.io/en/latest/): leg movement data processing

## Processing and Analytic Software Standards
The following guidelines were presented to the HBCD pipeline developers and working groups, along with community developers, wishing to include their tools as part of the HBCD release environment to ensure standardization of HBCD software and documentation. These guidelines were developed based on principles and utilities developed by [NMIND](https://www.nmind.org/about) to foster reproducibility and standardization of tools within the field of neuroimaging ([Kiar et. al 2023](https://www.nature.com/articles/s41562-023-01647-0)). This includes the [NMIND Coding Standards Checklist](https://www.nmind.org/standards-checklist/), a rating system to assess the quality of documentation, infrastructure, and testing ability of neuroimaging software. 

Developers were instructed to complete the checklist and open a pull request in the [proceedings repository](https://github.com/nmind/proceedings) (with the exported JSON associated with the tool) for external review. Issues or feature requests for  this utility can be posted as an issue to the NMIND [GitHub repository](https://github.com/nmind/standards-checklist)\! 

At minimum, equivalent standards to the Bronze badge in the rating system are required. Items not relevant can be ignored/circumvented. For example, providing software dependencies is not as critical because all HBCD software is required to be containerized. Developers were instructed to user their best judgment regarding the relevance of each item to their specific software.

### Documentation 
#### NMIND Documentation Checklist
- [ ] Landing page (e.g., GitHub README, website) provides a link to documentation and brief description of what program does  
- [ ] Documentation is up to date with version of software  
- [ ] Typical intended usage is described  
- [ ] An example of its usage is shown  
- [ ] Document functions intended to be used by users (i.e., public function docstring / help coverage ≥ 10%)  
- [ ] Description of required input parameters for user-facing functions with reasonable description of inputs (i.e., "NIfTI of brain mask in MNI" vs. "An image file")  
- [ ] Description of output(s)  
- [ ] User installation instructions available  
- [ ] Dependencies listed (i.e., external and within-language requirements)

#### Webpage For Documentation
In addition to the general guidelines provided by the checklist, each pipeline is required to have living documentation made available via a web page using utilities such as [ReadtheDocs](https://about.readthedocs.com/?ref=readthedocs.com), [GitHub Pages](https://pages.github.com/?(null)), [Wiki](https://support.microsoft.com/en-us/office/create-and-edit-a-wiki-dc64f9c2-d1a2-44b5-ac59-b9d535551a32), etc. This allows for information to stay up-to-date as compared to a publication and also is easier to navigate than a simple GitHub README given the depth of information typically required for image processing pipelines. 

We recommended using the [fMRIPrep ReadtheDocs](https://fmriprep.org/en/stable/) as a guide for overall organization and what level of detail each section should ideally include. 

### Infrastructure
#### NMIND Infrastructure Checklist
- [ ] Code is open source  
- [ ] Package is under version control  
- [ ] Readme is present  
- [ ] License is present (see more details in following section)  
- [ ] Issues tracking is enabled (i.e., either through GitHub or external site)  
- [ ] Digital Object Identifier (DOI) points to latest version (e.g., Zenodo)  
- [ ] All documented installation instructions can be successfully followed

#### Licensing and Obtaining a DOI
All included software require a [license](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/adding-a-license-to-a-repository) and also a DOI for software publication. Internal pipelines to HBCD might be leveraged for release data prior to publication. For pipelines without an associated scientific article yet that can be cited, developers obtained a DOI by self-publishing on [Zenodo](https://cdnis-brain.readthedocs.io/zenodo/). Software provided for HBCD releases from non-HBCD PIs will be required to be peer reviewed and published along with the DOI.   
All software is required to run on BIDS input data or currently available HBCD derivatives as provided in the most current HBCD release. 

#### Versioning and New Release Policies
Beyond basic version control in GitHub, developers are instructed to tag new releases that are associated with specific versions of the repository whenever a large update (or large number of updates) has been made. The new tagged release should also include a change log that carefully documents the differences between the new and prior version.

Developers may also wish to decide on a standard release cycle as well as special cases/parameters which warrant a new release (e.g. a serious bug fix that needs to be implemented in version ASAP). Ideally there would be documentation around which versions are expected to receive long-term support vs versions that will be deprecated and the timeline for deprecation.

### Testing Ability

#### NMIND Testing Checklist
- [ ] Provide / generate / point to test data**  
- [ ] Provide instructions for users to run tests that include instructions for evaluation for correct behavior

**Note that standards for testing ability may not be relevant to or high-priority for all processing pipelines used by HBCD. Additionally, depending on how specialized a given application is for HBCD, making test data openly available that is representative of the workflow is likely not possible. 
