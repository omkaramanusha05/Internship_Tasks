#Symmetric Difference
#https://www.hackerrank.com/challenges/symmetric-difference/problem


m = int(input())
set_m = set(map(int, input().split()))

n = int(input())
set_n = set(map(int, input().split()))

result = set_m.symmetric_difference(set_n)

for i in sorted(result):
    print(i)
