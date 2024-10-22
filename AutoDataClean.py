import pandas as pd

# Configuration
input_file = 'path/to/your/input.csv'  # Replace with your input CSV file path
output_file = 'path/to/your/output.csv'  # Replace with your output CSV file path
missing_value_strategy = 'mean'  # Options: 'mean', 'median', 'mode', 'drop'

def load_data(file_path):
    """Load data from a CSV file."""
    try:
        data = pd.read_csv(file_path)
        print("Data loaded successfully.")
        return data
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None

def remove_duplicates(data):
    """Remove duplicate rows from the DataFrame."""
    original_shape = data.shape
    data = data.drop_duplicates()
    new_shape = data.shape
    print(f"Removed {original_shape[0] - new_shape[0]} duplicate rows.")
    return data

def handle_missing_values(data, strategy='mean'):
    """Handle missing values based on the given strategy."""
    if strategy == 'mean':
        data = data.fillna(data.mean())
    elif strategy == 'median':
        data = data.fillna(data.median())
    elif strategy == 'mode':
        data = data.fillna(data.mode().iloc[0])
    elif strategy == 'drop':
        data = data.dropna()
    else:
        print("Invalid missing value strategy. No changes made.")
    print(f"Missing values handled using {strategy} strategy.")
    return data

def standardize_column_names(data):
    """Standardize column names to lowercase and replace spaces with underscores."""
    data.columns = [col.strip().lower().replace(' ', '_') for col in data.columns]
    print("Column names standardized.")
    return data

def convert_data_types(data):
    """Convert data types if possible (e.g., strings to numbers where applicable)."""
    for col in data.columns:
        try:
            data[col] = pd.to_numeric(data[col], errors='ignore')
        except Exception as e:
            print(f"Could not convert column {col}: {e}")
    print("Data types converted where applicable.")
    return data

def save_data(data, file_path):
    """Save the cleaned DataFrame to a CSV file."""
    data.to_csv(file_path, index=False)
    print(f"Cleaned data saved to {file_path}.")

def clean_data(file_path, output_path, missing_strategy):
    """Main function to clean the data."""
    # Load the data
    data = load_data(file_path)
    if data is None:
        return
    
    # Perform cleaning tasks
    data = remove_duplicates(data)
    data = handle_missing_values(data, strategy=missing_strategy)
    data = standardize_column_names(data)
    data = convert_data_types(data)

    # Save the cleaned data
    save_data(data, output_path)
    print("Data cleaning completed.")

if __name__ == "__main__":
    clean_data(input_file, output_file, missing_value_strategy)
