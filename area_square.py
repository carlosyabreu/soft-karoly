
def calculate_square_area(side):
    return side * side

area = calculate_square_area(5)
print(area)

def build_ferrari(color: str = 'red') -> str:
    print(f"Built a {color} Ferrari")

build_ferrari('blue')

# Prompt the user to select a shape and wait
selection = input("""\t'C' - Circle
\t'S' - Square
\t'R' - Rectangle
""")

def calculate_rhombus_area(p: float, q: float) -> float:
    return p * q / 2

a = calculate_rhombus_area(2, 3)
print(f"The area of rhombus is {a}")
