import textwrap
if __name__ == '__main__':
    # n, m = int(input()), int(input())
    # design = []
    #
    # mid_row = n//2
    # mid_col = m//2 + 1
    # pattern = '.|.'
    # text = 'WELCOME'
    #
    # print(mid_row, mid_col)
    # if 5 < n < 101 and 15 < m < 303:
    #     for i in range(mid_row):
    #         top_line = '-'
    #         for j in range(m):
    #             if j == mid_col - 1:
    #                 top_line = top_line + pattern + (pattern * (i))
    #             else:
    #                 top_line = top_line + '-'
    #         # line_dash.center('.|.')
    #         design.append(top_line)
    #     for x in design:
    #         print(x.center(10))

    n = int(input().split(' ')[0])
    flag = False

    for i in range(n):
        if i == n // 2:
            print('WELCOME'.center(n * 3, '-'))
            flag = True
            continue
        if not flag:
            print(('.|.' * (i * 2 + 1)).center(n * 3, '-'))
        if flag:
            print(('.|.' * (((n - i) * 2) - 1)).center(n * 3, '-'))


