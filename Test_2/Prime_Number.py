maxNumber = int(input('请输入自然数：（要求大于2）'))
lst = list(range(2,maxNumber))
m = int(maxNumber ** 0.5)

for index,value in enumerate(lst):
    if value > m:
        break
    for value_0 in lst [: index : -1]:
        print('\n',(value_0),'\n')
        if value_0 % value == 0:
            lst.remove(value_0)
print('\n列表结果为：',(lst),'\n')