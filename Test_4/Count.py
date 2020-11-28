upcount = []
lowcount = []
digcount = []
othcount = []

def getstr(s):
    for i in s:
        if i.isupper():
            upcount.append(i)
        elif i.islower():
            lowcount.append(i)
        elif i.isdigit():
            digcount.append(i)
        else :
            othcount.append(i)
    return upcount, lowcount, digcount, othcount

s = input('请输入一个字符串：')
a, b, c, d = getstr(s)

print('大写字母的个数为：{}'.format(len(a)))
print('小写字母的个数为：{}'.format(len(b)))
print('数字的个数为：{}'.format(len(c)))
print('其他字符的个数为：{}'.format(len(d)))

a = tuple(a)
b = tuple(b)
c = tuple(c)
d = tuple(d)

print(a,b,c,d)

