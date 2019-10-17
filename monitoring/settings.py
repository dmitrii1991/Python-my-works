"""
path_to_file = путь к файлу .xlsx
path_to_db = путь к базе данных .db
path_error_dump_file = путь к логам ошибок.json
path_logfile = путь к логам
timeout = None
number of threads = количество потоков

в случае отсутствия файла в данных переменных, файлы будут создаваться в тек. директории
"""
import os

path_to_file = r''
path_to_db = r''
path_error_dump_file = r''
path_logfile = r''
timeout = None
number_of_threads = 5

# базовые проверки для построение путей
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# данный путь задается автоматически, путь будет задан из консоли то в main.py перезапишется
if os.path.exists(path_to_file):
    PATH_TO_XLSX = path_to_file
else:
    PATH_TO_XLSX = os.path.join(BASE_DIR, 'raw_data.xlsx')

if os.path.exists(path_to_db):
    PATH_TO_DB = path_to_db
else:
    PATH_TO_DB = os.path.join(BASE_DIR, 'db.db')

if os.path.exists(path_to_db):
    PATH_ERROR_DUMP_FILE = path_error_dump_file
else:
    PATH_ERROR_DUMP_FILE = os.path.join(BASE_DIR, 'dump_file.json')

if os.path.exists(path_logfile):
    PATH_LOGFILE = path_logfile
else:
    PATH_LOGFILE = os.path.join(BASE_DIR, 'logfile.txt')
