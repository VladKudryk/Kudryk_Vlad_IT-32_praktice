import  os

def list_files(directory):
    """Повертає список файлів у вказаній директорії.
    Args:
        directory: Шлях до директорії.
    Returns:
        Список назв файлів.
    """
    files = []
    for name in os.listdir(directory):
        path = os.path.join(directory, name)
        if os.path.isfile(path):
            files.append(name)
    return files

def find_files(directory, substring):
    """Знаходить файли, у назвах яких є вказаний підрядок.
    Args:
        directory: Шлях до директорії.
        substring: Підрядок для пошуку.
    Returns:
        Список знайдених файлів.
    """
    files = list_files(directory)
    found = []
    for name in files:
        if substring in name:
            found.append(name)
    return found

def create_file(path, text):
    """Створює файл і записує в нього текст.
    Args:
        path: Шлях до файлу.
        text: Текст для запису.
    Returns:
        Шлях до створеного файлу.
    """
    with open(path, "w", encoding="utf-8") as file:
        file.write(text)
    return path

if __name__ == "__main__":
    print("Список файлів:", list_files("."))
    print("Пошук файлів:", find_files(".", "py"))
    create_file("test_file.txt", "Перевірка модуля")
    print("Створено файл test_file.txt")