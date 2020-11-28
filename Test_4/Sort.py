def Sorted(s):
    a = []
    temp = s[::]
    while temp:
        c = min(temp)
        a.append(c)
        temp.remove(c)
    return a

s = []
str = input('请输入要排序的元素（用空格分开）：')
for i in str.split(' '):
    s.append(i)

print('排序的结果为：',Sorted(s))