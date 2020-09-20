from abc import ABCMeta, abstractmethod


class Idol(metaclass=ABCMeta):

    @abstractmethod
    def greetingOnStage():
        pass


class Girl():

    def __init__(self, greeting):
        self._greeting = greeting

    def greeting(self):
        print(self._greeting)


class IdolAdapter(Idol):

    def __init__(self, girl):
        self._girl = girl

    def greetingOnStage(self):
        self._girl.greeting()


if __name__ == "__main__":
    ralara = IdolAdapter(Girl("真中らぁら小学6年生!"))
    ralara.greetingOnStage()
