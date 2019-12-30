from  OO.Person import Person as Person
from OO.Department import Department as Department

class Teacher(Person):
    TeacherCount = 0
    def __init__(self, number,name,sex,birthday,depatment:Department, salay):
        super().__init__(number,name,sex,birthday)
        self.depatment = depatment
        self.salay = salay
        Teacher.TeacherCount += 1

    def give_raise(self, percent, bonus=.0):
        self.salay = self.salay * (1 + percent) + bonus

    def __del__(self):
        Teacher.TeacherCount -= 1

    def __str__(self):
        return "编号：{},姓名：{},性别：{}，部门：{}".format(self.number, self.name, self.sex,self.depatment)


