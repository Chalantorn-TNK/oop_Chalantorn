print('กรอกข้อมูล')
name = str(input('โปรดกรอกชื่อ \n'))

age = int(input('โปรดกรอกอายุ \n'))

id = int(input('โปรดกรอกรหัสประจำตัว \n'))

level = int(input('โปรดกรอกระดับชั้น \n'))

nickname = str(input('โปรดกรอกชื่อเล่น \n'))

height = float(input('โปรดกรอกส่วนสูง \n'))

weight = float(input('โปรดกรอกน้ำหนัก \n'))

print(f'\nชื่อ:   {name}   อายุ:    {age}  ปี')
print(f'รหัสประจำตัวนักเรียน:  {id}   ระดับชั้น:   {level}')
print(f'ชื่อเล่น:   {nickname}')
print(f'ส่วนสูง: {height}   เซนติเมตร  น้ำหนัก: {weight} กิโลกรัม')
print(f'ส่วนสูง + น้ำหนัก = {height + weight}')