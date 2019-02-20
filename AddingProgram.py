#Brandon Kreiser
#Calculating Program

#Describes the program to the user
print('''
This is a basic calculator program.
It will crash if you enter any letter.
''')

while True: #Repeats the program infinately
    
    #Asks for the first 2 numbers
    num1 = int(input('Please enter the first number: '))
    num2 = int(input('Please enter the second number: '))
    
    #Tells the user what input corrisponds to which operator
    print('======================')
    print('To Add       : Enter 1')
    print('To Subtract  : Enter 2')
    print('To Multiply  : Enter 3')
    print('To Divide    : Enter 4')
    print('======================')

    #Does the operation according the to number inputed, and will
    #tell the user to enter a proper number if an improper one is inputed.
    op_num = False
    while op_num == False:
        op = int(input('Operator Number : '))
        print('========================')
        if op == 1:
            op_num = True
            print('The sum of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(num1+num2) + '.')
        elif op == 2:
            op_num = True
            print('The difference of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(num1-num2) + '.')
        elif op == 3:
            op_num = True
            print('The product of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(num1*num2) + '.')
        elif op == 4:
            op_num = True
            print('The quotient of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(num1/num2) + '.')
        else:
            print('Be sure to enter an operator number')
        print('========================')
