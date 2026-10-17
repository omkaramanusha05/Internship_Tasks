#Sherlock and the Valid String
#https://www.hackerrank.com/challenges/sherlock-and-valid-string/problem

from collections import Counter

def isValid(s):
    freq = Counter(s)
    count = Counter(freq.values())

    if len(count) == 1:
        return "YES"

    if len(count) == 2:
        (f1, c1), (f2, c2) = count.items()

        if (f1 == 1 and c1 == 1) or (f2 == 1 and c2 == 1):
            return "YES"

        if abs(f1 - f2) == 1:
            if f1 > f2 and c1 == 1:
                return "YES"
            if f2 > f1 and c2 == 1:
                return "YES"

    return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
