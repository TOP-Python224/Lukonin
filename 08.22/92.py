def get_day_and_month(year: int, day_count: int) -> int:
    """Функция принимает на вход год и порядковый номер дня, и возвращает дату."""
    d_in_m = [31, 28+is_leap, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    for i in range(len(d_in_m)):
        if day_count <= d_in_m[i]:
            return f"{day_count}-{i + 1}-{year}"
        day_count -= d_in_m[i]


year, day_count = list(map(int, input('Год и день в году: ').split()))
is_leap = year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

if get_day_and_month(year, day_count) is None:
    raise ValueError("введено неверное количество дней")
else:
    print(f'Дата: {get_day_and_month(year, day_count)}\n')

expiration_date = int(input("Введите срок годности/гарантии: "))

if 0 < day_count <= 365 + is_leap:
    end_day = day_count + expiration_date

    if is_leap and end_day > 366:
        year += end_day // 366
        day_count = end_day - 366
    elif not is_leap and end_day > 365:
        year += end_day // 365
        day_count = end_day - 365
    print(f"Дата окончания годности/гарантии: {get_day_and_month(year, day_count)}")