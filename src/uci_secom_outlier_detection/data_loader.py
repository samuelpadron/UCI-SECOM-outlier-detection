import os 
import requests
import zipfile
import pandas as pd 
from io import BytesIO
from pathlib import Path


DATA_URL = "https://archive.ics.uci.edu/static/public/179/secom.zip"
PROJECT_ROOT = Path(__file__).resolve().parents[2]
DATA_PATH = PROJECT_ROOT / "data" / "raw"
DATA_FILE = DATA_PATH / "secom.data"
LABELS_FILE = DATA_PATH / "secom_labels.data"
    

def download_data():
    if DATA_FILE.exists() and LABELS_FILE.exists():
        return

    Path(DATA_PATH).mkdir(parents=True, exist_ok=True)
    
    print("Downloading UCI SECOM dataset ")
    r = requests.get(DATA_URL)
    r.raise_for_status()
    with zipfile.ZipFile(BytesIO(r.content)) as zip_file:
        zip_file.extractall(path=DATA_PATH)
        
def load_dataset():
    download_data()
    data_df = pd.read_csv(DATA_FILE, sep=r'\s+', header=None)
    labels_df = pd.read_csv(LABELS_FILE, sep=r'\s+', header=None)
    return data_df, labels_df
    


if __name__ == "__main__":
    download_data()