import secrets
import string

print('Do you need a username or password?')
user_or_pass = str(input('Type username or password: '))
if user_or_pass == 'username':
    print('What are your initials?')
    initials = str(input('Type your three initials: '))
    n = int(input('How many random digits do you want after your initals: '))

    def user_name(initials, n):
        return str(initials) + ''.join([secrets.choice(string.digits) for _ in range(n)])

    print(user_name(initials, n))

elif user_or_pass == 'password':
    print('How many characters does your password need to be?')
    n = int(input('# of characters: '))

    def generate(n): 
        return "".join([secrets.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(n)])

    print('Your password is: ' + str(generate(n)))

else:
    print('Error!')