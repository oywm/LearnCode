# class Solution:
def digital_count(n, k):
    count = 0
    for i in range(n + 1):
        j = i
        if k == 0 and j == 0:
            count += 1
        while j > 0:
            r = j % 10
            if r == k:
                count += 1
            if j != 0:
                j = int(j / 10)
            else:
                break

    return count


print(digital_count(12, 2))
