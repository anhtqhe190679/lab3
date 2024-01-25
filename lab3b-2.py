def hex_to_decimal(hex_string):
    try:
        decimal_value = int(hex_string, 16)
        print(f"Giá trị cơ số 10 của {hex_string} là: {decimal_value}")
    except ValueError:
        print(f"Lỗi: {hex_string} không phải là chuỗi thập lục phân hợp lệ.")

user_input = input("Nhập cơ số 16: ")
if all(char.isdigit() or char.lower() in 'abcdef' for char in user_input):
    hex_to_decimal(user_input)
else:
    print("Lỗi: Chuỗi đầu vào chứa ký tự không phải là chữ số thập lục phân.")