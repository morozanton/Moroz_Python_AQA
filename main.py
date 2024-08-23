import sys
import re


def parse_cl_args() -> dict:
    """
    Обрабатывает аргументы, переданные через командную строку, если они есть.
    :return: Именованный список аргументов.
    """
    args = sys.argv[1:]
    response = {}
    if args:
        for arg in args:
            try:
                response["number"] = int(arg)
            except ValueError:
                if array := str_to_list(arg):
                    response["array"] = array
                else:
                    response["name"] = arg
    return response


def str_to_list(s: str) -> list:
    """
    Возвращает список всех чисел, содержащихся в строке, используя любой нечисловой разделитель.
    :param s: Входная строка.
    :return: Список целых чисел, содержащихся в строке.
    """
    return re.findall(r"\d+", s)


def main(cl: dict) -> None:
    """
    Основная последовательность программы.
    Отдельные действия не выделены в самостоятельные функции для сокращения объема кода.
    :param cl: Словарь аргументов из командной строки, если они имеются.
                Для недостающих аргументов используется ввод из консоли.
    """
    number = cl.get("number") or int(input("Введите число: "))
    if number > 7:
        print("Привет", end="")

    name = cl.get("name") or input("\nВведите имя: ")
    if name == "Вячеслав":
        print("Привет, Вячеслав")
    else:
        print("Нет такого имени")

    array = cl.get("array") or str_to_list(
        input("\nВведите список элементов массива, разделяя их произвольным символом.\nПример: 1,2,3: "))
    print([n for n in array if not int(n) % 3])


if __name__ == "__main__":
    print('CLI usage: python main number "name" "array"')
    print("Prompt mode usage: python main\n")
    main(parse_cl_args())
