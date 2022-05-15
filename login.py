
def login(user: str, passw: str) -> bool:
    is_authenticated = False

    if user == 'admin' and passw == '1234':
        is_authenticated = True

    return is_authenticated

username: str = input('Username: ')
password: str = input('Password: ')

logged_in = login(username, password)

if logged_in == True:
    message = 'Login succesful'
elif logged_in == False:
    message = 'Login failed, check your credential'

print(message)
