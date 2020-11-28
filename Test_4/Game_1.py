import random
import string

origin =''.join(random.sample(string.ascii_letters+string.digits,50))+''.join(random.sample(string.ascii_letters+string.digits,50))

def judge():
    #origin="Python的创始人为Guido van Rossum"    #练习的内容
    print("练习内容：")
    print(origin)
    while True:         #进行长度的检测，如果长度不符合标准那么就重新输入
        try:
            useInput = input("请输入:")
            assert len(useInput) == len(origin)    # assert断言：可以理解为“这里一定是成立的”，如果表达式不成立（False），则抛出异常。
        except:
            print("输入的长度有误,请再次输入")
        else:
            count = 0 #对正确的进行计数
            for i in range(len(origin)):        #对每一个字符进行比较
                if useInput[i] == origin[i]:
                    count = count + 1
                else:
                    continue
            result = round(count / len(origin) * 100,2)
            while result > 0:
                if result >= 90:
                    print('优秀')
                    break
                if result >= 80:
                    print('良好')
                    break
                if result >= 70:
                    print('中等')
                    break
                if result >= 60:
                    print('及格')
                    break
                if result < 60:
                    print('不及格')
                    break
            #print(result)
            break #跳出while这循环，如果不跳出从新到line14进行程序
judge()