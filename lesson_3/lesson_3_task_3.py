from address import Address
from mailing import Mailing

to_address = Address('150054', 'Ярославль', 'Щапова', '12', '10')
from_address = Address('142111', 'Подольск', 'Трубная', '28', '57')

mailing = Mailing(to_address, from_address, 1000, '45681')

print(f'Отправление {mailing.track} из {mailing.from_address.index}, '
    f'{mailing.from_address.city}, {mailing.from_address.street}, '
    f'{mailing.from_address.house} - {mailing.from_address.apartment}'
    f' в {mailing.to_address.index}, {mailing.to_address.city}, '
    f'{mailing.to_address.street}, '
    f'{mailing.to_address.house} - {mailing.to_address.apartment}.'
    f'Стоимость {mailing.cost} рублей.')
