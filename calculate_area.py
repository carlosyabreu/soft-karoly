
area = 0

def calculate_square_area(side: int) -> int:
    global area
    area = side * side
    print(f"The area is {area}")

calculate_square_area(4)

print(f"Write out the value of area {area}")
