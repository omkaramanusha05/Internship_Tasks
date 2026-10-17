#Weighted Uniform Strings
https://www.hackerrank.com/challenges/weighted-uniform-string/problem


def weightedUniformStrings(s, queries):
    weights = set()
    prev = ''
    count = 0

    for ch in s:
        if ch == prev:
            count += 1
        else:
            prev = ch
            count = 1

        weight = (ord(ch) - ord('a') + 1) * count
        weights.add(weight)

    result = []

    for q in queries:
        if q in weights:
            result.append("Yes")
        else:
            result.append("No")

    return result


if __name__ == '__main__':
    s = input().strip()
    n = int(input().strip())

    queries = []

    for _ in range(n):
        queries.append(int(input().strip()))

    result = weightedUniformStrings(s, queries)

    print('\n'.join(result))
