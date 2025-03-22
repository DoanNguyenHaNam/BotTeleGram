import os
from __init__ import *

def find_file(root_dir, target_file):
    for root, dirs, files in os.walk(root_dir):
        if target_file in files:
            return os.path.join(root, target_file)
    return None

image=''
txt=open('list_mod_le.txt','r')
for ID in txt:
    ID=ID.replace(' ','').replace('\n','')
    print(ID)
    root_directory = "Image/"
    file_to_find = f"{ID}.jpg"

    # Tìm file
    file_path = find_file(root_directory, file_to_find)

    if file_path:
        print(f"File found: {file_path}")
        with open('list_mod_le.txt','w') as f:f.write(ID)
        a,name=ten_skin_hieu_ung(int(ID))
        
        image=image+file_to_find+':'+name+'\r\n'
        with open(f'File_Mod_Mod_Le/image.txt','wb') as f:
            f.write(image.encode('utf-8'))
