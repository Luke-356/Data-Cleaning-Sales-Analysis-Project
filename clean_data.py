import pandas as pd

#Load data
df = pd.read_csv("sales.csv")

#clean column names and remove null values
df.columns = df.columns.str.lower().str.replace(" ", "_")
df = df.dropna()

#convert date columns to datetime
df['order_date'] = pd.to_datetime(df['order_date'], dayfirst=True)
df['ship_date'] = pd.to_datetime(df['ship_date'], dayfirst=True)

#remove duplicates
df = df.drop_duplicates()

#remove unnecessary columns
df = df.drop(columns=['row_id'])

#create new columns for year and month of order date
df['order_year'] = df['order_date'].dt.year
df['order_month'] = df['order_date'].dt.month

#save cleaned data to new csv file
df.to_csv("cleaned_sales.csv", index=False)

# Sales by category
print("\nSales by Category:")
print(df.groupby('category')['sales'].sum())

# Profit by region
print("\nProfit by Region:")
print(df.groupby('region')['profit'].sum())

# Monthly sales
print("\nMonthly Sales:")
print(df.groupby('order_month')['sales'].sum())

# Worst performing sub-categories
print("\nProfit by Sub-Category:")
print(df.groupby('sub-category')['profit'].sum().sort_values())

