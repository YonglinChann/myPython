import types
class Person(object):
    def __init__(self, name = '', age = 20, sex = 'man'):
        self.setName(name)
        self.setAge(age)
        self.setSex(sex)
    def setName(self, name):
        if not isinstance(name,str):
            print('姓名必须为字符串！')
            return
        self.__name = name
    def setAge(self, age):
        if not isinstance(age,int):
            print('年龄必须是整数！')
            return
        self.__age = age
    def setSex(self, sex):
        if sex != '男' and sex != '女':
            print('性别必须是男性或女性！')
            return
        self.__sex = sex
    def show(self):
        print(self.__name)
        print(self.__age)
        print(self.__sex)

class Student(Person):
    def __init__(self, name = '', age = 30, sex = 'man', major = 'Computer'):
        super(Student, self).__init__(name, age, sex)
        self.setMajor(major)
    def setMajor(self, major):
        if not isinstance(major, str):
            print('学科必须是字符串！')
            return
        self.__major = major
    def show(self):
        super(Student, self).show()
        print(self.__major)

if __name__ == '__main__':
    xiaozhang = Person('校长', 60, '男')
    xiaozhang.show()
    alin = Student('阿林', 20, '男', '物联网工程18')
    alin.show()