# Step 1: Import Libraries
import pandas as pd

# Step 2: Load Dataset
df = pd.read_csv("messy_company_dataset.csv")   # Replace with actual file path

# Step 3: Inspect Dataset
print("Dataset Info:")
print(df.info())
print("\nSummary Statistics:")
print(df.describe(include='all'))
print("\nMissing Values:")
print(df.isnull().sum())
print("\nDuplicate Records:", df.duplicated().sum())

# Step 4: Handle Missing Values
# Example: Fill numerical columns with mean, categorical with mode
df['Salary'] = df['Salary'].fillna(df['Salary'].mean())
df['Department'] = df['Department'].fillna(df['Department'].mode()[0])

# Forward fill for sequential data (e.g., joining date)
df['JoiningDate'] = df['JoiningDate'].fillna(method='ffill')

# Drop rows if too many missing values
df = df.dropna(thresh=3)   # keep rows with at least 3 non-null values

# Step 5: Correct Data Types
df['JoiningDate'] = pd.to_datetime(df['JoiningDate'], errors='coerce')
df['EmployeeID'] = df['EmployeeID'].astype(str)

# Step 6: Handle Inconsistent Entries
df['Department'] = df['Department'].str.strip().str.title()   # normalize text
df['Gender'] = df['Gender'].replace({'M':'Male','F':'Female','male':'Male','female':'Female'})

# Step 7: Remove Duplicates
df = df.drop_duplicates()

# Step 8: Verify Cleaned Dataset
print("\nCleaned Dataset Info:")
print(df.info())
print("\nMissing Values After Cleaning:")
print(df.isnull().sum())
print("\nDuplicate Records After Cleaning:", df.duplicated().sum())

# Step 9: Export Cleaned Dataset
df.to_csv("cleaned_company_dataset.csv", index=False)
print("\n✅ Cleaned dataset exported successfully!")
