from abc import ABCMeta, abstractmethod


class Live(metaclass=ABCMeta):

    @abstractmethod
    def introduction():
        pass

    @abstractmethod
    def music():
        pass

    @abstractmethod
    def code():
        pass


class Meganee():

    def __init__(self, live: Live):
        self._live = live

    def startLive(self, getCode: bool = False):
        self._live.introduction()
        self._live.music()
        if getCode:
            self._live.code()


class PriparaLive(Live):

    def __init__(self, music):
        self._music = music

    def introduction(self):
        print("コーデの数だけマイチケをスキャンしてね")

    def music(self):
        print(self._music)

    def code(self):
        print('さぁ、神アイドルのステージへ。神アイドルチャレンジ、スイッチオン')


class PrichanLive(Live):

    def __init__(self, music):
        self._music = music

    def introduction(self):
        print("ジュエルパクト、スタンバイ")

    def music(self):
        print(self._music)

    def code(self):
        print('ジュエルチャンス、スタートだもん!')


if __name__ == "__main__":
    pripara_live = PriparaLive('Make it!')
    meganee = Meganee(pripara_live)
    meganee.startLive()

    prichan_live = PrichanLive('SUPER CUTIE SUPER GIRL')
    meganee = Meganee(prichan_live)
    meganee.startLive(True)
