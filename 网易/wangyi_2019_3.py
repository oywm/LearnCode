def light():
    l = []
    test_num = int(input())
    for i in range(test_num):
        count = 0
        pos = 0
        road_distance = int(input())
        road_struct = input()
        while pos <= road_distance - 1:
            if road_struct[pos] == 'X':
                pos += 1
            else:
                count += 1
                pos += 3
        l.append(count)
    for i in l:
        print(i)

light()

