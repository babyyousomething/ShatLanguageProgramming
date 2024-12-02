import sys
import time  # Для работы с временем
import random  # Для модуля random
from colorama import Fore, Style


class ShatInterpreter:
    def __init__(self):
        pass

    def interpret_file(self, file_path):
        """Читает и интерпретирует файл с расширением .shat."""
        if not file_path.endswith(".shat"):
            raise ValueError("Ожидался файл с расширением .shat")

        try:
            with open(file_path, "r", encoding="utf-8") as f:
                for line in f:
                    self.interpret_command(line.strip())
        except FileNotFoundError:
            print(f"Файл {file_path} не найден.")

    def interpret_command(self, command):
        """Интерпретирует одну строку кода."""
        if not command:
            return  # Пропуск пустых строк

        if command.startswith("печатать "):
            content = command[len("печатать "):]
            print(content)

        elif command.startswith("повторить "):
            parts = command.split(maxsplit=2)
            if len(parts) != 3:
                print(Fore.RED + "Ошибка: неверный синтаксис команды 'повторить'." + Style.RESET_ALL)
                return
            _, count, text = parts
            try:
                count = int(count)
                for _ in range(count):
                    print(text)
            except ValueError:
                print(Fore.RED + "Ошибка: параметр количества повторений должен быть числом." + Style.RESET_ALL)

        elif command.startswith("подождать "):
            parts = command.split()
            if len(parts) != 2:
                print(Fore.RED + "Ошибка: неверный синтаксис команды 'подождать'." + Style.RESET_ALL)
                return
            _, wait_time = parts
            try:
                wait_time = int(wait_time)
                time.sleep(wait_time)  # Пауза на заданное количество секунд
            except ValueError:
                print(Fore.RED + "Ошибка: время ожидания должно быть числом." + Style.RESET_ALL)

        elif command.startswith("случайное_число "):
            parts = command.split()
            if len(parts) != 3:
                print(Fore.RED + "Ошибка: неверный синтаксис команды 'случайное_число'." + Style.RESET_ALL)
                return
            _, start, end = parts
            try:
                start, end = int(start), int(end)
                print(random.randint(start, end))
            except ValueError:
                print(Fore.RED + "Ошибка: границы диапазона должны быть числами." + Style.RESET_ALL)

        elif command.startswith("случайный_выбор "):
            parts = command.split(maxsplit=1)
            if len(parts) != 2:
                print(Fore.RED + "Ошибка: неверный синтаксис команды 'случайный_выбор'." + Style.RESET_ALL)
                return
            _, elements = parts
            try:
                elements = eval(elements)  # Преобразуем строку в список
                if isinstance(elements, list):
                    print(random.choice(elements))
                else:
                    print(Fore.RED + "Ошибка: передан неверный формат списка." + Style.RESET_ALL)
            except Exception as e:
                print(Fore.RED + f"Ошибка: {e}" + Style.RESET_ALL)

        else:
            print(Fore.RED + f"Неизвестная команда: {command}" + Style.RESET_ALL)


# Запуск интерпретатора через командную строку
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Использование: python interpreter.py <путь_к_файлу.shat>")
        sys.exit(1)

    file_path = sys.argv[1]
    interpreter = ShatInterpreter()
    interpreter.interpret_file(file_path)
