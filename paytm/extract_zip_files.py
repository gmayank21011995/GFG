import zipfile
import os

zip_path = "data/archive.zip"
extract_to = "data/unzipped/"

with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    zip_ref.extractall(extract_to)

print("ZIP extracted to:", extract_to)
