# def isAlphaNumeric(string):
#     return string.isalnum()
#
# def isAlpha(string):
#     return string.isalpha() or any(char.isalpha() for char in string)
#
# def isdigit(string):
#     return string.isdigit() or any(char.isdigit() for char in string)
#
# def islower(string):
#     return string.islower() or any(char.islower() for char in string)
#
# def isUpper(string):
#     return string.isupper() or any(char.isupper() for char in string)
#
# # import re
# if __name__ == '__main__':
#     s = input()
#     # updated_string = re.sub(r'[\']', '', s)
#     # print(updated_string)
#     if 0 < len(s) < 1000:
#         # print(isAlphaNumeric(s))
#         # print(isAlpha(s))
#         # print(isdigit(s))
#         # print(islower(s))
#         # print(isUpper(s))
#
#         check = [False]*5
#         for i in s:
#             if i.isalnum():
#                 check[0] = True
#             if i.isalpha():
#                 check[1] = True
#             if i.isdigit():
#                 check[2] = True
#             if i.islower():
#                 check[3] = True
#             if i.isupper():
#                 check[4] = True
#
#         for x in check:
#             print(x)
#

if __name__ == '__main__':
    s = input()
    validate = [False, False, False, False, False]
    for i in s:
        if i.isalnum():
            validate[0] = True
        if i.isalpha():
            validate[1] = True
        if i.isdigit():
            validate[2] = True
        if i.islower():
            validate[3] = True
        if i.isupper():
            validate[4] = True
    for x in validate:
        print(x)