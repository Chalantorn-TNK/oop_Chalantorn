a = int(input("ใส่ค่า: "))
i = 1
while i < 25:
    sum = a * i
    b = sum / 2
    if b % 2 != 0: 
        print(f"{a} * {i} = {b}")
    i += 1  
