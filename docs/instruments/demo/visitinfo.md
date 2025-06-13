# Visit Information

**Table Name**: `par_visit_data`       

<p style="margin: 0 0 5px;">Visit information contains all participant visit data, including:</p>
<ul>
<li>Visit information: Label, Stage, Date, if the visit was missed, and the reason if visit was missed</li>
<li>Project, <a href="#cohorts">Cohort</a>, and Site</li>
<li>Withdrawal information: if the participant withdrew from the study, the reason, and date</li>
<li>Protocol violation information: if there was a protocol exception and the date</li>
<li>Substance use flags raised by any of the following:
<ul>
<li><a href="../../measures/pregexp/substanceuse#tlfb">TLFB</a> (Self-reported use)
<li><a href="../../measures/biospec">Biospecimen results</a>
<li><a href="../../measures/pregexp/preghealth#instruments">Infant health- V2</a> Field <code>007</code> when option 1 (NOWS - Neonatal Opioid Withdrawal Syndrome) or 5 (FAS - Fetal Alcohol Syndrome) was selected</li>
</ul>
</ul>

<div id="cohorts" class="notification-banner" onclick="toggleCollapse(this)">
  <span class="text">Cohort & Caregiver Types</span>
  <span class="arrow">▸</span>
</div>
<div class="notification-open-collapsible-content">
<p>Cohort types included in the data release are as follows, with each listed item indicating a specific subtype or Caregiver Type (e.g., "HBCD Main Child - Postnatal Recruitment"):</p>
<ul>
<li><strong>HBCD Main Child -</strong> <em>Postnatal Recruitment</em>, <em>Type A-F</em></li>
<li><strong>HBCD Multiple Birth -</strong> <em>Main Child</em>, <em>Postnatal Recruitment</em>, <em>Postnatal Recruitment - Sibling</em>, <em>Type A-F</em></li>
</ul>
<b>Caregiver Type A-F Definitions</b>
<table style="width: 100%; border-collapse: collapse; table-layout: fixed;">
<tbody>
    <tr>
        <td>Type A</td>
        <td>Temporary Alternative Caregiver</td>
    </tr>
    <tr>
        <td>Type B</td>
        <td style="word-wrap: break-word; white-space: normal;">Change in Primary Caregiver (Placement Only) Without Change in Legal Custody (But Birth Parent Unable to Complete Visit)</td>
    </tr>
    <tr>
        <td>Type C</td>
        <td>Change in Joint Custody</td>
    </tr>
    <tr>
        <td>Type D</td>
        <td style="word-wrap: break-word; white-space: normal;">Child Removed From Birth Parent and Placed in Foster Care (Change in Placement)</td>
    </tr>
    <tr>
        <td>Type E</td>
        <td>Change in Legal Custody and Placement (e.g. adoption)</td>
    </tr>
    <tr>
        <td>Type F</td>
        <td>Original Consented Parent</td>
    </tr>            
</tbody>
</table>
</div>

