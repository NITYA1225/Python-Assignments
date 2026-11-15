import pandas as pd
# Create the student DataFrame
student = {
    "roll": ["01", "02", "03", "04", "05"],
    "name": ["Amit", "Riya", "Sima", "Raju", "Rohit"],
    "dept": ["CSE", "IT", None, "ECE", None],
    "marks": [90, None, 80, 85, 95]
}
df = pd.DataFrame(student)
print("Original DataFrame:")
print(df)
# 1. Find out the columns with null values
print("\nColumns with null values:")
print(df.isnull().sum())
# 2. Fill the null value of Sima with CSE
df.loc[df["name"] == "Sima", "dept"] = "CSE"
# 3. Delete the null value of Rohit
df = df.dropna(subset=["dept"])
# 4. Update the dept of Raju with VLSI
df.loc[df["name"] == "Raju", "dept"] = "VLSI"
print("\nFinal DataFrame:")
print(df)
