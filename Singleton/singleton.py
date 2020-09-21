class Goddess():
    __goddess = None

    def __init__(self):
        if Goddess.__goddess != None:
            raise Exception("女神はすでに存在しています")
        else:
            Goddess.__goddess = self

    @classmethod
    def getGoddess(cls):
        if cls.__goddess is None:
            Goddess()
        return Goddess.__goddess

    def challengeGodIdol(self):
        print('さぁ、神アイドルのステージへ。神アイドルチャレンジ、スイッチオン')


if __name__ == "__main__":
    july = Goddess.getGoddess()
    janys = Goddess.getGoddess()
    july.challengeGodIdol()
    if july == janys:
        print('二人は女神です。')
