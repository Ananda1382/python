def count_substring(string, sub_string):
    count = 0
    sub_len = len(sub_string)

    copyText = 'wecome'[::-1]

    print('copyText', copyText)

    # Iterate through the string
    for i in range(len(string) - sub_len + 1):
        # If the substring is found at the current position, increase the count
        if string[i:i + sub_len] == sub_string:
            count += 1

    return count

if __name__ == '__main__':
    # string = input().strip()
    # sub_string = input().strip()
    string = 'ABCDCDC'
    sub_string = 'CDC'
    count = count_substring(string, sub_string)
    print(count)