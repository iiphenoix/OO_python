class Department:
    def __init__(self,depnumber,adminstrate,louceng):
        self.depnumber = depnumber
        self.adminstrate = adminstrate
        self.louceng = louceng

    def __str__(self):
        return "编号：{},管理者：{},楼层：{}".format(self.depnumber,self.adminstrate,self.louceng)

