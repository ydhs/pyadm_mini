import argparse
import shutil
import os

def copy_file(src, dest):
    """Копирует файл из src в dest."""
    try:
        shutil.copy2(src, dest)
        print(f"Файл успешно скопирован из {src} в {dest}")
    except Exception as err:
        print(f"Ошибка при копировании файла: {err}")

def delete_path(path):
    """Удаляет файл или папку."""
    try:
        if os.path.isfile(path):
            os.remove(path)
            print(f"Файл {path} удалён.")
        elif os.path.isdir(path):
            shutil.rmtree(path)
            print(f"Папка {path} удалена.")
        else:
            print(f"Ошибка: {path} не является файлом или папкой.")
    except Exception as err:
        print(f"Ошибка при удалении: {err}")

parser = argparse.ArgumentParser(description="Простая утилита системного администрирования")
# первый аргумент, команда что сделать
subparsers = parser.add_subparsers(dest='command', required=True)

# парсер копирования
copy_parser = subparsers.add_parser("copy", help="Копирует файл из src в dest (только файл, не папку)")
copy_parser.add_argument("source", type=str, help="Путь источник")
copy_parser.add_argument("destination", type=str, help="Путь назначение")
copy_parser.set_defaults(func=copy_file)

# парсер удаления
delete_parser = subparsers.add_parser("delete", help="Удаляет файл или папку")
delete_parser.add_argument("path", type=str, help="Путь к файлу или папке для удаления")
delete_parser.set_defaults(func=delete_path)

argv = parser.parse_args()
if argv.command == "copy":
    argv.func(argv.source, argv.destination)
elif argv.command == "delete":
    argv.func(argv.path)
