
list = []
def insert(element, position):
    list.insert(position, element)

def print_the_list():
    print(list)

def remove(element):
    for item in list:
        if item == element:
            list.remove(element)
            break

def append(element):
    list.append(element)

def sort():
    list.sort()

def pop():
    list.pop()

def reverse():
    list.reverse()


if __name__ == '__main__':
    N = int(input())
    for i in range(N):
        inputValue = input().split()
        commandName = inputValue[0]

        if commandName == 'append':
            value = int(inputValue[1])
            append(value)
        elif commandName == 'insert':
            position = int(inputValue[1])
            if inputValue[2].isdigit():
                value = int(inputValue[2])
                insert(value, position)
            else:
                value = str(inputValue[2])
                test=''
                print('value', value)
                for char in value:
                    if char.isdigit():
                         test+=char
                print('test', test)
                insert(int(test), position)

        elif commandName == 'remove':
            value = int(inputValue[1])
            remove(value)
        elif commandName == 'sort':
            sort()
        elif commandName == 'pop':
            pop()
        elif commandName == 'reverse':
            reverse()
        elif commandName == 'print':
            print_the_list()
        else:
            break
