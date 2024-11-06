a = int(input("ใส่ค่า "))
for i in range(1,25):
    sum = a * i
    b = sum / 2
    if b % 2 != 0:
        print(f"{a} * {i} = {sum}")