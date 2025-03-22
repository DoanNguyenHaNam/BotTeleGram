if True:
	import os
	try:import pyzstd;from colorama import Fore;from colorama import Fore;from colorama import Style;from colorama import Style;from termcolor import colored
	except:
		try:os.system('python -m pip install pyzstd');os.system('python -m pip install termcolor');os.system('python -m pip install colorama');import pyzstd;from colorama import Fore;from colorama import Fore;from colorama import Style;from colorama import Style
		except:os.system('pip install pyzstd');os.system('pip install termcolor');os.system('pip install colorama');import pyzstd;from colorama import Fore;from colorama import Fore;from colorama import Style;from colorama import Style
	from shutil import make_archive;from pyzstd import decompress,compress,ZstdDict;from os import listdir;import sys;import os;from termcolor import colored;import re;import getopt;import pyzstd;import sys;import glob;import colorama;from colorama import Fore;from colorama import Style;from colorama import Fore;from colorama import Style;import shutil;import zipfile;import shutil;from zipfile import* 
	os.system('color')
	mac_dinh=[b'105: Toro', b'106: Krixi', b'107: Zephys', b'108: Gildur', b'109: Veera', b'110: Kahlii', b'111: Violet', b'112: Yorn', b'113: Chaugnar', b'114: Omega', b'115: Jinna', b'116: Butterfly', b'117: Ormarr', b'118: Alice', b'119: Mganga', b'120: Mina', b'121: Marja', b'123: Maloch', b'124: Ignis', b'126: Arduin', b"127: Azzen'Ka", b'128: L\xe1\xbb\xaf B\xe1\xbb\x91', b'129: Tri\xe1\xbb\x87u V\xc3\xa2n', b'130: Airi', b'131: Murad', b'132: Hayate', b'133: Valhein', b'134: Skud', b'135: Thane', b'136: Ilumia', b'137: Paine', b"139: Kil'Groth", b'140: Superman', b'141: Lauriel', b'142: Natalya', b'144: Taara', b'146: Zill', b'148: Preyta', b'149: Xeniel', b'150: Nakroth', b'152: \xc4\x90i\xc3\xaau Thuy\xe1\xbb\x81n', b'153: Kaine', b'154: Yena', b'156: Aleister', b'157: Raz', b'162: Kriknak', b'163: Ryoma', b'166: Arthur', b'167: Ng\xe1\xbb\x99 Kh\xc3\xb4ng', b'168: Lumburr', b'169: Slimz', b'170: Moren', b'171: Cresht', b'173: Fennik', b'174: Joker', b'175: Grakk', b'177: Lindis', b'180: Max', b'184: Helen', b'186: TeeMee', b'187: Arum', b'189: Krizzix', b'190: Tulen', b'191: Rouie', b'192: Celica', b'193: Amily', b'194: Wiro', b'195: Enzo', b'196: Elsu', b"199: Elando'rr", b'206: Charlotte',b'501: TelAnnas', b'502: Astrid', b'503: Zuka', b'504: Wonder Woman', b'505: Baldum', b'506: Omen', b'507: The Flash', b'508: Wisp', b"509: Y'bneth", b'510: Liliana', b'511: Ata', b'512: Rourke', b'513: Zata', b'514: Roxie', b'515: Richter', b'518: Quillen', b'519: Annette', b'520: Veres', b'521: Florentino', b'522: Errol', b"523: D'Arcy", b'524: Capheny', b'525: Zip', b'526: Ishar', b'527: Sephera', b'528: Qi', b'529: Volkath', b'530: Dirak', b'531: Keera', b'532: Thorne', b'533: Laville', b'534: Dextra', b'535: Sinestrea', b'536: Aoi', b'537: Allain', b'538: Iggy', b'539: Lorion', b'540: Bright', b'541: Bonnie', b'542: Tachi', b'543: Aya', b'544: Yan', b'545: Yue', b'546: Teeri', b'548: Bijan',b'567: Erin',b'568: Ming',b'597: Biron']
	from __init__ import *
	def hex_to_dec(a):
		len(a)
		a=a[::-1]
		a=a.hex()
		a=int(a,16)
		return a
	def dec_to_hex(a):
		a=hex(a)[2:]
		if len(a)%2==1:
			a='0'+a
		return (bytes.fromhex(a))[::-1]
	def ten_skin_hieu_ung(skinid):
		with open('Pmin_Sources/Resources/1.57.1/Databin/Client/Actor/heroSkin.bytes','rb') as f:
			a=f.read()
			a=decompress_(a,ZSTD_DICT)
			p=a.find(dec_to_hex(skinid)+b'\x00\x00'+dec_to_hex(int(str(skinid)[:3])))
			if p!=-1:
				ten=a[p+12:p+31]
				skin=a[p+40:p+59]
				code=a[p-4:p+hex_to_dec(a[p-4:p-2])]
				if b'Skin_' in code:
					h=b'\x8f'
				else:
					h=b'PminMod'
					with open(f'./Pmin_Sources/Resources/1.57.1/Databin/Client/Sound/BattleBank.bytes','rb') as f:
						a=f.read()
						a=decompress_(a,ZSTD_DICT)
						if bytes(str(skinid),'utf-8') in a:
							h=b'\x8f'
				if skinid==13204 or skinid==53702 or skinid == 15305:h=b'\x8f'
		txt=open('Pmin_Sources/resources/1.57.1/Languages/VN_Garena_VN/languageMap_Xls.txt','rb')
		a=txt.read()
		a=decompress_(a,ZSTD_DICT)
		txt=a.split(b'\r')
		'''p=a.find(ten)
		a1=a[p+len(ten)+3:a.find(b'\r',p)].decode()
		print(a1)
		p=a.find(skin)
		a2=a[p+len(skin)+3:a.find(b'\r',p)].decode()
		print(a2)'''
		try:
			for i in txt:
				if ten in i:
					a1=i[len(ten)+3:]
					break
			for i in txt:
				if skin in i:
					a2=i[len(skin)+3:]
					break
		except:h=b'PminMod'
		try:
			b1=a1;b2=a2
		except:b1,b2=b'',b''
		return b1+b' '+b2
	ten=b''
	'''for a in mac_dinh:
		ten=ten+b"####\n"
		ten=ten+a+b'\n-->'
		a=int(a[:3].decode())
		for i in range(1,20):
			h=ten_skin_hieu_ung(a*100+i)
			ten=ten+str(a*100+i).encode('utf-8')+b' : '+h+b'\n-->'
		ten+=b'\n'
		with open('id_skinnn.txt','wb') as f:f.write(ten)'''
	List_Id=[]
	for id in os.listdir(f'./Pmin_Sources/Resources/1.57.1/Ages/Prefab_Characters/Prefab_Hero'):
					if '_' in id and 'bytes' not in id:
						id=id[:3].encode('utf-8')
						List_Id.append(id)
	output=b''
	with open(f'./Pmin_Sources/Resources/1.57.1/Databin/Client/Sound/BattleBank.bytes','rb') as f:
		a=f.read()
		a=decompress_(a,ZSTD_DICT)
		a=a[134:]
		while len(a)>40:
			dem=a[6:8]
			dem=hex_to_dec(dem)
			code=a[:dem+4]
			if b'SFX' not in code and b'VO' not in code:
				pass
			else:
				for id in List_Id:
					p=code.find(id)
					if p!=-1 and code[p:p+5] not in output:
						if (b'_' in code[p:p+5]):
							p=code.find(id,p+1)
							if p!=-1 and code[p:p+5] not in output:
								output+=code[p:p+5]+b': '+ten_skin_hieu_ung(int(code[p:p+5].decode()))+b'\n'
						else:
							output+=code[p:p+5]+b': '+ten_skin_hieu_ung(int(code[p:p+5].decode()))+b'\n'
				print(code)
			a=a[dem+4:]
	with open(f'#id_effect.txt','wb') as f:
							f.write(output)
if True:
    import os
    
    # Đọc dữ liệu từ file
    with open('#id_effect.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    # Tạo dictionary để lưu các nhóm theo 3 chữ số đầu tiên
    grouped_data = {}
    
    for line in lines:
        line = line.strip()  # Loại bỏ khoảng trắng và xuống dòng
        if line:
            # Lấy 3 chữ số đầu tiên của ID
            group_key = line[:3]
            if group_key not in grouped_data:
                grouped_data[group_key] = []
            grouped_data[group_key].append(line)
    
    # Ghi dữ liệu đã sắp xếp ra file mới
    with open('#id_effect_split.txt', 'w', encoding='utf-8') as f:
        for group_key in sorted(grouped_data.keys()):  # Sắp xếp theo group_key
            f.write(f"**{group_key}**\n")
            f.write("\n".join(grouped_data[group_key]) + "\n\n")
