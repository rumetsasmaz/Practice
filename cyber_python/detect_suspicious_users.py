def detect_suspicious_users(user_list):
    suspicious_users = []
    for user in user_list:
        if user == "admin" or user == "root" or len(user) < 3:
            suspicious_users.append(user)
    return suspicious_users

users = ["admin", "berk", "root", "al", "developer", "x"]
print(detect_suspicious_users(users))