#Brandon Kreiser
#ConsecutiveDuplicates


#Loop the program.
while True:
    print('Would you like to look for Consecutive Doubles, or All Doubles?')

    correctInput = False
    while correctInput == False:
        option = int(input('Please insert a [1] for Consecutive or a [2] for All: '))
        if option == 1 or option == 2:
            correctInput = True

    print('')
    
    #Set the number list and ask the user how many numbers will be entered.
    numbers = [0]
    numAmount = int(input('How many integers will you enter?: '))

    #Ask the user to input numbers and add them to the numbers list.
    for x in range(numAmount):
        answer = int(input('What is integer #' + str(x + 1) + '?: '))
        numbers.insert(x, answer)

    print('')

    if option == 1:
    #Check for consecutive duplacates.
        for x in range(numAmount):
            if numbers[x] == numbers[x + 1]:
                print('Integers ' + str(x + 1) + ' and ' + str(x + 2) + ' are both ' + str(numbers[x + 1]) + '.')

    elif option == 2:
        #Check for any duplicate numbers and displays the proper message.
        for x in range(numAmount):
            for y in range(numAmount):
                if numbers[x] == numbers[y]:
                    if x != y and x < y:
                        print('Integers ' + str(x + 1) + ' and ' + str(y + 1) + ' are both ' + str(numbers[x]) + '.')

    print('')
