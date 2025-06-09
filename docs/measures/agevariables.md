# Age Variable Definitions

Fields reporting age in the tabulated data include global, single-point (i.e. static) variables in [Basic Demographics](#basic-demographics) (e.g. Maternal Age at V01), and [instrument-specific variables](#tabulated-instrument-data) for age that vary depending on the date of administration for a given instrument. In the [raw file-based data](#raw-file-based-data) (EEG, magnetic resonance imaging/spectroscropy, and motion sensor data), fields reporting age vary depending on the date of data acquisition, reported in the session- and scan-level `.tsv` files. See details for each below. 

## Basic Demographics

Tabulated Basic Demographics data (`sed_basic_demographics`) includes variables derived across instruments, with the following set of variables reporting age - please see [Basic Demographics](demographics.md#basic-demographics) for more information. **Note that all of the following are single-point, static variables (i.e. they do not change over time) that should be present and consistent across all Visits (V01, V02, etc.):**

<table style="width: 100%; border-collapse: collapse; table-layout: fixed; font-size: 13px;">
    <thead>
      <tr>
        <th style="width: 20%; padding: 5px; text-align: center;">Name</th>
        <th style="width: 10%; padding: 5px; text-align: center;">Variable Name</th>
        <th style="width: 30%; padding: 5px; text-align: center;">Description</th>
        <th style="width: 30%; padding: 5px; text-align: center;">Unit & Calculation</th>
      </tr>
    </thead>
    <tbody>
<td style="padding: 8px; word-wrap: break-word; white-space: normal;">Maternal Age at V01 (MAV01)</td>
<td style="padding: 8px; word-wrap: break-word; white-space: normal;"><code>mother_age_v01</code></td>
<td style="padding: 8px; word-wrap: break-word; white-space: normal;">Birth parent's age, obtained from the scheduled date of the V01 visit</td>
<td style="padding: 8px; word-wrap: break-word; white-space: normal;">Years (to two decimal places), with fractional years calculated by dividing the number of whole months (rounded down) by 12</td>
</tr>
<tr>
<td style="padding: 8px; word-wrap: break-word; white-space: normal;">Maternal Age at Delivery (MAD)</td>
<td style="padding: 8px; word-wrap: break-word; white-space: normal;"><code>mother_age_delivery</code></td>
<td style="padding: 8px; word-wrap: break-word; white-space: normal;">Birth parent's age at the time of their child's delivery (date of birth)</td>
<td style="padding: 8px; word-wrap: break-word; white-space: normal;">Years (to two decimal places), with fractional years calculated by dividing the total whole months (rounded down) by 12</td>
</tr>
<tr>
<td style="padding: 8px; word-wrap: break-word; white-space: normal;">Gestational Age at Delivery (GAD)</td>
<td style="padding: 8px; word-wrap: break-word; white-space: normal;"><code>gestational_age_delivery</code></td>
<td style="padding: 8px; word-wrap: break-word; white-space: normal;">Time elapsed between the first day of the birth parent's <span class="tooltip">LMP
		<span class="tooltiptext">last menstrual period, estimated as EDD minus 280 days</span>
	  </span> and the child's date of birth</td>
<td style="padding: 8px; word-wrap: break-word; white-space: normal;">Whole weeks, rounded down to the nearest week</td>
</tr>
</tbody>
</table>


## Tabulated Instrument Data

All [tabulated data](../datacuration/phenotypes.md) include the following fields that report the age of the **child participants** at the time of instrument administration: 

<table style="width: 100%; border-collapse: collapse; table-layout: fixed; font-size: 13px;">
    <thead>
      <tr>
        <th style="width: 20%; padding: 5px; text-align: center;">Name</th>
        <th style="width: 10%; padding: 5px; text-align: center;">Variable Name</th>
        <th style="width: 30%; padding: 5px; text-align: center;">Description</th>
        <th style="width: 20%; padding: 5px; text-align: center;">Unit & Calculation</th>
        <th style="width: 10%; padding: 5px; text-align: center;">Visit(s)</th>
      </tr>
    </thead>
    <tbody>
<tr>
<td style="padding: 8px; word-wrap: break-word; white-space: normal;">Gestational Age at Administration (GAA)</td>
<td style="padding: 8px; word-wrap: break-word; white-space: normal;"><code>&lt;instrument&gt;_gestational_age</code></td>
<td style="padding: 8px; word-wrap: break-word; white-space: normal;">Time from the first day of the birth parent's <span class="tooltip">LMP
		<span class="tooltiptext">Last menstrual period, estimated as EDD minus 280 days</span>
	  </span> to the instrument administration date.
    <span class="tooltip">Max 4 week variation
		<span class="tooltiptext">Varies no more than 4 weeks across protocol elements except when protocol exceptions were granted</span>
	  </span>
    </td>
<td style="padding: 8px; word-wrap: break-word; white-space: normal;">Whole weeks, rounded down to the nearest week</td>
<td style="padding: 8px; word-wrap: break-word; white-space: normal;">V01 only</td>
</tr>
<tr>
<td style="padding: 8px; word-wrap: break-word; white-space: normal;">Chronological Age at Administration</td>
<td style="padding: 8px; word-wrap: break-word; white-space: normal;"><code>&lt;instrument&gt;_candidate_age</code></td>
<td style="padding: 8px; word-wrap: break-word; white-space: normal;">Time from birth (with the birthdate jittered up to 7 days to mitigate identification risks) to the date of instrument administration</td>
<td style="padding: 8px; word-wrap: break-word; white-space: normal;"><span class="tooltip">Years
		<span class="tooltiptext">Reporting in years, rather than months, ensures consistency across developmental stages (e.g., toddlerhood, childhood), while three-decimal precision compensates for birthdate adjustments, yielding values closer to actual age.</span></span> (to 3 decimal places), calculated by dividing the total days elapsed (rounded down) by 365.25</td>
<td style="padding: 8px; word-wrap: break-word; white-space: normal;">V02 onward</td>
</tr>
<tr>
<td style="padding: 8px; word-wrap: break-word; white-space: normal;">Adjusted Chronological Age at Administration (ACAA)</td>
<td style="padding: 8px; word-wrap: break-word; white-space: normal;"><code>&lt;instrument&gt;_adjusted_age</code></td>
<td style="padding: 8px; word-wrap: break-word; white-space: normal;">Time elapsed between the <span class="tooltip">EDD
		<span class="tooltiptext">estimated date of delivery</span>
	  </span> and date of instrument administration</td>
<td style="padding: 8px; word-wrap: break-word; white-space: normal;">Whole weeks, rounded down to the nearest week</td>
<td style="padding: 8px; word-wrap: break-word; white-space: normal;">V02 onward</td>
</tr>
</tbody>
</table>

## Raw File-Based Data

Raw file-based data includes raw magnetic resonance imaging (MRI), spectroscopy (MRS), electroencephalography (EEG), and motion/accelerometry (see [here](../../datacuration/rawbids/#raw-file-based-bids-data) for details). This data is acquired from child participants and is thus unavailable for the prenatal visit V01. For visit V02 onward, age of the child on the date of data acquisition is reported within the subject folder-level `sub-<label>_sessions.tsv` and session folder-level `sub-<label>_ses-<label>_scans.tsv` files via the following:

<table style="width: 100%; border-collapse: collapse; table-layout: fixed; font-size: 13px;">
    <thead>
      <tr>
        <th style="width: 20%; padding: 5px; text-align: center;">Name</th>
        <th style="width: 10%; padding: 5px; text-align: center;">Variable Name</th>
        <th style="width: 30%; padding: 5px; text-align: center;">Description</th>
        <th style="width: 20%; padding: 5px; text-align: center;">Unit & Calculation</th>
        <th style="width: 10%; padding: 5px; text-align: center;">Visit(s)</th>
      </tr>
    </thead>
    <tbody>
<tr>
<td style="padding: 8px; word-wrap: break-word; white-space: normal;">Adjusted Age at Time of Scan</td>
<td style="padding: 8px; word-wrap: break-word; white-space: normal;"><code>age_adjusted</code></td>
<td style="padding: 8px; word-wrap: break-word; white-space: normal;">Time from <span class="tooltip">EDD
		<span class="tooltiptext">estimated date of delivery</span>
	  </span> to the date of data acquisition</td>
<td style="padding: 8px; word-wrap: break-word; white-space: normal;">Days (not rounded)</td>
<td style="padding: 8px; word-wrap: break-word; white-space: normal;">V02 onward</td>
</tr>
<tr>
<td style="padding: 8px; word-wrap: break-word; white-space: normal;">Chronological Age at Time of Scan</td>
<td style="padding: 8px; word-wrap: break-word; white-space: normal;"><code>age</code></td>
<td style="padding: 8px; word-wrap: break-word; white-space: normal;">Time from birth (with the birthdate jittered up to 7 days to mitigate identification risks) to the date of data acquisition.</td>
<td style="padding: 8px; word-wrap: break-word; white-space: normal;"><span class="tooltip">Years
		<span class="tooltiptext">Reporting in years, rather than months, ensures consistency across developmental stages (e.g., toddlerhood, childhood), while 3-decimal precision compensates for birthdate adjustments, yielding values closer to actual age.</span></span> (to three decimal places), calculated by dividing the total days elapsed (rounded down) by 365.25</td>
<td style="padding: 8px; word-wrap: break-word; white-space: normal;">V02 onward</td>
</tr>
</tbody>
</table>





