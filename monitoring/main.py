import sys
import os.path
import requests
import sqlite3
import time
import datetime
import json
import traceback
import logging
import threading
from pprint import pprint
import pandas as pd

from settings import *


def create_monitoring_db(path: str):
    conn = sqlite3.connect(path)
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS monitoring (
                      id INTEGER PRIMARY KEY AUTOINCREMENT,
                      ts TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
                      url TEXT NOT NULL,
                      label TEXT NOT NULL,
                      response_time FLOAT,
                      status_code INTEGER DEFAULT NULL,
                      content_length INTEGER DEFAULT NULL
                      );
                   """)
    conn.commit()
    conn.close()


def add_data_monitoring_db(path, url, label, response_time, status_code, content_length):
    conn = sqlite3.connect(path)
    cursor = conn.cursor()
    if int(status_code) // 100 != 2:
        content_length = "NULL"
    cursor.execute("""INSERT INTO monitoring
                           (url, label, response_time, status_code, content_length)
                           VALUES (?, ?, ?, ?, ?)""", (url, label, response_time, status_code, content_length)
                   )
    conn.commit()
    conn.close()


def benchmark(func):
    """decorator"""
    def wrapper(*args, **kwags):
        start_func = time.time()
        result = func.get(*args, **kwags)
        end_func = time.time()
        return result, round((end_func - start_func) * 1000)
    return wrapper


def json_serial(obj):
    if isinstance(obj, (datetime.datetime, datetime.date)):
        return obj.isoformat()


def work_with_df(data, PATH_TO_DB, PATH_ERROR_DUMP_FILE, timeout):
    for _, row in data:
        try:
            label = row['label']
            url = row['url']
            response, response_time = benchmark(requests)(url, timeout=timeout)  # использование декоратора
            status_code = response.status_code
            content_length = len(response.text)
            add_data_monitoring_db(PATH_TO_DB, url=url, label=label, response_time=response_time,
                                   status_code=status_code, content_length=content_length)
            logging.info(f'status_code = {status_code}, url = {url}, response_time = {response_time}')
        except Exception as exc:
            data = {
                "timestamp": datetime.datetime.now(),
                "url": url,
                "error": {
                    "exception_type": exc.__repr__(),
                    "exception_value": exc.__str__(),
                    "stack_info": traceback.format_exc(),
                }
            }
            with open(PATH_ERROR_DUMP_FILE, "a") as write_file:
                json.dump(data, write_file, indent=4, default=json_serial)
            logging.info(f'exception_type = {exc.__repr__()}')


if __name__ == '__main__':
    # получение данных с командной строки
    try:
        if os.path.exists(sys.argv[1]):
            PATH_TO_XLSX = sys.argv[1]
    except:
        pass
    # Настраиваем 2 вывода информации о ходе работы
    handlers = [logging.FileHandler(PATH_LOGFILE), logging.StreamHandler()]
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', handlers=handlers)
    # logging.disable(logging.CRITICAL)  # отключение протоколирования
    try:
        create_monitoring_db(PATH_TO_DB)
        raw_data = pd.ExcelFile(PATH_TO_XLSX)
        df = pd.read_excel(raw_data, 'Лист1')
        df_sorted = df[df['fetch'] == 1]
        if not df_sorted.empty and number_of_threads >= 1:
            df_sorted_numbers = len(df_sorted)
            # Тут идет проверка, чтобы количество данных не было меньше потоков (для избежания дублирования)
            while True:
                step = df_sorted_numbers // number_of_threads
                residue = df_sorted_numbers % number_of_threads
                if step != 0:
                    break
                number_of_threads -= 1
            threads = []
            for i in range(number_of_threads):
                t = threading.Thread(name=f'Поток №{i}',
                                     target=work_with_df,
                                     args=(df_sorted[i * step:residue + (i + 1) * step].iterrows(), PATH_TO_DB,
                                           PATH_ERROR_DUMP_FILE, timeout))
                threads.append(t)
                t.start()
    except FileNotFoundError as error:
        print(f'файл не найден! {error}')

    ## Данный код для самопроверки  - выгружает данные из БД
    # conn = sqlite3.connect(PATH_TO_DB)
    # cursor = conn.cursor()
    # cursor.execute("SELECT * FROM monitoring")
    # pprint(cursor.fetchall())
    # # print(len(cursor.fetchall()))
    # conn.close()


