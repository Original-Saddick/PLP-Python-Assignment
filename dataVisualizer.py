# Task 1: Load and Explore the Dataset

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# Set a professional plotting style for better visualization
sns.set_style("whitegrid")
plt.style.use("seaborn-v0_8-whitegrid")

def load_and_clean_data():
    """
    Loads the Iris dataset, performs an initial exploration, and demonstrates
    a cleaning process by introducing and then handling missing values.
    """
    try:
        # Load the Iris dataset from sklearn as a dictionary
        iris_data = load_iris()

        # Create a pandas DataFrame from the data
        df = pd.DataFrame(data=np.c_[iris_data['data'], iris_data['target']],
                          columns=iris_data['feature_names'] + ['species'])

        # Map the numerical species target to a categorical name for readability
        df['species'] = df['species'].map({0: 'setosa', 1: 'versicolor', 2: 'virginica'})

        print("Dataset loaded successfully.")
        print("-" * 30)

        # Display the first few rows to inspect the data
        print("First 5 rows of the dataset:")
        print(df.head())
        print("-" * 30)

        # Explore the structure and data types
        print("Dataset information:")
        df.info()
        print("-" * 30)

        # Check for missing values
        print("Missing values before cleaning:")
        print(df.isnull().sum())
        print("-" * 30)

        # Note: The Iris dataset is clean by default.
        # We will introduce a few missing values to demonstrate the cleaning process.
        print("Demonstrating missing value handling...")
        # Introduce a few NaN values
        df.loc[10:12, 'sepal length (cm)'] = np.nan
        df.loc[25:27, 'petal width (cm)'] = np.nan
        
        print("Missing values after adding NaN:")
        print(df.isnull().sum())
        print("-" * 30)

        # Clean the dataset by dropping rows with missing values
        df_cleaned = df.dropna()
        
        print("Missing values after cleaning (dropping rows):")
        print(df_cleaned.isnull().sum())
        print("-" * 30)
        
        print("Dataset shape after cleaning:", df_cleaned.shape)
        
        # We'll use the original, uncleaned dataset for the rest of the analysis
        # to ensure all data points are used.
        return df

    except Exception as e:
        print(f"An error occurred during data loading or cleaning: {e}")
        return None

# Task 2: Basic Data Analysis

def perform_basic_analysis(df):
    """
    Computes basic statistics and performs a grouped analysis on the dataset.
    
    Args:
        df (pd.DataFrame): The DataFrame to analyze.
    """
    if df is None:
        return
        
    print("Task 2: Basic Data Analysis")
    print("-" * 30)
    
    # Compute basic statistics of numerical columns
    print("Summary statistics of numerical columns:")
    print(df.describe())
    print("-" * 30)
    
    # Perform grouping on the 'species' categorical column
    print("Mean of numerical columns grouped by 'species':")
    grouped_data = df.groupby('species').mean()
    print(grouped_data)
    
    # Identify patterns and findings
    print("\nInteresting Findings:")
    print("1. Setosa has the smallest sepal and petal measurements on average.")
    print("2. Virginica has the largest sepal and petal measurements on average.")
    print("3. There's a clear separation in mean values for 'petal length (cm)' among the species,")
    print("   suggesting this feature is a strong indicator for classification.")
    print("-" * 30)
    
    return grouped_data

# Task 3: Data Visualization

def visualize_data(df, grouped_data):
    """
    Creates and displays four different types of visualizations.
    
    Args:
        df (pd.DataFrame): The DataFrame for plotting.
        grouped_data (pd.DataFrame): The grouped data for the bar chart.
    """
    if df is None or grouped_data is None:
        return

    print("Task 3: Data Visualization")
    print("-" * 30)

    # 1. Line Chart (Simulating a trend)
    plt.figure(figsize=(10, 6))
    # We will plot the cumulative mean of petal length as an example of a trend
    df['cumulative_mean_petal_length'] = df['petal length (cm)'].expanding().mean()
    plt.plot(df.index, df['cumulative_mean_petal_length'], marker='o', linestyle='-')
    plt.title('Simulated Trend: Cumulative Mean of Petal Length')
    plt.xlabel('Data Point Index')
    plt.ylabel('Cumulative Mean Petal Length (cm)')
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    # 2. Bar Chart
    plt.figure(figsize=(10, 6))
    sns.barplot(x=grouped_data.index, y=grouped_data['petal length (cm)'])
    plt.title('Average Petal Length by Species')
    plt.xlabel('Species')
    plt.ylabel('Average Petal Length (cm)')
    plt.show()

    # 3. Histogram
    plt.figure(figsize=(10, 6))
    sns.histplot(data=df, x='petal width (cm)', bins=20, kde=True)
    plt.title('Distribution of Petal Width')
    plt.xlabel('Petal Width (cm)')
    plt.ylabel('Frequency')
    plt.show()

    # 4. Scatter Plot
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='sepal length (cm)', y='petal length (cm)', hue='species', data=df)
    plt.title('Relationship between Sepal Length and Petal Length')
    plt.xlabel('Sepal Length (cm)')
    plt.ylabel('Petal Length (cm)')
    plt.legend(title='Species')
    plt.show()

if __name__ == "__main__":
    # Load and clean the data
    iris_df = load_and_clean_data()
    
    # If the data was loaded successfully, proceed with analysis and visualization
    if iris_df is not None:
        # Perform basic data analysis
        grouped_df = perform_basic_analysis(iris_df)
        
        # Visualize the data
        visualize_data(iris_df, grouped_df)
