import pandas as pd

def clean_data(file_path, output_path):
    df=pd.read_csv(file_path)
    df.drop_duplicates(inplace=True)
    df.fillna(df.mean(numeric_only=True), inplace=True)
    df.columns = df.columns.str.lower().str.replace(' ','_')
    df.to_csv(output_path, index=False)
    print(f"Cleaned data saved to: {output_path}")
clean_data('input_data.csv', 'cleaned_data.csv')

