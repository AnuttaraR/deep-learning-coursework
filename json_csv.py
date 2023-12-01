import pandas as pd
import json

# Specify the paths
json_file_path = 'yelp_academic_dataset_review.json'
csv_output_path = 'yelp_csv_dataset.csv'

# Open the JSON file and read lines
with open(json_file_path, 'r', encoding='utf-8') as json_file:
    # Read the first 10,000 lines from the JSON file
    json_lines = [json_file.readline() for _ in range(10000)]

# Parse each JSON line and store the data in a list
data = [json.loads(line) for line in json_lines]

# Convert the list of dictionaries to a DataFrame
df = pd.DataFrame(data)

# Save the DataFrame to a CSV file
df.to_csv(csv_output_path, index=False)

# Display the first few rows of the resulting CSV file
print(f"Subset of Yelp dataset saved to '{csv_output_path}':")
print(df.head())
