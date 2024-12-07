# Structural MRI (sMRI)

HBCD protocols for structural MRI were informed by recent large-scale developmental neuroimaging studies including ABCD, HCP Lifespan, and BCP. These studies provided a solid starting point for the development of well-validated, high-resolution protocols harmonized across all three major scanner vendors (Casey et al., 2018) and the importance of T2w acquisition in infants due to suboptimal grey/white T1w contrast resulting from incomplete myelination (Howell et al., 2019, Myers et al., 2023).

<p style="font-size: 1.1em; margin-bottom: 0px"><strong>Key features of the HBCD T1w and T2w structural imaging protocols include:</strong></p>
- 0.8 mm isotropic resolution
- The use of compressed SENSE reconstructions to allow high acceleration factors and thus much shorter acquisition times (under 9 minutes total for T1w and T2w – see vendor specific pages for details)
- The use of embedded navigators to track motion during structural imaging (White et al., 2010, Tisdall et al., 2016, Andersen et al., 2019). In the current release, scans were not prospectively corrected for motion, although this is intended to come online in later releases.
- As with ABCD, the contrast-relevant parameters are matched as closely as possible across vendors for the T1w scans.
- Also similar to ABCD, for the T2w scans, vendor-specific parameters were chosen to achieve similar contrast and SNR, accounting for the fact that each vendor implements their 3D T2w pulse sequences differently.

<details class="collapsible references">
  <summary class="references">References</summary>
 <p>Andersen, M., Björkman-Burtscher, I. M., Marsman, A., Petersen, E. T., & Boer, V. O. (2019). Improvement in diagnostic quality of structural and angiographic MRI of the brain using motion correction with interleaved, volumetric navigators.
<em>PLoS One</em>, 14(5), Article e0217145. <a href="https://doi.org/10.1371/journal.pone.0217145">10.1371/journal.pone.0217145</a></p>

<p>Casey, B. J., Cannonier, T., Conley, M. I., Cohen, A. O., Barch, D. M., Heitzeg, M. M., Soules, M. E., Teslovich, T., Dellarco, D. V., Garavan, H., Orr, C. A., Wager, T. D., Banich, M. T., Speer, N. K., Sutherland, M. T., Riedel, M. C., Dick, A. S., Bjork, J. M., Thomas, K. M., … ABCD Imaging Acquisition Workgroup. (2018). The Adolescent Brain Cognitive Development (ABCD) study: Imaging acquisition across 21 sites. <em>Developmental Cognitive Neuroscience</em>, 32, 43–54. <a href="https://doi.org/10.1016/j.dcn.2018.03.001">https://doi.org/10.1016/j.dcn.2018.03.001</a></p>

<p>Howell, B. R., Styner, M. A., Gao, W., Yap, P.-T., Wang, L., Baluyot, K., Yacoub, E., Chen, G., Potts, T., Salzwedel, A., Li, G., Gilmore, J. H., Piven, J., Smith, J. K., Shen, D., Ugurbil, K., Zhu, H., Lin, W., & Elison, J. T. (2019). The UNC/UMN Baby Connectome Project (BCP): An overview of the study design and protocol development. <em>NeuroImage</em>, 185, 891–905. <a href="https://doi.org/10.1016/j.neuroimage.2018.03.049">https://doi.org/10.1016/j.neuroimage.2018.03.049</a></p>

<p>Myers, M. J., Labonte, A. K., Gordon, E. M., Laumann, T. O., Tu, J. C., Wheelock, M. D., Nielsen, A. N., Schwarzlose, R., Camacho, M. C., Warner, B. B., Raghuraman, N., Luby, J. L., Barch, D. M., Fair, D. A., Petersen, S. E., Rogers, C. E., Smyser, C. D., & Sylvester, C. M. (2023). Functional parcellation of the neonatal brain. In <em>bioRxivorg</em>. <a href="https://doi.org/10.1101/2023.11.10.566629">https://doi.org/10.1101/2023.11.10.566629</a></p>

<p>Tisdall, M. D., Reuter, M., Qureshi, A., Buckner, R. L., Fischl, B., & van der Kouwe, A. J. W. (2016). Prospective motion correction with volumetric navigators (vNavs) reduces the bias and variance in brain morphometry induced by subject motion. <em>Neuroimage</em>, 127, pp. 11-22. <a href="https://doi.org/10.1016/j.neuroimage.2015.11.054">10.1016/j.neuroimage.2015.11.054</a></p>

<p>White, N., Roddey, C., Shankaranarayanan, A., Han, E., Rettmann, D., Santos, J., Kuperman, J., & Dale, A. (2010). PROMO: Real-time prospective motion correction in MRI using image-based tracking. <em>Magn. Reson Med</em>, 63 (1), pp. 91-105, <a href="https://doi.org/10.1002/mrm.22176">10.1002/mrm.22176</a></p>
</details>