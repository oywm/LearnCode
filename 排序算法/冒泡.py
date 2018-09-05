def mao_pao(list1):
    for j in range(len(list1)-1):
        for i in range(len(list1)-(j+1)):
            # if list1[i + 1]:
                if list1[i] > list1[i + 1]:
                    list1[i], list1[i + 1] = list1[i + 1], list1[i]

                else:
                    pass
            # else:
            #     break
        print(list1)


a = [9, 5, 97, 8, 3]
mao_pao(a)