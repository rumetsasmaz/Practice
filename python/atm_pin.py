correct_pin = "3692"
balance = 1000
attempt = 3

while attempt > 0:
    user_input = (input("Enter Your Pin!: "))
    if user_input == correct_pin:
        print(f"Correct Pin Your Balance is {balance}")
        break
    else:
        attempt -= 1 
        print(f"Wrong Pin You Got {attempt} Left!:  ")


if attempt == 0:
    print("Card Blocked!!")