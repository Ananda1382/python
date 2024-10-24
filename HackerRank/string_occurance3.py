# def find_substring_withnoBuiltinFunctionsUsed(mainString, subString):
#     count = 0
#     match = ''
#     j = 0
#     for i in range(len(mainString)+1):
#         if count > 0:
#             i = i - 1
#         if mainString[i] == subString[j] and j < len(subString):
#             match = match + mainString[i]
#             j += 1
#         if match == subString:
#             count += 1
#             match = ''
#             j = 0
#
#     return count

def find_substring_withBuiltinFunctionsUsed(mainString, subString):
    count = 0
    for i in range(len(mainString) - len(subString) + 1):
        if mainString[i:i+len(subString)] == subString:
            count += 1
    return count


if __name__ == '__main__':
    mainString = 'ABCDCDC'
    subString = 'CDC'
    # print(find_substring(mainString, subString))
    print(find_substring_withBuiltinFunctionsUsed(mainString, subString))