import datetime
#注意包的导入格式
from OO.Person import Person as Person
from OO.Teacher import Teacher as Teacher
from OO.Student import  Student as Student
from OO.Department import Department as Department


if __name__ == '__main__':

    per = Person ("1","wu","女",datetime.date(1995,5,10))
    dep = Department("x","wi",6)
    tea = Teacher("1","wu","女",datetime.date(1995,5,10),dep,5000)

    stu = Student("a","li","男",datetime.date(1998,2,15),90)
    stu2 = Student("b", "Zhou", "女", datetime.date(1998, 2, 19), 80)  #必须是stu2,stu 是占原来的位置，使得stu.StudentCount不会加1

    #感受下两者区别，因为age使用了装饰器property且 @age.deleter进行修饰，所以age不能删除。同时为age的修改的函数也进行了修饰
    # del (per.age)
    # del (per.sex)
    # print(per.age)
    # print(per.sex)
    #
    #
    # print(per)  #调用Person.py里的__str()__函数
    # #脚本中直接写 per   调用__repr__(self)函数

    # print(tea.depatment.depnumber)  #获取教师所在的部门编号

    print(per.AllCount)
    print(tea.TeacherCount)
    print(stu.StudentCount)




