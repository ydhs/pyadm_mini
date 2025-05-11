import argparse
import shutil
import os


def copy_path(src, dest):
    """Копирует файл или папку из src в dest"""
    try:
        if os.path.isdir(src):
            shutil.copytree(src, dest)
            print(f"Папка успешно скопирована из {src} в {dest}")
        elif os.path.isfile(src):
            shutil.copy2(src, dest)
            print(f"Файл успешно скопирован из {src} в {dest}")
        else:
            print(f"Ошибка: {src} не является файлом или папкой.")
    except Exception as err:
        print(f"Ошибка при копировании: {err}")


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


def count_files_and_folders(path):
    """Подсчитывает количество файлов и папок"""
    try:
        if not os.path.exists(path):
            print(f"Ошибка: указанный путь {path} не существует.")
            return

        if not os.path.isdir(path):
            print(f"Ошибка: {path} не является папкой.")
            return

        file_count = 0
        folder_count = 0

        for root, dirs, files in os.walk(path):
            folder_count += len(dirs)
            file_count += len(files)

        print(f"Проанализировали папку: {path}")
        print(f"Общее количество файлов: {file_count}")
        print(f"Общее количество папок включая подпапки: {folder_count}")
    except Exception as err:
        print(f"Ошибка при подсчёте: {err}")


parser = argparse.ArgumentParser(description="Простая утилита системного администрирования")
subparsers = parser.add_subparsers(dest='command', required=True)

copy_parser = subparsers.add_parser("copy", help="Копирует файл или папку из src в dest")
copy_parser.add_argument("source", type=str, help="Путь источник")
copy_parser.add_argument("destination", type=str, help="Путь назначение")
copy_parser.set_defaults(func=copy_path)

delete_parser = subparsers.add_parser("delete", help="Удаляет файл или папку")
delete_parser.add_argument("path", type=str, help="Путь к файлу или папке для удаления")
delete_parser.set_defaults(func=delete_path)

count_parser = subparsers.add_parser("count", help="Подсчитывает количество файлов и папок в указанной директории")
count_parser.add_argument("path", type=str, help="Путь к директории для подсчёта")
count_parser.set_defaults(func=count_files_and_folders)

if __name__ == "__main__":
    argv = parser.parse_args()
    if argv.command == "copy":
        argv.func(argv.source, argv.destination)
    elif argv.command == "delete":
        argv.func(argv.path)
    elif argv.command == "count":
        argv.func(argv.path)
