#Определяются не реализованные функции в заданных модулях и формируются на их основе заготовки задач для mindy

from typing import List, Tuple, Optional
import traceback, logging
logging.basicConfig(filename="code_parser.log", level=logging.INFO)

def get_func(text:  List[str]) -> Optional[Tuple[str, List[str]]]:
    '''
        Возвращает название первой встретившейся не реализованной функции и оставшийся код

        Возвращает пару из: 
        1. Только название функций из первой найденной в списке text строки, которая содержит 
        подстроку def, после которой идет комментарий, а за ним с новой строки сразу оператор pass
        2. Список всех строк после этой строки
        если такой строки с def нет, возвращает None

        >>> get_func(['anythings1', 'def mystring()', '\'\'\'', 'anythings2', '\'\'\'', 'pass', 'anythings3'])
        ('def mystring()', ['\'\'\'', 'anythings2', '\'\'\'', 'pass', 'anythings3'])        
    '''
    pass


def get_all_funcs(file_name: str, text: List[str]) -> List[Tuple[str, str]]:
    '''
        Список кортежей с данными о функциях

        Возвращает список пар, образованный последовательным применением get_func к text,
        пока get_func не вернет None, при этом в список добавляется первый элемент пары из get_func,
        а значение text обновляется, присваивая ему второй элемент пары, возвращамый из get_func

        >>> get_all_funcs('module_name.py', ['anythings', 'def mystring()', '\'\'\'', 'anythings', '\'\'\'', 'pass', 'anythings'])
        [('module_name.py', 'def mystring()')]
    '''
    pass

def get_file_funcs(file_name: str) -> List[Tuple[str, str]]:
    ''' список контежей с данными о функциях из файла filename

        нужно прочитать строки из файла filename и вернуть результат get_all_funcs
    '''
    result: List[Tuple[str, str]] = []

    try:
        with open(file_name) as file_entry:
            result = get_all_funcs(file_name, file_entry.read().split('\n'))
    except IOError:
        logging.error(traceback.format_exc())
        print(f"Error while getting the file: {file_name}")
    finally:
        return result
    pass
    
def join_funcs_by_module(funcs: List[Tuple[str, str]]) -> List[Tuple[str, [str]]]:
    '''
        Сгруппировать функции по модулям, к которым они принадлежат

        Пройтись по всем кортежам из func, сгруппировать кортежи по первому элементу,
        и получить список кортежей, где первый элемент пары будет первый совпадающий элемент у 
        сгруппированных кортежей, а второй элемент - список из вторых элементов сгруппированных кортежей 
    '''
    pass

def join_funcs(funcs: List[Tuple[str, str]]) -> List[List[Tuple[str, [str]]]]:
    '''
        Сформировать список задач, состоящий из 5ти функций, фукции из одинакового модуля помещать в один список

        Сформировать списки по пять элементов из funcs, получить: List[List[Tuple[str, str]]]
        Для каждого элемента из полученного списка применить join_funcs_by_module, возвращающее значение 
        сохранять в новый список.
        Вернуть полученный список

        
        >>> join_funcs([('test_module1.py', 'func1()'), ('test_module1.py', 'func3()'), ('test_module1.py', 'func4()'), ('test_module2.py', 'func11()'), ('test_module2.py', 'func12()'), ('test_module2.py', 'func14()')])
        [[('test_module1.py', ['func1()', 'func3()', 'func4()']), ('test_module2.py', ['func11()', 'func12()'])], [('test_module2.py', ['func14()'])]]
    '''
    pass

def get_all_file_funcs(file_names: List[str]) -> List[List[Tuple[str, [str]]]]:
    '''
        Находит во всех файлах не реализованные функции и возвращает список этих функций

        Получить список functions: List[Tuple[str, str]], элементы которого - это все элементы списка, полученного путем применения get_file_funcs 
        для всех файлов из списка file_names
        Вернуть список, колученный в результате выполнения ф-ии join_funcs(functions)

        >>> get_all_file_funcs(['test_module1.py', 'test_module2.py'])
        [[('test_module1.py', ['func1()', 'func3()', 'func4()']), ('test_module2.py', ['func11()', 'func12()'])], [('test_module2.py', ['func14()'])]]
    '''
    pass