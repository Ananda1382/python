def find_keyWord():
    keyWord = 'ACHAND27'
    found = False
    try:
        with open('C:\VirtualDSA\VDSA_Ref1.txt') as file:   
            for line in file:
                if keyWord in line:
                    print(line)
                    found = True
                    break
    except:
        print('File not found')
        return       

    if not found:
        print('Keyword not found')
    
def add_text():
    additionKeyWord = "Hello"
    with open('C:\VirtualDSA\VDSA_Ref.txt', 'a') as file:   
        file.write('\n' + additionKeyWord + '\n')
    
def main():
    choice = input('do you want to find(F) or Add(A)\n')
    if (choice == 'F'):
        find_keyWord()
    elif (choice == 'A' ):
        add_text();

main()


