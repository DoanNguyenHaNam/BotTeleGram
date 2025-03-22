import os
try:import pyzstd;from colorama import Fore;from colorama import Fore;from colorama import Style;from colorama import Style;from termcolor import colored
except:
    try:os.system('python -m pip install pyzstd');os.system('python -m pip install termcolor');os.system('python -m pip install colorama');import pyzstd;from colorama import Fore;from colorama import Fore;from colorama import Style;from colorama import Style
    except:os.system('pip install pyzstd');os.system('pip install termcolor');os.system('pip install colorama');import pyzstd;from colorama import Fore;from colorama import Fore;from colorama import Style;from colorama import Style
from shutil import make_archive;from pyzstd import decompress,compress,ZstdDict;from os import listdir;import sys;import os;from termcolor import colored;import re;import getopt;import pyzstd;import sys;import glob;import colorama;from colorama import Fore;from colorama import Style;from colorama import Fore;from colorama import Style;import shutil;import zipfile;import shutil;from zipfile import* 
def giai_nen(z,a): 
    import zipfile 
    fantasy_zip = zipfile.ZipFile(z+a)
    fantasy_zip.extractall(z)
    return '\033[1;32mGiai Nen Xong File: ' +a
import sys
try:
    folder=sys.argv[1]
except:
    folder=input('Nhập Tên Folder: ')
if os.path.isdir('./GinTV/') == 0 :
    os.mkdir('./GinTV/')
try:
    folder_mod=sys.argv[2]
except:
    folder_mod=input('Nhập Tên Folder Bạn Muốn Để Vào: ')
if os.path.isdir(f'./GinTV/{folder_mod}/') == 0 :
    os.mkdir(f'./GinTV/{folder_mod}/')
    os.mkdir(f'./GinTV/{folder_mod}/Máy Mạnh/')
    os.mkdir(f'./GinTV/{folder_mod}/Máy Mạnh/Android')
    os.mkdir(f'./GinTV/{folder_mod}/Máy Mạnh/Android/files')
    os.mkdir(f'./GinTV/{folder_mod}/Máy Mạnh/IOS')
    os.mkdir(f'./GinTV/{folder_mod}/Máy Trung/')
    os.mkdir(f'./GinTV/{folder_mod}/Máy Trung/Android')
    os.mkdir(f'./GinTV/{folder_mod}/Máy Trung/Android/files')
    os.mkdir(f'./GinTV/{folder_mod}/Máy Trung/IOS')
    os.mkdir(f'./GinTV/{folder_mod}/Máy Yếu/')
    os.mkdir(f'./GinTV/{folder_mod}/Máy Yếu/Android')
    os.mkdir(f'./GinTV/{folder_mod}/Máy Yếu/Android/files')
    os.mkdir(f'./GinTV/{folder_mod}/Máy Yếu/IOS')
shutil.copytree(f'File_Mod/{folder}/com.garena.game.kgvn/files/Resources',f'./GinTV/{folder_mod}/Máy Mạnh/Android/files/Resources')
shutil.copytree(f'File_Mod/{folder}/com.garena.game.kgvn/files/Resources',f'./GinTV/{folder_mod}/Máy Trung/Android/files/Resources')
shutil.copytree(f'File_Mod/{folder}/com.garena.game.kgvn/files/Resources',f'./GinTV/{folder_mod}/Máy Yếu/Android/files/Resources')
#Máy Mạnh
shutil.make_archive(f'./GinTV/{folder_mod}/Máy Mạnh/IOS/Resources','zip',f'./GinTV/{folder_mod}/Máy Mạnh/Android/files')
#Máy Trung
giai_nen(f'./GinTV/{folder_mod}/Máy Trung/Android/files/Resources/1.57.1/Ages/Prefab_Characters/Prefab_Hero/','CommonActions.pkg.bytes')
with open(f'pmin_sources/Resources/1.57.1/Ages/Prefab_Characters/Prefab_Hero/commonresource/born.xml','rb') as f:
    a=f.read()
with open(f'GinTV/{folder_mod}/Máy Trung/Android/files/Resources/1.57.1/Ages/Prefab_Characters/Prefab_Hero/commonresource/born.xml','wb') as f:
    f.write(a)
