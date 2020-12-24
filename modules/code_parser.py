#Определяются не реализованные функции в заданных модулях и формируются на их основе заготовки задач для mindy

from typing import List, Tuple, Dict, Optional
import traceback, logging
logging.basicConfig(filename="code_parser.log", level=logging.INFO)

def get_func(text:  List[str]) -> Optional[Tuple[str, List[str]]]:
    '''
        Возвращает название первой встретившейся не реализованной функции и оставшийся код

        Возвращает пару из: 
        1. Только название функций из первой строки, которая содержит подстроку def, после которой идет комментарий, 
           а за ним с новой строки сразу оператор pass,
        2. Список всех строк после этой строки
        если такой строки с def нет, возвращает None

    '''
    pass


def get_all_funcs(text: List[str]) -> List[Tuple[str, str]]:
    '''
        Список кортежей с данными о функциях

        Возвращает список, образованный последовательным применением get_func к text,
        пока get_func не вернет None, при этом в список добавляется первый элемент пары из get_func,
        а значение text обновляется, присваивая ему второй элемент пары, возвращамый из get_func

    '''
    pass
 
def get_file_funcs(file_name: str) -> List[Dict[str, str]]:
    ''' список словарей с данными о функциях из файла filename

        нужно прочитать строки из файла filename и вернуть результат get_all_funcs

    '''
#    result: List[Dict[str, str]] = []
#
#    try:
#        with open(file_name) as file_entry:
#            result = get_all_funcs(file_entry.read().split('\n'))
#    except IOError:
#        logging.error(traceback.format_exc())
#       print(f"Error while getting the file: {file_name}")
#    finally:
#        return result
    pass
    

def get_all_file_funcs(file_names: List[str]) -> List[Tuple[str, str]]:
    '''
        Находит во всех файлах не реализованные функции и возвращает список этих функций

        Возвращает список, элементы которого - это элементы списка, полученного путем применения get_file_funcs 
        для всех файлов из списка file_names

    '''
    pass

def get_task_descriptions(tasks: List[Tuple[str, str]]) -> List[List[Tuple[str, str]]]:
    '''
        Формирует список всех функций, разделенных на списки из 5 функций

    '''
    pass