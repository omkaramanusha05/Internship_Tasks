#Set .add()
#https://www.hackerrank.com/challenges/py-set-add/problem

n = int(input())
s = set()

for _ in range(n):
    s.add(input().strip())

print(len(s))
