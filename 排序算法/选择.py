def choice(alist):
    for i in range(len(alist) - 1):
        min1 = i
        for j in range(i + 1, len(alist)):
            if alist[min1] > alist[j]:
                min1 = j

        alist[i], alist[min1] = alist[min1], alist[i]

        print(alist)


alist = [54, 26, 93, 93, 17, 77, 31, 44, 55, 20]
print(alist)
choice(alist)
