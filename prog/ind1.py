#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import sys

def get_train():
    """
    Запросить данные о поездах.
    """
    nomer = input("Номер поезда? ")
    punkt = input("Пункт назначения? ")
    time = int(input("Время отправления? "))
    # Создать словарь.
    return {
            'nomer': nomer,
            'punkt': punkt,
            'time': time,
        }


def display_trains(punkts):
    """
    Отобразить список поездов.
    """
    # Проверить, что список поездов не пуст.
    if punkts:
       # Заголовок таблицы.
        line = '+-{}-+-{}-+-{}-+-{}-+'.format(
            '-' * 4,
            '-' * 30,
            '-' * 20,
            '-' * 17
        )
        print(line)
        print('| {:^4} | {:^30} | {:^20} | {:^17} |'.format(
            "№",
            "Номер поезда",
            "Пункт назначения",
            "Время отправления"
            )
        )
        print(line)
        # Вывести данные о всех поездах.
        for idx, train in enumerate(punkts, 1):
            print('| {:>4} | {:<30} | {:<20} | {:>17} |'.format(
                idx,
                train.get('nomer', ''),
                train.get('punkt', ''),
                train.get('time', 0)
                )
            )
        print(line)
       
    else:
        print("Список поездов пуст.")
       
       
def select_trains(punkts, period):
    """
    Выбрать поезда с заданным временем.
    """
    result = []
    for van in punkts:
        if van.get('time', 0) >= period:
            result.append(van) 
   # Возвратить список выбранных поездов.
    return result


def main():
    """
    Главная функция программы.
    """
    trains = []
    
    while True:
        command = input(">>> ").lower()
        if command == 'exit':
           break
        elif command == 'add':
            train = get_train()
            trains.append(train) 
        elif command == 'list':
            display_trains(trains)
        elif command.startswith('select '):
            parts = command.split(' ', maxsplit=1)
            period = int(parts[1])
            # Выбрать поезда с заданным временем.
            selected = select_trains(trains, period)
            display_trains(selected)
        elif command == 'help':
            print("Список команд:\n")
            print("add - добавить поезд;")
            print("list - вывести список поездов;")
            print("select <время> - запросить поезда с временем отправления;")
            print("help - отобразить справку;")
            print("exit - завершить работу с программой.")
        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)


if __name__ == '__main__':
    main()