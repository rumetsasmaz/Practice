def check_password(password):
    if len(password) >=  8:
        return True
    else:
        return False

user_password = input("Enter Your Password: ")

is_valid = check_password(user_password)

print(f"Is My Password Is Valid!: {is_valid}")