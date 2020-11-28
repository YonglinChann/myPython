while True:
    try:
        n = int(input('输入评委的人数：'))
        assert n > 2
        break
    except:
        print('必须输入大于2的整数!')

maxScore,minScore = 0,100
total = 0
print('\n')
for i in range(n):
    while True:
        try:
            score = float(input('请输入第{0}个评委的分数：'.format(i + 1)))
            assert 0 <= score <= 100
            break
        except:
            print('成绩必须是属于0～100的实数!')
    total += score
    if score > maxScore:
        maxScore = score
    if score < minScore:
        minScore = score
finalScore = round((total - maxScore - minScore) / (n - 2),2)
formatter = '\n去掉一个最高分：{0}\n去掉一个最低分：{1}\n\n最后的得分为：{2}'
print(formatter.format(maxScore,minScore,finalScore))