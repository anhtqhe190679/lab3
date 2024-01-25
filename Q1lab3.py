n = int(input("Nhập số n: "))

def phan1():
    b = int(input("Nhập số b: "))
    for i in range (1, b + 1, 1):
        for a in range (1,i+1):
            print(a, end=' ')
        print("")
                               
tong = 0
def phan2():
    tong = n*(n+1)/2
    return int(tong)
print(f"Tổng dãy số: ",phan2())
print(f"",phan1())