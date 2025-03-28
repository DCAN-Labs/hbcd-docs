# Tabulated Data [🚧 UNDER CONSTRUCTION 🚧]
## Plain text vs. Parquet files
Tabulated data in the BIDS `rawdata/phenotype/` directory are available in both tab-separated values (TSV) and [Apache Parquet](https://parquet.apache.org/) formats. Some concatenated, file-based data are also offered as CSV and Parquet files.

Plain text formats (TSV/CSV) are widely compatible and easy to inspect, but become inefficient for large datasets. They lack support for partial loading of only selected columns and cannot store important metadata such as column data types. As a result, tools like Python or R must guess data types during import, leading to inaccuracies. For example, integers may be misread as doubles, or categorical values stored as characters (e.g., "0" for No, "1" for Yes), as is often the case for NBDC datasets, may be treated as numeric. In addition, columns with mostly missing values may even be misinterpreted as empty (by default, the import functions only consider the first n rows to infer the data type and may interpret the column as an empty if those n rows all have missing values).

To avoid these issues when using plain text files, it's strongly recommended to manually define column types based on the accompanying data dictionary. The `NBDCtools` R package provides a convenient wrapper function, `read_dsv_formatted()`, to automate this process (see [Recommended Programs](recprograms.md#tabulated-data) for details).

In contrast, [Apache Parquet](https://parquet.apache.org/documentation/latest/) is a modern, columnar, compressed format designed for scalable and efficient data processing. Parquet is compatible with common data science tools such as Python, R, Spark, and Matlab and particularly useful for large datasets. Compression reduces file sizes on disk, and columnar storage allows for column-wide loading, improving loading speed and memory usage to enhance performance for analytical workflows. Finally, metadata (including column types, variable/value labels, and categorical codes) is embedded directly in the file, ensuring accurate data import without manual specification (see [here] for how this feature is used when exporting tabulated data using DEAP).

**Example: Loading data in Python and R:**

```bash
# Loading data in Python (using `pandas` module):
import pandas as pd
parquet_df = pd.read_parquet("path/to/file.parquet")

# Loading the data in R (requires 'arrow' package):
library(readr)  
library(arrow)
parquet_df <- read_parquet("path/to/file.parquet")
```
Both formats are provided to support a range of tools and user preferences. However, **we recommend using Parquet for NBDC tabulated data to take advantage of automatically correctly specified data types, faster loading speeds, and lower memory usage.**


## Shadow Matrix
Each TSV/Parquet ***data file*** has a corresponding ***shadow matrix file*** that mirrors the data file structure and column names. Shadow matrix files can be exported as CSV files via Lasso when running a query (see details [here](../lasso.md#step-5-query-the-associated-data)) DEAP when downloading data (see [here](../overview.md) for a description of how to export data using Lasso or DEAP).

In the main data files, missing values appear as blank cells. The shadow matrix provides essential context by reporting *the reason why a value is missing*. Each cell in the shadow matrix corresponds to the same cell in the data file:

- If the data cell contains a value, the shadow matrix cell is blank.
- If the data cell is missing, the corresponding shadow matrix cell includes a code or description indicating why the data is missing (e.g., “don’t know,” “decline to answer,” “missed visit”).

[ADD VISUAL HERE THAT SHOWS THE STRUCTURE OF DATA AND SHADOW FILE]

In HBCD, some participant responses like “Don’t know” or “Decline to answer” are deliberately converted to missing values in the data file, with the original response reason stored in the shadow matrix. This prevents analytical errors such as inadvertently treating placeholder codes (like `777` or `999`, common in other datasets) as valid numeric values during analysis.

While this approach supports cleaner analyses, there are situations where non-responses are themselves meaningful. For example, a researcher might be interested in how often participants do not understand a given question and how this relates to other variables. In such cases, users can re-integrate the non-responses from the shadow matrix back into the data. 

### Working with Shadow Matrices in R and Python 
To help researchers to use the shadow matrix files in combination with the data files, e.g., to explore and understand patterns of missing data, the following provides helper functions for both **Python** and **R** which automatically join the tabulated data file with its corresponding shadow matrix file so data columns are combined with columns columns providing the reasons for missingness in the same data frame.
These functions let you:

* Quickly inspect why data is missing (e.g., "`NOT_COLLECTED`", "`DECLINED`")  
* Integrate missingness reasons into your analysis or filtering  
* Use tools like `missingno` (Python) or `naniar` (R) for visualization and QC

🐍 Python Helper Function (using pandas)  

```
python  
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
# df = load_data_with_shadow("data.csv", "shadow_matrix.csv")  
# df[df["income"].isna()][["income_missing_reason"]]  # View reasons for missing income  
```

<i class="fa fa-bar-chart"></i> Optional: R Helper Function (using `tidyverse` and `naniar`) for visualization  

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
# df <- load_data_with_shadow("data.csv", "shadow_matrix.csv")  
# vis_miss(df)  # Visualize missingness and reasons  
```
