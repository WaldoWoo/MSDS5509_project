import os
import zipfile
import shutil
from config import RAW_DATA_PATH

def download_and_prepare_data():
  """
    Downloads the dataset from Kaggle, unzips it, and moves it to the RAW_DATA_PATH.
    """
# Download dataset from Kaggle
print("Downloading dataset from Kaggle...")
os.system("kaggle datasets download -d tayloredwards0/single-residence-energy-usage --force")

# Create the raw data directory if it doesn't exist
os.makedirs(RAW_DATA_PATH, exist_ok=True)

# Unzip the dataset
print("Unzipping dataset...")
with zipfile.ZipFile("single-residence-energy-usage.zip", 'r') as zip_ref:
  zip_ref.extractall(".")  # Extract to current working directory

# Move extracted files to the RAW_DATA_PATH
print(f"Moving files to {RAW_DATA_PATH}...")
for file_name in ["measured_weather_data.csv", "usage_data.csv"]:
  if os.path.exists(file_name):
  shutil.move(file_name, os.path.join(RAW_DATA_PATH, file_name))
else:
  print(f"File {file_name} not found in the extracted content.")

# Clean up the downloaded zip file
os.remove("single-residence-energy-usage.zip")
print("Dataset preparation complete.")

if __name__ == "__main__":
  download_and_prepare_data()

# Verify the files in the RAW_DATA_PATH
print(f"Files in '{RAW_DATA_PATH}':", os.listdir(RAW_DATA_PATH))
