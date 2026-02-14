from address import Address
from mailing import Mailing

to_address = Address('450064', 'Ufa', 'Mira', '3', '56')
from_address = Address('123456', 'Moskow', 'Pushkina', '5', '2')

mailing = Mailing(to_address, from_address, 500, 'TRACK234')

print(f"Отправление {mailing.track} из {from_address.index}, {from_address.city}, {from_address.street}, {from_address.house} - {from_address.apartment} в {to_address.index}, {to_address.city}, {to_address.street}, {to_address.house} - {to_address.apartment}. Стоимость {mailing.cost} рублей.")
