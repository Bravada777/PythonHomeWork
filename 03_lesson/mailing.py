class Mailing:
    def __init__(self, to_address, from_address, cost, track):
        self.to_address = to_address
        self.from_address = from_address
        self.cost = cost
        self.track = track

    def print_mailing(self):
        return (f'Отправление {self.track} из '
                f'{self.from_address.full_address()} в '
                f'{self.to_address.full_address()}. '
                f'Стоимость {self.cost} рублей.')
