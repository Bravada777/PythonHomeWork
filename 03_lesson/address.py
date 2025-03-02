class Address:
    def __init__(self, index, city, street, house, apartment):
        self.index = index
        self.city = city
        self.street = street
        self.house = house
        self.apartment = apartment

    def full_address(self):
        return (f'{self.index}, '
                f'{self.city}, '
                f'{self.street}, '
                f'{self.house} - {self.apartment}')
