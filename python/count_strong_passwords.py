def count_strong_passwords(passwords):
    valid_count = 0
    for password in passwords:
        if len(password) >= 8:
            valid_count += 1 

    return valid_count



pass_list = ["123", "secret147852", "admin" , "super_secure_pass"]

print(count_strong_passwords(pass_list))

