def format_text(text: str) -> str:
    """Возвращает строку с восстановленными заглавными буквами и делает заглавной букву 'i' при определенных условиях."""
    new_text = ''
    new_text += text[0].upper()
    i = 1
    while i < len(text) - 2:
        new_text += text[i]
        if text[i] == '.' or text[i] == '?' or text[i] == '!':
            new_text += ' '
            new_text += text[i+2].upper()
            i += 3
        else:
            if i == len(text) - 3:
                new_text += text[len(text)-2 : len(text)]
            i += 1
    i = 1
    while i < len(text) - 1:
        if (text[i-1] == " " and text[i] == "i"
                and (text[i+1] == " " or text[i+1] == "."
                     or text[i+1] == "!" or text[i+1] == "?"
                     or text[i+1] == "’")):
            new_text = new_text[0:i] + "I" + new_text[i+1 : len(new_text)]
        i += 1
    return new_text

text = input("Введите текст: ")
print(f'Новая версия: {format_text(text)}')
