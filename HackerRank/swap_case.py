def swap_case(toSwap):
    return toSwap.swapcase()

if __name__ == '__main__':
    stringToSwap = str(input())
    if 0 < len(stringToSwap) <= 1000:
        print(swap_case(stringToSwap))