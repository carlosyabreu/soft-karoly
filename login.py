
# business logic
def login(user: str, passw: str) -> bool:
    is_authenticated = False

    if user == 'admin' and passw == '1234':
        is_authenticated = True

    return is_authenticated

username: str = input('Username: ')
password: str = input('Password: ')

attempt = 0
max_attempts = 3
is_authentication = False

while login(username, password) == False:
    attempt += 1
    if attempt > max_attempts: break

    print('Login failed, re-enter your credentials: ')
    username: str = input('Username: ')
    password: str = input('Password: ')
else:
    is_authentication = True
    print('Login successful')

if not is_authentication:
    print('Your login has been temporarily locked.')
