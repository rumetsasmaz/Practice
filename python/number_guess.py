secret_number = 8

while True: 
    user_guess = int(input("Your Guess: "))
   
    if user_guess == secret_number:
        print(f"Correct Number Is {secret_number} ")
        break
    else:
        print("Your Guess Is Wrong Try Again")
