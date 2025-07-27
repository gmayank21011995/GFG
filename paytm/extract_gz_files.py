import gzip
import shutil

gz_path = "data/file.csv.gz"
output_path = "data/file.csv"

with gzip.open(gz_path, 'rb') as f_in:
    with open(output_path, 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)

print("GZ file extracted to:", output_path)
