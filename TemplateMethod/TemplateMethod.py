from abc import ABCMeta, abstractmethod


class AbstractIdol(metaclass=ABCMeta):

    @abstractmethod
    def greeting():
        pass

    @abstractmethod
    def music():
        pass

    @abstractmethod
    def getCode():
        pass

    def live(self):
        self.greeting()
        self.music()
        self.getCode()


class Pripara(AbstractIdol):

    def __init__(self, music):
        self.__music = music

    def greeting(self):
        print('コーデの数だけマイチケをスキャンしてね')

    def music(self):
        print(f'{self.__music}!!!')

    def getCode(self):
        print('さぁ、神アイドルのステージへ。神アイドルチャレンジ、スイッチオン')


class Prichan(AbstractIdol):

    def __init__(self, music):
        self.__music = music

    def greeting(self):
        print('ジュエルパクト、スタンバイ')

    def music(self):
        print(f'{self.__music}!')

    def getCode(self):
        print('ジュエルチャンス、スタートだもん!')


if __name__ == "__main__":
    mireli = Pripara("ぷりっとぱ〜ふぇくと")
    mireli.live()

    ann_emo = Prichan("ツヨキ!ツインテールズ")
    ann_emo.live()
