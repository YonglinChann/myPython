import math

def run(num):
    a = int(math.sqrt(num + 1))
    for i in range(2,num + 1):
        if num % i == 0:
            return '这个数 不是 素数。'
        else:
            return '这个数 是 素数。'

num = int(input('请输入一个数：'))

print('\n',run(num))