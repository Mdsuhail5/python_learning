class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other) -> bool:
        return self.x == other.x and self.y == other.y


point = Point(1, 2)
other = Point(1, 2)
print(point == other)
# if we do
print(point == other)
# it will return false as it will compare the addresses
# similarly for other comparision and other opertaion we have
# __lt__,__gt__ and many other magic methods
# basically magic methods is used to perform operations on the objects
