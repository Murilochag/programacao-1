people = int(input('how many people: '))
pizzas = int(input('how many pizzas do you have? '))

divPizza = (pizzas * 8) / people
leftover = pizzas % divPizza

print(f'{people} peaple with {pizzas} pizzas \nEach person gets {divPizza} pieces of pizza \nThere are {leftover}')