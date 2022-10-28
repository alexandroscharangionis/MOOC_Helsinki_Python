def create_tuple(x: int, y: int, z: int):
    numbers = [x, y, z]
    tup = (min(numbers), max(numbers), x + y + z)
    return tup
