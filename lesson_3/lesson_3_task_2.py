from smartphone import Smartphone
catalog = []

catalog.append(Smartphone('Samsung', 'Samsung A32', '+79604637924'))
catalog.append(Smartphone('Honor', 'Honor 8S', '+79176430075'))
catalog.append(Smartphone('Fly', 'Fly 432', '+79870421695'))
catalog.append(Smartphone('Infinix', 'Infinix gt 20 Pro', '+79610450063'))

for phone in catalog:
    print(f'{phone.brand} - {phone.model}. {phone.number}')