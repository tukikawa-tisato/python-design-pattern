from abc import ABCMeta, abstractmethod


class Ticket(metaclass=ABCMeta):

    def __init__(self, idol):
        self._idol = idol

    @abstractmethod
    def use(self):
        pass

    @property
    def idol(self):
        return self._idol


class Machine(metaclass=ABCMeta):

    def create(self, idol: str) -> Ticket:
        idol = self.createIdol(idol)
        return idol

    @abstractmethod
    def createIdol(self, idol: str) -> Ticket:
        pass


class TomoTicket(Ticket):

    def __init__(self, idol):
        super().__init__(idol)
        print(f'{idol}さんがトモチケを登録しました。')

    def use(self):
        print(f'{self.idol}さんのトモチケをスキャンするよ。')


class MyTicket(Ticket):

    def __init__(self, idol):
        super().__init__(idol)
        print(f'{idol}さんがマイチケを登録しました。')

    def use(self):
        print(f'{self.idol}さんのマイチケをスキャンするよ。')


class TicketMachine(Machine):
    def __init__(self):
        self._members = []

    def createIdol(self, ticket: Ticket):
        self._members.append(ticket)
        return ticket

    @property
    def members(self):
        return self._members


if __name__ == "__main__":
    ticketMachine = TicketMachine()
    ralara = ticketMachine.create(MyTicket('真中らぁら'))
    mireli = ticketMachine.create(MyTicket('南みれぃ'))
    sofi = ticketMachine.create(MyTicket('北条そふぃ'))
    sofi.use()

    reona = ticketMachine.create(TomoTicket('レオナ・ウェスト'))
    reona.use()
