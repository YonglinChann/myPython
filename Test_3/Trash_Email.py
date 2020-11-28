def check(text,rate = 0.2):
    characters = '【】*-/\\'
    num = sum(map(
        lambda ch: text.count(ch),
        characters
    ))
    if num / len(text) > rate:
        return '垃圾邮件'
    return '正常邮件'

text = input('请输入邮件内容：')
print('\n过滤系数在0.2条件下，该邮件为',check(text))
print('\n过滤系数在0.5条件下，该邮件为',check(text,0.5))