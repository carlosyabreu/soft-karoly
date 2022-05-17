
def login(user: str, passw: str) -> bool:
    is_authenticated = False

    if user == 'admin' and passw == '1234':
        is_authenticated = True

    return is_authenticated

username: str = input('Username: ')
password: str = input('Password: ')

is_authentication = False

for attempt in range(4):
    if login(username, password) == True:
        is_authentication = True
        print("Login successful")
        break
    else:
        print("Login failed, re-enter your credentials.")
        username: str = input('Username: ')
        password: str = input('Password: ')
