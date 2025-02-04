```
BaseException - базовое исключение, от которого берут начало все остальные.
 +-- SystemExit - исключение, порождаемое функцией sys.exit при выходе из программы.
 +-- KeyboardInterrupt - порождается при прерывании программы пользователем (обычно сочетанием клавиш Ctrl+C).
 +-- GeneratorExit - порождается при вызове метода close объекта generator.
 +-- Exception - а вот тут уже заканчиваются полностью системные исключения (которые лучше не трогать) и начинаются обыкновенные, с которыми можно работать.
      +-- StopIteration - порождается встроенной функцией next, если в итераторе больше нет элементов.
      +-- StopAsyncIteration -  порождается встроенной функцией anext, если в асинхронном итераторе больше нет элементов.
      +-- ArithmeticError - арифметическая ошибка.
      |    +-- FloatingPointError - порождается при неудачном выполнении операции с плавающей запятой. На практике встречается нечасто.
      |    +-- OverflowError - возникает, когда результат арифметической операции слишком велик для представления.
      |                        Не появляется при обычной работе с целыми числами (так как python поддерживает длинные числа), но может возникать в некоторых других случаях.
      |    +-- ZeroDivisionError - деление на ноль.
      +-- AssertionError - выражение в функции assert ложно.
      +-- AttributeError - объект не имеет данного атрибута (значения или метода).
      +-- BufferError - операция, связанная с буфером, не может быть выполнена.
      +-- EOFError - функция наткнулась на конец файла и не смогла прочитать то, что хотела.
      +-- ImportError - не удалось импортирование модуля или его атрибута.
      |    +-- ModuleNotFoundError
      +-- LookupError - некорректный индекс или ключ.
      |    +-- IndexError - индекс не входит в диапазон элементов.
      |    +-- KeyError - несуществующий ключ (в словаре, множестве или другом объекте).
      +-- MemoryError - недостаточно памяти.
      +-- NameError - не найдено переменной с таким именем.
      |    +-- UnboundLocalError - сделана ссылка на локальную переменную в функции, но переменная не определена ранее.
      +-- OSError - ошибка, связанная с системой.
      |    +-- BlockingIOError - операция блокирует неблокируемый объект ввода-вывода (например, сокеты или файлы).
      |    +-- ChildProcessError - неудача при операции с дочерним процессом.
      |    +-- ConnectionError - базовый класс для исключений, связанных с подключениями.
      |    |    +-- BrokenPipeError - Возникает, когда попытка записи данных в закрытый канал или сокет завершается неудачей.
      |    |    +-- ConnectionAbortedError - Соединение неожиданно прервано до завершения.
      |    |    +-- ConnectionRefusedError - Соединение отклонено сервером (например, порт закрыт).
      |    |    +-- ConnectionResetError - Соединение сброшено другой стороной.
      |    +-- FileExistsError - попытка создания файла или директории, которая уже существует.
      |    +-- FileNotFoundError - файл или директория не существует.
      |    +-- InterruptedError - системный вызов прерван входящим сигналом.
      |    +-- IsADirectoryError - ожидался файл, но это директория.
      |    +-- NotADirectoryError - ожидалась директория, но это файл.
      |    +-- PermissionError - не хватает прав доступа.
      |    +-- ProcessLookupError - указанного процесса не существует.
      |    +-- TimeoutError - закончилось время ожидания.
      +-- ReferenceError - попытка доступа к атрибуту со слабой ссылкой.
      +-- RuntimeError - возникает, когда исключение не попадает ни под одну из других категорий.
      |    +-- NotImplementedError - возникает, когда абстрактные методы класса требуют переопределения в дочерних классах.
      |    +-- RecursionError - вызывается при превышении максимальной глубины рекурсии, часто из-за бесконечной рекурсии.
      +-- SyntaxError - синтаксическая ошибка.
      |    +-- IndentationError - неправильные отступы.
      |         +-- TabError - смешивание в отступах табуляции и пробелов.
      +-- SystemError - внутренняя ошибка.
      +-- TypeError - операция применена к объекту несоответствующего типа.
      +-- ValueError - функция получает аргумент правильного типа, но некорректного значения.
      |    +-- UnicodeError - ошибка, связанная с кодированием / раскодированием unicode в строках.
      |         +-- UnicodeDecodeError - исключение, связанное с кодированием unicode.
      |         +-- UnicodeEncodeError - исключение, связанное с декодированием unicode.
      |         +-- UnicodeTranslateError - исключение, связанное с переводом unicode.
      +-- Warning - предупреждение.
           +-- DeprecationWarning - предупреждает о функциях, которые устарели и будут удалены в будущей версии Python.
           +-- PendingDeprecationWarning - предназначено для функций, которые планируется упразднить в далеком будущем.
           +-- RuntimeWarning - предупреждает о проблемах, которые не попадают в другие категории, но все равно заслуживают внимания во время выполнения.
           +-- SyntaxWarning - предупреждает о сомнительном синтаксисе, который может привести к неожиданному поведению.
           +-- UserWarning - общее предупреждение для пользователей, часто используемое разработчиками для обозначения некритических проблем.
           +-- FutureWarning - предупреждает об изменениях, которые произойдут в будущих версиях Python.
           +-- ImportWarning - предупреждает о проблемах во время операций импорта.
           +-- UnicodeWarning - предупреждает о проблемах с операциями, связанными с Unicode.
           +-- BytesWarning - предупреждает о проблемах с операциями с байтами или байтовыми массивами.
           +-- ResourceWarning - предупреждает об использовании ресурсов (например, о незакрытых файлах).
           +-- EncodingWarning


EnvironmentError
IOError
WindowsError
```




