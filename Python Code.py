import calendar

# Получаем текущий месяц и год
now = calendar.datetime.datetime.now()
year = now.year
month = now.month

# Выводим заголовок календаря
print(calendar.month_name[month], year)
print("Mo Tu We Th Fr Sa Su")

# Выводим календарь на текущий месяц и год
cal = calendar.monthcalendar(year, month)
for week in cal:
    for day in week:
        if day == 0:
            print("  ", end="")
        else:
            print(f"{day:2d}", end=" ")
    print()