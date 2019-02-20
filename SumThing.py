#Brandon Kreiser


#Generate the sequence.
def sequenceGenerator(start,end,difference):
   sequence = []
   for index in range(start,end + 1,difference):
      sequence.append(index)
   return sequence

#Find the sum of the sequence. 
def add(numbers):
   total = 0
   for index in range(len(numbers)):
      total = total + numbers[index]
   return total

#Ask the user for information about the squence.
start = int(input('What number will be at the start of this sequence? '))
end = int(input('What number will be at the end of this seqence? '))
difference = int(input('What will be the common differance between the numbers? '))

#Generate a sequence, and add the total.
numbers = sequenceGenerator(start,end,difference)
total = add(numbers)

#Print the results.
print()
print(str(total) +' is the sum of the sequence ' + str(numbers))
print()
   
