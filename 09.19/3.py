from pathlib import Path

directory = Path('./# TestFolder')
keywords_file = Path('./# keywords.txt')
result = []

def get_txt_files(directory: Path) -> list[str]:
    """Выводит список текстовых файлов в принятом каталоге."""
    txt_files = []
    for elem in directory.iterdir():
        if Path.is_file(elem) and elem.match('*.txt'):
            txt_files += [directory / elem.name]
    return txt_files

def get_keywords(keywords_file: Path) -> list[str]:
    """Выводит список ключевых слов из принятого файла."""
    with open(keywords_file, encoding = 'utf-8') as file:
        keywords = []
        for line in file:
            for word in line.split():
                keywords += [word]
    return keywords

def find_keywords(directory: Path, keywords_file: Path, n = 0) -> list:
    """Выводит список словарей, содержащих данные о текстовых файлах, в которых найдены ключевые слова.
    :param directory: каталог с текстовыми файлами
    :param keywords_file: файл с ключевыми словами
    :param n: глубина сохраняемого контекста, n строк перед и n строк после строки, содержащей ключевое слово, по умолчанию 0.
    """
    for txt_file in get_txt_files(directory):
        with open(txt_file, encoding = 'utf-8') as file:
            text = file.readlines()
        for keyword in get_keywords(keywords_file):
            line_index = -1
            for line in text:
                line_index += 1
                for word in line.split():
                    if word.startswith(keyword):
                        start_pos = line_index - n
                        stop_pos = line_index + n + 1
                        if start_pos < 0: start_pos = 0
                        result.append({'filename': file.name,
                                    'line_number': line_index,
                                    'keyword': keyword,
                                    'context': n,
                                    'text': text[start_pos: stop_pos]})
    return result

print(find_keywords(directory, keywords_file, n=2))
