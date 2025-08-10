import pandas as pd

file_path = 'sales_data.csv'
sales_data = pd.read_csv(file_path)


# 1. Take a look at the first 5 rows of the dataframe and print them.
print("First 5 Rows of the DataFrame:")
print(sales_data.head())


# 2. For each region, calculate the sales and profit.
region_sales_profit = sales_data.groupby('Region')[['Sales', 'Profit']].sum()
print("\nSales and Profit by Region:")
print(region_sales_profit)


# 3. Find the three highest-selling and most profitable products.
top_selling_products = sales_data.groupby('Product')['Sales'].sum().nlargest(3)
top_profitable_products = sales_data.groupby('Product')['Profit'].sum().nlargest(3)
print("\nThree Highest-Selling Products:")
print(top_selling_products)
print("\nThree Most Profitable Products:")
print(top_profitable_products)


# 4. Divide the profit by the sales to create a new column named "Profit Margin".
sales_data['Profit Margin'] = sales_data['Profit'] / sales_data['Sales']


# 5. Save the updated dataframe as "updated_sales_data.csv".
updated_file_path = 'sales_data-2.csv'
sales_data.to_csv(updated_file_path, index=False)
print(f"\nUpdated DataFrame saved to: {updated_file_path}")