# BaseException
Базовое исключение, от которого берут начало все остальные.
## SystemExit
Исключение, порождаемое функцией sys.exit при выходе из программы.
## KeyboardInterrupt
Порождается при прерывании программы пользователем (обычно сочетанием клавиш Ctrl+C).
## GeneratorExit
Порождается при вызове метода close объекта generator.
## Exception
А вот тут уже заканчиваются полностью системные исключения (которые лучше не трогать) и начинаются обыкновенные, с которыми можно работать.
### StopIteration
Порождается встроенной функцией next, если в итераторе больше нет элементов.
### StopAsyncIteration
Порождается встроенной функцией anext, если в асинхронном итераторе больше нет элементов.
### ArithmeticError
Арифметическая ошибка.
#### FloatingPointError
Порождается при неудачном выполнении операции с плавающей запятой. На практике встречается нечасто.
#### OverflowError
Возникает, когда результат арифметической операции слишком велик для представления. Не появляется при обычной работе с целыми числами (так как python поддерживает длинные числа), но может возникать в некоторых других случаях.
#### ZeroDivisionError
Деление на ноль.
### AssertionError
Выражение в функции assert ложно.
### AttributeError
Объект не имеет данного атрибута (значения или метода).
### BufferError
Операция, связанная с буфером, не может быть выполнена.
### EOFError
Функция наткнулась на конец файла и не смогла прочитать то, что хотела.
### ImportError
Не удалось импортирование модуля или его атрибута.
#### ModuleNotFoundError
### LookupError
Некорректный индекс или ключ.
#### IndexError
Индекс не входит в диапазон элементов.
#### KeyError
Несуществующий ключ (в словаре, множестве или другом объекте).
### MemoryError
Недостаточно памяти.
### NameError
Не найдено переменной с таким именем.
#### UnboundLocalError
Сделана ссылка на локальную переменную в функции, но переменная не определена ранее.
### OSError
Ошибка, связанная с системой.
#### BlockingIOError
Операция блокирует неблокируемый объект ввода-вывода (например, сокеты или файлы).
#### ChildProcessError
Неудача при операции с дочерним процессом.
#### ConnectionError
Базовый класс для исключений, связанных с подключениями.
##### BrokenPipeError
Возникает, когда попытка записи данных в закрытый канал или сокет завершается неудачей.
##### ConnectionAbortedError
Соединение неожиданно прервано до завершения.
##### ConnectionRefusedError
Соединение отклонено сервером (например, порт закрыт).
##### ConnectionResetError
Соединение сброшено другой стороной.
#### FileExistsError
Попытка создания файла или директории, которая уже существует.
#### FileNotFoundError
Файл или директория не существует.
#### InterruptedError
Системный вызов прерван входящим сигналом.
#### IsADirectoryError
Ожидался файл, но это директория.
#### NotADirectoryError
Ожидалась директория, но это файл.
#### PermissionError
Не хватает прав доступа.
#### ProcessLookupError
Указанного процесса не существует.
#### TimeoutError
Закончилось время ожидания.
### ReferenceError
Попытка доступа к атрибуту со слабой ссылкой.
### RuntimeError
Возникает, когда исключение не попадает ни под одну из других категорий.
#### NotImplementedError
Возникает, когда абстрактные методы класса требуют переопределения в дочерних классах.
#### RecursionError
Вызывается при превышении максимальной глубины рекурсии, часто из-за бесконечной рекурсии.
### SyntaxError
Синтаксическая ошибка.
#### IndentationError
Неправильные отступы.
##### TabError
Смешивание в отступах табуляции и пробелов.
### SystemError
Внутренняя ошибка.
### TypeError
Операция применена к объекту несоответствующего типа.
### ValueError
Функция получает аргумент правильного типа, но некорректного значения.
#### UnicodeError
Ошибка, связанная с кодированием / раскодированием unicode в строках.
##### UnicodeDecodeError
Исключение, связанное с кодированием unicode.
##### UnicodeEncodeError
Исключение, связанное с декодированием unicode.
##### UnicodeTranslateError
Исключение, связанное с переводом unicode.
### Warning
Предупреждение.
#### DeprecationWarning
Предупреждает о функциях, которые устарели и будут удалены в будущей версии Python.
#### PendingDeprecationWarning
Предназначено для функций, которые планируется упразднить в далеком будущем.
#### RuntimeWarning
Предупреждает о проблемах, которые не попадают в другие категории, но все равно заслуживают внимания во время выполнения.
#### SyntaxWarning
Предупреждает о сомнительном синтаксисе, который может привести к неожиданному поведению.
#### UserWarning
Общее предупреждение для пользователей, часто используемое разработчиками для обозначения некритических проблем.
#### FutureWarning
Предупреждает об изменениях, которые произойдут в будущих версиях Python.
#### ImportWarning
Предупреждает о проблемах во время операций импорта.
#### UnicodeWarning
Предупреждает о проблемах с операциями, связанными с Unicode.
#### BytesWarning
Предупреждает о проблемах с операциями с байтами или байтовыми массивами.
#### ResourceWarning
Предупреждает об использовании ресурсов (например, о незакрытых файлах).
#### EncodingWarning

