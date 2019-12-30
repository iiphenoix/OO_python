from  OO.Person import Person as p

class Student(p):
    StudentCount = 0
    def __init__(self,number,name,sex,birthday,grade):
        super().__init__(number,name,sex,birthday)
        self.grade = grade
        Student.StudentCount += 1



    def __del__(self):
        Student.StudentCount -= 1

    def __str__(self):
        return "编号：{},姓名：{},性别：{}".format(self.number,self.name,self.sex)



