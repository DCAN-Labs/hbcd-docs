# Access & Download Data

## How To Obtain Access To HBCD Study Data

<div style="display: flex; justify-content: space-between; align-items: center;">
  <img src="../images/NBDC-C-Horizontal.png" alt="NBDC-logo" style="width: 40%;">
  <img src="../images/Format=Horizontal, Color=Black@2x.png" alt="Lasso-logo" style="width: 30%; margin-right: 80px;">
</div>

HBCD Study data is publicly shared via the NBDC [Data Use Certification (DUC)](https://nbdc-splash-beta.lassoinformatics.com/data-access-process) that researchers sign in agreement to follow the rules outlined for data use. DUC submission is conducted through the [NBDC portal supported by Lasso](https://nbdc-hbcd-beta.lassoinformatics.com). The steps for signing onto this platform and submitting a DUC are outlined here [ADD LINK]().

## How To Download HBCD Study Data

After obtaining data access, users can download HBCD Study release data via the **[Lasso Portal]()** or **Data Exploration and Analysis Portal**  ([DEAP]()) - ADD LINKS.

<p style="text-align: center;">
  <a class="button-link" href="https://nbdc-splash-beta.lassoinformatics.com/hbcd-study">HBCD Study on NBDC Data Hub &nbsp; ↗️</a>
</p>

### Lasso HBCD User Warnings

#### <span style = "color: #ffa500;" class="fas fa-exclamation-triangle"></span> Additional Columns (`cohort` & `site`) Not Defined in Data Dictionary
Dataset downloads from Lasso will automatically contain two additional columns that are not currently described in the data dictionary: `cohort` (*HBCD Main Child*) and `site` (*site ID*). The `cohort` and `site` columns are identical to the [Visit Information](../measures/demographics/#visit-information) variables `par_visit_data_cohort` and `par_visit_data_site`, respectively.


#### <span style = "color: #ffa500;" class="fas fa-exclamation-triangle"></span> Blank Columns in Query Tool

The following columns are currently blank in the Lasso Dictionary Query Tool for the HBCD Study and will become available in a future release (columns not applicable to HBCD and thus expected to be blank are noted [here](#dd-faq)): **unit**, column names appended with **\*_es**, and columns prepended with **url_\***.

## Explore Data

HBCD data is organized into tables, each of which contains a set of variables. The data dictionary provides detailed information about each variable in the HBCD data tables. The dictionary includes the variable name, label, description, data type, and other relevant information. 

Prior to obtaining data access via DUC, users can explore the NBDC Data Hub data dictionary via the **[Lasso Portal Query Tool]()** or **[DEAP]()** - ADD LINKS. Below are the definitions for the columns in the data dictionaries for these utilities. Note that some columns also correspond to elements in the BIDS JSON files that accompany all tabulated data (hover over <i class="bi bi-filetype-json" style="font-size:18px; color:blue;"></i> icon for details in table below).

<div id="dd-faq" class="notification-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fa-regular fa-lightbulb"></i></span>
  <span class="text">Why are some data dictionary columns empty?</span>
  <span class="notification-arrow">▸</span>
</div>
<div class="notification-collapsible-content">
<p>There are NBDC data dictionary column names that are currently inapplicable to HBCD study data and thus excluded from the table below. Note that these columns will still be present when querying the data dictionary via the Lasso Portal or DEAP, but the column values will be blank. Examples include <b><code>atlas</code></b>, <b><code>metric</code></b>, <b><code>sub_domain</code></b>, columns including <b><code>nda/deap/redcap</code></b>, etc. These columns can be safely ignored. Also see the <a href="#blank-columns-in-query-tool">Lasso User Warning</a> in the section above.</p>
</div>

<div id="table-banner" class="table-banner" onclick="toggleCollapse(this)">
  <span class="table-text">Data Dictionary Column Definitions</span>
  <span class="arrow">▸</span>
</div>
<div class="table-open-collapsible-content">
<table style="width: 100%; border-collapse: collapse; table-layout: fixed; font-size: 13px;">
    <thead>
      <tr>
        <th style="width: 20%; border: 1px solid #ddd; padding: 5px; text-align: center;">Column Name<br>(DEAP)</th>
        <th style="width: 5%; border: 1px solid #ddd; padding: 5px; text-align: center;">Column Name<br>(Lasso)</th>
        <th style="width: 30%; border: 1px solid #ddd; padding: 5px; text-align: center;">Description</th>
        <th style="width: 25%; border: 1px solid #ddd; padding: 5px; text-align: center;"><b>{</b>Possible Values<b>}</b> / Example(s)</th>
        <th style="width: 5%; border: 1px solid #ddd; padding: 5px; word-wrap: break-word; white-space: normal; text-align: center;">
            <span class="tooltip tooltip-left">Mutable
                <span class="tooltiptext">Values may vary between releases</span>
            </span></th>
      </tr>
    </thead>
    <tbody>
    <tr>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">Study</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">study</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">Indicates if table/measure is part of core or sub/auxiliary study</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;"><b>{</b>Core; Substudy<b>}</b></td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">NO</td>
    </tr>
    <tr>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">Domain</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">domain</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">Domain/Workgroup</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">
        <span class="tooltip">Demographics; EEG
        <span class="tooltiptext">See full list under <a href="../../measures/#tabulated-data">Tabulated Data</a></span>
      </span></td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">NO</td>
    </tr>
    <tr>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">Table name</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">table_name</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">Name of table/measure</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;"><code>mh_p_cbcl</code></td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">NO</td>
    </tr>
    <tr>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">Table label&nbsp;
        <span class="tooltip tooltip-right"><i class="bi bi-filetype-json" style="font-size:18px;"></i>
        <span class="tooltiptext">Corresponds to MeasurementToolMetadata > Description in BIDS JSON</span>
      </span>
      </td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">table_label</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">Label for table/measure</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">Child Behavior Checklist [Parent]</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">YES</td>
    </tr>
    <tr>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">Variable name</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">name</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">Name of column/variable/question</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;"><code>mh_p_cbcl__aggr_001</code></td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">NO</td>
    </tr>
    <tr>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">Variable label&nbsp;
        <span class="tooltip tooltip-right"><i class="bi bi-filetype-json" style="font-size:18px;"></i>
        <span class="tooltiptext">Corresponds to Description in BIDS JSON</span>
      </span>
      </td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">label</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">Label for column/variable/question</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">"Demands a lot of attention"</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">YES</td>
    </tr>
    <tr>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">Instruction</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">instruction</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">Instructions preceding table/measure questions</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">"The next set of question is about your child's behavior in different situations and contexts. Please fill in a response to all questions."</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">YES</td>
    </tr>
    <tr>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">Header</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">header</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">Header/instructions for a set of questions</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">"Below is a list of items that describe children and youths. For each item that describes your child <span class="tooltip"><strong>...</strong>
        <span class="tooltiptext">... now or within the past 6 months, please choose whether the item is very true or often true of your child, somewhat or sometimes true of your child, or not true of your child. Please answer all items as well as you can, even if some do not seem to apply to your child."</span>
      </span>
     </td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">YES</td>
    </tr>
    <tr>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">Note</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">note</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">Note displayed to participants</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">"Enter weight in pounds."</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">YES</td>
    </tr>
    <tr>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">Unit&nbsp;
        <span class="tooltip tooltip-right"><i class="bi bi-filetype-json" style="font-size:18px;"></i>
        <span class="tooltiptext">Corresponds to Units in BIDS JSON</span>
      </span>
      </td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">unit</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">Unit of measurement</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">m, cm2, lbs</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">YES</td>
    </tr>
    <tr>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">Variable type&nbsp;
        <span class="tooltip tooltip-right"><i class="bi bi-filetype-json" style="font-size:18px;"></i>
        <span class="tooltiptext">Derivative element in BIDS JSON set to <i>true</i> if <i>type_var</i> = <i>summary score</i> or <i>derived item</i></span>
      </span>
      </td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">type_var</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">Type of column/variable/question</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;"><b>{</b>
        <span class="tooltip">administrative
        <span class="tooltiptext">Data that gives context to the assessments, e.g. date of assessment, language, quality control, etc.</span>
      </span>;
      <span class="tooltip">item
        <span class="tooltiptext">Original data provided by the participant, e.g. questions in a questionnaire</span>
      </span>; 
      <span class="tooltip">derived item
        <span class="tooltiptext">Derived from original data provided by the participant - e.g. if the participant filled in two fields to enter their height in feet and inches, a derived item could integrate this information into one field that provides the height in inches</span>
      </span>; <span class="tooltip">summary score
        <span class="tooltiptext">Summary and/or score output based on algorithmic conversions of items/raw data</span>
      </span><b>}</b></td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">YES</td>
    </tr>
    <tr>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">Data type</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">type_data</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">Data type (in database)</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;"><b>{</b>date; timestamp; time;
      <span class="tooltip">character
        <span class="tooltiptext">Character only used for categorical columns</span>
      </span>;
      text; integer; double<b>}</b></td>
    </td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">NO</td>
    </tr>
    <tr>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">Level of measurement</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">type_level</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">Measurement level/scale type</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;"><b>{</b>nominal; ordinal; interval; ratio<b>}</b></td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">YES</td>
    </tr>
    <tr>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">Field type</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">type_field</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">Field type in data capture system as presented to participant</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">dropdown; radio; checkbox</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">YES</td>
    </tr>
    <tr>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">Display order</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">order_display</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">Display order of item within measure</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">&nbsp;</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">YES</td>
    </tr>
    <tr>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">Branching logic</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">branching_logic</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">Branching logic applied to column/variable/question</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">&nbsp;</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">YES</td>
    </tr>
    <tr>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">Label (Spanish)</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">label_es</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">Label (Spanish)</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">&nbsp;</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">YES</td>
    </tr>
    <tr>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">Instruction (Spanish)</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">instruction_es</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">Instruction (Spanish)</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">&nbsp;</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">YES</td>
    </tr>
    <tr>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">Header (Spanish)</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">header_es</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">Header (Spanish)</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">&nbsp;</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">YES</td>
    </tr>
    <tr>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">Note (Spanish)</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">note_es</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">Note (Spanish)</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">&nbsp;</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">YES</td>
    </tr>
  <tr>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">Required field (LORIS)</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;"><i>Not present</i></td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">Specifies if a field is required in LORIS</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">&nbsp;</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">YES</td>
    </tr>
    <tr>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">Collection Platform</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;"><i>Not present</i></td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">Platform the data was collected with</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">&nbsp;</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">YES</td>
    </tr>
    <tr>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">Identifier column(s)</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">unique_identifiers</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">Unique identifier column names (variable/table)</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">&nbsp;</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">NO</td>
    </tr>
    <tr>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">Documentation for table</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">url_table</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">Link to description in <a href="../../measures#data-measure-release-notes" target="_blank">Release Notes</a></td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">&nbsp;</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">YES</td>
    </tr>
    <tr>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">Responsible data use warning (table)</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">url_table_warn_use</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">Link to <a href="../resp_data_use/#warnings" target="_blank">responsible use warning</a> (table)</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">&nbsp;</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">YES</td>
    </tr>
    <tr>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">Data quality warning (table)</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">url_table_warn_data</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">Link to <a href="../resp_data_use/#warnings" target="_blank">data warning</a> (table)</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">&nbsp;</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">YES</td>
    </tr>
    <tr>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">Responsible data use warning (variable)</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">url_warn_use</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">Link to <a href="../resp_data_use/#warnings" target="_blank">responsible use warning</a> (variable)</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">&nbsp;</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">YES</td>
    </tr>
    <tr>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">Data quality warning (variable)</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">url_warn_data</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">Link to <a href="../resp_data_use/#warnings" target="_blank">data warning</a> (variable)</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">&nbsp;</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">YES</td>
    </tr>
    <tr>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">Sort order</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">order_sort</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">Standard sort order in table/measure (and ⇒ column order in data/database)</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">&nbsp;</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">YES</td>
    </tr>
</tbody>
</table>
</div>

##