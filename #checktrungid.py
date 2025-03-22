import os
with open('list_mod.txt','rb') as f:
    txt=f.read()
List=[]
List2=[]
'''i=0
for idd in txt.split(b'\r\n'):
    if idd[:3] not in List:
        p=idd.find(b' ')
        if p!=-1:
            t=idd[:p]
        List2.append(t)
        List.append(idd[:3])
    else:
        print(i,idd)
    i+=1'''
List2=[b'15015', b'15015', b'15015', b'15015', b'11607', b'15710', b'16712', b'16311', b'17407', b'17407', b'17407', b'53107', b'13011', b'13011', b'53503', b'15204', b'15204', b'12106', b'51306', b'54307', b'52414', b'13311', b'53702', b'54002', b'54402', b'54804', b'11113', b'11113', b'14213', b'52102', b'50308', b'53608', b'53802', b'13609', b'10620', b'10620', b'17504', b'54505', b'14111', b'53002', b'53002', b'12912', b'10506', b'10506', b'10506', b'15612', b'50605', b'50605', b'50605']
with open('list_mod.txt','wb') as f:
    for ID in List2:
        f.write(ID+b'\r\n')