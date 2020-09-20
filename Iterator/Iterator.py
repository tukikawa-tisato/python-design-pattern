from abc import ABCMeta, abstractmethod


class Iterator(metaclass=ABCMeta):

    @abstractmethod
    def hasNext() -> bool:
        pass

    @abstractmethod
    def next() -> object:
        pass

    @abstractmethod
    def previous() -> object:
        pass


class Aggregate(metaclass=ABCMeta):

    @abstractmethod
    def iterator() -> Iterator:
        pass


class Idol():

    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name


class Pripara(Aggregate):

    def __init__(self):
        self.__idols = []

    def getIdolAt(self, index: int) -> Idol:
        return self.__idols[index]

    def appendIdol(self, idol: Idol):
        self.__idols.append(idol)

    def getLength(self) -> int:
        return len(self.__idols)

    def iterator(self) -> Iterator:
        return PriparaIterator(self)


class PriparaIterator(Iterator):

    def __init__(self, pripara: Pripara):
        self.__pripara = pripara
        self.__index = 0

    def hasNext(self) -> bool:
        if (self.__index < self.__pripara.getLength()):
            return True
        else:
            return False

    def next(self) -> object:
        idol = self.__pripara.getIdolAt(self.__index)
        self.__index += 1
        return idol


if __name__ == "__main__":
    pripara = Pripara()
    pripara.appendIdol(Idol("真中らぁら"))
    pripara.appendIdol(Idol("南みれぃ"))
    pripara.appendIdol(Idol("北条そふぃ"))
    iterator = pripara.iterator()
    while(iterator.hasNext()):
        idol = iterator.next()
        print(idol.name)
