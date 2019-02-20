def something(n):
    answer = 1

    for x in range(2, n+1):
        answer *= x

    return answer

print('Enter an integer: ')
a = input()

print(str(a) + '! = ' + str(something(int(a))))
