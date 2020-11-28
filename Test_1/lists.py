a = eval(input('请输入一个列表（请参照格式：[a,b,c]）：'))
print(list(filter(lambda x : x % 2 == 0,a)))