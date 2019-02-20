#Brandon Kreiser
#Grade Calculator #2

#This tells the user the usage of the program
print('This is a program for students who want to calculate their final')
print('letter grade of multiple tests taken.')
print('')

#Asks the user for their name
Name = str(input('What is your name? '))

#Repeats the code
while False == False:
    
    #Asks for the total amount of tests taken
    #Then it gets each tests score
    #Lastly it calculates the average of all the tests and stores it in 'finalGrade'
    testNumber = int(input('How many tests have you been taken? '))
    count = str(0)
    finalGrade = str(0)
    while int(count) < testNumber:
        count = str(int(count) + 1)
        addingNum = int(input('What was the score of test #' + count + ' '))
        finalGrade = str(int(finalGrade) + addingNum)
    finalGrade = int(int(finalGrade)/testNumber)

    #All code beneath this line is used to print a message according to the final grade
    print('')
    print('')

    #Prints the over 100 message
    if finalGrade >100:
        print('Wow '+ Name + ', you managed to get above a 100%...')
        print('░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░')
        print('░░░░░░░░░░░░░░░░▄▄███▄▄▄░▄▄██▄░░░░░░░')
        print('░░░░░░░░░██▀███████████████▀▀▄█░░░░░░')
        print('░░░░░░░░█▀▄▀▀▄██████████████▄░░█░░░░░')
        print('░░░░░░░█▀▀░▄██████████████▄█▀░░▀▄░░░░')
        print('░░░░░▄▀░░░▀▀▄████████████████▄░░░█░░░')
        print('░░░░░▀░░░░▄███▀░░███▄████░████░░░░▀▄░')
        print('░░░▄▀░░░░▄████░░▀▀░▀░░░░░░██░▀▄░░░░▀▄')
        print('░▄▀░░░░░▄▀▀██▀░░░░░▄░░▀▄░░██░░░▀▄░░░░')
        print('█░░░░░█▀░░░██▄░░░░░▀▀█▀░░░█░░░░░░█░░░')
        print('█░░░▄▀░░░░░░██░░░░░▀██▀░░█▀▄░░░░░░▀▀▀')
        print('▀▀▀▀░▄▄▄▄▄▄▀▀░█░░░░░░░░░▄█░░█▀▀▀▀▀█░░')
        print('░░░░█░░░▀▀░░░░░░▀▄░░░▄▄██░░░█░░░░░▀▄░')
        print('░░░░█░░░░░░░░░░░░█▄▀▀▀▀▀█░░░█░░░░░░█░')
        print('░░░░▀░░░░░░░░░░░░░▀░░░░▀░░░░▀░░░░░░░░')
        print('░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░')
        print('...HOWWWWWWWW!?!?!?!?!?!')
        print('Congratz anyways though.')

    #Prints the fail message
    elif finalGrade < 60:
        for x in range(100):
            print('ಠ_ಠ')  
        print(Name + '. Your final score was ' + str(finalGrade) + '%')
        print('That is lower than a D-')
        print('You failed.')
        
    #Prints the D messages 
    elif finalGrade < 65:
        print(str(finalGrade) + '%')
        print(Name +', your final score is an D-')
    elif finalGrade == 65:
        print(str(finalGrade) + '%')
        print(Name +', your final score is an D')
    elif finalGrade < 70:
        print(str(finalGrade) + '%')
        print(Name +', your final score is an D+')
        
    #Prints the C messages
    elif finalGrade < 75:
        print(str(finalGrade) + '%')
        print(Name +', your final score is an C-')
    elif finalGrade == 75:
        print(str(finalGrade) + '%')
        print(Name +', your final score is an C')
    elif finalGrade < 80:
        print(str(finalGrade) + '%')
        print(Name +', your final score is an C+')
        
    #Prints the B messages
    elif finalGrade < 85:
        print(str(finalGrade) + '%')
        print(Name +', your final score is an B-')
    elif finalGrade == 55:
        print(str(finalGrade) + '%')
        print(Name +', your final score is and B')
    elif finalGrade < 90:
        print(str(finalGrade) + '%')
        print(Name +', your final score is an B+')
        
    #Prints the A messages
    elif finalGrade < 95:
        print(str(finalGrade) + '%')
        print(Name +', your final score is an A-')
    elif finalGrade == 95:
        print(str(finalGrade) + '%')
        print(Name +', your final score is an A')
    elif finalGrade < 100:
        print(str(finalGrade) + '%')
        print(Name +', your final score is an A+')
    elif finalGrade == 100:
        print(str(finalGrade) + '%')
        print(Name +', your final score is an A+')
     
    print('')
    print('')
