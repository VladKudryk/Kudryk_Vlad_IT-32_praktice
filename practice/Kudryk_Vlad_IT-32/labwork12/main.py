
import kudryk_files

print("Список файлів:")
print(kudryk_files.list_files("."))

print("\nФайли, у назві яких є 'py':")
print(kudryk_files.find_files(".", "py"))

kudryk_files.create_file(
    "vlad_kudryk.txt",
    "Ім'я: Влад\nПрізвище: Кудрик\nГрупа: ІТ-32"
)

print("\nСтворено файл vlad_kudryk.txt")