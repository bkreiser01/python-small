#Brandon Kreiser
#ConsecutiveDuplicates


#loops the program
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
    loops = 0
    while loops < numAmount:
        answer = int(input('What is integer #' + str(loops + 1) + '?: '))
        numbers.insert(loops, answer)
        loops = loops + 1

    print('')

    if option == 1:
    #Check for consecutive duplacates.
        loopA = 0
        while loopA < numAmount:
            if numbers[loopA] == numbers[loopA + 1]:
                print('Integers ' + str(loopA + 1) + ' and ' + str(loopA + 2) + ' are both ' + str(numbers[loopA + 1]))
            loopA = loopA + 1

    elif option == 2:
        #Check for any duplicate numbers and displays the proper message.
        loopA = 0
        while loopA < numAmount:
            loopB = loopA
            while loopB < numAmount:
                if numbers[loopA] == numbers[loopB]:
                    if loopA != loopB:
                        print('Integers ' + str(loopA + 1) + ' and ' + str(loopB + 1) + ' are both ' + str(numbers[loopA]))
                loopB = loopB + 1
            loopA = loopA + 1

    print('')
