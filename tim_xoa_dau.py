import unicodedata

BANG_XOA_DAU = str.maketrans(
    "ÁÀẢÃẠĂẮẰẲẴẶÂẤẦẨẪẬĐÈÉẺẼẸÊẾỀỂỄỆÍÌỈĨỊÓÒỎÕỌÔỐỒỔỖỘƠỚỜỞỠỢÚÙỦŨỤƯỨỪỬỮỰÝỲỶỸỴ"
    "áàảãạăắằẳẵặâấầẩẫậđèéẻẽẹêếềểễệíìỉĩịóòỏõọôốồổỗộơớờởỡợúùủũụưứừửữựýỳỷỹỵ",
    "A"*17 + "D" + "E"*11 + "I"*5 + "O"*17 + "U"*11 + "Y"*5 +
    "a"*17 + "d" + "e"*11 + "i"*5 + "o"*17 + "u"*11 + "y"*5
)

inp = input('Nhập: ')

def xoa_dau(txt: str) -> str:
    if not unicodedata.is_normalized("NFC", txt):
        txt = unicodedata.normalize("NFC", txt)
    return txt.translate(BANG_XOA_DAU)

with open('tim.txt', encoding='utf-8') as f:  # Đọc file với UTF-8
    a = f.read()
    a = xoa_dau(a).lower()
    c = ''
    for t in a.split('\n'):
        p = t.find(' ')
        if inp == '':
            c += t[p+1:] + '\n'
        else:
            c += t + '\n'

with open('tim.txt', 'w', encoding='utf-8') as f:  # Ghi file với UTF-8
    f.write(c)
