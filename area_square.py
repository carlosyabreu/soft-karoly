
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
