chuoi1 = input("Nhập chữ thứ nhất: ")
chuoi2 = input("Nhập chuỗi thứ hai: ")
def la_anagrams(str1, str2):
    def clean_string(s):
        return ''.join(char.lower() for char in s if char.isalnum())

    clean_str1 = clean_string(str1)
    clean_str2 = clean_string(str2)

    return sorted(clean_str1) == sorted(clean_str2)

ket_qua = la_anagrams(chuoi1, chuoi2)

if ket_qua:
    print(f'"{chuoi1}" và "{chuoi2}" là từ hoán vị.')
else:
    print(f'"{chuoi1}" và "{chuoi2}" không phải là từ hoán vị.')