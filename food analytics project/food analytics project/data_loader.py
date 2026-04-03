import pandas as pd



def data_loader(file_name):
    try:
        df = pd.read_csv(file_name)
        return df
    except FileNotFoundError:
        print("Error: File not found")
    except pd.errors.EmptyDataError:
        print("Error: File is empty")
    except Exception as e:
        print("Error:", e)


def data_preview(df):
    print("\n" + "="*50)
    print("📊 DATA PREVIEW")
    print("="*50)

    print(f"\n🔹 Shape: {df.shape[0]} rows × {df.shape[1]} columns")

    print("\n🔹 Columns:")
    print(", ".join(df.columns))

    print("\n🔹 Data Types:")
    print(df.dtypes.to_string())

    print("\n🔹 Missing Values:")
    print(df.isnull().sum().to_string())

    print("\n🔹 First 5 Rows:")
    print(df.head().to_string(index=False))

    print("\n" + "="*50)
    
    
def data_type_corrector(df):
    for col in df.columns:
        if df[col].dtype == 'object':
            converted = pd.to_numeric(df[col], errors='coerce')
            if converted.notnull().sum() > 0:
                df[col] = converted
                continue
            converted = pd.to_datetime(df[col], errors='coerce')
            if converted.notnull().sum() > 0:
                df[col] = converted
    return df

def data_cleaner(df):
    df = df.drop_duplicates()
    for col in df.columns:
        if df[col].dtype == 'object':
            df[col].fillna("Unknown", inplace=True)
        else:
            df[col].fillna(0, inplace=True)

    if 'amount' in df.columns:
        df['amount'] = df['amount'].astype(str).str.strip()
        df['amount'] = df['amount'].replace('', 0)
        df['amount'] = pd.to_numeric(df['amount'], errors='coerce')
        df['amount'] = df['amount'].fillna(0)

    df = data_type_corrector(df)
    print("Data cleaned successfully")
    return df

def process_data(file_name):
    df = data_loader(file_name)
    if df is not None:
        df = data_cleaner(df)
        return df
    return None

# df = process_data("food_sales.csv")
# if df is not None:
#     data_preview(df)
#     df.to_csv("cleaned_dataset.csv", index=False)
#     print("Cleaned dataset saved")