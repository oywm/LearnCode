def direction():
    n = int(input())
    direct_turn = input()
    l_count = direct_turn.count('L')
    r_count = n - l_count
    if l_count > r_count:
        num = l_count - r_count
        num = num % 4
        if num == 0:
            print('N')
        elif num == 1:
            print('W')
        elif num == 2:
            print('S')
        else:
            print('E')
    elif l_count == r_count:
        print('N')
    else:
        num = r_count - l_count
        num = num % 4
        if num == 0:
            print('N')
        elif num == 1:
            print('E')
        elif num == 2:
            print('S')
        else:
            print('W')

direction()
