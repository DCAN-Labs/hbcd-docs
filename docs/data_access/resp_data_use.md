# Responsible Data Use

## Rationale
The HEALthy Brain and Child Development (HBCD) study dataset is a large, rich, and complex resource that can drive scientific discovery, provide a foundation for translation and implementation research, and inform development of public policy. To create this dataset, thousands of participants have given generously of their time and their bodies to help advance science. They have trusted us with sensitive information. The use of HBCD data carries ethical responsibilities to minimize risks of harm to participants and to treat them respectfully and justly. One way data users can respect participants’ contributions is by conducting careful, high-quality science.  

## Warnings
To facilitate responsible data use, warnings have been added to tables and variables in the NBDC Data Dictionary and are linked to sections of the [Release Notes](../measures/index.md) to provide additional information for data users. We recommend that all data users:

1.    	Review the data warnings for any variable that you will be downloading and/or using by clicking the link and reviewing the warning associated with that variable
2.    	Review any resources and citations included with the warning and follow recommended guidelines
3.    	Reach out to the HBCD Responsible Use of Data Committee (RUDC) chair Pilar Ossorio (<span class="blue-text">pnossorio@wisc.edu</span>) with any questions about data warnings or responsible data use.
 
There are 2 types of warnings, both of which may aid in more scientifically rigorous use of HBCD data:

<p>
<div id="warning-banner" class="warning-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fas fa-exclamation-triangle"></i></span>
  <span class="text">Data Warning</span>
  <span class="arrow">▸</span>
</div>
<div class="collapsible-content">
<p>The purpose of this warning is to improve transparency and offer technical assistance by alerting the user to issues of data quality, providing information on how variables were constructed, providing instructions on how to calculate or analyze specific variables, or providing code (if necessary).</p> 
</div>
</p>

<p>
<div id="alert-banner" class="alert-banner" onclick="toggleCollapse(this)">
    <span class="emoji"><i class="fas fa-exclamation-circle"></i></span>
    <span class="text">Responsible Use Warning</span>
  <span class="arrow">▸</span>
</div>
<div class="collapsible-content">
<p>The purpose of this warning is to offer guidance for research design, data interpretation, and communication of findings, including conceptual information.</p>
</div>
</p>
Warnings section of readthedocs RUD homepage: "These warnings also include conceptual information (e.g., difference between sex assigned at birth and gender identity, the possibility of bias due to attrition or non-response)." 
We will remove the example, "(e.g., difference between sex assigned at birth and gender identity, the possibility of bias due to attrition or non-response)". This will be replaced with a new example. 

## Recommendations for Rigorous, Reproducible, and Responsible Data Use
The HBCD Responsible Use of Data Committee (RUDC) provides the following guidance for researchers planning to use HBCD data:

### Learn and abide by the provisions of the Data Use Certificate.
<b class="gray-text">All users of HBCD data should be listed on a Data Use Certificate (DUC) and bound by it.</b> Among other things, the DUC prohibits any attempt to establish the identities of HBCD participants. To protect participants against identification, users agree to adhere to a minimum cell threshold of ten participants in publications and other public presentations. Epidemiologists, statisticians, and other data analysts argue that a cell size between 1 and 10 is usually too small for meaningful analysis; therefore, avoiding analysis of small cells can produce more rigorous, reproducible science and also helps protect study participants from identification.   

