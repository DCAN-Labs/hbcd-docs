# Wearable Sensors
**Full Name**: Infant leg movement data collected by wearable sensors.   
**Construct**: motor behavior, physical activity, sleep   

Wearable sensor data (accelerometer and gyroscope) were collected continuously over 72 hours from sensors placed on infants’ right and left ankles to estimate movement frequency, intensity, and sleep periods. Caregivers followed normal routines, removing sensors only for water exposure (e.g., baths) and replacing them afterward. Each sensor (Axivity AX6) was calibrated by recording 10 seconds on each of its six flat surfaces before data collection. Sensors recorded accelerometer (±16 g) and gyroscope (±2000 dps) data at 25 Hz, enabling estimates of sedentary, light, moderate-to-vigorous activity, and sleep. See [Pini et al. 2024](https://doi.org/10.1016/j.dcn.2024.101446) for a full measure description.

<details>
<summary>Implementation & Data Collection Details</summary>
<ul>
<li><b>Method of Administration</b>: RA placed sensors on child at visit, sensors then worn while 72 hours of data were collected across typical activities in the natural environment.</li>
<li><b>Visits</b>: V02, V03</li>
</ul>
</details>

## Quality Control & Known Issues  
Raw calibration files were checked during active data collection to verify the presence of sufficient data for each of the six axes. A random selection of 72-hour data files were reviewed on a weekly basis to check for the presence of data, labeling of right and left leg, and sampling rate used. Since the QC process is manual and visual, only a small percentage of files were reviewed each week.

Quality control revealed that issues were generally rare and most data were deemed to be present and accurately collected. Errors that did arise were corrected when possible (though this was typically not feasible). 
<p>
<details>
<summary>Common QC Errors</summary>
</p>
<p>
<ul>
    <li>Calibration files:
        <ul>
            <li>Inadequate data for each of the six axes, often due to human error</li>
            <li>Missing data, caused by either human error or technical difficulties</li>
        </ul>
    </li>
    <li>72-hour files:
    <ul>
        <li>Missing data, due to human error, technical issues, or a parent/legal guardian declining to participate in this aspect of the study</li>
        <li>Sensors being removed for extended periods during the 72-hour collection</li>
        <li>Incorrect sampling rate</li>
    </ul>
</details>
</p>

Subject matter experts would like users to note that accelerometer sensor timestamps can drift over time. Although right and left leg sensors start recording simultaneously with the same sampling rate and duration, exact time alignment cannot be assumed. By our estimates, Axivity AX6 sensors recording at 25 samples/sec diverge from one another by a couple of seconds over 72 hours, with the magnitude of this discrepancy increasing over time. Furthermore, offsets differed between sensors, necessitating a calibration procedure to correct for these differences ([Oh et al., 2024](https://doi.org/10.3390/s24175736)).

In addition, for raw data downloads, when calibration files are missing, it is technically possible to use a different set of calibration files from the same 2 sensors that were collected from a different data collection session close in time. For processed data downloads, when calibration files are missing, data are not processed. In analysis, users are advised to use caution in analyzing datasets with missing data.


<details class="collapsible references">
  <summary class="references">References</summary>
 <ul>
<p>Ghazi, M. A., Zhou, J., Havens, K. L., &amp; Smith, B. A. (2024). Accelerometer thresholds for estimating physical activity intensity levels in infants: A preliminary study. <em>Sensors</em> (Basel, Switzerland), 24(14), 4436. <a href="https://doi.org/10.3390/s24144436">https://doi.org/10.3390/s24144436</a></p>
<p>Jeung, S., Cockx, H., Appelhoff, S., Berg, T., Gramann, K., Grothkopp, S., Warmerdam, E., Hansen, C., Oostenveld, R., BIDS Maintainers, &amp; Welzel, J. (2024). Motion-BIDS: an extension to the brain imaging data structure to organize motion data for reproducible research. <em>Scientific Data</em>, 11(1), 716. <a href="https://doi.org/10.1038/s41597-024-03559-8">https://doi.org/10.1038/s41597-024-03559-8</a></p>
<p>Oh, J., Loeb, G. E., &amp; Smith, B. A. (2024). The utility of calibrating wearable sensors before quantifying infant leg movements. <em>Sensors</em> (Basel, Switzerland), 24(17), 5736. <a href="https://doi.org/10.3390/s24175736">https://doi.org/10.3390/s24175736</a></p>
<p>Oh, J., Ordoñez, E. L. T., Velasquez, E., Mejía, M., Del Pilar Grazioso, M., Rohloff, P., &amp; Smith, B. A. (2024). Associating neuromotor outcomes at 12 months with wearable sensor measures collected during early infancy in rural Guatemala. <em>Gait &amp; Posture</em>, 113, 477–489. <a href="https://doi.org/10.1016/j.gaitpost.2024.08.005">https://doi.org/10.1016/j.gaitpost.2024.08.005</a></p>
<p>Pini, N., Fifer, W. P., Oh, J., Nebeker, C., Croff, J. M., Smith, B. A., &amp; Novel Technology/Wearable Sensors Working Group. (2024). Remote data collection of infant activity and sleep patterns via wearable sensors in the HEALthy Brain and Child Development Study (HBCD). <em>Developmental Cognitive Neuroscience</em>, 69(101446), 101446. <a href="https://doi.org/10.1016/j.dcn.2024.101446">https://doi.org/10.1016/j.dcn.2024.101446</a></p>
<p>Smith, B. A., Trujillo-Priego, I. A., Lane, C. J., Finley, J. M., &amp; Horak, F. B. (2015). Daily quantity of infant leg movement: Wearable sensor algorithm and relationship to walking onset. <em>Sensors</em> (Basel, Switzerland), 15(8), 19006–19020. <a href="https://doi.org/10.3390/s150819006">https://doi.org/10.3390/s150819006</a></p>
<p>Trujillo-Priego, I. A., &amp; Smith, B. A. (2017). Kinematic characteristics of infant leg movements produced across a full day. <em>Journal of Rehabilitation and Assistive Technologies Engineering</em>, 4, 205566831771746. <a href="https://doi.org/10.1177/2055668317717461">https://doi.org/10.1177/2055668317717461</a></p>
<p>Trujillo-Priego, I. A., Zhou, J., Werner, I. F., Deng, W., &amp; Smith, B. A. (2020). Infant leg activity intensity before and after naps. <em>Journal for the Measurement of Physical Behaviour</em>, 3(2), 157–163.<a href="https://doi.org/10.1123/jmpb.2019-0011">https://doi.org/10.1123/jmpb.2019-0011</a></p>
</ul>
</details>
<br>