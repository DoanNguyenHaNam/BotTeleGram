import os
try:import pyzstd;from colorama import Fore;from colorama import Fore;from colorama import Style;from colorama import Style;from termcolor import colored
except:
    try:os.system('python -m pip install pyzstd');os.system('python -m pip install termcolor');os.system('python -m pip install colorama');import pyzstd;from colorama import Fore;from colorama import Fore;from colorama import Style;from colorama import Style
    except:os.system('pip install pyzstd');os.system('pip install termcolor');os.system('pip install colorama');import pyzstd;from colorama import Fore;from colorama import Fore;from colorama import Style;from colorama import Style
from shutil import make_archive;from pyzstd import decompress,compress,ZstdDict;from os import listdir;import sys;import os;from termcolor import colored;import re;import getopt;import pyzstd;import sys;import glob;import colorama;from colorama import Fore;from colorama import Style;from colorama import Fore;from colorama import Style;import shutil;import zipfile;import shutil;from zipfile import* 
from __init__ import *
def giai_nen(z,a): 
    import zipfile 
    fantasy_zip = zipfile.ZipFile(z+a)
    fantasy_zip.extractall(z)
    return '\033[1;32mGiai Nen Xong File: ' +a
import sys
from __init__ import*
try:
    folder=sys.argv[1]
except:
    folder=input('Nhập Tên Folder: ')
if os.path.isdir('./PMINMOD/') == 0 :
    os.mkdir('./PMINMOD/')
try:
    folder_mod=sys.argv[2]
except:
    folder_mod=input('Nhập Tên Folder Bạn Muốn Để Vào: ')
folder_mod='PACK '+folder_mod+' PMINMOD'
if os.path.isdir(f'./PMINMOD/{folder_mod}/') == 0 :
    os.mkdir(f'./PMINMOD/{folder_mod}/')
    os.mkdir(f'./PMINMOD/{folder_mod}/Máy Mạnh/')
    os.mkdir(f'./PMINMOD/{folder_mod}/Máy Mạnh/Android')
    os.mkdir(f'./PMINMOD/{folder_mod}/Máy Mạnh/IOS')
    os.mkdir(f'./PMINMOD/{folder_mod}/Máy Trung/')
    os.mkdir(f'./PMINMOD/{folder_mod}/Máy Trung/Android')
    os.mkdir(f'./PMINMOD/{folder_mod}/Máy Trung/IOS')
    os.mkdir(f'./PMINMOD/{folder_mod}/Máy Yếu/')
    os.mkdir(f'./PMINMOD/{folder_mod}/Máy Yếu/Android')
    os.mkdir(f'./PMINMOD/{folder_mod}/Máy Yếu/IOS')
shutil.copytree(f'File_Mod/{folder}/com.garena.game.kgvn/files/Resources',f'./PMINMOD/{folder_mod}/Máy Mạnh/Android/Resources')
shutil.copytree(f'File_Mod/{folder}/com.garena.game.kgvn/files/Resources',f'./PMINMOD/{folder_mod}/Máy Trung/Android/Resources')
shutil.copytree(f'File_Mod/{folder}/com.garena.game.kgvn/files/Resources',f'./PMINMOD/{folder_mod}/Máy Yếu/Android/Resources')
#Máy Mạnh
shutil.make_archive(f'./PMINMOD/{folder_mod}/Máy Mạnh/IOS/Resources','zip',f'./PMINMOD/{folder_mod}/Máy Mạnh/Android')
#Máy Trung
giai_nen(f'./PMINMOD/{folder_mod}/Máy Trung/Android/Resources/1.57.1/Ages/Prefab_Characters/Prefab_Hero/','CommonActions.pkg.bytes')
with open(f'pmin_sources/Resources/1.57.1/Ages/Prefab_Characters/Prefab_Hero/commonresource/born.xml','rb') as f:
    a=f.read()
with open(f'PMINMOD/{folder_mod}/Máy Trung/Android/Resources/1.57.1/Ages/Prefab_Characters/Prefab_Hero/commonresource/born.xml','wb') as f:
    f.write(a)
for file in ['Back.xml','HasteE1.xml','HasteE1_leave.xml']:
    with open(f'PMINMOD/{folder_mod}/Máy Trung/Android/Resources/1.57.1/Ages/Prefab_Characters/Prefab_Hero/commonresource/{file}','rb') as f:
        a=f.read()
        check=a.find(b'Mod_by_YOUTUBE')
        if check!=-1:
            a1=a_goc=a[check:]
            p=a1.find(b'prefab_skill_effects')
            while p!=-1:
                p1=a1.find(b'"',p)
                a1=a1.replace(a1[p:p1],a1[p:p1]+b'_low')
                p=a1.find(b'prefab_skill_effects',p1)
            a=a.replace(a_goc,a1)
    with open(f'PMINMOD/{folder_mod}/Máy Trung/Android/Resources/1.57.1/Ages/Prefab_Characters/Prefab_Hero/commonresource/{file}','wb') as f:
        f.write(compress_(a)+ngaunhien())
