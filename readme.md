# Утилита для копирования, удаления и анализа файлов

Это простая утилита для системного администрирования, позволяющая делать распространённые операции с помощью Python.

## Возможности

- Копирование файлов и папок
- Удаление файлов и папок
- Подсчёт количества файлов и папок в указанной директории
- Использование из командной строки

## Требования

- Python 3.*

## Установка

Установка не требуется. Просто склонируйте репозиторий и запустите скрипт.

```sh
git clone https://github.com/ydhs/pyadm_mini.git
cd pyadm_mini
```

## Использование

### Копирование файла или папки

```sh
python main.py copy <путь_источник> <путь_назначение>
```

Примеры:

```sh
python main.py copy C:\source.txt D:\destination.txt
python main.py copy C:\source_folder D:\destination_folder
```

### Удаление файла или папки

```sh
python main.py delete <путь>
```

Примеры:

```sh
python main.py delete C:\file.txt
python main.py delete C:\folder_to_delete
```

### Подсчёт количества файлов и папок

```sh
python main.py count <путь>
```

Примеры:

```sh
python main.py count C:\some_folder
```

