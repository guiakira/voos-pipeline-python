from data_clean import clean_data, url, output_path
from transform import transform_data
import os

def main():
    os.makedirs("./data", exist_ok=True)
    os.makedirs("./logs", exist_ok=True)

    df_clean = clean_data(url, output_path)
    df_transformed = transform_data(df_clean)

if __name__ == "__main__":
    main()