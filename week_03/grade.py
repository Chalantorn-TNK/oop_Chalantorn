print('โปรแกรมตัดเกรด')
point = int(input('ใส่คะแนน '))

if  point > 100:
    print('กรอกคะแนนไม่เกิน 100')

elif point >= 80:
    print('ได้เกรด 4')

elif point >= 70:
    print('ได้เกรด 3')
    
elif point >= 60:
    print('ได้เกรด 2')

elif point >= 50:
    print('ได้เกรด 1')

elif point < 0:
    print('ห้ามกรอกคะแนนน้อยกว่า 0')

else:
    point < 49
    print('ได้เกรด 0 ')
    print('ต้องการแก้หรือไม่')
    solve = input(' พิมพ์ Y/N ')
    if  solve == 'Y':
        print('คุณสอบแก้ผ่าน')
        print(f'คะแนนที่ขาด คือ {50-point}คะแนน')
    elif solve == 'N':
        print('คุณสอบไม่ผ่าน')

    else: 
        print('กรอก Y หรือ N เท่านั้น')
    

