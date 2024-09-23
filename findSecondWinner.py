if __name__ == '__main__':
    n = int(input('Enter N value:'))
    arr = map(int, input().split())
    listArray = list(arr)
    winner = -float('inf')
    runner = -float('inf')
    if 2 <= n <=10:
        for num in listArray:
            # print('num:', num)
            if -100 <= num <= 100:
                if winner < num:
                    runner = winner
                    winner = num
                if runner < num < winner:
                    runner = num

    print(runner)



