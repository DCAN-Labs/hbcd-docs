# Tabulated Data

## Plain Text vs. Parquet Files
Tabulated data in the BIDS `rawdata/phenotype/` directory includes demographic, toxicology, and behavioral data (see details [here](../../datacuration/phenotypes.md)) available in both tab-separated values (TSV) and [Apache Parquet](https://parquet.apache.org/) formats. Some concatenated, file-based data are also offered as CSV and Parquet files. Both formats are provided to support a range of tools and user preferences. However, **we recommend using Parquet for NBDC tabulated data to ensure correctly specified data types, faster loading speeds, and lower memory usage.**

### Plain Text (TSV/CSV)
Plain text formats (TSV/CSV) are widely compatible and easy to inspect, but less efficient for large datasets. They don't support selective column loading or preserve metadata, such as data type specification. As a result, tools like Python or R must guess data types during import, often incorrectly. For example, categorical values like "0"/"1" for "Yes"/"No" (commonly used in NBDC datasets) may be interpreted as numeric, and columns with mostly missing values may be treated as empty if the first few rows lack data.

To avoid such issues, it's recommended to manually define column types using the accompanying data dictionary during the import. The `NBDCtools` R package offers a helper function, `read_dsv_formatted()`, to automate this process (see [Recommended Programs](recprograms.md#tabulated-data) for details).

### Parquet
<div id="parquetbids" class="notification-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fa-regular fa-lightbulb"></i></span>
  <span class="text">Note: Parquet Not Currently Supported by BIDS</span>
  <span class="arrow">▸</span>
</div>
<div class="collapsible-content">
<p>Please note that Parquet files are not officially supported by the <a href="https://bids-specification.readthedocs.io/en/stable/">BIDS specification</a>. For NBDC datasets, we decided to add Parquet as an alternative file format to the BIDS standard TSV to allow users to take advantage of the features of this modern and efficient open source format that is commonly used in the data science community.</p>
</div>

[Apache Parquet](https://parquet.apache.org/documentation/latest/) is a modern, compressed, columnar format optimized for large-scale data. In contrast to TSV files, Parquet supports selective column loading and smaller file sizes. This improves loading speed and memory usage and enhances performance for analytical workflows. Crucially, parqet can store metadata (including column types, variable/value labels, and categorical coding) directly in the file, enabling accurate import without manual setup (see [here] for how DEAP handles Parquet export).


<p style="margin-bottom: 0; padding-bottom: 0;"><b>Example: Loading parquet file in Python (using <a href="https://docs.pola.rs/">polars</a> or <a href="https://pandas.pydata.org/docs/getting_started/index.html">pandas</a> modules)</b></p>

```bash
# Using `polars` module [RECOMMENDED]:
import polars as pl
parquet_df = pl.read_parquet("path/to/file.parquet")

# Using `pandas` module:
import pandas as pd
parquet_df = pd.read_parquet("path/to/file.parquet")
```

<p style="margin-bottom: 0; padding-bottom: 0;"><b>Example: Loading parquet file in R (<a href="https://arrow.apache.org/docs/r/">arrow</a> package):</b></p>

```bash 
# Using `arrow` package:
library(arrow)
parquet_df <- read_parquet("path/to/file.parquet")
```

## Shadow Matrices
Each TSV and Parquet ***data file*** in the BIDS `/rawdata/phenotype/` directory has a corresponding ***shadow matrix file*** in the same format (TSV or Parquet). These shadow matrix files mirror the structure and column names of the original data files. Shadow matrices can be exported as CSV files via Lasso when running a query (see details [here](../lasso.md#step-5-query-the-associated-data)) or downloaded in a chosen file format via DEAP (see details [here]() - ADD LINK).

In the data files, missing values are represented as blank cells. Shadow matrices provide essential context by indicating why a value is missing. Each cell in a shadow matrix corresponds to the same cell in the associated data file:

- If a data cell contains a value, the corresponding shadow matrix cell is blank.
- If a data cell is missing, the corresponding shadow matrix cell includes a code or description indicating the reason (e.g., “don’t know,” “declined to answer,” “missed visit”), as illustrated below by the <mark style="background-color: #f9cb9b; font-weight: normal;">highlighted cells</mark> in the data file (*left*) vs. the corresponding shadow matrix (*right*).

![](../images/shadowmatrix.png)

In HBCD, some participant responses like “Don’t know” or “Decline to answer” (which are typically considered non-responses) are deliberately converted to missing values in the data file, with the original response converted to a missingness reason stored in the shadow matrix. This prevents analytical errors such as inadvertently treating placeholder codes (like `777` or `999`, common in other datasets) as valid numeric values during analysis.

<div id="shadowFYI" class="notification-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fa-regular fa-lightbulb"></i></span>
  <span class="text">When should I use shadow matrices?</span>
  <span class="arrow">▸</span>
</div>
<div class="collapsible-content">
<p>While the approach of storing missingness reasons in a shadow matrix file supports cleaner analyses, there are situations where non-responses are themselves meaningful. For example, a researcher might be interested in how often participants do not understand a given question and how this relates to other variables. In such cases, users can re-integrate the non-responses from the shadow matrix back into the data.</p>
</div>

### Working with Shadow Matrices in R and Python 
Below we provide helper functions (for both **Python** and **R**) to help researchers with using the shadow matrix files in combination with the data files to, for example, explore and understand patterns of missing data. These functions join the tabulated data file with its corresponding shadow matrix file so data columns are combined with columns providing the reasons for missingness in the same data frame.
These functions let you:

* Quickly inspect why data is missing (e.g., `Decline to Answer`, `Logic Skipped`, etc.)  
* Integrate missingness reasons into your analysis or use them during filtering  
* Generate missing data visualizations to help understand patterns of missingness

### 🚧 UNDER CONSTRUCTION 🚧 - CODE NEEDS TO BE TESTED
#### 🐍 Python Helper Function 
```
import pandas as pd

def load_data_with_shadow(data_path, shadow_path):  
    """  
    Loads a data CSV and its corresponding shadow matrix,  
    and returns a DataFrame with an added '_missing_reason' suffix column  
    for each column with missing data.  
    """  
    data = pd.read_csv(data_path)  
    shadow = pd.read_csv(shadow_path)

    # Annotate data with missingness reason columns  
    for col in data.columns:  
        if col in shadow.columns:  
            data[f"{col}_missing_reason"] = shadow[col]

    return data

# Example usage:  
df = load_data_with_shadow("data.csv", "shadow_matrix.csv")  
df[df["income"].isna()][["income_missing_reason"]]  # View reasons for missing income  
```

#### <i class="fa fa-bar-chart"></i> R Helper Function For Visualization  
```
library(readr)  
library(dplyr)  
library(naniar)

load_data_with_shadow <- function(data_path, shadow_path) {  
  data <- read_csv(data_path, show_col_types = FALSE)  
  shadow <- read_csv(shadow_path, show_col_types = FALSE)

  # Rename shadow columns with _NA suffix (required by naniar)  
  colnames(shadow) <- paste0(colnames(shadow), "_NA")

  # Bind the data and the shadow matrix  
  combined <- bind_cols(data, shadow)

  return(combined)  
}

# Example usage:  
df <- load_data_with_shadow("data.csv", "shadow_matrix.csv")  
vis_miss(df)  # Visualize missingness and reasons  
```
