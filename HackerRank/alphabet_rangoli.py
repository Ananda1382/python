if __name__ == '__main__':
    n = int(input())
    cols = ((n-1)*(n-1)) + 1
    rows = ((n-1)*2) + 1
    center_row = rows // 2
    alpha_map = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f'}
    mid = '-'+alpha_map.get(1)+'-'
    top = (alpha_map.get(n)).center(cols, '-')
    print(top)
    for i in range(1,rows):
        if i < rows // 2:
            top  = (top.strip('-').center(3,'-') + (alpha_map.get(n-i)).center(2, '-') + top.strip('-').ljust(2,'-')).center(cols,'-')

            print(top)
        if i  == rows // 2:
            for j in range(2,n+1):
                mid = alpha_map.get(j).rjust(2,"-") + mid + alpha_map.get(j).ljust(2, "-")
            print(mid)

