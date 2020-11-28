import re
words = input("请输入一句英文：")
l = re.split('[\. ]+',words)
print(l)
ji = 0
for i in l:
    if len(i) == 5:
        print(i)
    else:
        print('')