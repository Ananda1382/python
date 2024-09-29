def cartesian_product(aValue, bValue):
    catesian_product = []
    for i in range(len(aValue)):
        for j in range(len(bValue)):
            product = aValue[i], bValue[j]
            catesian_product.append(product)
    return catesian_product


if __name__ == '__main__':
    n = int(input())
    a_val = []
    b_val = []
    for i in range(n):
        value_list = (input().split())
        if i == 0:
            a_val = [int(num) for num in value_list]
        if i == 1:
            b_val = [int(num) for num in value_list]
    print(cartesian_product(a_val, b_val))
