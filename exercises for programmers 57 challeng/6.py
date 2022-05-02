from datetime import date

age = int(input('what is your current age? '))
retire = int(input('at what age would you like to retire? '))

today = date.today()

print(f'you have {retire - age} years left until you can retire. \nIt´s {today.year}, so you can retire in {today.year + retire - age}')