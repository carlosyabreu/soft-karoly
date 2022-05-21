
# primes = list()
# print(primes)

# primes = []
# primes.append(2)
# primes.append(3)
# primes.append(5)
# primes.append(7)

# print(primes)

list = ["Michael", "Peter", "Carlos", "Joanna"]
# name = list[2]
# print(name)

def is_valid_index(index: int, list: list) -> bool:
    result = False

    if 0 <= index and index < len(list):
        result = True
    return result

index = 3
print(f"Index {index} is valid" if is_valid_index(index, list) else f"Index {index} is out of range")
