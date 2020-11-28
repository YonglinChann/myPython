s = str('This is is a book')
a = []
for i in s.split(' '):
    if i not in a:
        a.append(i)

result = ' '.join(a)
print('\n结果为：',result)