# Diffusion MRI (dMRI)

## Diffusion-Weighted Imaging (DWI)
DWI refers to the raw image data acquired during scanning. The DWI protocol provides diffusion-weighted images that may be used to estimate multiple models of diffusion behavior in the central nervous system. The protocol acquires roughly 140 diffusion-weighted echo planar images at four b-values (diffusion-weighting) between 0 and 3000 s/mm^2 (12-13 minutes total acquisition time). For raw image acquisition, a minimum of 60% of the diffusion-weighted volumes are required to be collected for the acquisition to be deemed successful. 

The diffusion-weighted images are processed with denoising and Gibbs artifact reduction, and corrected for eddy current distortion, head motion and echo planar susceptibility distortion (Cieslak et al. 2021). The diffusion encoding enables the estimation of multiple diffusion MRI models including diffusion tensor imaging (DTI) (Basser et al. 1994), diffusion kurtosis imaging (DKI) (Wu et al. 2010), and mean apparent propagator (MAP) (Özarslan et al. 2013). Each of these is described in greater detail below.


## Derived Images
### Diffusion Tensor Imaging (DTI) Maps
DTI maps, including **fractional anisotropy (FA)** and **mean diffusivity (MD)**, are commonly used measures that represent the DWI signal using a 3D multivariate normal (Gaussian) distribution of water diffusion displacements. The FA of the diffusion tensor represents the degree of anisotropic diffusion. In neural tissues, FA is increased in white matter bundles with dense, parallel fiber orientations. The MD corresponds the directionally-averaged apparent diffusion coefficient of water in the tissue and is inversely related to the density of cellular membranes. 

### Diffusion Kurtosis Imaging (DKI) Maps
DKI maps, including mean kurtois (MK) and radial kurtosis (RK), provide commonly used measures that expand the DTI signal model to estimate non-Gaussian diffusion kurtosis behavior in the brain. DKI maps may be used to better represent more complex diffusion-weighted signals phenomena that may be associated with more restricted diffusion. The mean kurtosis (MK) is the directionally averaged kurtosis measure, which is increased in regions of dense white matter. The radial kurtosis (RK) is the kurtosis associated with the diffusion signal perpendicular to the white matter axons.  

### Mean Apparent Propagator (MAP) Maps


zero displacement probablility

<details class="collapsible references">
  <summary class="references">References</summary>
<p>Alexander AL, Lee JE, Lazar M, Field AS. (2007). Diffusion tensor imaging of the brain. <em>Neurotherapeutics</em>, 4(3):316-29. <a href="https://doi.org/10.1016/j.nurt.2007.05.011">10.1016/j.nurt.2007.05.011</a></p>
<p>Basser PJ, Mattiello J, LeBihan D. (1994). MR diffusion tensor spectroscopy and imaging. <em>Biophys J.</em>, 66(1):259-67. <a href="https://doi.org/10.1016/S0006-3495(94)80775-1">10.1016/S0006-3495(94)80775-1</a></p>
<p>Cieslak M, Cook PA, He X, Yeh FC, Dhollander T, Adebimpe A, Aguirre GK, Bassett DS, Betzel RF, Bourque J, Cabral LM, Davatzikos C, Detre JA, Earl E, Elliott MA, Fadnavis S, Fair DA, Foran W, Fotiadis P, Garyfallidis E, Giesbrecht B, Gur RC, Gur RE, Kelz MB, Keshavan A, Larsen BS, Luna B, Mackey AP, Milham MP, Oathes DJ, Perrone A, Pines AR, Roalf DR, Richie-Halford A, Rokem A, Sydnor VJ, Tapera TM, Tooley UA, Vettel JM, Yeatman JD, Grafton ST, Satterthwaite TD. (2021). QSIPrep: an integrative platform for preprocessing and reconstructing diffusion MRI data. <em>Nature Methods</em>, 18(7):775-778. <a href="https://doi.org/10.1038/s41592-021-01185-5">10.1038/s41592-021-01185-5</a></p>
<p>Özarslan E, Koay CG, Shepherd TM, Komlosh ME, İrfanoğlu MO, Pierpaoli C, Basser PJ. (2013). Mean apparent propagator (MAP) MRI: a novel diffusion imaging method for mapping tissue microstructure. <em>Neuroimage</em>, 78:16-32. <a href="https://doi.org/10.1016/j.neuroimage.2013.04.016">10.1016/j.neuroimage.2013.04.016</a></p>
<p>Wu EX, Cheung MM. (2010). MR diffusion kurtosis imaging for neural tissue characterization. <em>NMR Biomed</em>, 23(7):836-48. <a href="https://doi.org/10.1002/nbm.1506">10.1002/nbm.1506</a></p>
</details>

