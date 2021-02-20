import random;

number = random.randint(1,9)
chances = 5
guess = 0

print("Guessing Game(1-9)")

while number!=guess and chances > 0:
    guess = int(input("Enter Your Guess:"))
    chances = chances - 1
    if(number>guess):
        print("Your Guess was too low. Guess a number higher than ",str(guess))
    elif(number<guess):
        print("Your guess was too high. Guess a number lower than ",str(guess))
    else:
        print("Congratulations!You Won!!!")
    
if not chances < 0:
    print("You lose!!! The number is", str(number))   
      
    