#Brandon Kreiser
#Grade Calculator #1

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
        
    #Prints the A  messages 
    if finalGrade > 95 and finalGrade <= 100:
        print(str(finalGrade) + '%')
        print(Name +', your final score is an A+')
    if finalGrade == 95:
        print(str(finalGrade) + '%')
        print(Name +', your final score is an A')
    if finalGrade >= 90 and finalGrade < 95:
        print(str(finalGrade) + '%')
        print(Name +', your final score is an A-')
        
    #Prints the B messages
    if finalGrade < 90 and finalGrade > 85:
        print(str(finalGrade) + '%')
        print(Name +', your final score is an B+')
    if finalGrade == 85:
        print(str(finalGrade) + '%')
        print(Name +', your final score is an B')
    if finalGrade < 85 and finalGrade >=80:
        print(str(finalGrade) + '%')
        print(Name +', your final score is an B-')
        
    #Prints the C messages
    if finalGrade < 80 and finalGrade > 75:
        print(str(finalGrade) + '%')
        print(Name +', your final score is an C+')
    if finalGrade == 75:
        print(str(finalGrade) + '%')
        print(Name +', your final score is an C')
    if finalGrade < 75 and finalGrade >=70:
        print(str(finalGrade) + '%')
        print(Name +', your final score is an C-')
        
    #Prints the D messages
    if finalGrade < 70 and finalGrade > 65:
        print(str(finalGrade) + '%')
        print(Name +', your final score is an D+')
    if finalGrade == 65:
        print(str(finalGrade) + '%')
        print(Name +', your final score is an D')
    if finalGrade < 65 and finalGrade >=60:
        print(str(finalGrade) + '%')
        print(Name +', your final score is an D-')
        
    #Prints the fail message
    if finalGrade <60:
        #Repeats a dissapointed face 100 times
        for x in range(100):
            print('ಠ_ಠ')
        
        print(Name + '. Your final score was ' + str(finalGrade) + '%')
        print('That is lower than a D-')
        print('You failed.')
        
    print('')
    print('')
