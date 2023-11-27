name=input("name?")
z=["Avishek","Anik","Jumar","Arko","Sourav","Arafat","Sudipto","Kowshik","Joy"]
password=["1234","5678",]
pas=input("pass?:   ")
while name not in z:
    name=input("Enter name")
while pas not in password :
    pas=input("Enter valid password:  ")
print("Thank you")



name = ''
while name != 'your name':
 print('Please type your name.')
 name = input()
print('Thank you!')



while True:
 print('Please type your name.')
v name = input()
w if name == 'your name':
x break
y print('Thank you!')



while True:
 print('Who are you?')
 name = input()
u if name != 'Joe':
v continue
 print('Hello, Joe. What is the password? (It is a fish.)')
w password = input()
 if password == 'swordfish':
x break
y print('Access granted.')

name = ''
while not name:
 print('Enter your name:')
 name = input()
print('How many guests will you have?')
numOfGuests = int(input())
if numOfGuests:
 print('Be sure to have enough room for all your guests.')w
print('Done')


print('My name is')
for i in range(5):
 print('Jimmy Five Times (' + str(i) + ')')
