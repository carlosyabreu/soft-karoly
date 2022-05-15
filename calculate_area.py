

def calculate_square_area(side: float) -> float:
    return side * side

def calculate_rectangle_area(length: float, width: float) -> float:
    return length * width

def calculate_circle_area(radius: float) -> float:
    pi : int = 3.14
    return pi * radius ** 2

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


def calculate_area(selection: str):
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

    return area

def getShapeArea(tag: str):
    shape: str = 'Unknow'
    if tag == 'S':
        shape = 'Square'
    elif tag == 'R':
        shape = 'Rectangle'
    elif tag == 'C':
        shape = 'Circle'
    
    return shape

area = calculate_area(selection)

print(f"The area of the {getShapeArea(selection)}: {area}")

