from smartphone import Smartphone


catalog = [
    Smartphone("Nokia", "3310", "+79991112233"),
    Smartphone("Motorola", "RAZR V3", "+79991112244"),
    Smartphone("Sony Ericsson", "K750i", "+79991112255"),
    Smartphone("BlackBerry", "Curve 8900", "+79991112266"),
    Smartphone("Samsung", "SGH-E250", "+79991112277")
]


for smartphone in catalog:
    print(smartphone.print_details())
