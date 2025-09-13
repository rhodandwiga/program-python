# =============================================
# Assignment: Data Analysis and Visualization
# Using a CSV dataset (example: sales.csv)
# =============================================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ================================
# Task 1: Load and Explore the Dataset
# ================================
try:
    # Load dataset (replace 'sales.csv' with your dataset filename)
    df = pd.read_csv("sales.csv")

    # Display the first few rows
    print("First 5 rows of the dataset:")
    print(df.head())

    # Explore structure
    print("\nDataset Info:")
    print(df.info())

    print("\nMissing values per column:")
    print(df.isnull().sum())

    # Clean dataset (drop or fill missing values)
    df = df.dropna()   # You can also use df.fillna(value=0)

except FileNotFoundError:
    print("Error: The file 'sales.csv' was not found. Please check the path and filename.")


# ================================
# Task 2: Basic Data Analysis
# ================================
if 'df' in locals():
    # Summary statistics
    print("\nStatistical Summary:")
    print(df.describe())

    # Example grouping: average sales per region (replace 'Region' and 'Sales' with your dataset columns)
    if "Region" in df.columns and "Sales" in df.columns:
        grouped = df.groupby("Region")["Sales"].mean()
        print("\nAverage Sales per Region:")
        print(grouped)

    # ================================
    # Task 3: Data Visualization
    # ================================

    # 1. Line chart (e.g., sales over time if Date column exists)
    if "Date" in df.columns and "Sales" in df.columns:
        df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
        df = df.dropna(subset=["Date"])
        df = df.sort_values("Date")

        plt.figure(figsize=(10,6))
        plt.plot(df["Date"], df["Sales"], marker="o", linestyle="-", color="blue", label="Sales")
        plt.title("Line Chart: Sales Over Time")
        plt.xlabel("Date")
        plt.ylabel("Sales")
        plt.legend()
        plt.show()

    # 2. Bar chart (average sales per region)
    if "Region" in df.columns and "Sales" in df.columns:
        plt.figure(figsize=(8,5))
        sns.barplot(x="Region", y="Sales", data=df, estimator="mean", ci=None, palette="viridis")
        plt.title("Bar Chart: Average Sales per Region")
        plt.xlabel("Region")
        plt.ylabel("Average Sales")
        plt.show()

    # 3. Histogram (distribution of sales)
    if "Sales" in df.columns:
        plt.figure(figsize=(8,5))
        plt.hist(df["Sales"], bins=20, color="orange", edgecolor="black")
        plt.title("Histogram: Sales Distribution")
        plt.xlabel("Sales")
        plt.ylabel("Frequency")
        plt.show()

    # 4. Scatter plot (example: Sales vs Quantity if both exist)
    if "Sales" in df.columns and "Quantity" in df.columns:
        plt.figure(figsize=(8,5))
        sns.scatterplot(x="Quantity", y="Sales", hue="Region", data=df, palette="Set1")
        plt.title("Scatter Plot: Sales vs Quantity")
        plt.xlabel("Quantity")
        plt.ylabel("Sales")
        plt.legend(title="Region")
        plt.show()
