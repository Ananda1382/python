def find_Acronym():
    acronym = input('Enter the acronym you want to find\n')
    found = False
    try:
        with open('C:\VirtualDSA\VDSA_Ref.txt') as file:
            for line in file:
                if acronym in line:
                    print(line)
                    found = True
                    break
    except:
        print('File not found')

    if not found:
        print('Entered Acronym not found')

def add_Acronym():
    acronym = input('Enter the acronym you want to add\n')
    with open('C:\VirtualDSA\VDSA_Ref.txt', 'a') as file:
        file.write('\n' + acronym + '\n')

def main():
    add_Acronym()

main()

