import flet as ft
import main
import io
import contextlib

def main_gui(page: ft.Page):
    # Настройки окна
    page.title = "pyadm_mini GUI (Flet)"
    page.padding = 20
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.window.width = 800
    page.window.height = 900
    page.window.resizable = False
    page.update()

    # Пикеры для операций
    picker_src = ft.FilePicker()
    picker_dst = ft.FilePicker()
    picker_del = ft.FilePicker()
    picker_cnt = ft.FilePicker()
    page.overlay.extend([picker_src, picker_dst, picker_del, picker_cnt])

    # Поле для вывода результатов
    output = ft.Text(value="", selectable=True)

    # Копирование
    page.add(ft.Text("Копирование файла", size=18, weight="bold"))
    src = ft.TextField(label="Путь источник", width=400)
    dst = ft.TextField(label="Путь назначение", width=400)

    def on_src_selected(e: ft.FilePickerResultEvent):
        if e.files:
            src.value = e.files[0].path
            page.update()
    picker_src.on_result = on_src_selected

    def on_dst_selected(e: ft.FilePickerResultEvent):
        if e.path:
            dst.value = e.path
            page.update()
    picker_dst.on_result = on_dst_selected

    btn_src = ft.ElevatedButton("Выбрать источник", on_click=lambda e: picker_src.pick_files())
    btn_dst = ft.ElevatedButton("Выбрать папку назначения", on_click=lambda e: picker_dst.get_directory_path())

    def do_copy(e):
        # перенаправляем вывод stdout в буфер
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            main.copy_path(src.value, dst.value)
        output.value = buf.getvalue()
        page.update()
    btn_copy = ft.ElevatedButton("Copy", on_click=do_copy)

    page.add(src, btn_src, dst, btn_dst, btn_copy, ft.Divider())

    # Удаление
    page.add(ft.Text("Удаляет файл или папку", size=18, weight="bold"))
    path_del = ft.TextField(label="Путь к файлу или папке для удаления", width=400)

    def on_del_selected(e: ft.FilePickerResultEvent):
        if e.files:
            path_del.value = e.files[0].path
            page.update()

    picker_del.on_result = on_del_selected

    btn_del = ft.ElevatedButton("Выбрать путь", on_click=lambda e: picker_del.pick_files())

    def do_delete(e):
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            main.delete_path(path_del.value)
        output.value = buf.getvalue()
        page.update()

    btn_delete = ft.ElevatedButton("Delete", on_click=do_delete)

    page.add(path_del, btn_del, btn_delete, ft.Divider())

    # Подсчёт
    page.add(ft.Text("Подсчитывает количество файлов и папок в указанной директории", size=18, weight="bold"))
    path_cnt = ft.TextField(label="Путь к директории для подсчёта", width=400)

    def on_cnt_selected(e: ft.FilePickerResultEvent):
        if e.path:
            path_cnt.value = e.path
            page.update()

    picker_cnt.on_result = on_cnt_selected

    btn_cnt = ft.ElevatedButton("Выбрать папку", on_click=lambda e: picker_cnt.get_directory_path())

    def do_count(e):
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            main.count_files_and_folders(path_cnt.value)
        output.value = buf.getvalue()
        page.update()

    btn_count = ft.ElevatedButton("Посчитать", on_click=do_count)

    page.add(path_cnt, btn_cnt, btn_count, ft.Divider())

    # Выводное поле
    page.add(ft.Text("Результат:"), output)


if __name__ == "__main__":
    ft.app(target=main_gui)
