import pandas as pd

df = pd.read_csv('orders.csv')

df['order_date'] = pd.to_datetime(df['order_date'])

df['month_year'] = df['order_date'].dt.to_period('M')

monthly_revenue = df.groupby('month_year').apply(lambda x: (x['product_price'] * x['quantity']).sum())

print("Monthly Revenue:")
print(monthly_revenue)

product_revenue = df.groupby('product_name').apply(lambda x: (x['product_price'] * x['quantity']).sum())

print("\nProduct Revenue:")
print(product_revenue)

customer_revenue = df.groupby('customer_id').apply(lambda x: (x['product_price'] * x['quantity']).sum())

print("\nCustomer Revenue:")
print(customer_revenue)


top_10_customers = customer_revenue.nlargest(10)

print("\nTop 10 Customers:")
print(top_10_customers)
