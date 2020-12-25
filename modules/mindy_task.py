##на основе списка функций создаются задачи для реализации ф-й максимум по 5 штук
#from typing import List, Tuple
#
#def get_module_name(file_name: str) -> str:
#    '''
#        Вернуть название файла без расширения и пути к этому файлу
#
#        >>> get_module_name('/manager/git.py')
#        'git'
#    '''
#    pass
#
#def get_task_name(funcs: List[Tuple[str, [str]]]) -> str:
#    '''
#        Составить название задачи по модулям, в которые входят функции для реализации
#
#        Вернуть строку "Реализовать функции в модулях: " +
#        добавлять через ", " значения, которые вернет ф-я get_module_name(), передавая в качестве
#        аргумента последовательно все значения первых эл-ов у кортежей из списка funcs
#
#        >>> get_task_name([('test_module1.py', ['func1()', 'func3()', 'func4()']), ('test_module2.py', ['func11()', 'func12()'])])
#        'Реализовать функции в модулях: test_module1, test_module2'
#    '''
#    pass
#
#def get_task_description(funcs: List[Tuple[str, [str]]]) -> str:
#    '''
#        >>> get_task_description([('test_module1.py', ['func1()', 'func3()', 'func4()']), ('test_module2.py', ['func11()', 'func12()'])])
#        'В модуле test_module1 реализовать функции:\nfunc1()\nfunc3()\nfunc4()\nВ модуле test_module2 реализовать функции:\nfunc11()\nfunc12()\n'
#    '''
#    pass

import requests
import json
import ast

url = "http://83.166.241.65:8888/get_reply?"

user = 'erladoisl'


r = 'результаты работы за прошлый месяц пользователя Раиля'
res = requests.get(url, data = {'text':r, 'user':user}).text.encode('l1').decode()
desc, data = res.split('||')
data = ast.literal_eval(data)
print(data)