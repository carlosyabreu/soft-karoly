
def login(user: str, passw: str) -> bool:
    is_authenticated = False

    if user == 'admin' and passw == '1234':
        is_authenticated = True

    return is_authenticated

username: str = input('Username: ')
password: str = input('Password: ')

while login(username, password) == False:
    print('Login failed, re-enter your credentials: ')
    username: str = input('Username: ')
    password: str = input('Password: ')

print('Login successful')
