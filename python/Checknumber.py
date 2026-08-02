def check_number(num):
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:   
        return "Zero"

print(check_number(int(input("Enter a number: "))))