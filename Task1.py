days_count = int(input("введите количество дней \n"))
people_count = int(input("введите сколько людей \n "))

days_count = abs(days_count)
day_price = 428

if days_count <= 6:  # если количество дней меньше или равно 6
    day_price = int(450)  # тогда цена 450
elif ((days_count % 31 == 0) or (days_count % 30 == 0)) and (days_count > 30):
    day_price = 1

print(day_price)
