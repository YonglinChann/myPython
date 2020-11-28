a = input('请输入一个字符串：')
d = dict()
for ch in a:
    d[ch] = d.get(ch,0) + 1
result = max(d.items(),key = lambda item : item[1])
print('字符串中出现最多的【字符】及【次数】分别为：\n',result)