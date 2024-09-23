
if __name__ == '__main__':
    n = int(input('Enter N value: '))
    arr = map(int, input().split())
    listArray = list(arr)
    winner = -100
    runner = -100
    def swapTwoNumber(listArray, i, j):
        if listArray[i] > listArray[j]:
            temp = listArray[i]
            listArray[i] = listArray[j]
            listArray[j] = temp
    if n >=2 and n <=10:
        for i in range(len(listArray)):
            if -100 <= listArray[i] <= 100:
                for j in range(i+1, len(listArray)):
                    swapTwoNumber(listArray, i, j)
        print('Sorted listArray', listArray)
        for num in listArray:
            if num > winner:
                runner = winner
                winner = num
    print(runner)

