#Set .symmetric_difference() Operation
#https://www.hackerrank.com/challenges/py-set-symmetric-difference-operation/problem


if __name__ == '__main__':
    m = int(input())
    a = set(map(int, input().split()))

    n = int(input())
    b = set(map(int, input().split()))

    result = a.symmetric_difference(b)

    print(len(result))
