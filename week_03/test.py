print('กรอกข้อมูล')
name = str(input('โปรดกรอกชื่อ \n'))

age = int(input('โปรดกรอกอายุ \n'))

id = int(input('โปรดกรอกรหัสประจำตัว \n'))

level = int(input('โปรดกรอกระดับชั้น \n'))

nickname = str(input('โปรดกรอกชื่อเล่น \n'))


height = float(input('โปรดกรอกส่วนสูง \n'))

weight = float(input('โปรดกรอกน้ำหนัก \n'))

print('ชื่อ:', name , 'อายุ:' , age ,'ปี \n' 'รหัสประจำตัวนักเรียน:' , id , 'ระดับชั้น:' , level )
print('ชื่อเล่น:' , nickname)
print('ส่วนสูง:' , height , 'น้ำหนัก:' , weight)
print('ส่วนสูง + น้ำหนัก =' , height + weight)