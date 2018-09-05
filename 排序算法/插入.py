def insert(alist):
    n = len(alist)
    for i in range(1, n):
        for j in range(i):
            if alist[i-j] < alist[i-(j+1)]:
                alist[i - j], alist[i - (j + 1)] = alist[i - (j + 1)], alist[i - j]
            else:
                break
    print(alist)


alist = [54, 226, 93, 17, 77, 31, 44, 55, 20]
print(alist)
insert(alist)
