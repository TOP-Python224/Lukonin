from pathlib import Path

directory = Path(input('path: '))

def show_files(dir: str) -> tuple[str]:
    """Выводит список файлов в принятом каталоге."""
    result = ()
    for elem in dir.iterdir():
        if Path.is_file(elem):
            result += (elem.name, )
    print(result)
    return result

show_files(directory)