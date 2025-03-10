# How To Download Data: DEAP

<p style="text-align: center; font-size: 1.6em">🚧 UNDER CONSTRUCTION 🚧</p>

## Create Custom Datasets
The Data Exploration and Analysis Portal (DEAP) can be used to explore and download HBCD data. It has two main pages:

The **Variable Selection** page allows users to explore the ontology of data tables, i.e., their hierarchical organization into domains and subdomains, as well as the data dictionary, i.e., how variables are grouped into different tables, in an interactive manner and provides extensive filter and search capabilities. Users can select variables and add them to a selection of variables of interest.

The **Manage Selections and Downloads** page allows users to manage their selection of variables and download a data dictionary containing just these variables. (This application does not allow to download the data itself. Users with a valid data use certificate can download the data through Lasso).

Note that warning labels are included next to relevant variables and tables; these link directly to Data and Responsible Use warnings provided in the release notes - see [here](resp_data_use.md#warnings) for details. 

<div id="level" class="table-banner" onclick="toggleCollapse(this)">
  <span class="table-text">Level Term Definitions</span>
  <span class="arrow">▸</span>
</div>
<div class="table-open-collapsible-content">
<table style="width: 100%; border-collapse: collapse; table-layout: fixed; font-size: 13px;">
    <thead>
      <tr>
        <th style="width: 10%; border: 1px solid #ddd; padding: 5px; text-align: center;">Column Name</th>
        <th style="width: 10%; border: 1px solid #ddd; padding: 5px; word-wrap: break-word; white-space: normal; text-align: center;">JSON Element</th>
        <th style="width: 35%; border: 1px solid #ddd; padding: 5px; text-align: center;">Description</th>
        <th style="width: 10%; border: 1px solid #ddd; padding: 5px; text-align: center;">Example</th>
        <th style="width: 5%; border: 1px solid #ddd; padding: 5px; word-wrap: break-word; white-space: normal; text-align: center;">
      <span class="tooltip tooltip-left">Mutable
        <span class="tooltiptext">Can change across releases</span>
      </span></th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td style="border: 1px solid #ddd; padding: 4px; word-wrap: break-word; white-space: normal;">name</td>
        <td style="border: 1px solid #ddd; padding: 4px; word-wrap: break-word; white-space: normal;">&nbsp;</td>
        <td style="border: 1px solid #ddd; padding: 4px; word-wrap: break-word; white-space: normal;">Name of the categorical column/variable/question for which value/label pairs are reported</td>
        <td style="border: 1px solid #ddd; padding: 4px; word-wrap: break-word; white-space: normal;">&nbsp;</td>
        <td style="border: 1px solid #ddd; padding: 4px; word-wrap: break-word; white-space: normal;">NO</td>
      </tr>
      <tr>
        <td style="border: 1px solid #ddd; padding: 4px; word-wrap: break-word; white-space: normal;">value</td>
        <td style="border: 1px solid #ddd; padding: 4px; word-wrap: break-word; white-space: normal;">left hand side</td>
        <td style="border: 1px solid #ddd; padding: 4px; word-wrap: break-word; white-space: normal;">Value of the level</td>
        <td style="border: 1px solid #ddd; padding: 4px; word-wrap: break-word; white-space: normal;">1</td>
        <td style="border: 1px solid #ddd; padding: 4px; word-wrap: break-word; white-space: normal;">NO</td>
      </tr>
      <tr>
        <td style="border: 1px solid #ddd; padding: 4px; word-wrap: break-word; white-space: normal;">order_level</td>
        <td style="border: 1px solid #ddd; padding: 4px; word-wrap: break-word; white-space: normal;"></td>
        <td style="border: 1px solid #ddd; padding: 4px; word-wrap: break-word; white-space: normal;">
          <span class="tooltip">Position of the level
            <span class="tooltiptext">Indicates the order in which response options were displayed to participants and how they should be presented to data users in applications</span>
          </span></td>
        <td style="border: 1px solid #ddd; padding: 4px; word-wrap: break-word; white-space: normal;">2</td>
        <td style="border: 1px solid #ddd; padding: 4px; word-wrap: break-word; white-space: normal;">YES</td>
      </tr>
      <tr>
        <td style="border: 1px solid #ddd; padding: 4px; word-wrap: break-word; white-space: normal;">label</td>
        <td style="border: 1px solid #ddd; padding: 4px; word-wrap: break-word; white-space: normal;">right hand side</td>
        <td style="border: 1px solid #ddd; padding: 4px; word-wrap: break-word; white-space: normal;">Label of the level</td>
        <td style="border: 1px solid #ddd; padding: 4px; word-wrap: break-word; white-space: normal;">Yes</td>
        <td style="border: 1px solid #ddd; padding: 4px; word-wrap: break-word; white-space: normal;">YES</td>
      </tr>
      <tr>
        <td style="border: 1px solid #ddd; padding: 4px; word-wrap: break-word; white-space: normal;">label_es</td>
        <td style="border: 1px solid #ddd; padding: 4px; word-wrap: break-word; white-space: normal;"></td>
        <td style="border: 1px solid #ddd; padding: 4px; word-wrap: break-word; white-space: normal;">Label of the level (Spanish)</td>
        <td style="border: 1px solid #ddd; padding: 4px; word-wrap: break-word; white-space: normal;">Si</td>
        <td style="border: 1px solid #ddd; padding: 4px; word-wrap: break-word; white-space: normal;">YES</td>
      </tr>
</table>
</div>

## Download Datasets

## Organize & Share Datasets




