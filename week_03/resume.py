print('กรอกข้อมูล')
name = str(input('โปรดกรอกชื่อ \n'))

age = int(input('โปรดกรอกอายุ \n'))

id = int(input('โปรดกรอกรหัสประจำตัว \n'))

level = int(input('โปรดกรอกระดับชั้น \n'))

nickname = str(input('โปรดกรอกชื่อเล่น \n'))


height = float(input('โปรดกรอกส่วนสูง \n'))

weight = float(input('โปรดกรอกน้ำหนัก \n'))

print('\nชื่อ: ' + name +  ' อายุ: '  +str (age) + ' ปี')
print('รหัสประจำตัวนักเรียน: ' +  str (id)   + ' ระดับชั้น: ' + str(level))
print('ชื่อเล่น: ' +  nickname)
print('ส่วนสูง: ' + str (height) + ' เซนติเมตร' + ' น้ำหนัก: ' + str (weight) +' กิโลกรัม')
print('ส่วนสูง + น้ำหนัก = ' + str(height + weight))