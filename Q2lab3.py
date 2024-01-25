n = int(input("Nhập 1 số nguyên: "))

def phan1():
    print("Các số nguyên chia hết cho 5: ")
    for i in range(1, n+1):
        if i > 500:
            break
        elif i > 150:
            continue
        elif i % 5 == 0:
            print(i)

def phan2():
    b = int(input("Nhập số nguyên: "))
    b = str(b)
    do_dai = len(b)
    print(f"Số digits của {b} là: {do_dai} ")

def phan3():
    c = input("Nhập dãy số (cách nhau bằng dấu cách): ").split()
    for i in reversed(c):
        print(i)
    
print(phan1())
print(phan2())
print(phan3())
