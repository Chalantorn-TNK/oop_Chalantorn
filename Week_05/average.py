num = []
number = int(input("ต้องการป้อนทั้งหมดกี่ตัว : "))
for i in range(1,number+1):
    ex = int(input(f"ใส่ค่าตัวที่ {i}:"))
    list.append(ex)
print(f"ค่าเฉลี่ยของ {list} = {sum(list)//number} ")