import pandas as pd

# Create a sample DataFrame
data = {'Name': ['John', 'Mary', 'David'],
        'Age': [25, 31, 42]}
df = pd.DataFrame(data)

# Print the original DataFrame
print("Original DataFrame:")
print(df)

# Use iterrows() to iterate over each row and write to it
for index, row in df.iterrows():
    df.loc[index,'Age'] = 30  # Change the age to 30
    print(f"Updated row {index}: {row}")

# Print the updated DataFrame
print("\nUpdated DataFrame:")
print(df)