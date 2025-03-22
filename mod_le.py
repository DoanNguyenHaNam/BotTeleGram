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
        with open('list_mod_le_2.txt','w') as f:f.write(ID)
        a,name=ten_skin_hieu_ung(int(ID))
        with open('main.py','rb') as f:
            a=f.read().replace(
                b'folder_mod=input(\'\\t\\tNh\xe1\xba\xadp Folder \xc4\x90\xe1\xbb\x83 V\xc3\xa0o: \')\r\n',b'folder_mod=input(\'\\t\\tNh\xe1\xba\xadp Folder \xc4\x90\xe1\xbb\x83 V\xc3\xa0o: \')\r\n    folder_mod=folder_mod.replace(\'_\',\' \')\r\n'
            )
            a=a.decode()
            a=a.replace(
                'File_Mod', 'File_Mod_Mod_Le'
            )
            a=a.encode('utf-8').replace(
                b'list_mod.txt',b'list_mod_le_2.txt'
            )
            a+=b'''\r\nshutil.make_archive(f'File_Mod_Mod_Le/{folder_mod}', 'zip', f'File_Mod_Mod_Le/{folder_mod}')
if os.path.exists(f'File_Mod_Mod_Le/{folder_mod}'):
    shutil.rmtree(f'File_Mod_Mod_Le/{folder_mod}')
'''
        with open('main_mod_le.py','wb') as f:
            f.write(a)
        print('py main_mod_le.py '+name.replace(' ','_')+' t t s')
        os.system('py main_mod_le.py '+name.replace(' ','_')+' t t s')

        
        image=image+file_to_find+':'+name+'\r\n'
        with open(f'File_Mod_Mod_Le/image.txt','wb') as f:
            f.write(image.encode('utf-8'))
