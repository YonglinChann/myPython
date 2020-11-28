class Vector:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
    def add(self,another):
        x = self.x + another.x
        y = self.y + another.y
        z = self.z + another.z
        print('加法运算的结果为：({},{},{})'.format(x, y, z))
    def sub(self,another):
        x = self.x - another.x
        y = self.y - another.y
        z = self.z - another.z
        print('减法运算的结果为：({},{},{})'.format(x, y, z))
    def mul(self,n):
        x = self.x * n
        y = self.y * n
        z = self.z * n
        print('乘法运算的结果为：({},{},{})'.format(x, y, z))
    def tru(self,n):
        x = self.x / n
        y = self.y / n
        z = self.z / n
        print('除法运算的结果为：({},{},{})'.format(x,y,z))
    def length(self):
        a = pow(pow(self.x, 2) + pow(self.y, 2) + pow(self.z, 2), 0.5)
        print('长度为：{}'.format(round(a, 3)))

v1 = Vector(1,2,3)
v2 = Vector(2,3,4)
v1.add(v2)
v1.sub(v2)
v1.mul(2)
v1.tru(2)
v1.length()
