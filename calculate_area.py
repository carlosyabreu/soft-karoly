

def calculate_square_area(side: float) -> float:
    return side * side

def calculate_rectangle_area(length: float, width: float) -> float:
    return length * width

def calculate_circle_area(radius: float) -> float:
    return math.pi * radius ** 2

print("""
   --------------------------------------
   Area Calculator
   -------------------------------------- 
   Select a shape:
""")

selection = input("""\t'S' - Square
\t'R' - Rectangle
\t'C' - Circle
""")

area = 0

if selection == 'S':
    side = input("Enter the side: ")
    area = calculate_square_area(float(side))
elif selection == 'R':
    lenght = input("Enter the length: ")
    width = input("Enter the width: ")
    area = calculate_rectangle_area(float(lenght), float(width))
elif selection == 'C':
    radius = input("Enter the radious: ")
    area = calculate_circle_area(float(radius))
else:
    print("Invalid selection. Choose 'S', 'R', 'C'")

print(f"Write out the area: {area}")
