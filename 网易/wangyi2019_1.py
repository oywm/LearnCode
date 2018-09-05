'''
输入描述:
每个输入包含一个测试用例。
每个测试用例的第一行包含两个正整数，分别表示工作的数量N(N<=100000)和小伙伴的数量M(M<=100000)。
接下来的N行每行包含两个正整数，分别表示该项工作的难度Di(Di<=1000000000)和报酬Pi(Pi<=1000000000)。
接下来的一行包含M个正整数，分别表示M个小伙伴的能力值Ai(Ai<=1000000000)。
保证不存在两项工作的报酬相同。

输出描述:
对于每个小伙伴，在单独的一行输出一个正整数表示他能得到的最高报酬。一个工作可以被多个人选择。

输入例子1:
3 3
1 100
10 1000
1000000000 1001
9 10 1000000000

输出例子1:
100
1000
1001
'''
import sys
import bisect
task = {} # [] 列表 {} 字典
lines = sys.stdin.readlines()
n, m = map(int, lines[0].strip().split()) # strip() 移除字符头尾指定的字符，split()按照指定的字符分割字符串 由于有空行，这句可以不写
for line in lines[1:-1]:
    if not line.strip().split(): # 存在空行，你能信...
        continue
    # print(line)
    a, b = map(int, line.strip().split()) # 把第二行到倒数第二行转换成int型赋值给a, b
    task[a] = max(task.get(a, 0), b) # 如果相同难度的工作，将报酬最大的放入字典对应的位置上
arr = sorted(task.keys()) # 将字典中按工作难度排序 默认为升序 arr只赋了工作难度的值
for i in range(1, len(arr)):  # 如果工作难度大，报酬少，则把工作难度低报酬多的报酬赋值给工作难度大的报酬
    if task[arr[i]] < task[arr[i -1]]:
        task[arr[i]] = task[arr[i -1]]
skills = map(int, lines[-1].strip().split())
for skill in skills:
    if skill in task:
        print(task[skill])
    else:
        ind = bisect.bisect(arr, skill)
        if ind == 0:
            print(0)
        else:
            print(task[arr[ind - 1]])

