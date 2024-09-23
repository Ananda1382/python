# 1. get the length of given two strings
# 2. compare both strings length are greater than 0 otherwise return
# 3. compare substring length is greater than the original string then return
# 4. if substring length is less than main string then
# Traverse main string char by char with starting substring charAt(0)
# if found match take 2nd char and comare with original string from the last found position and continue

def count_substring(string, sub_string):
    mainStringLength = len(string)
    subStringLength = len(sub_string)
    found = 0
    if mainStringLength <= 0 or subStringLength <= 0:
        print("SubString Length and Main String Length are less than Zero")
        return 0

    if subStringLength > mainStringLength:
        print("SubString Length is greater than the main String Length")
        return 0

    if subStringLength < mainStringLength:
            for j in range(mainStringLength):
                if j > mainStringLength - subStringLength:
                    break
                if sub_string[0] == string[j]:
                    for k in range(subStringLength):
                        if sub_string[k] == string[j]:
                            if k == subStringLength - 1:
                                found += 1
                            k += 1
                            j += 1
                            continue
                        else:
                            break
            else:
                print('No match')
            return found
    else:
        return 0
print('Total Found count1 ==', count_substring('ABCDCDC', 'CDC'))
print('Total Found count2 ==', count_substring('ABCDCDC', 'C'))
print('Total Found count3 ==', count_substring('C', 'aaaaaC'))
print('Total Found count4 ==', count_substring('Anand', 'Vijay'))
print('Total Found count5 ==', count_substring('Anand', 'Anc'))