<b class="gray-text">Access to HBCD data is limited to people who are listed on an active HBCD DUC.</b> This means you cannot enter HBCD data into a generative AI tool/large language model, such as ChatGPT, because doing so would leak HBCD data to people who do not have a DUC (see [FAQ: Can I Use ChatGPT...](../faq.md/#faq-ai)).  

### Consider ethical principles throughout the research process.
<b class="gray-text">Equity-focused reflection:</b> Regulations for the protection of humans in federally-funded research (e.g., 45 C.F.R. 46) do not require IRBs to oversee research using anonymized data obtained from a repository. Nonetheless, the data come from people to whom we have ethical obligations, including obligations of respect, minimizing harm, and justice. Data users should keep these principles in mind at each stage of their research. 

### Use non-stigmatizing language in scientific communications.
<b class="gray-text">Use clear and respectful language when describing people whose data you analyzed.</b> Person-first language emphasizes individuals’ inherent value and respects them as people before describing any conditions or diseases they may have. For example, consider using “person with a substance use disorder” or “person in recovery from a substance use disorder” and avoid referring to participants as “addicts,” “users,” or “former users.”  Avoid terms such as “drug baby” or “crack baby” in favor of descriptions such as “Infant with prenatal substance exposure” or “infant with neonatal opioid withdrawal syndrome.”   

<div style="padding: 0;">
  <b class="gray-text">Recommendations for language regarding people with substance use disorders:</b>
  <ul style="margin: 0 0 20px 20px; padding: 0;">
    <li><a href="https://nida.nih.gov/nidamed-medical-health-professionals/health-professions-education/words-matter-terms-to-use-avoid-when-talking-about-addiction">Words Matter - Terms to Use and Avoid When Talking About Addiction</a></li>
    <li><a href="https://doi.org/10.1111/acer.14840">Why language matters in alcohol research: Reducing stigma (Shi et al., 2022)</a></li>
  </ul>
</div>

<div style="padding: 0;">
<b class="gray-text">Recommendations for writing and talking about Fetal Alcohol Spectrum Disorder:</b>
  <ul style="margin: 0 0 20px 20px; padding: 0;">
    <li><a href="https://canfasd.ca/wp-content/uploads/publications/CanFASD-Common-Messages-Guide-2023_FINAL-1.pdf">Common Messages: Guidelines for talking and writing about FASD</a></li>
  </ul>
</div>

<div style="padding: 0;">
<b class="gray-text">Recommendations for using language regarding people with disabilities:</b>
  <ul style="margin: 0 0 20px 20px; padding: 0;">
    <li><a href="https://www.cdc.gov/disability-and-health/articles-documents/communicating-with-and-about-people-with-disabilities.html">Communicating With and About People with Disabilities (CDC)</a></li>
  </ul>
</div>

### Use population descriptors thoughtfully and scientifically.
<b class="gray-text">Best practice is to include the right variable for the scientific question.</b> Genetic and/or biological variables are not interchangeable with demographic descriptions. Demographic descriptors should be used when they are scientifically justified and accompanied by clear definitions and rationales.
  
<b class="gray-text">Use of race and ethnicity:</b> The National Academies of Sciences, Engineering, and Medicine (NASEM) recently published a report, [*Rethinking Race and Ethnicity in Biomedical Research*](https://doi.org/10.17226/27913), which can be downloaded free of charge. This report emphasizes that race variables are “not a substitute for unseen or unmeasured biological predictors of interest” (Conclusion 5-5; [NASEM, 2024](https://doi.org/10.17226/27913)). This report also notes that the Office for Management and Budget’s race and ethnicity categories, which must be used for government reporting purposes (e.g., by federal grantees), are a minimum set of categories and need not be used for scientific analyses (Conclusion 5-1; [NASEM, 2024](https://doi.org/10.17226/27913)).  

<b class="gray-text">Population descriptors in genomics research:</b> NASEM also published a report, [*Using Population Descriptors in Genetics and Genomics Research*](https://doi.org/10.17226/26902), articulating best practices for using population descriptors in genomics. Importantly, the report cautions researchers against using race as a proxy for genetic variation or assigning genetic ancestry labels based on race, regardless of whether race was self-identified. In addition, researchers should be mindful of the connotations and impacts of terminology used to label groups and should disclose how they select and assign group labels ([NASEM, 2023](https://doi.org/10.17226/26902)).

### Analyses should reflect the complexity of brain and child development.  Use relevant social and environmental variables (available in the HBCD dataset) as covariates in your analyses.
<b class="gray-text">It is essential to recognize the differences of life experiences and environments</b>, acknowledging that human development is a dynamic process influenced by the potential for adaptation and change ([Simmons et al., 2021](https://doi.org/10.1177/09567976211003564)). Studying this complexity requires use of statistical models that include appropriate covariates. Data users are encouraged to consider contextual information regarding which covariates might confound, modify, or mediate the effect they seek to study ([Greenland & Pearce, 2015](https://doi.org/10.1146/annurev-publhealth-031914-122559)).   

<b class="gray-text">Avoid oversimplifying complex constructs.</b> Constructs such as race and ethnicity are complex, shaped by historical, cultural, and social factors. These constructs do not refer to fixed, biological categories of people. At every stage of research, investigators should evaluate and decide whether use of such constructs is scientifically justified ([Cardenas-Inguinez & Gonzales, 2024](https://doi.org/10.1038/s41593-024-01608-4); [NASEM, 2024](https://doi.org/10.17226/27913)). 

<b class="gray-text">Complex constructs, e.g., race, should not be used as proxies for variables such as socioeconomic status, access to healthcare, or environmental exposures.</b> Including social and environmental variables in one’s analysis allows for a more accurate understanding of underlying contributors to outcomes of interest ([Hoffman et al., 2022](https://doi.org/10.1016/j.jadohealth.2021.11.008)). HBCD has collected data on many social and environmental variables relevant for child development. For help finding these variables in the dataset or learning how to use them contact Pilar Ossorio (<span class="blue-text">pnossorio@wisc.edu</span>).

### Promoting transparency and reproducibility in research. 
<b class="gray-text">Transparency in reporting methods and results is essential.</b> A review of ABCD Study manuscripts found that sharing analytic scripts (e.g., on Github, OSF, Zenodo) and providing detailed information about missing data significantly improved transparency and reproducibility ([Lopez et al., 2024](https://doi.org/10.1016/j.dcn.2024.101408)). We recommend that HBCD data users review the [checklist of recommendations](https://www.sciencedirect.com/science/article/pii/S1878929324000690?via%3Dihub#tbl0010) to improve transparency and reproducibility.

<b class="gray-text">Researchers should consider features of the data available in HBCD, the strengths and limitations therein, and follow guidance for rigor and reproducibility.</b> [Sarasoga-Harris and colleagues (2022)](https://doi.org/10.1016/j.dcn.2022.101115) have developed a practical guide for researchers and reviewers, including relevant analytical and methodological considerations.

## References
<div class="references">
    <p>Canadian Fetal Alcohol Spectrum Disorder Research Network. (2023). Common messages guide. CanFASD. <a href="https://canfasd.ca/wp-content/uploads/publications/CanFASD-Common-Messages-Guide-2023_FINAL-1.pdf">https://canfasd.ca/wp-content/uploads/publications/CanFASD-Common-Messages-Guide-2023_FINAL-1.pdf</a></p>
    <p>Cardenas-Iniguez, C., Gonzalez, M.R. Recommendations for the responsible use and communication of race and ethnicity in neuroimaging research. Nat Neurosci 27, 615–628 (2024). <a href="https://doi.org/10.1038/s41593-024-01608-4">https://doi.org/10.1038/s41593-024-01608-4</a></p>
    <p>CDC. (2024, December 10). Communicating with and about people with disabilities. Disability and Health. <a href="https://www.cdc.gov/disability-and-health/articles-documents/communicating-with-and-about-people-with-disabilities.html">https://www.cdc.gov/disability-and-health/articles-documents/communicating-with-and-about-people-with-disabilities.html</a></p>
    <p>Greenland, S., & Pearce, N. (2015). Statistical foundations for model-based adjustments. Annual Review of Public Health, 36(1), 89–108. <a href="https://doi.org/10.1146/annurev-publhealth-031914-122559">https://doi.org/10.1146/annurev-publhealth-031914-122559</a></p>
    <p>Hoffman, E. A., LeBlanc, K., Weiss, S. R. B., & Dowling, G. J. (2022). Transforming the future of adolescent health: Opportunities from the adolescent brain cognitive development study. The Journal of Adolescent Health: Official Publication of the Society for Adolescent Medicine, 70(2), 186–188. <a href="https://doi.org/10.1016/j.jadohealth.2021.11.008">https://doi.org/10.1016/j.jadohealth.2021.11.008</a></p>
    <p>Lopez, D. A., Cardenas-Iniguez, C., Subramaniam, P., Adise, S., Bottenhorn, K. L., Badilla, P., Mukwekwerere, E., Tally, L., Ahanmisi, O., Bedichek, I. L., Matera, S. D., Perez-Tamayo, G. M., Sissons, N., Winters, O., Harkness, A., Nakiyingi, E., Encizo, J., Xiang, Z., Wilson, I. G., … Huber, R. S. (2024). Transparency and reproducibility in the Adolescent Brain Cognitive Development (ABCD) study. Developmental Cognitive Neuroscience, 68(101408), 101408. <a href="https://doi.org/10.1016/j.dcn.2024.101408">https://doi.org/10.1016/j.dcn.2024.101408</a></p>
    <p>National Academies of Sciences, Engineering, and Medicine. 2024. Rethinking Race and Ethnicity in Biomedical Research. Washington, DC: The National Academies Press. <a href="https://doi.org/10.17226/27913">https://doi.org/10.17226/27913</a></p>
    <p>National Academies of Sciences, Engineering, and Medicine. 2023. Using Population Descriptors in Genetics and Genomics Research: A New Framework for an Evolving Field. Washington, DC: The National Academies Press. <a href="https://doi.org/10.17226/26902">https://doi.org/10.17226/26902</a></p>
    <p>National Institute on Drug Abuse. (2021, November 29). Words matter - terms to use and avoid when talking about addiction. National Institute on Drug Abuse. <a href="https://nida.nih.gov/nidamed-medical-health-professionals/health-professions-education/words-matter-terms-to-use-avoid-when-talking-about-addiction">https://nida.nih.gov/nidamed-medical-health-professionals/health-professions-education/words-matter-terms-to-use-avoid-when-talking-about-addiction</a></p>
    <p>Saragosa-Harris, N. M., Chaku, N., MacSweeney, N., Guazzelli Williamson, V., Scheuplein, M., Feola, B., Cardenas-Iniguez, C., Demir-Lira, E., McNeilly, E. A., Huffman, L. G., Whitmore, L., Michalska, K. J., Damme, K. S., Rakesh, D., & Mills, K. L. (2022). A practical guide for researchers and reviewers using the ABCD Study and other large longitudinal datasets. Developmental Cognitive Neuroscience, 55(101115), 101115. <a href="https://doi.org/10.1016/j.dcn.2022.101115">https://doi.org/10.1016/j.dcn.2022.101115</a></p>
    <p>Shi, H. D., McKee, S. A., & Cosgrove, K. P. (2022). Why language matters in alcohol research: Reducing stigma. Alcoholism, Clinical and Experimental Research, 46(6), 1103–1109. <a href="https://doi.org/10.1111/acer.14840">https://doi.org/10.1111/acer.14840</a></p>
    <p>Simmons, C., Conley, M. I., Gee, D. G., Baskin-Sommers, A., Barch, D. M., Hoffman, E. A., Huber, R. S., Iacono, W. G., Nagel, B. J., Palmer, C. E., Sheth, C. S., Sowell, E. R., Thompson, W. K., & Casey, B. J. (2021). Responsible use of open-access developmental data: The adolescent brain cognitive development (ABCD) study. Psychological Science, 32(6), 866–870. <a href="https://doi.org/10.1177/09567976211003564">https://doi.org/10.1177/09567976211003564</a></p>
</div>
<br>


 
