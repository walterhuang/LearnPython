price = input('how much did you pay? ')
price = float(price)
if price >= 1.00:
    tax = .07
    print('Tax rate is: ' + str(tax))
else:
    tax = 0
    print('Tax rate is: ' + str(tax))

country = input('Enter the name of your home country: ')
if country.lower() == 'canada':
    print('So you must like hockey!')
else:
    print('You are not from Canada')

# Multiple Conditions
province = input('What is your province? ')

if province == 'Alberta' or province == 'Nunavut':
    tax = 0.05
elif province == 'Ontario':
    tax = 0.13
else:
    tax = 0.15

if province in('Alberta', 'Nunavut', 'Yukon'):
    tax = 0.05

if country.lower() == 'canada':
    if province in('Alberta', \
        'Nunavut', 'Yukon'):
        tax = 0.05
    elif province == 'Ontario':
        tax = 0.13
    else:
        tax = 0.15
else:
    tax = 0.0

print(tax)