back_folder = ['commonresource','KeySpell','PassiveResource','mowen','Ultrafire']
def zipdir2(path, ziph):
        for ii in back_folder:
            nonee = './{}'.format(ii)
            DIR2 = './GinTV/{}/Máy Trung/Android/files/Resources/1.57.1/Ages/Prefab_Characters/Prefab_Hero/{}'.format(folder_mod,ii)
            DIR = './GinTV/{}/Máy Trung/Android/files/Resources/1.57.1/Ages/Prefab_Characters/Prefab_Hero/{}'.format(folder_mod,ii)
            for root, dirs, files in os.walk(DIR):
                for file in listdir(DIR2):
                    ziph.write(os.path.join(root, file),
                            os.path.relpath(os.path.join(nonee,file),
                                            os.path.join(path, '..')))
with zipfile.ZipFile('./GinTV/{}/Máy Trung/Android/files/Resources/1.57.1/Ages/Prefab_Characters/Prefab_Hero/CommonActions.pkg.bytes'.format(folder_mod), 'w', zipfile.ZIP_STORED) as zipf:
        zipdir2('tmp/', zipf)
for iii in back_folder:
        if os.path.isdir('./GinTV/{}/Máy Trung/Android/files/Resources/1.57.1/Ages/Prefab_Characters/Prefab_Hero/{}'.format(folder_mod,iii))== 1 :
            shutil.rmtree('./GinTV/{}/Máy Trung/Android/files/Resources/1.57.1/Ages/Prefab_Characters/Prefab_Hero/{}'.format(folder_mod,iii))
shutil.make_archive(f'./GinTV/{folder_mod}/Máy Trung/IOS/Resources','zip',f'./GinTV/{folder_mod}/Máy Trung/Android/files')
#Máy Yếu
giai_nen(f'./GinTV/{folder_mod}/Máy Yếu/Android/files/Resources/1.57.1/Ages/Prefab_Characters/Prefab_Hero/','CommonActions.pkg.bytes')
for file in ['Born.xml','Back.xml','HasteE1.xml','HasteE1_leave.xml']:
    with open(f'pmin_sources/Resources/1.57.1/Ages/Prefab_Characters/Prefab_Hero/commonresource/{file}','rb') as f:
        a=f.read()
    with open(f'GinTV/{folder_mod}/Máy Yếu/Android/files/Resources/1.57.1/Ages/Prefab_Characters/Prefab_Hero/commonresource/{file}','wb') as f:
        f.write(a)
back_folder = ['commonresource','KeySpell','PassiveResource','mowen','Ultrafire']
def zipdir2(path, ziph):
        for ii in back_folder:
            nonee = './{}'.format(ii)
            DIR2 = './GinTV/{}/Máy Yếu/Android/files/Resources/1.57.1/Ages/Prefab_Characters/Prefab_Hero/{}'.format(folder_mod,ii)
            DIR = './GinTV/{}/Máy Yếu/Android/files/Resources/1.57.1/Ages/Prefab_Characters/Prefab_Hero/{}'.format(folder_mod,ii)
            for root, dirs, files in os.walk(DIR):
                for file in listdir(DIR2):
                    ziph.write(os.path.join(root, file),
                            os.path.relpath(os.path.join(nonee,file),
                                            os.path.join(path, '..')))
with zipfile.ZipFile('./GinTV/{}/Máy Yếu/Android/files/Resources/1.57.1/Ages/Prefab_Characters/Prefab_Hero/CommonActions.pkg.bytes'.format(folder_mod), 'w', zipfile.ZIP_STORED) as zipf:
        zipdir2('tmp/', zipf)
for iii in back_folder:
        if os.path.isdir('./GinTV/{}/Máy Yếu/Android/files/Resources/1.57.1/Ages/Prefab_Characters/Prefab_Hero/{}'.format(folder_mod,iii))== 1 :
            shutil.rmtree('./GinTV/{}/Máy Yếu/Android/files/Resources/1.57.1/Ages/Prefab_Characters/Prefab_Hero/{}'.format(folder_mod,iii))
shutil.make_archive(f'./GinTV/{folder_mod}/Máy Yếu/IOS/Resources','zip',f'./GinTV/{folder_mod}/Máy Yếu/Android/files')
