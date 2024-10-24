if __name__ == '__main__':
    n = int(input().split()[0])
    pattern = '.|.'
    text = 'WELCOME'
    if 5 < n < 101 and 15 < n*3 < 303:
        for i in range(n):
            if i < n//2:
                top = (pattern * ((i*2)+1)).center(n*3, '-')
                print(top)
            if i == n//2:
                mid = text.center(n*3, '-')
                print(mid)
            if i > n//2:
                bottom = (pattern * (((n-i)*2)-1)).center(n*3, '-')
                print(bottom)