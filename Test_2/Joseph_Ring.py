def demo(lst,k):

    t_lst = lst[:]
    print('\n')
    while len(t_lst) > 1:
        print(t_lst)
        for i in range(k - 1):
            t_lst.append(t_lst.pop(0))
        t_lst.pop(0)
    return t_lst[0]

lst = list(range(1,11))

print('\n',demo(lst,3),'\n')