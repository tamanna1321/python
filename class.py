class Student:
    def __init__(self,na):
        print("hello")
        # print(self)
        # print(na)
        # self.name= na
        # print(self.name)
    def getVal(self):
        self.name= input("Enter name ")
        self.classs= input("Enter class ")
    def printVal(self):
        print(f"The name of student is {self.name} and class is {self.classs}")
        
        
if __name__=="__main__":
    stu1= Student("Bhumika")
    stu1.getVal()
    # stu1.printVal()
    # print(stu1)
    stu2= Student("Tamanna")
    # print(stu2)
    stu2.getVal()
    stu1.printVal()
    stu2.printVal()