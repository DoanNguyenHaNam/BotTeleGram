import os
for file in os.listdir('xml'):
	with open(f'xml/{file}','rb') as f:
		a=f.read()
		with open(f'xml/{file}','wb') as f:
			f.write(a)
		if b'</Item>' in a:
			import xml.etree.ElementTree as ET
			def byteint(num):
				return num.to_bytes(4, byteorder = 'little')

			def bytestr(stri):
				outbyte=byteint(len(stri)+4)
				outbyte=outbyte+stri.encode()
				return outbyte

			def byteattr(key,attr):
				if key == 'Var':
					if attr[key] == 'Array':
						stri = 'JTArr'
					elif attr[key] == 'String':
						stri = 'JTPri'
					else:
						stri = 'JT' + attr[key]
					aid = 6
				elif key == 'Var_Raw':
					stri = attr[key]
					aid = 6
				elif key == 'Type':
					stri = 'Type' + attr[key]
					aid = 8
				elif key=='Type_Raw':
					stri=attr[key]
					aid=8
				else:
					import unicodedata
					if unicodedata.numeric(key):
						stri = attr[key]
						aid = int(key)
				stripro=stri.encode()
				outbyte = byteint(len(stripro) + 8) + byteint(aid) + stripro
				return outbyte

			def bytenode(node):
				iftex=False
				if node.tag=='Item':
					name1='Element'
				else:
					name1=node.tag
				name=bytestr(name1)
				attr1=b''
				aindex=len(node.attrib)
				plus=8
				for key in node.attrib:
					attr1=attr1+byteattr(key,node.attrib)
				if (node.text!=None) and (node.text[0:1]!='\n'):
					if node.text==' ':
						stri1=''
					else:
						stri1=node.text
					iftex=True
					stripro=('V'+stri1).encode()
					attr1=attr1+byteint(len(stripro)+8)+byteint(5)+stripro+byteint(4)
					aindex+=1
					plus=4
				attr1=byteint(len(attr1)+plus)+byteint(aindex)+attr1+byteint(4)
				alchild=b''
				if len(node):
					cindex=0
					for child in node:
						alchild=alchild+bytenode(child)
						cindex+=1
					alchild = byteint(len(alchild) + 8) + byteint(cindex) + alchild
				else:
					if iftex==False:
						alchild=byteint(4)
				bnode = name + attr1 + alchild
				bnode = byteint(len(bnode)+4) + bnode
				return bnode
			#PATH
			xmlfile=f'xml/{file}'
			tree=ET.parse(xmlfile)
			attr=b''
			byt=bytenode(tree.getroot())
			if os.path.isdir(f'bytes') == 0 :
				os.mkdir(f'bytes')
			f=open(f'bytes/{file}','wb')
			f.write(byt)
			f.close()
			
		if b'\x04\x00\x00\x00' in a:
			# -*- coding:utf-8 -*-
			import xml.etree.ElementTree as ET
			import sys
			from xml.dom import minidom

			def getint():
				return int.from_bytes(byt.read(4), 'little')

			def  getstr(pos=None):
				if pos is not None:
					byt.seek(pos, 0)
				ofs=getint()
				stri=byt.read(ofs-4)
				return stri.decode()

			def analynode(fid=None, sta=None):
				global i
				if sta==None:
					sta = byt.tell()
				else:
					byt.seek(sta, 0)
				ofs=getint()
				stri=getstr()
				if stri=='Element':
					stri1='Item'
				else:
					stri1=stri
				myid=i
				i=i+1
				byt.seek(4,1)
				aidx=getint()
				ite=False
				attr={}
				for j in range(0,aidx):
					attr1=analyattr()
					if type(attr1)==str:
						text1=attr1
						ite=True
					else:
						attr.update(attr1)
				if fid == None:
					nod[myid] = ET.SubElement(root, stri1, attrib=attr)
				else:
					nod[myid] = ET.SubElement(nod[fid], stri1, attrib=attr)
				if ite==True:
					if text1=='':
						nod[myid].text=' '
					else:
						nod[myid].text=text1
				checkfour()
				chk=sta+ofs-byt.tell()
				if chk>12:
					byt.seek(4,1)
					sidx=getint()
					for h in range (0,sidx):
						attr=analynode(myid,byt.tell())
				byt.seek(sta+ofs,0)

			def analyattr(pos=None):
				if pos==None:
					pos = byt.tell()
				else:
					byt.seek(pos, 0)
				ofs = getint()
				type = getint()
				if type == 5:
					stri = byt.read(ofs - 8).decode()[1:]
					checkfour()
					byt.seek(pos + ofs, 0)
					return stri
				else:
					if type == 6:
						stri = byt.read(ofs - 8).decode()
						if stri[0:2] == 'JT':
							if stri == 'JTArr':
								stri = 'Array'
							elif stri == 'JTPri':
								stri = 'String'
							else:
								stri = stri[2:]
							name = 'Var'
						else:
							name = 'Var_Raw'
					elif type == 8:
						stri2 = byt.read(ofs - 8).decode()
						if stri2[0:4]=='Type':
							stri=stri2[4:]
							name = 'Type'
						else:
							stri=stri2
							name='Type_Raw'
					else:
						stri = byt.read(ofs - 8).decode()
						name = str(type)
						byt.seek(pos + ofs, 0)
					return {name:stri}

			def checkfour():
				if getint()!=4:
					byt.seek(-4,1)

			#PATH FILE
			filexml=f'xml/{file}'
			byt=open(filexml, 'rb')
			i=0
			nod={}
			ofs = getint()
			stri = getstr()
			if stri == 'Element':
				stri1 = 'Item'
			else:
				stri1 = stri
			byt.seek(4, 1)
			aidx = getint()
			ite = False
			attr={}
			for j in range(0, aidx):
				attr1 = analyattr()
				if type(attr1) == str:
					text1 = attr1
					ite = true
				else:
					attr.update(attr1)
				root = ET.Element(stri1, attrib=attr)
			if ite == True:
				nod[myid].text = text1
			checkfour()
			chk = ofs - byt.tell()
			if chk > 12:
				byt.seek(4, 1)
				sidx = getint()
				for h in range(0, sidx):
					analynode(None, byt.tell())
			byt.close
			xmlstr = minidom.parseString(ET.tostring(root)).toprettyxml(indent="   ")
			if os.path.isdir(f'xml') == 0 :
				os.mkdir(f'xml')
			with open(f'xml/{file}', "w" , encoding="utf-8") as f:
				f.write(xmlstr)
		skinid=''
		if skinid=='':pass
		else:
			with open(f'xml/{file}', "r" , encoding="utf-8") as f:
				xml=f.read()
				for skin in xml.split('\n      <Item Var="Com" Type="Assets.Scripts.GameLogic.SkinElement">'):
					if f'/{skinid}_' in skin:
						break
				skin=skin.replace('<ArtSkinPrefabLOD ','<ArtPrefabLOD ').replace('</ArtSkinPrefabLOD>','</ArtPrefabLOD>').replace('<ArtSkinLobbyShowLOD ','<ArtLobbyShowLOD ').replace('</ArtSkinLobbyShowLOD>','</ArtLobbyShowLOD>')
				skin=skin[skin.find('<ArtPrefabLOD '):]
				p=skin.find('\n      </Item>')
				if p!=-1:
					skin=skin[:p]
				skin=skin.replace('>\n      ','>\n')
				p=xml.find('<ArtPrefabLOD ')
				p2=xml.find('\n   <SkinPrefab ')
				de=xml[p:p2]
				xml=xml.replace(de,skin,1)
				xml=rut_gon_infos(xml)
				xml=xml.replace('hero_skill_effects/141_DiaoChan/14111_','hero_skill_effects/141_DiaoChan/14111/14111_')
				pz=xml.split('\n      <Item Var="Com" Type="Assets.Scripts.GameLogic.SkinElement">')
				for i in range(1,len(pz)-1):
					if f'/{skinid}_' in pz[i]:
						skin=pz[i]
						p=skin.find('\n      </Item>')
						if p!=-1:
							skin=skin[:p+len('\n      </Item>')]
						break
				for i in range(1,len(pz)-1):
					p=pz[i].find('\n      </Item>')
					xml=xml.replace(pz[i][:p+len('\n      </Item>')],skin,1)
				with open(f'xml/{file}', "w" , encoding="utf-8") as f:
					f.write(xml)