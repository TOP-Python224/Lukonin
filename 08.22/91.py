def ordinalDate(day: int, month: int, year: int) -> int:
    """Преобразовывает дату из календарного формата в порядковый.

    :param day: календарный день
    :param month: календарный месяц
    :param year: календарный год
    :returns: порядковый номер дня в году
    """
    year_is_leap = year % 400 == 0 or year % 4 == 0 and year % 100 != 0
    month_days = [31, 28+year_is_leap, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    md = 0
    for i in range(month-1):
        md += month_days[i]
    return md + day

day, month, year = map(int, input('День, месяц, год: ').split())
print(f'Порядковый номер дня в году: {ordinalDate(day, month, year)}\n')
