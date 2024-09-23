def swap_scores(result, i, j):
    if result[i][1] > result[j][1]:
        temp = result[i][0], result[i][1]
        result[i][0], result[i][1] = result[j][0],result[j][1]
        result[j][0], result[j][1] = temp
        return result

if __name__ == '__main__':
    result = []
    for n in range (int(input('Enter N value:'))):
        # if 2 <= n <= 5:
        name = input()
        score = float(input())
        element = [name, score]
        result.append(element)

        for i in range(len(result)):
            for j in range(i+1, len(result)):
                swap_scores(result, i, j)
    print('Sorted result:', result)
    lowest = result[0][1]
    secondLowest = result[0][1]
    for i in range(1,len(result)):
        if lowest < result[i][1] > secondLowest:
            secondLowest = result[i][1]
            break
    secondLowestList =[]
    for i in range(len(result)):
        if secondLowest == result[i][1]:
            secondLowestList.append(result[i])
            for k in range(len(secondLowestList)):
                for l in range(k + 1, len(secondLowestList)):
                    if secondLowestList[k][0] > secondLowestList[l][0]:
                        temp = secondLowestList[k][0]
                        secondLowestList[k][0] = secondLowestList[l][0]
                        secondLowestList[l][0] = temp
    print('secondLowestList:', secondLowestList)
    for i in range(len(secondLowestList)):
        print(secondLowestList[i][0])


