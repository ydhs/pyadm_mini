import unittest
import subprocess
import os


class TestCopyParser(unittest.TestCase):

    def setUp(self):
        """Создаём тестовый файл"""
        self.test_file = "test_file.txt"
        self.copy_file = "copied_test_file.txt"
        with open(self.test_file, "w") as f:
            f.write("Тест")

    def test_copy_command(self):
        """Проверка команды copy и факт копирования файла"""
        result = subprocess.run(["python", "main.py", "copy", self.test_file, self.copy_file], capture_output=True,
                                text=True)
        self.assertEqual(result.returncode, 0)
        self.assertTrue(os.path.exists(self.copy_file))  # Проверяем, что файл был скопирован

    def tearDown(self):
        """Удаляем тестовый стенд."""
        os.remove(self.test_file)
        os.remove(self.copy_file)


if __name__ == "__main__":
    unittest.main()
