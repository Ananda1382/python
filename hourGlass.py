import numpy as np
def hourGlass_MaxSum(array):
    max_sum = -float('inf')
    for i in range(1, len(array)-1):
        for j in range(1, len(array)-1):
            top = array[i-1][j-1] + array[i-1][j] + array[i-1][j+1]
            mid = array[i][j]
            bottom = array[i+1][j-1] + array[i+1][j] + array[i+1][j+1]
            hour_sum = top + mid + bottom

        if hour_sum > max_sum:
            max_sum = hour_sum

    return max_sum

matrix = np.random.randint(10, size=(6, 6))
print(matrix)
print(hourGlass_MaxSum(matrix))




