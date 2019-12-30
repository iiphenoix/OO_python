import datetime
class Person:
    AllCount = 0
    def __init__(self,number,name,sex,birthday):
        self.number = number
        self.name = name
        self.birthday = birthday
        self.sex = sex
        Person.AllCount += 1

    @property
    def age(self):
        return datetime.date.today().year - self.birthday.year
    @age.setter
    def age(self,value):
        return AttributeError("禁止赋值年龄")

    @age.deleter
    def age(self):
        return AttributeError("年龄不能删除")

    def __repr__(self):
        return "<个人：{} at 0x{}>".format(self.number,id(self))

    def __str__(self):
        return "编号：{},姓名：{},性别：{}".format(self.number,self.name,self.sex)

    def __del__(self):
        Person.AllCount -= 1
