import pandas as pd
import numpy as np
import plotly.express as px
import io
from google.colab import files

class DataInspector:
    def __init__(self):
        self.df = None

    def upload_data(self):
        """Triggers a file upload pop-up in Google Colab and reads a CSV."""
        print("Please upload your CSV file:")
        uploaded = files.upload()
        
        # Get the name of the uploaded file
        file_name = list(uploaded.keys())[0]
        
        # Read the file into a Pandas DataFrame, catching common null strings
        null_flags = ["?", "N/A", "NULL", "null"]
        self.df = pd.read_csv(io.BytesIO(uploaded[file_name]), na_values=null_flags)
        
        print(f"\nSuccessfully loaded {file_name}!")
        print(f"Dataset has {self.df.shape[0]} rows and {self.df.shape[1]} columns.")

    def handle_missing_values(self, strategy='median'):
        if self.df is None:
            print("Error: No data loaded. Run upload_data() first.")
            return
        for col in self.df.columns:
            if self.df[col].isnull().any():
                if self.df[col].dtype in ['int64', 'float64']:
                    if strategy == 'median':
                        fill_value = self.df[col].median()
                    elif strategy == 'mean':
                        fill_value = self.df[col].mean()
                    self.df[col].fillna(fill_value, inplace=True)
                else:
                    self.df[col].fillna(self.df[col].mode()[0], inplace=True)
        print(f"Data cleaning complete. All missing values filled using '{strategy}'.")

    def plot_associations(self):
        """Generates a data correlation heatmap."""
        if self.df is None:
            print("Error: No data loaded.")
            return
        numeric_df = self.df.select_dtypes(include=['int64', 'float64'])
        if numeric_df.empty:
            print("No numeric columns found to correlate.")
            return
        corr_matrix = numeric_df.corr()
        fig = px.imshow(corr_matrix, text_auto=True, color_continuous_scale='RdBu_r', title="Data Correlation Heatmap")
        fig.show()

    def plot_scatter(self, x_column, y_column):
        """Generates a scatter plot comparing two numerical variables."""
        if self.df is None:
            print("Error: No data loaded.")
            return
        fig = px.scatter(self.df, x=x_column, y=y_column, title=f"Scatter Plot: {x_column} vs {y_column}", template="plotly_white")
        fig.show()

    def plot_histogram(self, column):
        """Generates a histogram to show the distribution of a single column."""
        if self.df is None:
            print("Error: No data loaded.")
            return
        fig = px.histogram(self.df, x=column, title=f"Histogram of {column}", template="plotly_white")
        fig.show()

    def plot_box(self, x_column, y_column):
        """Generates a box plot (great for Categorical vs Numerical variables)."""
        if self.df is None:
            print("Error: No data loaded.")
            return
        fig = px.box(self.df, x=x_column, y=y_column, title=f"Box Plot: {y_column} by {x_column}", template="plotly_white")
        fig.show()
