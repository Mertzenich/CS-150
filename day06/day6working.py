x = 5
print(x > 0 and x < 10)

n = 25
print(n % 2 == 0 or n % 3 == 0)

print(not n==25)

age = int(input('age: '))
if age >= 18:
    print('Welcome')
else:
    print(' not allowed')
    
length = float(input('Length: '))
width = float(input('Width: '))

if length == width:
    print('square')
    
else:
    print('not square')


passwd = 'password'
username = 'adam'

userPrompt = input('Username: ')
passwdPrompt = input('Password: ')

if userPrompt == username and passwdPrompt == passwd:
    print('Welcome, ', username)
else:
    print('Incorrect username or password')

Grade = 90

if Grade>=90:
    letter = 'A'
elif Grade>=80:
    letter = 'B'
elif Grade>=70:
    letter = 'C'
elif Grade>=60:
    letter = 'D'
elif Grade<=59:
    letter = 'F'

print(letter)