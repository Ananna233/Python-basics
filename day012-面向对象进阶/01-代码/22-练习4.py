# 学生类 Student:
# 属性：学号，姓名，年龄，性别，成绩

# 班级类 Grade
# 属性 班级名称，班中的学生【使用列表存储学生】
# 方法
# 1.查看该班级中的所有学生的信息
# 2.查看指定学号的学生信息
# 3.查看班级中成绩不及格的学生信息
# 4.将班级中的学生按照成绩降序排序

class Student(object):
    def __init__(self, number, name, age, gender, score):
        self.number = number
        self.name = name
        self.age = age
        self.gender = gender
        self.score = score

    def __str__(self):  # 重写 print(Student)
        return '学号:{}, 姓名:{}, 年龄{}, 性别{}, 成绩{}'.format(self.number, self.name, self.age, self.gender, self.score)


class Grade(object):
    def __init__(self, class_name, students=None):
        self.class_name = class_name
        if students == None:
            students = []
        self.students = students

    def show_all(self):  # 1.查看该班级中的所有学生的信息
        for student in self.students:
            print(student)

    def search(self, num):  # 2.查看指定学号的学生信息
        for student in self.students:
            if student.number == num:
                print(student)
                break
        else:
            print('查找不到该学生({})'.format(num))

    def failed_students(self):  # 3.查看班级中成绩不及格的学生信息
        result = filter(lambda student: student.score < 60, self.students)
        for student in result:
            print(student)

    def order_students(self):  # 4.将班级中的学生按照成绩降序排序
        # self.students.sort(key=lambda s: s.score, reverse=True)  # 直接修改self.students
        return sorted(self.students, key=lambda s: s.score, reverse=True)  # 不会修改原列表


s1 = Student('001', 'zhangsan', 18, 'male', 45)
s2 = Student('002', 'lisi', 20, 'female', 95)
s3 = Student('003', 'Tony', 17, 'male', 75)
s4 = Student('004', 'jack', 21, 'male', 90)
s5 = Student('005', 'xiaobai', 18, 'female', 58)

grade = Grade('G301', [s1, s2, s3, s4, s5])
grade.show_all()
grade.search('002')
print('-------------------')
grade.failed_students()
print('-------------------')
x = grade.order_students()
for student in x:
    print(student)
