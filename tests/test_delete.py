import unittest
import subprocess
import os
import shutil


class TestDeleteParser(unittest.TestCase):

    def setUp(self):
        """Создаём тестовый файл и папку"""
        self.test_file = "test_file.txt"
        self.test_folder = "test_folder"
        with open(self.test_file, "w") as f:
            f.write("Тест")
        os.makedirs(self.test_folder, exist_ok=True)

    def test_delete_file_command(self):
        """Проверка команды delete и факта удаления файла"""
        result = subprocess.run(["python", "main.py", "delete", self.test_file], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0)
        self.assertFalse(os.path.exists(self.test_file))  # Проверяем, что файл был удалён

    def test_delete_folder_command(self):
        """Проверка команды delete и факта удаления папки"""
        result = subprocess.run(["python", "main.py", "delete", self.test_folder], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0)
        self.assertFalse(os.path.exists(self.test_folder))  # Проверяем, что папка была удалена

    def tearDown(self):
        """Удаляем тестовый стенд"""
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
        if os.path.exists(self.test_folder):
            shutil.rmtree(self.test_folder)


if __name__ == "__main__":
    unittest.main()
