#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Импортируем модуль os
import os
import sys


if __name__ == '__main__':
    while True:
        # Принимаем имя переменной среды
        key_value = input("Enter the key of the environment variable:")
        # Проверяем, инициализирована ли переменная
        try:
            if os.environ[key_value]:
                print(
                    "The value of",
                    key_value,
                    " is ",
                    os.environ[key_value]
                )
        # Если переменной не присвоено значение, то ошибка
        except KeyError:
            print(key_value, 'environment variable is not set.')
            # Завершаем процесс выполнения скрипта
            sys.exit(1)