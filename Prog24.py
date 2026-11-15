import pandas as pd
# Import the Titanic dataset from Desktop
df = pd.read_csv(r"C:\Users\NITYA GOYAL\OneDrive\Desktop\Titanic-Dataset.csv")
# 1. Clean the dataset and print the resultant dataset
df = df.dropna()
print("Cleaned Dataset:")
print(df)
# 2. Find details of passengers whose age is more than 30 and category is female
result = df[(df["Age"] > 30) & (df["Sex"] == "female")]
print("\nPassengers whose age is more than 30 and category is female:")
print(result)
# 3. Find details of the passengers of Class 1
result = df[df["Pclass"] == 1]
print("\nPassengers of Class 1:")
print(result)
# 4. Remove the duplicate values of PassengerId
df = df.drop_duplicates(subset=["PassengerId"])
print("\nDataset after removing duplicate PassengerId:")
print(df)
# 5. Insert a column named Status in the dataset
df.insert(1, "Status", "Passenger")
print("\nDataset after inserting Status column:")
print(df)