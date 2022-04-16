#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import argparse
import json
import os
import sys
from datetime import date


def get_product(prds, name, shop, cost):
    """
    Добавить данные.
    """
    prds.append(
        {
            "name": name,
            "shop": shop,
            "cost": cost
        }
    )
    return prds


def display_products(prds):
    if prds:
        # Заголовок таблицы.
        line = '+-{}-+-{}-+-{}-+-{}-+'.format(
            '-' * 4,
            '-' * 30,
            '-' * 20,
            '-' * 8
        )
        print(line)
        print(
            '| {:^4} | {:^30} | {:^20} | {:^8} |'.format(
                "No",
                "Продукт",
                "Магазин",
                "Цена"
            )
        )
        print(line)
        # Вывести данные о всех сотрудниках.
        for idx, product in enumerate(prds, 1):
            print(
                '| {:>4} | {:<30} | {:<20} | {:>8} |'.format(
                    idx,
                    product.get('name', ''),
                    product.get('shop', ''),
                    product.get('cost', 0)
                )
            )
            print(line)
    else:
        print("Список продуктов пуст")

def save_products(file_name, prds):
    """
    Сохранить все записи в файл JSON.
    """
    # Открыть файл с заданным именем для записи.
    with open(file_name, "w", encoding="utf-8") as fout:
        # Выполнить сериализацию данных в формат JSON.
        # Для поддержки кирилицы установим ensure_ascii=False
        json.dump(prds, fout, ensure_ascii=False, indent=4)


def load_products(file_name):
    """
    Загрузить все записи из файла JSON.
    """
    # Открыть файл с заданным именем для чтения.
    with open(file_name, "r", encoding="utf-8") as fin:
        return json.load(fin)


def main(command_line=None):
    # Создать родительский парсер для определения имени файла.
    file_parser = argparse.ArgumentParser(add_help=False)
    file_parser.add_argument(
        "-d",
        "--data",
        action="store",
        required=False,
        help="The data file name"
    )
    # Создать основной парсер командной строки.
    parser = argparse.ArgumentParser("products")
    parser.add_argument(
        "--version",
        action="version",
        version="%(prog)s 0.1.0"
    )
    subparsers = parser.add_subparsers(dest="command")
    # Создать субпарсер для добавления работника.
    add = subparsers.add_parser(
        "add",
        parents=[file_parser],
        help="Add a new product"
    )
    add.add_argument(
        "-n",
        "--name",
        action="store",
        required=True,
        help="The product's name"
    )
    add.add_argument(
        "-s",
        "--shop",
        action="store",
        help="The product's shop"
    )
    add.add_argument(
        "-c",
        "--cost",
        action="store",
        type=int,
        required=True,
        help="The cost of products"
    )
    # Создать субпарсер для отображения всех продуктов.
    _ = subparsers.add_parser(
        "display",
        parents=[file_parser],
        help="Display all workers"
    )

    # Выполнить разбор аргументов командной строки.
    args = parser.parse_args(command_line)
    # Получить имя файла.
    data_file = args.data
    if not data_file:
        os.environ.setdefault('WORKERS_DATA', 'd.json')
        data_file = os.environ.get("WORKERS_DATA")
    if not data_file:
        print("The data file name is absent", file=sys.stderr)
        sys.exit(1)
    # Загрузить все продукты из файла, если файл существует.
    is_dirty = False
    if os.path.exists(data_file):
        products = load_products(data_file)
    else:
        products = []
    # Добавить работника.
    if args.command == "add":
        products = get_product(
            products,
            args.name,
            args.shop,
            args.cost
        )
        is_dirty = True
    # Отобразить все продукты.
    elif args.command == "display":
        display_products(products)
    # Сохранить данные в файл, если список продуков был изменен.
    if is_dirty:
        save_products(data_file, products)


if __name__ == "__main__":
    main()