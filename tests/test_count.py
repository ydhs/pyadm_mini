import unittest
import subprocess
import os
import sys

# Добавляем путь к корню проекта, чтобы main.py корректно импортировался
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


class TestCountParser(unittest.TestCase):

    def setUp(self):
        """Создаём тестовую папку с файлами"""
        self.test_folder = "test_folder"
        os.makedirs(self.test_folder, exist_ok=True)
        with open(os.path.join(self.test_folder, "file1.txt"), "w") as f:
            f.write("Тестовый файл 1")
        with open(os.path.join(self.test_folder, "file2.txt"), "w") as f:
            f.write("Тестовый файл 2")
        os.makedirs(os.path.join(self.test_folder, "sub_folder"), exist_ok=True)

    def test_count_command(self):
        """Проверка команды count"""
        result = subprocess.run(["python", "main.py", "count", self.test_folder], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0)
        self.assertTrue("Общее количество файлов" in result.stdout)
        self.assertTrue("Общее количество папок" in result.stdout)

    def tearDown(self):
        """Удаляем тестовый стенд."""
        for root, dirs, files in os.walk(self.test_folder, topdown=False):
            for name in files:
                os.remove(os.path.join(root, name))
            for name in dirs:
                os.rmdir(os.path.join(root, name))
        os.rmdir(self.test_folder)


if __name__ == "__main__":
    unittest.main()
