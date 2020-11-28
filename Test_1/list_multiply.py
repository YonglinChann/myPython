from functools import reduce
a = eval(input('请输入包含若干整数的列表（请参照格式：[1,2,3,4]）：'))
a = reduce(lambda x,y : x * y,a)
print('整数列表的连乘结果为：',a)