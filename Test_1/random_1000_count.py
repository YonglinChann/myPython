import random
a = [random.randint(0,100) for i in range(1000)]
b = set(a)
print('*结果如下：')
for i in b:
    print(i,' :',a.count(i))
print('（对应0-100各个整数 : 出现的次数）')