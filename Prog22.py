#  Wap in python to create a dataframe using dictionary for 5 employees with their  id ,name,department, and salary. and perform the following operations on it.
#1. Display the records of first 2 employees.
import pandas as pd

# Create a dictionary
data = {
    'ID': [101, 102, 103, 104, 105],
    'Name': ['Rahul', 'Priya', 'Amit', 'Sneha', 'Rohan'],
    'Department': ['HR', 'IT', 'Finance', 'IT', 'Sales'],
    'Salary': [30000, 45000, 40000, 55000, 35000]
}

# Create DataFrame
df = pd.DataFrame(data)

print("Complete DataFrame:")
print(df)

# 1. Display first two employees
print("\nFirst two employees:")
print(df.head(2))

# 2. Display last two employees
print("\nLast two employees:")
print(df.tail(2))

# 3. Display employee with greatest salary
print("\nEmployee with greatest salary:")
print(df[df['Salary'] == df['Salary'].max()])