Библиотека "xml" в Python используется для работы с XML-данными
Она предоставляет функциональность для чтения, записи, и обработки XML-файлов

|                     |                                                                                                  |
|---------------------|--------------------------------------------------------------------------------------------------|
| `etree.ElementTree` | Позволяет работать с XML-деревом, включая чтение, запись, и обработку XML-элементов              |
| `dom`               | Предоставляет интерфейсы для работы с DOM (Document Object Model) XML-документов                 |
| `sax`               | Предоставляет SAX (Simple API for XML) интерфейс для обработки XML-документов в потоковом режиме |

### xml.etree.ElementTree.parse(file)
Читает XML-файл и возвращает корневой элемент дерева

```python
import xml.etree.ElementTree as ET

tree = ET.parse("file.xml")
root = tree.getroot()
```

### xml.etree.ElementTree.Element.findall(tag)
Возвращает список элементов с указанным тегом.

```python
import xml.etree.ElementTree as ET

tree = ET.parse("file.xml")
root = tree.getroot()

elements = root.findall("tag")
```

### xml.etree.ElementTree.Element.attrib
Возвращает атрибуты элемента в виде словаря

```python
import xml.etree.ElementTree as ET

tree = ET.parse("file.xml")
root = tree.getroot()

for element in root:
    attributes = element.attrib
    print(attributes)
```
