# Version: BR8

<p style="font-size: 1.1em">Release date: November 26, 2024</p>

<ul>
<p style="font-size: 1.1em; margin-bottom: 0px;"><u>Total number of unique participants and visits included in data dump:</u></p>
<li>1,358 unique participants  </li>
<li>1,919 visits
<ul>
<li>V01 visits: 1,127 (185 participants for which only V01 visit exists)  </li>
<li>V02 visits: 666  </li>
<li>V03 visits: 126</li></ul>
</li>
</ul>

## New Features
<ul>
<b>Parquet files set up:</b>
<li>Setup for generation of parquet files, including libraries (read, write and build schema) and dependencies for LORIS  </li>
<li>Includes 'skip_parquet' option to enable/disable feature (to avoid generating parquet files until these are ready to be run)  </li>
<li>Currently disabled so no parquet files have been generated yet  </li>
</ul>

<ul>
<b>BioSpecimen toxicology results:</b>   
<li>Filtered entries based on 'collect_date' up to cutoff date of July 1, 2024 (201 entries removed)  </li>
<li>Accompanying Data Dictionary placeholders added for Lasso compatibility  </li>
<li>Not yet updated with Data Dictionary provided by WG  </li>
</ul>

<ul>
<b>Basic Demographics:</b>   
<li>Added new details to demographic fieldnames (Specify source of the data; e.g. Ripple vs REDCap)    </li>
</ul>

## Data Conversions
<ul>
<b>Label adjustments:</b>   
<li>Converted '_i_' section of instrument name to '__'   </li>
</ul>

## Filters
<ul>
<li>Visit Data: <br />
<ul>
<li>Applied filter to only include visits whose 'status' is 'LaunchPad Complete'  </li></ul>
</li>
<li>Only include visits V01 to V03  </li>
<li>Excluded 'screen_household_income' field for 'basic_demographics' category</li>
</ul>