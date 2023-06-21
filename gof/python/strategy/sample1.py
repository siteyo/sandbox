from abc import ABC, abstractmethod
from typing import Final


class Human:
    name: str
    height: int
    weight: int
    age: int

    def __init__(self, name: str, height: int, weight: int, age: int) -> None:
        self.name = name
        self.height = height
        self.weight = weight
        self.age = age


class BadComparator:
    __type: int
    COMPARE_AGE: Final[int] = 1
    COMPARE_HEIGHT: Final[int] = 2
    COMPARE_WEIGHT: Final[int] = 3

    def __init__(self, type) -> None:
        self.__type = type

    def compare(self, h1: Human, h2: Human) -> int:
        if type == self.COMPARE_AGE:
            if h1.age > h2.age:
                return 1
            elif h1.age == h2.age:
                return 0
            else:
                return -1
        elif type == self.COMPARE_HEIGHT:
            if h1.height > h2.height:
                return 1
            elif h1.height == h2.height:
                return 0
            else:
                return -1
        elif type == self.COMPARE_WEIGHT:
            if h1.weight > h2.weight:
                return 1
            elif h1.weight == h2.weight:
                return 0
            else:
                return -1
        else:
            raise Exception


def bad_compare() -> None:
    h1 = Human("taro", 170, 60, 20)
    h2 = Human("jiro", 180, 65, 18)

    bad_compare = BadComparator(1)
    bad_compare.compare(h1, h2)


# ------------------------------------------------------


class IComparator(ABC):
    @abstractmethod
    def compare(self, h1: Human, h2: Human) -> int:
        pass


class AgeComparator(IComparator):
    def compare(self, h1: Human, h2: Human) -> int:
        if h1.age > h2.age:
            return 1
        elif h1.age == h2.age:
            return 0
        else:
            return -1


class HeightComparator(IComparator):
    def compare(self, h1: Human, h2: Human) -> int:
        if h1.height > h2.height:
            return 1
        elif h1.height == h2.height:
            return 0
        else:
            return -1


class WeightComparator(IComparator):
    def compare(self, h1: Human, h2: Human) -> int:
        if h1.weight > h2.weight:
            return 1
        elif h1.weight == h2.weight:
            return 0
        else:
            return -1


class Context:
    __comparator: IComparator

    def __init__(self, comparator: IComparator) -> None:
        self.__comparator = comparator

    @property
    def comparator(self) -> IComparator:
        return self.__comparator

    def compare(self, h1: Human, h2: Human) -> int:
        return self.comparator.compare(h1, h2)


def strategy_compare() -> None:
    h1 = Human("taro", 170, 60, 20)
    h2 = Human("jiro", 180, 65, 18)

    comparator = AgeComparator()
    context = Context(comparator)

    print(context.compare(h1, h2))


if __name__ == "__main__":
    strategy_compare()
