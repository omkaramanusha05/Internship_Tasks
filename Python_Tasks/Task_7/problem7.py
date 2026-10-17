#Alphabet Rangoli
#https://www.hackerrank.com/challenges/alphabet-rangoli/problem

    import string
    alpha = string.ascii_lowercase

    lines = []
    for i in range(size):
        row = "-".join(alpha[size-1:i:-1] + alpha[i:size])
        lines.append(row.center(4 * size - 3, "-"))

    print("\n".join(lines[::-1] + lines[1:]))
