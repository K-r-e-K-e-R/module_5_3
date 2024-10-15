class House:
    def __init__(self, name, floors):
        self.name = name
        self.floors = floors

    def __str__(self):
        # Возвращаеем строку с названием и количеством этажей
        return f"Название: {self.name}, кол-во этажей: {self.floors}"

    def __eq__(self, other):
        if isinstance(other, House):
            return self.floors == other.floors
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, House):
            return self.floors > other.floors
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, House):
            return self.floors >= other.floors
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, House):
            return self.floors < other.floors
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, House):
            return self.floors <= other.floors
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, House):
            return self.floors != other.floors
        return NotImplemented

    def __add__(self, floors):
        if isinstance(floors, int):
            total_floors = self.floors + floors
            return House(f"{self.name}", total_floors)
        return NotImplemented

    def __iadd__(self, floors):
        if isinstance(floors, int):
            self.floors += floors
            return self
        return NotImplemented

    def __radd__(self, floors):
        return self + floors


home1 = House("ЖК Эльбрус", 10)
home2 = House("ЖК Альбатрос", 16)

print(home1)
print(home2)

print(home1 == home2)  # __eq__

home1 = home1 + 10  # __add__
print(home1)
print(home1 == home2)

home1 += 10  # __iadd__
print(home1)

home2 = 14 + home2  # __radd__
print(home2)

print(home1 > home2)  # __gt__
print(home1 >= home2)  # __ge__
print(home1 < home2)  # __lt__
print(home1 <= home2)  # __le__
print(home1 != home2)  # __ne__
