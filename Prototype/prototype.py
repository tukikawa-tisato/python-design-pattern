from abc import ABCMeta, abstractmethod
import copy


class Idol(metaclass=ABCMeta):

    @abstractmethod
    def greeting():
        pass

    @abstractmethod
    def clone(self):
        pass


class Meganee():

    def __init__(self):
        self.__idols = {}

    def registerIdol(self, name: str, idol: Idol):
        self.__idols[name] = idol

    def createIdol(self, name: str) -> Idol:
        return self.__idols[name]


class Pripara(Idol):

    def __init__(self, name: str):
        self._name = name

    def greeting(self, greeting: str):
        print(greeting)

    def live(self, music: str):
        print(music)

    def clone(self):
        return copy.copy(self)


class Prichan(Idol):

    def __init__(self, name):
        self._name = name

    def greeting(self, greeting: str):
        print(greeting)

    def streaming(self, subject):
        print(subject)

    def clone(self):
        return copy.copy(self)


if __name__ == "__main__":
    meganee = Meganee()

    ralara = Pripara("真中らぁら")
    mirai = Prichan("桃山みらい")

    meganee.registerIdol("真中らぁら", ralara)
    meganee.registerIdol("桃山みらい", mirai)

    idol_ralara = meganee.createIdol("真中らぁら")
    idol_ralara.greeting("かしこまっ！")
    idol_mirai = meganee.createIdol("桃山みらい")
    idol_mirai.greeting("そうなんだ")
