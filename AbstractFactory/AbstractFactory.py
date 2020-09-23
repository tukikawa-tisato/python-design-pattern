from abc import ABCMeta, abstractmethod


class Idol(metaclass=ABCMeta):

    def __init__(self, name, age):
        self._name = name
        self._age = age

    def greeting(self):
        print(self._name)

    @abstractmethod
    def live(self, music):
        pass


class Unit(metaclass=ABCMeta):

    def __init__(self, name):
        self._name = name
        self._idols = []

    @abstractmethod
    def live(self):
        pass

    def greeting(self):
        for idol in self._idols:
            idol.greeting()

    def add(self, idol: Idol):
        self._idols.append(idol)


class System(metaclass=ABCMeta):

    @classmethod
    def getSystem(cls, classname):
        system = None
        try:
            system = globals()[classname]()
        except:
            print('error')

        return system

    @abstractmethod
    def createIdol(self):
        pass

    @abstractmethod
    def createUnit(self):
        pass


class PriparaIdol(Idol):

    def __init__(self, name, age):
        super().__init__(name, age)

    def live(self, music, getCode=False):
        print('===================')
        print("コーデの数だけマイチケをスキャンしてね")
        self.greeting()
        print(music)
        if getCode:
            print('さぁ、神アイドルのステージへ。神アイドルチャレンジ、スイッチオン')
        print('===================')


class PriparaUnit(Unit):

    def __init__(self, name):
        super().__init__(name)

    def live(self, music, getCode=False):
        print('--------------------')
        print("コーデの数だけマイチケをスキャンしてね")
        self.greeting()
        print(music)
        if getCode:
            print('さぁ、神アイドルのステージへ。神アイドルチャレンジ、スイッチオン')
        print('--------------------')


class Pripara(System):

    def createIdol(self, name, age):
        return PriparaIdol(name, age)

    def createUnit(self, name):
        return PriparaUnit(name)


if __name__ == "__main__":
    meganee = Pripara.getSystem("Pripara")

    ralara = meganee.createIdol("真中らぁら", 12)
    mireli = meganee.createIdol("南みれぃ", 14)
    sofi = meganee.createIdol("北条そふぃ", 15)
    mireli.live("ぷりっとぱ～ふぇくと", True)

    solami_smile = meganee.createUnit("SoLaMi♡SMILE")
    solami_smile.add(ralara)
    solami_smile.add(mireli)
    solami_smile.add(sofi)
    solami_smile.live("トライアングルスター")
