# get name from keyboard
first_name = "WALTER" #input('First name:')
last_name = "Huang" #input('Last name:')

print('Hello,'+' '+first_name.capitalize()+' '+last_name.upper())

print('Hello, {} {}'.format(first_name, last_name))
print('Hello, {0} {1}'.format(first_name, last_name))

# only available in Python 3
output = f'Hello, {first_name} {last_name}'
print(output)