EnvironmentError
IOError
WindowsError





# Методы Exception

[Подробнее про магические атрибуты исключений](?Languages/Python/Methods/Magic%20attributes#exception)

| Метод/Атрибут    | Описание                                                        | Пример использования                                             |
|------------------|-----------------------------------------------------------------|------------------------------------------------------------------|
| `add_note`       | Добавляет примечание к исключению                               | `e.add_note("Доп. информация")`                                  |
| `args`           | Кортеж аргументов, переданных при создании исключения           | `print(e.args)`                                                  |
| `with_traceback` | Привязывает traceback (информацию о стеке вызовов) к исключению | `new_exc = e.with_traceback(tb)`<br>`raise e.with_traceback(tb)` |

# Методы ExceptionGroup

Конструктор
```python
ExceptionGroup(message, exceptions)
```

| Метод/Атрибут    | Описание                                                                     | Пример использования                                          |
|------------------|------------------------------------------------------------------------------|---------------------------------------------------------------|
| `add_note`       | Добавляет примечание для всей группы исключений                              | `eg.add_note("Доп. информация")`                              |
| `args`           | Возвращает кортеж с описанием группы и списком исключений                    | `print(eg.args)`                                              |
| `derive`         | Создает новую группу исключений из подмножества текущей группы               | `derived_group = eg.derive([ValueError("Ошибка")])`           |
| `exceptions`     | Список всех исключений, входящих в группу                                    | `for e in eg.exceptions: print(e)`                            |
| `message`        | Описание группы исключений                                                   | `print(eg.message)`                                           |
| `split`          | Разделяет группу на две: исключения, удовлетворяющие условию, и остальные    | `match, rest = eg.split(lambda e: isinstance(e, ValueError))` |
| `subgroup`       | Возвращает подгруппу исключений, удовлетворяющих условию                     | `subgroup = eg.subgroup(lambda e: isinstance(e, KeyError))`   |
| `with_traceback` | Привязывает traceback (информацию о стеке вызовов) ко всей группе исключений | `new_group = eg.with_traceback(tb)`                           |

```pycon
>>> e = ValueError("Ошибка")
>>> e.add_note("Дополнительная информация о причине ошибки")
>>> print(e.__notes__)
['Дополнительная информация о причине ошибки.']
>>> raise e
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: Ошибка
Дополнительная информация о причине ошибки
>>> e.args
('Ошибка',)
```

```pycon
>>> try:
...     raise ExceptionGroup("Ошибки обработки данных", [
...         ValueError("Некорректное значение"),
...         TypeError("Несовместимый тип"),
...         KeyError("Ключ не найден"),
...     ])
... except ExceptionGroup as eg:
...     print(f"Сообщение группы: {eg.message}")
...     print("Исключения в группе:")
...     for e in eg.exceptions:
...         print(f"- {type(e).__name__}: {e}")
...     print("---")
...     # Разделяем на ValueError и остальные
...     match, rest = eg.split(lambda e: isinstance(e, ValueError))
...     print("Ошибки ValueError:")
...     for e in match.exceptions:
...         print(e)
...     print("Остальные ошибки:")
...     for e in rest.exceptions:
...         print(e)
...
Сообщение группы: Ошибки обработки данных
Исключения в группе:
- ValueError: Некорректное значение
- TypeError: Несовместимый тип
- KeyError: 'Ключ не найден'
---
Ошибки ValueError:
Некорректное значение
Остальные ошибки:
Несовместимый тип
'Ключ не найден'
```

```pycon
>>> try:
...     raise ExceptionGroup("Группа ошибок", [ValueError("Ошибка 1"), KeyError("Ошибка 2")])
... except ExceptionGroup as eg:
...     derived_group = eg.derive([ValueError("Ошибка 3")])
...     for e in derived_group.exceptions:
...         print(e.args)
...
('Ошибка 3',)
```
