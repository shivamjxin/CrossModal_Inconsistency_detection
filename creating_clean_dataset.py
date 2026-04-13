import pandas as pd
import os

df = pd.read_csv("sample_train.tsv", sep = '\t')
img_path = 'images' 

def check_img(img_id):
    return os.path.exists(os.path.join(img_path,f'{img_id}.jpg'))

df["is_downloaded"] = df['id'].apply(check_img)
df_cleaned = df[df['is_downloaded'] == True].copy()

# droping the helper column
df_cleaned.drop(columns = ['is_downloaded'], inplace = True)
df_cleaned.to_csv("cleaned_sample_train", sep = '\t', index = False)