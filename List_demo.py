MyCarList = ["Tesla","BMW", "Porshe", "BMW"]
def Display():
    for car in MyCarList:
        print(car)
    print("(0--0)--")
#Displaying content with the help of print Statment
print(MyCarList)
Display()
print("---------------------------------------------")
MyCarList[2] = "Audi"
#Changing one Element in List

MyCarList.append("Jaguar")
Display()
MyCarList.append("BMW")
Display()
print(MyCarList.count("BMW"))

print(MyCarList.reverse())
print(type(MyCarList))
Display()
