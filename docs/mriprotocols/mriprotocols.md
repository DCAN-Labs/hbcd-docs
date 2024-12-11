# MRI Protocols & Installation

The HBCD MRI protocol includes structural MRI, functional MRI, diffusion MRI, magnetic resonance spectroscopy (MRS), and quantitative relaxometry on Siemens, GE, and Philips MRI scanners. Per [Dean et al (2024)](https://www.sciencedirect.com/science/article/pii/S1878929324001130):

>*The majority of pulse sequences used for the HBCD MRI protocol are research-specific and some require signing transfer agreements with the academic centers at which the sequences were developed. While our goal was to use product sequences where possible, the decision to use research-specific pulse sequences was motivated by the desire to take advantage of additional non-product features (e.g., motion-tracking navigators) and/or the need for modifications to better harmonize across all three vendors (e.g., ensuring similar RF pulse shapes and timings).* 

Here we describe how to obtain and install the relevant sequences for your system as well as provide Scanning SOPs and other relevant resources provided to HBCD study sites. Please review for [Dean et al (2024)](https://www.sciencedirect.com/science/article/pii/S1878929324001130) for comprehensive details on the magnetic resonance protocols included.

## Siemens Protocol v2.2 (XA30)
Before importing the HBCD protocol, please ensure you have received and installed the necessary C2P sequence packages for access to the latest versions of each sequence. Without the C2P packages installed, the full protocol cannot be imported.

**NOTE: Siemens has identified a bug in NXVA30A SP02 (the software baseline used for this study) that may cause your scanner to become non-responsive during the installation of the certificates required for custom sequences. Please ensure you have SP02 SD05 installed on your scanner before proceeding, as this fixes the bug and allows you to install custom sequences.**

- **[Multiband EPI (University of Minnesota)](https://www.cmrr.umn.edu/multiband/)**
- **[vNav Morphometry (University of Pennsylvania)](https://mri-motion-correction-vnav-morphometry.readthedocs-hosted.com/en/nxva30a_162141/requesting.html)**
- **QALAS (Boston Children’s Hospital):** Please contact Borjan Gagoski (Borjan.Gagoski@childrens.harvard.edu)
- **ISTHMUS spectroscopy (Johns Hopkins University):** Please contact Richard Edden (edden@jhu.edu)

### Resources
[HBCD_v2.2_32ch.pdf](siemens/HBCD_v2.2_32ch.pdf)<br>
[HBCD_v2.2_64ch.pdf](siemens/HBCD_v2.2_64ch.pdf)<br>
[HBCD_v2.2_32ch.exar1](siemens/HBCD_v2.2_32ch.exar1)<br>
[HBCD_v2.2_64ch.exar1](siemens/HBCD_v2.2_64ch.exar1)<br>
[DiffusionVectors_HBCD_pe1_03142022.dvs](siemens/DiffusionVectors_HBCD_pe1_03142022.dvs)<br>
[DiffusionVectors_HBCD_pe2_03142022.dvs](siemens/DiffusionVectors_HBCD_pe2_03142022.dvs)


## GE Protocol v2.2
Request sequences from your local GE scientist. 
Download the latest protocol from https://bit.ly/HBCD_GE.
Read and follow the release notes carefully!

## Philips Protocol
Contact your local Philips scientist for the sequences and protocol.  

