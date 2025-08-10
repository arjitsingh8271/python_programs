import pandas as pd

def total_sales_by_product(dataframe):
    dataframe['Total_Sales'] = dataframe['Quantity'] * dataframe['Price']
    result = dataframe.groupby('Product', as_index=False)['Total_Sales'].sum()
    return result

sales = pd.DataFrame({
    'Product': ['apple', 'orange', 'apple', 'banana', 'apple', 'apple'],
    'Quantity': [2, 3, 5, 2, 4, 3],
    'Price': [5.0, 4.5, 5.5, 6.5, 4.5, 5.0]
})

result = total_sales_by_product(sales)
print(result)
