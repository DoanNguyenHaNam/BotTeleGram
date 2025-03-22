DIR='Pmin_Sources/Resources/1.57.1/Languages/VN_Garena_VN/languageMap_Xls.txt'
from __init__ import *
Input = input('EX: "15413: Yena Trấn Yêu Thần Lộc"').encode('utf-8').lower()
txt= open('language.txt','r')
for Input in txt:
    Input=Input.replace('\n','')
    Input=Input.encode('utf-8')
    def ten_skin_hieu_ung(skinid,Name=b'PminDepTrai'):
        with open('Pmin_Sources/Resources/1.57.1/Databin/Client/Actor/heroSkin.bytes','rb') as f:
            a=f.read()
            a=decompress_(a,ZSTD_DICT)
            p=a.find(dec_to_hex(skinid)+b'\x00\x00'+dec_to_hex(int(str(skinid)[:3])))
            if p!=-1:
                ten=a[p+12:p+31]
                skin=a[p+40:p+59]
                print(ten,skin)
        txt=open(DIR,'rb')
        a=txt.read()
        a=decompress_(a,ZSTD_DICT)
        p=a.find(ten)
        if p!=-1:
            p2=a.find(b'\r',p)
            ten=a[p:p2].replace(ten+b' = ',b'').lower()
            print(ten)
        p=a.find(skin)
        if p!=-1:
            p2=a.find(b'\r',p)
            a=a.replace(a[p:p2],skin+b' = '+(Name.lower()).replace(ten,b''))
            p2=a.find(b'\r',p)
            print(a[p:p2])
        else:
            a+=b'\r'+skin+b' = '+(Name.lower()).replace(ten,b'')
        with open(DIR,'wb') as f:
            f.write(a)
    if True:
        id=Input.split(b': ')[0]
        Name=Input.split(b': ')[1]
        ten_skin_hieu_ung(int(id.decode()),Name)    
