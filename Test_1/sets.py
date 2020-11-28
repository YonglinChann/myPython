setA = eval(input('请输入集合A（请参照格式：{a,b,c}）：'))
setB = eval(input('请输入集合B（请参照格式：{a,b,c}）：'))

print('集合AB的交集为：',setA & setB,'\n')
print('集合AB的并集为：',setA | setB,'\n')
print('集合AB的差为：',setA - setB)