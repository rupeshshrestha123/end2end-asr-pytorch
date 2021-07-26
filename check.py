import pandas as pd
train_manifest=pd.read_csv('ne_np_female_train_manifest.csv')
for i in train_manifest[0]:
    print(i)

# fh=open('/content/drive/MyDrive/ne_np_female_dataset/train/txt/nep_0258_0119737288.txt')
# for line in fh:
#   print(line)
