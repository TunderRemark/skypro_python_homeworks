from smartphone import Smartphone

catalog = []

phone_1 = Smartphone('Apple', 'IPhone 10', '+79008005252')
phone_2 = Smartphone('Apple', 'IPhone 14', '+79014258968')
phone_3 = Smartphone('Samsung', 'Galaxy A3', '+79807453245')
phone_4 = Smartphone('Huawei', 'P50', '+79948254125')
phone_5 = Smartphone('Honor', '50 Pro', '+79998883232')

catalog.append(phone_1)
catalog.append(phone_2)
catalog.append(phone_3)
catalog.append(phone_4)
catalog.append(phone_5)

for phone in catalog:
    print(f'{phone.brand} - {phone.model}. {phone.number}')
