import argparse
import pandas as pd
import os
from tqdm import tqdm as tqdm
import urllib.request
import numpy as np
import sys
import urllib.error  # Added this for specific error handling

parser = argparse.ArgumentParser(description='r/Fakeddit image downloader')
parser.add_argument('type', type=str, help='train, validate, or test')
args = parser.parse_args()

df = pd.read_csv(args.type, sep="\t")
df = df.replace(np.nan, '', regex=True)
df.fillna('', inplace=True)

pbar = tqdm(total=len(df))

if not os.path.exists("images"):
    os.makedirs("images")

for index, row in df.iterrows():
    # download if the row claims to have an image and a valid URL
    if row["hasImage"] == True and row["image_url"] != "" and row["image_url"] != "nan":
        image_url = row["image_url"]
        save_path = os.path.join("images", f"{row['id']}.jpg")
        
        # Checks if we already have the image
        if not os.path.exists(save_path):
            try:
                urllib.request.urlretrieve(image_url, save_path)
            except urllib.error.HTTPError as e:
                # This catches 404 "Not Found" or 403 "Forbidden" errors
                pass 
            except Exception as e:
                # This catches other issues like internet timeouts
                pass
                
    pbar.update(1)

pbar.close()
print("done")