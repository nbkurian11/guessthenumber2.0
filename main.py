import random 

answer = 0
guess = 0


print("Think of a number between 1 and 10 and I will try to guess it.")



while answer < 1 or answer > 10: 
    answer = int(input("Enter your secret number here: "))
    if answer < 1:
        print("The secret number cannot be less than 1")
    if answer > 10:
        print("The secret number cannot be greater than 10")


print("Now I will guess your number!")




while True:
    computer_guess = random.randrange(1,10)
    numGuess = str(computer_guess)
    check = str(input("Is this your number:" + numGuess + "? [yes or no]"))
    guess += 1
    print("Number of guesses: ", guess)
    if check.lower() == "yes":
        print("Yes! I am correct.")
        break



