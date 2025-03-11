from address import Address
from mailing import Mailing


from_address = Address(
    index='125239',
    city='Москва',
    street='Коптевская',
    house='89',
    apartment='1')

to_address = Address(
    index='656064',
    city='Барнаул',
    street='Павловский тракт',
    house='77',
    apartment='2')


mailing = Mailing(
    to_address=to_address,
    from_address=from_address,
    cost=300,
    track='ABC12345')


print(mailing.print_mailing())
