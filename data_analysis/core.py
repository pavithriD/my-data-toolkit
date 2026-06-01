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
        
        file_name = list(uploaded.keys())[0]
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

    def plot_scatter(self, x_column=None, y_column=None):
        """Generates a scatter plot. Automatically picks numeric columns if none are provided."""
        if self.df is None:
            print("Error: No data loaded.")
            return
        
        num_cols = self.df.select_dtypes(include=['int64', 'float64']).columns.tolist()
        
        # If user didn't specify columns, automatically pick the first two numeric ones
        if x_column is None and len(num_cols) > 0:
            x_column = num_cols[0]
        if y_column is None and len(num_cols) > 1:
            y_column = num_cols[1]
            
        if not x_column or not y_column:
            print("Error: Could not automatically find two numeric columns for a scatter plot.")
            return
            
        fig = px.scatter(self.df, x=x_column, y=y_column, title=f"Scatter Plot: {x_column} vs {y_column}", template="plotly_white")
        fig.show()

    def plot_histogram(self, column=None):
        """Generates a histogram. Automatically picks the first numeric column if none is provided."""
        if self.df is None:
            print("Error: No data loaded.")
            return
            
        if column is None:
            num_cols = self.df.select_dtypes(include=['int64', 'float64']).columns.tolist()
            if num_cols:
                column = num_cols[0]
                
        if not column:
            print("Error: No numeric column available for a histogram.")
            return
            
        fig = px.histogram(self.df, x=column, title=f"Histogram of {column}", template="plotly_white")
        fig.show()

    def plot_box(self, x_column=None, y_column=None):
        """Generates a box plot. Automatically finds a categorical and numeric column if none are provided."""
        if self.df is None:
            print("Error: No data loaded.")
            return
            
        cat_cols = self.df.select_dtypes(include=['object', 'category']).columns.tolist()
        num_cols = self.df.select_dtypes(include=['int64', 'float64']).columns.tolist()
        
        if x_column is None:
            # Try to pick a categorical column for X, otherwise fallback to a numeric one
            x_column = cat_cols[0] if cat_cols else (num_cols[0] if num_cols else None)
        if y_column is None and num_cols:
            y_column = num_cols[0]
            
        if not x_column or not y_column:
            print("Error: Not enough data columns to generate a box plot.")
            return
            
        fig = px.box(self.df, x=x_column, y=y_column, title=f"Box Plot: {y_column} by {x_column}", template="plotly_white")
        fig.show()
