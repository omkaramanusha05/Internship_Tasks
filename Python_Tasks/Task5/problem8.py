#Set .add()
#https://www.hackerrank.com/challenges/py-set-add/problem

n = int(input())
s = set()

for i in range(n):
    name = input()
    s.add(name)

print(len(s))
