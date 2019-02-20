#Brandon Kreiser

#Displays a prompt, then asks for input
print("Please enter the letter 'X'.")
userLetter = input()

#While loop will continue until the user inputs X.
while userLetter is not 'X':
    #Displays prompts, then asks for input
    print("That's not what I asked for!")
    print("Please enter the letter 'X'.")
    userLetter = input()

#Displays prompt
print("Very good!  You clearly have superior keyboarding skills.")
