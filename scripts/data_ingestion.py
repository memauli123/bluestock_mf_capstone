from pathlib import Path
import pandas as pd

# Get the script directory and navigate to data/raw folder
SCRIPT_DIR = Path(__file__).parent.absolute()
RAW_FOLDER = SCRIPT_DIR.parent / "data" / "raw"
csv_files = list(RAW_FOLDER.glob("*.csv"))
print(f"Found {len(csv_files)} CSV files\n") #prints the number of CSV files in the raw folder

# Loop through each CSV file and print its name, shape, columns, data types, first 5 rows, and missing values   
for file in csv_files:
    print("=" * 70) #prints a separator line for better readability between files
    print(f"FILE: {file.name}")
    try:
        df = pd.read_csv(file)

        print("\nShape:")
        print(df.shape)

        print("\nColumns:")
        print(df.columns.tolist())

        print("\nData Types:")
        print(df.dtypes)

        print("\nFirst 5 Rows:")
        print(df.head())

        print("\nMissing Values:")
        print(df.isnull().sum())

    except Exception as e:
        print(f"Error reading {file.name}: {e}")
    print("\n")