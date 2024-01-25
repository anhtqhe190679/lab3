import re
chuoi_1 = input("Nhập câu có chứa từ và số: ")
chuoi_2 = input("Nhập chuỗi có kí tự đặc biệt: ")
danh_sach_3 = input("Nhập 1 danh sách bất kì: ").split()
chuoi_4 = input("Viết 1 chuỗi mà các chữ phân tách bởi dấu gạch ngang: ")
def main():

    ket_qua_1 = xoa_ky_tu_khong_phai_so(chuoi_1)
    print("Công việc 1:", ket_qua_1)

   
    ket_qua_2 = xoa_ky_tu_dac_biet(chuoi_2)
    print("Công việc 2:", ket_qua_2)

   
    ket_qua_3 = xoa_chuoi_rong(danh_sach_3)
    print("Công việc 3:", ket_qua_3)

  
    ket_qua_4 = tach_theo_gach_ngang(chuoi_4)
    print("Công việc 4:", ket_qua_4)

def xoa_ky_tu_khong_phai_so(chuoi):
    return ''.join(ky_tu for ky_tu in chuoi if ky_tu.isdigit())

def xoa_ky_tu_dac_biet(chuoi):
    return re.sub(r'[^\w\s]', '', chuoi)

def xoa_chuoi_rong(danh_sach_chuoi):
    return list(filter(None, danh_sach_chuoi))

def tach_theo_gach_ngang(chuoi):
    return chuoi.split('-')

if __name__ == "__main__":
    main()
