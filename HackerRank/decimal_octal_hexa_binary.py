def print_formatted(number):
    if 1 <= number <= 99:
        width = len(bin(number)[2:])
        for i in range(1, number+1):
            print(f"{i:d}".rjust(width), f"{i:o}".rjust(width), f"{i:x}".upper().rjust(width), f"{i:b}".rjust(width))
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)