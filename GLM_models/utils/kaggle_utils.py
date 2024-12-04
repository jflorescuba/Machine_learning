import os
import pandas as pd
from kaggle.api.kaggle_api_extended import KaggleApi
import zipfile

def download_and_load_kaggle_data(dataset_name, file_name, download_path='.'):
    """
    Function to download a dataset from Kaggle, extract it (if it's a zip), 
    and load it into a pandas DataFrame.
    
    Parameters:
    dataset_name (str): The name of the dataset on Kaggle in the format 'username/dataset-name'.
    file_name (str): The name of the file you want to download (e.g., 'file.csv' or 'file.zip').
    download_path (str): The path where the file will be downloaded (default is the current directory).
    
    Returns:
    pd.DataFrame: The loaded pandas DataFrame.
    """
    # Authentication
    api = KaggleApi()
    api.authenticate()
    
    # Download the file from Kaggle
    api.dataset_download_file(dataset_name, file_name, path=download_path)
    
    file_path = os.path.join(download_path, file_name)
    
    # Check if the file is a ZIP
    if file_name.endswith('.zip'):
        # If it's a ZIP file, extract and load the CSV into a DataFrame
        with zipfile.ZipFile(file_path, 'r') as zip_ref:
            zip_ref.extractall(download_path)  # Extract files to the download path
            # Get the extracted file name (assuming there's only one file inside the ZIP)
            extracted_file_name = zip_ref.namelist()[0]
            # Load the extracted CSV file into a DataFrame
            df = pd.read_csv(os.path.join(download_path, extracted_file_name))
    else:
        # If it's a CSV file directly, load it into a DataFrame
        df = pd.read_csv(file_path)
    
    return df
