def calculate_age(birth_year):
    from datetime import datetime
    current_year = datetime.now().year
    age = current_year - birth_year
    return age

print(calculate_age(int(input("What is your birth year? "))))