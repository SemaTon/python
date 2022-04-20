enter_seconds = int(input("Введите время в секундах: "))
second = enter_seconds % 60
minutes = (enter_seconds // 60) % 60
hour = (enter_seconds // 60**2) % 60
day = (enter_seconds // 60**2 * 24) % 24
month = (enter_seconds // 60**2 * 24 * 30) % 30
print(month, 'mon', day, 'd', hour, 'h', minutes, 'min', second, 's')