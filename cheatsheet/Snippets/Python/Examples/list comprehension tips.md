```pycon
>>> list_of_tuples = [(1, 2), (3, 4), (5, 6)]
>>> result_list = [
...     item
...     for tpl in list_of_tuples
...     for item in tpl
... ]
>>> print(result_list)
[1, 2, 3, 4, 5, 6]
```
```pycon
>>> list_of_tuples = [(1, 2), (3, 4), (5, 6)]
>>> result_list = []
>>> for tpl in list_of_tuples:
...     for item in tpl:
...         result_list.append(item)
... 
>>> print(result_list)
[1, 2, 3, 4, 5, 6]
```
