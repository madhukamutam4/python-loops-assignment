import pandas as pd

# Task 1
df = pd.read_csv('orders.csv', index_col='order_id')

print("First 5 rows")
print(df.head())

print("Last 5 rows")
print(df.tail())

# Task 2
print("How many rows and columns does the dataset have?")
print(df.shape)

print("Which columns have missing values and how many nulls does each have?")
print(df.isnull().sum())

print("Data types:")
print(df.dtypes)

# Convert date column
df['order_date'] = pd.to_datetime(df['order_date'])

df['year'] = df['order_date'].dt.year.astype('Int64')
df['month'] = df['order_date'].dt.month.astype('Int64')

# Task 3
print("Statistical Summary")
print(df.describe())