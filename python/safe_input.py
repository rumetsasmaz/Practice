try:
    number = int(input("Enter a number: "))
    print(f"You entered: {number}")
except ValueError:
    print("Please enter a valid integer.")