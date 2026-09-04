import os 
import requests
import zipfile
from io import BytesIO
from pathlib import Path

DATA_URL = "https://archive.ics.uci.edu/static/public/179/secom.zip"
DATA_PATH = Path('data/raw')
    

def download_data():
    data_file = DATA_PATH / "secom.data"
    labels_file = DATA_PATH / "secom_labels.data"
    
    if data_file.exists() and labels_file.exists():
        return

    Path(DATA_PATH).mkdir(parents=True, exist_ok=True)
    
    print("Downloading UCI SECOM dataset ")
    r = requests.get(DATA_URL)
    r.raise_for_status()
    with zipfile.ZipFile(BytesIO(r.content)) as zip_file:
        zip_file.extractall(path=DATA_PATH)
    


if __name__ == "__main__":
    download_data()