back_folder = ['commonresource','KeySpell','PassiveResource','mowen','Ultrafire']
def zipdir2(path, ziph):
        for ii in back_folder:
            nonee = './{}'.format(ii)
            DIR2 = './PMINMOD/{}/Máy Trung/Android/Resources/1.57.1/Ages/Prefab_Characters/Prefab_Hero/{}'.format(folder_mod,ii)
            DIR = './PMINMOD/{}/Máy Trung/Android/Resources/1.57.1/Ages/Prefab_Characters/Prefab_Hero/{}'.format(folder_mod,ii)
            for root, dirs, files in os.walk(DIR):
                for file in listdir(DIR2):
                    ziph.write(os.path.join(root, file),
                            os.path.relpath(os.path.join(nonee,file),
                                            os.path.join(path, '..')))
with zipfile.ZipFile('./PMINMOD/{}/Máy Trung/Android/Resources/1.57.1/Ages/Prefab_Characters/Prefab_Hero/CommonActions.pkg.bytes'.format(folder_mod), 'w', zipfile.ZIP_STORED) as zipf:
        zipdir2('tmp/', zipf)
for iii in back_folder:
        if os.path.isdir('./PMINMOD/{}/Máy Trung/Android/Resources/1.57.1/Ages/Prefab_Characters/Prefab_Hero/{}'.format(folder_mod,iii))== 1 :
            shutil.rmtree('./PMINMOD/{}/Máy Trung/Android/Resources/1.57.1/Ages/Prefab_Characters/Prefab_Hero/{}'.format(folder_mod,iii))
shutil.make_archive(f'./PMINMOD/{folder_mod}/Máy Trung/IOS/Resources','zip',f'./PMINMOD/{folder_mod}/Máy Trung/Android')
#Máy Yếu
giai_nen(f'./PMINMOD/{folder_mod}/Máy Yếu/Android/Resources/1.57.1/Ages/Prefab_Characters/Prefab_Hero/','CommonActions.pkg.bytes')
for file in ['Born.xml','Back.xml','HasteE1.xml','HasteE1_leave.xml']:
    with open(f'pmin_sources/Resources/1.57.1/Ages/Prefab_Characters/Prefab_Hero/commonresource/{file}','rb') as f:
        a=f.read()
    with open(f'PMINMOD/{folder_mod}/Máy Yếu/Android/Resources/1.57.1/Ages/Prefab_Characters/Prefab_Hero/commonresource/{file}','wb') as f:
        f.write(a)
back_folder = ['commonresource','KeySpell','PassiveResource','mowen','Ultrafire']
def zipdir2(path, ziph):
        for ii in back_folder:
            nonee = './{}'.format(ii)
            DIR2 = './PMINMOD/{}/Máy Yếu/Android/Resources/1.57.1/Ages/Prefab_Characters/Prefab_Hero/{}'.format(folder_mod,ii)
            DIR = './PMINMOD/{}/Máy Yếu/Android/Resources/1.57.1/Ages/Prefab_Characters/Prefab_Hero/{}'.format(folder_mod,ii)
            for root, dirs, files in os.walk(DIR):
                for file in listdir(DIR2):
                    ziph.write(os.path.join(root, file),
                            os.path.relpath(os.path.join(nonee,file),
                                            os.path.join(path, '..')))
with zipfile.ZipFile('./PMINMOD/{}/Máy Yếu/Android/Resources/1.57.1/Ages/Prefab_Characters/Prefab_Hero/CommonActions.pkg.bytes'.format(folder_mod), 'w', zipfile.ZIP_STORED) as zipf:
        zipdir2('tmp/', zipf)
for iii in back_folder:
        if os.path.isdir('./PMINMOD/{}/Máy Yếu/Android/Resources/1.57.1/Ages/Prefab_Characters/Prefab_Hero/{}'.format(folder_mod,iii))== 1 :
            shutil.rmtree('./PMINMOD/{}/Máy Yếu/Android/Resources/1.57.1/Ages/Prefab_Characters/Prefab_Hero/{}'.format(folder_mod,iii))
shutil.make_archive(f'./PMINMOD/{folder_mod}/Máy Yếu/IOS/Resources','zip',f'./PMINMOD/{folder_mod}/Máy Yếu/Android')
checkCamXa='NamNgu'
for camxa in listdir(f'File_Mod/{folder}/'):
    if 'CAM XA' in camxa:
        checkCamXa=camxa
        break
