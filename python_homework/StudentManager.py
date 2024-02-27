"""
作业：
实现学生管理系统：

学生信息包含：
    - 编号（sid), 姓名（name), 年龄（age), 性别（gender) 四个信息
    - 每个学生信息使用字典形式保存
    - 使用列表保存所有学生的信息

1. 实现菜单函数，输出下列信息，返回用户输入的编号，并进行输入校验。

    print("****************************************")
    print("*                                学生管理系统                         *")
    print("*              1. 添加新学生信息              *")
    print("*             2. 通过学号修改学生信息                 *")
    print("*                3. 通过学号删除学生信息                 *")
    print("*                4. 通过姓名删除学生信息                 *")
    print("*             5. 通过学号查询学生信息          *")
    print("*                6. 通过姓名查询学生信息          *")
    print("*                7. 显示所有学生信息             *")
    print("*                8. 退出系统                                           *")
    print("****************************************")
    select_op = input("输入编号选择操作：")

2. 实现控制函数，用来控制菜单的输出与功能的选择，直到用户选择8，结束程序运行。
3. 实现添加学生函数，函数参数为编号，姓名，年龄，性别四个参数，返回是否添加成功的结果，要求编号不可重复。
4. 实现修改函数，参数为学号，如果学生存在，则进行修改，不存在输出提示，并返回是否修改成功
5. 实现删除函数，参数为学号，如果学生存在，则进行删除，不存在输出提示，并返回是否删除成功
6. 实现删除函数，参数为姓名，如果学生存在，则进行删除（同名学生全部删除），不存在输出提示，并返回是否删除成功
7. 实现查询函数，参数为学号，如果学生存在，则输出学生信息，不存在输出提示，并返回是否查询成功
8. 实现查询函数，参数为姓名，如果学生存在，则输出学生信息（同名学生全部输出），不存在输出提示，并返回是否删除成功
9. 实现函数，输出所有学生信息
"""


class StudentManger:

    def __init__(self):
        self.students = []

    def menu(self):
        print("****************************************")
        print("*                                学生管理系统                         *")
        print("*              1. 添加新学生信息              *")
        print("*             2. 通过学号修改学生信息                 *")
        print("*                3. 通过学号删除学生信息                 *")
        print("*                4. 通过姓名删除学生信息                 *")
        print("*             5. 通过学号查询学生信息          *")
        print("*                6. 通过姓名查询学生信息          *")
        print("*                7. 显示所有学生信息             *")
        print("*                8. 退出系统                                           *")
        print("****************************************")
        select_op = input("输入编号选择操作：")
        return select_op

    def control_func(self):
        while True:
            select_op = self.menu()
            if select_op in "12345678":

                if select_op == '1':
                    self.add_student()
                elif select_op == '2':
                    self.modify_by_sid()
                elif select_op == '3':
                    self.delete_by_sid()
                elif select_op == '4':
                    self.delete_by_name()
                elif select_op == '5':
                    self.query_by_sid()
                elif select_op == '6':
                    self.query_by_name()
                elif select_op == '7':
                    self.show_all_students()
                elif select_op == '8':
                    print("退出系统")
                    break
            else:
                print("输入无效，请重新输入")

    # 1-添加学生
    def add_student(self):
        new_sid = input("请输入学号：")
        new_name = input("请输入姓名：")
        new_age = input("请输入年龄：")
        new_gender = input("请输入性别：")
        new_student = {'sid': new_sid, 'name': new_name, 'age': new_age, 'gender': new_gender}
        for student in self.students:
            if student["sid"] == new_sid:
                print("该学生已存在，添加失败")
        self.students.append(new_student)

    # 2-通过学号修改学生信息
    def modify_by_sid(self):
        sid = input("请输入需修改学生学号：")

        for student in self.students:
            if student["sid"] == sid:
                student["name"] = input("请输入姓名：")
                student["age"] = input("请输入年龄：")
                student["gender"] = input("请输入性别：")
        else:
            print("该学生信息不存在")

    # 3-通过学号删除学生信息
    def delete_by_sid(self):
        sid = input("请输入需删除学生学号：")
        for student in self.students:
            if student["sid"] == sid:
                self.students.remove(student)
        else:
            print("该学生信息不存在")

    # 4. 通过姓名删除学生信息
    def delete_by_name(self):
        name = input("请输入需删除学生姓名：")
        # 标志位
        count = 0
        for student in self.students:
            if student["name"] == name:
                self.students.remove(student)
                count += 1

        if count > 0:
            print(f"删除 {name} 成功")
    # 5. 通过学号查询学生信息
    def query_by_sid(self):
        sid = input("请输入需查询学生学号：")
        for student in self.students:
            if student["sid"] == sid:
                print(student)
        else:
            print("该学生信息不存在")
    # 6. 通过姓名查询学生信息
    def query_by_sid(self):
        name = input("请输入需查询学生姓名：")
        stu = []
        for student in self.students:
            if student["name"] == name:
                stu.append(student)
        if stu:
            for i in stu:
                print(i)
        else:
            print("该学生信息不存在")

    # 7. 显示所有学生信息
    def show_all_students(self):
        if len(self.students) != 0:
            for student in self.students:
                print(student)
        else:
            print("学生信息为空")


# 测试
sms = StudentManger()
sms.control_func()
