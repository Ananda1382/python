for n in range(2,10):
    for m in range(2,n):
        if (n%m == 0):
            print(n, 'is not a prime')
            break
    else:
       print(n, 'is a prime')