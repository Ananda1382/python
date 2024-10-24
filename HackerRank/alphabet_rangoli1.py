def print_rangoli(size):
    if (size == 1):
        print('a')
        return
    rangoli = ""

    middle = createLine(size,0,1 ,0)

    width = len(middle)

    for x in range(size - 1, 0, -1):
        rangoli += f"{createLine(size, x, x + 1, width)}\n"
    rangoli += f"{middle}\n"
    for a in range(1, size, 1):
        rangoli += f"{createLine(size, a, a + 1, width)}\n"
    print(rangoli)

def createLine(n, centerLetterIndex, startLetterIndex, width):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    pattern = ""
    for x in range(startLetterIndex, n):
        if x == n - 1:
            pattern += alphabet[x]
        else:
            pattern += alphabet[x] + "-"
    return f"{pattern[::-1]}-{alphabet[centerLetterIndex]}-{pattern}".center(width, "-")


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
