count = 0

letter = input("Enter a letter: ")
for l in "elephant":
    if l == letter:
        count = count + 1

print(count)




# Ask number from user
# Make number value = 1-10
# Make a number of attempts value 
# If user guesses number right then print "you win"
# If user guesses wrongthe print "you lose"

secret = 3
count = 5

guess = input("Enter a number 1-10: ")
while count > 0:
    guess = int(input("Enter a number 1-10: "))
    if guess == secret:
        print("You win!")
        break
    else:
       count -= 1
       if count == 0:
           print("You lose")

























