# 暴力破解时间复杂度过高
# def num():
#     i = 1
#     count = 0
#     n, k = map(int, (input().split()))
#     while i <= n:
#         j = 1
#         while j <= n:
#             if i % j >= k:
#                 count += 1
#                 # print(count)
#             j += 1
#         i += 1
#     print(count)
#
#
# num()


def num_x_y():
    n, k = map(int, input().split())
    count = 0
    if k == 0:
        count = n * n
    else:
        for y in range(k + 1, n + 1):
            count += (n // y) * (y - k)
            if n % y >= k:
                count += (n % y - k + 1)
    print(count)


num_x_y()

