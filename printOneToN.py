if __name__ == '__main__':
    n = int(input('Enter your Input for N:'))
    expectedOutput = 0
    if n >= 1 and n <= 150:
        for element in range(1,n+1):
            digitLength = len(str(element))
            expectedOutput = expectedOutput * (10 ** digitLength) + element
    print(expectedOutput)