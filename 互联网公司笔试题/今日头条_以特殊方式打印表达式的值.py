# coding:utf-8
"""
输入字符串表达式，要求计算值，并将值用特殊方式打印
"""

a = [
    ['6', '6', '6', '6', '6'],
    ['.', '.', '.', '.', '6'],
    ['6', '6', '6', '6', '6'],
    ['6', '6', '6', '6', '6'],
    ['6', '.', '.', '.', '6'],
    ['6', '6', '6', '6', '6'],
    ['6', '6', '6', '6', '6'],
    ['6', '6', '6', '6', '6'],
    ['6', '6', '6', '6', '6'],
    ['6', '6', '6', '6', '6']
    ]

b = [
    ['6', '.', '.', '.', '6'],
    ['.', '.', '.', '.', '6'],
    ['.', '.', '.', '.', '6'],
    ['.', '.', '.', '.', '6'],
    ['6', '.', '.', '.', '6'],
    ['6', '.', '.', '.', '.'],
    ['6', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '6'],
    ['6', '.', '.', '.', '6'],
    ['6', '.', '.', '.', '6']
    ]

c = [
    ['6', '.', '.', '.', '6'],
    ['.', '.', '.', '.', '6'],
    ['6', '6', '6', '6', '6'],
    ['6', '6', '6', '6', '6'],
    ['6', '6', '6', '6', '6'],
    ['6', '6', '6', '6', '6'],
    ['6', '6', '6', '6', '6'],
    ['.', '.', '.', '.', '6'],
    ['6', '6', '6', '6', '6'],
    ['6', '6', '6', '6', '6']
    ]

d = [
    ['6', '.', '.', '.', '6'],
    ['.', '.', '.', '.', '6'],
    ['6', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '6'],
    ['.', '.', '.', '.', '6'],
    ['.', '.', '.', '.', '6'],
    ['6', '.', '.', '.', '6'],
    ['.', '.', '.', '.', '6'],
    ['6', '.', '.', '.', '6'],
    ['.', '.', '.', '.', '6'],
    ]

e = [
    ['6', '6', '6', '6', '6'],
    ['.', '.', '.', '.', '6'],
    ['6', '6', '6', '6', '6'],
    ['6', '6', '6', '6', '6'],
    ['.', '.', '.', '.', '6'],
    ['6', '6', '6', '6', '6'],
    ['6', '6', '6', '6', '6'],
    ['.', '.', '.', '.', '6'],
    ['6', '6', '6', '6', '6'],
    ['6', '6', '6', '6', '6'],
    ]


arr = [a, b, c, d, e]
space = ['.', '.']


def print_number(number):

    res = str(number)
    for i in range(5):
        for j in range(len(res)):
            k = int(res[j])
            print(*arr[i][k], end="", sep="")
            if j < len(res)-1:
                print(*space, end="", sep="")
        print()


if __name__ == '__main__':
    n = int(input())
    r = [eval(input()) for i in range(n)]
    for item in r:
        print_number(item)


