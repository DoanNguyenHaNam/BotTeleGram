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
for inp in os.listdir('Pmin_Sources/Resources/'):
	break
t1=f'./Pmin_Sources/Resources/{inp}/Ages/Prefab_Characters/Prefab_Hero/'
t2=f'./Pmin_Sources/Resources/{inp}/Prefab_Characters/'
for file in listdir(t2):
	if 'Actor' in file:
		print(giai_nen(t2,file),end='\r')
for file in listdir(t1):
	if 'Rapid' not in file and 'Newbie' not in file and 'Actor' in file:
		print(giai_nen(t1,file),end='\r')
	if file== 'CommonActions.pkg.bytes':
		print(giai_nen(t1,file),end='\r')
print(giai_nen(f'./Pmin_Sources/Resources/{inp}/Ages/','Prefab_Gear.pkg.bytes'),end='\r')