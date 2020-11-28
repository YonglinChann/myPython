import string
def kaisa(s,k):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    before = string.ascii_letters
    after = lower[k:] + lower[:k] + upper[k:] + upper[:k]
    table = ''.maketrans(before,after)
    return s.translate(table)
s = input('请输入一个字符串：')
k = int(input('请输入一个整数密钥：'))
print('\n加密后的结果为：',kaisa(s,k))