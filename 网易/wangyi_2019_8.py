count = 0


def num_of_pack():
    v = []
    n, w = map(int, input().split())
    v = list(map(int, input().split()))
    v.sort(reverse=True)
    if sum(v) < w:
        print(2**n)
    else:
        dfs(0, 0, v, w, n)
        print(count)


def dfs(s, i, v, w, n):
    global count
    if i < n:
        if s > w:
            return
        else:
            dfs(s, i+1, v, w, n)
            if s+v[i] <= w:
                count += 1
                dfs(s+v[i], i+1, v, w, n)


num_of_pack()