def leaf_year(year):
    return year and year % 4 == 0 and year % 100 != 0 or year % 400 == 0
    # leap = False
    # if year != 0 and year > 0:
    #     if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    #         leap = True
    #         # return leap
    #     else:
    #         # leap = False
    #         print(year, 'is not a multiple of 4 hence it`s not a leap year')
    #         # return leap
    #
    # else:
    #     # leap = False
    #     print("Year is either 0 or not greater than 0")
    #
    # return leap

user_input = int(input("Please enter a year: "))
print('Is', user_input, 'a leaf year?', leaf_year(user_input))