s = str(input('请输入一句英文单词：'))
a = []
for i in s.split(' '):
    if i not in a:
        a.append(i)

result = ' '.join(a)
print('\n结果为：',result)