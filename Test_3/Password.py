from string import digits,ascii_lowercase,ascii_uppercase
s = str(input('请输入一个字符串：'))
def check(pwd):
    if not isinstance(pwd,str) or len(pwd) < 6:
        return 'not suitable for password'
    d = {1:'很弱', 2:'弱', 3:'中等', 4:'强'}
    r = [False] * 4
    for ch in pwd:
        if not r[0] and ch in digits:
            r[0] = True
        elif not r[1] and ch in ascii_lowercase:
            r[1] = True
        elif not r[2] and ch in ascii_uppercase:
            r[2] = True
        elif not r[3] and ch in ',.!;?<>':
            r[3] = True
    return d.get(r.count(True),'error')
print('\n您的密码强度为：',check(s))