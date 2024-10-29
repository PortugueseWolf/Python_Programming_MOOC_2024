def create_tuple(x: int, y: int, z: int) -> tuple:
    list = [x, y, z]
    list.sort()
    tuple = (list[0], list[2], sum(list))
    return tuple

if __name__ == "__main__":
    print(create_tuple(5, 3, -1))