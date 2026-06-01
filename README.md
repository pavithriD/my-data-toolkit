# My Custom Data Analysis Toolkit

## Overview
A robust Python toolkit designed for automated data cleaning, quick exploration, and interactive visualization within Google Colab environments. This tool simplifies common preprocessing tasks such as data sanitization, missing value imputation, and correlation mapping into just a few lines of code.

---

## Features
* **Intelligent Data Loading:** Automatically detects and handles common empty strings (like `'?'`, `'N/A'`, `'NULL'`) when importing datasets.
* **Automated Cleaning:** Identifies missing values and automatically fills them using mean, median, or most frequent (mode) strategies depending on the data type.
* **Interactive Visualizations:** Generates a dynamic, interactive correlation heatmap powered by Plotly to quickly find relationships between your numeric variables.

---

## Installation

You can install this toolkit directly from GitHub into any Google Colab notebook by running the following command:

```bash
pip install "git+https://github.com/pavithriD/my-data-toolkit.git"

## How to Use

> **Important Note:** This tool uses Google Colab's native upload interface and is optimized exclusively for **Google Colab** cloud environments.

Open a blank Google Colab notebook, install the package, and run the pipeline using the code below.

### Option A: Fully Automated Mode (The tool chooses for you)
If you don't provide any column names, the tool automatically detects your data types and selects relevant columns for your charts:

```python
from data_analysis.core import DataInspector

inspector = DataInspector()
inspector.upload_data()
inspector.handle_missing_values(strategy='median')

# Generates all charts completely automatically!
inspector.plot_associations()
inspector.plot_scatter()    
inspector.plot_histogram()  
inspector.plot_box()

###Option B: Custom Mode (Choose your own columns)
If you want to look at specific variables in your dataset, simply pass your exact CSV column headers as text strings inside the parentheses:

# Compare two specific numerical columns side-by-side
inspector.plot_scatter(x_column="Age", y_column="Salary")

# Look at the distribution of one specific numerical column
inspector.plot_histogram(column="Salary")

# Break down a numerical column by a categorical group column
inspector.plot_box(x_column="Rating", y_column="Salary")


