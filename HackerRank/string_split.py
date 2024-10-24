# def split_and_join(line):
#     return line.replace(" ", "-")
#     # return line.split()
#
#
# if __name__ == '__main__':
#     line = input()
#     result = split_and_join(line)
#     print(result)
#

def print_full_name(first, last):
    first_part = 'Hello ' + first
    second_part = last + '! You just delved into python.'
    print(first_part, second_part)

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)
