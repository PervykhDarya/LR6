#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Импортируем модуль os
import os


if __name__ == '__main__':
    # Создаём цикл, чтобы вывести все переменные среды
    print("The keys and values of all environment variables:")
    for key in os.environ:
        print(key, '=>', os.environ[key])
    # Выводим значение одной переменной
    print("The value of HOME is: ", os.environ['HOME'])