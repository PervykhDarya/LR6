#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Импортируем модуль os
import os


if __name__ == '__main__':
    # Задаём значение переменной DEBUG
    os.environ.setdefault('DEBUG', 'True')
    # Проверяем значение переменной среды
    if os.environ.get('DEBUG') == 'True':
        print('Debug mode is on')
    else:
        print('Debug mode is off')