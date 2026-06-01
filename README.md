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
pip install "git+[https://github.com/pavithriD/my-data-toolkit.git](https://github.com/pavithriD/my-data-toolkit.git)"



## How to Use

> **Important Note:** This tool uses Google Colab's native upload interface and is optimized exclusively for **Google Colab** environments.

Open a blank Google Colab notebook, install the package, and run the complete pipeline using the code below:

```python
from data_analysis.core import DataInspector

# 1. Initialize the tool
inspector = DataInspector()

# 2. Upload your CSV file interactively (opens a Colab pop-up)
inspector.upload_data()

# 3. Handle missing values automatically using the median strategy
inspector.handle_missing_values(strategy='median')

# 4. Generate an interactive correlation heatmap
inspector.plot_associations()

# 5. NEW: Try out the brand new custom visualization plots!
inspector.plot_scatter("Age", "Salary")
inspector.plot_histogram("Salary")
inspector.plot_box("Rating", "Salary")
