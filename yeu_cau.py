import os
import shutil
import sys
try:
    name=sys.argv[1]
except:
    name=input('Mod Theo Yêu Cầu: ')
name='Mod_Theo_Yêu_Cầu_@'+name
with open('main.py', 'rb') as f:
    a = f.read()
    a = a.replace(b'File_Mod', b'File_Mod_YeuCau').decode('utf-8')
    a += "\ntry:\n    shutil.make_archive(f'./File_Mod_YeuCau/{folder_mod}', 'zip', f'./File_Mod_YeuCau/{folder_mod}')\n    shutil.rmtree(f'./File_Mod_YeuCau/{folder_mod}')    \nexcept Exception as e:\n    print(f'Lỗi: {e}')\n"
with open(f'yeu_cau_fix.py','wb') as f:
    f.write(a.encode('utf-8'))
os.system(f'py yeu_cau_fix.py {name}')