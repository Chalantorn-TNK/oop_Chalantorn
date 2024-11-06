import random
while True:
    ran = random.choice(["ค้อน","กรรไกร","กระดาษ"])
    print("โปรแกรมเป่ายิงฉุบ")
    print(ran)
    print("เลือก ค้อน กรรไกร กระดาษ")
    play = str(input("คุณเลือก : "))


    win = 0
    lose = 0 
    allow = 0

    if play == ran:
        print("ผลลัพธ์คือ เสมอ")
        allow += 1
    elif play == "หยุด":
        print(f"ผลชนะ  = {win} ผลแพ้  = {lose} ผลเสมอ = {allow} ")
        break
    elif (play == "ค้อน" and ran == "กรรไกร"):
        print("คุณชนะ!")
        win += 1
    elif (play == "กรรไกร" and ran == "กระดาษ"):
        print("คุณชนะ!")
        win += 1
    elif (play== "กระดาษ" and ran == "ค้อน"):
        print("คุณชนะ!")
        win += 1
    else:
        print("คุณแพ้!")
        lose += 1
