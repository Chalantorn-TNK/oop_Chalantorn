num = int(input("จำนวนคนที่จะป้อน :"))
resume = {}
for i in range(1,num+1):
    print(f"กรุณากรอกคนที่ {i}")
    resume["nuckname"] = str(input("กรุณากรอกชื่อเล่น : "))
    resume["stdid"] = str(input("กรุณากรอกเลขที่ : "))
    resume["hobby"] = str(input("กรุณากรอกงานอดิเรก : "))
    resume["color"] = str(input("กรุณากรอกสีที่ชอบ : "))
    print(f"ข้อมูลคนที่ {str(i)}\n{resume}")