length = float(input("what is the length of the room in feet? "))
width = float(input("what is the width of the room in feet? "))

squarefeet = length * width
squaremeters = squarefeet * 0.09290304

print(f'you entered dimensions of {length} feet by {width} feet.\nThe area is\n{squarefeet} square feet\n{squaremeters :.3f} in meters')