if checkCamXa!='NamNgu':
    codeCamXa=b'    <Track trackName="HitTriggerTick0" eventType="HitTriggerTick" guid="CAM_XA_PMIN_MOD" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Event eventName="HitTriggerTick" time="0.000" isDuration="false" guid="REUP_CC">\r\n        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <TemplateObject name="hitTargetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <int name="SelfSkillCombineID_1" value="530510" refParamName="" useRefParam="false" />\r\n        <TemplateObject name="triggerId" id="-1" objectName="None" isTemp="false" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>\r\n  </Action>'
    if os.path.isdir(f'./PMINMOD/{folder_mod}/{checkCamXa}') == 0 :
        os.mkdir(f'./PMINMOD/{folder_mod}/{checkCamXa}/')
        os.mkdir(f'./PMINMOD/{folder_mod}/{checkCamXa}/Máy Mạnh/')
        os.mkdir(f'./PMINMOD/{folder_mod}/{checkCamXa}/Máy Mạnh/Android')
        os.mkdir(f'./PMINMOD/{folder_mod}/{checkCamXa}/Máy Mạnh/IOS')
        os.mkdir(f'./PMINMOD/{folder_mod}/{checkCamXa}/Máy Trung/')
        os.mkdir(f'./PMINMOD/{folder_mod}/{checkCamXa}/Máy Trung/Android')
        os.mkdir(f'./PMINMOD/{folder_mod}/{checkCamXa}/Máy Trung/IOS')
        os.mkdir(f'./PMINMOD/{folder_mod}/{checkCamXa}/Máy Yếu/')
        os.mkdir(f'./PMINMOD/{folder_mod}/{checkCamXa}/Máy Yếu/Android')
        os.mkdir(f'./PMINMOD/{folder_mod}/{checkCamXa}/Máy Yếu/IOS')
    shutil.copytree(f'File_Mod/{folder}/{checkCamXa}/com.garena.game.kgvn/files/Resources',f'./PMINMOD/{folder_mod}/{checkCamXa}/Máy Mạnh/Android/Resources')
    shutil.copytree(f'File_Mod/{folder}/{checkCamXa}/com.garena.game.kgvn/files/Resources',f'./PMINMOD/{folder_mod}/{checkCamXa}/Máy Trung/Android/Resources')
    shutil.copytree(f'File_Mod/{folder}/{checkCamXa}/com.garena.game.kgvn/files/Resources',f'./PMINMOD/{folder_mod}/{checkCamXa}/Máy Yếu/Android/Resources')
    #Máy Mạnh
    shutil.make_archive(f'./PMINMOD/{folder_mod}/{checkCamXa}/Máy Mạnh/IOS/Resources','zip',f'./PMINMOD/{folder_mod}/{checkCamXa}/Máy Mạnh/Android')
    #Máy Trung
    giai_nen(f'./PMINMOD/{folder_mod}/{checkCamXa}/Máy Trung/Android/Resources/1.57.1/Ages/Prefab_Characters/Prefab_Hero/','CommonActions.pkg.bytes')
    with open(f'pmin_sources/Resources/1.57.1/Ages/Prefab_Characters/Prefab_Hero/commonresource/born.xml','rb') as f:
        a=f.read()
        a=decompress_(a)
        a=a.replace(b'  </Action>',codeCamXa)
    with open(f'PMINMOD/{folder_mod}/{checkCamXa}/Máy Trung/Android/Resources/1.57.1/Ages/Prefab_Characters/Prefab_Hero/commonresource/born.xml','wb') as f:
        f.write(compress_(a)+ngaunhien())
    for file in ['Back.xml','HasteE1.xml','HasteE1_leave.xml']:
        with open(f'PMINMOD/{folder_mod}/{checkCamXa}/Máy Trung/Android/Resources/1.57.1/Ages/Prefab_Characters/Prefab_Hero/commonresource/{file}','rb') as f:
            a=f.read()
            check=a.find(b'Mod_by_YOUTUBE')
            if check!=-1:
                a1=a_goc=a[check:]
                p=a1.find(b'prefab_skill_effects')
                while p!=-1:
                    p1=a1.find(b'"',p)
                    a1=a1.replace(a1[p:p1],a1[p:p1]+b'_low')
                    p=a1.find(b'prefab_skill_effects',p1)
                a=a.replace(a_goc,a1)
        with open(f'PMINMOD/{folder_mod}/{checkCamXa}/Máy Trung/Android/Resources/1.57.1/Ages/Prefab_Characters/Prefab_Hero/commonresource/{file}','wb') as f:
            f.write(compress_(a)+ngaunhien())
    back_folder = ['commonresource','KeySpell','PassiveResource','mowen','Ultrafire']
    def zipdir2(path, ziph):
            for ii in back_folder:
                nonee = './{}'.format(ii)
                DIR2 = './PMINMOD/{}/{}/Máy Trung/Android/Resources/1.57.1/Ages/Prefab_Characters/Prefab_Hero/{}'.format(folder_mod,checkCamXa,ii)
                DIR = './PMINMOD/{}/{}/Máy Trung/Android/Resources/1.57.1/Ages/Prefab_Characters/Prefab_Hero/{}'.format(folder_mod,checkCamXa,ii)
                for root, dirs, files in os.walk(DIR):
                    for file in listdir(DIR2):
                        ziph.write(os.path.join(root, file),
                                os.path.relpath(os.path.join(nonee,file),
                                                os.path.join(path, '..')))
    with zipfile.ZipFile('./PMINMOD/{}/{}/Máy Trung/Android/Resources/1.57.1/Ages/Prefab_Characters/Prefab_Hero/CommonActions.pkg.bytes'.format(folder_mod,checkCamXa), 'w', zipfile.ZIP_STORED) as zipf:
            zipdir2('tmp/', zipf)
    for iii in back_folder:
            if os.path.isdir('./PMINMOD/{}/{}/Máy Trung/Android/Resources/1.57.1/Ages/Prefab_Characters/Prefab_Hero/{}'.format(folder_mod,checkCamXa,iii))== 1 :
                shutil.rmtree('./PMINMOD/{}/{}/Máy Trung/Android/Resources/1.57.1/Ages/Prefab_Characters/Prefab_Hero/{}'.format(folder_mod,checkCamXa,iii))
    shutil.make_archive(f'./PMINMOD/{folder_mod}/{checkCamXa}/Máy Trung/IOS/Resources','zip',f'./PMINMOD/{folder_mod}/{checkCamXa}/Máy Trung/Android')
    #Máy Yếu
    giai_nen(f'./PMINMOD/{folder_mod}/{checkCamXa}/Máy Yếu/Android/Resources/1.57.1/Ages/Prefab_Characters/Prefab_Hero/','CommonActions.pkg.bytes')
    for file in ['Born.xml','Back.xml','HasteE1.xml','HasteE1_leave.xml']:
        with open(f'pmin_sources/Resources/1.57.1/Ages/Prefab_Characters/Prefab_Hero/commonresource/{file}','rb') as f:
            a=f.read()
            a=decompress_(a)
            a=a.replace(b'  </Action>',codeCamXa)
        with open(f'PMINMOD/{folder_mod}/{checkCamXa}/Máy Yếu/Android/Resources/1.57.1/Ages/Prefab_Characters/Prefab_Hero/commonresource/{file}','wb') as f:
            f.write(compress_(a)+ngaunhien())
    back_folder = ['commonresource','KeySpell','PassiveResource','mowen','Ultrafire']
    def zipdir2(path, ziph):
            for ii in back_folder:
                nonee = './{}'.format(ii)
                DIR2 = './PMINMOD/{}/{}/Máy Yếu/Android/Resources/1.57.1/Ages/Prefab_Characters/Prefab_Hero/{}'.format(folder_mod,checkCamXa,ii)
                DIR = './PMINMOD/{}/{}/Máy Yếu/Android/Resources/1.57.1/Ages/Prefab_Characters/Prefab_Hero/{}'.format(folder_mod,checkCamXa,ii)
                for root, dirs, files in os.walk(DIR):
                    for file in listdir(DIR2):
                        ziph.write(os.path.join(root, file),
                                os.path.relpath(os.path.join(nonee,file),
                                                os.path.join(path, '..')))
    with zipfile.ZipFile('./PMINMOD/{}/{}/Máy Yếu/Android/Resources/1.57.1/Ages/Prefab_Characters/Prefab_Hero/CommonActions.pkg.bytes'.format(folder_mod,checkCamXa), 'w', zipfile.ZIP_STORED) as zipf:
            zipdir2('tmp/', zipf)
    for iii in back_folder:
            if os.path.isdir('./PMINMOD/{}/{}/Máy Yếu/Android/Resources/1.57.1/Ages/Prefab_Characters/Prefab_Hero/{}'.format(folder_mod,checkCamXa,iii))== 1 :
                shutil.rmtree('./PMINMOD/{}/{}/Máy Yếu/Android/Resources/1.57.1/Ages/Prefab_Characters/Prefab_Hero/{}'.format(folder_mod,checkCamXa,iii))
    shutil.make_archive(f'./PMINMOD/{folder_mod}/{checkCamXa}/Máy Yếu/IOS/Resources','zip',f'./PMINMOD/{folder_mod}/{checkCamXa}/Máy Yếu/Android')