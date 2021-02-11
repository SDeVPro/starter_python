# class Student:
#     def __init__(self,fish,kurs,ball,age):
#         self.fish = fish
#         self.kurs = kurs
#         self.ball = ball
#         self.age = age
#     def __str__(self):
#         return "FISH:\t"+self.fish + "Kursi:\t"+self.kurs + "Ball:\t"+self.ball + "Yoshi:\t"+self.age
    
# studentlist = []
# while True:
#     print("1-student qo'shish\n2-ro'yxatni chiqarish\n3-kursi bo'yicha tartiblash\n4-yoshi bo'yicha tartiblash\nq-quit")
#     cmd = input()
#     if cmd == "1":
#         fish = input("FISHni kiriting:")
#         kurs = input("Kursini kiriting:")
#         ball = input("Ballini kiriting:")
#         age = input("Yoshini kiriting:")

#         st = Student(fish,kurs, ball,age)
#         studentlist.append(st)
#     elif cmd == "2":
#         print("____________TALABA RO'YXATI_________")
#         for st in studentlist:
#             print(st)
#         print("_____________________________________")
#     elif cmd == "3":
#         sortedList = studentlist
#         sortedList.sort(key=lambda x:x.kurs)
#         for i in sortedList:
#             print(i)

#     elif cmd == "4":
#         sortedList = studentlist
#         sortedList.sort(key=lambda x:x.age)
#         for i in sortedList:
#             print(i)
#     elif cmd == "q":
#         break



# class Uy:
#     def __init__(self,turi,xonasi,rangi,balandligi):
#         self.turi = turi
#         self.xonasi = xonasi
#         self.rangi = rangi
#         self.balandligi = balandligi
#     def __str__(self):
#         return "Turi:\t"+self.turi + "Xonasi:\t"+self.xonasi + "Rangi:\t"+self.rangi + "Balandligi:\t"+self.balandligi
    
# Uylist = []
# while True:
#     print("1-Uyni qo'shish\n2-ro'yxatni chiqarish\n3-turi bo'yicha tartiblash\n4-xonasi bo'yicha tartiblash\nq-quit")
#     cmd = input()
#     if cmd == "1":
#         turi = input("TURni kiriting:")
#         Xonasi = input("Xonasini kiriting:")
#         Rangini = input("Rangini kiriting:")
#         Balandligini = input("Balandligini kiriting:")

#         home = Uy(turi,Xonasi,Rangini,Balandligini)
#         Uylist.append(home)
#     elif cmd == "2":
#         print("____UY RO'YXATI___")
#         for home in Uylist:
#             print(home)
#         print("_____________________________________")
#     elif cmd == "3":
#         sortedList = Uylist
#         sortedList.sort(key=lambda x:x.kurs)
#         for i in sortedList:
#             print(i)

#     elif cmd == "4":
#         sortedList = Uylist
#         sortedList.sort(key=lambda x:x.age)
#         for i in sortedList:
#             print(i)
#     elif cmd == "q":
#         break


class Car:
    def __init__(self,korxona,rusumi,rangi,yili,karobkasi,narhi):
        self.korxona = korxona
        self.rangi = rangi
        self.yili = yili
        self.karobkasi = karobkasi
        self.narhi = narhi
        self.rusumi = rusumi
    def __str__(self):
        return "Korxona\t" + self.korxona + "Rusumi\t" + self.rusumi + "Rangi:\t" + self.rangi + "Yili:\t"+self.yili + "Karobkasi:\t"+self.karobkasi + "Narhi\t" + narhi
    
avtolist = []
while True:
    print("1-mashina qo'shish\n2-ro'yxatni chiqarish\n3-yili bo'yicha tartiblash\n4-narhi bo'yicha tartiblash\nq-quit")
    cmd = input()
    if cmd == "1":
        korxona = input("Korxonani kiriting:")
        rangi = input("Rangini kiriting:")
        yili = input("yilini kiriting:")
        karobkasi = input("Karobkasini kiriting:")
        narhi = input("Narhini kiriting")
        rusumi = input("Mashina rusumini kiriting:")
        avto = Car(korxona,rangi,yili,karobkasi,narhi,rusumi)
        avtolist.append(avto)
    elif cmd == "2":
        print("____________MASHINA RO'YXATI_________")
        for avto in avtolist:
            print(avto)
        print("_____________________________________")
    elif cmd == "3":
        sortedList = avtolist
        sortedList.sort(key=lambda x:x.yili)
        for i in sortedList:
            print(i)

    elif cmd == "4":
        sortedList = avtolist
        sortedList.sort(key=lambda x:x.narhi)
        for i in sortedList:
            print(i)
    elif cmd == "q":
        break