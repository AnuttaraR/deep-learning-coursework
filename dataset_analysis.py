import pandas as pd

# Load the Yelp dataset
file_path = "yelp_academic_dataset_review.json"

# Read only the first 500000 rows as a sample since less memory
df = pd.read_json(file_path, lines=True, nrows=5000)

# Display column names
print("Column Names:")
print(df.columns)

# Check for null values
print("\nNull Values:")
print(df.isnull().sum())

# Check for duplicates
duplicates = df[df.duplicated()]
print("\nDuplicates:")
print(duplicates)
df = df.drop_duplicates()

# Check for missing values
missing_values = df[df.isnull().any(axis=1)]
print("\nMissing Values:")
print(missing_values)
df = df.dropna()

# Create a new column "sentiment" based on the "stars" column
df['sentiment'] = df['stars'].apply(lambda x: 'negative' if x in [1, 2] else ('neutral' if x in [3, 4] else 'positive'))

# Save the feature engineered dataset
#df.to_json("reduced_feature_engineered_dataset.json", orient="records", lines=True)

