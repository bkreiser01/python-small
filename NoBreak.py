#Brandon

correctLetter = False

while correctLetter == False:
  
    #Asks the user to input a capital X
    letter = input("Please input the letter 'X' (Case Sensitive): ")

    #Checks the users input. If it is an X, the while loop stops.
    #If it is an x, the program reminds the user what Case Sensitive means.
    #Anything else and the program contines the while loop
    if letter == 'X':
        correctLetter = True
    elif letter == 'x':
        print('')
        print('============================================================================================')
        print('case-sen·si·tive')
        print('/ˌkāsˈsensədiv/')
        print('adjective [COMPUTING]')
        print('adjective: case-sensitive')
        print('')
        print('(of a program or function) differentiating between capital and lowercase letters')
        print(' <> (of input) treated differently depending on whether it is in capitals or lowercase text.')
        print('============================================================================================')
        print('')
    else:
        print('Really? Thats your answer? I said')

        
print('')
print("Congratz. You can obviously are a technical genius who is ahead of your time.")
