import pandas as pd
# Create DataFrame in wide format
df = pd.DataFrame({
    "employee_id": ["E01", "E02", "E03", "E04", "E05"],
    "employee_name": ["Amit", "Riya", "Sima", "Raju", "Rohit"],
    "contact_1": [9876543210, 9876543211, 9876543212, 9876543213, 9876543214],
    "contact_2": [9123456780, 9123456781, 9123456782, 9123456783, 9123456784],
    "project_location_1": ["Kolkata", "Delhi", "Mumbai", "Pune", "Chennai"],
    "project_location_2": ["Delhi", "Pune", "Kolkata", "Mumbai", "Bangalore"]
})
print("Wide Format:")
print(df)
# Reshape the DataFrame into long format using melt()
long_df = pd.melt(
    df,
    id_vars=["employee_id", "employee_name"],
    var_name="Attribute",
    value_name="Value"
)
print("\nLong Format:")
print(long_df)