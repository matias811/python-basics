

def check_password(username, password):
    hidden_password = '*' * len(password)
    print(f'Hey {username}, your password {hidden_password} is {len(password)} letters long.')


check_password("username", "password")