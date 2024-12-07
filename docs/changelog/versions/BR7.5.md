# Version: BR7.5

<p style="font-size: 1.1em">Release date: November 19, 2024</p>

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
<b>BioSpecimen toxicology results:</b> Updated file with USDTL urine toxicology results was added  
<li>'bio' domain prepended for column headers of .tsv table  </li>
<li>'bio' domain prepended for filenames ('bio<em>biosample</em>urine.tsv' &amp; 'bio<em>biosample</em>urine.json')  </li>
<li>'participant' and 'session_id) included  </li>
<li>1,232 entries in the file (559 entries filtered out)  </li>
<li>'-999' values were not removed  </li>
<li>Accompanying Data Dictionary is set as placeholder (Not yet updated with Data Dictionary provided). To be updated for BR8 or upcoming iterations.  </li>
</ul>

<ul>
<b>Basic Demographics:</b> Renamed demographic fieldnames to make it more clear what the source of the data is (Ripple vs REDCap)
<li><strong>Ripple:</strong>
<ul>
<li>Mother - 'Demographics Screener' (adm<em>bm</em>screen): 'screen<em>race'; 'screen</em>ethnicity'; 'screen<em>race</em>multi' (to be further specified with 'mother' for BR8)  </li>
<li>Child - Session table (LORIS backend): 'child<em>race'; 'child</em>ethnicity' (currently set to 'n/a')  </li></ul>
</li>
<li><strong>REDCap:</strong>
<ul>
<li>Mother/Child - 'Demographics' form (sed<em>bm</em>demo): 'rc<em>mother</em>race'; 'rc<em>mother</em>ethnicity'; rc<em>child</em>race'; 'rc<em>child</em>ethnicity'</li></ul>
</li>
</ul>