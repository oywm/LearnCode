def get_up():
    # 定了n个闹钟
    n = int(input())
    get_up_time = []
    # 将n个闹钟的转化为分钟存储在一个列表里
    for i in range(n):
        Hi, Mi = map(int, input().split())
        get_up_time.append(Hi * 60 + Mi)

    x = int(input())

    A, B = map(int, input().split())
    class_time = A * 60 + B

    get_up_time.sort(reverse=True)

    for i in range(n):
        if class_time - get_up_time[i] >= x:
            h = get_up_time[i] // 60
            m = get_up_time[i] % 60
            print(h, m)
            break


get_up()
