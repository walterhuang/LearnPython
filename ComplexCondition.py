gpa = float(input('What was your Grade Point Average? '))
#lowest_grade = float(input('What was your lowest grade? '))
lowest_grade = input('What was your lowest grade? ')
lowest_grade = float(lowest_grade)

if gpa >= .85:
    if lowest_grade >= .70:
        print('You made the honour roll')

if gpa >= .85 and lowest_grade >= .70:
    print('You made the honour egg roll')

if gpa >= .85 and lowest_grade >= .70:
    honour_roll = True
else:
    honour_roll = False

if honour_roll:
    print('You made the honour pork roll')