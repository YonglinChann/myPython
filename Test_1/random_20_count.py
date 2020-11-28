import random
a = [random.randint(0,100) for i in range(20)]
#print(a)
b = a[0:10]
b.sort()
a[0:10] = b
b = a[10:20]
b.sort(reverse = True)
a[10:20] = b
print(a)