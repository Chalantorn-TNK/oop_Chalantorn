class Product:
    def __init__(self,name,price,stock):
        self.name = name
        self.__price = price
        self.__stock = stock
        self.Product = []  

    def addproduct(self):
        while True:
            print("เพิ่มสินค้า (พิมพ์ 'หยุด' สิ้นสุดการเพิ่ม)")
            name = input("ชื่อสินค้า: ")
            if name == "หยุด":
                break
            
            price = int(input("ราคา: "))
            stock = int(input("จำนวน: "))
            self.Product.append({"ชื่อสินค้า": name, "ราคา": price, "จำนวน": stock})
           
        print("เพิ่มสินค้าเสร็จสิ้น!")
        
    def addstock(self, add):
        self.__stock += add

    def checkproduct(self):
        return f"ชื่อสินค้า: {self.name}, ราคา: {self.__price}, จำนวน: {self.__stock}"

    def editprice(self, edit):
        self.__price = edit



pd1 = Product("สินค้า1", 400, 5)
pd1.addstock(1)
pd1.editprice(200)
print(pd1.checkproduct())
pd1.addproduct()


