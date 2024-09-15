from _dev.utils import to_table_code_py, to_table_code_java, to_table_code_sql


DICT = {
    "General": {
        "GIT": {
            "Команды": """
[https://git-scm.com/](https://git-scm.com/)

|                                          |
|------------------------------------------|
| git config --global user.name "username" |
| git config --global user.email "email"   |

|                              |                                             |
|------------------------------|---------------------------------------------|
| git init                     | инициализация нового репозитория            |
| git clone [url]              | клонирование существующего репозитория      |
| git add [file]               | добавление файла в индекс                   |
| git commit -m "message"      | коммит с сообщением                         |
| git diff                     | просмотр изменений в файлах                 |
| git status                   | просмотр текущего статуса репозитория<br>`Tracked` - файлы, о которых знает Git и которые добавляются в репозиторий.<br>`Untracked` - файлы, находящиеся в вашем рабочем каталоге, но не добавленные в репозиторий |
| git branch                   | просмотр списка веток                       |
| git checkout [branch/commit] | переключение на другую ветку/коммит         |
| git merge [branch]           | слияние ветки с текущей                     |
| git pull                     | получение и обновление удалённой ветки      |
| git push                     | отправка изменений на удалённый репозиторий |
| git log                      | просмотр истории коммитов                   |
| git reset [file]             | сброс индексации файла                      |
| git rm [file]                | удаление файла из репозитория               |
| mkdir [path]                 | сделать новый каталог                       |
| cd [path]                    | изменяет текущий рабочий каталог            |
| git init                     | инициализировать Git в этой папке           |
| git status                   | проверяем статус                            |
| git add [file_name]          | подготавливаем файл<br>Использование `--all` вместо отдельных имен файлов приведет к<br>`stage` изменению всех (новых, измененных и удаленных) файлов.<br>Сокращенная команда` git add --all` для `git add -A` |
| git status                   | проверяем статус                            |
| git commit -m "комментарий"  | подтверждаем                                |



# Git Commit без этапа
```sh
git status --short  # Увидеть изменения в более компактном виде
git commit -a -m "комментарий"
```
Обычно не рекомендуется пропускать промежуточную среду.
Пропуск этапа этапа иногда может привести к включению нежелательных изменений.


# Новая ветка Git
Мы работаем в нашем локальном репозитории 
и не хотим нарушать или разрушать основной проект.

```bash
git branch name              # Создаем новый ветки
git checkout name            # Извлечение файла ветки
git commit -m "комментарий"  # Подтверждаем
```

# Аварийное отделение
Теперь представьте, что мы еще не закончили с образами `hello-world`, но нам нужно исправить ошибку на `master`.
Я не хочу связываться с `master` напрямую, и я не хочу связываться с образами `hello-world`, так как это еще не сделано.

```bash
git checkout -b emergency-fix  # Создаем новую ветку для решения чрезвычайной ситуации
git status
git add name
git commit -m "комментарий"
```

# Объединить ветки
У нас готово аварийное исправление, 
поэтому давайте объединим ветки `master` и `Emergency-fix`.
Во-первых, нам нужно перейти на ветку `master`:

```bash
git checkout master
git merge emergency-fix      # Объединяем текущую ветку (master) с Emergency-fix
git branch -d emergency-fix  # Удалить Emergency-Fix
```

# Объединить конфликт

```bash
git checkout hello-world-images
git add --all
git commit -m "added new image"
```

![GIT.png](General/GIT/GIT.png)
""",
            "gitignore": """
| Шаблон | Примеры соответствия | Пояснение |
|--------|----------------------|-----------|
| **/logs                              | `logs/debug.log`<br>`logs/monday/foo.bar`<br>`build/logs/debug.log`                                | Добавьте в начало шаблона две звездочки,<br>чтобы сопоставлять каталоги в любом месте репозитория. |
| **/logs/debug.log                    | `logs/debug.log`<br>`build/logs/debug.log`<br>но не<br>`logs/build/debug.log`                      | Две звездочки можно также использовать для сопоставления файлов<br>на основе их имени и имени родительского каталога. |
| *.log                                | `debug.log`<br>`foo.log`<br>.log<br>`logs/debug.log`                                               | Одна звездочка — это подстановочный знак, который может<br>соответствовать как нескольким символам, так и ни одному. |
| *.log<br>!important.log              | `debug.log`<br>`trace.log`<br>но не<br>`important.log`<br>`logs/important.log`                     | Добавление восклицательного знака в начало шаблона отменяет действие шаблона.<br>Если файл соответствует некоему шаблону,<br>но при этом также соответствует отменяющему шаблону, указанному после,<br>такой файл не будет игнорироваться. |
| *.log<br>!important/*.log<br>trace.* | `debug.log`<br>`important/trace.log`<br>но не<br>`important/debug.log`                             | Шаблоны, указанные после отменяющего шаблона,<br>снова будут помечать файлы как игнорируемые,<br>даже если ранее игнорирование этих файлов было отменено. |
| /debug.log                           | `debug.log`<br>но не<br>`logs/debug.log`                                                           | Косая черта перед именем файла соответствует файлу в корневом каталоге репозитория. |
| debug.log                            | `debug.log`<br>`logs/debug.log`                                                                    | По умолчанию шаблоны соответствуют файлам, находящимся в любом каталоге |
| debug?.log                           | `debug0.log`<br>`debugg.log`<br>но не<br>`debug10.log`                                             | Знак вопроса соответствует строго одному символу. |
| debug[0-9].log                       | `debug0.log`<br>`debug1.log`<br>но не<br>`debug10.log`                                             | Квадратные скобки можно также использовать<br>для указания соответствия одному символу из заданного диапазона. |
| debug[01].log                        | `debug0.log`<br>`debug1.log`<br>но не<br>`debug2.log`<br>`debug01.log`                             | Квадратные скобки соответствуют одному символу из указанного набора. |
| debug[!01].log                       | `debug2.log`<br>но не<br>`debug0.log`<br>`debug1.log`<br>`debug01.log`                               | Восклицательный знак можно использовать для указания<br>соответствия любому символу, кроме символов из указанного набора. |
| debug[a-z].log                       | `debuga.log`<br>`debugb.log`<br>но не<br>`debug1.log`                                              | Диапазоны могут быть цифровыми или буквенными. |
| logs                                 | `logs`<br>`logs/debug.log`<br>`logs/latest/foo.bar`<br>`build/logs`<br>`build/logs/debug.log`      | Без косой черты в конце этот шаблон будет соответствовать и файлам,<br>и содержимому каталогов с таким именем.<br>В примере соответствия слева игнорируются и каталоги, и файлы с именем `logs` |
| logs/                                | `logs/debug.log`<br>`logs/latest/foo.bar`<br>`build/logs/foo.bar`<br>`build/logs/latest/debug.log` | Косая черта в конце шаблона означает каталог.<br>Все содержимое любого каталога репозитория, соответствующего этому имени<br>(включая все его файлы и подкаталоги), будет игнорироваться |
| logs/<br>!logs/important.log         | `logs/debug.log`<br>`logs/important.log`                                                           | Минуточку!<br>Разве файл `logs/important.log` из примера слева<br>не должен быть исключен нз списка игнорируемых?<br>Нет!<br>Из-за странностей Git, связанных с производительностью,<br>вы не можете отменить игнорирование файла, которое задано шаблоном соответствия каталогу |
| logs/**/debug.log                    | `logs/debug.log`<br>`logs/monday/debug.log`<br>`logs/monday/pm/debug.log`                          | Две звездочки соответствуют множеству каталогов или ни одному. |
| logs/*day/debug.log                  | `logs/monday/debug.log`<br>`logs/tuesday/debug.log`<br>но не<br>`logs/latest/debug.log`            | Подстановочные символы можно использовать и в именах каталогов. |
| logs/debug.log                       | `logs/debug.log`<br>но не<br>`debug.log`<br>`build/logs/debug.log`                                 | Шаблоны, указывающие на файл в определенном каталоге,<br>задаются относительно корневого каталога репозитория.<br>(При желании можно добавить в начало косую черту, но она ни на что особо не повлияет.) |
""",
            "Setup deploy key": """
GitHub UserName <input style="border-style: none;display: inline-block;background-color: #191919;min-width: 154px;font-size: 16px;padding: 2px;border: 1px solid #2B2B2B;color: #AFB1B3;height: 100%;" placeholder="UserName" type="username" id="github-username-input" oninput="element=this.parentElement.nextElementSibling.nextElementSibling.lastChild.firstChild.firstChild;lines=element.innerHTML.split('\\n');for(var i=0;i&lt;lines.length;i++){if (!this.value){v='github-username'} else {v=this.value};if(i === 0           ){lines[i]=lines[i].substring(0,153)+v+'&quot;</span>';}};element.innerHTML=lines.join('\\n')">

Email           <input style="border-style: none;display: inline-block;background-color: #191919;min-width: 154px;font-size: 16px;padding: 2px;border: 1px solid #2B2B2B;color: #AFB1B3;height: 100%;" placeholder="Email"    type="email"    id="github-email-input"    oninput="element=this.parentElement.nextElementSibling                   .lastChild.firstChild.firstChild;lines=element.innerHTML.split('\\n');for(var i=0;i&lt;lines.length;i++){if (!this.value){v='github-email'   } else {v=this.value};if(i === 1){lines[i]=lines[i].substring(0,141)+v+'&quot;</span>';};if(i === 2){lines[i]=lines[i].substring(0,135)+v+'&quot;</span>';}};element.innerHTML=lines.join('\\n')">


```bash
git config --global user.name "github-username"
git config --global user.email "github-email"
ssh-keygen -t ed25519 -C "github-email"


eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_rsa
```

`ssh-keygen -t rsa -b 4096 -C "github-email"`

Скопировать содержимое `id_rsa.pub` и вставить в ключи для деплоя в репозиторий

`git clone git@github.com:github-username/github-repo-name.git`
""",
            "git": """

|                                                              |                                                                                                                  |
|--------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------|
| `echo "# название" >> README.md`                             | Создание файла `README.md`                                                                                       |
| `git init`                                                   | Инициализация репозитория                                                                                        |
| `git add README.md`                                          | Добавления файла `README.md` в проект                                                                            |
| `git commit -m "first commit"`                               | Получает проиндексированный снимок состояния<br>и выполняет его коммит в историю проекта                         |
| `git remote add origin https://github.com/username/repo.git` | Команда, которой устанавливается подключение<br>к удаленному серверу и `git` репозиторию, размещающемуся на нем. |
| `git push -u origin master`                                  | Кзменения отправляются на удаленный сервер                                                                       |

|                              |                                    |
|------------------------------|------------------------------------|
| `git log --oneline`          | Посмотреть все коммиты             |
| `git checkout .`             | Восстановить все                   |
| `git checkout "код коммита"` | Вернуть до состояния этого коммита |
| `git checkout master`        | Вернуться в ветку мастер           |

Восстановить файлы на локальном компьютере:
`git fetch --all`

`git reset --hard origin/master` или `git reset --hard origin/<название_ветки>`

|                                                  |                                                                                  |
|--------------------------------------------------|----------------------------------------------------------------------------------|
| `git add text.txt`                               | Добавить файл в репозиторий                                                      |
| `git rm text.txt`                                | Удалить файл                                                                     |
| `git status`                                     | Текущее состояние репозитория (изменения, неразрешенные конфликты и тп)          |
| `git commit -a -m "Commit description"`          | Сделать коммит                                                                   |
| `git push origin`                                | Замерджить все ветки локального репозитория на удаленный репозиторий             |
| `git push origin master`                         | Аналогично предыдущему, но делается пуш только ветки master                      |
| `git push origin HEAD`                           | Запушить текущую ветку, не вводя целиком ее название                             |
| `git pull origin`                                | Замерджить все ветки с удаленного репозитория                                    |
| `git pull origin master`                         | Аналогично предыдущему, но накатывается только ветка master                      |
| `git pull origin HEAD`                           | Накатить текущую ветку, не вводя ее длинное имя                                  |
| `git fetch origin`                               | Скачать все ветки с origin, но не мерджить их в локальный репозиторий            |
| `git fetch origin master`                        | Аналогично предыдущему, но только для одной заданной ветки                       |
| `git checkout -b some_branch origin/some_branch` | Начать работать с веткой some_branch (уже существующей)                          |
| `git branch some_branch`                         | Создать новый бранч (ответвится от текущего)                                     |
| `git checkout some_branch`                       | Переключиться на другую ветку (из тех, с которыми уже работаем)                  |
| `git branch`                                     | Получаем список веток, с которыми работаем (звездочкой отмечена текущая ветвь)   |
| `git branch -a # | grep something`               | Просмотреть все существующие ветви                                               |
| `git merge some_branch`                          | Замерджить some_branch в текущую ветку                                           |
| `git branch -d some_branch`                      | Удалить бранч (после мерджа)                                                     |
| `git branch -D some_branch`                      | Просто удалить бранч (тупиковая ветвь)                                           |
| `git show commit_hash`                           | Изменения, сделанные в заданном коммите                                          |
| `git push origin :branch-name`                   | Удалить бранч из репозитория на сервере                                          |
| `git reset --hard commit_hash`                   | Откатиться к конкретному коммиту и удалить последующие (хэш смотрим в «git log») |
| `git push -f`                                    | Залить на сервер измененные коммиты                                              |
| `git clean -f`                                   | Удаление untracked files                                                         |

""",
        },
        "Паттерны проектирования": {
            "index": """
# Паттерны проектирования

### Порождающие паттерны <img alt="C" src="General/Паттерны проектирования/C.png" height="17">

Порождающие паттерны проектирования фокусируются на процессах создания объектов.
Они помогают абстрагировать процесс инстанцирования, что может быть полезным,
когда конкретный процесс создания объекта должен быть отделён от его использования.
Это позволяет создавать объекты более гибко и предотвращает жесткую связь между кодом и конкретными классами объектов.


### Структурные паттерны <img alt="S" src="General/Паттерны проектирования/S.png" height="17">

Структурные паттерны проектирования фокусируются на том, как компоненты системы (например, классы и объекты)
могут быть объединены для создания более крупных и гибких структур.
Эти паттерны помогают определить отношения между компонентами и обеспечивают гибкость и масштабируемость систем.


### Поведенческие паттерны <img alt="B" src="General/Паттерны проектирования/B.png" height="17">

Поведенческие паттерны проектирования фокусируются на взаимодействии и распределении обязанностей между объектами и классами.
Они помогают определить, как объекты должны взаимодействовать друг с другом и как распределять ответственность между ними.


![patterns.png](General/Паттерны проектирования/patterns.png)

- [https://ru.wikipedia.org/wiki/Design_Patterns](https://ru.wikipedia.org/wiki/Design_Patterns)
    - [https://ru.wikipedia.org/wiki/Порождающие_шаблоны_проектирования](https://ru.wikipedia.org/wiki/Порождающие_шаблоны_проектирования)
    - [https://ru.wikipedia.org/wiki/Структурные_шаблоны_проектирования](https://ru.wikipedia.org/wiki/Структурные_шаблоны_проектирования)
    - [https://ru.wikipedia.org/wiki/Поведенческие_шаблоны_проектирования](https://ru.wikipedia.org/wiki/Поведенческие_шаблоны_проектирования)

# ChatGPT Promt

````markdown
Я буду тебе писать название паттерна проектирования, а ты будешь максимально кратко объяснять его в виде шпаргалки с примерами кода.
По шаблону:
# <Название шаблона на английском языке> (<Перевод названия на русском языке>)

**Описание**: <Описание>

**Когда использовать**: <Когда использовать>

```python
<Короткий пример кода объясняющий работу паттерна>
```

Заменяй только то что находится в <>
````

# patterns_image_generator.py

<details><summary>code</summary>

```python@patterns_image_generator.py
# pip install pillow
from PIL import Image, ImageDraw, ImageFont


color = {
    "orange": (254, 203, 158),
    "blue": (153, 205, 252),
    "green": (207, 252, 157),
}
pattern_color = {
    "C": color["blue"],
    "S": color["orange"],
    "B": color["green"],
}
pattern = {
    "C": [
        "Singleton (Одиночка)",
        "Factory (Фабрика)",
        "Abstract Factory (Абстрактная фабрика)",
        "Builder (Строитель)",
        "Prototype (Прототип)",
    ],
    "S": [
        "Adapter (Адаптер)",
        "Bridge (Мост)",
        "Composite (Компоновщик)",
        "Decorator (Декоратор)",
        "Facade (Фасад)",
        "Flyweight (Легковес)",
        "Proxy (Заместитель)",
    ],
    "B": [
        "Chain of Responsibility (Цепочка обязанностей)",
        "Command (Команда)",
        "Interpreter (Интерпретатор)",
        "Iterator (Итератор)",
        "Mediator (Посредник)",
        "Memento (Снимок)",
        "Observer (Наблюдатель)",
        "State (Состояние)",
        "Strategy (Стратегия)",
        "Template Method (Шаблонный метод)",
        "Visitor (Посетитель)",
    ],
}
indent = 16
border = 3
rectangle = (64, 45)
text_x_indent = indent * 0.4
text_y_indent = indent // 2
now_x = indent
now_y = indent
font = ImageFont.truetype("arial", 25)

image_x = indent + sum(
    rectangle[0] + indent*2 + font.getbbox(max(pattern_list, key=len))[2]
    for pattern_list in pattern.values()
)
image_y = indent + max(
    len(pattern_list) for pattern_list in pattern.values()
) * (rectangle[1] + indent)
image = Image.new("RGB", (image_x, image_y), "#FFFFFF")
draw = ImageDraw.Draw(image)


for pattern_type, pattern_list in pattern.items():
    for pattern in pattern_list:
        draw.rectangle(
            (now_x, now_y, now_x + rectangle[0], now_y + rectangle[1]),
            pattern_color[pattern_type],
            outline="#000000",
            width=border,
        )
        draw.text(
            (now_x + indent + text_x_indent, now_y + text_y_indent),
            pattern_type,
            fill="#000000",
            font=font,
        )
        draw.text(
            (now_x + rectangle[0] + indent, now_y + text_y_indent),
            pattern,
            fill="#000000",
            font=font,
        )
        draw.point((now_x, now_y), "#FF0000")
        now_y += rectangle[1] + indent

    now_y = indent
    now_x += rectangle[0] + indent * 2 + font.getbbox(max(pattern_list, key=len))[2]


image.save("patterns.png", format="PNG")
```

</details>
""",
            "Порождающие паттерны": {
                "Singleton (Одиночка)": """
## Singleton (Одиночка)

**Описание:** Гарантирует, что у класса есть только **один экземпляр**,
и предоставляет глобальную точку доступа к этому экземпляру.

**Когда использовать:** Когда нужно ограничить создание объекта одним экземпляром,
например, для логгера, подключения к базе данных, конфигурационного объекта.

```python
class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance


singleton1 = Singleton()
singleton2 = Singleton()
print(singleton1 is singleton2)  # True
```
""",
                "Factory (Фабрика)": """
## Factory (Фабрика)

**Описание:** Предоставляет интерфейс для создания объектов в суперклассе,
но позволяет подклассам изменять тип создаваемых объектов.

**Когда использовать:** Когда нужно делегировать создание объектов подклассам
или когда тип создаваемых объектов заранее неизвестен.

```python
class Car:
    def drive(self):
        raise NotImplementedError


class ElectricCar(Car):
    def drive(self):
        return "Driving an electric car"


class PetrolCar(Car):
    def drive(self):
        return "Driving a petrol car"


class CarFactory:
    @staticmethod
    def create_car(car_type):
        if car_type == "electric":
            return ElectricCar()
        elif car_type == "petrol":
            return PetrolCar()
        else:
            raise ValueError("Unknown car type")
```
""",
                "Abstract Factory (Абстрактная фабрика)": """
# Abstract Factory (Абстрактная фабрика)

**Описание**: Предоставляет интерфейс для создания семейств связанных объектов без указания их конкретных классов.

**Когда использовать**: Когда нужно создавать семейства объектов, которые должны использоваться вместе.

```python
class AbstractProductA:
    def do_something(self):
        pass

class ConcreteProductA1(AbstractProductA):
    def do_something(self):
        return "Product A1"

class ConcreteProductA2(AbstractProductA):
    def do_something(self):
        return "Product A2"

class AbstractFactory:
    def create_product_a(self):
        pass

class ConcreteFactory1(AbstractFactory):
    def create_product_a(self):
        return ConcreteProductA1()

class ConcreteFactory2(AbstractFactory):
    def create_product_a(self):
        return ConcreteProductA2()

factory1 = ConcreteFactory1()
product_a1 = factory1.create_product_a()
print(product_a1.do_something())  # Product A1

factory2 = ConcreteFactory2()
product_a2 = factory2.create_product_a()
print(product_a2.do_something())  # Product A2
```
""",
                "Builder (Строитель)": """
### Builder (Строитель)
Паттерн Строитель используется для пошагового создания сложных объектов.
Он отделяет конструирование объекта от его представления,
так что один и тот же процесс создания может создавать разные представления.

```python
class House:
    def __init__(self):
        self.walls = None
        self.roof = None
        self.doors = None

    def __str__(self):
        return f"Walls: {self.walls}, Roof: {self.roof}, Doors: {self.doors}"


class HouseBuilder:
    def __init__(self):
        self.house = House()

    def build_walls(self, walls):
        self.house.walls = walls
        return self

    def build_roof(self, roof):
        self.house.roof = roof
        return self

    def build_doors(self, doors):
        self.house.doors = doors
        return self

    def get_house(self):
        return self.house


builder = HouseBuilder()
house = builder.build_walls("Brick walls").build_roof("Tile roof").build_doors("Wooden doors").get_house()
print(house)
```
""",
                "Prototype (Прототип)": """
# Prototype (Прототип)

**Описание**: Позволяет создавать новые объекты путем копирования существующих экземпляров (прототипов).

**Когда использовать**: Когда создание объектов дорогое или сложное, а также когда нужно избежать повторного выполнения инициализационного кода.

```python
import copy


class Prototype:
    def __init__(self, value):
        self.value = value

    def clone(self):
        return copy.deepcopy(self)


prototype = Prototype(42)
clone = prototype.clone()
print(clone.value)  # 42
```
""",
            },
            "Структурные паттерны": {
                "Adapter (Адаптер)": """
# Adapter (Адаптер)

**Описание**: Позволяет объектам с несовместимыми интерфейсами работать вместе, преобразуя интерфейс одного объекта в интерфейс, ожидаемый другим.

**Когда использовать**: Когда нужно использовать существующий класс с несовместимым интерфейсом.

```python
class Adaptee:
    def specific_request(self):
        return "Adaptee behavior"

class Adapter:
    def __init__(self, adaptee):
        self._adaptee = adaptee

    def request(self):
        return self._adaptee.specific_request()

adaptee = Adaptee()
adapter = Adapter(adaptee)
print(adapter.request())  # Adaptee behavior
```
""",
                "Bridge (Мост)": """
# Bridge (Мост)

**Описание**: Разделяет абстракцию и реализацию, позволяя изменять их независимо друг от друга.

**Когда использовать**: Когда нужно разделить абстракцию и реализацию для независимой модификации и избежать жесткой связанности.

```python
class Implementation:
    def operation(self):
        pass

class ConcreteImplementationA(Implementation):
    def operation(self):
        return "Implementation A"

class ConcreteImplementationB(Implementation):
    def operation(self):
        return "Implementation B"

class Abstraction:
    def __init__(self, implementation):
        self._implementation = implementation

    def execute(self):
        return self._implementation.operation()

abstraction_a = Abstraction(ConcreteImplementationA())
abstraction_b = Abstraction(ConcreteImplementationB())

print(abstraction_a.execute())  # Implementation A
print(abstraction_b.execute())  # Implementation B
```
""",
                "Composite (Компоновщик)": """
### Composite (Компоновщик)

Паттерн Компоновщик позволяет работать с группами объектов так же, как с отдельными объектами.
Это удобно для представления иерархических структур.

```python
class Graphic:
    def render(self):
        pass


class Line(Graphic):
    def render(self):
        print("Rendering a line")


class Rectangle(Graphic):
    def render(self):
        print("Rendering a rectangle")


class GraphicGroup(Graphic):
    def __init__(self):
        self.graphics = []

    def add(self, graphic):
        self.graphics.append(graphic)

    def render(self):
        for graphic in self.graphics:
            graphic.render()


group = GraphicGroup()
group.add(Line())
group.add(Rectangle())
group.add(Line())
group.render()
# Rendering a line
# Rendering a rectangle
# Rendering a line
```
""",
                "Decorator (Декоратор)": """
## Decorator (Декоратор)

**Описание:** Позволяет динамически добавлять новое поведение объектам, оборачивая их в класс-оболочку.

**Когда использовать:** Когда нужно добавлять дополнительные функциональности объектам без изменения их класса.

```python
class Component:
    def operation(self):
        pass


class ConcreteComponent(Component):
    def operation(self):
        return "ConcreteComponent"


class Decorator(Component):
    def __init__(self, component):
        self._component = component

    def operation(self):
        return f"Decorator({self._component.operation()})"


component = ConcreteComponent()
decorated = Decorator(component)
print(decorated.operation())  # "Decorator(ConcreteComponent)"
```
""",
                "Facade (Фасад)": """
### Facade (Фасад)

Паттерн Фасад предоставляет унифицированный интерфейс к набору интерфейсов в подсистеме, упрощая использование сложных систем.

```python
class CPU:
    def freeze(self):
        print("Freezing CPU")

    def jump(self, position):
        print(f"Jumping to {position}")

    def execute(self):
        print("Executing instructions")


class Memory:
    def load(self, position, data):
        print(f"Loading data from {position} to {data}")


class HardDrive:
    def read(self, lba, size):
        print(f"Reading {size} bytes from LBA {lba}")
        return "data"


class ComputerFacade:
    def __init__(self):
        self.cpu = CPU()
        self.memory = Memory()
        self.hard_drive = HardDrive()

    def start(self):
        self.cpu.freeze()
        self.memory.load(0, self.hard_drive.read(1024, 4096))
        self.cpu.jump(0)
        self.cpu.execute()


computer = ComputerFacade()
computer.start()
# Freezing CPU
# Reading 4096 bytes from LBA 1024
# Loading data from 0 to data
# Jumping to 0
# Executing instructions
```
""",
                "Flyweight (Легковес)": """
# Flyweight (Легковес)

**Описание**: Оптимизация использования памяти за счёт разделения общих данных между множеством объектов.

**Когда использовать**: Когда нужно создать много мелких объектов, которые имеют общие части данных.

```python
class Flyweight:
    def __init__(self, shared_state):
        self.shared_state = shared_state

class FlyweightFactory:
    def __init__(self):
        self._flyweights = {}

    def get_flyweight(self, shared_state):
        if shared_state not in self._flyweights:
            self._flyweights[shared_state] = Flyweight(shared_state)
        return self._flyweights[shared_state]

factory = FlyweightFactory()
flyweight1 = factory.get_flyweight("shared")
flyweight2 = factory.get_flyweight("shared")
print(flyweight1 is flyweight2)  # True
```
""",
                "Proxy (Заместитель)": """
# Proxy (Заместитель)

**Описание**: Представляет собой объект-заместитель, который контролирует доступ к другому объекту.

**Когда использовать**: Когда нужно управлять доступом к объекту, например, для ленивой инициализации, контроля доступа или логирования.

```python
class RealSubject:
    def request(self):
        return "RealSubject: Handling request."

class Proxy:
    def __init__(self, real_subject):
        self._real_subject = real_subject

    def request(self):
        print("Proxy: Checking access before forwarding request.")
        return self._real_subject.request()

real_subject = RealSubject()
proxy = Proxy(real_subject)
print(proxy.request())
# Proxy: Checking access before forwarding request.
# RealSubject: Handling request.
```
""",
            },
            "Поведенческие паттерны": {
                "Chain of Responsibility (Цепочка обязанностей)": """
# Chain of Responsibility (Цепочка обязанностей)

**Описание**: Позволяет передавать запрос по цепочке обработчиков, где каждый обработчик решает, обработать запрос или передать следующему.

**Когда использовать**: Когда нужно передавать запрос последовательно через ряд обработчиков, не определяя явно, какой обработчик его обработает.

```python
class Handler:
    def __init__(self, successor=None):
        self._successor = successor

    def handle(self, request):
        if self._successor:
            return self._successor.handle(request)
        return None

class ConcreteHandlerA(Handler):
    def handle(self, request):
        if request == "A":
            return "Handled by A"
        return super().handle(request)

class ConcreteHandlerB(Handler):
    def handle(self, request):
        if request == "B":
            return "Handled by B"
        return super().handle(request)


handler = ConcreteHandlerA(ConcreteHandlerB())
print(handler.handle("A"))  # Handled by A
print(handler.handle("B"))  # Handled by B
print(handler.handle("C"))  # None
```
""",
                "Command (Команда)": """
# Command (Команда)

**Описание**: Инкапсулирует запрос как объект, позволяя параметризовать объекты с различными запросами, ставить запросы в очередь или делать их отменяемыми.

**Когда использовать**: Когда нужно отделить вызов операции от объекта, который её выполняет, или когда требуется логировать, отменять и повторять операции.

```python
class Command:
    def execute(self):
        pass

class Light:
    def turn_on(self):
        return "Light is on"

class LightOnCommand(Command):
    def __init__(self, light):
        self._light = light

    def execute(self):
        return self._light.turn_on()

class RemoteControl:
    def __init__(self, command):
        self._command = command

    def press_button(self):
        return self._command.execute()


light = Light()
command = LightOnCommand(light)
remote = RemoteControl(command)
print(remote.press_button())  # Light is on
```
""",
                "Interpreter (Интерпретатор)": """
# Interpreter (Интерпретатор)

**Описание**: Определяет грамматику языка и интерпретирует предложения в этом языке.

**Когда использовать**: Когда нужно анализировать и исполнять предложения в специфическом языке или грамматике.

```python
class Expression:
    def interpret(self, context):
        pass

class Number(Expression):
    def __init__(self, value):
        self.value = value

    def interpret(self, context):
        return self.value

class Add(Expression):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def interpret(self, context):
        return self.left.interpret(context) + self.right.interpret(context)


context = {}
expr = Add(Number(3), Number(4))
print(expr.interpret(context))  # 7
```
""",
                "Iterator (Итератор)": """
# Iterator (Итератор)

**Описание**: Предоставляет способ последовательного доступа ко всем элементам коллекции без раскрытия её внутреннего представления.

**Когда использовать**: Когда нужно последовательно обойти элементы коллекции без раскрытия её внутренней структуры.

```python
class Iterator:
    def __init__(self, collection):
        self._collection = collection
        self._index = 0

    def has_next(self):
        return self._index < len(self._collection)

    def next(self):
        if self.has_next():
            value = self._collection[self._index]
            self._index += 1
            return value
        raise StopIteration


collection = [1, 2, 3]
iterator = Iterator(collection)

while iterator.has_next():
    print(iterator.next())  # 1 2 3
```
""",
                "Mediator (Посредник)": """
# Mediator (Посредник)

**Описание**: Определяет объект, инкапсулирующий взаимодействие между наборами объектов, чтобы предотвратить их прямую связь.

**Когда использовать**: Когда нужно уменьшить связанность между объектами и централизовать управление их взаимодействием.

```python
class Mediator:
    def notify(self, sender, event):
        pass

class ConcreteMediator(Mediator):
    def __init__(self, component1, component2):
        self._component1 = component1
        self._component2 = component2
        self._component1.mediator = self
        self._component2.mediator = self

    def notify(self, sender, event):
        if sender == self._component1 and event == "event1":
            return self._component2.do_action()
        elif sender == self._component2 and event == "event2":
            return self._component1.do_action()

class Component:
    def __init__(self):
        self.mediator = None

    def do_action(self):
        return "Action performed"

    def trigger(self, event):
        return self.mediator.notify(self, event)


component1 = Component()
component2 = Component()
mediator = ConcreteMediator(component1, component2)
print(component1.trigger("event1"))  # Action performed
print(component2.trigger("event2"))  # Action performed
```
""",
                "Memento (Снимок)": """
# Memento (Снимок)

**Описание**: Позволяет сохранять и восстанавливать внутреннее состояние объекта без раскрытия его реализации.

**Когда использовать**: Когда нужно сохранить состояние объекта и при необходимости восстановить его позже, не нарушая инкапсуляции.

```python
class Memento:
    def __init__(self, state):
        self._state = state

    def get_state(self):
        return self._state

class Originator:
    def __init__(self, state):
        self._state = state

    def set_state(self, state):
        self._state = state

    def create_memento(self):
        return Memento(self._state)

    def restore_memento(self, memento):
        self._state = memento.get_state()

class Caretaker:
    def __init__(self):
        self._mementos = []

    def add_memento(self, memento):
        self._mementos.append(memento)

    def get_memento(self, index):
        return self._mementos[index]


originator = Originator("State1")
caretaker = Caretaker()
caretaker.add_memento(originator.create_memento())
originator.set_state("State2")
print(originator._state)  # State2
originator.restore_memento(caretaker.get_memento(0))
print(originator._state)  # State1
```
""",
                "Observer (Наблюдатель)": """
# Observer (Наблюдатель)

**Описание**: Определяет зависимость один ко многим между объектами,
так что при изменении состояния одного объекта все зависимые объекты уведомляются и обновляются автоматически.

**Когда использовать**: Когда изменение состояния одного объекта требует обновления других объектов,
и вы не хотите, чтобы объекты были жестко связаны.

```python
class Observer:
    def update(self, message):
        pass

class ConcreteObserver(Observer):
    def update(self, message):
        print(f"Received message: {message}")

class Subject:
    def __init__(self):
        self._observers = []

    def add_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)

    def notify_observers(self, message):
        for observer in self._observers:
            observer.update(message)


subject = Subject()
subject.add_observer(ConcreteObserver())
subject.add_observer(ConcreteObserver())
subject.notify_observers("Hello Observers!")
# Received message: Hello Observers!
# Received message: Hello Observers!
```
""",
                "State (Состояние)": """
# State (Состояние)

**Описание**: Позволяет объекту изменять своё поведение в зависимости от внутреннего состояния, меняя свой класс.

**Когда использовать**: Когда объект может находиться в одном из нескольких состояний, и поведение объекта меняется в зависимости от его состояния.

```python
class State:
    def handle(self, context):
        pass

class ConcreteStateA(State):
    def handle(self, context):
        context.state = ConcreteStateB()
        print("Transition to ConcreteStateB")

class ConcreteStateB(State):
    def handle(self, context):
        context.state = ConcreteStateA()
        print("Transition to ConcreteStateA")

class Context:
    def __init__(self, state):
        self.state = state

    def request(self):
        self.state.handle(self)


context = Context(ConcreteStateA())
context.request()  # Transition to ConcreteStateB
context.request()  # Transition to ConcreteStateA
```
""",
                "Strategy (Стратегия)": """
# Strategy (Стратегия)

**Описание**: Определяет семейство алгоритмов, инкапсулирует их и делает их взаимозаменяемыми.

**Когда использовать**: Когда нужно выбрать один из нескольких алгоритмов на этапе выполнения программы.

```python
class Strategy:
    def execute(self, a, b):
        pass

class AddStrategy(Strategy):
    def execute(self, a, b):
        return a + b

class MultiplyStrategy(Strategy):
    def execute(self, a, b):
        return a * b

class Context:
    def __init__(self, strategy):
        self.strategy = strategy

    def execute_strategy(self, a, b):
        return self.strategy.execute(a, b)


context = Context(AddStrategy())
print(context.execute_strategy(5, 3))  # 8

context = Context(MultiplyStrategy())
print(context.execute_strategy(5, 3))  # 15
```
""",
                "Template Method (Шаблонный метод)": """
# Template Method (Шаблонный метод)

**Описание**: Определяет скелет алгоритма, позволяя подклассам переопределять некоторые шаги, не изменяя структуру алгоритма.

**Когда использовать**: Когда нужно задать общий алгоритм, но позволить подклассам изменять отдельные шаги.

```python
class AbstractClass:
    def template_method(self):
        self.step_one()
        self.step_two()

    def step_one(self):
        pass

    def step_two(self):
        pass

class ConcreteClass(AbstractClass):
    def step_one(self):
        print("Step One Implemented")

    def step_two(self):
        print("Step Two Implemented")


obj = ConcreteClass()
obj.template_method()
# Step One Implemented
# Step Two Implemented
```
""",
                "Visitor (Посетитель)": """
# Visitor (Посетитель)

**Описание**: Позволяет добавлять новые операции к объектам без изменения их классов.
Определяет операцию, которая может быть выполнена для каждого элемента структуры объектов.

**Когда использовать**: Когда нужно выполнять операции над элементами структуры объектов, не изменяя сами элементы.

```python
class Element:
    def accept(self, visitor):
        pass

class Visitor:
    def visit_concrete_element_a(self, element):
        pass

    def visit_concrete_element_b(self, element):
        pass

class ConcreteElementA(Element):
    def accept(self, visitor):
        visitor.visit_concrete_element_a(self)

class ConcreteElementB(Element):
    def accept(self, visitor):
        visitor.visit_concrete_element_b(self)

class ConcreteVisitor(Visitor):
    def visit_concrete_element_a(self, element):
        return "Visited ConcreteElementA"

    def visit_concrete_element_b(self, element):
        return "Visited ConcreteElementB"


element_a = ConcreteElementA()
element_b = ConcreteElementB()
visitor = ConcreteVisitor()

print(visitor.visit_concrete_element_a(element_a))  # Visited ConcreteElementA
print(visitor.visit_concrete_element_b(element_b))  # Visited ConcreteElementB
```

## Example

Предположим, у нас есть разные типы документов: PDFDocument и WordDocument.
Мы хотим добавить операцию экспорта в разные форматы (например, в HTML), не изменяя сами классы документов.

```python
from abc import ABC, abstractmethod


class Document(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass

class PDFDocument(Document):
    def accept(self, visitor):
        visitor.visit_pdf(self)

    def pdf_specific_operation(self):
        return "PDF content"

class WordDocument(Document):
    def accept(self, visitor):
        visitor.visit_word(self)

    def word_specific_operation(self):
        return "Word content"

class Visitor(ABC):
    @abstractmethod
    def visit_pdf(self, pdf_doc):
        pass

    @abstractmethod
    def visit_word(self, word_doc):
        pass

class ExportToHTMLVisitor(Visitor):
    def visit_pdf(self, pdf_doc):
        content = pdf_doc.pdf_specific_operation()
        print(f"Exporting PDF to HTML: {content}")

    def visit_word(self, word_doc):
        content = word_doc.word_specific_operation()
        print(f"Exporting Word to HTML: {content}")


pdf_doc = PDFDocument()
word_doc = WordDocument()

visitor = ExportToHTMLVisitor()

pdf_doc.accept(visitor)
word_doc.accept(visitor)
```


### Как это работает на практике

- **Минимальные изменения в классах объектов**: Единственное, что требуется добавить в классы, — это метод `accept`.
Это небольшое изменение открывает возможность для множества новых операций (посетителей). Все остальное остается неизменным.
Это ограничение паттерна: чтобы объект мог взаимодействовать с посетителем,
он должен поддерживать механизм "принятия" посетителя через метод `accept`.
- **Легкость добавления новых операций**: Если требуется добавить новую операцию, нужно просто создать нового посетителя,
реализующего эту операцию. Сами классы объектов при этом не меняются.
Это и есть суть паттерна `Visitor` — отделение алгоритма от структуры данных.

Это позволяет разделить ответственность: сами классы объектов отвечают за свои данные и базовое поведение, 
а все дополнительные операции выносятся в посетителей.
""",
            },
            "Антипаттерны": """
Антипаттерн — это распространенный подход к решению часто встречающихся проблем,
который может нанести больше вреда, чем пользы.

[https://ru.wikipedia.org/wiki/Антипаттерн](https://ru.wikipedia.org/wiki/Антипаттерн)
[https://habr.com/ru/companies/slurm/articles/706024/](https://habr.com/ru/companies/slurm/articles/706024/)


# Антипаттерны в объектно-ориентированном программировании

### Базовый класс-утилита (BaseBean)
Наследование функциональности из класса-утилиты вместо делегирования к нему.

### Anemic Domain Model
боязнь размещать логику в объектах предметной области.

### Вызов предка (Call super)
Для реализации прикладной функциональности методу класса-потомка требуется
в обязательном порядке вызывать те же методы класса-предка.

### Ошибка пустого подкласса (Empty subclass failure)
Создание класса (в Perl), который не проходит «проверку пустоты подкласса» («Empty Subclass Test»)
из-за различного поведения по сравнению с классом, который наследуется от него без изменений.

### Божественный объект (God object)
Концентрация слишком большого количества функций в одной части системы (классе).

### Объектная клоака (Object cesspool)
Переиспользование объектов, находящихся в непригодном для переиспользования состоянии.

### Полтергейст (Poltergeist)
Объекты, чьё единственное предназначение — передавать информацию другим объектам.

### Проблема йо-йо (Yo-yo problem)
Чрезмерная размытость сильно связанного кода (например, выполняемого по порядку) по иерархии классов.

### Одиночество (Singletonitis)
Неуместное использование паттерна одиночка.

### Френд-зона (Friend zone)
Неуместное использование дружественных классов и дружественных функций в языке C++.

### Каша из интерфейсов (Interface soup)
Объединение нескольких интерфейсов, разделенных согласно
принципу изоляции интерфейсов (Interface segregation), в один.

### Висящие концы
Интерфейс, большинство методов которого бессмысленны и реализуются «пустышками».

### Заглушка (Stub)
Попытка «натянуть» на объект уже имеющийся малоподходящий по смыслу интерфейс, вместо создания нового.


# Антипаттерны при написании кода

### Ненужная сложность (Accidental complexity)
Внесение ненужной сложности в решение.

### Действие на расстоянии (Action at a distance)
Неожиданное взаимодействие между широко разделёнными частями системы.

### Накопить и запустить (Accumulate and fire)
Установка параметров подпрограмм в наборе глобальных переменных.

### Слепая вера (Blind faith)
Недостаточная проверка корректности исправления ошибки или результата работы подпрограммы.

### Лодочный якорь (Boat anchor)
Сохранение более не используемой части системы.

### Активное ожидание (Busy spin, busy waiting)
Потребление ресурсов ЦПУ (процессорного времени) во время ожидания события,
обычно при помощи постоянно повторяемой проверки,
вместо того, чтобы использовать асинхронное программирование (к примеру, систему сообщений или событий).

### Кэширование ошибки (Caching failure)
Забывать сбросить флаг ошибки после её обработки.

### Воняющий подгузник (The Diaper Pattern Stinks)
Сброс флага ошибки без её обработки или передачи вышестоящему обработчику.

### Проверка типа вместо интерфейса (Checking type instead of membership, Checking type instead of interface)
Проверка того, что объект имеет специфический тип в то время, когда требуется только определённый интерфейс.

### Инерция кода (Code momentum)
Сверхограничение части системы путём постоянного подразумевания её поведения в других частях системы.

### Кодирование путём исключения (Coding by exception)
Добавление нового кода для поддержки каждого специального распознанного случая.

### Таинственный код (Cryptic code)
Использование аббревиатур вместо мнемоничных имён.

### Жёсткое кодирование (Hard code)
Внедрение предположений об окружении системы в слишком большом количестве точек её реализации.

### Мягкое кодирование (Soft code)
Патологическая боязнь жёсткого кодирования, приводящая к тому, что настраивается всё что угодно,
при этом конфигурирование системы само по себе превращается в программирование.

### Поток лавы (Lava flow)
Сохранение нежелательного (излишнего или низкокачественного) кода по причине того,
что его удаление слишком дорого или будет иметь непредсказуемые последствия.

### Волшебные числа (Magic numbers)
Использование числовых констант без объяснения их смысла.

### Процедурный код (Procedural code)
Когда другая парадигма является более подходящей.

### Спагетти-код (Spaghetti code, иногда «макароны»)
Код с чрезмерно запутанным порядком выполнения.

### Лазанья-код (Lasagnia code, или «лук» (onion))
Чрезмерное связывание между собой уровней абстракции,
приводящее к невозможности изменения одного уровня без изменения остальных.

### Равиоли-код (Ravioli code, или «пельмени»)
Объекты настолько «склеены» между собой, что практически не допускают рефакторинга.

### Мыльный пузырь (Soap bubble)
Объект, инициализированый мусором, максимально долго притворяется, что содержит какие-то данные.

### Мьютексный ад (Mutex hell)
Внедрение слишком большого количества объектов синхронизации между потоками.

### (Мета-)шаблонный рак (Template cancer)
Повсеместное использование шаблонов (в основном C++), в том числе там, где их использование не оправдано.
Это уменьшает понимание и сопровождение кода и замедляет компиляцию.


# Методологические антипаттерны

### Программирование методом копирования-вставки (Copy and paste programming)
Копирование (и лёгкая модификация) существующего кода вместо создания общих решений.

### Дефакторинг (De-Factoring)
Процесс уничтожения функциональности и замены её документацией.

### Золотой молоток (Golden hammer)
Сильная уверенность в том, что любимое решение универсально применимо.
Название происходит от поговорки «когда в руках молоток, все проблемы кажутся гвоздями».

### Фактор невероятности (Improbability factor)
Предположение о невозможности того, что сработает известная ошибка.

### Преждевременная оптимизация (Premature optimization)
Оптимизация на этапе проектирования сегмента кода, приводящая к его усложнению или искажению.

### Программирование методом подбора (Programming by permutation)
Подход к разработке программного обеспечения небольшими изменениями без понимания их смысла.

### Изобретение колеса/велосипеда (Reinventing the wheel)
Создание с нуля вместо использования хорошего готового решения.

### Изобретение квадратного колеса (Reinventing the square wheel)
Создание плохого решения, при условии, что уже существует известное решение лучше.

### Самоуничтожение (Self-destruction)
Фатальная ошибка либо нестандартное поведение программы, приводящая к отказу в обслуживании,
возникшая вследствие другой менее серьёзной ошибки. Например, при возникновении ошибки,
приложение начинает очень быстро и много писать в лог, вследствие чего заканчивается место
на жёстком диске быстрее, чем это обнаружит мониторинг.

### Два тоннеля
Вынесение новой функциональности в отдельное приложение вместо расширения уже имеющегося.
Чаще всего применяется, когда по каким-либо причинам (в основном, при нехватке времени либо нежелании менеджмента)
внесение изменений в уже имеющийся код требует больших затрат, чем создание нового.
При этом у клиента в конечном итоге работают два приложения,
запускаясь одновременно либо попеременно друг из друга.

### Коммит-убийца (Commit assasin)
Внесение отдельных изменений в систему контроля версий без проверки влияния их на другие части программы.
Как правило, после подобных коммитов работа коллектива парализуется
на время исправления проблем в местах, которые ранее работали безошибочно.

""",
        },
        "HTTP": {
            "HTTР": """HTTP
(Hypertext Transfer Protocol)
Протокол для передачи гипертекстовых документов, таких как веб-страницы.
HTTPS (HTTP Secure) - это расширение HTTP, которое использует шифрование
данных для безопасной передачи информации между сервером и клиентом.
Протокол HTTPS использует те же методы, что и протокол HTTP,
такие как GET, POST, PUT, DELETE и т. д.
Однако в отличие от HTTP, HTTPS использует шифрование данных
для защиты информации во время передачи.
""",
            "Requests": """
|        |            |
|--------|------------|
| GET    | Получение данных с сервера.<br>Не изменяют состояние сервера и обычно используются<br>для получения данных, не требующих аутентификации. |
| POST   | Отправки данных на сервер.<br>Используются для создания новых ресурсов или<br>изменения существующих ресурсов на сервере. |
| PUT    | Обновления ресурса на сервере.<br>Заменяет текущий ресурс на новый ресурс. |
| PATCH  | Изменяет существующий ресурс |
| DELETE | Удаления ресурса с сервера |
""",
            "Протоколы связи": """
|                                                                 |                 |
|-----------------------------------------------------------------|-----------------|
| HTTP (Hypertext Transfer Protocol)                              | Протокол передачи гипертекста, который используется<br>для передачи веб-страниц и другого контента между сервером и клиентом в Интернете.<br>HTTP использует методы запроса-ответа между клиентом и сервером, где клиент отправляет запрос на сервер,<br>а сервер отправляет ответ с запрошенной информацией.<br>HTTP также поддерживает кэширование, что позволяет уменьшить количество передаваемых данных и ускорить загрузку страниц.                                                                                                                                                                |
| HTTPS (Hypertext Transfer Protocol Secure)                      | Это безопасная версия HTTP, которая использует шифрование SSL/TLS для защиты передаваемых данных от перехвата и подделки.<br>HTTPS добавляет дополнительный уровень безопасности в сравнении с HTTP и является необходимым<br>для обеспечения безопасной передачи конфиденциальной информации,<br>такой как пароли, номера кредитных карт и другие личные данные.                                                                                                                                                                                                                                        |
| SMTP (Simple Mail Transfer Protocol)                            | Протокол передачи почты, который используется для отправки электронной почты между почтовыми серверами.<br>SMTP работает на уровне приложения в модели OSI и использует порт 25 для обмена данными.<br>SMTP использует методы запроса-ответа, где отправитель отправляет сообщение на сервер,<br>а сервер затем доставляет сообщение получателю.                                                                                                                                                                                                                                                         |
| POP3 (Post Office Protocol version 3)                           | Протокол приема почты, который используется для получения электронной почты с сервера на клиентское устройство.<br>POP3 работает на уровне приложения и использует порт 110 для обмена данными.<br>Когда клиентский компьютер подключается к почтовому серверу,<br>POP3 загружает все письма с сервера на устройство, а затем удаляет их с сервера.                                                                                                                                                                                                                                                      |
| IMAP (Internet Message Access Protocol)                         | Протокол доступа к электронной почте, который также используется для получения электронной почты с сервера<br>на клиентское устройство, но предоставляет более продвинутые функции,<br>такие как хранение писем на сервере и синхронизация между устройствами.<br>IMAP работает на уровне приложения и использует порт 143 для обмена данными.<br>IMAP позволяет клиентам просматривать только заголовки писем или загружать их содержимое полностью,<br>а также удалять письма на сервере, не загружая их на устройство.                                                                                |
| TCP/IP<br>(Transmission Control Protocol/<br>Internet Protocol) | Это семейство протоколов, используемых для обмена данными в сети Интернет.<br>TCP отвечает за надежную передачу данных между приложениями,<br>установление и управление соединениями, а также контроль потока данных.<br>IP же отвечает за маршрутизацию пакетов данных между устройствами в сети,<br>идентификацию устройств, управление адресами и т.д.<br>TCP/IP также включает другие протоколы, такие как DNS (Domain Name System),<br>который переводит доменные имена в IP-адреса, и DHCP (Dynamic Host Configuration Protocol),<br>который автоматически назначает IP-адреса устройствам в сети. |
| FTP (File Transfer Protocol)                                    | Протокол передачи файлов, который используется для передачи файлов между компьютерами в сети.<br>FTP работает на уровне приложения и использует порт 21 для установки соединения и передачи команд,<br>а также порт 20 для передачи данных.<br>FTP позволяет пользователям загружать и скачивать файлы с сервера,<br>создавать и удалять директории и управлять правами доступа к файлам.                                                                                                                                                                                                                |
| SSH (Secure Shell)                                              | Протокол безопасной удаленной работы с командной строкой, который используется<br>для управления удаленными компьютерами и серверами.<br>SSH работает на уровне приложения и использует порт 22 для обмена данными.<br>SSH обеспечивает защиту от перехвата и подделки данных с помощью шифрования,<br>а также обеспечивает возможность удаленной аутентификации и управления устройством.                                                                                                                                                                                                               |
| DNS (Domain Name System)                                        | Протокол, который переводит доменные имена в IP-адреса и обратно.<br>DNS работает на уровне приложения и использует порт 53 для обмена данными.<br>DNS предоставляет возможность использования доменных имен для доступа к ресурсам<br>в сети вместо использования IP-адресов, что упрощает и облегчает работу сети.                                                                                                                                                                                                                                                                                     |
| SNMP (Simple Network Management Protocol)                       | Протокол управления сетью, который используется для мониторинга и управления сетевыми устройствами,<br>такими как маршрутизаторы, коммутаторы, серверы и т.д.<br>SNMP работает на уровне приложения и использует порты 161 и 162 для обмена данными.<br>SNMP позволяет администраторам мониторить статус устройств, настраивать их параметры и диагностировать проблемы в сети.                                                                                                                                                                                                                          |


""",
        },
        "Парадигмы": {
            "Императивная": """
# КАК

Разработчик пишет для компьютера инструкции, которым тот следует.

Виды программирования относятся к императивной парадигме:
процедурное структурное аспектно-ориентированное объектно-ориентированное и другие.

Пример
Сложи два числа;
Если а, то сделай б, а иначе сделай в;
Отправь запрос на сервер;
Открой файл;
Выведи строку.

C# - Разработчик говорит как это можно получить (императивный)

```C#
int[] N = new int[] { 5, 1, 3, 9, 12, 583, 998, 7538, 72, 53, 71, 85, 7, 2, 9 };
List<int> nums = new List<int>();

for (int i = 0; i < N.Length; i++) {
    if (N[i] > 3 && N[i] < 100){
        nums.Add(N[i]);
    }
}

int[] N2 = nums.ToArray();
```

Императивное программирование даёт больше свободы, поэтому его чаще используют
в творческих областях, особенно там, где важен порядок выполняемых действий.
""",
            "Декларативная": """
# ЧТО

Разработчик описывает проблему и ожидаемый результат, но не пишет никаких инструкций.

В декларативном программировании отсутствуют переменные,
состояние и прочие понятия, которые свойственны императивной парадигме.

К декларативной парадигме относятся функциональное и логическое программирование.

Пример
Дано:    5, 1, 3, 9, 12, 583, 998, 7538, 72, 53, 71, 85, 7, 2, 9
Задача:  Получить из этого массива все числа, которые больше 3, но меньше 100.
Решение: Получить из массива N все числа, которые больше 3 и меньше 100.

SQL - Разработчик говорит, что ему нужно (декларативный)

```sql
SELECT num FROM N WHERE num > 3 AND num < 100;
```
Декларативное программирование — это обёртка для императивного.
Не подходит для задач, для решения которых важно иметь доступ к состоянию программы.
Например, если нужно проверить, нажата ли кнопка или поставлена ли галочка в чекбокс.
""",
        },
        "ip": """
IP-адреса делятся на 5 классов

`A`, `B` и `C` — это классы коммерческой адресации.
`D` – для многоадресных рассылок.
`E` – для экспериментов.

> Класс А: 1.0.0.0 — 126.0.0.0, маска 255.0.0.0
> Класс В: 128.0.0.0 — 191.255.0.0, маска 255.255.0.0
> Класс С: 192.0.0.0 — 223.255.255.0, маска 255.255.255.0
> Класс D: 224.0.0.0 — 239.255.255.255, маска 255.255.255.255
> Класс Е: 240.0.0.0 — 247.255.255.255, маска 255.255.255.255

IP бывают **белые и серые** (или публичные и частные).
**Публичным IP адресом** называется IP адрес, который используется для выхода в Интернет.
Адреса, используемые в локальных сетях, относят к частным.
Частные IP не маршрутизируются в Интернете.

### Частные IP адреса

| Класс | Частные сети            | Маска подсети | Диапазон адресов              |
|-------|-------------------------|---------------|-------------------------------|
| A     | 10.0.0.0                | 255.0.0.0     | 10.0.0.0 - 10.255.255.255     |
| B     | 172.16.0.0 - 172.31.0.0 | 255.240.0.0   | 172.16.0.0 - 172.31.255.255   |
| C     | 192.168.0.0             | 255.255.0.0   | 192.168.0.0 - 192.168.255.255 |

**Маска подсети** — битовая маска, определяющая, какая часть IP-адреса узла сети относится к адресу сети,
а какая — к адресу самого узла в этой сети.

У всех IP адресов есть две части **сеть** и **узел**.
**Сеть** – это та часть IP, которая не меняется во всей сети и все адреса устройств начинаются именно с номера сети.
**Узел** – это изменяющаяся часть IP. Каждое устройство имеет свой уникальный адрес в сети, он называется узлом.

Маску принято записывать двумя способами: `префиксным` и `десятичным`.
Например, маска частной подсети `A` выглядит в десятичной записи как `255.0.0.0`,
но не всегда удобно пользоваться десятичной записью при составлении схемы сети.
Легче записать маску как префикс, то есть `/8`.

![Таблица_масок_подсети.png](General/Таблица_масок_подсети.png)

Адрес `127.0.0.0` – `127.255.255.255` (**loopback** – петля на себя).
Данная сеть нужна для диагностики.

`169.254.0.0` – `169.254.255.255` (APIPA – Automatic Private IP Addressing).
Механизм «придумывания» IP адреса.
Служба APIPA генерирует IP адреса для начала работы с сетью.

[https://habr.com/ru/articles/350878/](https://habr.com/ru/articles/350878/)
""",
        "ООП": """
|              |                                                                                                                          |
|--------------|--------------------------------------------------------------------------------------------------------------------------|
| Инкапсуляция | предназначена для изоляции контрактных обязательств абстракции<br>(протокол/интерфейс) от их реализации (public/private) |
| Наследование | это когда тип данных может наследовать данные и<br>функциональность некоторого существующего типа                        |
| Полиморфизм  | способность функции обрабатывать данные разных типов                                                                     |
| Абстракция   | это процесс упрощения или скрытия сложной реальности,<br>чтобы сосредоточиться на наиболее важных аспектах.              |

В программировании, абстракция означает создание общей концепции, которая скрывает детали реализации, 
но предоставляет только необходимый набор функций и методов для взаимодействия с объектом. 
В итоге, абстракция помогает создавать более понятный, гибкий и расширяемый код.


**Абстракция** - это процесс создания абстрактных классов и интерфейсов для представления концептуальных объектов и их взаимодействия в программе. 
Абстракция позволяет скрыть реализацию объектов и предоставить только необходимый набор свойств и методов для их использования. 
Это упрощает процесс разработки и поддержки программы, улучшает ее читаемость и расширяемость.

Например, в программе для управления банковским счетом можно создать абстрактный класс "Счет" со свойствами "номер счета" и "баланс", 
а также методами для внесения и снятия денег. 
Конкретные типы счетов, такие как "текущий счет" или "депозитный счет", могут быть созданы на основе этого абстрактного класса 
и расширены своими дополнительными свойствами и методами.
""",
        "Networking Protocols": """
|                  |                                                            |                                |
|------------------|------------------------------------------------------------|--------------------------------|
| FTP              | File Transfer Protocol                                     | Port 21                        |
| SSH              | Secure Shell                                               | Port 22                        |
| Teinet           | Port 23                                                    |                                |
| SMTP             | Simple Mail Transfer Protocol                              | Port 25                        |
| DNS              | Domain Naming System (or Service)                          | Port 53                        |
| HTTP             | Hypertext Transfer Protocol                                | Port 80                        |
| POP3             | Post Office Protocol                                       | Port 110                       |
| IMAP             | Internet Message Access Protocol                           | Port 143                       |
| HTTPS            | HTTP Secure                                                | Port 443                       |
| RDP              | Remote Desktop Protocol                                    | Port 3389                      |
| TCP              | Transmission Control Protocol                              |                                |
| UDP              | User Datagram Protocol                                     |                                |
| ARP              | Address Resolution Protocol                                |                                |
| RARP             | Reverse ARP                                                |                                |
| DHCP             | Dynamic Host Configuration Protocol                        | Server Port 67, Client Port 68 |
| MTP              | Media Transfert Protocol                                   |                                |
| SFTP             | Secure File Transfer Protocol                              |                                |
| SSL              | Secure Socket Layer                                        |                                |
| TLS              | Transport Layer Security                                   |                                |
| E6               | Ethernet globalization protocols                           |                                |
| NTP              | Network time protocol                                      |                                |
| PPP              | Point to Point Protocol                                    |                                |
| NNTP             | Network News Transfer Protocol                             |                                |
| QOTD             | Quote Of The Day                                           |                                |
| Bitcoin Protocol | Protocol for Bitcoin transactions and transfers on the web |                                |
| ICMP             | Internet Control Message Protocol                          |                                |
| IGMP             | Internet Group Management Protocol                         |                                |
| GGP              | Gateway-to-Gateway Protocol                                |                                |
| IP-in-IP         | IP in IP (encapsulation)                                   |                                |
""",
        "Interpreter Compiler": """
|               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|---------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Интерпретатор | Программа, которая читает и исполняет команды на другом языке программирования.<br>Он принимает код на этом языке, анализирует его, и выполняет инструкции,<br>указанные в коде.<br>Интерпретаторы часто используются для языков программирования, которые<br>поддерживают интерпретацию, таких как `Python`, `Ruby` и `JavaScript`.<br>Они также могут быть использованы для языков, которые обычно компилируются,<br>таких как `C++` или `C#`, чтобы обеспечить более быструю отладку и тестирование кода                                                                                       |
| Компилятор    | Программа, которая преобразует код на одном языке программирования в машинный<br>язык, который может быть понят целевой машиной.<br>Компилятор анализирует код, выполняет необходимые преобразования, и создает<br>исполняемый файл, который содержит машинный код, готовый к выполнению.<br>Компиляторы часто используются для языков программирования, которые требуют<br>компиляции перед выполнением, таких как `C++` или `C#`. Они также могут быть<br>использованы для языков, которые обычно интерпретируются, таких как<br>`Python` и `Ruby`, чтобы создать более быстро выполняемый код. |
""",
        "sync async": """
|               |                                                                                                                                                                                                                                                                                    |
|---------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Синхронность  | Означает, что программа выполняет одну задачу за раз, поэтому она не может<br>выполнять несколько задач одновременно. Это означает, что если одна задача<br>занимает много времени, то все остальные задачи будут ждать,<br>пока эта задача не будет завершена.                    |
| Асинхронность | Означает, что программа может выполнять несколько задач одновременно.<br>Она может ожидать ответа от сервера и продолжать выполнение других задач<br>в то время, как она ждет. Это позволяет программе эффективно использовать<br>ресурсы и обрабатывать больше задач за один раз. |

[https://habr.com/ru/post/421625](https://habr.com/ru/post/421625)
""",
        "Угрозы безопасности": """
### Cross-Site Scripting (XSS)
XSS-атаки позволяют злоумышленникам внедрять вредоносный JavaScript-код
на страницы сайта, который затем выполняется в браузерах пользователей.
Это может использоваться для кражи данных, таких как cookie-файлы, сессии или для проведения фишинговых атак.
**Экранирование данных!**

|     |          |
|----:|:---------|
| `<` | `&lt;`   |
| `>` | `&gt;`   |
| `&` | `&amp;`  |
| `"` | `&quot;` |
| `'` | `&#39;`  |

### Cross-Site Request Forgery (CSRF)
CSRF-атаки заставляют пользователя выполнять нежелательные действия на сайте,
на который он в данный момент авторизован, без его ведома.
Это может включать изменение пароля, перевод средств или выполнение других действий от имени пользователя.

**Использование CSRF-токенов**
Встраивайте уникальный токен в каждую форму или запрос, который необходимо проверить на стороне сервера.
Токен должен быть уникален для каждого сеанса или формы и должен проверяться при обработке запросов.
""",
        "Google Search": """
| Синтаксис     | Описание                                                   | Пример использования                            |
|---------------|------------------------------------------------------------|-------------------------------------------------|
| `""`          | Поиск точного совпадения                                   | `"лучшие рестораны Москвы"`                     |
| `-`           | Исключение слова или фразы                                 | `рецепты пасты -томат или -"томат"`             |
| `site:`       | Поиск на определенном сайте                                | `вакансии site:example.com`                     |
| `intitle:`    | Поиск слов в заголовках                                    | `intitle:"как сделать сайт"`                    |
| `filetype:`   | Поиск файлов определенного типа                            | `резюме filetype:pdf`                           |
| `OR`          | Поиск по нескольким вариантам слов или фраз                | `"кошки" OR "собаки"`                           |
| `*`           | Замена неизвестных или пропущенных слов                    | `"лучший * в мире"`                             |
| `..`          | Поиск в диапазоне чисел                                    | `смартфоны $300..$500`                          |
| `define:`     | Быстрый поиск определения слова                            | `define:алгоритм`                               |
| `related:`    | Поиск сайтов, похожих на указанный                         | `related:nytimes.com`                           |
| `cache:`      | Просмотр кэша страницы                                     | `cache:example.com`                             |
| `inurl:`      | Поиск слов в URL                                           | `inurl:блог`                                    |
| `allintitle:` | Поиск всех слов в заголовке                                | `allintitle:как создать блог`                   |
| `around(X)`   | Поиск слов, находящихся на расстоянии X слов друг от друга | `"искусственный интеллект" AROUND(5) "будущее"` |
| `info:`       | Поиск информации о сайте                                   | `info:example.com`                              |
| `weather:`    | Поиск погоды в конкретном месте                            | `weather:Москва`                                |
| `stocks:`     | Поиск информации о котировках акций                        | `stocks:AAPL`                                   |
| `map:`        | Поиск карты местности                                      | `map:Париж`                                     |
| `movie:`      | Поиск информации о фильмах                                 | `movie:Inception`                               |

""",
        "Encodings": """
![encoding.png](General/encoding.png)
""",
    },
    "Languages": {
        "Python": {
            "Libraries": {
                "index": """
# =={color:#b82e2e;background-color: inherit;}Внимание! Все шпаргалки сгенерированы с помощью <b><u>ChatGPT 3.5</u></b>==

<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="101" height="20" role="img" aria-label="ChatGPT: 3.5"><title>ChatGPT: 3.5</title><linearGradient id="s" x2="0" y2="100%"><stop offset="0" stop-color="#bbb" stop-opacity=".1"/><stop offset="1" stop-opacity=".1"/></linearGradient><clipPath id="r"><rect width="101" height="20" rx="3" fill="#fff"/></clipPath><g clip-path="url(#r)"><rect width="74" height="20" fill="#555"/><rect x="74" width="27" height="20" fill="#007ec6"/><rect width="101" height="20" fill="url(#s)"/></g><g fill="#fff" text-anchor="middle" font-family="Verdana,Geneva,DejaVu Sans,sans-serif" text-rendering="geometricPrecision" font-size="110"><image x="5" y="3" width="14" height="14" xlink:href="data:image/svg+xml;base64,PHN2ZyBmaWxsPSJ3aGl0ZXNtb2tlIiByb2xlPSJpbWciIHZpZXdCb3g9IjAgMCAyNCAyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48dGl0bGU+T3BlbkFJPC90aXRsZT48cGF0aCBkPSJNMjIuMjgxOSA5LjgyMTFhNS45ODQ3IDUuOTg0NyAwIDAgMC0uNTE1Ny00LjkxMDggNi4wNDYyIDYuMDQ2MiAwIDAgMC02LjUwOTgtMi45QTYuMDY1MSA2LjA2NTEgMCAwIDAgNC45ODA3IDQuMTgxOGE1Ljk4NDcgNS45ODQ3IDAgMCAwLTMuOTk3NyAyLjkgNi4wNDYyIDYuMDQ2MiAwIDAgMCAuNzQyNyA3LjA5NjYgNS45OCA1Ljk4IDAgMCAwIC41MTEgNC45MTA3IDYuMDUxIDYuMDUxIDAgMCAwIDYuNTE0NiAyLjkwMDFBNS45ODQ3IDUuOTg0NyAwIDAgMCAxMy4yNTk5IDI0YTYuMDU1NyA2LjA1NTcgMCAwIDAgNS43NzE4LTQuMjA1OCA1Ljk4OTQgNS45ODk0IDAgMCAwIDMuOTk3Ny0yLjkwMDEgNi4wNTU3IDYuMDU1NyAwIDAgMC0uNzQ3NS03LjA3Mjl6bS05LjAyMiAxMi42MDgxYTQuNDc1NSA0LjQ3NTUgMCAwIDEtMi44NzY0LTEuMDQwOGwuMTQxOS0uMDgwNCA0Ljc3ODMtMi43NTgyYS43OTQ4Ljc5NDggMCAwIDAgLjM5MjctLjY4MTN2LTYuNzM2OWwyLjAyIDEuMTY4NmEuMDcxLjA3MSAwIDAgMSAuMDM4LjA1MnY1LjU4MjZhNC41MDQgNC41MDQgMCAwIDEtNC40OTQ1IDQuNDk0NHptLTkuNjYwNy00LjEyNTRhNC40NzA4IDQuNDcwOCAwIDAgMS0uNTM0Ni0zLjAxMzdsLjE0Mi4wODUyIDQuNzgzIDIuNzU4MmEuNzcxMi43NzEyIDAgMCAwIC43ODA2IDBsNS44NDI4LTMuMzY4NXYyLjMzMjRhLjA4MDQuMDgwNCAwIDAgMS0uMDMzMi4wNjE1TDkuNzQgMTkuOTUwMmE0LjQ5OTIgNC40OTkyIDAgMCAxLTYuMTQwOC0xLjY0NjR6TTIuMzQwOCA3Ljg5NTZhNC40ODUgNC40ODUgMCAwIDEgMi4zNjU1LTEuOTcyOFYxMS42YS43NjY0Ljc2NjQgMCAwIDAgLjM4NzkuNjc2NWw1LjgxNDQgMy4zNTQzLTIuMDIwMSAxLjE2ODVhLjA3NTcuMDc1NyAwIDAgMS0uMDcxIDBsLTQuODMwMy0yLjc4NjVBNC41MDQgNC41MDQgMCAwIDEgMi4zNDA4IDcuODcyem0xNi41OTYzIDMuODU1OEwxMy4xMDM4IDguMzY0IDE1LjExOTIgNy4yYS4wNzU3LjA3NTcgMCAwIDEgLjA3MSAwbDQuODMwMyAyLjc5MTNhNC40OTQ0IDQuNDk0NCAwIDAgMS0uNjc2NSA4LjEwNDJ2LTUuNjc3MmEuNzkuNzkgMCAwIDAtLjQwNy0uNjY3em0yLjAxMDctMy4wMjMxbC0uMTQyLS4wODUyLTQuNzczNS0yLjc4MThhLjc3NTkuNzc1OSAwIDAgMC0uNzg1NCAwTDkuNDA5IDkuMjI5N1Y2Ljg5NzRhLjA2NjIuMDY2MiAwIDAgMSAuMDI4NC0uMDYxNWw0LjgzMDMtMi43ODY2YTQuNDk5MiA0LjQ5OTIgMCAwIDEgNi42ODAyIDQuNjZ6TTguMzA2NSAxMi44NjNsLTIuMDItMS4xNjM4YS4wODA0LjA4MDQgMCAwIDEtLjAzOC0uMDU2N1Y2LjA3NDJhNC40OTkyIDQuNDk5MiAwIDAgMSA3LjM3NTctMy40NTM3bC0uMTQyLjA4MDVMOC43MDQgNS40NTlhLjc5NDguNzk0OCAwIDAgMC0uMzkyNy42ODEzem0xLjA5NzYtMi4zNjU0bDIuNjAyLTEuNDk5OCAyLjYwNjkgMS40OTk4djIuOTk5NGwtMi41OTc0IDEuNDk5Ny0yLjYwNjctMS40OTk3WiIvPjwvc3ZnPg=="/><text aria-hidden="true" x="465" y="150" fill="#010101" fill-opacity=".3" transform="scale(.1)" textLength="470">ChatGPT</text><text x="465" y="140" transform="scale(.1)" fill="#fff" textLength="470">ChatGPT</text><text aria-hidden="true" x="865" y="150" fill="#010101" fill-opacity=".3" transform="scale(.1)" textLength="170">3.5</text><text x="865" y="140" transform="scale(.1)" fill="#fff" textLength="170">3.5</text></g></svg>

<!--
https://img.shields.io/badge/ChatGPT-3.5-blue?logo=openai
-->
""",
                "System": {
                    "os": {
                        "index": r"""
# Работа с файлами и директориями

| Функция/Атрибут                     | Описание                                                                                            |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| `os.listdir(".")`                   | Возвращает список файлов и директорий в указанном каталоге.                                         |
| `os.scandir(path=".")`              | Возвращает итератор `DirEntry`, который предоставляет информацию<br>о файлах и директориях в директории `path`.<br>Более выгодный аналог `os.listdir` |
| `os.walk(".")`                      | Рекурсивно обходит файлы в дереве директорий                                                        |
| `os.getcwd()`                       | Возвращает текущий рабочий каталог                                                                  |
| `os.chdir(path)`                    | Изменяет текущий рабочий каталог на указанный                                                       |
| `os.mkdir(path, mode=0o777)`        | Создает новую директорию с указанным путем и правами доступа                                        |
| `os.makedirs(path, exist_ok=True)`  | Рекурсивно создает директории, включая промежуточные                                                |
| `os.removedirs(path)`               | Удаляет директории рекурсивно.                                                                      |
| `os.remove(path)`                   | Удаляет файл по указанному пути                                                                     |
| `os.rmdir(path)`                    | Удаляет пустую директорию                                                                           |
| `os.rename(src, dst)`               | Переименовывает файл или директорию                                                                 |
| `os.replace(src, dst)`              | Перемещает файл или директорию на новое место. Если целевой путь существует, он будет заменен       |
| `os.urandom(n)`                     | Возвращает `n` байт случайных данных, пригодных для использования в криптографии.                   |
| `os.unlink(path)`                   | Удаляет файл по указанному пути (аналог `os.remove`).                                               |
| `os.symlink(src, dst)`              | Создает символическую ссылку на файл или директорию (только Unix)                                   |
| `os.stat(path)`                     | [[Languages/Python/Libraries/System/os/os.stat.md]] Возвращает информацию о пути (например, размер, время последней модификации).                |
| `os.lstat(path)`                    | То же, что и `os.stat`, но не разыменовывает символические ссылки                                   |
| `os.path`                           | [[Languages/Python/Libraries/System/os/os.path.md]] Содержит функции для работы с путями, такие как `join`, `split`, `isfile`, `isdir` |

# Управление процессами

| Функция/Атрибут            | Описание                                                                                                                                           |
|----------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| `os.system(command)`       | Выполняет команду в оболочке и возвращает код завершения                                                                                           |
| `os.popen(command)`        | Выполняет команду в оболочке и возвращает объект файла, связанный с потоком вывода                                                                 |
| `os.kill(pid, sig)`        | Отправляет сигнал процессу с указанным идентификатором (PID) и [[Languages/Python/Libraries/System/signal.md]]<br>`os.kill(12345, signal.SIGTERM)` |
| `os._exit(n)`              | Немедленно завершает выполнение текущего процесса с указанным кодом возврата                                                                       |
| `os.waitpid(pid, options)` | Ожидает завершения процесса с указанным идентификатором (PID) и возвращает его код завершения и статус                                             |
| `os.fork()`                | Создает новый процесс путем форкинга текущего (только для Unix)                                                                                    |
| `os.execv(path, args)`     | Заменяет текущий процесс новым процессом, указанным в path                                                                                         |
| `os.abort()`               | Немедленно завершает процесс сгенерировав сигнатуру `SIGABRT`                                                                                      |
| `os.getpid()`             | Возвращает идентификатор текущего процесса                                                                                                          |
| `os.getppid()`            | Возвращает идентификатор родительского процесса                                                                                                     |

# Работа с файловыми дескрипторами

| Функция/Атрибут                    | Описание                                                                                                                    |
|------------------------------------|-----------------------------------------------------------------------------------------------------------------------------|
| `os.open(path, flags, mode=0o777)` | Открывает файл и возвращает файловый дескриптор. `flags` определяет режим открытия (например, `os.O_RDONLY`, `os.O_WRONLY`) |
| `os.close(fd)`                     | Закрывает файловый дескриптор `fd`                                                                                          |
| `os.read(fd, n)`                   | Читает до `n` байт из файла, связанного с файловым дескриптором `fd`                                                        |
| `os.write(fd, str)`                | Записывает строку в файл, связанный с файловым дескриптором `fd`                                                            |
| `os.lseek(fd, pos, how)`           | Перемещает указатель чтения/записи в файл, связанный с файловым дескриптором `fd`. `how` определяет начало перемещения      |
| `os.fsync(fd)`                     | Принудительно записывает все изменения, сделанные в файле, связанный с файловым дескриптором `fd`                           |
| `os.dup(fd)`                       | Дублирует файловый дескриптор `fd`                                                                                          |
| `os.dup2(fd, fd2)`                 | Дублирует файловый дескриптор `fd` в `fd2`                                                                                  |

# Функции для работы с файловыми системами

| Функция                    | Описание                                                     |
|----------------------------|--------------------------------------------------------------|
| `os.fsencode("filename")`  | Кодирует имя файла в системную кодировку                     |
| `os.fsdecode(b"filename")` | Декодирует имя файла из системной кодировки                  |
| `os.get_exec_path()`       | Возвращает список путей для поиска исполняемых файлов        |
| `os.fdopen(fd, mode)`      | Открывает файловый объект, связанный с файловым дескриптором |

# Атрибуты, связанные с путями и разделителями

| Атрибут      | Описание                                                                                                             |
|--------------|----------------------------------------------------------------------------------------------------------------------|
| `os.altsep`  | Альтернативный разделитель пути. Используется, если он поддерживается ОС. В Windows это `/` вместо `\`               |
| `os.curdir`  | Строка, представляющая текущую директорию. Обычно это `.`                                                            |
| `os.pardir`  | Строка, представляющая родительскую директорию. Обычно это `..`                                                      |
| `os.sep`     | Строка, представляющая разделитель пути, используемый в операционной системе. В Windows это `\`, в Unix — `/`        |
| `os.pathsep` | Строка, разделяющая компоненты в переменных среды, таких как `PATH`. В Windows это `;`, в Unix — `:`                 |
| `os.linesep` | Строка, представляющая разделитель строк, используемый в операционной системе. В Windows это `\r\n`, в Unix — `\n`   |
| `os.defpath` | Стандартный `PATH`, используемый если переменная окружения `PATH` не установлена                                     |
| `os.extsep`  | Разделитель расширения файлов. В большинстве ОС это `.`                                                              |
| `os.devnull` | Путь к специальному файлу, который отбрасывает все записанные в него данные (`/dev/null` на UNIX и `NUL` на Windows) |

# Информация о системе и среде выполнения

| Атрибут/Функция                | Описание                                                                                   |
|--------------------------------|--------------------------------------------------------------------------------------------|
| `os.name`                      | Имя операционной системы. Например, `posix` для Unix-подобных систем, `nt` для Windows     |
| `os.getenv(key, default=None)` | Возвращает значение переменной окружения или значение по умолчанию                         |
| `os.environ`                   | Словарь, содержащий переменные окружения                                                   |
| `os.getlogin()`                | Возвращает имя пользователя, вошедшего в систему                                           |
| `os.getpid()`                  | Возвращает идентификатор текущего процесса                                                 |
| `os.getppid()`                 | Возвращает идентификатор родительского процесса                                            |
| `os.cpu_count()`               | Возвращает количество процессоров в системе                                                |
| `os.uname()`                   | Возвращает информацию о системе, такую как имя системы, имя узла и версию ОС (только Unix) |
| `os.putenv(key, value)`        | Устанавливает значение переменной окружения **(не рекомендуется)**                         |
| `os.unsetenv(key)`             | Удаляет переменную окружения **(не рекомендуется)**                                        |

# Константы для работы с правами доступа и процессами

| Константа          | Описание                                                                                                 |
|--------------------|----------------------------------------------------------------------------------------------------------|
| `os.F_OK`          | Проверка на существование файла (используется в `os.access`)                                             |
| `os.R_OK`          | Проверка на возможность чтения файла (используется в `os.access`)                                        |
| `os.W_OK`          | Проверка на возможность записи в файл (используется в `os.access`)                                       |
| `os.X_OK`          | Проверка на возможность выполнения файла (используется в `os.access`)                                    |
| `os.EX_OK`         | Статус выхода для успешного выполнения команды (обычно 0)                                                |
| `os.O_RDONLY`      | Открытие файла только для чтения                                                                         |
| `os.O_WRONLY`      | Открытие файла только для записи                                                                         |
| `os.O_RDWR`        | Открытие файла для чтения и записи                                                                       |
| `os.O_CREAT`       | Создание файла, если он не существует                                                                    |
| `os.O_EXCL`        | Используется с `O_CREAT`, чтобы убедиться, что операция создания не завершится, если файл уже существует |
| `os.O_TRUNC`       | Очищает файл при его открытии, если он существует.                                                       |
| `os.O_APPEND`      | Добавление данных в конец файла                                                                          |
| `os.O_BINARY`      | Открытие файла в бинарном режиме (Windows)                                                               |
| `os.O_TEXT`        | Открытие файла в текстовом режиме (Windows)                                                              |
| `os.O_TEMPORARY`   | Открытие временного файла (Windows)                                                                      |
| `os.O_SHORT_LIVED` | Указание, что файл будет существовать недолго (Windows)                                                  |
| `os.O_SEQUENTIAL`  | Указание, что файл будет читаться последовательно (Windows)                                              |
| `os.O_RANDOM`      | Указание, что файл будет читаться в произвольном порядке (Windows)                                       |
| `os.P_NOWAIT`      | Дочерний процесс запускается, но родительский процесс продолжает выполнение (используется в `os.spawnv`) |
| `os.P_WAIT`        | Родительский процесс ожидает завершения дочернего процесса (используется в `os.spawnv`)                  |
| `os.P_DETACH`      | Дочерний процесс отделяется от родителя и не может получить доступ к его оконному интерфейсу (Windows)   |

# Управление файловыми дескрипторами

| Переменная    | Описание                                            |
|---------------|-----------------------------------------------------|
| `os.SEEK_SET` | Смещение для начала файла (значение `0`)            |
| `os.SEEK_CUR` | Смещение для текущей позиции в файле (значение `1`) |
| `os.SEEK_END` | Смещение для конца файла (значение `2`)             |

## Примеры использования

### Получение списка всех поддиректорий в директории:
```python
import os

print([f.path for f in os.scandir("my_dir") if f.is_dir()])
```

### Работа с файловыми путями
```pycon
>>> import os
>>>
>>> path = "/path/to/file.txt"
>>> print("Базовое имя файла:", os.path.basename(path))
Базовое имя файла: file.txt
>>> print("Директория:", os.path.dirname(path))
Директория: /path/to
>>> print("Существует ли файл:", os.path.exists(path))
Существует ли файл: False
```

### Работа с файлами
```python
import os

fd = os.open("example.txt", os.O_CREAT | os.O_WRONLY)
os.write(fd, b"Hello, World!")
os.close(fd)
```

### Чтение и запись через файловый дескриптор
```python
import os

fd = os.open("file.txt", os.O_RDWR | os.O_CREAT)
os.write(fd, b"Hello, World!")
os.lseek(fd, 0, os.SEEK_SET)
print(os.read(fd, 12))
os.close(fd)
```

### Выполнение системной команды и получение результата
```python
import os

stream = os.popen("ls")
output = stream.read()
print(output)
```

### Получение случайных данных
```pycon
>>> import os
>>>
>>> random_bytes = os.urandom(16)
>>> print("Случайные байты:", random_bytes)
Случайные байты: b"U\x1c\x9a\xec\x80E!\xc2\xdaR\x03\xab\xb8\x19\xe0\xa4"
```

```python
import os

with os.scandir("directory") as it:
    for entry in it:
        print(entry.name, entry.is_file(), entry.is_dir())
```

### Выполнение команды в оболочке
```python
import os

os.system("echo Hello, World!")
```

### Работа с путями
```python
import os

print("Разделитель путей:", os.sep)
print("Разделитель расширений:", os.extsep)
print("Путь к devnull:", os.devnull)
```

### Создание и удаление директорий
```python
import os

os.makedirs("example_dir/subdir")
os.removedirs("example_dir/subdir")
```

# Полезные ссылки
- [Официальная документация](https://docs.python.org/3/library/os.html)
- [Real Python - How to Use Python’s os and subprocess Modules](https://realpython.com/python-os-module/)
- [Real Python - Working with Files in Python](https://realpython.com/working-with-files-in-python/)

""",
                        "os.path": """

| Функция/Метод                | Описание                                                             | Пример                                   |
|------------------------------|----------------------------------------------------------------------|------------------------------------------|
| `os.path.basename(path)`     | Возвращает имя файла из пути.                                        | `os.path.basename("/path/to/file.txt")`  |
| `os.path.dirname(path)`      | Возвращает путь к директории без имени файла.                        | `os.path.dirname("/path/to/file.txt")`   |
| `os.path.split(path)`        | Разделяет путь на кортеж `(dirname, basename)`.                      | `os.path.split("/path/to/file.txt")`     |
| `os.path.splitext(path)`     | Разделяет путь на кортеж `(root, ext)` с корнем и расширением файла. | `os.path.splitext("/path/to/file.txt")`  |
| `os.path.join(path, *paths)` | Соединяет компоненты пути в единый путь.                             | `os.path.join("path", "to", "file.txt")` |
| `os.path.abspath(path)`      | Преобразует путь в абсолютный путь.                                  | `os.path.abspath("file.txt")`            |
| `os.path.realpath(path)`     | Возвращает канонический путь, учитывая символические ссылки.         | `os.path.realpath("symlink")`            |
| `os.path.exists(path)`       | Проверяет, существует ли путь.                                       | `os.path.exists("file.txt")`             |
| `os.path.isfile(path)`       | Проверяет, является ли путь файлом.                                  | `os.path.isfile("file.txt")`             |
| `os.path.isdir(path)`        | Проверяет, является ли путь директорией.                             | `os.path.isdir("directory")`             |
| `os.path.getsize(path)`      | Возвращает размер файла в байтах.                                    | `os.path.getsize("file.txt")`            |
| `os.path.abspath(path)`      | Возвращает абсолютный путь.                                          | `os.path.abspath("file.txt")`            |

""",
                        "os.stat": """
Функция `os.stat()` используется для получения информации о файле или каталоге по его пути.
Она возвращает объект `os.stat_result`, который содержит различные атрибуты, описывающие состояние файла.

# Синтаксис
```python
os.stat(path, *, dir_fd=None, follow_symlinks=True)
```

# Параметры
- `path` - Путь к файлу или директории. Может быть как абсолютным, так и относительным
- `dir_fd` - Дескриптор каталога; если задан, `path` интерпретируется как относительный путь относительно этого каталога
- `follow_symlinks` - Указывает, нужно ли следовать символическим ссылкам

# Возвращаемый объект `os.stat_result`
Результат вызова `os.stat()` — объект `os.stat_result`, который является кортежем с именованными полями:

| Атрибут    | Описание                                                         | **Пример значения** |
|------------|------------------------------------------------------------------|---------------------|
| `st_mode`  | Флаг режима файла, включая тип файла и права доступа             | `33188` (файл)      |
| `st_ino`   | Номер inode (индексного дескриптора) файла                       | `12345678`          |
| `st_dev`   | Идентификатор устройства, на котором расположен файл             | `2049`              |
| `st_nlink` | Количество жестких ссылок на файл                                | `1`                 |
| `st_uid`   | Идентификатор пользователя (UID) владельца файла                 | `1000`              |
| `st_gid`   | Идентификатор группы (GID) владельца файла                       | `1000`              |
| `st_size`  | Размер файла в байтах                                            | `1024`              |
| `st_atime` | Время последнего доступа к файлу в секундах с начала эпохи Unix  | `1609459200.0`      |
| `st_mtime` | Время последней модификации файла в секундах с начала эпохи Unix | `1609459200.0`      |
| `st_ctime` | Время изменения метаданных файла или создания файла (на Windows) | `1609459200.0`      |

## Пример использования
```python
import os
import time


stat_info = os.stat("example.txt")

print(f"Размер файла: {stat_info.st_size} байт")
print(f"Последний доступ: {time.ctime(stat_info.st_atime)}")
print(f"Последняя модификация: {time.ctime(stat_info.st_mtime)}")
print(f"Права доступа: {oct(stat_info.st_mode)}")
```

# Полезные функции для анализа `st_mode`
Флаг `st_mode` может содержать информацию о правах доступа и типе файла.
Для упрощения анализа можно использовать следующие функции из модуля [[Languages/Python/Libraries/System/stat.md]]:

- `stat.S_ISDIR(mode)` - Проверяет, является ли файл директорией
- `stat.S_ISREG(mode)` - Проверяет, является ли файл обычным файлом
- `stat.S_IMODE(mode)` - Возвращает права доступа в формате `0777`

## Пример использования функций из `stat`
```python
import os
import stat

path = "example.txt"
stat_info = os.stat(path)

if stat.S_ISDIR(stat_info.st_mode):
    print(f"{path} — это директория.")
elif stat.S_ISREG(stat_info.st_mode):
    print(f"{path} — это обычный файл.")
else:
    print(f"{path} — это другой тип файла.")

print(f"Права доступа: {oct(stat.S_IMODE(stat_info.st_mode))}")

print("Size of file:", stat_info.st_size)
print("Last accessed time:", stat_info.st_atime)
```


### Частые применения
1. Проверка размера файла — чтобы убедиться, что файл не пустой или не превышает определенного размера
2. Проверка прав доступа — для проверки или изменения прав доступа перед выполнением операций над файлом
3. Анализ времени изменения файла — для выполнения действий на основе того, как давно файл был изменен

# Полезные ссылки
- [Официальная документация os.stat](https://docs.python.org/3/library/os.html#os.stat)
- [Документация модуля stat](https://docs.python.org/3/library/stat.html)

""",
                    },
                    "sys": r"""
Этот модуль предоставляет доступ к некоторым объектам, используемым или поддерживаемым
интерпретатором, и к функциям, которые тесно взаимодействуют с интерпретатором.

# Динамические объекты

|                  |                                                                            |
|------------------|----------------------------------------------------------------------------|
| `argv`           | Аргументы командной строки<br>`argv[0]` — путь к скрипту, если он известен |
| `path`           | Путь поиска модуля<br>`path[0]` — каталог скрипта, иначе `""`              |
| `modules`        | Словарь загруженных модулей                                                |
| `displayhook`    | Вызывается для отображения результатов в интерактивном сеансе              |
| `excepthook`     | Вызывается для обработки любого неперехваченного исключения, отличного от `SystemExit`<br>Чтобы настроить печать в интерактивном сеансе или установить пользовательский<br>обработчик исключений верхнего уровня, назначьте другие функции для замены этих. |
| `stdin`          | Стандартный объект входного файла<br>`input()`                             |
| `stdout`         | Стандартный объект выходного файла<br>`print()`                            |
| `stderr`         | Стандартный объект ошибки; используется для сообщений об ошибках<br>Назначая им другие объекты файлов (или объекты, которые ведут себя как файлы),<br>можно перенаправить весь ввод-вывод интерпретатора. |
| `last_type`      | Тип последнего неперехваченного исключения                                 |
| `last_value`     | Значение последнего неперехваченного исключения                            |
| `last_traceback` | Трассировка последнего неперехваченного исключения<br>Эти три доступны только в интерактивном сеансе после того, как<br>трассировка была напечатана. |

# Статические объекты

|                                  |                                                                           |
|----------------------------------|---------------------------------------------------------------------------|
| `builtin_module_names`           | Кортеж имен модулей, встроенных в этот интерпретатор                      |
| `copyright`                      | Уведомление об авторских правах, относящееся к этому интерпретатору       |
| `exec_prefix`                    | Префикс, используемый для поиска машинно-специфической библиотеки Python  |
| `executable`                     | Абсолютный путь к исполняемому двоичному файлу интерпретатора Python      |
| `float_info`                     | Именованный кортеж с информацией о реализации `float`.                    |
| `float_repr_style`               | Строка, указывающая стиль вывода `repr()` для `float`                     |
| `hash_info`                      | Именованный кортеж с информацией о хеш-алгоритме.                         |
| `hexversion`                     | Информация о версии, закодированная как одно целое число                  |
| `implementation`                 | Информация о реализации Python.                                           |
| `int_info`                       | Именованный кортеж с информацией о реализации `int`.                      |
| `maxsize`                        | Наибольшая поддерживаемая длина контейнеров.                              |
| `maxunicode`                     | Значение наибольшей кодовой точки `Unicode`                               |
| `platform`                       | Идентификатор платформы                                                   |
| `prefix`                         | Префикс, используемый для поиска библиотеки Python                        |
| `thread_info`                    | Именованный кортеж с информацией о реализации потока.                     |
| `version`                        | Версия этого интерпретатора в виде строки                                 |
| `version_info`                   | Информация о версии в виде именованного кортежа                           |
| `dllhandle`                      | **[только для Windows]** целочисленный дескриптор библиотеки `DLL Python` |
| `winver`                         | **[только для Windows]** номер версии библиотеки `DLL Python`             |
| `_enablelegacywindowsfsencoding` | **[только для Windows]**                                                  |
| `__stdin__`                      | Исходный `stdin`<br>**не трогать!**                                       |
| `__stdout__`                     | Исходный `stdout`<br>**не трогать!**                                      |
| `__stderr__`                     | Исходный `stderr`<br>**не трогать!**                                      |
| `__displayhook__`                | Исходный `displayhook`<br>**не трогать!**                                 |
| `__excepthook__`                 | Исходный `excepthook`<br>**не трогать!**                                  |

# Функции

|                       |                                                                       |
|-----------------------|-----------------------------------------------------------------------|
| `displayhook()`       | Вывести объект на экран и сохранить его в `builtins._`                |
| `excepthook()`        | Вывести исключение и его трассировку в `sys.stderr`                   |
| `exception()`         | Вернуть активное исключение текущего потока                           |
| `exc_info()`          | Вернуть информацию об активном исключении текущего потока             |
| `exit()`              | Выйти из интерпретатора, вызвав `SystemExit`                          |
| `getdlopenflags()`    | Вернуть флаги, которые будут использоваться для вызовов `dlopen()`    |
| `getprofile()`        | Получить глобальную функцию профилирования                            |
| `getrefcount()`       | Вернуть счетчик ссылок для объекта (плюс один :-)                     |
| `getrecursionlimit()` | Вернуть максимальную глубину рекурсии для интерпретатора              |
| `getsizeof()`         | Вернуть размер объекта в байтах                                       |
| `gettrace()`          | Получить глобальную функцию трассировки отладки                       |
| `setdlopenflags()`    | Установить флаги, которые будут использоваться для вызовов `dlopen()` |
| `setprofile()`        | Установить глобальную функцию профилирования                          |
| `setrecursionlimit()` | Установить макс. глубина рекурсии для интерпретатора                  |
| `settrace()`          | Установить глобальную функцию трассировки отладки                     |

## Примеры

### argv

```python
import sys

# Передаем два аргумента при запуске скрипта
# python myscript.py arg1 arg2
print(sys.argv[0])  # myscript.py
print(sys.argv[1])  # arg1
print(sys.argv[2])  # arg2
```

### stdin, stdout, stderr

```python
import sys

# Читаем данные из стандартного потока ввода
data = sys.stdin.readline()

# Пишем данные в стандартный поток вывода
sys.stdout.write("Hello, world!\n")

# Пишем ошибки в стандартный поток ошибок
sys.stderr.write("Error occurred\n")
```

### platform

```python
import sys

if sys.platform == "win32":
    print("Windows")
elif sys.platform == "linux":
    print("Linux")
elif sys.platform == "darwin":
    print("MacOS")
```

### getsizeof

```python
import sys

a = [1, 2, 3]
print(sys.getsizeof(a))  # 88 размер объекта в байтах
```

```python
import sys

print(sys.path)
[
    "", 
    "C:\\Users\\User\\AppData\\Local\\Programs\\Python\\Python311\\python311.zip", 
    "C:\\Users\\User\\AppData\\Local\\Programs\\Python\\Python311\\DLLs", 
    "C:\\Users\\User\\AppData\\Local\\Programs\\Python\\Python311\\Lib", 
    "C:\\Users\\User\\AppData\\Local\\Programs\\Python\\Python311", 
    "C:\\Users\\User\\AppData\\Local\\Programs\\Python\\Python311\\Lib\\site-packages"
]
```

```python
import sys

def divide(x, y):
    try:
        result = x / y
    except:
        print(sys.exc_info())

divide(1, 0)
# (<class "ZeroDivisionError">, ZeroDivisionError("division by zero"), <traceback object>)
```
""",
                    "subprocess": r"""
Библиотека `subprocess` в Python используется для запуска новых процессов, выполнения команд в системе,
а также для управления стандартными потоками ввода, вывода и ошибок.
Эта библиотека предоставляет мощный интерфейс для взаимодействия с внешними процессами.

# Основные функции

| Функция                        | Описание                                                                                                           | Пример использования         |
|--------------------------------|--------------------------------------------------------------------------------------------------------------------|------------------------------|
| `subprocess.run()`             | Выполняет команду, ожидает завершения процесса<br>и возвращает результат в виде объекта `CompletedProcess`.        | {subprocess_run}             |
| `subprocess.Popen()`           | Запускает новый процесс и возвращает объект `Popen`,<br>который можно использовать для взаимодействия с процессом. | {subprocess_Popen}           |
| `subprocess.call()`            | Выполняет команду и возвращает код завершения процесса.                                                            | {subprocess_call}            |
| `subprocess.check_call()`      | Выполняет команду и вызывает исключение,<br>если процесс завершился с ошибкой.                                     | {subprocess_check_call}      |
| `subprocess.check_output()`    | Выполняет команду и возвращает её вывод.<br>Если процесс завершился с ошибкой, вызывается исключение.              | {subprocess_check_output}    |
| `subprocess.getoutput()`       | Выполняет команду и возвращает её вывод в виде строки.<br>Удобно для команд, не требующих сложного взаимодействия. | {subprocess_getoutput}       |
| `subprocess.getstatusoutput()` | Выполняет команду и возвращает кортеж (код завершения, вывод).                                                     | {subprocess_getstatusoutput} |

## Класс Popen

| Метод                 | Описание                                                                                                    | Пример использования |
|-----------------------|-------------------------------------------------------------------------------------------------------------|----------------------|
| `Popen.poll()`        | Проверяет завершился ли процесс.<br>Возвращает код завершения или `None`, если процесс ещё выполняется.     | {popen_poll}         |
| `Popen.wait()`        | Ожидает завершения процесса и возвращает код завершения.                                                    | {popen_wait}         |
| `Popen.communicate()` | Отправляет данные на стандартный ввод процесса<br>и получает данные из стандартного вывода и вывода ошибок. | {popen_communicate}  |
| `Popen.terminate()`   | Посылает процессу сигнал `SIGTERM`, запрашивая его завершение.                                              | {popen_terminate}    |
| `Popen.kill()`        | Принудительно завершает процесс, посылая сигнал `SIGKILL`.                                                  | {popen_kill}         |
| `Popen.stdin`         | Стандартный поток ввода процесса (если установлен `stdin=subprocess.PIPE`).                                 | {popen_stdin}        |
| `Popen.stdout`        | Стандартный поток вывода процесса (если установлен `stdout=subprocess.PIPE`).                               | {popen_stdout}       |
| `Popen.stderr`        | Стандартный поток ошибок процесса (если установлен `stderr=subprocess.PIPE`).                               | {popen_stderr}       |

## Управление потоками ввода-вывода

Пример взаимодействия с процессом через потоки ввода-вывода:

```python
import subprocess

process = subprocess.Popen(
    ["grep", "pattern"],
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE
)

stdout, stderr = process.communicate(input=b"text\npattern\nanother line\n")
print(stdout.decode())  # "pattern\n"
```

# Примеры использования

### Простой запуск команды
```python
import subprocess

subprocess.run(["ls", "-l"])
```

### Получение вывода команды
```python
import subprocess

print(subprocess.check_output(["echo", "Hello, World!"]).decode())  # "Hello, World!\n"
```

### Проверка кода завершения
```python
import subprocess

try:
  subprocess.check_call(["false"])
except subprocess.CalledProcessError as e:
  print(f"Процесс завершился с ошибкой: {{e.returncode}}")
```

### Запуск процесса с передачей данных на ввод
```python
import subprocess

process = subprocess.Popen(["cat"], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
stdout, _ = process.communicate(input=b"Hello, World!\n")
print(stdout.decode())  # "Hello, World!\n"
```

# Исключения

| Исключение                      | Описание                                                                                        |
|---------------------------------|-------------------------------------------------------------------------------------------------|
| `subprocess.CalledProcessError` | Вызывается, если процесс завершился с ненулевым кодом возврата.                                 |
| `subprocess.TimeoutExpired`     | Вызывается, если процесс не завершился в течение указанного времени (используется с `timeout`). |
| `subprocess.SubprocessError`    | Базовое исключение для всех исключений, связанных с `subprocess`.                               |

# Полезные параметры

| Параметр             | Описание                                                                                                                             |
|----------------------|--------------------------------------------------------------------------------------------------------------------------------------|
| `stdin`              | Определяет источник стандартного ввода процесса (например, `subprocess.PIPE`, `None`, или файловый объект).                          |
| `stdout`             | Определяет место, куда будет направлен стандартный вывод процесса (например, `subprocess.PIPE`, `None`, или файловый объект).        |
| `stderr`             | Определяет место, куда будет направлен стандартный поток ошибок процесса (например, `subprocess.PIPE`, `None`, или файловый объект). |
| `shell`              | Если `True`, команда будет выполнена через оболочку (shell). Будьте осторожны, так как это может быть небезопасно.                   |
| `cwd`                | Устанавливает текущий рабочий каталог для процесса.                                                                                  |
| `env`                | Определяет переменные окружения для процесса.                                                                                        |
| `universal_newlines` | Если `True`, ввод-вывод будет интерпретироваться как текст (строки), а не байты.                                                     |
| `timeout`            | Определяет максимальное время ожидания завершения процесса, после чего будет вызвано исключение `TimeoutExpired`.                    |

# Советы по безопасности

1. **Избегайте использования `shell=True`**, особенно с данными, полученными от пользователя, так как это может привести к уязвимостям типа `shell injection`.
2. **Используйте абсолютные пути** к командам для повышения безопасности и предсказуемости поведения скрипта.
3. **Управляйте таймаутами** для долгих процессов с помощью параметра `timeout`.

# Полезные ссылки

- [Официальная документация](https://docs.python.org/3/library/subprocess.html)
- [Real Python - Guide to Subprocess](https://realpython.com/python-subprocess/)

""".format(
                        subprocess_run=to_table_code_py('result = subprocess.run(["ls", "-l"])'),
                        subprocess_Popen=to_table_code_py('process = subprocess.Popen(["ls", "-l"])'),
                        subprocess_call=to_table_code_py('return_code = subprocess.call(["ls", "-l"])'),
                        subprocess_check_call=to_table_code_py('subprocess.check_call(["ls", "-l"])'),
                        subprocess_check_output=to_table_code_py('output = subprocess.check_output(["ls", "-l"])'),
                        subprocess_getoutput=to_table_code_py('output = subprocess.getoutput("ls -l")'),
                        subprocess_getstatusoutput=to_table_code_py(
                            'status, output = subprocess.getstatusoutput("ls -l")'
                        ),
                        popen_poll=to_table_code_py("status = process.poll()"),
                        popen_wait=to_table_code_py("return_code = process.wait()"),
                        popen_communicate=to_table_code_py("stdout, stderr = process.communicate(input_data)"),
                        popen_terminate=to_table_code_py("process.terminate()"),
                        popen_kill=to_table_code_py("process.kill()"),
                        popen_stdin=to_table_code_py('process.stdin.write(b"data")'),
                        popen_stdout=to_table_code_py("output = process.stdout.read()"),
                        popen_stderr=to_table_code_py("error_output = process.stderr.read()"),

                    ),
                    "multiprocessing": r"""
Библиотека "multiprocessing" используется в Python для поддержки параллельного выполнения кода, основанного на процессах.
Она предоставляет возможность создания и управления процессами, а также обмена данными между ними.

Методы модуля "multiprocessing" и его подмодулей:

`Process`: Класс для создания и управления процессов. Может быть использован для запуска функций или методов в отдельных процессах.
`Pool`: Класс для параллельного выполнения функций на нескольких процессах. Позволяет создавать пул процессов, управлять ими и получать результаты выполнения.
`Queue`: Класс для обмена данными между процессами. Поддерживает безопасную передачу объектов через очередь.
`Lock`: Класс для создания и использования блокировок (locks) в многопроцессорных программах. Обеспечивает синхронизацию доступа к ресурсам между процессами.
`Value` и `Array`: Классы для создания и использования разделяемых объектов синхронизации и обмена данными между процессами.
`Manager`: Класс для создания сервера процесса и разделенных объектов, доступных для различных процессов.

`Process()`: Создает объект процесса, принимает функцию или метод в качестве аргумента для выполнения в отдельном процессе.

```python
from multiprocessing import Process

def my_function():
    print("Hello from another process!")

if __name__ == "__main__":
    p = Process(target=my_function)
    p.start()
    p.join()
```

`Pool()`: Создает пул процессов и выполняет функцию для каждого элемента заданного массива аргументов.

```python
from multiprocessing import Pool

def square(x):
    return x ** 2

if __name__ == "__main__":
    with Pool(processes=3) as pool:
        print(pool.map(square, [1, 2, 3, 4, 5]))
```

`Queue()`: Создает очередь для обмена данными между процессами. Позволяет безопасно добавлять и извлекать элементы.

```python
from multiprocessing import Process, Queue

def worker(queue):
    item = queue.get()
    print("Processed:", item)

if __name__ == "__main__":
    q = Queue()
    p = Process(target=worker, args=(q,))
    p.start()
    q.put("Data")
    p.join()
```

Обратите внимание, что предоставленный код является кратким примером и может потребоваться дополнительная логика в реальных сценариях использования.
""",
                    "concurrent": r"""
Библиотека "concurrent" в Python используется для реализации параллельного выполнения задач и управления потоками и процессами.

Методы и подмодули библиотеки "concurrent":

concurrent.futures: Предоставляет высокоуровневый интерфейс для асинхронного выполнения задач.
concurrent.futures.ThreadPoolExecutor: Позволяет создавать пул потоков для параллельного выполнения задач.
concurrent.futures.ProcessPoolExecutor: Позволяет создавать пул процессов для параллельного выполнения задач.
concurrent.futures.as_completed: Возвращает итератор, который возвращает результаты задач по мере их завершения.
concurrent.futures.wait: Ожидает завершения задач и возвращает кортеж с завершенными и незавершенными задачами.
concurrent.futures.Future: Представляет отложенный результат выполнения задачи.

Некоторые из самых часто используемых методов библиотеки "concurrent" в Python:

submit(fn, *args, **kwargs): Подает задачу на выполнение в пул потоков или процессов.

```python
import concurrent.futures

def square(x):
    return x ** 2

with concurrent.futures.ThreadPoolExecutor() as executor:
    future = executor.submit(square, 5)
    print(future.result())  # 25
```

map(fn, *iterables, timeout=None): Применяет функцию к каждому элементу итерируемых объектов и возвращает результаты в том же порядке.

```python
import concurrent.futures

def square(x):
    return x ** 2

with concurrent.futures.ThreadPoolExecutor() as executor:
    numbers = [1, 2, 3, 4, 5]
    print(list(executor.map(square, numbers)))  # [1, 4, 9, 16, 25]
```

shutdown(wait=True): Завершает работу пула потоков или процессов.

```python
import concurrent.futures

with concurrent.futures.ThreadPoolExecutor() as executor:
    # Выполнение задач
    executor.shutdown()
```
""",
                    "keyboard": r"""
Библиотека "keyboard" используется для управления клавиатурой компьютера с помощью кода на языке Python.
Она позволяет эмулировать нажатия клавиш, считывать нажатия клавиш в реальном времени и манипулировать состоянием клавиш.

Таблица методов модуля "keyboard" и его подмодулей:

Метод                   | Описание
-----------------------|-----------------------
keyboard.press()       | Эмулирует нажатие заданной клавиши.
keyboard.release()     | Освобождает заданную клавишу после её нажатия.
keyboard.is_pressed()  | Проверяет, нажата ли заданная клавиша.
keyboard.write()       | Вводит заданный текст на клавиатуре.
keyboard.add_hotkey()  | Регистрирует горячую клавишу и связанный с ней обработчик.
keyboard.wait()        | Приостанавливает выполнение программы до нажатия заданной клавиши.
keyboard.unhook_all()  | Отключает все горячие клавиши.

Список самых часто используемых методов библиотеки "keyboard":

keyboard.press(): эмулирует нажатие клавиши.

```python
import keyboard

keyboard.press("A")  # Нажатие клавиши "A"
```

keyboard.release(): освобождает заданную клавишу после её нажатия.

```python
import keyboard

keyboard.release("A")  # Освобождение клавиши "A"
```

keyboard.is_pressed(): проверяет, нажата ли заданная клавиша.

```python
import keyboard

if keyboard.is_pressed("A"):  # Проверка, нажата ли клавиша "A"
    print("Клавиша A нажата")
```
""",
                    "fnmatch": r"""
Библиотека `fnmatch` в Python используется для работы с шаблонами файловых имен, основанными на Unix shell-подобном синтаксисе.
Она позволяет легко сопоставлять строки с шаблонами, которые включают такие символы, как `*`, `?`, и `[]`.

# Основные функции и их описание

| Функция                 | Описание                                                                                                         | Пример использования  |
|-------------------------|------------------------------------------------------------------------------------------------------------------|-----------------------|
| `fnmatch.fnmatch()`     | Сопоставляет строку с шаблоном.<br>Регистро**зависимо** на Unix и регистро**независимо** на Windows.             | {fnmatch_fnmatch}     |
| `fnmatch.fnmatchcase()` | Сопоставляет строку с шаблоном с учетом регистра на всех платформах.                                             | {fnmatch_fnmatchcase} |
| `fnmatch.filter()`      | Фильтрует список строк, оставляя только те, которые соответствуют шаблону.                                       | {fnmatch_filter}      |
| `fnmatch.translate()`   | Преобразует шаблон в регулярное выражение,<br>которое можно использовать с `re` для более сложных сопоставлений. | {fnmatch_translate}   |

# Специальные символы в шаблонах

| Символ    | Описание                                                                                                                                  | Пример                                                              |
|-----------|-------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------|
| `*`       | Соответствует любой строке (включая пустую).                                                                                              | `"*.txt"` соответствует `"file.txt"` и `"a.txt"`                    |
| `?`       | Соответствует любому одному символу.                                                                                                      | `"file?.txt"` соответствует `"file1.txt"`, но не `"file12.txt"`     |
| `[seq]`   | Соответствует любому символу из `seq`.<br>Например, `[abc]` соответствует `a`, `b`, или `c`.                                              | `"file[0-9].txt"` соответствует `"file1.txt"`, но не `"file12.txt"` |
| `[!seq]`  | Соответствует любому символу, который **не** входит в `seq`.<br>Например, `[!abc]` соответствует любому символу, кроме `a`, `b`, или `c`. | `"file[!0-9].txt"` соответствует `"fileA.txt"`, но не `"file1.txt"` |

# Примеры использования

### Сопоставление строки с шаблоном
```python
import fnmatch

print(fnmatch.fnmatch("data.csv", "*.csv"))  # True
print(fnmatch.fnmatch("data.txt", "*.csv"))  # False
```

### Сопоставление с учетом регистра
```python
import fnmatch

print(fnmatch.fnmatchcase("Data.CSV", "*.csv"))  # False
print(fnmatch.fnmatchcase("Data.CSV", "*.CSV"))  # True
```

### Фильтрация списка файлов
```python
import fnmatch

files = ["data1.csv", "data2.txt", "data3.csv"]
csv_files = fnmatch.filter(files, "*.csv")
print(csv_files)  # ["data1.csv", "data3.csv"]
```

### Использование с регулярными выражениями
```python
import fnmatch
import re

pattern = fnmatch.translate("*.txt")
print(pattern)  # (?s:.*\.txt)\Z

regex = re.compile(pattern)
print(regex.match("file.txt"))  # <re.Match object; span=(0, 8), match='file.txt'>
print(regex.match("file.csv"))  # None
```

## Примечания

- На Unix-системах функции `fnmatch()` и `fnmatchcase()` работают **с учетом регистра**, а на Windows они **регистронезависимы**.
Однако `fnmatchcase()` **всегда учитывает регистр**, независимо от платформы.
- Используйте `fnmatch.translate()` для сложных сопоставлений, которые требуют регулярных выражений.

# Полезные примеры

### Сопоставление с шаблоном для нескольких расширений
```python
import fnmatch

files = ["report.doc", "data.csv", "image.png", "script.py"]
docs = fnmatch.filter(files, "*.[dc][so][cv]")
print(docs)  # ["report.doc", "data.csv"]
```

### Фильтрация скрытых файлов (начинающихся с точки)
```python
import fnmatch

files = [".bashrc", "data.csv", ".gitignore", "script.py"]
hidden_files = fnmatch.filter(files, ".*")
print(hidden_files)  # [".bashrc", ".gitignore"]
```

# Полезные ссылки

- [Официальная документация](https://docs.python.org/3/library/fnmatch.html)
- [Real Python - Guide to Filename Matching](https://realpython.com/lessons/filename-matching/)
""".format(
                        fnmatch_fnmatch=to_table_code_py('fnmatch.fnmatch("foo.txt", "*.txt")'),
                        fnmatch_fnmatchcase=to_table_code_py('fnmatch.fnmatchcase("Foo.txt", "*.TXT")'),
                        fnmatch_filter=to_table_code_py('fnmatch.filter(["foo.txt", "bar.py"], "*.txt")'),
                        fnmatch_translate=to_table_code_py('pattern = fnmatch.translate("*.txt")'),
                    ),
                    "glob": r"""
Библиотека "glob" предназначена для поиска файлов с использованием шаблонов и расширений в заданном каталоге.

Методы модуля "glob" и их краткое описание:

glob.glob(pathname): Возвращает список всех путей, соответствующих заданному шаблону.
glob.escape(pathname): Экранирует все специальные символы в заданном пути, чтобы они были интерпретированы как обычные символы.

Пример кода для демонстрации работы метода glob.glob():

```python
import glob

files = glob.glob("*.txt")
print(files)
```

В этом примере метод glob.glob("*.txt") ищет все файлы с расширением ".txt" в текущем каталоге и возвращает
список путей к этим файлам, который затем выводится на экран.
""",
                    "resource": r"""
Библиотека "resource" в Python используется для доступа и управления системными ресурсами, такими как время CPU, память и дескрипторы файлов.

Методы и подмодули модуля "resource":

`getrusage(who)` - возвращает информацию о системных ресурсах для указанного процесса или группы процессов.
`getrlimit(resource)` - получает текущие ограничения на указанный ресурс.
`setrlimit(resource, limits)` - устанавливает ограничения на указанный ресурс.
`getpagesize()` - возвращает размер страницы памяти операционной системы.
`getrusage()` - возвращает информацию о системных ресурсах для текущего процесса.
`RUSAGE_SELF` - константа, указывающая на текущий процесс.
`RUSAGE_CHILDREN` - константа, указывающая на дочерние процессы текущего процесса.

Наиболее часто используемые методы:

`getrusage(who)` - получает информацию о системных ресурсах для указанного процесса или группы процессов.

```python
import resource

usage = resource.getrusage(resource.RUSAGE_SELF)
print(usage)
```

`getrlimit(resource)` - получает текущие ограничения на указанный ресурс.

```python
import resource

limit = resource.getrlimit(resource.RLIMIT_CPU)
print(limit)
```

`setrlimit(resource, limits)` - устанавливает ограничения на указанный ресурс.

```python
import resource

# Ограничение на время CPU - 2 секунды
limits = (2, resource.RLIM_INFINITY)
resource.setrlimit(resource.RLIMIT_CPU, limits)
```
""",
                    "posix": r"""
Библиотека "posix" в Python используется для взаимодействия с функциями и операциями,
специфичными для POSIX-совместимых операционных систем, таких как Linux и macOS.

Таблица методов модуля "posix" и его подмодулей и краткое описание:

Модуль "posix":
getpid(): Возвращает идентификатор текущего процесса.
getuid(): Возвращает идентификатор пользователя текущего процесса.
getgid(): Возвращает идентификатор группы текущего процесса.
chmod(path, mode): Изменяет права доступа к файлу или директории.
chown(path, uid, gid): Изменяет владельца и группу файловой системы.
getcwd(): Возвращает текущую рабочую директорию.
listdir(path): Возвращает список файлов и директорий в указанной директории.

Подмодуль "posixpath":
join(path1, path2): Объединяет два пути в один.
isfile(path): Проверяет, является ли путь файлом.
isdir(path): Проверяет, является ли путь директорией.
basename(path): Возвращает базовое имя последнего компонента пути.
dirname(path): Возвращает каталог пути.

Список часто используемых методов, их краткое описание и

getpid(): Возвращает идентификатор текущего процесса.

```python
import os
print(os.getpid())
```

getcwd(): Возвращает текущую рабочую директорию.

```python
import os
print(os.getcwd())
```

listdir(path): Возвращает список файлов и директорий в указанной директории.

```python
import os
print(os.listdir("/path/to/directory"))
```
""",
                    "stat": r"""
Библиотека "stat" в Python используется для работы с информацией о файловой системе,
такой как атрибуты файла, права доступа и временные метки.

|                     |                                                    |
|---------------------|----------------------------------------------------|
| stat.S_ISDIR(mode)  | Проверяет, является ли файл директорией            |
| stat.S_ISREG(mode)  | Проверяет, является ли файл обычным файлом         |
| stat.S_ISLNK(mode)  | Проверяет, является ли файл символической ссылкой  |
| stat.S_ISSOCK(mode) | Проверяет, является ли файл сокетом                |
| stat.S_ISFIFO(mode) | Проверяет, является ли файл каналом FIFO           |
| stat.S_ISBLK(mode)  | Проверяет, является ли файл блочным устройством    |
| stat.S_ISCHR(mode)  | Проверяет, является ли файл символьным устройством |
| stat.S_IMODE(mode)  | Возвращает режим доступа к файлу                   |
| stat.S_IFMT(mode)   | Возвращает тип файла и режим доступа               |

### Примеры

```python
import os
import stat

file_path = "path/to/file.txt"
file_stat = os.stat(file_path)

if stat.S_ISDIR(file_stat.st_mode):
    print("File is a directory")
else:
    print("File is not a directory")

if stat.S_ISREG(file_stat.st_mode):
    print("File is a regular file")
else:
    print("File is not a regular file")

print("File mode:", stat.S_IMODE(file_stat.st_mode))
```
""",
                    "getopt": r"""
Библиотека "getopt" в Python используется для разбора аргументов командной строки.
Она позволяет программам легко определять и обрабатывать аргументы, передаваемые при запуске программы.

Методы и подмодули библиотеки "getopt":
getopt.getopt(args, shortopts, longopts=None): Парсит аргументы командной строки, возвращает пару (opts, args), где opts - список кортежей со значением и аргументом, args - список непарсированных аргументов.
getopt.gnu_getopt(args, shortopts, longopts=None): Аналогичен методу getopt.getopt(), но поддерживает нестандартный формат аргументов, включая возможность использования дефисов в значении аргумента.
getopt.GetoptError: Исключение, возникающее при ошибке разбора аргументов командной строки. Оно содержит информацию об ошибке и методы для доступа к ней.


getopt.getopt(args, shortopts, longopts=None): Парсит аргументы командной строки и возвращает опции и аргументы.

```python
import getopt
import sys

args = sys.argv[1:]
shortopts = "ho:v"   # Опции без аргументов: -h, -o, -v
longopts = ["help", "output=", "verbose"]  # Опции с аргументами: --help, --output, --verbose

try:
    opts, args = getopt.getopt(args, shortopts, longopts)
except getopt.GetoptError:
    print("Ошибка в аргументах командной строки.")
```

getopt.gnu_getopt(args, shortopts, longopts=None): Парсит аргументы командной строки с нестандартным форматом и возвращает опции и аргументы.

```python
import getopt
import sys

args = sys.argv[1:]
shortopts = "ho:v"   # Опции без аргументов: -h, -o, -v
longopts = ["help", "output=", "verbose"]  # Опции с аргументами: --help, --output, --verbose

try:
    opts, args = getopt.gnu_getopt(args, shortopts, longopts)
except getopt.GetoptError:
    print("Ошибка в аргументах командной строки.")
```
""",
                    "optparse": r"""
Библиотека "optparse" используется для обработки командной строки в Python.
Она предоставляет удобные инструменты для определения и разбора аргументов командной строки,
а также для создания гибких и понятных интерфейсов командной строки для ваших программ.

Методы модуля "optparse" и его подмодулей:

OptionParser: Класс, который предоставляет функциональность для определения и разбора аргументов командной строки.
OptionGroup: Класс, позволяющий группировать опции вместе для более удобного использования.
Option: Класс, представляющий отдельную опцию командной строки.
OptionContainer: Базовый класс для группировки опций.
OptionConflictError: Исключение, возникающее при конфликте опций.
OptionValueError: Исключение, возникающее при некорректном значении опции.

Некоторые из самых часто используемых методов "optparse" и их описание:

add_option(): Добавляет опцию в парсер командной строки.

```python
parser.add_option("-f", "--file", dest="filename", help="Specify input file")
```

parse_args(): Разбирает аргументы командной строки и возвращает объект, содержащий значения опций.

```python
(options, args) = parser.parse_args()
```

print_help(): Выводит справку о доступных опциях командной строки.

```python
parser.print_help()
```

error(): Генерирует сообщение об ошибке и выводит справку о доступных опциях командной строки.

```python
parser.error("Input file is required")
```

set_defaults(): Устанавливает значения по умолчанию для опций.

```python
parser.set_defaults(verbose=True)
```
""",
                    "grp": r"""
Библиотека "grp" в Python используется для работы с группами пользователей в операционной системе.
Методы модуля "grp" и его подмодулей:

`grp.getgrgid(gid)`: Возвращает информацию о группе по ее идентификатору.
`grp.getgrnam(name)`: Возвращает информацию о группе по ее имени.
`grp.getgrall()`: Возвращает список всех групп в системе.
`grp.getgrgid(gid).gr_name`: Возвращает имя группы по ее идентификатору.
`grp.getgrgid(gid).gr_passwd`: Возвращает пароль группы по ее идентификатору.

Самые часто используемые методы:

Метод `grp.getgrgid(gid)` используется для получения информации о группе по ее идентификатору.

```python
import grp

gid = 1000
group_info = grp.getgrgid(gid)
print(group_info)
```

Метод `grp.getgrnam(name)` используется для получения информации о группе по ее имени.

```python
import grp

group_name = "developers"
group_info = grp.getgrnam(group_name)
print(group_info)
```

Метод `grp.getgrall()` возвращает список всех групп в системе.

```python
import grp

all_groups = grp.getgrall()
for group_info in all_groups:
    print(group_info)
```

Пожалуйста, обратите внимание, что эти примеры кода могут потребовать соответствующих разрешений для доступа к информации о группах пользователя на операционной системе.
""",
                    "posixpath": r"""
Библиотека "posixpath" в Python используется для работы с путями файловой системы в POSIX-совместимых операционных системах.
Она предоставляет функции и методы для манипуляции, анализа и навигации по путям к файлам и директориям.

Методы и подмодули библиотеки "posixpath":

`posixpath.basename(path)`: Возвращает базовое имя файла или директории из заданного пути.
`posixpath.dirname(path)`: Возвращает имя директории из заданного пути.
`posixpath.isabs(path)`: Проверяет, является ли заданный путь абсолютным.
`posixpath.join(path, *paths)`: Объединяет компоненты пути в один.
`posixpath.normcase(path)`: Возвращает нормализованную версию заданного пути с учетом регистра символов.
`posixpath.normpath(path)`: Возвращает нормализованную версию заданного пути с учетом символов ".", ".." и разделителей.
`posixpath.realpath(path)`: Возвращает каноническое имя (полный путь) для заданного пути.
`posixpath.split(path)`: Разделяет заданный путь на имя директории и базовое имя файла или директории.

Некоторые из наиболее часто используемых методов библиотеки "posixpath":

`basename(path)`: Возвращает имя файла из заданного пути.

```python
import posixpath

path = "/home/user/example.txt"
filename = posixpath.basename(path)
print(filename)  # example.txt
```

`dirname(path)`: Возвращает имя директории из заданного пути.

```python
import posixpath

path = "/home/user/example.txt"
directory = posixpath.dirname(path)
print(directory)  # /home/user
```

`isabs(path)`: Проверяет, является ли заданный путь абсолютным.

```python
import posixpath

path = "/home/user/example.txt"
is_absolute = posixpath.isabs(path)
print(is_absolute)  # True
```
""",
                    "genericpath": r"""
Библиотека "genericpath" в Python используется для работы с путями и файловой системой на разных платформах.
Она предоставляет универсальные методы для обработки путей, создания новых путей, проверки наличия файлов и директорий,
а также для работы с именами файлов.

Таблица методов и их описания в модуле "genericpath":

| Метод            | Описание                                                |
|------------------|---------------------------------------------------------|
| isdir(path)      | Проверяет, является ли указанный путь директорией.        |
| isfile(path)     | Проверяет, является ли указанный путь файлом.            |
| exists(path)     | Проверяет, существует ли указанный путь.                 |
| lexists(path)    | Проверяет, существует ли указанный путь (обходя символические ссылки). |
| split(path)      | Разделяет путь на директорию и базовое имя файла.        |
| splitext(path)   | Разделяет путь на базовое имя файла и расширение.        |
| basename(path)   | Возвращает последний компонент пути (имя файла или директории). |
| dirname(path)    | Возвращает директорию из пути.                          |
| join(path, *paths) | Объединяет пути в переносимый образ.                    |
| normpath(path)   | Преобразует путь, удаляя избыточные разделители и ссылки "." и "..". |
| abspath(path)    | Возвращает абсолютный путь.                             |


isdir(path): Проверяет, является ли указанный путь директорией.

```python
import os.path

path = "/path/to/directory"
if os.path.isdir(path):
    print(f"{path} is a directory.")
```

isfile(path): Проверяет, является ли указанный путь файлом.

```python
import os.path

path = "/path/to/file.txt"
if os.path.isfile(path):
    print(f"{path} is a file.")
```

exists(path): Проверяет, существует ли указанный путь.

```python
import os.path

path = "/path/to/file.txt"
if os.path.exists(path):
    print(f"{path} exists.")
```

splitext(path): Разделяет путь на базовое имя файла и расширение.

```python
import os.path

path = "/path/to/file.txt"
base_name, extension = os.path.splitext(path)
print(f"Base name: {base_name}")
print(f"Extension: {extension}")
```
""",
                    "gc": r"""
Библиотека "gc" в Python используется для управления сборкой мусора.
Она предоставляет функции и методы для контроля за автоматическим освобождением памяти, которая больше не используется программой.

Методы модуля "gc" и его подмодулей:

Метод                     | Описание
-------------------------|---------------------------------------
gc.disable()              | Отключает автоматическую сборку мусора.
gc.enable()               | Включает автоматическую сборку мусора.
gc.collect()              | Принудительно запускает сборку мусора.
gc.get_threshold()        | Возвращает текущие пороги сборки мусора.
gc.set_threshold(threshold) | Устанавливает пороги сборки мусора.
gc.get_count()            | Возвращает количество сборок мусора, проведенных до сих пор.
gc.get_objects()          | Возвращает список всех объектов, находящихся в памяти.

Самые часто используемые методы в библиотеке "gc":

Метод                       | Описание                        | Пример кода
----------------------------|---------------------------------|-------------------
gc.collect()                | Принудительно запускает сборку мусора. | gc.collect()
gc.get_threshold()          | Возвращает текущие пороги сборки мусора. | threshold = gc.get_threshold()
gc.set_threshold(threshold) | Устанавливает пороги сборки мусора. | gc.set_threshold(700, 10, 10)
gc.get_count()              | Возвращает количество сборок мусора, проведенных до сих пор. | count = gc.get_count()

Этот код показывает использование метода gc.collect(), который принудительно запускает сборку мусора:

```python
import gc

# Создание объектов
x = [1, 2, 3]
y = [4, 5, 6]

# Удаление ссылок на объекты
del x
del y

# Принудительная сборка мусора
gc.collect()
```
Надеюсь, это поможет вам понять и использовать библиотеку "gc" в Python.
Если у вас возникнут дополнительные вопросы, не стесняйтесь задавать их.
""",
                    "nt": r"""
Библиотека "nt" в Python используется для работы с функциями операционной системы Windows.

Методы модуля "nt" и его подмодулей:

Модуль "nt":
nt.getcwd(): Возвращает текущую рабочую директорию.
nt.listdir(path): Возвращает список файлов и директорий в указанном пути.
nt.mkdir(path): Создает новую директорию по указанному пути.
nt.remove(path): Удаляет файл по указанному пути.
nt.rename(src, dst): Переименовывает файл или директорию.
nt.system(command): Выполняет команду операционной системы.

Подмодуль "ntpath":
ntpath.basename(path): Возвращает имя файла или директории из указанного пути.
ntpath.dirname(path): Возвращает имя директории из указанного пути.
ntpath.exists(path): Проверяет, существует ли файл или директория по указанному пути.
ntpath.join(path, *paths): Объединяет пути в один.
ntpath.split(path): Разделяет путь на имя директории и имя файла.

Некоторые часто используемые методы и их описание:

nt.getcwd(): Возвращает текущую рабочую директорию.

```python
import nt
current_dir = nt.getcwd()
print(current_dir)
```

nt.listdir(path): Возвращает список файлов и директорий в указанном пути.


```python
import nt
file_list = nt.listdir("C:/Users")
print(file_list)
```

nt.mkdir(path): Создает новую директорию по указанному пути.

```python
import nt
nt.mkdir("C:/Users/NewDirectory")
```

nt.remove(path): Удаляет файл по указанному пути.

```python
import nt
nt.remove("C:/Users/example.txt")
```

nt.rename(src, dst): Переименовывает файл или директорию.

```python
import nt
nt.rename("C:/Users/old_name.txt", "C:/Users/new_name.txt")
```

nt.system(command): Выполняет команду операционной системы.

```python
import nt
nt.system("dir")
```
""",
                    "filecmp": r"""
Библиотека "filecmp" используется для сравнения файлов и директорий в Python.
Она предоставляет функциональность для сравнения содержимого файлов, определения различий между файлами и обнаружения одинаковых файлов.

Методы и подмодули модуля "filecmp" можно представить в следующей таблице:

   Метод/Подмодуль          | Краткое Описание
   ------------------------|-------------------
   cmp(files1, files2)     | Сравнивает содержимое двух файлов и возвращает True, если они одинаковы, и False в противном случае.
   cmpfiles(dir1, dir2)    | Сравнивает содержимое двух директорий и возвращает список различий и список одинаковых файлов.
   clear_cache()           | Очищает кэш, используемый для сравнения файлов и директорий.
   dircmp(dir1, dir2)      | Возвращает объект "dircmp", содержащий информацию о сравнении двух директорий, включая различия и одинаковые файлы.
   cmp_fuzzy(file1, file2) | Сравнивает содержимое двух файлов с использованием нечеткого(размытого) алгоритма сравнения.

Некоторые из самых часто используемых методов библиотеки "filecmp" вместе с краткими описаниями и примерами кода:

Метод cmp(files1, files2) Сравнивает содержимое двух файлов.

```python
import filecmp

if filecmp.cmp("file1.txt", "file2.txt"):
    print("Файлы одинаковы.")
else:
    print("Файлы различаются.")
```

Метод cmpfiles(dir1, dir2) Сравнивает содержимое двух директорий и возвращает списки различий и одинаковых файлов.

```python
import filecmp

diff_files, common_files = filecmp.cmpfiles("dir1", "dir2")

print("Различные файлы:")
for file in diff_files:
    print(file)

print("Одинаковые файлы:")
for file in common_files:
    print(file)
```
""",
                    "pymsgbox": r"""
Библиотека "pymsgbox" используется для создания простых диалоговых окон с сообщениями, предупреждениями и запросами пользователю в Python.

Таблица методов модуля "pymsgbox" и их краткое описание:
`alert`: Отображает диалоговое окно с сообщением для пользователя.
`confirm`: Отображает диалоговое окно с вопросом для пользователя с двумя вариантами ответа (Да/Нет).
`prompt`: Отображает диалоговое окно с запросом пользователю на ввод текста.
`password`: Отображает диалоговое окно с запросом пользователю на ввод пароля (текста, скрытого звездочками).
`textbox`: Отображает диалоговое окно с возможностью ввода и редактирования текста пользователем.

Список самых частых методов "pymsgbox", их краткое описание и примерный код для демонстрации:

`alert(message, title=""):`
Описание: Отображает диалоговое окно с сообщением для пользователя.

```python
import pymsgbox

pymsgbox.alert("Привет, пользователь!", "Информация")
```

`confirm(text, title="", buttons=["Да", "Нет"]):`
Описание: Отображает диалоговое окно с вопросом для пользователя с двумя вариантами ответа.

```python
import pymsgbox

response = pymsgbox.confirm("Вы уверены, что хотите продолжить?", "Подтверждение")
if response == "Да":
    # Действия при выборе "Да"
    pass
else:
    # Действия при выборе "Нет"
    pass
```

`prompt(text, title="", default=""):`
Описание: Отображает диалоговое окно с запросом пользователю на ввод текста.

```python
import pymsgbox

username = pymsgbox.prompt("Введите ваше имя:", "Ввод данных")
```

`password(text, title=""):`
Описание: Отображает диалоговое окно с запросом пользователю на ввод пароля (скрытого звездочками).

```python
import pymsgbox

password = pymsgbox.password("Введите пароль:", "Подтверждение")
```

`textbox(text="", title="", default="", multiline=False):`
Описание: Отображает диалоговое окно с возможностью ввода и редактирования текста пользователем.

```python
import pymsgbox

text = pymsgbox.textbox("Введите текст:", "Редактирование текста")
```
""",
                    "pygetwindow": r"""
Библиотека "pygetwindow" используется для управления окнами в операционной системе с помощью Python.
Она предоставляет функции для поиска, получения информации о размерах и позиции окон, а также для управления их видимостью и активностью.

Методы и подмодули библиотеки "pygetwindow":

`getAllTitles()`: Возвращает список заголовков всех открытых окон.
`getWindowsWithTitle(title)`: Возвращает список окон с указанным заголовком.
`getWindowGeometry(window)`: Возвращает геометрию (размеры и позицию) указанного окна.
`getWindowAt(x, y)`: Возвращает окно, находящееся по указанным координатам.
`getActiveWindow()`: Возвращает активное окно.
`getWindowBorders(window)`: Возвращает границы указанного окна.
`getWindowRect(window)`: Возвращает прямоугольник, охватывающий указанное окно.
`getWindowPID(window)`: Возвращает идентификатор процесса, связанного с указанным окном.
`getWindowProcessID(window)`: Возвращает идентификатор процесса, связанного с указанным окном.
`getWindowThreadID(window)`: Возвращает идентификатор потока, связанного с указанным окном.
`getWindowThreadProcessId(window)`: Возвращает идентификатор потока и процесса, связанных с указанным окном.
`getWindowThreadProcessId(window)`: Возвращает идентификатор потока и процесса, связанных с указанным окном.
`getWindowThreadProcessId(window)`: Возвращает идентификатор потока и процесса, связанных с указанным окном.
`getWindowThreadProcessId(window)`: Возвращает идентификатор потока и процесса, связанных с указанным окном.
`getWindowThreadProcessId(window)`: Возвращает идентификатор потока и процесса, связанных с указанным окном.
`getWindowThreadProcessId(window)`: Возвращает идентификатор потока и процесса, связанных с указанным окном.

Некоторые из самых часто используемых методов библиотеки "pygetwindow":

`getAllTitles()`: Возвращает список заголовков всех открытых окон.

```python
import pygetwindow

window_titles = pygetwindow.getAllTitles()
print(window_titles)
```

`getWindowsWithTitle(title)`: Возвращает список окон с указанным заголовком.

```python
import pygetwindow

windows = pygetwindow.getWindowsWithTitle("Notepad")
for window in windows:
    print(window.title)
```

`getActiveWindow()`: Возвращает активное окно.

```python
import pygetwindow

active_window = pygetwindow.getActiveWindow()
print(active_window.title)
```

`getWindowGeometry(window)`: Возвращает геометрию (размеры и позицию) указанного окна.

```python
import pygetwindow

window = pygetwindow.getWindowsWithTitle("Notepad")[0]
geometry = pygetwindow.getWindowGeometry(window)
print(geometry)
```

`getWindowRect(window)`: Возвращает прямоугольник, охватывающий указанное окно.

```python
import pygetwindow

window = pygetwindow.getWindowsWithTitle("Notepad")[0]
rect = pygetwindow.getWindowRect(window)
print(rect)
```
""",
                    "psutil": r"""
Библиотека "psutil" в Python используется для доступа и управления информацией о системе и процессах.
Она предоставляет функции для получения информации о процессоре, памяти, дисках, сети и др.
Это полезно для мониторинга системы, оптимизации ресурсов и отладки.



| Метод                  | Описание                              |
|-----------------------|---------------------------------------|
| psutil.cpu_percent()  | Возвращает процент использования ЦП   |
| psutil.virtual_memory()  | Возвращает информацию о виртуальной памяти   |
| psutil.disk_usage()  | Возвращает использование дискового пространства   |
| psutil.net_io_counters()  | Возвращает сетевые счетчики ввода-вывода   |
| psutil.process_count()  | Возвращает количество запущенных процессов   |



psutil.cpu_percent(): Возвращает текущий процент использования CPU в виде числа от 0 до 100.

```python
import psutil

cpu_percent = psutil.cpu_percent()
print("Текущий процент использования CPU:", cpu_percent)
```

psutil.virtual_memory(): Возвращает информацию о виртуальной памяти в виде объекта.
Можно получить доступ к атрибутам, таким как "total" (всего памяти), "available" (доступно памяти), "used" (используется памяти) и др.

```python
import psutil

virtual_memory = psutil.virtual_memory()
print("Общая доступная память:", virtual_memory.total)
print("Доступная память:", virtual_memory.available)
print("Используется памяти:", virtual_memory.used)
```

psutil.disk_usage(): Возвращает информацию об использовании дискового пространства для указанного пути в виде объекта.
Можно получить доступ к атрибутам, таким как "total" (всего пространства),
"used" (используется пространство), "free" (свободное пространство) и др.

```python
import psutil

disk_usage = psutil.disk_usage("/")
print("Общее пространство диска:", disk_usage.total)
print("Используется пространства диска:", disk_usage.used)
print("Свободное пространство диска:", disk_usage.free)
```

psutil.net_io_counters(): Возвращает сетевые счетчики ввода-вывода в виде объекта.
Можно получить доступ к атрибутам, таким как "bytes_sent" (отправленные байты), "bytes_recv" (полученные байты), "packets_sent" (отправленные пакеты) и др.

```python
import psutil

net_io_counters = psutil.net_io_counters()
print("Отправленные байты:", net_io_counters.bytes_sent)
print("Полученные байты:", net_io_counters.bytes_recv)
```

psutil.process_count(): Возвращает количество текущих запущенных процессов.

```python
import psutil

process_count = psutil.process_count()
print("Количество запущенных процессов:", process_count)
```
""",
                    "spwd": r"""
Библиотека "spwd" в Python используется для доступа к информации о пользовательских учетных записях в системе UNIX.
Она предоставляет функции для получения доступа к файлу `/etc/shadow`,
который хранит зашифрованные пароли пользователей, а также другую информацию о пользователях.

Таблица методов модуля "spwd":

Метод                | Описание
---------------------|-------------------------
`spwd.getspnam(name)`| Возвращает информацию о пользователе по его имени в виде объекта `spwd.struct_spwd`.
`spwd.getspall()`    | Возвращает список всех пользователей в системе, каждый в виде объекта `spwd.struct_spwd`.
`spwd.struct_spwd`   | Объект, представляющий информацию о пользователе, содержащий следующие атрибуты:
`sp_nam`(имя пользователя), `sp_pwd`(зашифрованный пароль),
`sp_lstchg`(последнее изменение пароля), `sp_min`(минимальный срок действия пароля),
`sp_max`(максимальный срок действия пароля), `sp_warn`(предупреждение о необходимости изменения пароля),
`sp_inact`(срок неактивности до блокировки учетной записи),
`sp_expire`(дата истечения срока действия пароля), `sp_flag`(флаги учетной записи).

Список самых частых методов модуля "spwd" и их описания:

Метод                | Описание                                           | Пример кода
---------------------|----------------------------------------------------|------------------------
`spwd.getspnam(name)`| Возвращает информацию о пользователе по его имени. | `user_info = spwd.getspnam("john")`
`spwd.getspall()`    | Возвращает список всех пользователей в системе.    | `users = spwd.getspall()`

Примечание: Примеры кода не могут быть предоставлены для данной библиотеки, поскольку требуется доступ к системным файлам.
""",
                    "fcntl": r"""
Библиотека "fcntl" в Python используется для обращения к системным вызовам управления файловыми дескрипторами и флагами файлового управления.

Методы модуля "fcntl" включают:

fcntl.flock(fd, operation): Блокирует или разблокирует файловый дескриптор при помощи операции блокировки.
fcntl.ioctl(fd, request, arg): Вызывает системный вызов IOCTL для управления устройством, связанным с файловым дескриптором.
fcntl.fcntl(fd, command, arg): Выполняет команду файлового управления на файловом дескрипторе, такую как получение или изменение флагов управления файла.
и другие...

Некоторые из наиболее распространенных методов "fcntl" включают:

fcntl.flock(fd, operation) Блокирует или разблокирует файловый дескриптор.

```python
import fcntl

file_descriptor = open("file.txt", "w")
fcntl.flock(file_descriptor, fcntl.LOCK_EX)
# Выполните операции с заблокированным файлом
fcntl.flock(file_descriptor, fcntl.LOCK_UN)
file_descriptor.close()
```

fcntl.ioctl(fd, request, arg) Выполняет системный вызов IOCTL для управления устройством.

```python
import fcntl

file_descriptor = open("/dev/sda", "r")
request_code = 123  # Код запроса, связанный с устройством
arg = 456  # Аргумент IOCTL
fcntl.ioctl(file_descriptor, request_code, arg)
file_descriptor.close()
```

fcntl.fcntl(fd, command, arg) Выполняет команду файлового управления на файловом дескрипторе.

```python
import fcntl

file_descriptor = open("file.txt", "r")
command = fcntl.F_GETFL  # Получить флаги управления файла
flags = fcntl.fcntl(file_descriptor, command, 0)
print(flags)
file_descriptor.close()
```
""",
                    "signal": """
Библиотека `signal` позволяет работать с сигналами в Unix-подобных операционных системах.
Сигналы — это уведомления, которые операционная система посылает процессам для того,
чтобы сообщить о каких-либо событиях (например, о завершении работы, прерывании и т.д.).

- **Сигнал** — сообщение, посылаемое операционной системой процессу для уведомления о каком-либо событии.
- **Обработчик сигнала** — функция, которая вызывается, когда процесс получает сигнал.

| Сигнал           | Описание                           | Действие по умолчанию |
|------------------|------------------------------------|-----------------------|
| `signal.SIGINT`  | Прерывание (обычно `CTRL+C`)       | Завершение процесса   |
| `signal.SIGTERM` | Завершение процесса                | Завершение процесса   |
| `signal.SIGKILL` | Принудительное завершение процесса | Завершение процесса   |
| `signal.SIGALRM` | Таймер истек                       | Завершение процесса   |
| `signal.SIGHUP`  | Обрыв связи                        | Завершение процесса   |
| `signal.SIGUSR1` | Пользовательский сигнал 1          | Завершение процесса   |
| `signal.SIGUSR2` | Пользовательский сигнал 2          | Завершение процесса   |

> **Примечание:** Сигнал `SIGKILL` нельзя перехватить или игнорировать.

# Установка обработчика сигнала

Для установки обработчика используется функция `signal.signal()`:

```python
def handler(signum, frame):
    print(f"Сигнал {signum} получен")

signal.signal(signal.SIGINT, handler)
```

- `signum`: номер сигнала.
- `frame`: текущее состояние стека (можно игнорировать).

# Игнорирование сигналов

Сигнал можно игнорировать, установив обработчик в `signal.SIG_IGN`:

```python
signal.signal(signal.SIGINT, signal.SIG_IGN)
```

# Восстановление стандартного обработчика

```python
signal.signal(signal.SIGINT, signal.SIG_DFL)
```

# Отправка сигналов процессу

Для отправки сигнала процессу используется функция [[Languages/Python/Libraries/System/os/]]`.kill()`:

```python
import os
os.kill(os.getpid(), signal.SIGTERM)
```

- `os.getpid()` возвращает ID текущего процесса.
- `signal.SIGTERM` — сигнал завершения.

# Работа с таймерами

Функция `signal.alarm()` устанавливает таймер, который отправляет сигнал `SIGALRM` после указанного времени:

```python
signal.alarm(5)  # Через 5 секунд процесс получит сигнал SIGALRM
```

- `signal.alarm(0)` отменяет таймер.

# Ожидание сигнала

Функция `signal.pause()` блокирует выполнение программы до получения сигнала:

```python
signal.pause()  # Ожидание сигнала
```

## Пример использования

```python
import signal
import time

# Обработчик сигнала
def handler(signum, frame):
    print(f"Сигнал {signum} получен. Прерывание программы.")

# Устанавливаем обработчик для SIGINT
signal.signal(signal.SIGINT, handler)

print("Программа работает. Нажмите Ctrl+C для прерывания.")

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("Программа завершена.")

```

Этот пример перехватывает сигнал `SIGINT` (`Ctrl+C`) и выполняет пользовательский обработчик,
который выводит сообщение о получении сигнала.

# Часто используемые функции

| Функция                          | Описание                                                                 |
|----------------------------------|--------------------------------------------------------------------------|
| `signal.signal(signum, handler)` | Устанавливает обработчик для сигнала                                     |
| `signal.getsignal(signum)`       | Возвращает текущий обработчик сигнала                                    |
| `signal.pause()`                 | Останавливает выполнение до получения сигнала                            |
| `signal.alarm(seconds)`          | Устанавливает таймер для отправки сигнала `SIGALRM` через заданное время |
| `signal.setitimer()`             | Устанавливает высокоточный таймер и отправляет сигнал                    |
| `signal.siginterrupt()`          | Устанавливает, должен ли системный вызов быть прерван сигналом           |

## Пример работы с таймером

```python
import signal

def timeout_handler(signum, frame):
    print("Таймер истек!")

# Устанавливаем обработчик для SIGALRM
signal.signal(signal.SIGALRM, timeout_handler)

# Устанавливаем таймер на 5 секунд
signal.alarm(5)

print("Ожидание сигнала...")

# Ожидание сигнала
signal.pause()
```

Этот пример устанавливает таймер на 5 секунд и ждет его истечения.
Когда таймер истекает, вызывается обработчик `timeout_handler`.

## Полезные замечания

1. **Обработчики сигналов**: Старайтесь минимизировать выполнение кода в обработчиках сигналов,
так как они могут быть вызваны в любой момент, что может привести к непредсказуемому поведению.
2. **Портируемость**: Библиотека `signal` доступна только в Unix-подобных системах (Linux, macOS).
На Windows поддерживаются лишь некоторые функции, такие как `signal.SIGINT`.
3. **Сигналы и потоки**: Сигналы обрабатываются в главном потоке. Если ваш процесс использует несколько потоков,
убедитесь, что обработка сигналов не нарушает работу приложения.

""",
                    "io": """
Библиотека io в Python предоставляет возможности работы с потоками ввода-вывода.

io.StringIO() - создание в памяти строкового потока.

```python
import io

stream = io.StringIO()
stream.write("Hello, world!")
stream.seek(0)
print(stream.read())  # Hello, world!
```

io.BytesIO() - создание в памяти потока байт.

```python
import io

stream = io.BytesIO()
stream.write(b"Hello, world!")
stream.seek(0)
print(stream.read())  # b"Hello, world!"
```

io.open() - открытие файла в нужном режиме.

```python
import io

with io.open("example.txt", "w") as f:
    f.write("Hello, world!")

with io.open("example.txt", "r") as f:
    print(f.read())  # Hello, world!
```

io.TextIOWrapper() - обертка для текстовых потоков.

```python
import io

with io.open("example.txt", "w") as f:
    wrapper = io.TextIOWrapper(f, encoding="utf-8")
    wrapper.write("Привет, мир!")

with io.open("example.txt", "r") as f:
    wrapper = io.TextIOWrapper(f, encoding="utf-8")
    print(wrapper.read())  # Привет, мир!
```

io.BufferedWriter() - буферизированный записывающий поток.

```python
import io

with io.open("example.txt", "wb") as f:
    writer = io.BufferedWriter(f)
    writer.write(b"Hello, world!")

with io.open("example.txt", "rb") as f:
    reader = io.BufferedReader(f)
    print(reader.read())  # b"Hello, world!"
```

io.BufferedReader() - буферизированный читающий поток.

```python
import io

with io.open("example.txt", "wb") as f:
    f.write(b"Hello, world!")

with io.open("example.txt", "rb") as f:
    reader = io.BufferedReader(f)
    print(reader.read())  # b"Hello, world!"
```

io.FileIO() - создание потока для работы с файлом в бинарном режиме.

```python
import io

with io.FileIO("example.txt", "w") as f:
    f.write(b"Hello, world!")

with io.FileIO("example.txt", "r") as f:
    print(f.read())  # b"Hello, world!"
```

io.TextIOBase() - базовый класс для всех текстовых потоков.

```python
import io

class UpperTextIO(io.TextIOBase):
    def __init__(self, stream):
        self._stream = stream

    def write(self, text):
        self._stream.write(text.upper())

with io.open("example.txt", "w") as f:
    wrapper = io.TextIOWrapper(f, encoding="utf-8")
    upper_wrapper = UpperTextIO(wrapper)
    upper_wrapper.write("hello, world!")
    wrapper.flush()

with io.open("example.txt", "r") as f:
    wrapper = io.TextIOWrapper(f, encoding="utf-8")
    print(wrapper.read())  # HELLO, WORLD!
```

io.StringIO.getvalue() - получение содержимого из строкового потока.

```python
import io

stream = io.StringIO()
stream.write("Hello, world!")
print(stream.getvalue())  # Hello, world!
```

io.BytesIO.getvalue() - получение содержимого из потока байт.

```python
import io

stream = io.BytesIO()
stream.write(b"Hello, world!")
print(stream.getvalue())  # b"Hello, world!"
```

io.TextIOWrapper.detach() - отсоединение потока от обертки.

```python
import io

with io.open("example.txt", "w") as f:
    wrapper = io.TextIOWrapper(f, encoding="utf-8")
    wrapper.write("Hello, world!")
    stream = wrapper.detach()
    stream.write(b"!!!")

with io.open("example.txt", "r") as f:
    wrapper = io.TextIOWrapper(f, encoding="utf-8")
    print(wrapper.read())  # Hello, world!!!
```

io.BufferedRandom() - буферизированный поток с произвольным доступом.

```python
import io

with io.open("example.txt", "wb") as f:
    writer = io.BufferedRandom(f)
    writer.write(b"Hello, world!")
    writer.flush()
    writer.seek(-6, io.SEEK_CUR)
    writer.write(b"Python!")

with io.open("example.txt", "rb") as f:
    reader = io.BufferedReader(f)
    print(reader.read())  # b"Hello, Python!"
```
""",
                },
                "Data types": {
                    "xml": r"""
Библиотека "xml" в Python используется для работы с XML-данными.
Она предоставляет функциональность для чтения, записи, и обработки XML-файлов.

Методы модуля "xml" и его подмодулей:
xml.etree.ElementTree: Позволяет работать с XML-деревом, включая чтение, запись, и обработку XML-элементов.
xml.dom: Предоставляет интерфейсы для работы с DOM (Document Object Model) XML-документов.
xml.sax: Предоставляет SAX (Simple API for XML) интерфейс для обработки XML-документов в потоковом режиме.

Самые часто используемые методы:
xml.etree.ElementTree.parse(file): Читает XML-файл и возвращает корневой элемент дерева.

```python
import xml.etree.ElementTree as ET

tree = ET.parse("file.xml")
root = tree.getroot()
```

xml.etree.ElementTree.Element.findall(tag): Возвращает список элементов с указанным тегом.

```python
import xml.etree.ElementTree as ET

tree = ET.parse("file.xml")
root = tree.getroot()

elements = root.findall("tag")
```

xml.etree.ElementTree.Element.attrib: Возвращает атрибуты элемента в виде словаря.

```python
import xml.etree.ElementTree as ET

tree = ET.parse("file.xml")
root = tree.getroot()

for element in root:
    attributes = element.attrib
    print(attributes)
```

Помните, что без доступа к конкретному XML-файлу, точные примеры кода могут быть недоступны.
""",
                    "jsonschema": r"""
Библиотека "jsonschema" используется для валидации данных в формате JSON по схеме.
Она позволяет проверить, соответствуют ли данные определенным правилам и структуре, заданным в JSON-схеме.

Таблица методов модуля "jsonschema" и их краткое описание:

   Метод          | Описание
   -------------- | --------------------------------------------
   validate       | Проверяет, соответствуют ли данные схеме.
   Draft4Validator | Класс, осуществляющий валидацию на основе JSON-схемы в соответствии с разделом 4 стандарта.
   Draft6Validator | Класс, осуществляющий валидацию на основе JSON-схемы в соответствии с разделом 6 стандарта.
   Draft7Validator | Класс, осуществляющий валидацию на основе JSON-схемы в соответствии с разделом 7 стандарта.
   ValidationError | Класс исключения, возникающего при невалидных данных.
   exceptions     | Подмодуль, содержащий различные классы исключений.

Список самых часто используемых методов "jsonschema" и их краткое описание:

`validate(schema, instance)` - Проверяет, соответствуют ли данные `instance` схеме `schema`.
Возвращает `None`, если данные валидны. В противном случае, возникает исключение `ValidationError`.

```python
from jsonschema import validate

schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "age": {"type": "integer"}
    }
}

data = {
    "name": "John",
    "age": 25
}

try:
    validate(schema, data)
    print("Data is valid.")
except ValidationError as e:
    print("Data is invalid:", e)
```

`Draft4Validator(schema)` - Создает экземпляр валидатора на основе JSON-схемы с использованием стандарта Draft 4.
Используется для последующей валидации данных.

```python
from jsonschema import Draft4Validator

schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "age": {"type": "integer"}
    }
}

validator = Draft4Validator(schema)

data = {
    "name": "John",
    "age": 25
}

for error in validator.iter_errors(data):
    print("Validation error:", error.message)
```
""",
                    "jsonpointer": r"""
Библиотека "jsonpointer" используется для работы с указателями JSON (JSON pointers).
Она предоставляет функциональность для создания, обновления и извлечения данных из JSON-структур с использованием указателей.

Методы модуля "jsonpointer" и их краткое описание:

`resolve_pointer(json_obj, pointer)`: Разрешает указатель JSON и возвращает соответствующее значение из JSON-объекта.
`set_pointer(json_obj, pointer, value)`: Устанавливает значение по указателю JSON в JSON-объекте.
`remove_pointer(json_obj, pointer)`: Удаляет значение по указателю JSON из JSON-объекта.
`list_pointers(json_obj)`: Возвращает список всех указателей JSON в JSON-объекте.
`escape_pointer(pointer)`: Экранирует специальные символы в указателе JSON.

Некоторые из самых часто используемых методов "jsonpointer" и их краткое описание:

`resolve_pointer(json_obj, pointer)`: Разрешает указатель JSON и возвращает соответствующее значение из JSON-объекта.

```python
import jsonpointer

json_obj = {"name": "John", "age": 30}
pointer = "/name"
value = jsonpointer.resolve_pointer(json_obj, pointer)
print(value)  # John
```

`set_pointer(json_obj, pointer, value)`: Устанавливает значение по указателю JSON в JSON-объекте.

```python
import jsonpointer

json_obj = {"name": "John", "age": 30}
pointer = "/name"
value = "Jane"
jsonpointer.set_pointer(json_obj, pointer, value)
print(json_obj)  # {"name": "Jane", "age": 30}
```

`remove_pointer(json_obj, pointer)`: Удаляет значение по указателю JSON из JSON-объекта.

```python
import jsonpointer

json_obj = {"name": "John", "age": 30}
pointer = "/name"
jsonpointer.remove_pointer(json_obj, pointer)
print(json_obj)  # {"age": 30}
```
""",
                    "queue": """
Модуль queue предоставляет различные классы для реализации очередей в Python.
Очереди используются для хранения и управления элементами данных в порядке "первым поступил - первым обслужен".

| Метод          | Описание                                               |
|----------------|--------------------------------------------------------|
| Queue(maxsize) | Создает новую очередь с максимальным размером maxsize. |
| q.put(item)    | Добавляет элемент item в очередь q.                    |
| q.get()        | Удаляет и возвращает элемент из очереди q.             |
| q.empty()      | Возвращает True, если очередь q пуста, иначе False.    |
| q.full()       | Возвращает True, если очередь q полна, иначе False.    |
| q.qsize()      | Возвращает количество элементов в очереди q.           |


**put(item)** Добавляет элемент в очередь.

```python
q = Queue()
q.put(1)
q.put(2)
print(q.qsize())  # 2
```

**get()** Удаляет и возвращает первый элемент из очереди.

```python
q = Queue()
q.put(1)
q.put(2)
print(q.get())  # 1
```

**empty()** Проверяет, пуста ли очередь.

```python
q = Queue()
print(q.empty())  # True
```
""",
                    "enum": r"""
Библиотека "enum" в Python используется для создания и использования перечислений,
которые представляют собой набор именованных значений.
Она облегчает работу с ограниченным набором значений, обеспечивая их типизацию и удобный доступ.

Методы модуля "enum" и его подмодулей:

Модуль "enum":
Enum: Базовый класс для создания перечислений.
auto: Декоратор, который автоматически присваивает значения перечисления.

Подмодуль "Enum":
name: Возвращает имя элемента перечисления.
value: Возвращает значение элемента перечисления.

Подмодуль "IntEnum":
IntEnum: Базовый класс для создания перечислений с целочисленными значениями.

Подмодуль "Flag":
Flag: Базовый класс для создания перечислений с битовыми флагами.
auto: Декоратор, который автоматически присваивает значения флагов.

Некоторые из самых часто используемых методов "enum" и их описание:

Enum.name: Возвращает имя элемента перечисления.
```python
from enum import Enum

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

print(Color.RED.name)  # "RED"
```

Enum.value: Возвращает значение элемента перечисления.
```python
from enum import Enum

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

print(Color.RED.value)  # 1
```

Flag: Базовый класс для создания перечислений с битовыми флагами.
```python
from enum import Flag, auto

class Permissions(Flag):
    READ = auto()
    WRITE = auto()
    EXECUTE = auto()

user_permissions = Permissions.READ | Permissions.WRITE
print(user_permissions)  # <Permissions.READ|WRITE: 3>
```
""",
                    "heapq": r"""
Библиотека "heapq" в Python используется для работы с heapq, имплементации алгоритма
"heap queue" (очереди с приоритетами). Это набор функций для эффективной работы
с "heap" (кучей) - структурой данных, которая обеспечивает быстрый доступ к наименьшему (или наибольшему) элементу.

Вот некоторые методы и подмодули, доступные в библиотеке "heapq":
`heapify(iterable)`: Перестраивает итерируемый объект в кучу.
`heappush(heap, item)`: Добавляет элемент в кучу.
`heappop(heap)`: Извлекает и возвращает наименьший элемент из кучи.
`heappushpop(heap, item)`: Добавляет элемент в кучу и сразу возвращает наименьший элемент.
`heapreplace(heap, item)`: Заменяет наименьший элемент и возвращает его.

Наиболее часто используемые методы в "heapq" включают:
`heappush`: Добавляет элемент в кучу. `heapq.heappush(heap, item)`.
`heappop`: Извлекает и возвращает наименьший элемент из кучи. `smallest = heapq.heappop(heap)`.

Обратите внимание, что описание методов и примеры кода предоставлены в соответствии с
запросом, но использование библиотеки "heapq" может потребовать дополнительных деталей
и контекста в вашем конкретном случае.
""",
                    "graphlib": r"""
Библиотека "graphlib" в Python используется для работы с графами и решения различных задач на графах,
таких как поиск кратчайшего пути, определение связности графа и других алгоритмических задач.

Таблица методов модуля "graphlib" и его подмодулей:

Метод                    | Описание                      
------------------------ | -----------------------------
graphlib.TopologicalSort | Реализует сортировку вершин графа в топологическом порядке.
graphlib.Graph           | Представляет граф и предоставляет методы для добавления вершин и ребер, проверки наличия ребер и других операций.
graphlib.DiGraph         | Представляет ориентированный граф и предоставляет методы для работы с ним, аналогичные методам Graph.
graphlib.find_cycles     | Позволяет найти все циклы в графе и предоставляет их в виде списка.

Список самых частых методов, их краткое описание и

TopologicalSort Сортирует вершины графа в топологическом порядке.

```python
import graphlib

graph = graphlib.Graph()
graph.add_edges_from([(1, 2), (1, 3), (2, 3), (2, 4)])

sorted_vertices = graphlib.TopologicalSort(graph)
print(sorted_vertices)
```

Graph.add_vertex Добавляет новую вершину в граф.

```python
import graphlib

graph = graphlib.Graph()
graph.add_vertex(1)
graph.add_vertex(2)
```

DiGraph.add_edge Добавляет новое ребро между двумя вершинами в ориентированном графе.

```python
import graphlib

graph = graphlib.DiGraph()
graph.add_edge(1, 2)
graph.add_edge(2, 3)
```

find_cycles Находит все циклы в графе и возвращает их в виде списка.

```python
import graphlib

graph = graphlib.Graph()
graph.add_edges_from([(1, 2), (2, 3), (3, 1), (4, 5)])

cycles = graphlib.find_cycles(graph)
print(cycles)
```
""",
                    "wave": r"""
Библиотека "wave" используется в Python для работы с аудиофайлами формата WAV.
Она позволяет открывать,
создавать, записывать и обрабатывать звуковые файлы в формате WAV.
Методы и подмодули библиотеки "wave" и их краткое описание:

wave.open(file, mode): Открывает WAV-файл с указанным именем файла и режимом доступа.
wave.Wave_read.getnchannels(): Возвращает число каналов в WAV-файле (моно или стерео).
wave.Wave_read.getsampwidth(): Возвращает размер образца в байтах.
wave.Wave_read.getframerate(): Возвращает частоту дискретизации аудиофайла.
wave.Wave_read.getnframes(): Возвращает количество фреймов в аудиофайле.
wave.Wave_read.readframes(n): Читает и возвращает n фреймов из аудиофайла.
wave.Wave_write.setnchannels(nchannels): Устанавливает число каналов для нового WAV-файла.
wave.Wave_write.setsampwidth(sampwidth): Устанавливает размер образца для нового WAV-файла.
wave.Wave_write.setframerate(framerate): Устанавливает частоту дискретизации для нового WAV-файла.
wave.Wave_write.writeframesraw(data): Записывает сырые байты аудио-данных в новый WAV-файл.
wave.Wave_write.writeframes(data): Записывает фреймы аудио-данных в новый WAV-файл.


wave.open(file, mode): Открывает WAV-файл для чтения или записи.

```python
import wave

with wave.open("audio.wav", "r") as wav_file:
    # проведите необходимые операции с аудиофайлом
```

wave.Wave_read.getnframes(): Возвращает количество фреймов в аудиофайле.

```python
import wave

with wave.open("audio.wav", "r") as wav_file:
    num_frames = wav_file.getnframes()
    print(f"Number of frames: {num_frames}")
```

wave.Wave_write.writeframes(data): Записывает фреймы аудио-данных в новый WAV-файл.

```python
import wave

new_frames = b"\x00\x00\x00\x00\x00\x00\x00\x00"  # пример сырых байтов аудио-данных

with wave.open("new_audio.wav", "w") as wav_file:
    wav_file.setnchannels(1)  # устанавливаем один канал
    wav_file.setsampwidth(2)  # устанавливаем размер образца в два байта
    wav_file.setframerate(44100)  # устанавливаем частоту дискретизации в 44100 Гц
    wav_file.writeframes(new_frames)  # записываем фреймы в новый WAV-файл
```
""",
                    "netrc": r"""
Библиотека "netrc" в Python используется для работы с файлами .netrc, которые содержат информацию о пользователях,
паролях и хостах для автоматической аутентификации при подключении к удаленным серверам.

Методы модуля "netrc":
`netrc.netrc(file)` - создает объект, представляющий файл .netrc.
`netrc.hosts()` - возвращает список имен хостов из файла .netrc.
`netrc.host(host)` - возвращает объект, представляющий информацию о конкретном хосте.
`netrc.authenticators(host)` - возвращает кортеж с именем пользователя, паролем и аутентификационным методом для указанного хоста.

Самые часто используемые методы:
`netrc.hosts()` - возвращает список хостов из файла .netrc.
`netrc.authenticators(host)` - возвращает информацию об аутентификации для указанного хоста.


`netrc.authenticators(host)`:

```python
import netrc

def get_credentials(hostname):
    credentials = netrc.netrc()
    auth = credentials.authenticators(hostname)
    if auth:
        username, _, password = auth
        return username, password
    else:
        return None

hostname = "example.com"
credentials = get_credentials(hostname)
if credentials:
    username, password = credentials
    print(f"Authenticated on {hostname} with username: {username} and password: {password}")
else:
    print(f"No credentials found for {hostname}")
```
""",
                },
                "Information": {
                    "math": """
# Функции и константы

| Название          | Описание                                                                                                                       | Пример использования                             |
|-------------------|--------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------|
| `acos(x)`         | Возвращает арккосинус                                                                                                          | `math.acos(1)`  # 0.0                            |
| `acosh(x)`        | Возвращает обратный гиперболический косинус                                                                                    | `math.acosh(1)`  # 0.0                           |
| `asin(x)`         | Возвращает арксинус в радианах                                                                                                 | `math.asin(1)`  # 1.5707963267948966             |
| `asinh(x)`        | Возвращает обратный гиперболический синус                                                                                      | `math.asinh(0)`  # 0.0                           |
| `atan(x)`         | Возвращает арктангенс в радианах                                                                                               | `math.atan(1)`  # 0.7853981633974483             |
| `atan2(y, x)`     | Возвращает арктангенс от частного двух аргументов, учитывая квадрант                                                           | `math.atan2(1, 1)`  # 0.7853981633974483         |
| `atanh(x)`        | Возвращает обратный гиперболический тангенс                                                                                    | `math.atanh(0)`  # 0.0                           |
| `cbrt(x)`         | **(В Python 3.11+)** Возвращает кубический корень                                                                              | `math.cbrt(27)`  # 3.0                           |
| `ceil(x)`         | Округляет число `x` до ближайшего целого вверх                                                                                 | `math.ceil(4.2)`  # 5                            |
| `comb(n, k)`      | **(В Python 3.10+)** Возвращает число сочетаний из `n` по `k`                                                                  | `math.comb(5, 2)`  # 10                          |
| `copysign(x, y)`  | Возвращает число `x` с знаком числа `y`                                                                                        | `math.copysign(3, -1)`  # -3.0                   |
| `cos(x)`          | Возвращает косинус угла `x`, выраженного в радианах                                                                            | `math.cos(0)`  # 1.0                             |
| `cosh(x)`         | Возвращает гиперболический косинус                                                                                             | `math.cosh(0)`  # 1.0                            |
| `degrees(x)`      | Преобразует угол `x` из радиан в градусы                                                                                       | `math.degrees(math.pi)`  # 180.0                 |
| `dist(p, q)`      | **(В Python 3.8+)** Возвращает евклидово расстояние<br>между точками `p` и `q`, представленными как кортежи координат          | `math.dist([1, 2], [4, 6])`  # 5.0               |
| `e`               | Константа основание натурального логарифма                                                                                     | `2.718281828459045`                              |
| `erf(x)`          | Возвращает значение функции ошибок для числа `x`                                                                               | `math.erf(1)`  # 0.8427007929497149              |
| `erfc(x)`         | Возвращает дополнительную функцию ошибок для числа `x`                                                                         | `math.erfc(1)`  # 0.15729920705028513            |
| `exp(x)`          | Возвращает значение `e**x`                                                                                                     | `math.exp(1)`  # 2.718281828459045               |
| `exp2(x)`         | **(В Python 3.8+)** Возвращает значение `2**x`                                                                                 | `math.exp2(3)`  # 8.0                            |
| `expm1(x)`        | Возвращает `e**x - 1`                                                                                                          | `math.expm1(0)`  # 0.0                           |
| `fabs(x)`         | Возвращает абсолютное значение в виде числа с плавающей точкой                                                                 | `math.fabs(-5)`  # 5.0                           |
| `factorial(x)`    | Возвращает факториал                                                                                                           | `math.factorial(5)`  # 120                       |
| `floor(x)`        | Округляет до ближайшего целого вниз                                                                                            | `math.floor(4.8)`  # 4                           |
| `fmod(x, y)`      | Возвращает остаток от деления `x` на `y`, используя тот же знак, что и `x`                                                     | `math.fmod(5, 2)`  # 1.0                         |
| `frexp(x)`        | Разлагает число `x` на мантиссу и экспоненту: возвращает кортеж `(m, e)`,<br>такой что `x = m * 2**e` и `0.5 <= abs(m) < 1.0`  | `math.frexp(8)`  # (0.5, 4)                      |
| `fsum(iterable)`  | Возвращает точную сумму чисел из итерируемого объекта.                                                                         | `math.fsum([0.1] * 10)`  # 1.0                   |
| `gamma(x)`        | Возвращает гамма-функцию                                                                                                       | `math.gamma(5)`  # 24.0                          |
| `gcd(x, y)`       | Возвращает наибольший общий делитель                                                                                           | `math.gcd(8, 12)`  # 4                           |
| `hypot(x, y)`     | Возвращает гипотенузу треугольника с катетами `x` и `y`, то есть `sqrt(x**2 + y**2)`                                           | `math.hypot(3, 4)`  # 5.0                        |
| `inf`             | Положительная бесконечность `float("inf")`                                                                                     | `inf`                                            |
| `isclose(a, b)`   | Проверяет, близки ли два числа `a` и `b` с учётом относительной и абсолютной точности                                          | `math.isclose(0.1 + 0.2, 0.3)`  # True           |
| `isfinite(x)`     | Возвращает `True`, если число конечно (не бесконечное и не `NaN`)                                                              | `math.isfinite(1.0)`  # True                     |
| `isinf(x)`        | Возвращает `True`, если число бесконечное                                                                                      | `math.isinf(float('inf'))`  # True               |
| `isnan(x)`        | Возвращает `True`, если число не является числом (`NaN`)                                                                       | `math.isnan(float('nan'))`  # True               |
| `isqrt(n)`        | **(В Python 3.8+)** Возвращает целочисленный квадратный корень                                                                 | `math.isqrt(16)`  # 4                            |
| `lcm(*args)`      | **(В Python 3.9+)** Возвращает наименьшее общее кратное всех переданных аргументов                                             | `math.lcm(4, 6)`  # 12                           |
| `ldexp(x, i)`     | Возвращает `x * (2**i)`                                                                                                        | `math.ldexp(1.5, 2)`  # 6.0                      |
| `lgamma(x)`       | Возвращает натуральный логарифм гамма-функции                                                                                  | `math.lgamma(5)`  # 3.1780538303479458           |
| `log(x, base)`    | Возвращает логарифм по основанию `base` <br>Если основание не указано, используется натуральный логарифм (`e`)                 | `math.log(8, 2)`  # 3.0                          |
| `log10(x)`        | Возвращает логарифм по основанию 10                                                                                            | `math.log10(100)`  # 2.0                         |
| `log1p(x)`        | Возвращает `log(1 + x)` с высокой точностью для малых значений `x`                                                             | `math.log1p(0.0001)`  # 0.00009999500033334777   |
| `log2(x)`         | Возвращает логарифм по основанию 2                                                                                             | `math.log2(8)`  # 3.0                            |
| `modf(x)`         | Возвращает кортеж из дробной и целой части                                                                                     | `math.modf(3.14)`  # (0.14000000000000012, 3.0)  |
| `nan`             | Представление "Не число" (`NaN`) `float('nan')`                                                                                | `print(math.nan)`  # nan                         |
| `nextafter(x, y)` | Возвращает ближайшее число к `x`, направленное в сторону `y`                                                                   | `math.nextafter(1.0, 2.0)`  # 1.0000000000000002 |
| `perm(n, k)`      | **(В Python 3.8+)** Возвращает число перестановок из `n` по `k`                                                                | `math.perm(5, 2)`  # 20                          |
| `pi`              | Константа π (приблизительно 3.141592653589793)                                                                                 | `print(math.pi)`  # 3.141592653589793            |
| `pow(x, y)`       | Возвращает результат возведения числа `x` в степень `y`                                                                        | `math.pow(2, 3)`  # 8.0                          |
| `prod(iterable)`  | **(В Python 3.8+)** Возвращает произведение всех элементов итерируемого объекта                                                | `math.prod([1, 2, 3, 4])`  # 24                  |
| `radians(x)`      | Преобразует угол из градусов в радианы                                                                                         | `math.radians(180)`  # 3.141592653589793         |
| `remainder(x, y)` | Возвращает остаток от деления `x` на `y`, аналогично оператору `%`, но с учетом знака делимого                                 | `math.remainder(5, 3)`  # -1.0                   |
| `sin(x)`          | Возвращает синус угла, выраженного в радианах                                                                                  | `math.sin(math.pi / 2)`  # 1.0                   |
| `sinh(x)`         | Возвращает гиперболический синус                                                                                               | `math.sinh(0)`  # 0.0                            |
| `sqrt(x)`         | Возвращает квадратный корень                                                                                                   | `math.sqrt(16)`  # 4.0                           |
| `tan(x)`          | Возвращает тангенс угла, выраженного в радианах                                                                                | `math.tan(math.pi / 4)`  # 0.9999999999999999    |
| `tanh(x)`         | Возвращает гиперболический тангенс                                                                                             | `math.tanh(0)`  # 0.0                            |
| `tau`             | Константа τ (2π, приблизительно 6.283185307179586)                                                                             | `math.tau`  # 6.283185307179586                  |
| `trunc(x)`        | Округляет число `x` до ближайшего целого, отбрасывая дробную часть                                                             | `math.trunc(4.9)`  # 4                           |
| `ulp(x)`          | Возвращает расстояние до следующего числа с плавающей точкой после `x`                                                         | `math.ulp(1.0)`  # 2.220446049250313e-16         |


# Примеры


### Работа с тригонометрическими функциями
```python
import math

angle_deg = 45
angle_rad = math.radians(angle_deg)

sin_val = math.sin(angle_rad)
cos_val = math.cos(angle_rad)
tan_val = math.tan(angle_rad)

print(f"Sin({angle_deg}°) = {sin_val}")  # Sin(45°) = 0.7071067811865475
print(f"Cos({angle_deg}°) = {cos_val}")  # Cos(45°) = 0.7071067811865476
print(f"Tan({angle_deg}°) = {tan_val}")  # Tan(45°) = 0.9999999999999999
```

### Проверка близости чисел
```python
import math

a = 0.1 + 0.2
b = 0.3

if math.isclose(a, b):
    print("Числа близки!")  # Числа близки!
else:
    print("Числа не близки!")
```

### Вычисление факториала и гамма-функции
```python
import math

n = 5
fact = math.factorial(n)
gamma_val = math.gamma(n + 1)  # gamma(n) = (n-1)!

print(f"Факториал {n}: {fact}")         # Факториал 5: 120
print(f"Gamma({n + 1}): {gamma_val}")   # Gamma(6): 120.0
```

### Использование функции `prod` для вычисления произведения элементов
```python
import math

numbers = [1, 2, 3, 4]
product = math.prod(numbers)
print(f"Произведение элементов: {product}")  # Произведение элементов: 24
```

### Работа с бесконечностями и `NaN`
```python
import math

positive_inf = math.inf
negative_inf = -math.inf
not_a_number = math.nan

print(math.isinf(positive_inf))  # True
print(math.isinf(negative_inf))  # True
print(math.isnan(not_a_number))  # True
```

### Преобразование между градусами и радианами
```python
import math

angle_deg = 90
angle_rad = math.radians(angle_deg)
converted_deg = math.degrees(angle_rad)

print(f"{angle_deg} градусов = {angle_rad} радиан")     # 90 градусов = 1.5707963267948966 радиан
print(f"{angle_rad} радиан = {converted_deg} градусов")  # 1.5707963267948966 радиан = 90.0 градусов
```


# Пояснения к функциям и константам

### `acos(x)`, `asin(x)`, `atan(x)`
- Арккосинус, арксинус и арктангенс возвращают угол в радианах, соответствующий данному тригонометрическому значению.
- Область определения:
    - `acos(x)`, `asin(x)` — `x` должен быть в диапазоне [-1, 1].
    - `atan(x)` — любое вещественное число.

### `acosh(x)`, `asinh(x)`, `atanh(x)`
- Обратные гиперболические функции.
- Область определения:
    - `acosh(x)` — `x` >= 1.
    - `atanh(x)` — `-1 < x < 1`.

### `cbrt(x)`
- Вычисляет кубический корень числа `x`.
- Доступен начиная с Python 3.11.

### `ceil(x)` и `floor(x)`
- `ceil(x)` округляет число вверх до ближайшего целого.
- `floor(x)` округляет число вниз до ближайшего целого.

### `comb(n, k)` и `perm(n, k)`
- `comb(n, k)` возвращает количество сочетаний из `n` по `k`.
- `perm(n, k)` возвращает количество перестановок из `n` по `k`.
- Доступны начиная с Python 3.8 и 3.10 соответственно.

### `copysign(x, y)`
- Возвращает число `x` с знаком `y`.
- Полезно для переноса знака при сохранении величины числа.

### `cos(x)`, `sin(x)`, `tan(x)` и их гиперболические аналоги `cosh(x)`, `sinh(x)`, `tanh(x)`
- Тригонометрические и гиперболические функции, работающие с углами, выраженными в радианах.

### `degrees(x)` и `radians(x)`
- Преобразуют углы между градусами и радианами.

### `dist(p, q)`
- Вычисляет евклидово расстояние между двумя точками `p` и `q`.

### `erf(x)` и `erfc(x)`
- Функция ошибок и её дополнение, используемые в статистике и теории вероятностей.

### `exp(x)`, `exp2(x)`, `expm1(x)`
- Экспоненциальные функции.
- `expm1(x)` вычисляет `e**x - 1` с высокой точностью для малых `x`.

### `fabs(x)`
- Возвращает абсолютное значение числа `x` как число с плавающей точкой.

### `factorial(x)`
- Вычисляет факториал числа `x`.

### `fmod(x, y)` и `remainder(x, y)`
- `fmod(x, y)` возвращает остаток от деления `x` на `y`, сохраняя знак `x`.
- `remainder(x, y)` возвращает остаток от деления с учётом знака делимого.

### `frexp(x)` и `ldexp(x, i)`
- `frexp(x)` разлагает число на мантиссу и экспоненту.
- `ldexp(x, i)` возвращает `x * (2**i)`.

### `fsum(iterable)`
- Возвращает точную сумму элементов итерируемого объекта, минимизируя ошибки округления.

### `gamma(x)` и `lgamma(x)`
- Гамма-функция и её логарифм.

### `gcd(x, y)` и `lcm(*args)`
- `gcd(x, y)` вычисляет наибольший общий делитель.
- `lcm(*args)` вычисляет наименьшее общее кратное для всех аргументов.

### `hypot(x, y)`
- Вычисляет гипотенузу прямоугольного треугольника с катетами `x` и `y`.

### `inf` и `nan`
- `inf` представляет бесконечность.
- `nan` представляет "Не число".

### `isclose(a, b)`
- Проверяет, близки ли два числа с учётом заданной точности.

### `isfinite(x)`, `isinf(x)`, `isnan(x)`
- Проверяют свойства числа: конечное ли оно, бесконечное или `NaN`.

### `isqrt(n)`
- Возвращает целочисленный квадратный корень числа `n`.

### `modf(x)`
- Разделяет число на дробную и целую части.

### `nextafter(x, y)`
- Возвращает ближайшее число к `x`, направленное в сторону `y`.

### `perm(n, k)`
- Вычисляет количество перестановок из `n` по `k`.

### `pi`, `e`, `tau`
- `pi` — число π.
- `e` — основание натурального логарифма.
- `tau` — число τ (2π).

### `pow(x, y)`
- Возводит `x` в степень `y`.

### `prod(iterable)`
- Возвращает произведение всех элементов итерируемого объекта.

### `radians(x)` и `degrees(x)`
- Преобразуют углы между градусами и радианами.

### `remainder(x, y)`
- Возвращает остаток от деления `x` на `y`, аналогично оператору `%`, но с учетом знака делимого.

### `sin(x)`, `sinh(x)`, `cos(x)`, `cosh(x)`, `tan(x)`, `tanh(x)`
- Тригонометрические и гиперболические функции.

### `trunc(x)`
- Округляет число `x` до ближайшего целого, отбрасывая дробную часть.

### ulp(x)
- Возвращает расстояние до следующего числа с плавающей точкой после `x`.


# Дополнительные примеры использования функций

### Проверка, является ли число бесконечным или `NaN`
```python
print(math.isinf(float("inf")))  # True
print(math.isnan(float("nan")))  # True
```

### gamma
```python
import math

x = 5
gamma_val = math.gamma(x)
print(f"Gamma({x}) равен {gamma_val}")  # Gamma(5) равен 24.0
```

### Использование функции `prod` для вычисления произведения элементов

```python
import math

numbers = [2, 3, 4]
product = math.prod(numbers)
print(f"Произведение элементов {numbers} равно {product}")  # 24
```

### Вычисление гипотенузы и угла в треугольнике
```python
import math

a = 3
b = 4

# Гипотенуза
c = math.hypot(a, b)
print(f"Гипотенуза равна {c}")  # 5.0

# Угол при катете a
angle_rad = math.atan2(b, a)
angle_deg = math.degrees(angle_rad)
print(f"Угол при катете a: {angle_deg}°")  # 53.13010235415598°
```

### Использование функции `isclose` для проверки близости чисел
```python
import math

a = 0.1 + 0.2
b = 0.3

if math.isclose(a, b):
    print("Числа близки")  # Числа близки
else:
    print("Числа не близки")
```

### Рассчет значения `ulp` (Unit in the Last Place)
```python
import math

x = 1.0
ulp_val = math.ulp(x)
print(f"ULP для {x} равен {ulp_val}")  # 2.220446049250313e-16
```

# Константы

| Константа  | Описание                                                             | Пример использования |
|------------|----------------------------------------------------------------------|----------------------|
| `math.pi`  | Число `π`, приблизительно `3.141592653589793`                        | `3.141592653589793`  |
| `math.e`   | Основание натурального логарифма, приблизительно `2.718281828459045` | `2.718281828459045`  |
| `math.tau` | Число `τ` (**2π**), приблизительно `6.283185307179586`               | `6.283185307179586`  |
| `math.inf` | Представляет положительную бесконечность                             | `inf`                |
| `math.nan` | Представляет "Не число" (`NaN`)                                      | `nan`                |


# Ссылки

- [Официальная документация](https://docs.python.org/3/library/math.html)
- [Real Python - Math Module](https://realpython.com/python-math-module/)
- [Документация по функциям и константам](https://docs.python.org/3/library/math.html#module-math)


# Полезные советы

- **Работа с углами**: Всегда помните, что тригонометрические функции
(`sin`, `cos`, `tan` и др.) работают с углами, выраженными в радианах.
Используйте `math.radians()` и `math.degrees()` для преобразования между градусами и радианами.
- **Числа с плавающей точкой**: При работе с числами с плавающей точкой (`float`)
учитывайте возможные ошибки округления. Функция `math.isclose()`
поможет проверить близость чисел с учётом заданной точности.
- **Оптимизация производительности**: Некоторые функции, такие как `math.isqrt()`,
предоставляют оптимизированные способы выполнения операций, что особенно полезно для больших чисел или частых вызовов функций.
- **Гамма-функция**: Функции `math.gamma()` и `math.lgamma()` полезны в статистике
и математике для работы с непрерывными распределениями и факториалами вещественных чисел.

""",
                    "textwrap": """
Функция textwrap.wrap из модуля textwrap в Python используется 
для разбиения текстовой строки на список строк с заданной шириной столбца.

Например, если у вас есть длинная строка и вы хотите разбить ее на строки 
с длиной в 10 символов, вы можете использовать textwrap.wrap следующим образом:

```python
import textwrap

long_string = "This is a very long string that needs to be wrapped."
wrapped_string = textwrap.wrap(long_string, width=10)

print(wrapped_string)
# ["This is a", "very long", "string", "that needs", "to be", "wrapped."]
```

Кроме textwrap.wrap, модуль textwrap также содержит другие функции, такие как:

textwrap.fill        эта функция принимает строку и ширину столбца и возвращает отформатированную строку, где каждая строка имеет не более заданного количества символов.
textwrap.indent      эта функция принимает строку и префикс, который нужно добавить к каждой строке, и возвращает новую строку с добавленным префиксом.
textwrap.shorten     эта функция принимает строку и максимальную длину, которую должна иметь итоговая строка. 
                     Если исходная строка длиннее, то она обрезается и добавляется многоточие в конце.
textwrap.dedent      эта функция удаляет общий префикс всех строк в тексте, чтобы сделать его более компактным.
textwrap.TextWrapper это класс, который представляет настройки форматирования текста, такие как ширина столбца, префикс, отступы и другие параметры. 
                     Вы можете использовать этот класс, чтобы создать экземпляр объекта, который может быть использован для форматирования нескольких строк текста.
""",
                    "datetime": """
| Формат | Значение                                          |
|--------|---------------------------------------------------|
| `%a`   | Название дня недели в сокращенном виде            |
| `%A`   | Название дня недели в полном виде                 |
| `%w`   | Номер дня недели в виде целого числа              |
| `%d`   | Номер дня месяца в виде целого числа              |
| `%b`   | Название месяца в сокращенном виде                |
| `%B`   | Название месяца в полном виде                     |
| `%m`   | Номер месяца в числовом представлении             |
| `%y`   | Номер года без столетия                           |
| `%Y`   | Номер года в полном представлении                 |
| `%H`   | Количество часов в 24-часовом формате             |
| `%I`   | Количество часов в 12-часовом формате             |
| `%p`   | До полудня или после полудня в 12-часовом формате |
| `%M`   | Количество минут в виде целого числа              |
| `%S`   | Количество секунд в виде целого числа             |
| `%f`   | Количество микросекунд в виде целого числа        |
| `%z`   | Часовой пояс в формате UTC                        |
| `%Z`   | Название часового пояса                           |
| `%j`   | Номер дня в году                                  |
| `%U`   | Номер недели в году, если считать с воскресенья   |
| `%w`   | Номер недели в году, если считать с понедельника  |
| `%c`   | Местное представление даты и времени              |
| `%x`   | Местное представление даты                        |
| `%X`   | Местное представление времени                     |
| `%%`   | Символ процента                                   |

![datetime.png](Languages/Python/Libraries/datetime.png)
""",
                    "decimal": """
from decimal import Decimal

Библиотека decimal предоставляет более точный способ работы с десятичными числами, чем встроенные типы данных float и double. 
Она позволяет представлять числа с фиксированной точностью и позволяет управлять точностью вычислений. 
Это может быть полезно в тех случаях, когда требуется точный результат, например, при финансовых расчетах.

Класс Decimal
Класс Decimal используется для создания и работы с десятичными числами с фиксированной точностью. Вот несколько примеров:i

```python
from decimal import Decimal

# Создание десятичного числа
a = Decimal("10.5")

# Арифметические операции
b = Decimal("2")
a + b  # 12.5
a - b  # 8.5
a * b  # 21.0
a / b  # 5.25

# Округление
a.quantize(Decimal("1.00"))  # 10.50
a.quantize(Decimal("0.1"))   # 10.5

# Преобразование в разные форматы
a.to_eng_string()     # "10.5"
a.as_integer_ratio()  # (21, 2)
```

Класс Context
Класс Context представляет контекст округления, который управляет поведением операций с десятичными числами. Вот несколько примеров:

```python
from decimal import Decimal, Context

# Создание контекста округления
ctx = Context(prec=3, rounding=ROUND_HALF_UP)

# Создание десятичного числа с использованием контекста
a = Decimal("10.5", context=ctx)

# Арифметические операции с использованием контекста
b = Decimal("2", context=ctx)
c = a + b
d = a - b
e = a * b
f = a / b

# Округление с использованием контекста
g = a.quantize(Decimal("1.00"), context=ctx)
h = a.quantize(Decimal("0.1"), context=ctx)
```

Функции округления
Модуль decimal также предоставляет несколько функций округления, которые можно использовать с десятичными числами. Вот несколько примеров:

```python
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_DOWN, ROUND_CEILING, ROUND_FLOOR

a = Decimal("10.555")

# Округление до двух знаков с округлением до ближайшего
a.quantize(Decimal("1.00"), rounding=ROUND_HALF_UP)  # 10.56    

# Округление до двух знаков с округлением в меньшую сторону
a.quantize(Decimal("1.00"), rounding=ROUND_FLOOR)  # 10.55

# Округление до целого числа, округление до ближайшего
a.quantize(Decimal("1"), rounding=ROUND_HALF_UP)  # 11

# Округление до целого числа, округление в большую сторону
a.quantize(Decimal("1"), rounding=ROUND_CEILING)  # 11
```
""",
                    "fractions": """
from fractions import Fraction

Модуль fractions предоставляет класс Fraction, который позволяет работать с дробными числами в виде объектов.
Класс Fraction позволяет представлять дробное число в виде числителя и знаменателя. 
Он автоматически упрощает дробь, позволяет выполнять арифметические операции с дробями 
и конвертировать дроби в различные форматы (например, вещественные числа или строки).

Вот примеры использования класса Fraction:

```python
from fractions import Fraction

# создание дроби с помощью числителя и знаменателя
print(Fraction(3, 4))    # 3/4

# создание дроби из вещественного числа
print(Fraction(0.5))    # 1/2

# арифметические операции с дробями
print(Fraction(1, 4) + Fraction(1, 2))    # 3/4

# конвертирование дроби в вещественное число
print(float(Fraction(3, 4)))    # 0.75

# конвертирование дроби в строку
print(str(Fraction(3, 4)))    # "3/4"
```

Класс Fraction может быть полезен в тех случаях, когда требуется более точный 
и удобный способ работы с дробными числами, чем встроенные типы данных. 
Он может использоваться, например, при работе с финансовыми расчетами, 
при расчете вероятностей или в других задачах, связанных с математикой.





Fraction   
Класс для представления рациональных чисел. 
Этот класс позволяет создавать объекты, которые представляют дроби в виде числителя и знаменателя. 
Например, Fraction(3, 4) создаст дробь 3/4.

```python
from fractions import Fraction

print(Fraction(3, 4) + Fraction(1, 2))  # 5/4
```

gcd

Функция для вычисления наибольшего общего делителя двух чисел.

```python
from fractions import gcd

print(gcd(6, 9))  # 3
```

lcm
Функция для вычисления наименьшего общего кратного двух чисел.

```python
from fractions import lcm

print(lcm(6, 9))  # 18
```

limit_denominator
Метод объекта Fraction, который позволяет получить рациональное число, 
ближайшее к данному, с знаменателем не превосходящим указанное значение.

```python
from fractions import Fraction

print(Fraction(7, 12).limit_denominator(5))  # 3/5
```

Fraction.from_float
Метод класса Fraction, который позволяет создать рациональное число, 
представляющее указанное число с плавающей точкой.

```python
from fractions import Fraction

print(Fraction.from_float(0.5))  # 1/2
```

Fraction.from_decimal
Метод класса Fraction, который позволяет создать рациональное число, представляющее указанное десятичное число.

```python
from fractions import Fraction

print(Fraction.from_decimal("0.75"))  # 3/4
```

is_integer
Метод объекта Fraction, который возвращает True, если данная дробь представляет целое число, и False в противном случае.

```python
from fractions import Fraction

print(Fraction(3, 2).is_integer())  # False
print(Fraction(6, 4).is_integer())  # True
```

Fraction.as_integer_ratio
Метод объекта Fraction, который возвращает кортеж из двух целых чисел, 
представляющих данную дробь в виде несократимой простой дроби.

```python
from fractions import Fraction

print(Fraction(5, 15).as_integer_ratio())  # (1, 3)
```

Fraction.from_ratio
Метод класса Fraction, который позволяет создать рациональное число на основе заданного отношения двух целых чисел.

```python
from fractions import Fraction

print(Fraction.from_ratio(5, 15))  # 1/3
```

Fraction.limit_denominator(max_denominator=1000000): 
Метод объекта Fraction, который возвращает рациональное число, ближайшее к данному, 
с знаменателем не превосходящим указанное значение. 
Если аргумент max_denominator не указан, то по умолчанию он равен 1 миллиону.

```python
from fractions import Fraction

print(Fraction(3, 4).limit_denominator(10))  # 1/1
```

Fraction.from_jedec
Метод класса Fraction, который позволяет создать рациональное число на основе заданной строки в формате JEDEC.

```python
from fractions import Fraction

print(Fraction.from_jedec("1/2"))  # 1/2
```

Fraction.from_tuple
Метод класса Fraction, который позволяет создать рациональное число на основе заданного кортежа из двух целых чисел (числителя и знаменателя).

```python
from fractions import Fraction

print(Fraction.from_tuple((3, 4)))  # 3/4
```
""",
                    "difflib": r'''
#### SequenceMatcher
Сравнение двух последовательностей и определение степени их сходства.

```python
import difflib

s1 = "Hello, world!"
s2 = "Hello, everyone!"

matcher = difflib.SequenceMatcher(None, s1, s2)
ratio = matcher.ratio()

print(f"Similarity ratio: {ratio}")

"""Similarity ratio: 0.6206896551724138"""
```


#### get_close_matches
Нахождение наиболее похожей строки в наборе строк на основе заданной строки.

```python
import difflib

colors = ["red", "green", "blue", "yellow"]
color = "grea"

matches = difflib.get_close_matches(color, colors)

print(f"Closest matches: {matches}")

"""Closest matches: ["green"]"""
```


#### unified_diff
Генерация отчета о различиях между двумя последовательностями.

```python
import difflib

text1 = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."""

text2 = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt ut labore et dolore magnus aliqua."""

d = difflib.unified_diff(text1.splitlines(), text2.splitlines())

print("\n".join(d))

"""
---

+++

@@ -1,3 +1,3 @@

 Lorem ipsum dolor sit amet,
 consectetur adipiscing elit,
-sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
+sed do eiusmod tempor incididunt ut labore et dolore magnus aliqua.
"""
```

#### HtmlDiff
Генерация отчета о различиях между двумя последовательностями в формате HTML.

```python
import difflib

text1 = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."""

text2 = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt ut labore et dolore magnus aliqua."""

d = difflib.HtmlDiff().make_file(text1.splitlines(), text2.splitlines())

with open("diff.html", "w") as f:
    f.writelines(d)
```














#### context_diff
Генерация отчета о различиях между двумя последовательностями в формате context diff.

```python
import difflib

text1 = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."""

text2 = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt ut labore et dolore magnus aliqua."""

d = difflib.context_diff(text1.splitlines(), text2.splitlines())

print("\n".join(d))

"""
***

---

***************

*** 1,3 ****

  Lorem ipsum dolor sit amet,
  consectetur adipiscing elit,
! sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
--- 1,3 ----

  Lorem ipsum dolor sit amet,
  consectetur adipiscing elit,
! sed do eiusmod tempor incididunt ut labore et dolore magnus aliqua.
"""
```

#### ndiff
Генерация отчета о различиях между двумя последовательностями в формате ndiff.

```python
import difflib

text1 = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."""

text2 = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt ut labore et dolore magnus aliqua."""

d = difflib.ndiff(text1.splitlines(), text2.splitlines())

print("\n".join(d))

"""
  Lorem ipsum dolor sit amet,
  consectetur adipiscing elit,
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
?                                                          ^

+ sed do eiusmod tempor incididunt ut labore et dolore magnus aliqua.
?                                                          ^^       
"""
```

#### isjunk и ignore
Использование пользовательских функций для игнорирования символов при сравнении последовательностей.

```python
import difflib

def isjunk(s):
    return s in [" ", "\n"]

text1 = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."""

text2 = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt ut labore et dolore magnus aliqua."""

matcher = difflib.SequenceMatcher(isjunk, text1, text2)
ratio = matcher.ratio()

print(f"Similarity ratio: {ratio}")

"""Similarity ratio: 0.9878542510121457"""
```

#### reduce_func
Использование пользовательской функции для преобразования различий в отчете о сравнении.

```python
import difflib

text1 = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."""

text2 = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt ut labore et dolore magnus aliqua."""

d = difflib.Differ()
diff = d.compare(text1.splitlines(), text2.splitlines())

def reduce_func(s):
    if s.startswith("- "):
        return f"<span style="color:red">{s}</span>"
    elif s.startswith("+ "):
        return f"<span style="color:green">{s}</span>"
    else:
        return s

diff = map(reduce_func, diff)
diff = "\n".join(diff)

print(diff)

"""
  Lorem ipsum dolor sit amet,
  consectetur adipiscing elit,
<span style="color:red">- sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</span>
?                                                          ^

<span style="color:green">+ sed do eiusmod tempor incididunt ut labore et dolore magnus aliqua.</span>
?                                                          ^^                                         
"""
```
''',
                    "random": """
Модуль random в Python предоставляет функции для генерации случайных чисел и последовательностей. 
Ниже приведен список некоторых из наиболее часто используемых функций:

random()                       - возвращает случайное число с плавающей запятой в диапазоне [0.0, 1.0).
randint(a, b)                  - возвращает случайное целое число в диапазоне [a, b], включая границы.
uniform(a, b)                  - возвращает случайное число с плавающей запятой в диапазоне [a, b).
randrange(start, stop[, step]) - возвращает случайный элемент из диапазона, созданного с использованием аргументов start, stop и step.
choice(seq)                    - возвращает случайный элемент из последовательности seq.
shuffle(seq)                   - перемешивает элементы последовательности seq в произвольном порядке.
sample(population, k)          - возвращает список длиной k из уникальных элементов случайно выбранных из population.

getstate() и setstate(state)   - используются для сохранения и восстановления внутреннего состояния генератора случайных чисел. 
                                 Состояние генератора включает в себя информацию, необходимую для воспроизведения последовательности случайных чисел.
getrandbits(k)                 - возвращает целое число, состоящее из k случайных битов.
choices(population, weights=None, *, cum_weights=None, k=1) 
                               - выбирает k элементов из population с возможностью задания весов для каждого элемента. 
                                 Функция может использоваться для случайной выборки элементов с заменой из набора данных, 
                                 где некоторые элементы могут быть выбраны чаще, чем другие.
randbytes(n) - возвращает n случайных байтов.

Это только некоторые функции, доступные в модуле random. 
Существует также много других функций, таких как seed(), gauss(), triangular(), betavariate(), expovariate() и многие другие. 
Вы можете получить дополнительную информацию о модуле random и его функциях в официальной документации Python.
""",
                    "PIL": {
                        "ImageDraw.Draw": """
```python
from PIL import Image
from PIL.ImageDraw import Draw

image = Image.open(r"")
draw = ImageDraw.Draw(image)
draw = Draw(image)
```

```python
[print(x) for x in dir(draw)]
```

arc                 Рисует дугу (часть "пончика") на изображении. 
                    Принимает четыре аргумента: координаты прямоугольника, в котором находится дуга, начальный и конечный углы (в градусах), а также цвет линии.

bitmap              Рисует изображение в виде битовой карты на текущем изображении. 
                    Принимает два аргумента: координаты верхнего левого угла и изображение в формате Bitmap.

chord               Рисует сегмент круга на изображении, соединяя начальную и конечную точки с центром. 
                    Принимает аргументы, аналогичные arc.

draw                Используется для рисования на изображении с помощью кисти. 
                    Принимает два аргумента: изображение и цвет кисти.

ellipse             Рисует эллипс на изображении. 
                    Принимает два аргумента: координаты прямоугольника, в котором находится эллипс, и цвет линии.

fill                Заполняет область на изображении определенным цветом. 
                    Принимает два аргумента: координаты прямоугольника и цвет.

font                Используется для настройки шрифта, который будет использоваться при отрисовке текста. 
                    Принимает аргумент в формате ImageFont. (не работало...)

fontmode            Задает режим отображения текста. Может принимать значения "1" или "L".

getfont             Возвращает текущий шрифт.

im                  Текущее изображение.

ink                 Цвет, используемый для рисования.

line                Рисует линию на изображении. 
                    Принимает два аргумента: координаты начальной и конечной точек и цвет линии.

mode                Режим изображения. 
                    Может принимать значения "1", "L", "P", "RGB" или "CMYK".

multiline_text      Рисует многострочный текст на изображении. 
                    Принимает три аргумента: координаты верхнего левого угла, текст и дополнительные параметры.

multiline_textbbox  Возвращает ограничивающий прямоугольник для многострочного текста. 
                    Принимает те же аргументы, что и multiline_text.

multiline_textsize  Возвращает размер многострочного текста. 
                    Принимает те же аргументы, что и multiline_text.

palette             Палитра изображения.

pieslice            Рисует сегмент пирога на изображении. 
                    Принимает аргументы, аналогичные arc.

point               Рисует точку на изображении. 
                    Принимает аргументы - координаты точки и цвет.

polygon             Рисует многоугольник на изображении. 
                    Принимает два аргумента: список координат вершин многоугольника и цвет линии.

rectangle           Рисует прямоугольник на изображении. 
                    Принимает два аргумента: координаты прямоугольника и цвет линии.

regular_polygon     Рисует правильный многоугольник на изображении. 
                    Принимает три аргумента: центр многоугольника, количество сторон и радиус.

rounded_rectangle   Рисует прямоугольник с закругленными углами на изображении. 
                    Принимает аргументы, аналогичные rectangle.

shape               Рисует многоугольник, который может быть заполнен или обведен. 
                    Принимает два аргумента: список координат вершин многоугольника и цвет.

text                Рисует текст на изображении. 
                    Принимает три аргумента: координаты верхнего левого угла, текст и цвет.

textbbox            Возвращает ограничивающий прямоугольник для текста. 
                    Принимает те же аргументы, что и text.

textlength          Возвращает длину текста. 
                    Принимает два аргумента: текст и шрифт.

textsize            Возвращает размер текста. 
                    Принимает два аргумента: текст и шрифт.
"""
                    },
                    "aalib": """
aalib - это библиотека для создания ASCII-графики из изображений. Она преобразует изображения в искусственные изображения, составленные из символов ASCII.

| Метод                            | Описание                                                             |
|----------------------------------|----------------------------------------------------------------------|
| aalib.AsciiArt                   | Создает объект AsciiArt для конвертации изображений в ASCII-графику. |
| AsciiArt.render(image)           | Преобразует изображение в ASCII-графику.                             |
| AsciiArt.render_to_memory(image) | Возвращает ASCII-графику в виде строки.                              |
| AsciiArt.save(filename, image)   | Сохраняет ASCII-графику в файл.                                      |


**render(image)** - Преобразует изображение в ASCII-графику.

```python
import aalib
import Image  # Предполагается, что у вас уже есть изображение под названием "image.jpg"

img = Image.open("image.jpg").convert("L")
width, height = img.size
ascii_img = aalib.AsciiArt(width=width, height=height)
ascii_img.render(img)
ascii_img.save("output.txt")
```

**render_to_memory(image)** - Возвращает ASCII-графику в виде строки.

```python
import aalib
import Image

img = Image.open("image.jpg").convert("L")
ascii_img = aalib.AsciiArt(width=80, height=40)
ascii_str = ascii_img.render_to_memory(img)
print(ascii_str)
```

**save(filename, image)** - Сохраняет ASCII-графику в файл.

```python
import aalib
import Image

img = Image.open("image.jpg").convert("L")
ascii_img = aalib.AsciiArt(width=80, height=40)
ascii_img.render(img)
ascii_img.save("output.txt", img)
```
""",
                    "argparse": """
Библиотека argparse в Python позволяет легко создавать интерфейсы командной строки для ваших скриптов. 
Эта библиотека предоставляет механизмы для определения аргументов командной строки и автоматического 
генерирования справочной информации и сообщений об ошибках.

Вот несколько примеров использования библиотеки argparse в Python:
Простой скрипт

```python
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("echo", help="echo the string you use here")

args = parser.parse_args()
print(args.echo)
```

Для запуска скрипта нужно использовать команду

```bash
python script.py hello
```

Аргументы с флагами

```python
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--verbosity", help="increase output verbosity", action="store_true")

args = parser.parse_args()
if args.verbosity:
    print("verbosity turned on")
```

Для запуска скрипта нужно использовать команду

```bash
python script.py --verbosity
```

Опциональный аргумент

```python
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--number", help="enter a number", type=int)

args = parser.parse_args()
if args.number:
    print(args.number * 2)
```

Для запуска скрипта нужно использовать команду

```bash
python script.py --number 5
```

Обязательный аргумент

```python
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("filename", help="the name of the file to read")

args = parser.parse_args()
print(args.filename)
```

Для запуска скрипта нужно использовать команду

```bash
python script.py filename.txt
```

Группировка аргументов

```python
import argparse

parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group()
group.add_argument("--verbose", help="increase output verbosity", action="store_true")
group.add_argument("--quiet", help="decrease output verbosity", action="store_true")

args = parser.parse_args()
if args.verbose:
    print("verbosity turned on")
elif args.quiet:
    print("verbosity turned off")
```

Для запуска скрипта нужно использовать команду

```bash
python script.py --verbose или python script.py --quiet
```




Позиционные аргументы с выбором

```python
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("operation", help="operation to perform", choices=["add", "sub", "mul", "div"])
parser.add_argument("num1", help="first number", type=int)
parser.add_argument("num2", help="second number", type=int)

args = parser.parse_args()
if args.operation == "add":
    print(args.num1 + args.num2)
elif args.operation == "sub":
    print(args.num1 - args.num2)
elif args.operation == "mul":
    print(args.num1 * args.num2)
else:
    print(args.num1 / args.num2)
```

Для запуска скрипта нужно использовать команду

```bash
python script.py add 5 3
```

Описание программы и аргументов

```python
import argparse

parser = argparse.ArgumentParser(description="A simple calculator program")
parser.add_argument("operation", help="operation to perform", choices=["add", "sub", "mul", "div"])
parser.add_argument("num1", help="first number", type=int)
parser.add_argument("num2", help="second number", type=int)

args = parser.parse_args()
if args.operation == "add":
    print(args.num1 + args.num2)
elif args.operation == "sub":
    print(args.num1 - args.num2)
elif args.operation == "mul":
    print(args.num1 * args.num2)
else:
    print(args.num1 / args.num2)
```

Для запуска скрипта нужно использовать команду: 

```bash
python script.py --help
```




Парсинг аргументов из файла

```python
import argparse

parser = argparse.ArgumentParser(fromfile_prefix_chars="@")
parser.add_argument("operation", help="operation to perform", choices=["add", "sub", "mul", "div"])
parser.add_argument("num1", help="first number", type=int)
parser.add_argument("num2", help="second number", type=int)

args = parser.parse_args(["@args.txt"])
if args.operation == "add":
    print(args.num1 + args.num2)
elif args.operation == "sub":
    print(args.num1 - args.num2)
elif args.operation == "mul":
    print(args.num1 * args.num2)
else:
    print(args.num1 / args.num2)
```

Для использования данного примера нужно создать файл "args.txt" со следующим содержимым

```text
add 5 3
```

Затем, чтобы запустить скрипт, нужно использовать команду

```bash
python script.py @args.txt
```

Аргумент со значением по умолчанию

```python
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--verbosity", help="increase output verbosity", action="store_true")
parser.add_argument("--num", help="a number", type=int, default=5)

args = parser.parse_args()
if args.verbosity:
    print("verbosity turned on")
print(args.num * 2)
```

Для запуска скрипта нужно использовать команду

```bash
python script.py --verbosity --num 3
```

Поддержка субкоманд

```python
import argparse

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(title="subcommands", dest="subcommand")

parser_a = subparsers.add_parser("command_a", help="command a help")
parser_a.add_argument("foo", type=int, help="foo help")

parser_b = subparsers.add_parser("command_b", help="command b help")
parser_b.add_argument("--bar", type=str, help="bar help")

args = parser.parse_args()
if args.subcommand == "command_a":
    print(args.foo)
else:
    print(args.bar)
```

Для запуска скрипта нужно использовать команду: 

```bash
python script.py command_a 5
```

или

```bash
python script.py command_b --bar test
```
""",
                    "cycler": """
Библиотека cycler в Python используется для создания циклических стилей,
особенно в контексте графиков и диаграмм в библиотеке Matplotlib.

| Метод         | Описание                                                  |
|---------------|-----------------------------------------------------------|
| cycler.cycler | Создает новый циклический объект с заданными параметрами. |

```python
from cycler import cycler

colors = cycler(color=["red", "green", "blue"])
linestyles = cycler(linestyle=["-", "--", "-."])

# Комбинирование циклических стилей
combined_styles = colors + linestyles
```
""",
                    "shlex": r"""
Библиотека "shlex" в Python используется для разбивки строки на токены в соответствии с синтаксисом оболочки Unix.
Она часто применяется при работе с командной строкой, парсинге аргументов командной строки и анализе ввода пользователя.

Методы модуля и их мега краткое описание:

shlex.split(s): Разбивает строку s на токены и возвращает список.
shlex.quote(s): Возвращает квотированную версию строки s с учетом синтаксиса оболочки.
shlex.join(args): Объединяет список аргументов args в одну строку с добавлением кавычек и экранированием.
shlex.shlex([stream[, filename[, posix]]]): Создает объект парсера токенов для чтения из потока stream.
    Опциональные параметры filename и posix устанавливают соответствующие атрибуты парсера.
shlex.push_source(source): Вставляет новый источник токенов в стек парсера.
shlex.pop_source(): Удаляет верхний источник токенов из стека парсера.
shlex.get_token(): Возвращает следующий токен из текущего источника парсера.
shlex.get_token_unquoted(): Возвращает следующий неквотированный токен из текущего источника парсера.

Наиболее часто используемые методы "shlex" вместе с их кратким описанием и примерным кодом:

shlex.split(s): Разбивает строку на токены и возвращает список.
Пример: tokens = shlex.split("hello world")  # ["hello", "world"]

shlex.quote(s): Возвращает квотированную версию строки с учетом синтаксиса оболочки.
Пример: quoted = shlex.quote("Hello, World!")  # "Hello, World!"

shlex.join(args): Объединяет список аргументов в строку с добавлением кавычек и экранированием.
Пример: command = shlex.join(["ls", "-l", "*.txt"])  # 'ls -l "*.txt"'
""",
                    "base64": r"""
Библиотека "base64" в Python используется для кодирования и декодирования данных в формате base64.
Base64 является способом представления двоичных данных в виде текста, что удобно для передачи и хранения данных,
которые не могут быть безопасно переданы в обычном двоичном формате.

Методы модуля "base64" и его подмодулей:

Модуль "base64":
b64encode(data): Кодирует данные в формате base64.
b64decode(data): Декодирует данные из формата base64.
b64encodebytes(data): Кодирует данные в формате base64 и возвращает байтовую строку.
b64decodebytes(data): Декодирует байтовую строку из формата base64 и возвращает декодированные данные.

Подмодуль "base64.urlsafe":
urlsafe_b64encode(data): Кодирует данные в формате base64 для URL без использования символов, которые могут вызывать проблемы в URL.
urlsafe_b64decode(data): Декодирует данные из формата base64 для URL.

Некоторые из самых часто используемых методов "base64" и их краткое описание:

b64encode(data): Кодирует данные в формате base64.

```python
import base64

data = b"Hello, World!"
encoded_data = base64.b64encode(data)
print(encoded_data)
```

b64decode(data): Декодирует данные из формата base64.

```python
import base64

encoded_data = b"SGVsbG8sIFdvcmxkIQ=="
decoded_data = base64.b64decode(encoded_data)
print(decoded_data)
```

urlsafe_b64encode(data): Кодирует данные в формате base64 для URL без использования символов, которые могут вызывать проблемы в URL.

```python
import base64

data = b"Hello, World!"
encoded_data = base64.urlsafe_b64encode(data)
print(encoded_data)
```

urlsafe_b64decode(data): Декодирует данные из формата base64 для URL.

```python
import base64

encoded_data = b"SGVsbG8sIFdvcmxkIQ=="
decoded_data = base64.urlsafe_b64decode(encoded_data)
print(decoded_data)
```
""",
                    "binhex": r"""
Библиотека "binhex" в Python используется для преобразования двоичных данных в шестнадцатеричный формат и обратно.
Она предоставляет функции для кодирования и декодирования данных, а также для чтения и записи файлов в формате binhex.

Методы модуля "binhex" и его подмодулей:

Модуль "binhex":
binhex.hexlify(data): Преобразует двоичные данные в шестнадцатеричный формат.
binhex.unhexlify(hexdata): Преобразует данные из шестнадцатеричного формата в двоичный формат.
binhex.binhex(binfile, hexfile): Кодирует двоичный файл в файл в формате binhex.
binhex.hexbin(hexfile, binfile): Декодирует файл в формате binhex в двоичный файл.

Наиболее часто используемые методы:

binhex.hexlify(data): Преобразует двоичные данные в шестнадцатеричный формат.

```python
import binhex

data = b"Hello, World!"
hex_data = binhex.hexlify(data)
print(hex_data)
```

binhex.unhexlify(hexdata): Преобразует данные из шестнадцатеричного формата в двоичный формат.

```python
import binhex

hex_data = "48656c6c6f2c20576f726c6421"
data = binhex.unhexlify(hex_data)
print(data)
```

binhex.binhex(binfile, hexfile): Кодирует двоичный файл в файл в формате binhex.

```python
import binhex

bin_file = "input.bin"
hex_file = "output.hex"
binhex.binhex(bin_file, hex_file)
```

binhex.hexbin(hexfile, binfile): Декодирует файл в формате binhex в двоичный файл.

```python
import binhex

hex_file = "input.hex"
bin_file = "output.bin"
binhex.hexbin(hex_file, bin_file)
```
""",
                    "xdrlib": r"""
Библиотека "xdrlib" в Python используется для работы с кодированием и декодированием данных в формате XDR (eXternal Data Representation).
XDR является стандартом для представления данных, независимым от платформы, и часто используется для обмена данными между различными системами.

Методы модуля "xdrlib" и его подмодулей:

Модуль "xdrlib":
pack_fstring(format_string, *args): Упаковывает аргументы в соответствии с заданным форматным строкой и возвращает упакованные данные в формате XDR.
unpack_fstring(format_string, packed_data): Распаковывает данные в формате XDR, используя заданную форматную строку, и возвращает распакованные значения.

Наиболее часто используемые методы:

pack_uint(value): Упаковывает беззнаковое целое число (unsigned int) в формате XDR.

```python
import xdrlib

packer = xdrlib.Packer()
packed_data = packer.pack_uint(42)
print(packed_data)
```

unpack_uint(packed_data): Распаковывает беззнаковое целое число (unsigned int) из данных в формате XDR и возвращает его значение.

```python
import xdrlib

packed_data = b"\x00\x00\x00\x2a"
unpacker = xdrlib.Unpacker(packed_data)
unpacked_value = unpacker.unpack_uint()
print(unpacked_value)
```

pack_string(value): Упаковывает строку в формате XDR.

```python
import xdrlib

packer = xdrlib.Packer()
packed_data = packer.pack_string("Hello, World!")
print(packed_data)
```

unpack_string(packed_data): Распаковывает строку из данных в формате XDR и возвращает ее значение.

```python
import xdrlib

packed_data = b"\x00\x00\x00\x0cHello, World!"
unpacker = xdrlib.Unpacker(packed_data)
unpacked_value = unpacker.unpack_string()
print(unpacked_value)
```

Пожалуйста, обратите внимание, что это только некоторые примеры методов библиотеки "xdrlib".
Для полного списка методов и их подробного описания рекомендуется обратиться к официальной документации Python.
""",
                    "string": r"""
Библиотека "string" в Python предоставляет набор методов для работы со строками.
Она обеспечивает функциональность для манипуляции и обработки текстовых данных.

Название метода           | Описание
   --------------------------|---------------------------------------------------------------
   `string.ascii_letters`     | Содержит все буквы алфавита в верхнем и нижнем регистрах.
   `string.ascii_lowercase`  | Содержит все буквы алфавита в нижнем регистре.
   `string.ascii_uppercase`  | Содержит все буквы алфавита в верхнем регистре.
   `string.digits`            | Содержит все цифры от 0 до 9.
   `string.hexdigits`         | Содержит все шестнадцатеричные цифры (от 0 до 9 и от A до F).
   `string.octdigits`         | Содержит все восьмеричные цифры (от 0 до 7).
   `string.punctuation`       | Содержит символы пунктуации.
   `string.printable`         | Содержит все печатные символы (буквы, цифры, символы пунктуации и пробельные символы).
   `string.whitespace`        | Содержит пробельные символы (пробел, табуляция, новая строка и т.д.).


`string.ascii_letters`: Возвращает все буквы алфавита в верхнем и нижнем регистрах.

```python
import string
print(string.ascii_letters)
```
`string.digits`: Возвращает все цифры от 0 до 9.

```python
import string
print(string.digits)
```
`string.punctuation`: Возвращает символы пунктуации.

```python
import string
print(string.punctuation)
```
""",
                    "rich": r'''
Библиотека `Rich` — это мощный инструмент для форматирования текста, вывода в терминал с использованием стилей,
цветов, таблиц, прогресс-баров и других элементов пользовательского интерфейса.
Она облегчает создание красивого и информативного вывода в консоли.
Библиотека также поддерживает рендеринг логов и трассировок ошибок.

# Основные возможности

1. **Цветной и стилизованный текст**
2. **Отображение таблиц**
3. **Прогресс-бары**
4. **Логи и трассировки ошибок**
5. **Отображение деревьев**
6. **Поддержка разметки Markdown**

# Установка

```bash
pip install rich
```

### Пример простого форматированного текста

```python
rich.print("[bold magenta]Hello, [italic]Rich[/italic]!")
```
> <span style="color:magenta"><span style="font-weight:700">Hello, <span style="font-style:italic">Rich</span>!</span></span>


## Основные функции и примеры

### Форматирование текста
В `Rich` используется синтаксис разметки для стилизации текста. Стили можно комбинировать.
```python
rich.print("[bold red]Ошибка:[/] неверный ввод!")
```
> <span style="font-weight:700;color:red">Ошибка:</span> неверный ввод!

Возможные стили: `bold`, `italic`, `underline`, `strikethrough`,
а также цветовые схемы (`red`, `green`, `blue` и другие).

## Таблицы
Вы можете создавать и выводить таблицы с помощью класса `Table`.
```python
from rich.table import Table
from rich.console import Console


console = Console()

table = Table(title="Таблица Пользователей")

table.add_column("Имя", justify="right", style="cyan", no_wrap=True)
table.add_column("Возраст", style="magenta")
table.add_column("Профессия", justify="right", style="green")

table.add_row("Иван", "32", "Инженер")
table.add_row("Анна", "28", "Дизайнер")
table.add_row("Петр", "40", "Менеджер")

console.print(table)
```
> &nbsp;&nbsp;&nbsp;&nbsp;<span style="font-style:italic">Таблица Пользователей</span>
> ┏━━━━━━┳━━━━━━━━━┳━━━━━━━━━━━┓
> ┃  Имя ┃ Возраст ┃ Профессия ┃
> ┡━━━━━━╇━━━━━━━━━╇━━━━━━━━━━━┩
> │ <span style="color:cyan">Иван</span> │ <span style="color:magenta">32</span>      │   <span style="color:green">Инженер</span> │
> │ <span style="color:cyan">Анна</span> │ <span style="color:magenta">28</span>      │  <span style="color:green">Дизайнер</span> │
> │ <span style="color:cyan">Петр</span> │ <span style="color:magenta">40</span>      │  <span style="color:green">Менеджер</span> │
> └──────┴─────────┴───────────┘


Этот код создаст таблицу с тремя столбцами, которая будет выведена в консоль с цветами и выравниванием.

### Прогресс-бары
```python
import time
from rich.progress import Progress


with Progress() as progress:
    task = progress.add_task("Обработка...", total=100)
    while not progress.finished:
        progress.update(task, advance=1)
        time.sleep(0.1)
```

Прогресс-бар будет обновляться в реальном времени, показывая прогресс задачи.

### Логи

`Rich` интегрируется с модулем `logging`, позволяя выводить цветные и более информативные логи.

```python
import logging
from rich.logging import RichHandler


logging.basicConfig(level="NOTSET", handlers=[RichHandler()])
log = logging.getLogger("rich")

log.info("Это информационное сообщение")
log.error("Это ошибка")
```

### Трассировки ошибок

`Rich` может красиво отображать трассировки ошибок, улучшая их читаемость.

```python
from rich.console import Console


console = Console()

try:
    1 / 0
except ZeroDivisionError:
    console.print_exception()
```

### Деревья

С помощью `Tree` можно отображать данные в виде иерархических деревьев.

```python
from rich.tree import Tree
from rich.console import Console


console = Console()

tree = Tree("Файловая система")
tree.add("Папка 1")
tree.add("Папка 2").add("Файл 1")

console.print(tree)
"""
Файловая система
├── Папка 1
└── Папка 2
    └── Файл 1
"""                    
```

### Markdown

`Rich` поддерживает рендеринг разметки Markdown.

```python
from rich.console import Console
from rich.markdown import Markdown


console = Console()
md = Markdown(
    """
# Заголовок

* Пункт 1
* Пункт 2
"""
)
console.print(md)
"""
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃                Заголовок                 ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛

 • Пункт 1
 • Пункт 2
"""
```

# Дополнительные возможности

- **Списки**: Создание стилизованных списков.
- **JSON**: Вывод `JSON` данных в цвете.
- **Ограничение по ширине**: Вывод данных с ограничением по ширине консоли.

''',
                },
                "Python": {
                    "markdown": {
                        "extensions": """
| Extension                      | Entry Point    | Dot Notation                       |
|--------------------------------|----------------|------------------------------------|
| Extra                          | `extra`        | `markdown.extensions.extra`        |
| &nbsp;&nbsp;Abbreviations      | `abbr`         | `markdown.extensions.abbr`         |
| &nbsp;&nbsp;Attribute Lists    | `attr_list`    | `markdown.extensions.attr_list`    |
| &nbsp;&nbsp;Definition Lists   | `def_list`     | `markdown.extensions.def_list`     |
| &nbsp;&nbsp;Fenced Code Blocks | `fenced_code`  | `markdown.extensions.fenced_code`  |
| &nbsp;&nbsp;Footnotes          | `footnotes`    | `markdown.extensions.footnotes`    |
| &nbsp;&nbsp;Markdown in HTML   | `md_in_html`   | `markdown.extensions.md_in_html`   |
| &nbsp;&nbsp;Tables             | `tables`       | `markdown.extensions.tables`       |
| Admonition                     | `admonition`   | `markdown.extensions.admonition`   |
| CodeHilite                     | `codehilite`   | `markdown.extensions.codehilite`   |
| Legacy Attributes              | `legacy_attrs` | `markdown.extensions.legacy_attrs` |
| Legacy Emphasis                | `legacy_em`    | `markdown.extensions.legacy_em`    |
| Meta-Data                      | `meta`         | `markdown.extensions.meta`         |
| New Line to Break              | `nl2br`        | `markdown.extensions.nl2br`        |
| Sane Lists                     | `sane_lists`   | `markdown.extensions.sane_lists`   |
| SmartyPants                    | `smarty`       | `markdown.extensions.smarty`       |
| Table of Contents              | `toc`          | `markdown.extensions.toc`          |
| WikiLinks                      | `wikilinks`    | `markdown.extensions.wikilinks`    |

[https://python-markdown.github.io/extensions/](https://python-markdown.github.io/extensions/)
""",
                    },
                    "typing": """
```python
from typing import Any  # Любой тип
```

```python
from typing import Literal  # Один из вариантов
direction: Literal["ASC", "DESC"] = "DESC"
```

```python
from typing import Union
val: Union[int, float] = 20.8  # or 20
```

```python
from typing import Final

val: Final = 2
val += 1  # Ошибки не произойдёт, но IDE подсветит как ошибку.
```

# Использование статической проверки типов в Python
Интерпретатор Python по умолчанию не осуществляет проверку типов.
Однако была создана версия интерпретатора Python – `mypy`,
которая обеспечивает проверку типов на уровне интерпретатора.

```python
from typing import NoReturn
# NoReturn сообщает что функция не завершается нормально.
# Например она возбуждает исключение.

def forever() -> NoReturn:
    while True:
        pass
```

Если это генераторная функция, то есть её тело содержит оператор `yield`, 
для возвращаемого можно воспользоваться аннотацией `Iterable[T]`, либо `Generator[YT, ST, RT]`:

```python
def generate_two() -> Iterable[int]:
    yield 1
    yield "2"  # Incompatible types in "yield" (actual type "str", expected type "int")
```

```python
from typing import Optional

amount: int
amount = None  # Incompatible types in assignment (expression has type "None", variable has type "int")

price: Optional[int]
price = None

# Аннотация Optional[T] эквивалентна Union[T, None], хотя такая запись и не рекомендуется.
```

# Предварительное объявление

Обычно вы не можете использовать тип до того, как он создан. Например, следующий код даже не запустится:

```python
class LinkedList:
    data: Any
    next: LinkedList  # NameError: name 'LinkedList' is not defined
```

Чтобы это исправить, допустимо использовать строковый литарал. В этом случае аннотации будут вычислены отложенно.

```python
class LinkedList:
    data: Any
    next: 'LinkedList'
```

Так же вы можете обращаться к классам из других модулей (конечно, если модуль импортирован):

```python
some_variable: 'somemodule.SomeClass'
```

или

```python
from __future__ import annotations

class LinkedList:
    data: int
    next: LinkedList
```

# Generic-типы

Иногда необходимо сохранить информацию о типе, при этом не фиксируя его жестко.
Например, если вы пишете контейнер, который хранит однотипные данные.
Или функцию, которая возвращает данные того же типа, что и один из аргументов.

Такие типы как `List` или `Callable`, которые, мы видели раньше как раз используют механизм дженериков.
Но кроме стандартных типов, вы можете создать свои дженерик-типы.
Для этого надо, во-первых, завести `TypeVar` переменную,
которая будет атрибутом дженерика, и, во-вторых,непосредственно объявить generic-тип:

```python
T = TypeVar("T")

class LinkedList(Generic[T]):
    data: T
    next: "LinkedList[T]"

    def __init__(self, data: T):
        self.data = data

head_int: LinkedList[int] = LinkedList(1)
head_int.next = LinkedList(2)
head_int.next = 2  # error: Incompatible types in assignment (expression has type "int", variable has type "LinkedList[int]")
head_int.data += 1
head_int.data.replace("0", "1")  # error: "int" has no attribute "replace"

head_str: LinkedList[str] = LinkedList("1")
head_str.data.replace("0", "1")

head_str = LinkedList[str](1)  # error: Argument 1 to "LinkedList" has incompatible type "int"; expected "str"
```

Как вы можете заметить, для generic-типов работает автоматический вывод типа параметра.
Если требуется, дженерик может иметь любое количеством параметров: `Generic[T1, T2, T3]`.
Также, при определении `TypeVar` вы можете ограничить допустимые типы:

```python
T2 = TypeVar("T2", int, float)

class SomethingNumeric(Generic[T2]):
    pass

x = SomethingNumeric[str]()  # error: Value of type variable "T2" of "SomethingNumeric" cannot be "str"
```

# Cast

Иногда анализатор статический анализатор не может корректно определить тип переменной,
в этом случае можно использовать функцию `cast`.
Её единственная задача — показать анализатору, что выражение имеет определённый тип.

```python
from typing import List, cast

def find_first_str(a: List[object]) -> str:
    index = next(i for i, x in enumerate(a) if isinstance(x, str))
    return cast(str, a[index])
```

Также это может быть полезно для декораторов:

```python
MyCallable = TypeVar("MyCallable", bound=Callable)

def logged(func: MyCallable) -> MyCallable:
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(func.__name__, args, kwargs)
        return func(*args, **kwargs)

    return cast(MyCallable, wrapper)

@logged
def mysum(a: int, b: int) -> int:
    return a + b

mysum(a=1)  # error: Missing positional argument "b" in call to "mysum"
```
""",
                    "itertools": """
# Основные функции и атрибуты

| Функция/Атрибут                   | Описание                                                                                                                                          |
|-----------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|
| `accumulate()`                    | Возвращает итератор, который вычисляет частичные суммы<br>(или другие накопленные функции, если указана) от переданного итератора                 |
| `chain()`                         | Принимает несколько итераторов и возвращает один итератор,<br>объединяющий все их элементы последовательно                                        |
| `combinations()`                  | Возвращает все возможные комбинации заданной длины из элементов итератора (без повторений)                                                        |
| `combinations_with_replacement()` | Возвращает все возможные комбинации с повторениями заданной длины из элементов итератора                                                          |
| `compress()`                      | Возвращает элементы из первого итератора,<br>где соответствующий элемент из второго итератора (маски) истинный                                    |
| `count()`                         | Возвращает итератор, который генерирует последовательность чисел,<br>начиная с `start` (по умолчанию 0) с шагом `step` (по умолчанию 1)           |
| `cycle()`                         | Бесконечно повторяет элементы переданного итератора                                                                                               |
| `dropwhile()`                     | Возвращает элементы из итератора, начиная с первого элемента,<br>для которого условие становится ложным                                           |
| `filterfalse()`                   | Возвращает элементы итератора, для которых условие ложно (противоположно `filter`)                                                                |
| `groupby()`                       | Группирует элементы последовательности по ключу (или значению функции).<br>Возвращает итератор с парами `(ключ, группа)`                          |
| `islice()`                        | Возвращает срез итератора (аналогично `slice()` для списков)                                                                                      |
| `pairwise()`                      | Выдаёт пары соседних элементов из `iterable`                                                                                                      |
| `permutations()`                  | Возвращает все возможные перестановки заданной длины (или длины итератора)                                                                        |
| `product()`                       | Возвращает декартово произведение входных итераторов (все возможные комбинации)                                                                   |
| `repeat()`                        | Повторяет переданный элемент `object` бесконечно или заданное количество раз `times`                                                              |
| `starmap()`                       | Применяет функцию к каждому элементу итератора, передавая элементы<br>как аргументы по позициям (аналогично `map()`, но с распаковкой аргументов) |
| `takewhile()`                     | Возвращает элементы из итератора до тех пор, пока условие истинно                                                                                 |
| `tee()`                           | Разделяет итератор на заданное количество независимых копий                                                                                       |
| `zip_longest()`                   | Объединяет элементы из нескольких итераторов, заполняя отсутствующие значения `fillvalue`                                                         |


# accumulate
Возвращает итератор, который вычисляет частичные суммы (или другие накопленные функции).
```python
from itertools import accumulate

print(list(accumulate([1, 2, 3, 4])))
# [1, 3, 6, 10]
```

# chain
Объединяет несколько итераторов в один.
```python
from itertools import chain

print(list(chain("ABC", "DEF")))
# ["A", "B", "C", "D", "E", "F"]
```

# combinations
Возвращает все возможные комбинации заданной длины без повторений.
```python
from itertools import combinations

print(list(combinations("ABC", 2)))
# [("A", "B"), ("A", "C"), ("B", "C")]
```

# combinations_with_replacement
Возвращает все возможные комбинации заданной длины с повторениями.
```python
from itertools import combinations_with_replacement

print(list(combinations_with_replacement("AB", 2)))
# [("A", "A"), ("A", "B"), ("B", "B")]
```

# compress
Возвращает элементы из первого итератора, где соответствующий элемент из второго итератора истинный.
```python
from itertools import compress

print(list(compress("ABCDEF", [1, 0, 1, 0, 1, 0])))
# ["A", "C", "E"]
```

# count
Создает бесконечный итератор, который начинает с заданного числа и увеличивается на заданный шаг.
```python
from itertools import count

for i in count(10, 2):
    if i > 20:
        break
    print(i)
# 10, 12, 14, 16, 18, 20
```

# cycle
Бесконечно повторяет элементы из итератора.
```python
from itertools import cycle

counter = 0
for item in cycle("AB"):
    if counter >= 6:
        break
    print(item)  # A, B, A, B, A, B
    counter += 1
```

# dropwhile
Пропускает элементы, пока условие истинно, затем возвращает оставшиеся элементы.
```python
from itertools import dropwhile

print(list(dropwhile(lambda x: x < 5, [1, 4, 6, 7])))
# [6, 7]
```

# filterfalse
Возвращает элементы итератора, для которых условие ложно.
```python
from itertools import filterfalse

print(list(filterfalse(lambda x: x % 2, range(10))))
# [0, 2, 4, 6, 8]
```

# groupby
Группирует элементы по ключу. Возвращает итератор с парами `(ключ, группа)`.
```python
from itertools import groupby

for key, group in groupby("AAAABBBCCDA"):
    print(key, list(group))
# A ["A", "A", "A", "A"]
# B ["B", "B", "B"]
# C ["C", "C"]
# D ["D"]
# A ["A"]
```

# islice
Возвращает срез итератора.
```python
from itertools import islice

print(list(islice(range(10), 2, 8, 2)))  # [2, 4, 6]
```

# pairwise
```python
from itertools import pairwise

print(list(pairwise("ABcd12")))
# [("A", "B"), ("B", "c"), ("c", "d"), ("d", "1"), ("1", "2")]
```

# permutations
Возвращает все возможные перестановки заданной длины.
```python
from itertools import permutations

print(list(permutations("ABC", 2)))
# [("A", "B"), ("A", "C"), ("B", "A"), ("B", "C"), ("C", "A"), ("C", "B")]
```

# product
Возвращает декартово произведение входных итераторов.
```python
from itertools import product

print(list(product("AB", "12")))
# [("A", "1"), ("A", "2"), ("B", "1"), ("B", "2")]
```

# repeat
Повторяет указанный элемент бесконечно или заданное количество раз.
```python
from itertools import repeat

for i in repeat(10, 3):
    print(i)
# 10, 10, 10
```

# starmap
Применяет функцию к каждому элементу итератора, распаковывая элементы как аргументы.
```python
from itertools import starmap

print(list(starmap(pow, [(2, 5), (3, 2), (10, 3)])))  # [32, 9, 1000]
```

# takewhile
Возвращает элементы из итератора до тех пор, пока условие истинно.
```python
from itertools import takewhile

print(list(takewhile(lambda x: x < 5, [1, 4, 6, 7])))  # [1, 4]
```

# tee
Создает несколько независимых копий одного итератора.
```python
from itertools import tee

it1, it2 = tee(range(5), 2)
print(list(it1))  # [0, 1, 2, 3, 4]
print(list(it2))  # [0, 1, 2, 3, 4]
```

# zip_longest
Объединяет элементы из нескольких итераторов, заполняя отсутствующие значения `fillvalue`.
```python
from itertools import zip_longest

print(list(zip_longest("AB", "12", fillvalue="-")))
# [("A", "1"), ("B", "2")]
```
""",
                    "collections": """
Библиотека `collections` предоставляет специализированные контейнерные типы данных,
которые расширяют стандартные структуры, такие как списки, кортежи и словари.
Эти структуры данных помогают сделать код более читабельным и эффективным.

| Контейнер                          | Описание                                                                                                                                |
|------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| `Counter`                          | Счетчик, который предназначен для подсчета хэшируемых объектов.<br>Возвращает словарь, где ключи — объекты, а значения — их количество. |
| `defaultdict`                      | Словарь, который автоматически создает значение по умолчанию<br>для несуществующих ключей при первом обращении к ним.                   |
| `OrderedDict`                      | Словарь, который сохраняет порядок добавления элементов.                                                                                |
| `namedtuple()`                     | Создает подклассы кортежей с именованными полями,<br>что позволяет обращаться к элементам по имени.                                     |
| `deque`                            | Двусторонняя очередь, которая поддерживает добавление<br>и удаление элементов с обоих концов с высокой производительностью.             |
| `ChainMap`                         | Объединяет несколько словарей или других отображений в одно,<br>обеспечивая единый вид для поиска и изменения данных.                   |
| `UserDict` `UserList` `UserString` | Классы для создания пользовательских словарей,<br>списков и строк с возможностью переопределения их поведения.                          |

# Counter

Подкласс словаря, который предназначен для подсчета хэша объектов (например, слов, символов и т.д.).
Он подсчитывает количество вхождений каждого элемента.

| Функция/Метод                               | Описание                                                                                                | Пример                             |
|---------------------------------------------|---------------------------------------------------------------------------------------------------------|------------------------------------|
| `Counter()`                                 | Создает объект `Counter`.                                                                               | `counter = Counter("abracadabra")` |
| `Counter().elements()`                      | Возвращает итератор по элементам, каждый из которых<br>повторяется столько раз, сколько он встречается. | `list(counter.elements())`         |
| `Counter().most_common([n])`                | Возвращает n самых распространенных элементов и их количество.                                          | `counter.most_common(2)`           |
| `Counter().subtract([iterable-or-mapping])` | Вычитает элементы, как и `update`, но уменьшает количество.                                             | `counter.subtract("abcd")`         |
| `Counter().update([iterable-or-mapping])`   | Увеличивает счетчик для элементов из `iterable` или другого `Counter`.                                  | `counter.update("abc")`            |


```python
from collections import Counter

counter = Counter("abracadabra")
print(counter)  # Counter({"a": 5, "b": 2, "r": 2, "c": 1, "d": 1})

# Выводим наиболее часто встречающиеся символы
print(counter.most_common(2))  # [("a", 5), ("b", 2)]
print(list(counter.elements()))  # ["a", "a", "a", "a", "a", "b", "b", "r", "r", "c", "d"]
```

# defaultdict

Подкласс словаря, который вызывает функцию для отсутствующих ключей и использует её результат в качестве значения по умолчанию.

| Функция/Метод                  | Описание                                  | Пример                 |
|--------------------------------|-------------------------------------------|------------------------|
| `defaultdict(default_factory)` | Создает словарь с значением по умолчанию. | `d = defaultdict(int)` |

```python
from collections import defaultdict

d = defaultdict(int)
d["a"] += 1
print(d)  # defaultdict(<class "int">, {"a": 1})
```

# OrderedDict

Подкласс словаря, который запоминает порядок добавления элементов.

| Функция/Метод                | Описание                                                 | Пример                |
|------------------------------|----------------------------------------------------------|-----------------------|
| `OrderedDict()`              | Создает упорядоченный словарь.                           | `od = OrderedDict()`  |
| `move_to_end(key, last=True)`| Перемещает элемент с заданным ключом в конец или начало. | `od.move_to_end("a")` |
| `popitem(last=True)`         | Удаляет и возвращает элемент с конца или начала.         | `od.popitem()`        |

```python
from collections import OrderedDict

od = OrderedDict()
od["a"] = 1
od["b"] = 2
od["c"] = 3
print(od)  # OrderedDict([("a", 1), ("b", 2), ("c", 3)])
```

# namedtuple

[Фабрика классов](?General/Паттерны%20проектирования/Порождающие%20паттерны/Factory%20(Фабрика).md), которая создает подклассы кортежа с именованными полями.

| Функция/Метод                       | Описание                                            | Пример                               |
|-------------------------------------|-----------------------------------------------------|--------------------------------------|
| `namedtuple(typename, field_names)` | Создает новый тип кортежа с именами полей.          | `Point = namedtuple("Point", "x y")` |
| `_replace(**kwargs)`                | Возвращает новый экземпляр, заменив указанные поля. | `p._replace(x=10)`                   |

```python
from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])
p = Point(10, 20)
print(p)    # Point(x=10, y=20)
print(p.x)  # 10
print(p.y)  # 20
```

# deque

Двусторонняя очередь, которая обеспечивает быстрый доступ и добавление элементов с обоих концов.

| Функция/Метод   | Описание                               | Пример             |
|-----------------|----------------------------------------|--------------------|
| `append(x)`     | Добавляет элемент в конец.             | `dq.append(1)`     |
| `appendleft(x)` | Добавляет элемент в начало.            | `dq.appendleft(1)` |
| `pop()`         | Удаляет и возвращает элемент с конца.  | `dq.pop()`         |
| `popleft()`     | Удаляет и возвращает элемент с начала. | `dq.popleft()`     |
| `rotate(n)`     | Вращает очередь на `n` шагов.          | `dq.rotate(1)`     |

```python
from collections import deque

dq = deque([1, 2, 3])
dq.append(4)
dq.appendleft(0)
print(dq)  # deque([0, 1, 2, 3, 4])
dq.pop()
dq.popleft()
print(dq)  # deque([1, 2, 3])
```

# ChainMap

Объединяет несколько словарей или других отображений в одно логическое целое. 

| Функция/Метод       | Описание                                                    | Пример                        |
|---------------------|-------------------------------------------------------------|-------------------------------|
| `ChainMap(*maps)`   | Создает новый `ChainMap` из указанных отображений.          | `cm = ChainMap(dict1, dict2)` |
| `new_child(m=None)` | Возвращает новый `ChainMap` с m как новой первичной картой. | `cm.new_child({"c": 3})`      |

```python
from collections import ChainMap

d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}

d = ChainMap(d1, d2)
print(d)  # ChainMap({"a": 1, "b": 2}, {"b": 3, "c": 4})

print(d["a"])  # 1
print(d["b"])  # 2 (из d1, так как b в d1 появился раньше, чем в d2)
print(d["c"])  # 4 (из d2)

d3 = {"c": 5, "d": 6}
d = d.new_child(d3)

print(d["c"])  # 5 (из d3, так как он добавлен в цепочку позже, чем d2)
print(d["d"])  # 6 (из d3)
```

# UserDict, UserList, UserString

Эти классы предоставляют возможность создания пользовательских классов,
наследуемых от словаря, списка и строки соответственно, с возможностью переопределения их поведения.

| Класс        | Описание                                              | Пример                             |
|--------------|-------------------------------------------------------|------------------------------------|
| `UserDict`   | Базовый класс для создания пользовательских словарей. | `class MyDict(UserDict): pass`     |
| `UserList`   | Базовый класс для создания пользовательских списков.  | `class MyList(UserList): pass`     |
| `UserString` | Базовый класс для создания пользовательских строк.    | `class MyString(UserString): pass` |

```python
from collections import UserDict, UserList, UserString

d = UserDict({"a": 1, "b": 2})
d["c"] = 3
print(d)  # {"a": 1, "b": 2, "c": 3}

l = UserList([1, 2, 3])
l.append(4)
print(l)  # [1, 2, 3, 4]

s = UserString("hello, world")
print(s.upper())  # HELLO, WORLD


class MyDict(UserDict):
    def __setitem__(self, key, value):
        print(f"Setting {key} to {value}")
        super().__setitem__(key, value)


md = MyDict()
md["a"] = 1  # Setting a to 1
```

# Полезные ссылки
- [Официальная документация](https://docs.python.org/3/library/collections.html)
- [Real Python - Advanced Python Collections](https://realpython.com/python-collections-module/)

""",
                    "functools": '''
`functools` - Утилиты для работы с функциями, упрощая их применение, создание и комбинирование

| Функция/Атрибут          | Описание                                                                                                                                                                        | Пример использования                                             |
|--------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------|
| `partial()`              | Создает новую функцию с частично фиксированными аргументами,<br>позволяя упростить вызов функции с заранее определенными аргументами                                            | `double = partial(multiply, y=2)`                                |
| `reduce()`               | Последовательно применяет функцию, принимающую два аргумента,<br>к элементам последовательности, сводя их к одному результату                                                   | `result = reduce(lambda x, y: x + y, numbers)`                   |
| `lru_cache()`            | Декоратор для кэширования результатов функции,<br>что помогает избежать повторных вычислений при одинаковых входных данных                                                      | `@lru_cache(maxsize=None)`                                       |
| `wraps()`                | Декоратор, сохраняющий метаданные оригинальной функции<br>(например, `__name__`, `__doc__`) при использовании декораторов                                                       | `@wraps(func)`                                                   |
| `total_ordering()`       | Класс-декоратор, который автоматически добавляет все методы сравнения<br>(`<`, `<=`, `>`, `>=`), если определены `__eq__`<br>и один из (`__lt__`, `__le__`, `__gt__`, `__ge__`) | `@total_ordering`                                                |
| `cmp_to_key()`           | Преобразует функцию сравнения старого стиля в функцию,<br>возвращающую ключ для сортировки<br>(например, для использования в `sorted()` или `min()`)                            | `sorted_data = sorted(data, key=cmp_to_key(compare))`            |
| `cache()`                | Декоратор для кэширования результатов функции,<br>аналогичный `lru_cache`, но без ограничений на размер кэша                                                                    | `@cache`                                                         |
| `update_wrapper()`       | Обновляет метаданные функции-декоратора,<br>чтобы они соответствовали оригинальной функции                                                                                      | `update_wrapper(wrapper, wrapped)`                               |
| `partialmethod()`        | Позволяет создавать методы с частично<br>фиксированными аргументами для использования в классах                                                                                 | `partialmethod(func, arg1, arg2)`                                |
| `singledispatch()`       | Декоратор, который преобразует функцию<br>в обобщенную функцию с поддержкой однотипного диспетчеризации,<br>позволяя создавать перегрузки для разных типов аргументов           | `@singledispatch`                                                |
| `singledispatchmethod()` | Версия `singledispatch`, предназначенная<br>для использования в классах как метод, а не как функция                                                                             | `@singledispatchmethod`                                          |
| `cached_property()`      | Декоратор, который превращает метод класса в свойство,<br>кэшируемое после первого вычисления                                                                                   | `@cached_property`                                               |
| `WRAPPER_ASSIGNMENTS`    | Список атрибутов, которые копируются<br>из оригинальной функции в функцию-декоратор                                                                                             | По умолчанию: `__module__` `__name__`<br>`__qualname__` `__doc__` `__annotations__` |
| `WRAPPER_UPDATES`        | Список атрибутов, которые обновляются<br>из оригинальной функции в функцию-декоратор                                                                                            | По умолчанию: `__dict__`                                     |


# partial
Создает новую функцию с частично фиксированными аргументами
Удобно для переиспользования функций с предустановленными параметрами
```python
from functools import partial

def multiply(x, y):
    return x * y

# `y` всегда равен 2
print(partial(multiply, y=2)(5))  # 10
```

# reduce
Последовательно применяет функцию, принимающую два аргумента,
к элементам последовательности, сводя их к одному результату
```python
from functools import reduce

numbers = [1, 2, 3, 4, 5]
print(reduce(lambda x, y: x + y, numbers))  # 15
```

# lru_cache
Кэширует результаты функции, улучшая производительность за счет предотвращения повторных вычислений
С ограничением на количество сохраненных значений
Это полезно для оптимизации рекурсивных функций
```python
from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

@lru_cache(maxsize=128)
def factorial(n):
    return n * factorial(n-1) if n else 1

print(fibonacci(10))  # 55
print(factorial(5))  # 120
```

# wraps
Используется для создания декораторов, которые сохраняют метаданные декорируемой функции
```python
from functools import wraps

def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Вызов функции {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def greet(name):
    """Приветствие пользователя"""
    return f"Hello, {name}!"

print(greet("Alice"))  # "Hello, Alice!"
print(greet.__name__)  # "greet"
print(greet.__doc__)   # "Приветствие пользователя"
```

# total_ordering
Класс-декоратор, который добавляет методы сравнения (`<`, `<=`, `>`, `>=`) к классу,
если определены `__eq__` и один из (`__lt__`, `__le__`, `__gt__`, `__ge__`)
```python
from functools import total_ordering

@total_ordering
class Number:
    def __init__(self, value):
        self.value = value
    
    def __eq__(self, other):
        return self.value == other.value
    
    def __lt__(self, other):
        return self.value < other.value

n1 = Number(1)
n2 = Number(2)

print(n1 < n2)  # True
print(n1 > n2)  # False
```

# cmp_to_key
Преобразует функцию сравнения старого стиля в функцию, возвращающую ключ для сортировки
```python
from functools import cmp_to_key

def compare(x, y):
    return x - y

sorted_list = sorted([5, 3, 6, 2, 1], key=cmp_to_key(compare))
print(sorted_list)  # [1, 2, 3, 5, 6]
```

# cache
Декоратор, который кэширует результаты вызовов функции `func`
с одинаковыми аргументами, чтобы избежать повторных вычислений
```python
from functools import cache

@cache
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

@cache
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(factorial(5))  # 120
print(fibonacci(10))  # 55
```

# update_wrapper
Обновляет метаданные функции-декоратора, чтобы они соответствовали оригинальной функции

```python
from functools import update_wrapper

def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("До вызова функции")
        return func(*args, **kwargs)
    return update_wrapper(wrapper, func)

@my_decorator
def my_function():
    print("Выполнение функции")

my_function()  # До вызова функции Выполнение функции
```

# partialmethod
Аналог `partial`, но используется для создания методов с частично фиксированными аргументами

```python
from functools import partialmethod

class MyClass:
    def multiply(self, x, y):
        return x * y
    
    double = partialmethod(multiply, y=2)

obj = MyClass()
print(obj.double(5))  # 10
```

# singledispatch
Позволяет создавать обобщенные функции с поддержкой
однотипного диспетчеризации (перегрузки) на основе типа первого аргумента

```python
from functools import singledispatch

@singledispatch
def process(value):
    print(f"Обработка объекта: {value}")

@process.register(int)
def _(value):
    print(f"Обработка целого числа: {value}")

@process.register(str)
def _(value):
    print(f"Обработка строки: {value}")

process(10)   # Обработка целого числа: 10
process("hi") # Обработка строки: hi
```

# singledispatchmethod
То же самое, что `singledispatch`, но используется как метод класса

```python
from functools import singledispatchmethod

class Processor:
    @singledispatchmethod
    def process(self, value):
        print(f"Обработка объекта: {value}")

    @process.register(int)
    def _(self, value):
        print(f"Обработка целого числа: {value}")

    @process.register(str)
    def _(self, value):
        print(f"Обработка строки: {value}")

processor = Processor()
processor.process(10)   # Обработка целого числа: 10
processor.process("hi") # Обработка строки: hi
```

# cached_property
Позволяет кэшировать результат вычислений метода и использовать его как свойство.
Значение вычисляется только один раз

```python
from functools import cached_property

class MyClass:
    @cached_property
    def heavy_computation(self):
        print("Выполняется вычисление...")
        return 42

obj = MyClass()
print(obj.heavy_computation)  # Выполняется вычисление ... 42
print(obj.heavy_computation)  # 42 (вычисление не выполняется повторно)
```

# WRAPPER_ASSIGNMENTS
Это кортеж, определяющий, какие атрибуты копируются из оригинальной функции в декорированную
По умолчанию копируются атрибуты: `__module__`, `__name__`, `__qualname__`, `__doc__`, `__annotations__`

# WRAPPER_UPDATES
Это кортеж, определяющий, какие атрибуты обновляются в декорированной функции
По умолчанию обновляется `__dict__`


# Частые применения
1. Оптимизация работы с функциями — использование `partial()` и `lru_cache()` для ускорения работы с часто вызываемыми функциями
2. Создание декораторов — с сохранением метаданных функции с помощью `wraps()`
3. Упрощение сравнения — автоматическое добавление методов сравнения с `total_ordering()`

# Полезные ссылки
- [Официальная документация](https://docs.python.org/3/library/functools.html)
- [Real Python - Guide to Python’s functools Module](https://realpython.com/python-functools/)

''',
                    "cachetools": """
| Класс/Функция             | Описание                                                                                         |
|---------------------------|--------------------------------------------------------------------------------------------------|
| `Cache`                   | Базовый класс для всех кэшей. Не используется напрямую, а служит основой для других типов кэшей. |
| `FIFOCache(maxsize)`      | Кэш с алгоритмом замещения **FIFO** (First In, First Out).                                       |
| `LFUCache(maxsize)`       | Кэш с алгоритмом замещения **LFU** (Least Frequently Used).                                      |
| `LRUCache(maxsize)`       | Кэш с алгоритмом замещения **LRU** (Least Recently Used).                                        |
| `MRUCache(maxsize)`       | Кэш с алгоритмом замещения **MRU** (Most Recently Used).                                         |
| `RRCache(maxsize)`        | Кэш с случайным замещением (Random Replacement).                                                 |
| `TLRUCache(maxsize, ttl)` | Кэш с временным ограничением и алгоритмом замещения **LRU** (Time-aware Least Recently Used).    |
| `TTLCache(maxsize, ttl)`  | Кэш с временным ограничением (**Time-to-Live**) и алгоритмом замещения **LRU**.                  |
| `cached(cache)`           | Декоратор для кэширования возвращаемого значения функции.                                        |
| `cachedmethod(cache)`     | Декоратор для кэширования возвращаемого значения метода класса.                                  |

# Cache
Базовый класс для всех кэшей.
Он не используется напрямую, но служит основой для других классов,
предоставляя основные методы для работы с кэшем.

# FIFOCache
Использует алгоритм **FIFO** (First In, First Out).
Когда кэш заполняется, самый старый элемент удаляется, чтобы освободить место для нового.
```python
from cachetools import FIFOCache

cache = FIFOCache(maxsize=3)
cache["a"] = 1
cache["b"] = 2
cache["c"] = 3

print(cache)  # FIFOCache([("a", 1), ("b", 2), ("c", 3)])

cache["d"] = 4
print(cache)  # FIFOCache([("b", 2), ("c", 3), ("d", 4)])
```

# LFUCache
Использует алгоритм **LFU** (Least Frequently Used).
Наименее часто используемые элементы удаляются первыми при необходимости освобождения места.
```python
from cachetools import LFUCache

cache = LFUCache(maxsize=2)
cache["a"] = 1
cache["b"] = 2

cache["a"]  # Доступ к элементу увеличивает счетчик использования
cache["c"] = 3  # Удаляет "b", так как он использовался реже

print(cache)  # LFUCache([("a", 1), ("c", 3)])
```

# LRUCache
Использует алгоритм **LRU** (Least Recently Used).
Наименее недавно используемые элементы удаляются первыми.
```python
from cachetools import LRUCache

cache = LRUCache(maxsize=2)
cache["a"] = 1
cache["b"] = 2

cache["a"]  # Доступ к элементу делает его "самым недавно использованным"
cache["c"] = 3  # Удаляет "b", так как он был использован давнее всего

print(cache)  # LRUCache([("a", 1), ("c", 3)])
```

# MRUCache
Использует алгоритм **MRU** (Most Recently Used).
Самый недавно использованный элемент удаляется первым при необходимости освобождения места.
```python
from cachetools import MRUCache

cache = MRUCache(maxsize=2)
cache["a"] = 1
cache["b"] = 2

cache["a"]  # Доступ к элементу делает его "самым недавно использованным"
cache["c"] = 3  # Удаляет "a", так как он был использован последним

print(cache)  # MRUCache([("b", 2), ("c", 3)])
```

# RRCache
Использует случайное замещение (Random Replacement).
Элементы удаляются случайным образом, когда кэш заполняется.
```python
from cachetools import RRCache

cache = RRCache(maxsize=2)
cache["a"] = 1
cache["b"] = 2
cache["c"] = 3

print(cache)  # Один из элементов ("a" или "b") будет удален случайным образом
```

# TLRUCache
Сочетает в себе временное ограничение (`ttl`) и алгоритм **LRU**.
Элементы удаляются либо при истечении времени жизни, либо по принципу **LRU**.
```python
from cachetools import TLRUCache
import time

cache = TLRUCache(maxsize=2, ttl=5)
cache["a"] = 1
time.sleep(6)  # Ждем 6 секунд
cache["b"] = 2

print(cache)  # "a" будет удален, так как его TTL истек
```

# TTLCache
Кэш с временным ограничением (Time-to-Live) и алгоритмом **LRU**.
Элементы удаляются либо по истечению времени жизни (`ttl`), либо по принципу **LRU**, если кэш переполнен.
```python
from cachetools import TTLCache
import time

cache = TTLCache(maxsize=2, ttl=5)
cache["a"] = 1
time.sleep(6)  # Ждем 6 секунд
cache["b"] = 2

print(cache)  # "a" будет удален, так как его TTL истек
```

# cached
Декоратор, который используется для кэширования возвращаемого значения функции.
Он может использовать любой из предоставленных кэшей.
```python
from cachetools import cached, LRUCache

cache = LRUCache(maxsize=2)

@cached(cache)
def get_value(x):
    return x * 2

print(get_value(2))  # Вычисляет и кэширует результат
print(get_value(2))  # Возвращает кэшированный результат
```

# cachedmethod
Декоратор для кэширования возвращаемого значения метода класса.
Декоратор позволяет задать кэш на уровне экземпляра класса.
```python
from cachetools import cachedmethod, LRUCache

class MyClass:
    def __init__(self):
        self._cache = LRUCache(maxsize=2)

    @cachedmethod(cache=lambda self: self._cache)
    def get_value(self, x):
        return x * 2

obj = MyClass()
print(obj.get_value(2))  # Вычисляет и кэширует результат
print(obj.get_value(2))  # Возвращает кэшированный результат
```
""",
                    "contextlib": """
Модуль contextlib - это стандартная библиотека Python, который содержит утилиты для работы с контекстными менеджерами.
Контекстные менеджеры могут использоваться, например, для управления ресурсами, такими как файлы или сетевые соединения.



#### contextlib.contextmanager
Декоратор превращает генераторную функцию в контекстный менеджер. 
Генератор должен содержать точку входа и выхода из контекста.

```python
import contextlib

@contextlib.contextmanager
def my_context():
    print("Entering context")
    yield
    print("Exiting context")

with my_context():
    print("Inside context")
```

В этом примере my_context() - это контекстный менеджер, который выводит сообщения при входе и выходе из контекста.



#### contextlib.suppress
это контекстный менеджер, который подавляет указанные исключения. 
Он используется, когда вы хотите, чтобы программа продолжала работать даже при возникновении определенных ошибок. 
Пример использования:

```python
import contextlib

with contextlib.suppress(FileNotFoundError):
    with open("non_existent_file.txt", "r") as f:
        print(f.read())
```

В этом примере suppress используется для подавления исключения FileNotFoundError, 
которое возникает, если файл non_existent_file.txt не найден. 
Вместо того, чтобы возбудить исключение, программа продолжит работу без выполнения блока кода внутри with выражения.


#### contextlib.redirect_stdout и contextlib.redirect_stderr
эти контекстные менеджеры перенаправляют стандартный вывод и стандартный вывод ошибок соответственно в файл или объект. 
Пример использования:

```python
import contextlib
import io

with io.StringIO() as output:
    with contextlib.redirect_stdout(output):
        print("Hello, world!")
    contents = output.getvalue()

print(contents)
```

В этом примере стандартный вывод перенаправляется в объект io.StringIO(), 
а затем содержимое этого объекта выводится на экран.

Модуль contextlib содержит и другие функции, такие как closing, nullcontext и ExitStack. 
Они все предназначены для упрощения работы с контекстными менеджерами в Python.










#### contextlib.closing
Это функция, которая превращает объект с методом close() в контекстный менеджер. 
Это может быть полезно, например, для работы с файлами или соединениями. 
Пример использования:

```python
import contextlib
from urllib.request import urlopen

with contextlib.closing(urlopen("https:&sol;&sol;www.example.com/")) as page:
    for line in page:
        print(line.decode("utf-8"))
```

В этом примере urlopen("https:&sol;&sol;www.example.com/") возвращает объект с методом close(), 
который используется внутри контекстного менеджера closing.



#### contextlib.nullcontext
Это класс, который предоставляет пустой контекстный менеджер, который не делает ничего. 
Он может быть использован, когда нужен контекстный менеджер, 
но никакой реальной работы в контексте выполнять не требуется. 
Пример использования:

```python
import contextlib

with contextlib.nullcontext():
    print("Hello, world!")
```

В этом примере ничего не происходит в контексте, но благодаря использованию nullcontext, 
код работает корректно в рамках контекстного менеджера.


#### contextlib.ExitStack
Это класс, который предоставляет возможность управления несколькими контекстными менеджерами одновременно. 
Он может быть использован, когда требуется обеспечить надежное управление ресурсами в случае, 
когда ресурсы могут быть открыты и закрыты в произвольном порядке. 
Пример использования:

```python
import contextlib

with contextlib.ExitStack() as stack:
    files = [stack.enter_context(open(f)) for f in ["file1.txt", "file2.txt", "file3.txt"]]
    for file in files:
        print(file.readline())
```

В этом примере ExitStack используется для управления тремя файлами, которые могут быть открыты и закрыты в любом порядке
Функция stack.enter_context(open(f)) добавляет каждый файл в стек контекстных менеджеров, 
который гарантирует их правильное закрытие в конце работы с ними.
""",
                    "setuptools": """
| Метод                     | Описание                                                     |
|---------------------------|--------------------------------------------------------------|
| setup()                   | Определяет настройки проекта и его зависимости.              |
| find_packages()           | Автоматически находит и включает все пакеты проекта.         |
| find_namespace_packages() | Аналогично find_packages(), но для пространств имен.         |
| setup_requires            | Зависимости, необходимые для установки проекта.              |
| install_requires          | Зависимости, необходимые для работы проекта.                 |
| entry_points              | Позволяет определить точки входа (entry points) для проекта. |

**setup()**

Описание: Определяет основные настройки проекта и его зависимости.


```python
from setuptools import setup

setup(
    name="mypackage",
    version="1.0.0",
    packages=["mypackage"],
    install_requires=["requests"],
)
```

**find_packages()**

Описание: Автоматически находит и включает все пакеты проекта.

```python
from setuptools import setup, find_packages

setup(
    name="mypackage",
    version="1.0.0",
    packages=find_packages(),
)
```

**entry_points**

Описание: Позволяет определить точки входа (entry points) для проекта, например, для создания скриптов командной строки.

```python
from setuptools import setup

setup(
    name="mypackage",
    version="1.0.0",
    entry_points={
        "console_scripts": [
            "myscript = mypackage.script:main",
        ],
    },
)
```
""",
                    "importlib": """
```pycon
>>> def im():
...     import math
...
>>> math
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'math' is not defined
>>> im()
>>> math
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'math' is not defined
```

```python
import importlib

importlib.reload(my_module)
```

```python
import subprocess
import importlib

library_name = input("Введите название библиотеки, которую вы хотите установить: ")

# проверяем, установлена ли библиотека
try:
    importlib.import_module(library_name)
    print(f"Библиотека {library_name} уже установлена.")
except ImportError:
    # устанавливаем библиотеку
    subprocess.call(["pip", "install", library_name])
    print(f"Библиотека {library_name} установлена успешно.")

```
""",
                    "logging": r"""
Библиотека "logging" в Python используется для добавления логирования,
то есть записи информации о работе программы, чтобы отслеживать ее выполнение и находить ошибки или проблемы.

Методы модуля "logging" и его подмодулей:

`getLogger()`: Возвращает объект логгера для указанного имени.
`basicConfig()`: Конфигурирует логгинг с использованием базовых параметров.
`Logger.setLevel()`: Устанавливает уровень логгирования для указанного логгера.
`Logger.addHandler()`: Добавляет обработчик к указанному логгеру.
`Formatter.format()`: Форматирует записи логгера в определенном формате.
`StreamHandler`: Обработчик, который выводит сообщения логгера в поток (например, на консоль).
`FileHandler`: Обработчик, который выводит сообщения логгера в файл.
`RotatingFileHandler`: Обработчик, который выводит сообщения логгера в файл с возможностью
автоматического поворота лог-файла при достижении определенного размера или количества записей.

Наиболее часто используемые методы:

`logging.debug()`: Регистрирует отладочное сообщение.

```python
import logging
logging.debug("This is a debug message")
```

`logging.info()`: Регистрирует информационное сообщение.

```python
import logging
logging.info("This is an info message")
```

`logging.warning()`: Регистрирует предупреждение.

```python
import logging
logging.warning("This is a warning message")
```

`logging.error()`: Регистрирует сообщение об ошибке.

```python
import logging
logging.error("This is an error message")
```

`logging.critical()`: Регистрирует критическое сообщение.

```python
import logging
logging.critical("This is a critical message")
```




import logging

Запись в файл

```python
logging.basicConfig(filename="example.log",
                    level=logging.DEBUG)
```

Запись в консоль

```python
logging.basicConfig(level=logging.DEBUG,
                    format="%(message)s")
```

Запись в файл и в консоль

```python
logging.basicConfig(filename="example.log",
                    level=logging.DEBUG,
                    format="%(asctime)s %(levelname)s %(message)s",
                    datefmt="%Y-%m-%d %H:%M:%S")
console = logging.StreamHandler()
console.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s "
                              "%(levelname)s "
                              "%(message)s",
                              datefmt="%Y-%m-%d %H:%M:%S")
console.setFormatter(formatter)
logging.getLogger("").addHandler(console)
```

Для самих сообщений

```
%s           строка
%d           для целых чисел
%c           для имени логгера
%f           для чисел с плавающей точкой
%r           для строковых представлений объектов
%m           для сообщения журнала
%x           целое число в шестнадцатеричной системе исчисления
%o           целое число в восьмеричной системе исчисления
%e, %E       число в экспоненциальной форме
```

Для настроек логгирования

```
%(message)s     сообщение журнала

%(asctime)s     время записи сообщения в формате (по умолчанию YYYY-MM-DD HH:MM:SS,sss настраивать в basicConfig(datefmt))
%(created)f     время записи сообщения в секундах, начиная с 1 января 1970 года

%(filename)s    имя файла, в котором был вызван логгер
%(funcName)s    имя функции, в которой был вызван логгер
%(name)s        имя логгера, который записывает сообщение
%(module)s      имя модуля, в котором был вызван логгер
%(threadName)s  имя потока, в котором был вызван логгер
%(processName)s имя процесса, в котором был вызван логгер

%(levelname)s   уровень журнала (например, DEBUG, INFO, WARNING, ERROR, CRITICAL)
%(levelno)s     уровень журнала в числовом формате (10 для DEBUG, 20 для INFO и т. д.)

%(lineno)d      номер строки, в которой был вызван логгер
%(pathname)s    полный путь к файлу, в котором был вызван логгер
%(process)d     идентификатор процесса, в котором был вызван логгер
%(thread)d      идентификатор потока, в котором был вызван логгер
```


Код для применения функций к тексту

```python
logging.info = lambda msg, *args, f=logging.info: f(Up(msg), *args)
```
""",
                    "tabnanny": """
Модуль tabnanny в Python используется для проверки исходных файлов
на наличие проблем с табуляцией, которые могут вызвать синтаксические ошибки.

| Метод                  | Описание                                               |
|------------------------|--------------------------------------------------------|
| process_tokens(tokens) | Проверяет токены файла на проблемы с табуляцией.       |
| NannyToken(token)      | Конструктор класса токенов, используемый для проверки. |

**process_tokens(tokens)** Проверяет токены файла на наличие проблем с табуляцией.

```python
import tokenize
from tabnanny import process_tokens

with open("file.py", "rb") as f:
    process_tokens(tokenize.generate_tokens(f.readline))
```
""",
                    "atexit": """
Модуль atexit в Python предоставляет возможность регистрации функций,
которые будут выполнены при завершении программы.
Это позволяет управлять завершением программы и выполнением дополнительных действий перед выходом.

| Метод/Подмодуль       | Описание                                                          |
|-----------------------|-------------------------------------------------------------------|
| atexit.register(func) | Регистрирует функцию func для выполнения при выходе из программы. |

**atexit.register(func)** Регистрирует функцию для выполнения при выходе из программы.

```python
import atexit

def exit_handler():
    print("Выход из программы")

atexit.register(exit_handler)
```
""",
                    "pstats": """
Библиотека "pstats" в Python используется для профилирования производительности программы.
Она предоставляет возможность анализировать данные о времени выполнения и вызовах функций,
что помогает оптимизировать код и улучшить его производительность.

Методы и подмодули библиотеки "pstats" включают:

"Stats" (статистика)
    - "add" - добавляет данные о времени выполнения и вызовах функций в статистику.
    - "print_stats" - выводит общую статистику по вызовам функций.
    - "sort_stats" - сортирует статистику по различным критериям.
    - "strip_dirs" - удаляет пути к файлам из статистики.
    - "calc_callees" - вычисляет информацию о вызываемых функциях.
    - "dump_stats" - сохраняет статистику в файл.

"Profile" (профиль)
    - "run" - запускает профилирование кода.
    - "runcall" - профилирует отдельный вызов функции.
    - "print_stats" - выводит статистику по профилированию.
    - "dump_stats" - сохраняет статистику в файл.

Некоторые из наиболее часто используемых методов "pstats" включают:

"print_stats()": Выводит основную статистику профилирования, включая время выполнения и количество вызовов функций.

Пример кода, демонстрирующего его использование:

```python
import pstats

# Создаем объект статистики
stats = pstats.Stats("profile_result")

# Выводим статистику на экран
stats.print_stats()

```

"sort_stats()": Сортирует статистику профилирования по выбранному критерию, такому как время выполнения или количество вызовов функций.

Пример кода, демонстрирующего его использование:

```python
import pstats

# Создаем объект статистики
stats = pstats.Stats("profile_result")

# Сортируем статистику по времени выполнения
stats.sort_stats("time")

# Выводим отсортированную статистику на экран
stats.print_stats()

```

Пожалуйста, обратите внимание, что примеры кода могут требовать предварительной настройки и обработки профилировочных данных.
""",
                    "getpass": r"""
Библиотека "getpass" в Python используется для безопасного ввода паролей и других конфиденциальных
данных пользователем в командной строке или интерактивной среде.

Методы модуля "getpass" и его подмодулей:

| Метод                                                                   | Описание                                                                                                                                         |
|-------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| getpass.getpass(prompt="Password: ", stream=None)                       | Запрашивает у пользователя ввод пароля с подсказкой<br>"Password: "<br>Возвращает введенный пароль в виде строки                                 |
| getpass.getuser()                                                       | Возвращает имя текущего пользователя операционной системы                                                                                        |
| getpass.getpass(prompt="Password: ", stream=None, fg=None, bg=None)     | Запрашивает у пользователя ввод пароля с подсказкой<br>"Password: "<br>Можно настроить цвет текста и фона подсказки                              |
| getpass.getpass(prompt="Password: ", stream=None, echo=True, mask=None) | Запрашивает у пользователя ввод пароля с подсказкой<br>"Password: "<br>Можно настроить отображение введенных символов (эхо) и символа-маскировки |

Самые часто используемые методы:

| Метод                                             | Описание                                                   |
|---------------------------------------------------|------------------------------------------------------------|
| getpass.getpass(prompt="Password: ", stream=None) | Запрашивает у пользователя ввод пароля с подсказкой        |
| getpass.getuser()                                 | Возвращает имя текущего пользователя операционной системы. |
""",
                    "reprlib": r"""
Библиотека "reprlib" используется для создания ограниченных представлений (сокращений) объектов в строковом виде.
Она предоставляет функциональность для генерации усеченных строковых представлений сложных объектов, таких как контейнеры,
чтобы они были более читаемыми и компактными.

Методы модуля "reprlib" и его подмодулей:

| Метод                    | Описание
|--------------------------|--------------
| reprlib.repr()           | Возвращает сокращенное строковое представление объекта с ограничением символов.
| reprlib.aRepr()          | Возвращает сокращенное представление объекта, указывая максимальное количество символов и добавляя многоточие в конце при необходимости.
| reprlib.recursive_repr() | Декоратор функции, который позволяет модифицировать стандартный метод `__repr__` для обработки рекурсивных вызовов.
| reprlib.dllist()         | Класс-контейнер, предоставляющий сокращенное строковое представление для двусвязного списка.
| reprlib.Repr()           | Класс, используемый для изменения поведения библиотеки "reprlib" путем настройки различных параметров.

Список самых часто используемых методов, их описание и

| Метод                    | Описание | Пример кода
|--------------------------|-------------- | -------------
| reprlib.repr()           | Возвращает ограниченное строковое представление объекта | obj = [1, 2, 3, 4, 5]; print(reprlib.repr(obj))
| reprlib.aRepr()          | Возвращает сокращенное представление объекта с максимальным количеством символов и многоточием | obj = "This is a long string"; print(reprlib.aRepr(obj, 10))
| reprlib.recursive_repr() | Декоратор для изменения поведения метода `__repr__` для обработки рекурсивных вызовов | @reprlib.recursive_repr(); def __repr__(self): return "MyClass()"
| reprlib.dllist()         | Класс-контейнер для двусвязного списка с ограниченным строковым представлением | dll = reprlib.dllist([1, 2, 3]); print(dll)
| reprlib.Repr()           | Класс для настройки поведения библиотеки "reprlib" | r = reprlib.Repr(); r.maxstring = 20; obj = "This is a long string"; print(r.repr(obj))

""",
                    "trace": r"""
Библиотека "trace" используется в Python для отладки и трассировки выполнения программы.
Она предоставляет инструменты для отслеживания, как программа выполняется и какие функции вызываются.

Методы модуля "trace" и его подмодулей:
`traceback.print_exc(limit=None, file=None, chain=True)` - выводит трассировку текущего исключения в файл или stdout.
`traceback.format_exc(limit=None, chain=True)` - возвращает трассировку текущего исключения в виде строки.
`sys.settrace(tracefunc)` - устанавливает функцию трассировки для последующих вызовов.
`sys.gettrace()` - возвращает текущую функцию трассировки.
`sys.setprofile(profilefunc)` - устанавливает функцию профилирования для последующих вызовов.
`sys.getprofile()` - возвращает текущую функцию профилирования.

`traceback.print_exc()` - выводит трассировку текущего исключения в стандартный вывод.

```python
try:
    # код, который может вызвать исключение
except Exception:
    traceback.print_exc()
```

`sys.settrace()` - устанавливает функцию трассировки для отслеживания вызовов функций.

```python
def trace_func(frame, event, arg):
    print(f"Calling function {frame.f_code.co_name}")
    return trace_func

sys.settrace(trace_func)
# код, вызывающий функции
sys.settrace(None)  # отключение трассировки
```

`sys.setprofile()` - устанавливает функцию профилирования для измерения времени выполнения функций.

```python
import cProfile

def profile_func(frame, event, arg):
    profiler = cProfile.Profile()
    profiler.enable()
    return profiler

sys.setprofile(profile_func)
# код, вызывающий функции
sys.setprofile(None)  # отключение профилирования
```

Существует более широкий набор функций и методов, которые могут быть полезны в разных ситуациях.
""",
                    "traceback": r"""
Библиотека "traceback" используется в Python для отображения трассировки стека, то есть печати
информации об исключении и последующих вызовах функций, которые привели к возникновению исключения.
Она помогает в отладке и идентификации причин возникновения ошибок в программе.

Методы и подмодули библиотеки "traceback" включают:
`traceback.print_tb(tb, limit=None, file=None)` - выводит трассировку стека в заданный файл (по умолчанию в sys.stdout) в виде списка строк.
`traceback.print_exception(etype, value, tb, limit=None, file=None)` - выводит полную информацию об исключении, включая тип и значение исключения, трассировку стека и подробности.
`traceback.print_exc(limit=None, file=None, chain=True)` - выводит трассировку стека последнего возникшего исключения.
`traceback.format_tb(tb, limit=None)` - возвращает трассировку стека в виде списка строк.
`traceback.format_exception(etype, value, tb, limit=None)` - возвращает полную информацию об исключении в виде списка строк.
`traceback.format_exc(limit=None, chain=True)` - возвращает трассировку стека последнего возникшего исключения в виде строки.

Некоторые из наиболее часто используемых методов в библиотеке "traceback" включают:
Метод `print_tb()` используется для вывода трассировки стека в стандартном выводе.

```python
import traceback

try:
    # некоторый код, в котором может произойти исключение
    x = 1 / 0
except:
    traceback.print_tb(sys.exc_info()[2])
```

Метод `print_exception()` используется для вывода полной информации об исключении, включая тип, значение и трассировку стека.

```python
import traceback

try:
    # некоторый код, в котором может произойти исключение
    x = 1 / 0
except:
    traceback.print_exception(*sys.exc_info())
```

Метод `format_exc()` используется для получения трассировки стека последнего возникшего исключения в виде строки.

```python
import traceback

try:
    # некоторый код, в котором может произойти исключение
    x = 1 / 0
except:
    error_traceback = traceback.format_exc()
    print(error_traceback)
```

Помните, что без дополнительного контекста исключения и вашего кода, приведенные примеры могут не работать напрямую.
Не забывайте адаптировать их под свои потребности и проверять документацию для более подробной информации о библиотеке "traceback".
""",
                    "warnings": r"""
Библиотека "warnings" в Python используется для управления предупреждениями, которые могут возникать во время выполнения программы.
Она позволяет контролировать вывод предупреждений и принимать соответствующие действия.

Методы и подмодули библиотеки "warnings":

`warn(message, warning_type, stacklevel)` - генерирует предупреждение с указанным сообщением, типом предупреждения и уровнем стека.
`filterwarnings(action, message, category, module, lineno, append)` - устанавливает фильтр для предупреждений, определяя действие, текст сообщения, категорию предупреждения, модуль, номер строки и флаг добавления фильтра.
`simplefilter(action, category=Warning, lineno=0, append=False)` - устанавливает простой фильтр для предупреждений с указанным действием, категорией, номером строки и флагом добавления фильтра.
`resetwarnings()` - сбрасывает все установленные фильтры предупреждений.
`showwarning(message, category, filename, lineno, file=None, line=None)` - выводит предупреждение с указанным сообщением, категорией, исходным файлом, номером строки, файлом вывода и строкой кода.
`catch_warnings(*, record=False, module=None)` - возвращает контекстный менеджер для временного перехвата предупреждений с опциональной записью в список или указанный модуль.

`warn(message, warning_type, stacklevel)` - генерирует предупреждение с заданным сообщением, типом предупреждения и уровнем стека.

```python
import warnings

warnings.warn("This is a warning message", UserWarning, stacklevel=2)
```

`filterwarnings(action, message, category, module, lineno, append)` - устанавливает фильтр для предупреждений с указанными параметрами.

```python
import warnings

warnings.filterwarnings("ignore", category=DeprecationWarning, module="my_module")
```

`simplefilter(action, category=Warning, lineno=0, append=False)` - устанавливает простой фильтр для предупреждений с указанным действием и категорией.

```python
import warnings

warnings.simplefilter("ignore", DeprecationWarning)
```

`resetwarnings()` - сбрасывает все установленные фильтры предупреждений.

```python
import warnings

warnings.resetwarnings()
```

`showwarning(message, category, filename, lineno, file=None, line=None)` - выводит предупреждение с указанными параметрами.

```python
import warnings

warnings.showwarning("This is a warning message", UserWarning, "example.py", 10)
```

`catch_warnings(*, record=False, module=None)` - контекстный менеджер для временного перехвата предупреждений.

```python
import warnings

with warnings.catch_warnings(record=True) as w:
    warnings.warn("This is a warning message")
    print(w[0].message)
```
""",
                    "keyword": r"""
Библиотека "keyword" в Python используется для работы с ключевыми словами языка.
Она предоставляет набор функций для проверки и манипуляции ключевыми словами, такими как "if", "for", "while" и другими.

Таблица методов модуля "keyword":
iskeyword(): Проверяет, является ли переданная строка ключевым словом в Python.
kwlist: Возвращает список всех ключевых слов в Python.

iskeyword():

```python
import keyword

print(keyword.iskeyword("if"))  # True
print(keyword.iskeyword("hello"))  # False
```

iskeyword(): Позволяет проверить, является ли строка ключевым словом Python.
kwlist: Возвращает список всех ключевых слов в Python.
""",
                    "frozenlist": r"""
Описание: библиотека "frozenlist" служит для создания неизменяемых списков в Python,
аналогично тому, как `tuple` предоставляет неизменяемую версию `list`.

Таблица методов:

| Метод          | Описание                                  |
|----------------|-------------------------------------------|
| __init__()     | Инициализирует новый объект frozenlist.   |
| __contains__() | Проверяет наличие элемента в списке.      |
| __getitem__()  | Получает элемент списка по индексу.       |
| __len__()      | Возвращает количество элементов в списке. |
| copy()         | Возвращает копию frozenlist.              |

Список самых частых методов, краткое описание и работающие примеры:

```python
# Метод __init__()
flist = frozenlist([1, 2, 3, 4, 5])
# Метод __contains__()
print(3 in flist)  # True, так как 3 есть в списке
# Метод __getitem__()
print(flist[1])    # 2, так как это элемент на позиции 1
# Метод __len__()
print(len(flist))  # 5, так количество элементов в списке равно 5
# Метод copy()
flist_copy = flist.copy()  # Создаст копию списка
```

Пожалуйста, убедитесь, что установлена библиотека `frozenlist`.
Если нет, используйте данную команду для установки - `pip install frozenlist`.
""",
                    "runpy": r"""
Библиотека "runpy" в Python используется для выполнения модулей как скриптов, а также для загрузки и выполнения кода из файлов или строк.
Методы модуля "runpy" и его подмодулей:

Метод | Описание
----- | --------
run_path(path, \[globals=None, locals=None\]) | Загружает и выполняет код из указанного файла по заданному пути.
run_module(mod_name, \[init_globals=None, run_name=None, alter_sys=False\]) | Загружает и выполняет указанный модуль.

""",
                    "zipimport": r"""
Библиотека "zipimport" в Python используется для импорта модулей из zip-архивов.
Она предоставляет возможность загружать и использовать код, хранящийся в сжатом формате,
что может быть полезно для эффективного распространения и дистрибуции приложений.

Вот таблица методов и подмодулей библиотеки "zipimport" и их краткое описание:

Метод/Подмодуль    | Описание
---------------------------------------
zipimport.zipimporter   | Класс, который позволяет импортировать модули из zip-архивов.
zipimport.zipimporter.get_code   | Возвращает объект кода модуля.
zipimport.zipimporter.get_data   | Возвращает содержимое файла из zip-архива.
zipimport.zipimporter.get_filename   | Возвращает имя файла из zip-архива, соответствующего модулю.
zipimport.zipimporter.get_source   | Возвращает исходный код модуля в виде строки.

Вот список самых часто используемых методов библиотеки "zipimport", их краткое описание и пример кода, демонстрирующего их работу:

zipimport.zipimporter.get_code Возвращает объект кода модуля.

```python
import zipimport

importer = zipimport.zipimporter("module.zip")
code_object = importer.get_code("module")
```

zipimport.zipimporter.get_data Возвращает содержимое файла из zip-архива.

```python
import zipimport

importer = zipimport.zipimporter("module.zip")
data = importer.get_data("file.txt")
```

zipimport.zipimporter.get_filename Возвращает имя файла из zip-архива, соответствующего модулю.

```python
import zipimport

importer = zipimport.zipimporter("module.zip")
filename = importer.get_filename("module")
```

zipimport.zipimporter.get_source Возвращает исходный код модуля в виде строки.

```python
import zipimport

importer = zipimport.zipimporter("module.zip")
source_code = importer.get_source("module")
```
""",
                    "zipapp": r"""
Библиотека "zipapp" в Python используется для упаковки и запуска приложений в формате ZIP.
Это позволяет создавать самодостаточные исполняемые файлы, которые можно легко передавать и развертывать.

Методы модуля "zipapp" и его подмодулей:

zipapp.create_archive(target, interpreter=None, main=None, *additional_files):
Создает ZIP-архив на основе указанных файлов и опционально добавляет интерпретатор и точку входа в приложение.

zipapp.get_interpreter(path):
Возвращает путь к интерпретатору Python, используемому для запуска приложения.

zipapp.get_metadata(entry):
Возвращает метаданные (метатеги) для указанной записи в ZIP-архиве.

zipapp.get_asset_name(entry):
Возвращает имя актива (файла) для указанной записи в ZIP-архиве.

zipapp.get_zip_uri(archive_path):
Возвращает URI для доступа к ZIP-архиву.

Некоторые из самых часто используемых методов:

create_archive: Создает ZIP-архив с указанными файлами.

```python
import zipapp

zipapp.create_archive("myapp.zip", interpreter="/usr/bin/python3", main="main.py", "additional_file1.txt", "additional_file2.dat")
```

get_interpreter: Возвращает путь к интерпретатору Python, используемому для запуска приложения.

```python
import zipapp

interpreter_path = zipapp.get_interpreter("myapp.zip")
print(f"Интерпретатор: {interpreter_path}")
```

get_metadata: Возвращает метаданные (метатеги) для указанной записи в ZIP-архиве.

```python
import zipapp

metadata = zipapp.get_metadata("myapp.zip/main.py")
print(f"Метаданные: {metadata}")
```

get_asset_name: Возвращает имя актива (файла) для указанной записи в ZIP-архиве.

```python
import zipapp

asset_name = zipapp.get_asset_name("myapp.zip/main.py")
print(f"Имя актива: {asset_name}")
```

Пожалуйста, обратите внимание, что приведенные примеры являются общими и могут потребоваться дополнительные настройки
в зависимости от вашего конкретного случая использования.
""",
                    "zipfile": r"""
Библиотека "zipfile" в Python используется для работы с архивами формата ZIP.
Она предоставляет функциональность для создания, чтения, обновления и извлечения файлов из архива.

Таблица методов библиотеки "zipfile" и их краткого описания:

`ZipFile(file, mode="r", compression=ZIP_STORED, allowZip64=True)` - создает объект ZipFile, представляющий архив ZIP из файла. Режимы могут быть чтение ("r"), запись ("w") или добавление ("a").
`ZipFile.extractall(path=None, members=None, pwd=None)` - извлекает все файлы из архива в указанную папку.
`ZipFile.extract(member, path=None, pwd=None)` - извлекает конкретный файл из архива.
`ZipFile.namelist()` - возвращает список имен файлов в архиве.
`ZipFile.open(name, mode="r", pwd=None)` - открывает файл в архиве и возвращает объект файлового дескриптора.
`ZipFile.close()` - закрывает объект ZipFile и освобождает ресурсы.

Список самых часто используемых методов, их краткого описания и пример демонстрирующий их работу:

`extractall(path=None, members=None, pwd=None)` - извлекает все файлы из архива в указанную папку.

```python
import zipfile

# Открываем архив
with zipfile.ZipFile("archive.zip", "r") as zip_ref:
    # Извлекаем все файлы
    zip_ref.extractall("destination_folder")
```

`namelist()` - возвращает список имен файлов в архиве.

```python
import zipfile

# Открываем архив
with zipfile.ZipFile("archive.zip", "r") as zip_ref:
    # Получаем список имен файлов
    file_names = zip_ref.namelist()

    # Выводим список имен файлов
    for name in file_names:
        print(name)
```

`extract(member, path=None, pwd=None)` - извлекает конкретный файл из архива.

```python
import zipfile

# Открываем архив
with zipfile.ZipFile("archive.zip", "r") as zip_ref:
    # Извлекаем файл с именем "file.txt"
    zip_ref.extract("file.txt", "destination_folder")
```
""",
                    "marshal": r"""
Библиотека "marshal" в Python используется для сериализации и десериализации объектов.
Она предоставляет функциональность для сохранения объектов в бинарном формате и восстановления их позже.

Методы модуля "marshal" и их краткое описание:
`dump(obj, file)` - Сериализует объект `obj` и записывает его в файл `file`.
`load(file)` - Читает сериализованные данные из файла `file` и восстанавливает объект.
`dumps(obj)` - Возвращает сериализованное представление объекта `obj` в виде строки.
`loads(bytes)` - Восстанавливает объект из сериализованного представления, передаваемого в виде строки `bytes`.
`version` - Целое число, представляющее версию протокола сериализации.

Наиболее распространенные методы "marshal" и их описание:

`dump(obj, file)` - Сериализует объект `obj` и записывает его в файл `file`.
```python
import marshal

data = {"name": "John", "age": 30}
with open("data.bin", "wb") as file:
    marshal.dump(data, file)
```

`load(file)` - Читает сериализованные данные из файла `file` и восстанавливает объект.
```python
import marshal

with open("data.bin", "rb") as file:
    data = marshal.load(file)
    print(data)  # {"name": "John", "age": 30}
```

`dumps(obj)` - Возвращает сериализованное представление объекта `obj` в виде строки.
```python
import marshal

data = {"name": "John", "age": 30}
serialized = marshal.dumps(data)
print(serialized)
```

`loads(bytes)` - Восстанавливает объект из сериализованного представления, передаваемого в виде строки `bytes`.
```python
import marshal

serialized = (
    b"\x80\x04\x95\x0f\x00\x00\x00\x00\x00\x00\x8c\x08\x00\x00\x00Hello!"
    b"\x94\x8c\x01\x00\x00\x00x\x94\x8c\x01\x00\x00\x00y\x94\x2e\x94\x94"
    b"\x8c\x06\x00\x00\x00result\x94\x94\x8c\x05\x00\x00\x00float\x94\x93\x00\x00\x00\x00\x00\x00\x00."
)

data = marshal.loads(serialized)
print(data)  # {"Hello!": {"x": "y", "result": None, "float": 0.0}}
```
""",
                    "formatter": r"""
Библиотека "formatter" в Python используется для форматирования и стилизации
текста в различных вариантах вывода, таких как консоль, файлы, строки и другие.
2.
Методы модуля "formatter":
format_text(): Форматирует указанный текст в соответствии с заданными параметрами.
stylize_text(): Применяет стилизацию к тексту, используя заданные форматы и цвета.
capitalize_text(): Преобразует первую букву каждого слова в тексте в верхний регистр.
align_text(): Выравнивает текст по заданному формату выравнивания (левому, правому или по центру).
truncate_text(): Обрезает текст до указанной длины и добавляет многоточие в конце, если текст был обрезан.

Подмодули "formatter":
html_format: Включает методы для форматирования текста в формате HTML.
csv_format: Содержит методы для форматирования текста в формате CSV.
json_format: Включает методы для форматирования текста в формате JSON.
xml_format: Содержит методы для форматирования текста в формате XML.
pdf_format: Включает методы для форматирования текста в формате PDF.

Самые часто используемые методы:
format_text(text, format): Форматирует указанный текст с использованием заданного формата.

formatted_text = formatter.format_text("Привет, мир!", "жирный")
print(formatted_text)  # "Привет, мир!" в жирном формате.

stylize_text(text, style): Применяет заданный стиль к указанному тексту.

stylized_text = formatter.stylize_text("Привет, мир!", "красный")
print(stylized_text)  # "Привет, мир!" в красном цвете.

align_text(text, alignment): Выравнивает указанный текст по заданному формату выравнивания.

aligned_text = formatter.align_text("Привет, мир!", "правый")
print(aligned_text)  # "Привет, мир!" справа выровненным.

Обратите внимание, что код представлен в качестве примера и может потребоваться дополнительная настройка и параметры для достижения желаемого результата.
""",
                    "pyparsing": r"""
Библиотека "pyparsing" используется для анализа и разбора текстовых данных в языке программирования Python.
Она предоставляет возможность создавать грамматики и правила для разбора сложных структур данных.

Методы модуля "pyparsing" и его подмодулей:

parseString(string) - Разбирает строку в соответствии с определенной грамматикой и возвращает структурированные данные.
Word(alphas) - Определяет грамматическое правило для разбора последовательности символов, состоящей только из букв.
nums - Подмодуль, содержащий грамматические правила для разбора числовых значений.
CaselessLiteral(string) - Определяет грамматическое правило для разбора нечувствительных к регистру строк.
QuotedString(quoteChar) - Определяет грамматическое правило для разбора строки, заключенной в кавычки.

Самые часто используемые методы "pyparsing" с их кратким описанием и примером кода:

parseString(string): Разбирает строку в соответствии с грамматикой и возвращает структурированные данные.

```python
from pyparsing import Word, alphas, nums

data = "Hello World"
print(Word(alphas).parseString(data))  # ["Hello"]
```

Word(alphas): Определяет грамматическое правило для разбора последовательности символов, состоящей только из букв.

```python
from pyparsing import Word, alphas

data = "Hello123"
print(Word(alphas).parseString(data))  # ["Hello"]
```

QuotedString(quoteChar): Определяет грамматическое правило для разбора строки, заключенной в кавычки.

```python
from pyparsing import QuotedString

data = '"Hello World"'
print(QuotedString('"').parseString(data))  # ["Hello World"]
```
""",
                    "pyclbr": r"""
Библиотека "pyclbr" в Python используется для анализа и чтения исходного кода классов и функций в модуле.
Она позволяет получить информацию о структуре программы, такую как классы, методы, атрибуты и их связи.

Таблица методов модуля "pyclbr" и его подмодулей:

   Метод              | Описание
   ------------------ | -------------------------------------------------------
   `readmodule()`     | Читает и анализирует модуль, возвращая словарь классов и функций.
   `readmodule_ex()`  | Похож на `readmodule()`, но также возвращает дополнительную информацию о модуле.
   `Class`            | Класс, представляющий отдельный класс из исходного кода.
   `Function`         | Класс, представляющий отдельную функцию из исходного кода.
   `Module`           | Класс, представляющий модуль и его структуру.

`readmodule()` Читает и анализирует модуль, возвращая словарь классов и функций.

```python
import pyclbr

module_data = pyclbr.readmodule("module_name")

for class_name, class_data in module_data.items():
    print(f"Class: {class_name}")
    for method_name, method_data in class_data.methods.items():
        print(f"Method: {method_name}")
```

`Class` Класс, представляющий отдельный класс из исходного кода.

```python
import pyclbr

class_data = pyclbr.Class("class_name")

print(f"Class: {class_data.name}")
for method_name, method_data in class_data.methods.items():
    print(f"Method: {method_name}")
```

`Function` Класс, представляющий отдельную функцию из исходного кода.

```python
import pyclbr

function_data = pyclbr.Function("function_name")

print(f"Function: {function_data.name}")
print(f"Start line: {function_data.lineno}")
```

`Module` Класс, представляющий модуль и его структуру.

```python
import pyclbr

module_data = pyclbr.Module("module_name")

print(f"Module: {module_data.name}")
for class_name, class_data in module_data.classes.items():
    print(f"Class: {class_name}")
```
""",
                    "gast": r"""
Библиотека "gast" используется для анализа и модификации абстрактного синтаксического дерева (AST) в Python.
Она предоставляет инструменты для работы с AST, такие как обход узлов дерева, замена узлов, добавление новых узлов и т.д.

Методы модуля "gast" и его подмодулей:

Модуль "gast":
NodeVisitor: Класс для обхода узлов AST.
NodeTransformer: Класс для модификации узлов AST.
parse: Функция для преобразования исходного кода в AST.


NodeVisitor: Класс, который позволяет обойти все узлы AST и выполнить определенные действия для каждого узла.

```python
from gast import NodeVisitor

class MyVisitor(NodeVisitor):
    def visit_FunctionDef(self, node):
        print("Found a function definition:", node.name)

# Создание экземпляра класса и обход AST
visitor = MyVisitor()
visitor.visit(ast_tree)
```

NodeTransformer: Класс, который позволяет модифицировать узлы AST путем замены, добавления или удаления узлов.

```python
from gast import NodeTransformer

class MyTransformer(NodeTransformer):
    def visit_FunctionDef(self, node):
        # Изменение имени функции
        node.name = "new_function_name"
        return node

# Создание экземпляра класса и модификация AST
transformer = MyTransformer()
new_ast_tree = transformer.visit(ast_tree)
```

parse: Функция, которая преобразует исходный код в AST.

```python
from gast import parse

source_code = "print('Hello, World!')"
ast_tree = parse(source_code)
```
""",
                    "bdb": r"""
Библиотека "bdb" используется в Python для создания отладочных средств и выполнения шагов отладки в программном коде.
Она обеспечивает возможности трассировки исполнения и отладки программ на уровне исходного кода.

| Метод          | Описание                               |
|----------------|----------------------------------------|
| run            | Запускает выполнение программы          |
| set_trace      | Устанавливает точку остановки           |
| clear_all_breaks | Удаляет все установленные точки остановки |
| breakpoint     | Устанавливает точку остановки на текущей позиции |
| set_break      | Устанавливает точку остановки по указанной линии кода |
| clear_break    | Удаляет точку остановки на указанной линии кода |
| get_break      | Возвращает информацию о точке остановки |
| break_here     | Развивает точку остановки и печатает справочные сообщения |
| start          | Запускает процесс отладки               |



set_trace: Устанавливает точку остановки и передает управление в режим интерактивной отладки.

```python
import bdb

def some_function():
    a = 10
    bdb.set_trace()  # Установка точки остановки
    print(a)

some_function()
```
run: Запускает выполнение программы до достижения точки остановки или завершения выполнения.

```python
import bdb

def some_function():
    a = 10
    bdb.set_trace()  # Установка точки остановки
    print(a)

bdb.run("some_function()")
```
breakpoint: Устанавливает точку остановки на текущей позиции выполнения кода.

```python
import bdb

def some_function():
    a = 10
    bdb.breakpoint()  # Установка точки остановки
    print(a)

some_function()
```
""",
                    "faulthandler": r"""
Библиотека "faulthandler" используется для обнаружения и отладки ошибок, связанных с сбоями в программе на языке Python.

Методы и подмодули библиотеки "faulthandler":

faulthandler.enable(): Активирует обработчик сбоев для записи информации о сбое.
faulthandler.disable(): Отключает обработчик сбоев.
faulthandler.is_enabled(): Проверяет, активирован ли обработчик сбоев.
faulthandler.dump_traceback(file=sys.stderr, all_threads=True): Записывает трассировку стека сбоя в указанный файл.
faulthandler.register(signal=SIGUSR1, all_threads=True, chain=True): Регистрирует обработчик сбоев для указанного сигнала.
faulthandler.cancel_dump_traceback(): Прекращает запись трассировки стека сбоя.
faulthandler.cancel_register(): Отменяет регистрацию обработчика сбоев для указанного сигнала.

Наиболее часто используемые методы "faulthandler":

faulthandler.enable(): Активирует обработчик сбоев для записи информации о сбое.

```python
import faulthandler
faulthandler.enable()
```

faulthandler.disable(): Отключает обработчик сбоев.

```python
import faulthandler
faulthandler.disable()
```

faulthandler.dump_traceback(file=sys.stderr, all_threads=True): Записывает трассировку стека сбоя в указанный файл.

```python
import faulthandler
faulthandler.dump_traceback(file=open("traceback.txt", "w"), all_threads=True)
```

Эти методы помогут вам обнаружить и отладить ошибки связанные с сбоями в вашей программе
на языке Python,путем получения информации о трассировке стека сбоя.
""",
                    "gtts": r"""
Библиотека "gtts" (Google Text-to-Speech) используется для преобразования текста в речь.
Она предоставляет возможность синтеза голоса на разных языках, используя голосовые данные от Google.

Методы модуля "gtts":
gTTS(text, lang): принимает текст и язык в качестве параметров и возвращает аудиофайл с синтезированным голосом.
save(file): сохраняет аудиофайл на диск.
get_urls(text): возвращает список URL-адресов, которые могут быть использованы для визуализации прогресса синтеза речи.
lang_check(): проверяет доступные языки для синтеза речи.

Методы подмодуля "gtts.lang":
tld(): возвращает список языков и их TLD (top-level domain).
tts_langs(): возвращает список языков, поддерживаемых gTTS.

Самые часто используемые методы:
gTTS(text, lang): Создает объект gTTS с указанным текстом и языком.
save(file): Сохраняет аудиофайл на диск с использованием указанного имени файла и расширения (.mp3).
get_urls(text): Возвращает список URL-адресов для отслеживания прогресса синтеза речи.

Пример кода для использования библиотеки "gtts":

```python
from gtts import gTTS

text = "Привет, как дела?"
language = "ru"

# Создание объекта gTTS с текстом и языком
tts = gTTS(text=text, lang=language)

# Сохранение аудиофайла
tts.save("output.mp3")

# Получение списка URL-адресов для визуализации прогресса синтеза речи
urls = tts.get_urls(text)
```

Эта библиотека полезна для создания аудиофайлов со сгенерированной речью на разных языках.
""",
                    "rlcompleter": r"""
Библиотека "rlcompleter" используется для автоматического завершения кода в интерактивной оболочке Python (REPL) с помощью клавиши Tab.
Она обеспечивает поддержку автозаполнения имён модулей, функций, переменных и атрибутов.

Методы и подмодули библиотеки "rlcompleter":
Submodule: `rlcompleter`
Метод `Completer(...)` - инициализирует объект автозавершения для использования в REPL.
Метод `Completer.complete(text, state)` - выполняет автозавершение указанного текста в заданном состоянии.
Метод `Completer.global_matches(text)` - возвращает список всех глобальных имен, соответствующих указанному тексту.

Метод `Completer.complete(text, state)` - данный метод выполняет автозавершение текста `text` в конкретном состоянии `state`.

```python
import rlcompleter

completer = rlcompleter.Completer()
text = "pr"
state = 0

completions = completer.complete(text, state)
print(completions)
```

Метод `Completer.global_matches(text)` - данный метод возвращает список глобальных имен, которые соответствуют указанному тексту `text`.

```python
import rlcompleter

completer = rlcompleter.Completer()
text = "pr"

matches = completer.global_matches(text)
print(matches)
```
""",
                    "fileinput": r"""
Библиотека "fileinput" используется для обработки текстовых файлов в Python.
Она предоставляет удобные инструменты для чтения и обработки содержимого файлов.

Методы модуля "fileinput" и его подмодулей:

input(): Возвращает итератор, который построчно читает файлы.
filename(): Возвращает текущее имя файла.
lineno(): Возвращает текущий номер строки файла.
filelineno(): Возвращает текущий номер строки относительно текущего файла.
isfirstline(): Проверяет, является ли текущая строка первой в файле.
isstdin(): Проверяет, читается ли текущая строка с stdin.
nextfile(): Переходит к следующему файлу.
close(): Закрывает файлы, открытые с помощью fileinput.

Некоторые из самых часто используемых методов библиотеки "fileinput" вместе с кратким описанием и примером кода:

input(): Возвращает итератор для построчного чтения файлов.

```python
import fileinput

for line in fileinput.input():
    print(line)
```

filename(): Возвращает текущее имя файла.

```python
import fileinput

for line in fileinput.input():
    print(f"Current file: {fileinput.filename()}")
```

lineno(): Возвращает текущий номер строки файла.

```python
import fileinput

for line in fileinput.input():
    print(f"Line number: {fileinput.lineno()}")
```
""",
                    "abc": """
`abc` предоставляет инструменты для работы с абстрактными базовыми классами (ABC).
Эти классы используются для определения интерфейсов, которые должны реализовывать дочерние классы.


### Основные компоненты

- **`ABC`** — абстрактный базовый класс.
- **`abstractmethod`** — декоратор для определения абстрактных методов,
которые должны быть реализованы в дочерних классах.


```python
from abc import ABC, abstractmethod


class MyAbstractClass(ABC):
    @abstractmethod
    def my_method(self):
        pass

    # Пример абстрактного свойства
    @property
    @abstractmethod
    def my_property(self):
        pass


class ConcreteClass(MyAbstractClass):
    def my_method(self):
        return "Method implemented"

    @property
    def my_property(self):
        return "Property value"


# Попытка создать экземпляр абстрактного класса напрямую вызовет ошибку
# my_abstract_instance = MyAbstractClass()  # Это вызовет TypeError

# Создание экземпляра класса, который реализует все абстрактные методы
concrete_instance = ConcreteClass()
print(concrete_instance.my_method())  # Method implemented
print(concrete_instance.my_property)  # Property value
```

Абстрактный метод в `ABC` не имеет реализации и должен быть переопределён в дочернем классе.
""",
                    "inspect": r"""
# inspect

- Проверка типов объектов `ismodule()`, `isclass()`, `ismethod()`, `isfunction()`, `isgeneratorfunction()`,
`isgenerator()`, `istraceback()`, `isframe()`, `iscode()`, `isbuiltin()`, `isroutine()`
- Получение членов объекта, удовлетворяющих заданному условию - `getmembers()`
<br>
- Поиск исходного кода объекта - `getfile()`, `getsourcefile()`, `getsource()`
- Получение документации по объекту - `getdoc()`, `getcomments()`
- Определение модуля, из которого поступил объект - `getmodule()`
- Упорядочивание классов таким образом, чтобы они представляли их иерархию - `getclasstree()`
<br>
- Получение информации об аргументах функции - `getargvalues()`, `getcallargs()`
- То же самое, с поддержкой функций Python 3 - `getfullargspec()`
- Форматирование спецификации аргумента - `formatargvalues()`
- Получение информации о кадрах - `getouterframes()`, `getinnerframes()`
- Получение текущего кадра стека - `currentframe()`
- Получение информации о кадрах в стеке или в трассировке - `stack()`, `trace()`
<br>
- Получить объект Signature для вызываемого - `signature()`
<br>
- Безопасно вычислить аннотации объекта - `get_annotations()`

# \_\_all\_\_

| **Название**                 | **Описание**                                                                                                                             |
|------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| `ArgInfo`                    | Класс, представляющий информацию об аргументах функции.                                                                                  |
| `Arguments`                  | Класс, описывающий аргументы функции, включая позиционные, ключевые и их значения по умолчанию.                                          |
| `Attribute`                  | Класс для описания атрибутов объекта, используемый внутри библиотеки `inspect`.                                                          |
| `BlockFinder`                | Внутренний класс для поиска блоков кода в исходном файле.                                                                                |
| `BoundArguments`             | Класс, представляющий привязанные аргументы функции после вызова.                                                                        |
| `CORO_CLOSED`                | Константа, указывающая, что корутина закрыта.                                                                                            |
| `CORO_CREATED`               | Константа, указывающая, что корутина создана, но еще не запущена.                                                                        |
| `CORO_RUNNING`               | Константа, указывающая, что корутина в процессе выполнения.                                                                              |
| `CORO_SUSPENDED`             | Константа, указывающая, что корутина приостановлена.                                                                                     |
| `CO_ASYNC_GENERATOR`         | Флаг состояния объекта кода, указывающий, что это асинхронный генератор.                                                                 |
| `CO_COROUTINE`               | Флаг состояния объекта кода, указывающий, что это корутина.                                                                              |
| `CO_GENERATOR`               | Флаг состояния объекта кода, указывающий, что это генератор.                                                                             |
| `CO_ITERABLE_COROUTINE`      | Флаг состояния объекта кода, указывающий, что это итерируемая корутина.                                                                  |
| `CO_NESTED`                  | Флаг состояния объекта кода, указывающий, что функция является вложенной.                                                                |
| `CO_NEWLOCALS`               | Флаг состояния объекта кода, указывающий, что функция использует новые локальные переменные.                                             |
| `CO_NOFREE`                  | Флаг состояния объекта кода, указывающий, что функция не использует свободные переменные.                                                |
| `CO_OPTIMIZED`               | Флаг состояния объекта кода, указывающий, что функция оптимизирована.                                                                    |
| `CO_VARARGS`                 | Флаг состояния объекта кода, указывающий,<br>что функция принимает произвольное количество позиционных аргументов (*args).               |
| `CO_VARKEYWORDS`             | Флаг состояния объекта кода, указывающий,<br>что функция принимает произвольное количество именованных аргументов (**kwargs).            |
| `ClassFoundException`        | Исключение, возникающее при поиске класса в дереве наследования.                                                                         |
| `ClosureVars`                | Класс, представляющий закрытые переменные функции (closure variables).                                                                   |
| `EndOfBlock`                 | Класс, обозначающий конец блока кода при анализе исходного файла.                                                                        |
| `FrameInfo`                  | Класс, представляющий информацию о фрейме стека вызовов (файл, строка, функция и т.д.).                                                  |
| `FullArgSpec`                | Класс, представляющий полную спецификацию аргументов функции,<br>включая позиционные, ключевые, аргументы с дефолтными значениями и т.д. |
| `GEN_CLOSED`                 | Константа, указывающая, что генератор закрыт.                                                                                            |
| `GEN_CREATED`                | Константа, указывающая, что генератор создан, но еще не запущен.                                                                         |
| `GEN_RUNNING`                | Константа, указывающая, что генератор в процессе выполнения.                                                                             |
| `GEN_SUSPENDED`              | Константа, указывающая, что генератор приостановлен.                                                                                     |
| `Parameter`                  | Класс, представляющий отдельный параметр функции, включая его имя, тип и значение по умолчанию.                                          |
| `Signature`                  | Класс, представляющий сигнатуру функции, включая параметры и возвращаемое значение.                                                      |
| `TPFLAGS_IS_ABSTRACT`        | Константа флага, указывающая, что класс является абстрактным.                                                                            |
| `Traceback`                  | Класс, представляющий трассировку исключения (стек вызовов) в момент возникновения исключения.                                           |
| `classify_class_attrs`       | Функция для классификации атрибутов класса на методы, поля и т.д.                                                                        |
| `cleandoc`                   | Функция для очистки строковой документации от лишних отступов и пустых строк.                                                            |
| `currentframe`               | Функция, возвращающая текущий фрейм стека вызовов.                                                                                       |
| `findsource`                 | Функция для поиска исходного кода объекта (функции, класса и т.д.).                                                                      |
| `formatannotation`           | Функция для форматирования аннотаций типов.                                                                                              |
| `formatannotationrelativeto` | Функция для форматирования аннотаций типов относительно указанного модуля.                                                               |
| `formatargvalues`            | Функция для форматирования значений аргументов функции.                                                                                  |
| `get_annotations`            | Функция для получения аннотаций типов объекта.                                                                                           |
| `getabsfile`                 | Функция для получения абсолютного пути к файлу, в котором определен объект.                                                              |
| `getargs`                    | Устаревшая функция для получения имен аргументов функции (используйте `getfullargspec` или `signature`).                                 |
| `getargvalues`               | Функция для получения значений аргументов в текущем фрейме.                                                                              |
| `getattr_static`             | Функция для статического получения атрибута объекта без вызова<br>`__getattr__` и других динамических механизмов доступа к атрибутам.    |
| `getblock`                   | Внутренняя функция для получения блока кода из исходного файла.                                                                          |
| `getcallargs`                | Функция для получения соответствия между аргументами<br>и параметрами функции при вызове с конкретными аргументами.                      |
| `getclasstree`               | Функция для построения дерева наследования классов.                                                                                      |
| `getclosurevars`             | Функция для получения закрытых переменных функции (closure).                                                                             |
| `getcomments`                | Функция для получения комментариев,<br>предшествующих определению объекта (функции, класса и т.д.).                                      |
| `getcoroutinelocals`         | Функция для получения локальных переменных корутины.                                                                                     |
| `getcoroutinestate`          | Функция для получения текущего состояния корутины.                                                                                       |
| `getdoc`                     | Функция для получения строки документации объекта.                                                                                       |
| `getfile`                    | Функция для получения имени файла, в котором определен объект.                                                                           |
| `getframeinfo`               | Функция для получения информации о фрейме стека вызовов.                                                                                 |
| `getfullargspec`             | Функция для получения полной спецификации аргументов функции.                                                                            |
| `getgeneratorlocals`         | Функция для получения локальных переменных генератора.                                                                                   |
| `getgeneratorstate`          | Функция для получения текущего состояния генератора.                                                                                     |
| `getinnerframes`             | Функция для получения всех внутренних фреймов стека вызовов.                                                                             |
| `getlineno`                  | Функция для получения номера строки, где определен объект.                                                                               |
| `getmembers`                 | Функция для получения всех членов объекта<br>(атрибутов, методов и т.д.) с возможностью фильтрации.                                      |
| `getmembers_static`          | Внутренняя функция для статического получения членов объекта.                                                                            |
| `getmodule`                  | Функция для получения модуля, в котором определен объект.                                                                                |
| `getmodulename`              | Функция для получения имени модуля по пути к файлу.                                                                                      |
| `getmro`                     | Функция для получения метода разрешения порядка (MRO) для класса.                                                                        |
| `getouterframes`             | Функция для получения всех внешних фреймов стека вызовов.                                                                                |
| `getsource`                  | Функция для получения исходного кода объекта (функции, класса и т.д.).                                                                   |
| `getsourcefile`              | Функция для получения исходного файла объекта.                                                                                           |
| `getsourcelines`             | Функция для получения исходного кода объекта<br>в виде списка строк и номера начальной строки.                                           |
| `indentsize`                 | Внутренняя функция для определения размера отступа в исходном коде.                                                                      |
| `isabstract`                 | Функция для проверки, является ли класс абстрактным.                                                                                     |
| `isasyncgen`                 | Функция для проверки, является ли объект асинхронным генератором.                                                                        |
| `isasyncgenfunction`         | Функция для проверки, является ли объект функцией асинхронного генератора.                                                               |
| `isawaitable`                | Функция для проверки, можно ли ожидать<br>объект (поддерживает `__await__` или является корутиной).                                      |
| `isbuiltin`                  | Функция для проверки, является ли объект встроенной функцией или методом.                                                                |
| `isclass`                    | Функция для проверки, является ли объект классом.                                                                                        |
| `iscode`                     | Функция для проверки, является ли объект объектом кода (`code object`).                                                                  |
| `iscoroutine`                | Функция для проверки, является ли объект корутиной.                                                                                      |
| `iscoroutinefunction`        | Функция для проверки, является ли объект функцией корутиной.                                                                             |
| `isdatadescriptor`           | Функция для проверки, является ли объект дескриптором данных.                                                                            |
| `isframe`                    | Функция для проверки, является ли объект фреймом стека вызовов.                                                                          |
| `isfunction`                 | Функция для проверки, является ли объект функцией.                                                                                       |
| `isgenerator`                | Функция для проверки, является ли объект генератором.                                                                                    |
| `isgeneratorfunction`        | Функция для проверки, является ли объект функцией генератора.                                                                            |
| `isgetsetdescriptor`         | Функция для проверки, является ли объект дескриптором getset.                                                                            |
| `ismemberdescriptor`         | Функция для проверки, является ли объект дескриптором члена класса.                                                                      |
| `ismethod`                   | Функция для проверки, является ли объект методом.                                                                                        |
| `ismethoddescriptor`         | Функция для проверки, является ли объект дескриптором метода.                                                                            |
| `ismethodwrapper`            | Функция для проверки, является ли объект оберткой метода.                                                                                |
| `ismodule`                   | Функция для проверки, является ли объект модулем.                                                                                        |
| `isroutine`                  | Функция для проверки, является ли объект вызываемой рутиной (функцией или методом).                                                      |
| `istraceback`                | Функция для проверки, является ли объект трассировкой исключения (`traceback object`).                                                   |
| `signature`                  | Функция для получения сигнатуры функции или метода.                                                                                      |
| `stack`                      | Функция для получения текущего стека вызовов в виде списка `FrameInfo`.                                                                  |
| `trace`                      | Функция для трассировки выполнения кода,<br>вызывающая заданную функцию для каждого фрейма стека.                                        |
| `unwrap`                     | Функция для получения оригинальной функции, удаляя все декораторы.                                                                       |
| `walktree`                   | Внутренняя функция для обхода дерева наследования классов.                                                                               |

#### Примечание

- **Константы состояния корутин и генераторов** (`CORO_*`, `GEN_*`, `CO_*`)
используются для определения текущего состояния корутин и генераторов.
- **Внутренние классы и функции** (например, `BlockFinder`, `walktree`)
обычно используются внутри библиотеки `inspect`
и не предназначены для прямого использования пользователями.
- **Функции для работы с аргументами и сигнатурами** (`getfullargspec`, `signature`, `getcallargs`)
позволяют детально анализировать параметры функций и методы их вызова.
- **Функции проверки типов объектов** (`isclass`, `isfunction`, `ismethod` и т.д.)
полезны для динамического анализа объектов во время выполнения программы.
- **Функции для получения исходного кода и документации** (`getsource`, `getdoc`, `findsource`)
позволяют извлекать информацию о коде для целей отладки или генерации документации.
- **Функции работы со стеком вызовов** (`currentframe`, `stack`, `getframeinfo`)
полезны для отладки и анализа выполнения программы.

# Примеры

`import inspect`

### getmembers

```python
class MyClass:
  def method1(self):
      pass

  def method2(self):
      pass

inspect.getmembers(MyClass, inspect.isfunction)
# [("method1", <function MyClass.method1>), ("method2", <function MyClass.method2>)]
```

### signature

```python
def my_function(a, b=10, *args, **kwargs):
  pass

sig = inspect.signature(my_function)
print(sig)  # <Signature (a, b=10, *args, **kwargs)>
print(sig.parameters)
# mappingproxy(OrderedDict([
#     ("a", <Parameter "a">),
#     ("b", <Parameter "b=10">),
#     ("args", <Parameter "*args">),
#     ("kwargs", <Parameter "**kwargs">)
# ]))
```

### stack

```python
def function_a():
    function_b()

def function_b():
    stack = inspect.stack()  # Получение информации о стеке
    for frame in stack:
        print(f"Function {frame.function} at line {frame.lineno} in {frame.filename}")

function_a()
```

### currentframe

```python
frame = inspect.currentframe()  # Получение текущего фрейма
print(f"Current frame at line {frame.f_lineno} in {frame.f_code.co_filename}")
```

# Полезные ссылки

- [Официальная документация](https://docs.python.org/3/library/inspect.html)
- [PEP 362 - Подписи вызовов](https://www.python.org/dev/peps/pep-0362/)
- [Real Python - Inspect Module](https://realpython.com/python-inspect-module/)
""",
                    "operator": """
Библиотека `operator` в Python предоставляет функции, которые соответствуют основным операциям,
таким как арифметические, логические, сравнения и работа с атрибутами, элементами и срезами.
Эти функции полезны для повышения читабельности и производительности кода, особенно
при использовании в функциях высшего порядка, таких как `map()`, `filter()` и `reduce()`.

# Арифметические операции

| Функция                   | Описание            | Пример                            |
|---------------------------|---------------------|-----------------------------------|
| `operator.add(a, b)`      | Возвращает `a + b`  | `operator.add(2, 3)` => `5`       |
| `operator.sub(a, b)`      | Возвращает `a - b`  | `operator.sub(5, 3)` => `2`       |
| `operator.mul(a, b)`      | Возвращает `a * b`  | `operator.mul(2, 3)` => `6`       |
| `operator.truediv(a, b)`  | Возвращает `a / b`  | `operator.truediv(7, 2)` => `3.5` |
| `operator.floordiv(a, b)` | Возвращает `a // b` | `operator.floordiv(7, 2)` => `3`  |
| `operator.mod(a, b)`      | Возвращает `a % b`  | `operator.mod(7, 2)` => `1`       |
| `operator.pow(a, b)`      | Возвращает `a ** b` | `operator.pow(2, 3)` => `8`       |
| `operator.neg(a)`         | Возвращает `-a`     | `operator.neg(5)` => `-5`         |
| `operator.pos(a)`         | Возвращает `+a`     | `operator.pos(-5)` => `-5`        |
| `operator.abs(a)`         | Возвращает `abs(a)` | `operator.abs(-5)` => `5`         |

# Логические операции

| Функция               | Описание                    | Пример                                  |
|-----------------------|-----------------------------|-----------------------------------------|
| `operator.and_(a, b)` | Логическое **И**: `a & b`   | `operator.and_(True, False)` => `False` |
| `operator.or_(a, b)`  | Логическое **ИЛИ**: `a | b` | `operator.or_(True, False)` => `True`   |
| `operator.xor(a, b)`  | Логическое **XOR**: `a ^ b` | `operator.xor(True, False)` => `True`   |
| `operator.not_(a)`    | Логическое **НЕ**: `not a`  | `operator.not_(True)` => `False`        |

# Сравнения

| Функция                 | Описание                | Пример                                  |
|-------------------------|-------------------------|-----------------------------------------|
| `operator.eq(a, b)`     | Возвращает `a == b`     | `operator.eq(2, 2)` => `True`           |
| `operator.ne(a, b)`     | Возвращает `a != b`     | `operator.ne(2, 3)` => `True`           |
| `operator.lt(a, b)`     | Возвращает `a < b`      | `operator.lt(2, 3)` => `True`           |
| `operator.le(a, b)`     | Возвращает `a <= b`     | `operator.le(2, 2)` => `True`           |
| `operator.gt(a, b)`     | Возвращает `a > b`      | `operator.gt(3, 2)` => `True`           |
| `operator.ge(a, b)`     | Возвращает `a >= b`     | `operator.ge(3, 2)` => `True`           |
| `operator.is_(a, b)`    | Возвращает `a is b`     | `operator.is_(a, b)` => `True/False`    |
| `operator.is_not(a, b)` | Возвращает `a is not b` | `operator.is_not(a, b)` => `True/False` |

# Операции с последовательностями

| Функция                       | Описание                                                   | Пример                                                    |
|-------------------------------|------------------------------------------------------------|-----------------------------------------------------------|
| `operator.concat(a, b)`       | Соединяет две последовательности                           | `operator.concat([1, 2], [3, 4])` => `[1, 2, 3, 4]`       |
| `operator.contains(a, b)`     | Проверяет, содержится ли `b` в `a`                         | `operator.contains([1, 2, 3], 2)` => `True`               |
| `operator.countOf(a, b)`      | Возвращает количество вхождений `b` в `a`                  | `operator.countOf([1, 2, 2, 3], 2)` => `2`                |
| `operator.indexOf(a, b)`      | Возвращает индекс первого вхождения `b` в `a`              | `operator.indexOf([1, 2, 3], 2)` => `1`                   |
| `operator.itemgetter(*items)` | Возвращает функцию, которая извлекает элементы по индексам | `f = operator.itemgetter(1, 2); f([1, 2, 3])` => `(2, 3)` |

# Операции с атрибутами и элементами

| Функция                       | Описание                                                   | Пример                                                    |
|-------------------------------|------------------------------------------------------------|-----------------------------------------------------------|
| `operator.attrgetter(attr)`   | Возвращает функцию, которая извлекает атрибут `attr`       | `f = operator.attrgetter("name"); f(obj)` => `"name"`     |
| `operator.itemgetter(*items)` | Возвращает функцию, которая извлекает элементы по индексам | `f = operator.itemgetter(1, 2); f([1, 2, 3])` => `(2, 3)` |
| `operator.setitem(a, b, c)`   | Устанавливает значение `c` элементу `b` в `a`              | `operator.setitem(my_dict, "key", "value")`               |
| `operator.delitem(a, b)`      | Удаляет элемент `b` из `a`                                 | `operator.delitem(my_dict, "key")`                        |
| `operator.getitem(a, b)`      | Извлекает элемент `b` из `a`                               | `operator.getitem(my_list, 0)` => `1`                     |

# Работа с срезами

| Функция                               | Описание                                        | Пример                                              |
|---------------------------------------|-------------------------------------------------|-----------------------------------------------------|
| `operator.index(a)`                   | Возвращает индекс `a`                           | `operator.index([1, 2, 3], 2)` => `1`               |
| `operator.getslice(a, start, end)`    | Возвращает срез списка от `start` до `end`      | `operator.getslice([1, 2, 3, 4], 1, 3)` => `[2, 3]` |
| `operator.setslice(a, start, end, b)` | Заменяет срез списка от `start` до `end` на `b` | `operator.setslice(my_list, 1, 3, [7, 8])`          |
| `operator.delslice(a, start, end)`    | Удаляет срез списка от `start` до `end`         | `operator.delslice(my_list, 1, 3)`                  |

# Примеры использования

### Применение функций `operator` в `map()`
```python
import operator

numbers = [1, 2, 3, 4, 5]
squared = list(map(operator.pow, numbers, [2] * len(numbers)))
print(squared)  # [1, 4, 9, 16, 25]
```

### Использование `itemgetter` для сортировки списка словарей
```python
import operator

students = [
  {"name": "Alice", "age": 25},
  {"name": "Bob", "age": 20},
  {"name": "Charlie", "age": 23},
]
sorted_students = sorted(students, key=operator.itemgetter("age"))
print(sorted_students)
# [{"name": "Bob", "age": 20}, {"name": "Charlie", "age": 23}, {"name": "Alice", "age": 25}]
```
""",
                    "ast": '''
# ast
**Abstract Syntax Tree** — абстрактное синтаксическое дерево
Позволяет анализировать и изменять исходный код Python программ.
Она предоставляет инструменты для разбора (парсинга) Python-кода в дерево синтаксических структур,
а также для создания, модификации и компиляции этих деревьев обратно в исполняемый код.

# Основные функции и классы

### parse
Разбирает Python-код, представленный в виде строки, и возвращает его в виде абстрактного синтаксического дерева (AST).
   
```python
import ast

code = "x = 42"
tree = ast.parse(code)
print(ast.dump(tree, indent=4))
"""
Module(
   body=[
       Assign(
           targets=[Name(id="x", ctx=Store())],
           value=Constant(value=42))
   ],
   type_ignores=[])
"""
```

### dump
```python
ast.dump(node, annotate_fields=True, include_attributes=False, indent=None)
```
Возвращает строковое представление AST-дерева. Если `annotate_fields=True`,
добавляет аннотации полей, если `include_attributes=True`, включает информацию об атрибутах.

```python
code = "y = x + 2"
tree = ast.parse(code)
print(ast.dump(tree, indent=4))
"""
Module(
    body=[
        Assign(
            targets=[
                Name(id="y", ctx=Store())],
            value=BinOp(
                left=Name(id="x", ctx=Load()),
                op=Add(),
                right=Constant(value=2)))],
    type_ignores=[])
"""
```

### NodeVisitor
Класс, предназначенный для обхода узлов дерева.
Переопределяя методы этого класса, можно обрабатывать определённые типы узлов (например, выражения, переменные, функции).

```python
class MyVisitor(ast.NodeVisitor):
    def visit_Assign(self, node):
        print(f"Присваивание найдено: {ast.dump(node)}")
        self.generic_visit(node)

tree = ast.parse("x = 5")
visitor = MyVisitor()
visitor.visit(tree)
# Присваивание найдено: Assign(targets=[Name(id="x", ctx=Store())], value=Constant(value=5))
```

### NodeTransformer
Этот класс позволяет изменять дерево `AST`.
Переопределяя методы, можно модифицировать узлы.
Методы, возвращающие новые узлы, заменяют существующие.

```python
class Transformer(ast.NodeTransformer):
   def visit_BinOp(self, node):
       if isinstance(node.op, ast.Add):
           node.op = ast.Sub()
       return node

code = "x = 1 + 2"
tree = ast.parse(code)
transformer = Transformer()
new_tree = transformer.visit(tree)

# Скомпилируем и выполним новый код
exec(compile(new_tree, filename="<ast>", mode="exec"))
print(x)  # 1 - 2, то есть -1
```

### Expression & Module
Узлы верхнего уровня. `ast.Module` — это представление программы или модуля, состоящего из списка операторов.
`ast.Expression` — выражение, которое можно выполнить и получить значение.

```python
tree = ast.parse("x = 5", mode="exec")  # Режим модуля
expr_tree = ast.parse("x + 2", mode="eval")  # Режим выражения
```

### literal_eval
Безопасная функция для вычисления литеральных выражений из строки или узла `AST`.
Поддерживает только простые типы, такие как строки, числа, списки и словари.

```python
print(ast.literal_eval("[1, 2, 3]"))  # [1, 2, 3]
```

# Важные узлы AST

- **`Module`**: Главный узел для кода, представляющий модуль.
- **`Expr`**: Узел для выражений.
- **`Assign`**: Операция присваивания.
- **`BinOp`**: Бинарные операции (например, `+`, `-`, `*`).
- **`FunctionDef`**: Определение функции.
- **`If`**: Оператор `if`.
- **`For`**: Цикл `for`.
- **`While`**: Цикл `while`.
- **`Call`**: Вызов функции.

### Пример сложного AST-дерева

Рассмотрим более сложный пример с условием и циклом.

```python
import ast

code = """
def foo(x):
    if x > 10:
        return x * 2
    else:
        return x + 2
"""

tree = ast.parse(code)
print(ast.dump(tree, indent=4))
"""
Module(
    body=[
        FunctionDef(
            name="foo",
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg="x")],
                kwonlyargs=[],
                kw_defaults=[],
                defaults=[]),
            body=[
                If(
                    test=Compare(
                        left=Name(id="x", ctx=Load()),
                        ops=[
                            Gt()],
                        comparators=[
                            Constant(value=10)]),
                    body=[
                        Return(
                            value=BinOp(
                                left=Name(id="x", ctx=Load()),
                                op=Mult(),
                                right=Constant(value=2)))],
                    orelse=[
                        Return(
                            value=BinOp(
                                left=Name(id="x", ctx=Load()),
                                op=Add(),
                                right=Constant(value=2)))])],
            decorator_list=[])],
    type_ignores=[])
"""
```

Вывод будет содержать структуру дерева, описывающую определение функции, условие `if` и возврат значений.

### Обработка и трансформация кода

`ast` позволяет писать программы, которые автоматически модифицируют Python-код.
Например, можно автоматически заменять одну операцию на другую, добавлять или изменять функции и так далее.

### Пример: замена оператора сложения на вычитание

```python
import ast

class SubtractTransformer(ast.NodeTransformer):
    def visit_BinOp(self, node):
        if isinstance(node.op, ast.Add):
            node.op = ast.Sub()
        return self.generic_visit(node)

code = "result = 1 + 2 + 3"
tree = ast.parse(code)
transformed_tree = SubtractTransformer().visit(tree)

# Компилируем и выполняем новый код
exec(compile(transformed_tree, filename="<ast>", mode="exec"))
print(result)  # -4 (1 - 2 - 3)
```
''',
                    "mypy": """
`mypy` — это статический анализатор типов для Python.
Он помогает разработчикам выявлять ошибки в типах на этапе компиляции, до выполнения программы.
Это полезно для больших проектов, где сложно отследить все возможные ошибки типов во время выполнения.
В отличие от стандартного динамического поведения Python, с помощью `mypy` можно явно аннотировать типы переменных,
аргументов функций и возвращаемых значений, чтобы повысить безопасность кода.

# Основные особенности и функции

### Аннотация типов
- `mypy` использует встроенную систему аннотаций типов в Python 3.5+.
- Аннотации типов добавляются с помощью синтаксиса Python для аргументов функций, возвращаемых значений и переменных.

### Поддержка стандартных типов
- `mypy` поддерживает типы из стандартной библиотеки `typing`: `List`, `Dict`, `Tuple`, `Union` и другие.

### Поддержка статической и динамической типизации
- Модели, не аннотированные типами, остаются динамическими.
- Можно комбинировать статическую и динамическую типизацию.

# Пример использования `mypy`

### Установка
Для установки `mypy` используйте команду:
```bash
pip install mypy
```

### Аннотация типов
Аннотации типов можно добавлять непосредственно в код:

```python
def greeting(name: str) -> str:
    return 'Hello ' + name
```

Здесь `name` — строка (`str`), и функция должна возвращать строку.
Если типы будут несоответствующими, `mypy` выдаст предупреждение.

### Проверка типов
Чтобы запустить проверку типов с помощью `mypy`, выполните команду:
```bash
mypy your_script.py
```

# Примеры аннотаций и их использования

### Аннотации для переменных
```python
x: int = 10
y: str = "Hello"
z: List[int] = [1, 2, 3]
```

### Аннотации для функций
```python
def add(a: int, b: int) -> int:
    return a + b

def process_data(data: List[str]) -> None:
    for item in data:
        print(item)
```

### Optional
```python
from typing import Optional

def get_user_name(user_id: int) -> Optional[str]:
    if user_id == 1:
        return "Alice"
    return None
```

### Union
```python
from typing import Union

def process(value: Union[int, str]) -> str:
    if isinstance(value, int):
        return f"Processing number {value}"
    return f"Processing string {value}"
```

### TypedDict
`TypedDict` позволяет аннотировать словари с заранее известными ключами.
```python
from typing import TypedDict

class Point(TypedDict):
    x: int
    y: int

def process_point(p: Point) -> None:
    print(p["x"], p["y"])

point = {"x": 10, "y": 20}
process_point(point)  # Успешно
```

### Mypy конфигурация

Mypy может быть настроен через файл конфигурации `mypy.ini` или `setup.cfg`

```ini
[mypy]
python_version = 3.9
ignore_missing_imports = True
disallow_untyped_calls = True
strict_optional = True
```

- `python_version` — указывает версию Python.
- `ignore_missing_imports` — игнорирует отсутствующие модули.
- `disallow_untyped_calls` — запрещает вызов неаннотированных функций.
- `strict_optional` — включает строгую проверку для `Optional`.

""",
                },
                "Algorithms": {
                    "bisect": r"""
Библиотека "bisect" в Python используется для выполнения бинарного поиска в отсортированных последовательностях.
Она предоставляет функции для нахождения места вставки элемента в отсортированный список и для выполнения деления списка на две части.

Методы библиотеки "bisect":
bisect_left(a, x): Возвращает наименьшую позицию для вставки элемента x в отсортированный список а, сохраняя его отсортированность.
bisect_right(a, x): Возвращает наибольшую позицию для вставки элемента x в отсортированный список а, сохраняя его отсортированность.
bisect(a, x): Эквивалентно вызову bisect_right(a, x).
insort_left(a, x): Вставляет элемент x в отсортированный список a на наименьшую позицию, сохраняя его отсортированность.
insort_right(a, x): Вставляет элемент x в отсортированный список a на наибольшую позицию, сохраняя его отсортированность.
insort(a, x): Эквивалентно вызову insort_right(a, x).


bisect_left(a, x) - возвращает индекс наименьшего элемента, который больше или равен x.

```python
import bisect
a = [1, 3, 5, 7]
x = 4
index = bisect.bisect_left(a, x)
print(index)  # 2
```

insort_right(a, x) - вставляет элемент x в отсортированный список a на наибольшую позицию, сохраняя его отсортированность.

```python
import bisect
a = [1, 3, 5, 7]
x = 4
bisect.insort_right(a, x)
print(a)  # [1, 3, 4, 5, 7]
```

bisect_right(a, x) - возвращает индекс первого элемента, который больше x.

```python
import bisect
a = [1, 3, 5, 7]
x = 4
index = bisect.bisect_right(a, x)
print(index)  # 3
```
""",
                    "hmac": r"""
Библиотека "hmac" в Python используется для создания и проверки кодов аутентификации HMAC (Hash-based Message Authentication Code).
HMAC обеспечивает целостность и аутентификацию сообщений, используя хеш-функции.

Таблица методов модуля "hmac" и их краткого описания:

| Метод                         | Описание                                                                             |
|-------------------------------|--------------------------------------------------------------------------------------|
| hmac.new(key, msg, digestmod) | Создает новый объект HMAC с заданным ключом, сообщением и используемой хеш-функцией. |
| hmac.digest()                 | Возвращает HMAC в виде строки байтов.                                                |
| hmac.hexdigest()              | Возвращает HMAC в виде шестнадцатеричной строки.                                     |
| hmac.compare_digest(a, b)     | Сравнивает два HMAC без утечек информации о значениях.                               |

   (Подмодулей в модуле "hmac" нет)

Список самых часто используемых методов, их краткое описание и

| Метод                         | Описание                                                                                | Пример кода                        |
|-------------------------------|-----------------------------------------------------------------------------------------|------------------------------------|
| hmac.new(key, msg, digestmod) | Создает новый HMAC объект с заданным ключом,<br>сообщением и используемой хеш-функцией. | hmac.new(key, msg, hashlib.sha256) |
| hmac.digest()                 | Возвращает HMAC в виде строки байтов.                                                   | hmac_object.digest()               |
| hmac.hexdigest()              | Возвращает HMAC в виде шестнадцатеричной строки.                                        | hmac_object.hexdigest()            |
| hmac.compare_digest(a, b)     | Сравнивает два HMAC и возвращает True, если они совпадают,<br>иначе возвращает False.   | hmac.compare_digest(hmac1, hmac2)  |
""",
                    "zlib": r"""
Библиотека "zlib" используется в Python для сжатия и распаковки данных с использованием алгоритма сжатия Deflate.

Методы модуля "zlib" и его подмодулей:

Модуль "zlib":
compress(data, level=-1): Сжимает данные с использованием алгоритма Deflate.
decompress(data, wbits=MAX_WBITS, bufsize=DEF_BUF_SIZE): Распаковывает сжатые данные.
crc32(data, value=0): Вычисляет контрольную сумму CRC-32 для данных.

Подмодуль "zlib.compressobj":
__init__(level=-1, method=DEFLATED, wbits=MAX_WBITS, memLevel=DEF_MEM_LEVEL, strategy=Z_DEFAULT_STRATEGY): Создает объект для сжатия данных.
compress(data): Сжимает данные и возвращает сжатый буфер.
flush(mode): Завершает сжатие и возвращает оставшийся сжатый буфер.

Подмодуль "zlib.decompressobj":
__init__(wbits=MAX_WBITS): Создает объект для распаковки данных.
decompress(data, max_length=0): Распаковывает данные и возвращает распакованный буфер.
flush(mode): Завершает распаковку и возвращает оставшийся распакованный буфер.

Самые часто используемые методы:

compress(data, level=-1): Сжимает данные с использованием алгоритма Deflate.

```python
import zlib
compressed_data = zlib.compress(b"Hello, world!")
```

decompress(data, wbits=MAX_WBITS, bufsize=DEF_BUF_SIZE): Распаковывает сжатые данные.

```python
import zlib
decompressed_data = zlib.decompress(compressed_data)
```

crc32(data, value=0): Вычисляет контрольную сумму CRC-32 для данных.
```python
import zlib
checksum = zlib.crc32(b"Hello, world!")
```

Пожалуйста, обратите внимание, что код предоставлен только для демонстрации работы методов и может потребоваться
дополнительная обработка данных в реальных сценариях использования.
""",
                    "lzma": r"""
Библиотека "lzma" в Python используется для сжатия и распаковки данных
с использованием алгоритма сжатия LZMA (Lempel-Ziv-Markov chain Algorithm).

Методы модуля "lzma" и его подмодулей:

`lzma.compress(data, format=lzma.FORMAT_XZ, check=-1)`: Сжимает данные, используя алгоритм сжатия LZMA.
`lzma.decompress(data, format=lzma.FORMAT_XZ, memlimit=None, filters=None)`: Распаковывает сжатые данные, сжатые с использованием алгоритма LZMA.
`lzma.LZMACompressor(format=lzma.FORMAT_XZ, check=-1, preset=None, filters=None)`: Создает объект компрессора LZMA для сжатия данных.
`lzma.LZMADecompressor(format=lzma.FORMAT_XZ, memlimit=None, filters=None)`: Создает объект декомпрессора LZMA для распаковки сжатых данных.
`lzma.is_check_supported(check)`: Проверяет, поддерживается ли заданный тип проверки сжатия.
`lzma.CHECK_NONE`: Константа, представляющая отсутствие проверки сжатия.
`lzma.CHECK_CRC32`: Константа, представляющая проверку сжатия с использованием алгоритма CRC32.
`lzma.CHECK_CRC64`: Константа, представляющая проверку сжатия с использованием алгоритма CRC64.
`lzma.CHECK_SHA256`: Константа, представляющая проверку сжатия с использованием алгоритма SHA-256.

`lzma.compress(data)`: Сжимает данные, используя алгоритм сжатия LZMA.

```python
import lzma

data = b"Hello, World!"
compressed_data = lzma.compress(data)
```

`lzma.decompress(data)`: Распаковывает сжатые данные, сжатые с использованием алгоритма LZMA.

```python
import lzma

compressed_data = b"\xfd7zXZ\x00\x00\x04\xe6\xd6\xb4\x46\x02\x00!\x01\x16\x00\x00\x00t/\xe5\xfd\x01\x00\x00\x00\xff\xff"
decompressed_data = lzma.decompress(compressed_data)
```

Обратите внимание, что эти примеры демонстрируют базовое использование методов
и не учитывают параметры настройки, такие как формат сжатия и проверка сжатия.
""",
                    "table2string": """
[https://github.com/EgorKhabarov/table2string](https://github.com/EgorKhabarov/table2string)

# table2string

[![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/EgorKhabarov/table2string/tests.yml?style=flat&logo=GitHub&label=Tests)](https://github.com/EgorKhabarov/table2string/actions/workflows/tests.yml) [![Publish Python Package to PyPI](https://img.shields.io/github/actions/workflow/status/EgorKhabarov/table2string/publish.yml?style=flat&logo=GitHub&label=Publish%20to%20PyPI)](https://github.com/EgorKhabarov/table2string/actions/workflows/publish.yml)

[![PyPi Package Version](https://img.shields.io/pypi/v/table2string.svg?style=flat&logo=pypi)](https://pypi.python.org/pypi/table2string) [![Supported Python versions](https://img.shields.io/pypi/pyversions/table2string.svg?style=flat&logo=pypi)](https://pypi.python.org/pypi/table2string) [![PyPi status](https://img.shields.io/pypi/status/table2string.svg?style=flat&logo=pypi)](https://pypi.python.org/pypi/table2string) [![PyPi downloads](https://img.shields.io/pypi/dm/table2string.svg?style=flat&logo=pypi)](https://pypi.org/project/table2string/)

## Convert table to string

While there are several libraries available for converting tables to strings in Python, none seemed to meet my specific requirements. 

- **Line Break Support:** Easily include line breaks within cells for enhanced readability.
- **Emoji Integration:** Effortlessly incorporate emoji characters into your tables to add visual appeal and context.

---

# Install

## PyPI

```shell
pip install -U table2string
```

## GitHub

```shell
pip install -U git+https://github.com/EgorKhabarov/table2string.git@master
```

---

# Usage example

```pycon
>>> from table2string import Table
>>> Table([("1", "2", "3"), ("qwe", "rty\\nuio", "")], name="Table Name").print()
+---------------+
|  Table Name   |
+-----+-----+---+
|   1 |   2 | 3 |
+-----+-----+---+
| qwe | rty |   |
|     | uio |   |
+-----+-----+---+
>>> from io import StringIO
>>> Table.from_csv(StringIO('c1,c2,c3\\n1,2,3\\nqwe,"rty\\nuio",'), name="Table Name").print()
+----------------+
|   Table Name   |
+-----+-----+----+
| c1  | c2  | c3 |
+-----+-----+----+
|   1 |   2 |  3 |
+-----+-----+----+
| qwe | rty |    |
|     | uio |    |
+-----+-----+----+
>>> Table.from_csv(StringIO('c1,c2,c3\\n1,2,3\\nqwe,"rty\\nuio",'), name="Table Name", column_names=False).print()
+---------------+
|  Table Name   |
+-----+-----+---+
|   1 |   2 | 3 |
+-----+-----+---+
| qwe | rty |   |
|     | uio |   |
+-----+-----+---+
>>> import sqlite3
>>> cursor = sqlite3.connect(":memory:").cursor().execute(
...     "CREATE TABLE data (c1 TEXT, c2 TEXT, c3 TEXT);"
... ).executemany(
...     "INSERT INTO data (c1, c2, c3) VALUES (?, ?, ?);",
...     [("1", "2", "3"), ("qwe", "rty\\nuio", "")],
... ).execute(
...     "SELECT c1, c2, c3 FROM data;"
... )
>>> Table.from_db_cursor(cursor, name="Table Name").print()
+---------------+
|  Table Name   |
+-----+-----+---+
|   1 |   2 | 3 |
+-----+-----+---+
| qwe | rty |   |
|     | uio |   |
+-----+-----+---+
>>> Table.from_db_cursor(
...     cursor.execute("SELECT c1, c2, c3 FROM data;"),
...     name="Table Name",
...     column_names=True,
... ).print()
+----------------+
|   Table Name   |
+-----+-----+----+
| c1  | c2  | c3 |
+-----+-----+----+
|   1 |   2 |  3 |
+-----+-----+----+
| qwe | rty |    |
|     | uio |    |
+-----+-----+----+
>>> from table2string import print_table, stringify_table
>>> print_table([("1", "2", "3"), ("qwe", "rty\\nuio", "")], name="Table Name")
+---------------+
|  Table Name   |
+-----+-----+---+
|   1 |   2 | 3 |
+-----+-----+---+
| qwe | rty |   |
|     | uio |   |
+-----+-----+---+
>>> print(stringify_table([("1", "2", "3"), ("qwe", "rty\\nuio", "")], name="Table Name"))
+---------------+
|  Table Name   |
+-----+-----+---+
|   1 |   2 | 3 |
+-----+-----+---+
| qwe | rty |   |
|     | uio |   |
+-----+-----+---+

```

## Custom width and height settings

| Width                               | Example        | Description                                                                                                                    |
|-------------------------------------|----------------|--------------------------------------------------------------------------------------------------------------------------------|
| `<width>`                           | `10`           | Setting `width` (`10`) for the whole table                                                                                     |
| `(<width>,)`                        | `(10,)`        | Setting `width_1` (`10`) for all column                                                                                        |
| `(<width_1>, <width_2>)`            | `(10, 20)`     | Setting `width_1` (`10`) for the first column and `width_2` (`20`)<br>for all other columns                                    |
| `(<width_1>, <width_2>, <width_3>)` | `(10, 20, 30)` | Setting `width_1` (`10`) for the first column and `width_2` (`20`)<br>for the second and `width_3` (`30`) for the third column |

<details>
<summary>Example</summary>

```pycon
>>> # Width of the entire table with borders
>>> print_table([(1,), (2.345,), ("example",)], max_width=10)
+--------+
|      1 |
+--------+
|  2.345 |
+--------+
| exampl↩|
| e      |
+--------+
>>> # Width of each column individually
>>> print_table([(1,), (2.345,), ("example",)], max_width=(10,))
+------------+
|          1 |
+------------+
|      2.345 |
+------------+
| example    |
+------------+
>>> print_table([("123456\\n\\n789000", "example")], max_width=(3, 4), max_height=4)
+-----+------+
| 123↩| exam↩|
| 456 | ple  |
|     |      |
| 789…|      |
+-----+------+
>>> print_table([("123456789",)], max_width=(1,), max_height=1)
+---+
| 1…|
+---+
>>> print_table(
...     table=[("123\\n456\\n789",)],
...     max_width=(3,),
...     max_height=4,
...     maximize_height=True,
... )
+-----+
| 123 |
| 456 |
| 789 |
|     |
+-----+
>>> print_table(
...     table=[("123456789",)],
...     max_width=(3,),
...     max_height=4,
...     maximize_height=True,
... )
+-----+
| 123↩|
| 456↩|
| 789 |
|     |
+-----+

```
</details>

## Text alignment

| Align                                     | Example           | Description                                                                                                                       |
|-------------------------------------------|-------------------|-----------------------------------------------------------------------------------------------------------------------------------|
| `"<align>"` or `("<align>",)`             | `"^"` or `("^",)` | Setting `align` (`"^"`) for all columns                                                                                           |
| `("<align_1>", "<align_2>")`              | `("^", "<")`      | Setting `align_1` (`"^"`) for the first column and `align_2` (`"<"`)<br>for all other columns                                     |
| `("<align_1>", "<align_2>", "<align_3>")` | `("^", "<", ">")` | Setting `align_1` (`"^"`) for the first column and `align_2` (`"<"`)<br>for the second and `align_3` (`">"`) for the third column |

### ALLOWED_ALIGNS

|    Align    | Description                                                                                                                                             |
|:-----------:|---------------------------------------------------------------------------------------------------------------------------------------------------------|
| `*` or `**` | Alignment depends on the type. If this is a number and there are no line breaks in this cell,<br>then align to the right; otherwise, align to the left. |
| `<` or `<<` | All lines are left aligned                                                                                                                              |
| `^` or `^^` | All lines are center aligned                                                                                                                            |
| `>` or `>>` | All lines are right aligned                                                                                                                             |
|    `<^`     | The first line is left aligned and the remaining lines are centered                                                                                     |
|    `<>`     | The first line is left aligned and the remaining lines are right aligned                                                                                |
|    `^<`     | The first line is aligned to the center, and the remaining lines are aligned to the left of the first line.                                             |
|    `^>`     | The first line is aligned to the center, and the remaining lines are aligned to the right of the first line.                                            |
|    `><`     | The first line is right aligned and the remaining lines are left aligned                                                                                |
|    `>^`     | The first line is right aligned and the remaining lines are centered                                                                                    |

<details>
<summary>Example</summary>

```pycon
>>> kwargs_1 = {
...     "table": [("1", "123456789\\nqwerty\\nasdfghjklzxcvb")],
...     "name": "Table Name\\nName\\nNaaaaame",
...     "column_names": ("1", "col 2\\nc2"),
...     "max_width": (5, 15),
... }
>>> print_table(**kwargs_1)
+-------------------------+
|       Table Name        |
|          Name           |
|        Naaaaame         |
+-------+-----------------+
|   1   |      col 2      |
|       |       c2        |
+-------+-----------------+
|     1 | 123456789       |
|       | qwerty          |
|       | asdfghjklzxcvb  |
+-------+-----------------+
>>> print_table(**kwargs_1, align="*", name_align="*", column_names_align="*")  # align="**", name_align="**", column_names_align="**"
+-------------------------+
| Table Name              |
| Name                    |
| Naaaaame                |
+-------+-----------------+
|     1 | col 2           |
|       | c2              |
+-------+-----------------+
|     1 | 123456789       |
|       | qwerty          |
|       | asdfghjklzxcvb  |
+-------+-----------------+
>>> print_table(**kwargs_1, align="<", name_align="<", column_names_align="<")  # align="<<", name_align="<<", column_names_align="<<"
+-------------------------+
| Table Name              |
| Name                    |
| Naaaaame                |
+-------+-----------------+
| 1     | col 2           |
|       | c2              |
+-------+-----------------+
| 1     | 123456789       |
|       | qwerty          |
|       | asdfghjklzxcvb  |
+-------+-----------------+
>>> print_table(**kwargs_1, align=">", name_align=">", column_names_align=">")  # align=">>", name_align=">>", column_names_align=">>"
+-------------------------+
|              Table Name |
|                    Name |
|                Naaaaame |
+-------+-----------------+
|     1 |           col 2 |
|       |              c2 |
+-------+-----------------+
|     1 |       123456789 |
|       |          qwerty |
|       |  asdfghjklzxcvb |
+-------+-----------------+
>>> print_table(**kwargs_1, align="^", name_align="^", column_names_align="^")  # align="^^", name_align="^^", column_names_align="^^"
+-------------------------+
|       Table Name        |
|          Name           |
|        Naaaaame         |
+-------+-----------------+
|   1   |      col 2      |
|       |       c2        |
+-------+-----------------+
|   1   |    123456789    |
|       |     qwerty      |
|       | asdfghjklzxcvb  |
+-------+-----------------+
>>> print_table(**kwargs_1, align="^<", name_align="^<", column_names_align="^<")
+-------------------------+
|       Table Name        |
|       Name              |
|       Naaaaame          |
+-------+-----------------+
|   1   |      col 2      |
|       |      c2         |
+-------+-----------------+
|   1   | 123456789       |
|       | qwerty          |
|       | asdfghjklzxcvb  |
+-------+-----------------+
>>> print_table(**kwargs_1, align="^>", name_align="^>", column_names_align="^>")
+-------------------------+
|       Table Name        |
|             Name        |
|         Naaaaame        |
+-------+-----------------+
|   1   |      col 2      |
|       |         c2      |
+-------+-----------------+
|   1   |      123456789  |
|       |         qwerty  |
|       | asdfghjklzxcvb  |
+-------+-----------------+
>>> print_table([("qwerty\\n123456789\\nasdfghjklzxcvb",)], max_width=(18,), align="^<")
+--------------------+
|   qwerty           |
|   123456789        |
|   asdfghjklzxcvb   |
+--------------------+
>>> print_table([("qwerty\\n123456789\\nasdfghjklzxcvb",)], max_width=(18,), align="^>")
+--------------------+
|           qwerty   |
|        123456789   |
|   asdfghjklzxcvb   |
+--------------------+

```
</details>

## Separator settings

| Separator              | Description                                |
|------------------------|--------------------------------------------|
| `sep=True`             | All horizontal dividers included           |
| `sep=False`            | All horizontal dividers are disabled       |
| `sep=(1,)`             | Only first delimiter                       |
| `sep=(1, 3, 5)`        | Only first third and fifth separator       |
| `sep=range(1, 100, 5)` | Delimiter every five lines first 100 lines |

<details>
<summary>Example</summary>

```pycon
>>> table_1 = [("qwe", "rty\\nuio"), ("123456\\n\\n789000", "example")]
>>> kwargs = {
...     "max_width": (3, 4),
...     "max_height": 4,
... }
>>> print_table(table_1, **kwargs, sep=True)
+-----+------+
| qwe | rty  |
|     | uio  |
+-----+------+
| 123↩| exam↩|
| 456 | ple  |
|     |      |
| 789…|      |
+-----+------+
>>> print_table(table_1, **kwargs, sep=False)
+-----+------+
| qwe | rty  |
|     | uio  |
| 123↩| exam↩|
| 456 | ple  |
|     |      |
| 789…|      |
+-----+------+
>>> table_2 = [("1", "2"), ("3", "4")]
>>> print_table(table_2, sep=True, name="Name")
+-------+
| Name  |
+---+---+
| 1 | 2 |
+---+---+
| 3 | 4 |
+---+---+
>>> print_table(table_2, sep=False, name="Name")
+-------+
| Name  |
+---+---+
| 1 | 2 |
| 3 | 4 |
+---+---+
>>> table_3 = [("1", "2"), ("3", "4"), ("5", "6"), ("7", "8")]
>>> print_table(table_3, sep=(1,))
+---+---+
| 1 | 2 |
+---+---+
| 3 | 4 |
| 5 | 6 |
| 7 | 8 |
+---+---+
>>> print_table(table_3, sep=(2,))
+---+---+
| 1 | 2 |
| 3 | 4 |
+---+---+
| 5 | 6 |
| 7 | 8 |
+---+---+
>>> print_table(table_3, sep=(1, 3))
+---+---+
| 1 | 2 |
+---+---+
| 3 | 4 |
| 5 | 6 |
+---+---+
| 7 | 8 |
+---+---+
>>> print_table(table_3, sep=(1,), name="Name")
+-------+
| Name  |
+---+---+
| 1 | 2 |
+---+---+
| 3 | 4 |
| 5 | 6 |
| 7 | 8 |
+---+---+
>>> print_table(table_3, sep=(2,), name="Name")
+-------+
| Name  |
+---+---+
| 1 | 2 |
| 3 | 4 |
+---+---+
| 5 | 6 |
| 7 | 8 |
+---+---+
>>> print_table(table_3, sep=(1, 3), name="Name")
+-------+
| Name  |
+---+---+
| 1 | 2 |
+---+---+
| 3 | 4 |
| 5 | 6 |
+---+---+
| 7 | 8 |
+---+---+

```
</details>

## Borders

<details>
<summary>Border types</summary>

```text
┌──────────────┬───────────────────┐
│  ascii_thin  │ ascii_thin_double │
│  +---+---+   │     +---+---+     │
│  |   |   |   │     |   |   |     │
│  +---+---+   │     +===+===+     │
│  |   |   |   │     |   |   |     │
│  +---+---+   │     +---+---+     │
│  |   |   |   │     |   |   |     │
│  +---+---+   │     +---+---+     │
├──────────────┼───────────────────┤
│ ascii_double │ ascii_double_thin │
│  +===+===+   │     +===+===+     │
│  ‖   ‖   ‖   │     ‖   ‖   ‖     │
│  +===+===+   │     +---+---+     │
│  ‖   ‖   ‖   │     ‖   ‖   ‖     │
│  +===+===+   │     +===+===+     │
│  ‖   ‖   ‖   │     ‖   ‖   ‖     │
│  +===+===+   │     +===+===+     │
├──────────────┼───────────────────┤
│     thin     │    thin_thick     │
│  ┌───┬───┐   │     ┌───┬───┐     │
│  │   │   │   │     │   │   │     │
│  ├───┼───┤   │     ┝━━━┿━━━┥     │
│  │   │   │   │     │   │   │     │
│  ├───┼───┤   │     ├───┼───┤     │
│  │   │   │   │     │   │   │     │
│  └───┴───┘   │     └───┴───┘     │
├──────────────┼───────────────────┤
│ thin_double  │  rounded_double   │
│  ┌───┬───┐   │     ╭───┬───╮     │
│  │   │   │   │     │   │   │     │
│  ╞═══╪═══╡   │     ╞═══╪═══╡     │
│  │   │   │   │     │   │   │     │
│  ├───┼───┤   │     ├───┼───┤     │
│  │   │   │   │     │   │   │     │
│  └───┴───┘   │     ╰───┴───╯     │
├──────────────┼───────────────────┤
│   rounded    │   rounded_thick   │
│  ╭───┬───╮   │     ╭───┬───╮     │
│  │   │   │   │     │   │   │     │
│  ├───┼───┤   │     ┝━━━┿━━━┥     │
│  │   │   │   │     │   │   │     │
│  ├───┼───┤   │     ├───┼───┤     │
│  │   │   │   │     │   │   │     │
│  ╰───┴───╯   │     ╰───┴───╯     │
├──────────────┼───────────────────┤
│    thick     │    thick_thin     │
│  ┏━━━┳━━━┓   │     ┌───┬───┐     │
│  ┃   ┃   ┃   │     │   │   │     │
│  ┣━━━╋━━━┫   │     ┠━━━╂━━━┨     │
│  ┃   ┃   ┃   │     │   │   │     │
│  ┣━━━╋━━━┫   │     ├───┼───┤     │
│  ┃   ┃   ┃   │     │   │   │     │
│  ┗━━━┻━━━┛   │     └───┴───┘     │
├──────────────┼───────────────────┤
│    double    │    double_thin    │
│  ╔═══╦═══╗   │     ╔═══╦═══╗     │
│  ║   ║   ║   │     ║   ║   ║     │
│  ╠═══╬═══╣   │     ╟───╫───╢     │
│  ║   ║   ║   │     ║   ║   ║     │
│  ╠═══╬═══╣   │     ╠═══╬═══╣     │
│  ║   ║   ║   │     ║   ║   ║     │
│  ╚═══╩═══╝   │     ╚═══╩═══╝     │
├──────────────┼───────────────────┤
│   booktabs   │  ascii_booktabs   │
│   ───────    │      -------      │
│              │                   │
│   ━━━━━━━    │      =======      │
│              │                   │
│   ───────    │      -------      │
│              │                   │
│   ───────    │      -------      │
├──────────────┼───────────────────┤
│   markdown   │                   │
│  |   |   |   │                   │
│  |---|---|   │                   │
│  |   |   |   │                   │
│  |   |   |   │                   │
└──────────────┴───────────────────┘
```
</details>

<details>
<summary>Example</summary>

```pycon
>>> from table2string import Table, Themes
>>> name = "Table Name"
>>> column_names = ("c1", "c2", "3")
>>> table = [("1", "2", "3"), ("qwe", "rty\\nuio", "")]
>>> t = Table(table)
>>> t_name = Table(table, name=name)
>>> t_column_names = Table(table, column_names=column_names)
>>> t_name_column_names = Table(table, name=name, column_names=column_names)

```

<details>
<summary>Themes.ascii_thin</summary>

```pycon

>>> t.print(theme=Themes.ascii_thin)
+-----+-----+---+
|   1 |   2 | 3 |
+-----+-----+---+
| qwe | rty |   |
|     | uio |   |
+-----+-----+---+
>>> t_column_names.print(theme=Themes.ascii_thin)
+-----+-----+---+
| c1  | c2  | 3 |
+-----+-----+---+
|   1 |   2 | 3 |
+-----+-----+---+
| qwe | rty |   |
|     | uio |   |
+-----+-----+---+
>>> t_name.print(theme=Themes.ascii_thin)
+---------------+
|  Table Name   |
+-----+-----+---+
|   1 |   2 | 3 |
+-----+-----+---+
| qwe | rty |   |
|     | uio |   |
+-----+-----+---+
>>> t_name_column_names.print(theme=Themes.ascii_thin)
+---------------+
|  Table Name   |
+-----+-----+---+
| c1  | c2  | 3 |
+-----+-----+---+
|   1 |   2 | 3 |
+-----+-----+---+
| qwe | rty |   |
|     | uio |   |
+-----+-----+---+

```
</details>


<details>
<summary>Themes.ascii_thin_double</summary>

```pycon
>>> t.print(theme=Themes.ascii_thin_double)
+-----+-----+---+
|   1 |   2 | 3 |
+=====+=====+===+
| qwe | rty |   |
|     | uio |   |
+-----+-----+---+
>>> t_column_names.print(theme=Themes.ascii_thin_double)
+-----+-----+---+
| c1  | c2  | 3 |
+=====+=====+===+
|   1 |   2 | 3 |
+-----+-----+---+
| qwe | rty |   |
|     | uio |   |
+-----+-----+---+
>>> t_name.print(theme=Themes.ascii_thin_double)
+---------------+
|  Table Name   |
+-----+-----+---+
|   1 |   2 | 3 |
+=====+=====+===+
| qwe | rty |   |
|     | uio |   |
+-----+-----+---+
>>> t_name_column_names.print(theme=Themes.ascii_thin_double)
+---------------+
|  Table Name   |
+-----+-----+---+
| c1  | c2  | 3 |
+=====+=====+===+
|   1 |   2 | 3 |
+-----+-----+---+
| qwe | rty |   |
|     | uio |   |
+-----+-----+---+

```
</details>


<details>
<summary>Themes.ascii_double</summary>

```pycon
>>> t.print(theme=Themes.ascii_double)
+=====+=====+===+
‖   1 ‖   2 ‖ 3 ‖
+=====+=====+===+
‖ qwe ‖ rty ‖   ‖
‖     ‖ uio ‖   ‖
+=====+=====+===+
>>> t_column_names.print(theme=Themes.ascii_double)
+=====+=====+===+
‖ c1  ‖ c2  ‖ 3 ‖
+=====+=====+===+
‖   1 ‖   2 ‖ 3 ‖
+=====+=====+===+
‖ qwe ‖ rty ‖   ‖
‖     ‖ uio ‖   ‖
+=====+=====+===+
>>> t_name.print(theme=Themes.ascii_double)
+===============+
‖  Table Name   ‖
+=====+=====+===+
‖   1 ‖   2 ‖ 3 ‖
+=====+=====+===+
‖ qwe ‖ rty ‖   ‖
‖     ‖ uio ‖   ‖
+=====+=====+===+
>>> t_name_column_names.print(theme=Themes.ascii_double)
+===============+
‖  Table Name   ‖
+=====+=====+===+
‖ c1  ‖ c2  ‖ 3 ‖
+=====+=====+===+
‖   1 ‖   2 ‖ 3 ‖
+=====+=====+===+
‖ qwe ‖ rty ‖   ‖
‖     ‖ uio ‖   ‖
+=====+=====+===+

```
</details>


<details>
<summary>Themes.ascii_double_thin</summary>

```pycon
>>> t.print(theme=Themes.ascii_double_thin)
+=====+=====+===+
‖   1 ‖   2 ‖ 3 ‖
+-----+-----+---+
‖ qwe ‖ rty ‖   ‖
‖     ‖ uio ‖   ‖
+=====+=====+===+
>>> t_column_names.print(theme=Themes.ascii_double_thin)
+=====+=====+===+
‖ c1  ‖ c2  ‖ 3 ‖
+-----+-----+---+
‖   1 ‖   2 ‖ 3 ‖
+=====+=====+===+
‖ qwe ‖ rty ‖   ‖
‖     ‖ uio ‖   ‖
+=====+=====+===+
>>> t_name.print(theme=Themes.ascii_double_thin)
+===============+
‖  Table Name   ‖
+=====+=====+===+
‖   1 ‖   2 ‖ 3 ‖
+-----+-----+---+
‖ qwe ‖ rty ‖   ‖
‖     ‖ uio ‖   ‖
+=====+=====+===+
>>> t_name_column_names.print(theme=Themes.ascii_double_thin)
+===============+
‖  Table Name   ‖
+=====+=====+===+
‖ c1  ‖ c2  ‖ 3 ‖
+-----+-----+---+
‖   1 ‖   2 ‖ 3 ‖
+=====+=====+===+
‖ qwe ‖ rty ‖   ‖
‖     ‖ uio ‖   ‖
+=====+=====+===+

```
</details>


<details>
<summary>Themes.ascii_booktabs</summary>

```pycon
>>> t.print(theme=Themes.ascii_booktabs)
 --------------- 
    1     2   3  
 =============== 
  qwe   rty      
        uio      
 --------------- 
>>> t_column_names.print(theme=Themes.ascii_booktabs)
 --------------- 
  c1    c2    3  
 =============== 
    1     2   3  
 --------------- 
  qwe   rty      
        uio      
 --------------- 
>>> t_name.print(theme=Themes.ascii_booktabs)
 --------------- 
   Table Name    
 --------------- 
    1     2   3  
 =============== 
  qwe   rty      
        uio      
 --------------- 
>>> t_name_column_names.print(theme=Themes.ascii_booktabs)
 --------------- 
   Table Name    
 --------------- 
  c1    c2    3  
 =============== 
    1     2   3  
 --------------- 
  qwe   rty      
        uio      
 --------------- 

```
</details>


<details>
<summary>Themes.thin</summary>

```pycon
>>> t.print(theme=Themes.thin)
┌─────┬─────┬───┐
│   1 │   2 │ 3 │
├─────┼─────┼───┤
│ qwe │ rty │   │
│     │ uio │   │
└─────┴─────┴───┘
>>> t_column_names.print(theme=Themes.thin)
┌─────┬─────┬───┐
│ c1  │ c2  │ 3 │
├─────┼─────┼───┤
│   1 │   2 │ 3 │
├─────┼─────┼───┤
│ qwe │ rty │   │
│     │ uio │   │
└─────┴─────┴───┘
>>> t_name.print(theme=Themes.thin)
┌───────────────┐
│  Table Name   │
├─────┬─────┬───┤
│   1 │   2 │ 3 │
├─────┼─────┼───┤
│ qwe │ rty │   │
│     │ uio │   │
└─────┴─────┴───┘
>>> t_name_column_names.print(theme=Themes.thin)
┌───────────────┐
│  Table Name   │
├─────┬─────┬───┤
│ c1  │ c2  │ 3 │
├─────┼─────┼───┤
│   1 │   2 │ 3 │
├─────┼─────┼───┤
│ qwe │ rty │   │
│     │ uio │   │
└─────┴─────┴───┘

```
</details>


<details>
<summary>Themes.thin_thick</summary>

```pycon
>>> t.print(theme=Themes.thin_thick)
┌─────┬─────┬───┐
│   1 │   2 │ 3 │
┝━━━━━┿━━━━━┿━━━┥
│ qwe │ rty │   │
│     │ uio │   │
└─────┴─────┴───┘
>>> t_column_names.print(theme=Themes.thin_thick)
┌─────┬─────┬───┐
│ c1  │ c2  │ 3 │
┝━━━━━┿━━━━━┿━━━┥
│   1 │   2 │ 3 │
├─────┼─────┼───┤
│ qwe │ rty │   │
│     │ uio │   │
└─────┴─────┴───┘
>>> t_name.print(theme=Themes.thin_thick)
┌───────────────┐
│  Table Name   │
├─────┬─────┬───┤
│   1 │   2 │ 3 │
┝━━━━━┿━━━━━┿━━━┥
│ qwe │ rty │   │
│     │ uio │   │
└─────┴─────┴───┘
>>> t_name_column_names.print(theme=Themes.thin_thick)
┌───────────────┐
│  Table Name   │
├─────┬─────┬───┤
│ c1  │ c2  │ 3 │
┝━━━━━┿━━━━━┿━━━┥
│   1 │   2 │ 3 │
├─────┼─────┼───┤
│ qwe │ rty │   │
│     │ uio │   │
└─────┴─────┴───┘

```
</details>


<details>
<summary>Themes.thin_double</summary>

```pycon
>>> t.print(theme=Themes.thin_double)
┌─────┬─────┬───┐
│   1 │   2 │ 3 │
╞═════╪═════╪═══╡
│ qwe │ rty │   │
│     │ uio │   │
└─────┴─────┴───┘
>>> t_column_names.print(theme=Themes.thin_double)
┌─────┬─────┬───┐
│ c1  │ c2  │ 3 │
╞═════╪═════╪═══╡
│   1 │   2 │ 3 │
├─────┼─────┼───┤
│ qwe │ rty │   │
│     │ uio │   │
└─────┴─────┴───┘
>>> t_name.print(theme=Themes.thin_double)
┌───────────────┐
│  Table Name   │
├─────┬─────┬───┤
│   1 │   2 │ 3 │
╞═════╪═════╪═══╡
│ qwe │ rty │   │
│     │ uio │   │
└─────┴─────┴───┘
>>> t_name_column_names.print(theme=Themes.thin_double)
┌───────────────┐
│  Table Name   │
├─────┬─────┬───┤
│ c1  │ c2  │ 3 │
╞═════╪═════╪═══╡
│   1 │   2 │ 3 │
├─────┼─────┼───┤
│ qwe │ rty │   │
│     │ uio │   │
└─────┴─────┴───┘

```
</details>


<details>
<summary>Themes.rounded</summary>

```pycon
>>> t.print(theme=Themes.rounded)
╭─────┬─────┬───╮
│   1 │   2 │ 3 │
├─────┼─────┼───┤
│ qwe │ rty │   │
│     │ uio │   │
╰─────┴─────┴───╯
>>> t_column_names.print(theme=Themes.rounded)
╭─────┬─────┬───╮
│ c1  │ c2  │ 3 │
├─────┼─────┼───┤
│   1 │   2 │ 3 │
├─────┼─────┼───┤
│ qwe │ rty │   │
│     │ uio │   │
╰─────┴─────┴───╯
>>> t_name.print(theme=Themes.rounded)
╭───────────────╮
│  Table Name   │
├─────┬─────┬───┤
│   1 │   2 │ 3 │
├─────┼─────┼───┤
│ qwe │ rty │   │
│     │ uio │   │
╰─────┴─────┴───╯
>>> t_name_column_names.print(theme=Themes.rounded)
╭───────────────╮
│  Table Name   │
├─────┬─────┬───┤
│ c1  │ c2  │ 3 │
├─────┼─────┼───┤
│   1 │   2 │ 3 │
├─────┼─────┼───┤
│ qwe │ rty │   │
│     │ uio │   │
╰─────┴─────┴───╯

```
</details>


<details>
<summary>Themes.rounded_thick</summary>

```pycon
>>> t.print(theme=Themes.rounded_thick)
╭─────┬─────┬───╮
│   1 │   2 │ 3 │
┝━━━━━┿━━━━━┿━━━┥
│ qwe │ rty │   │
│     │ uio │   │
╰─────┴─────┴───╯
>>> t_column_names.print(theme=Themes.rounded_thick)
╭─────┬─────┬───╮
│ c1  │ c2  │ 3 │
┝━━━━━┿━━━━━┿━━━┥
│   1 │   2 │ 3 │
├─────┼─────┼───┤
│ qwe │ rty │   │
│     │ uio │   │
╰─────┴─────┴───╯
>>> t_name.print(theme=Themes.rounded_thick)
╭───────────────╮
│  Table Name   │
├─────┬─────┬───┤
│   1 │   2 │ 3 │
┝━━━━━┿━━━━━┿━━━┥
│ qwe │ rty │   │
│     │ uio │   │
╰─────┴─────┴───╯
>>> t_name_column_names.print(theme=Themes.rounded_thick)
╭───────────────╮
│  Table Name   │
├─────┬─────┬───┤
│ c1  │ c2  │ 3 │
┝━━━━━┿━━━━━┿━━━┥
│   1 │   2 │ 3 │
├─────┼─────┼───┤
│ qwe │ rty │   │
│     │ uio │   │
╰─────┴─────┴───╯

```
</details>


<details>
<summary>Themes.rounded_double</summary>

```pycon
>>> t.print(theme=Themes.rounded_double)
╭─────┬─────┬───╮
│   1 │   2 │ 3 │
╞═════╪═════╪═══╡
│ qwe │ rty │   │
│     │ uio │   │
╰─────┴─────┴───╯
>>> t_column_names.print(theme=Themes.rounded_double)
╭─────┬─────┬───╮
│ c1  │ c2  │ 3 │
╞═════╪═════╪═══╡
│   1 │   2 │ 3 │
├─────┼─────┼───┤
│ qwe │ rty │   │
│     │ uio │   │
╰─────┴─────┴───╯
>>> t_name.print(theme=Themes.rounded_double)
╭───────────────╮
│  Table Name   │
├─────┬─────┬───┤
│   1 │   2 │ 3 │
╞═════╪═════╪═══╡
│ qwe │ rty │   │
│     │ uio │   │
╰─────┴─────┴───╯
>>> t_name_column_names.print(theme=Themes.rounded_double)
╭───────────────╮
│  Table Name   │
├─────┬─────┬───┤
│ c1  │ c2  │ 3 │
╞═════╪═════╪═══╡
│   1 │   2 │ 3 │
├─────┼─────┼───┤
│ qwe │ rty │   │
│     │ uio │   │
╰─────┴─────┴───╯

```
</details>


<details>
<summary>Themes.thick</summary>

```pycon
>>> t.print(theme=Themes.thick)
┏━━━━━┳━━━━━┳━━━┓
┃   1 ┃   2 ┃ 3 ┃
┣━━━━━╋━━━━━╋━━━┫
┃ qwe ┃ rty ┃   ┃
┃     ┃ uio ┃   ┃
┗━━━━━┻━━━━━┻━━━┛
>>> t_column_names.print(theme=Themes.thick)
┏━━━━━┳━━━━━┳━━━┓
┃ c1  ┃ c2  ┃ 3 ┃
┣━━━━━╋━━━━━╋━━━┫
┃   1 ┃   2 ┃ 3 ┃
┣━━━━━╋━━━━━╋━━━┫
┃ qwe ┃ rty ┃   ┃
┃     ┃ uio ┃   ┃
┗━━━━━┻━━━━━┻━━━┛
>>> t_name.print(theme=Themes.thick)
┏━━━━━━━━━━━━━━━┓
┃  Table Name   ┃
┣━━━━━┳━━━━━┳━━━┫
┃   1 ┃   2 ┃ 3 ┃
┣━━━━━╋━━━━━╋━━━┫
┃ qwe ┃ rty ┃   ┃
┃     ┃ uio ┃   ┃
┗━━━━━┻━━━━━┻━━━┛
>>> t_name_column_names.print(theme=Themes.thick)
┏━━━━━━━━━━━━━━━┓
┃  Table Name   ┃
┣━━━━━┳━━━━━┳━━━┫
┃ c1  ┃ c2  ┃ 3 ┃
┣━━━━━╋━━━━━╋━━━┫
┃   1 ┃   2 ┃ 3 ┃
┣━━━━━╋━━━━━╋━━━┫
┃ qwe ┃ rty ┃   ┃
┃     ┃ uio ┃   ┃
┗━━━━━┻━━━━━┻━━━┛

```
</details>


<details>
<summary>Themes.thick_thin</summary>

```pycon
>>> t.print(theme=Themes.thick_thin)
┌─────┬─────┬───┐
│   1 │   2 │ 3 │
┠━━━━━╂━━━━━╂━━━┨
│ qwe │ rty │   │
│     │ uio │   │
└─────┴─────┴───┘
>>> t_column_names.print(theme=Themes.thick_thin)
┌─────┬─────┬───┐
│ c1  │ c2  │ 3 │
┠━━━━━╂━━━━━╂━━━┨
│   1 │   2 │ 3 │
├─────┼─────┼───┤
│ qwe │ rty │   │
│     │ uio │   │
└─────┴─────┴───┘
>>> t_name.print(theme=Themes.thick_thin)
┌───────────────┐
│  Table Name   │
├─────┬─────┬───┤
│   1 │   2 │ 3 │
┠━━━━━╂━━━━━╂━━━┨
│ qwe │ rty │   │
│     │ uio │   │
└─────┴─────┴───┘
>>> t_name_column_names.print(theme=Themes.thick_thin)
┌───────────────┐
│  Table Name   │
├─────┬─────┬───┤
│ c1  │ c2  │ 3 │
┠━━━━━╂━━━━━╂━━━┨
│   1 │   2 │ 3 │
├─────┼─────┼───┤
│ qwe │ rty │   │
│     │ uio │   │
└─────┴─────┴───┘

```
</details>


<details>
<summary>Themes.double</summary>

```pycon
>>> t.print(theme=Themes.double)
╔═════╦═════╦═══╗
║   1 ║   2 ║ 3 ║
╠═════╬═════╬═══╣
║ qwe ║ rty ║   ║
║     ║ uio ║   ║
╚═════╩═════╩═══╝
>>> t_column_names.print(theme=Themes.double)
╔═════╦═════╦═══╗
║ c1  ║ c2  ║ 3 ║
╠═════╬═════╬═══╣
║   1 ║   2 ║ 3 ║
╠═════╬═════╬═══╣
║ qwe ║ rty ║   ║
║     ║ uio ║   ║
╚═════╩═════╩═══╝
>>> t_name.print(theme=Themes.double)
╔═══════════════╗
║  Table Name   ║
╠═════╦═════╦═══╣
║   1 ║   2 ║ 3 ║
╠═════╬═════╬═══╣
║ qwe ║ rty ║   ║
║     ║ uio ║   ║
╚═════╩═════╩═══╝
>>> t_name_column_names.print(theme=Themes.double)
╔═══════════════╗
║  Table Name   ║
╠═════╦═════╦═══╣
║ c1  ║ c2  ║ 3 ║
╠═════╬═════╬═══╣
║   1 ║   2 ║ 3 ║
╠═════╬═════╬═══╣
║ qwe ║ rty ║   ║
║     ║ uio ║   ║
╚═════╩═════╩═══╝

```
</details>


<details>
<summary>Themes.double_thin</summary>

```pycon
>>> t.print(theme=Themes.double_thin)
╔═════╦═════╦═══╗
║   1 ║   2 ║ 3 ║
╟─────╫─────╫───╢
║ qwe ║ rty ║   ║
║     ║ uio ║   ║
╚═════╩═════╩═══╝
>>> t_column_names.print(theme=Themes.double_thin)
╔═════╦═════╦═══╗
║ c1  ║ c2  ║ 3 ║
╟─────╫─────╫───╢
║   1 ║   2 ║ 3 ║
╠═════╬═════╬═══╣
║ qwe ║ rty ║   ║
║     ║ uio ║   ║
╚═════╩═════╩═══╝
>>> t_name.print(theme=Themes.double_thin)
╔═══════════════╗
║  Table Name   ║
╠═════╦═════╦═══╣
║   1 ║   2 ║ 3 ║
╟─────╫─────╫───╢
║ qwe ║ rty ║   ║
║     ║ uio ║   ║
╚═════╩═════╩═══╝
>>> t_name_column_names.print(theme=Themes.double_thin)
╔═══════════════╗
║  Table Name   ║
╠═════╦═════╦═══╣
║ c1  ║ c2  ║ 3 ║
╟─────╫─────╫───╢
║   1 ║   2 ║ 3 ║
╠═════╬═════╬═══╣
║ qwe ║ rty ║   ║
║     ║ uio ║   ║
╚═════╩═════╩═══╝

```
</details>


<details>
<summary>Themes.booktabs</summary>

```pycon
>>> t.print(theme=Themes.booktabs)
 ─────────────── 
    1     2   3  
 ━━━━━━━━━━━━━━━ 
  qwe   rty      
        uio      
 ─────────────── 
>>> t_column_names.print(theme=Themes.booktabs)
 ─────────────── 
  c1    c2    3  
 ━━━━━━━━━━━━━━━ 
    1     2   3  
 ─────────────── 
  qwe   rty      
        uio      
 ─────────────── 
>>> t_name.print(theme=Themes.booktabs)
 ─────────────── 
   Table Name    
 ─────────────── 
    1     2   3  
 ━━━━━━━━━━━━━━━ 
  qwe   rty      
        uio      
 ─────────────── 
>>> t_name_column_names.print(theme=Themes.booktabs)
 ─────────────── 
   Table Name    
 ─────────────── 
  c1    c2    3  
 ━━━━━━━━━━━━━━━ 
    1     2   3  
 ─────────────── 
  qwe   rty      
        uio      
 ─────────────── 

```
</details>


<details>
<summary>Themes.markdown</summary>

```pycon
>>> t.print(theme=Themes.markdown)
|   1 |   2 | 3 |
|-----|-----|---|
| qwe | rty |   |
|     | uio |   |
>>> t_column_names.print(theme=Themes.markdown)
| c1  | c2  | 3 |
|-----|-----|---|
|   1 |   2 | 3 |
| qwe | rty |   |
|     | uio |   |
>>> t_name.print(theme=Themes.markdown)
|  Table Name   |
|   1 |   2 | 3 |
|-----|-----|---|
| qwe | rty |   |
|     | uio |   |
>>> t_name_column_names.print(theme=Themes.markdown)
|  Table Name   |
| c1  | c2  | 3 |
|-----|-----|---|
|   1 |   2 | 3 |
| qwe | rty |   |
|     | uio |   |

```
</details>
</details>

## Emojis

<details>
<summary>Example</summary>

```python
from prettytable import PrettyTable
from table2string import Table

names = ("plain text", "emoji")
table = [
    (
        "text\\ntext",
        "👨‍👩‍👧‍👦👨‍👩‍👦‍👦👨‍👩‍👧‍👧\\n"
        "👨‍👨‍👧‍👦👨‍👨‍👧‍👧👨‍👩‍👧👩‍❤️‍👨\\n"
        "👨‍❤️‍👨👯👩‍🦼👭👨‍👩‍👧‍👦\\n"
        "👨‍👨‍👧‍👦👨‍👨‍👦👩‍👩‍👧\\n"
        "👨‍👨‍👧‍👧👨‍👩‍👦‍👦",
    ),
]
t = PrettyTable(title="prettytable", field_names=names, align="c")
t.add_rows(table)
print(t)

t = Table(table, name="table2string", column_names=names)
t.print(align="^", sep=(1,))
```

<details>
    <summary>Windows Terminal</summary>
    <img alt="emoji_example_1.png" src="https://raw.githubusercontent.com/EgorKhabarov/table2string/master/images/emoji_example_Windows_Terminal.png">
</details>

<details>
    <summary>Windows 10</summary>
    <img alt="emoji_example_windows_10_terminal.png" src="https://raw.githubusercontent.com/EgorKhabarov/table2string/master/images/emoji_example_windows_10_terminal.png">
</details>

<details>
    <summary>Windows 11</summary>
    <img alt="emoji_example_windows_11_terminal.png" src="https://raw.githubusercontent.com/EgorKhabarov/table2string/master/images/emoji_example_windows_11_terminal.png">
</details>

<details>
    <summary>VT100 terminal emulator</summary>
    <img alt="emoji_example_VT100_terminal_emulator.png" src="https://raw.githubusercontent.com/EgorKhabarov/table2string/master/images/emoji_example_VT100_terminal_emulator.png">
</details>
</details>
""",
                },
                "Web": {
                    "Django": {
                        "Команды": """
Запустить сервер

```
./manage.py runserver
```

Создать Django проект

```bash
django-admin startproject PROJECTNAME
```

Перейти в папку с этим проектом

```bash
cd PROJECTNAME
```

Создать приложение (App)

```
./manage.py startapp APPNAME
```

Сделать миграцию (изменение в базе данных)

```
./manage.py makemigrations
./manage.py migrate
```

Создать админа

```
./manage.py createsuperuser
```
"""
                    },
                    "Flask": {
                        "Типы переменных": """
| Тип                   | Пояснение                                            |
|-----------------------|------------------------------------------------------|
| string (по умолчанию) | принимает любой текст без косой черты                |
| int                   | принимает положительные целые числа                  |
| float                 | принимает положительные значения с плавающей запятой |
| path                  | нравится, но также принимает косые черты string      |
| uuid                  | принимает строки UUID                                |

```python
@app.route("/<type:name>")
def func(name: type):
    pass
```
""",
                    },
                    "Jinja": {
                        "index": """
**Шаблонный движок**: `Jinja3` — это шаблонный движок для `Python`,
который помогает отделить логику приложения от представления.
Это достигается за счет использования шаблонов для генерации HTML (или других текстовых форматов),
что позволяет легко изменять внешний вид и структуру выходных данных без изменения логики кода.

**Переменные**: В `Jinja3` переменные используются для динамической вставки данных в шаблон.
Они обозначаются двойными фигурными скобками `{{ variable }}`
и могут содержать любые данные, переданные из контекста рендеринга.
""",
                        "Базовый синтаксис": """
### Базовый синтаксис

<!--{% raw %}-->
- **Вывод переменных**: `{{ variable }}` — используется для вывода значения переменной в шаблоне.
- **Фильтры**: `{{ variable | filter }}` — фильтры применяются к переменным для изменения их значения перед выводом.
Например, `{{ name | upper }}` выводит значение переменной name в верхнем регистре.
- **Команды**: `{% command %}` — используется для управления логикой в шаблоне.
Например, `{% for item in list %}...{% endfor %}` для циклов, `{% if condition %}...{% endif %}` для условий.
- **Комментарии**: `{# comment #}` — используется для добавления комментариев, которые не отображаются в конечном выводе.
<!--{% endraw %}-->
""",
                        "Управляющие структуры": """
### Управляющие структуры

<!--{% raw %}-->
- **Циклы**: Используются для итерации по последовательностям данных, таким как списки или кортежи.
```jinja
{% for item in list %}
    <p>{{ item }}</p>
{% endfor %}
```
- **Условия**: Позволяют выполнять разные действия в зависимости от условий.
```jinja
{% if user.is_authenticated %}
    <p>Welcome, {{ user.name }}!</p>
{% else %}
    <p>Please log in.</p>
{% endif %}
```
Можно использовать `{% elif %}` для добавления дополнительных условий.
- **Макросы**: Функции, которые позволяют повторно использовать блоки кода в шаблонах.
```jinja
{% macro render_item(item) %}
    <div>{{ item.name }}</div>
{% endmacro %}

{{ render_item(item) }}
```
<!--{% endraw %}-->
""",
                        "Фильтры и функции": """
### Фильтры и функции

  - **Стандартные фильтры**: `Jinja3` предоставляет множество встроенных фильтров для обработки данных:
    - `length`: Возвращает длину последовательности.
    - `default`: Возвращает значение по умолчанию, если переменная пустая.
    - `join`: Объединяет элементы списка в строку, используя указанный разделитель.
    - `replace`: Заменяет подстроку в строке.
    - `upper` и `lower`: Преобразуют строку в верхний или нижний регистр.
    - `truncate`: Обрезает строку до указанной длины.
  - **Пользовательские фильтры**: Можно создавать собственные фильтры, регистрируя функции в приложении `Python` и подключая их к `Jinja3`.
""",
                        "Шаблонные наследования": """
### Шаблонные наследования

<!--{% raw %}-->
  - **Базовый шаблон**: Используется для создания общего каркаса страниц.
В базовом шаблоне определяются блоки, которые могут быть переопределены в дочерних шаблонах.
```jinja
<!DOCTYPE html>
<html>
<head>
    <title>{% block title %}My Site{% endblock %}</title>
</head>
<body>
    {% block content %}{% endblock %}
</body>
</html>
```
  - **Расширение шаблонов**: Дочерние шаблоны могут расширять базовый, переопределяя или дополняя его блоки.
```jinja
{% extends "base.html" %}

{% block title %}Home Page{% endblock %}

{% block content %}
    <h1>Welcome to the Home Page</h1>
    <p>This is the main content.</p>
{% endblock %}
```
Это позволяет легко поддерживать единый стиль и структуру для всех страниц, изменяя только необходимые части.
<!--{% endraw %}-->
""",
                        "Инклюды и импорт": """
### Инклюды и импорт

<!--{% raw %}-->
  - **Инклюд**: Используется для включения другого шаблона в текущий.
Это удобно для повторного использования небольших блоков `HTML`,
таких как заголовки, подвал сайта или навигационные меню.
```jinja
{% include 'header.html' %}
<p>Main content goes here.</p>
{% include 'footer.html' %}
```
При использовании `{% include %}` можно также передавать переменные в включаемый шаблон.
  - **Импорт макросов**: Позволяет импортировать макросы из других шаблонов для повторного использования кода.
```jinja
{% from 'macros.html' import render_item %}
<div>
    {{ render_item(item) }}
</div>
```
Это позволяет хранить макросы в отдельных файлах, упрощая их поддержку и организацию.
<!--{% endraw %}-->
""",
                        "Работа с контекстом": """
### Работа с контекстом

<!--{% raw %}-->
  - **Передача данных в шаблон**: При рендеринге шаблона данные передаются в него через контекст.
В контексте могут находиться переменные, которые используются для заполнения шаблона.
```python
from jinja2 import Template

template = Template("Hello, {{ name }}!")
output = template.render(name="Alice")
print(output)  # "Hello, Alice!"
```
  - **Контекстные переменные**: Переменные, переданные в шаблон, доступны только в пределах текущего рендеринга.
Однако, в `Jinja3` можно использовать и глобальные переменные или функции, которые доступны во всех шаблонах.
```jinja
{% set greeting = "Hello" %}
<p>{{ greeting }}, {{ user.name }}!</p>
```
  - **Вложенные контексты**: Внутри шаблона можно создавать вложенные контексты, используя директивы `{% with %}` или `{% set %}`.
```jinja
{% with message = "Welcome" %}
    <p>{{ message }}, {{ user.name }}!</p>
{% endwith %}
```

Это позволяет гибко управлять видимостью и доступностью данных в разных частях шаблона.
<!--{% endraw %}-->
""",
                        "Безопасность": """
### Безопасность

<!--{% raw %}-->
  - **Экранирование HTML**: `Jinja3` **по умолчанию экранирует все выводимые переменные**,
чтобы предотвратить **<u>XSS-атаки</u>** **(Cross-Site Scripting)**.
Это означает, что специальные HTML-символы, такие как `<`, `>`, `&`, автоматически заменяются их безопасными эквивалентами.
```jinja
{{ user_input }}  {# автоматическое экранирование #}
```
  - **Отключение экранирования**: Если необходимо вывести `HTML`-код без экранирования
(например, если вы уверены в безопасности данных), можно использовать фильтр `safe`.
```jinja
{{ user_input | safe }}
```
Однако это нужно делать с осторожностью, чтобы избежать возможных уязвимостей.
  - **Превентивные меры**: Важно всегда проверять и валидировать данные, которые приходят от пользователей,
даже если `Jinja3` экранирует их по умолчанию.
Это помогает предотвратить несанкционированный доступ или манипуляции с данными.
<!--{% endraw %}-->
""",
                        "Лучшие практики": """
### Лучшие практики

  - **Разделение логики и представления**: Держите логику приложения и шаблоны отдельно.
В шаблонах должна находиться только логика, связанная с представлением, а не бизнес-логика.
  - **Чистота шаблонов**: Старайтесь избегать сложных вычислений и операций в шаблонах.
Вместо этого выполняйте такие операции в контроллерах или моделях и передавайте результаты в шаблоны.
  - **Повторное использование шаблонов**: Используйте наследование шаблонов и макросы для создания повторно используемых компонентов.
Это облегчает поддержку и обновление кода.
  - **Минимизация количества включаемых файлов**: Старайтесь не дробить шаблоны на слишком мелкие части,
так как это может усложнить их поддержку и увеличить время загрузки.
  - **Использование кэширования**: При необходимости используйте кэширование скомпилированных шаблонов
для улучшения производительности приложения.
  - **Документирование и комментарии**: Оставляйте комментарии в шаблонах, чтобы объяснить назначение сложных или неочевидных частей кода.
""",
                    },
                    "webcolors": r"""
Библиотека "webcolors" используется для работы с цветами веб-страниц, конвертации цветовых кодов и определения названий цветов.

Описание методов модуля "webcolors" и его подмодулей:

Модуль "webcolors":
`hex_to_rgb(hex_color)`: преобразует шестнадцатеричный код цвета в формат RGB.
`rgb_to_hex(rgb_color)`: преобразует цвет в формате RGB в шестнадцатеричный код.
`name_to_rgb(color_name)`: возвращает RGB-значение заданного названия цвета.
`rgb_to_name(rgb_color)`: возвращает название цвета для заданного значения RGB.

Список часто используемых методов, их краткое описание и

Метод `hex_to_rgb(hex_color)`: преобразует шестнадцатеричный код цвета в формат RGB.

```python
from webcolors import hex_to_rgb

hex_color = "#FF0000"
rgb_color = hex_to_rgb(hex_color)
print(rgb_color)  # (255, 0, 0)
```

Метод `rgb_to_hex(rgb_color)`: преобразует цвет в формате RGB в шестнадцатеричный код.

```python
from webcolors import rgb_to_hex

rgb_color = (255, 0, 0)
hex_color = rgb_to_hex(rgb_color)
print(hex_color)  # "#FF0000"
```

Метод `name_to_rgb(color_name)`: возвращает RGB-значение заданного названия цвета.

```python
from webcolors import name_to_rgb

color_name = "red"
rgb_color = name_to_rgb(color_name)
print(rgb_color)  # (255, 0, 0)
```

Метод `rgb_to_name(rgb_color)`: возвращает название цвета для заданного значения RGB.

```python
from webcolors import rgb_to_name

rgb_color = (255, 0, 0)
color_name = rgb_to_name(rgb_color)
print(color_name)  # "red"
```
""",
                    "bleach": r"""
Библиотека "bleach" используется для безопасного удаления или экранирования HTML-тегов и атрибутов в тексте,
чтобы предотвратить возможность внедрения вредоносного кода или XSS-атак.

Метод              | Описание
-------------------|-----------------------------------------------------------
clean              | Удаляет или экранирует HTML-теги и атрибуты из текста
linkify            | Преобразует URL-адреса в тексте в ссылки
strip_tags         | Удаляет все HTML-теги из текста
escape             | Экранирует HTML-сущности в тексте
unescape           | Преобразует экранированные HTML-сущности в их исходное состояние

Наиболее часто используемые методы "bleach" вместе с их кратким описанием и примером кода:

Метод              | Описание                                   | Пример кода
-------------------|--------------------------------------------|------------------------------
clean              | Удаляет или экранирует HTML-теги и атрибуты | clean(text, tags=["p", "a"])
linkify            | Преобразует URL-адреса в тексте в ссылки   | linkify(text)
strip_tags         | Удаляет все HTML-теги из текста             | strip_tags(text)
escape             | Экранирует HTML-сущности в тексте           | escape(text)
unescape           | Преобразует экранированные HTML-сущности     | unescape(text)
""",
                    "webencodings": r"""
Библиотека "webencodings" используется для работы с кодированием и декодированием текста в веб-разработке.
Она предоставляет функции для преобразования между различными форматами кодировки, такими как HTML-entities, UTF-8 и другие.

Методы модуля "webencodings" и его подмодулей:

Модуль "webencodings":
decode(s, encoding="utf-8", errors="strict"): Декодирует строку "s" из указанной кодировки в Unicode.
encode(s, encoding="utf-8", errors="strict"): Кодирует строку "s" в указанной кодировке.
htmldecode(s, keep_ignorable=False, encoding="utf-8", errors="xmlcharrefreplace"): Декодирует строку "s" из HTML-entities в Unicode.
htmlencode(s, encoding="utf-8", errors="xmlcharrefreplace"): Преобразует строку "s" в HTML-entities.
unquote(qstring, encoding="utf-8", errors="replace"): Декодирует строку "qstring" из формата URL-кодирования.

Самые часто используемые методы "webencodings" и их описание с примерами кода:

decode(s, encoding="utf-8", errors="strict"): Декодирует строку "s" из указанной кодировки в Unicode.

```python
import webencodings

encoded_string = b"\xd0\x9f\xd1\x80\xd0\xb8\xd0\xb2\xd0\xb5\xd1\x82"
decoded_string = webencodings.decode(encoded_string, encoding="utf-8")
print(decoded_string)  # Привет
```

encode(s, encoding="utf-8", errors="strict"): Кодирует строку "s" в указанной кодировке.

```python
import webencodings

decoded_string = "Привет"
encoded_string = webencodings.encode(decoded_string, encoding="utf-8")
print(encoded_string)  # b"\xd0\x9f\xd1\x80\xd0\xb8\xd0\xb2\xd0\xb5\xd1\x82"
```

"htmldecode(s, keep_ignorable=False, encoding="utf-8", errors="xmlcharrefreplace")": Декодирует строку "s" из HTML-entities в Unicode.

```python
import webencodings

html_string = "&lt;div&gt;Hello&lt;/div&gt;"
decoded_string = webencodings.htmldecode(html_string)
print(decoded_string)  # <div>Hello</div>
```

"htmlencode(s, encoding="utf-8", errors="xmlcharrefreplace")": Преобразует строку "s" в HTML-entities.

```python
import webencodings

plain_string = "<div>Hello</div>"
encoded_string = webencodings.htmlencode(plain_string)
print(encoded_string)  # &lt;div&gt;Hello&lt;/div&gt;
```

unquote(qstring, encoding="utf-8", errors="replace"): Декодирует строку "qstring" из формата URL-кодирования.

```python
import webencodings

url_encoded_string = "Hello%20World%21"
decoded_string = webencodings.unquote(url_encoded_string)
print(decoded_string)  # Hello World!
```
""",
                    "certifi": r"""
Библиотека "certifi" в Python используется для работы с сертификатами в криптографии.
Она предоставляет набор корневых сертификатов, которые могут быть использованы
для проверки подлинности SSL-соединений при выполнении запросов HTTP.

Методы и подмодули "certifi":
Подмодуль "cacertifi": содержит корневые сертификаты, предназначенные для проверки SSL-соединений.
Функция `where()`: возвращает путь к файлу с набором корневых сертификатов.
Функция `contents()`: возвращает содержимое файла с корневыми сертификатами в виде строки.
Функция `old_where()`: возвращает путь к предыдущей версии файла с корневыми сертификатами.
Функция `old_contents()`: возвращает содержимое предыдущей версии файла с корневыми сертификатами.
Функция `contents_bytes()`: возвращает содержимое файла с корневыми сертификатами в виде байтовой строки.

Некоторые часто используемые методы "certifi":
Функция `where()`: возвращает путь к файлу с набором корневых сертификатов.

```python
import certifi

file_path = certifi.where()
print(file_path)
```

Функция `contents()`: возвращает содержимое файла с корневыми сертификатами в виде строки.

```python
import certifi

cert_contents = certifi.contents()
print(cert_contents)
```

Функция `old_where()`: возвращает путь к предыдущей версии файла с корневыми сертификатами.

```python
import certifi

old_file_path = certifi.old_where()
print(old_file_path)
```

Функция `old_contents()`: возвращает содержимое предыдущей версии файла с корневыми сертификатами.

```python
import certifi

old_cert_contents = certifi.old_contents()
print(old_cert_contents)
```

Функция `contents_bytes()`: возвращает содержимое файла с корневыми сертификатами в виде байтовой строки.

```python
import certifi

cert_bytes = certifi.contents_bytes()
print(cert_bytes)
```
""",
                    "rfc3986_validator": r"""
Название библиотеки: "rfc3986_validator"

Описание: Библиотека "rfc3986_validator" используется для проверки и валидации URL-адресов согласно стандарту RFC 3986.
Она обеспечивает функционал для проверки правильности формата URL и его различных компонентов, таких как схема, хост, путь и другие.

Методы модуля и их описание:

Модуль: rfc3986_validator
validate(url: str) -> bool: Проверяет, соответствует ли заданный URL формату RFC 3986. Возвращает True, если URL действительный, и False в противном случае.
get_scheme(url: str) -> str: Извлекает и возвращает схему (протокол) из заданного URL.
get_host(url: str) -> str: Извлекает и возвращает хост (доменное имя) из заданного URL.
get_path(url: str) -> str: Извлекает и возвращает путь из заданного URL.
get_query(url: str) -> str: Извлекает и возвращает параметры запроса из заданного URL.
get_fragment(url: str) -> str: Извлекает и возвращает фрагмент из заданного URL.

Список самых часто используемых методов, их описание и

validate(url: str) -> bool:
Описание: Проверяет, является ли заданный URL действительным согласно стандарту RFC 3986.

```python
from rfc3986_validator import validate

url = "https://www.example.com"
is_valid = validate(url)
print(is_valid)  # True, если URL действителен
```

get_host(url: str) -> str:
Описание: Извлекает и возвращает хост (доменное имя) из заданного URL.

```python
from rfc3986_validator import get_host

url = "https://www.example.com/path"
host = get_host(url)
print(host)  # "www.example.com"
```

get_path(url: str) -> str:
Описание: Извлекает и возвращает путь из заданного URL.

```python
from rfc3986_validator import get_path

url = "https://www.example.com/path"
path = get_path(url)
print(path)  # "/path"
```
""",
                    "grpc": r"""
Библиотека "grpc" в Python используется для реализации удаленного вызова процедур (RPC - Remote Procedure Call).
Это позволяет разработчикам создавать распределенные системы,
где клиентский код может вызывать функции на удаленном сервере, будто они находятся локально.

Методы и подмодули библиотеки "grpc":
grpc.insecure_channel(): Создает небезопасный канал связи для клиентского подключения к серверу.
grpc.secure_channel(): Создает безопасный канал связи (шифрованное соединение) для клиентского подключения к серверу.
grpc.Channel: Класс, представляющий канал связи между клиентом и сервером.
grpc.Server: Класс, представляющий сервер, который слушает входящие запросы и обрабатывает их с помощью определенных сервисов.
grpc.stub: Подмодуль, содержащий классы и функции для создания клиентских и серверных стабов (stub), облегчающих взаимодействие по RPC.
grpc.Service: Базовый класс для реализации пользовательских сервисов GRPC.
grpc.rpc_error: Подмодуль, содержащий классы исключений, связанных с ошибками RPC.

Некоторые часто используемые методы библиотеки "grpc":
grpc.insecure_channel(): Создает небезопасный канал связи с сервером. `channel = grpc.insecure_channel("localhost:50051")`
grpc.stub: Подмодуль, который предоставляет классы для создания клиентских и серверных стабов (stub) для удобного взаимодействия по RPC.
grpc.Server.add_insecure_port(): Определяет небезопасный порт, на котором сервер будет прослушивать входящие запросы. `server.add_insecure_port("[::]:50051")`
grpc.Server.start(): Запускает сервер, ожидающий входящих запросов. `server.start()`
grpc.Service: Базовый класс, который разработчики могут наследовать для создания пользовательских сервисов GRPC. `class MyService(grpc.Service):`
""",
                },
                "Other": {
                    "pythoncom": r"""
Библиотека "pythoncom" используется для взаимодействия с COM-объектами (Component Object Model) в Python.
Она предоставляет функциональность для создания, вызова и управления COM-объектами,
такими как приложения Windows, компоненты Office и другие COM-совместимые объекты.

Вот таблица методов модуля "pythoncom" и его подмодулей:

| Метод           | Описание                             |
|-----------------|--------------------------------------|
| CoInitialize    | Инициализирует библиотеку COM.        |
| CoUninitialize  | Завершает работу с библиотекой COM.    |
| CoCreateInstance| Создает экземпляр COM-объекта.        |
| PyCom_RegisterUnknownHandler | Регистрирует обработчик для неизвестных COM-объектов. |
| CLSIDToClassMap | Карта соответствия CLSID и классов COM. |
| IIDToInterfaceMap | Карта соответствия IID и интерфейсов COM. |

Некоторые из часто используемых методов библиотеки "pythoncom" включают:
CoInitialize(): Инициализирует библиотеку COM, обычно вызывается в начале программы.
CoCreateInstance(clsid, interface=None, context=None, flags=None):
Создает экземпляр COM-объекта с помощью указанного идентификатора класса (CLSID).
Возвращает интерфейс COM-объекта.
CoUninitialize(): Завершает работу с библиотекой COM, обычно вызывается в конце программы.

Пример кода демонстрирующий использование метода CoCreateInstance():

```python
import pythoncom

# Идентификатор класса для Excel
clsid = "{00024500-0000-0000-C000-000000000046}"

# Создание экземпляра объекта Excel 
excel = pythoncom.CoCreateInstance(clsid, None, None, pythoncom.CLSCTX_SERVER)

# Вывод версии Excel
print(excel.Version)
```

Обратите внимание, что код может варьироваться в зависимости от требуемых COM-объектов и их интерфейсов.
""",
                    "nntplib": r"""
Библиотека "nntplib" в Python используется для взаимодействия с серверами новостных групп (NNTP).
Она предоставляет функции и методы для чтения, отправки и управления сообщениями в новостных группах.

Вот таблица методов и их краткие описания для модуля "nntplib" и его подмодулей:

Метод                  | Описание
-----------------------|-------------------------------
nntplib.NNTP           | Класс для установки соединения с сервером NNTP.
NNTP.__init__()        | Инициализация объекта NNTP.
NNTP.quit()            | Отключение от сервера NNTP.
NNTP.group(group)      | Выбор новостной группы для чтения статей.
NNTP.list()            | Получение списка доступных новостных групп.
NNTP.article(num)      | Получение статьи по ее номеру.
NNTP.body(num)         | Получение тела статьи по ее номеру.
NNTP.head(num)         | Получение заголовка статьи по ее номеру.
NNTP.post(message)     | Отправка сообщения на сервер NNTP.
NNTP.search(criteria)  | Поиск статей, удовлетворяющих заданным критериям.

Вот список самых часто используемых методов в "nntplib" и их краткие описания:

NNTP.group(group): Выбирает новостную группу для чтения статей.
```python
from nntplib import NNTP

conn = NNTP("news.example.com")
conn.group("comp.lang.python")
```

NNTP.list(): Получает список доступных новостных групп.
```python
from nntplib import NNTP

conn = NNTP("news.example.com")
groups = conn.list()
```

NNTP.article(num): Получает статью по ее номеру.
```python
from nntplib import NNTP

conn = NNTP("news.example.com")
resp, article_lines, msg_id, info = conn.article("12345")
```

NNTP.post(message): Отправляет сообщение на сервер NNTP.
```python
from nntplib import NNTP

conn = NNTP("news.example.com")
resp = conn.post("<subject>", "<from>", "<body>")
```
""",
                    "wheel": r"""
Библиотека "wheel" в Python используется для упрощения установки пакетов и их распространения.
Она представляет собой формат пакета, который содержит предварительно
скомпилированные бинарные файлы, что позволяет ускорить процесс установки.

### Методы модуля "wheel"
`convert`: используется для преобразования исходных файлов пакета в формат wheel.
`install`: позволяет установить пакет из wheel-файла.
`unpack`: распаковывает содержимое wheel-файла.
`pack`: упаковывает исходные файлы пакета в wheel-файл.

### Подмодули
`metadata`: содержит методы для работы с метаданными пакета, такими как версия, автор и описание.
`tags`: предоставляет информацию о поддерживаемых платформах и интерпретаторах.
`signatures`: позволяет работать с подписями wheel-файлов.
`pep425tags`: предоставляет методы для работы с тегами PEP 425,
которые описывают совместимость пакетов с определенными версиями Python и операционных систем.


### convert
Преобразует исходные файлы пакета в формат wheel.

```python
from wheel import convert

convert.pack("path/to/source/package")
```

### install
Устанавливает пакет из wheel-файла.

```python
from wheel import install

install.install("path/to/wheel/file.whl")
```

### unpack
Распаковывает содержимое wheel-файла.

```python
from wheel import unpack

unpack.unpack("path/to/wheel/file.whl", "path/to/destination")
```

### pack</h3>
Упаковывает исходные файлы пакета в wheel-файл.

```python
from wheel import pack

pack.pack("path/to/source/package", "path/to/destination/file.whl")
```
""",
                    "js2py": r"""
Библиотека "js2py" используется в Python для выполнения и интерпретации JavaScript-кода.
Она предоставляет возможность взаимодействия между Python и JavaScript, позволяя исполнять JavaScript-код внутри среды Python.

Таблица методов модуля "js2py":

Метод           | Описание кратко   
----------------|----------------
eval_js()       | Исполняет переданный JavaScript-код и возвращает его результат.
call()          | Вызывает функцию JavaScript и передает ей аргументы.
set()           | Устанавливает значение переменной JavaScript.
get()           | Получает значение переменной JavaScript.
delete()        | Удаляет переменную JavaScript.

Список самых часто используемых методов, их краткое описание и

eval_js(): Исполняет переданный JavaScript-код и возвращает его результат.

```python
print(eval_js("1 + 2"))  # 3
```

call(): Вызывает функцию JavaScript и передает ей аргументы.

```python
js_function = js2py.eval_js("function add(a, b) { return a + b; }")
print(call(js_function, 2, 3))  # 5
```

set(): Устанавливает значение переменной JavaScript.

```python
set("x", 10)
print(eval_js("x"))  # 10
```

get(): Получает значение переменной JavaScript.

```python
eval_js("var message = 'Hello, world!'")
print(get("message"))  # Hello, world!
```

delete(): Удаляет переменную JavaScript.

```python
eval_js("var x = 5;")
delete("x")
print(eval_js("x"))  # undefined
```
""",
                    "pylab": r"""
Название библиотеки: "pylab"

Краткое описание: Библиотека "pylab" является комбинацией библиотеки "matplotlib" и "NumPy"
для выполнения научных и инженерных вычислений в Python.
Она предоставляет функции для создания графиков, визуализации данных и выполнения математических операций.

Таблица методов:

| Метод                | Описание                                                    |
|----------------------|-------------------------------------------------------------|
| `plot`               | Построить график из данных                                   |
| `scatter`            | Создать точечную диаграмму                                   |
| `hist`               | Построить гистограмму из данных                              |
| `imshow`             | Отобразить изображение                                       |
| `xlabel`             | Задать подпись для оси x                                    |
| `ylabel`             | Задать подпись для оси y                                    |
| `title`              | Задать заголовок графика                                    |
| `legend`             | Вывести легенду графика                                     |
| `grid`               | Отобразить сетку на графике                                 |
| `sin`                | Вычислить синус значения                                     |
| `cos`                | Вычислить косинус значения                                  |
| `exp`                | Вычислить экспоненту значения                               |


Метод `plot` позволяет строить графики из предоставленных данных.

```python
import pylab

x = [1, 2, 3, 4, 5]
y = [10, 20, 30, 40, 50]

pylab.plot(x, y)
pylab.show()
```

Метод `scatter` используется для создания точечной диаграммы.

```python
import pylab

x = [1, 2, 3, 4, 5]
y = [10, 20, 30, 40, 50]

pylab.scatter(x, y)
pylab.show()
```

Метод `hist` позволяет создать гистограмму из предоставленных данных.

```python
import pylab

data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]

pylab.hist(data)
pylab.show()
```

Метод `imshow` используется для отображения изображений.

```python
import pylab
import numpy as np

image = np.random.random((10, 10))

pylab.imshow(image)
pylab.show()
```

Метод `xlabel` задает подпись для оси x на графике.

```python
import pylab

x = [1, 2, 3, 4, 5]
y = [10, 20, 30, 40, 50]

pylab.plot(x, y)
pylab.xlabel("X-axis")
pylab.show()
```

Метод `ylabel` задает подпись для оси y на графике.

```python
import pylab

x = [1, 2, 3, 4, 5]
y = [10, 20, 30, 40, 50]

pylab.plot(x, y)
pylab.ylabel("Y-axis")
pylab.show()
```

Метод `title` задает заголовок для графика.

```python
import pylab

x = [1, 2, 3, 4, 5]
y = [10, 20, 30, 40, 50]

pylab.plot(x, y)
pylab.title("My Plot")
pylab.show()
```

Метод `legend` выводит легенду на графике.

```python
import pylab

x = [1, 2, 3, 4, 5]
y = [10, 20, 30, 40, 50]

pylab.plot(x, y, label="Data")
pylab.legend()
pylab.show()
```

Метод `grid` отображает сетку на графике.

```python
import pylab

x = [1, 2, 3, 4, 5]
y = [10, 20, 30, 40, 50]

pylab.plot(x, y)
pylab.grid(True)
pylab.show()
```

Метод `sin` используется для вычисления синуса значения.

```python
import pylab


print(pylab.sin(0.5))
```

Метод `cos` используется для вычисления косинуса значения.

```python
import pylab


print(pylab.cos(0.5))
```

Метод `exp` используется для вычисления экспоненты значения.

```python
import pylab


print(pylab.exp(2))
```
""",
                    "rasutil": r"""
Библиотека "rasutil" (raspberry utility) используется для упрощения
разработки и взаимодействия с Raspberry Pi в языке программирования Python.

Таблица методов для модуля "rasutil":
Method 1: GPIOInit() - Инициализирует пины GPIO на Raspberry Pi.
Method 2: GPIOSet(pin, value) - Устанавливает значение пина GPIO на Raspberry Pi.
Method 3: GPIORead(pin) - Считывает значение с пина GPIO на Raspberry Pi.

Методы модуля "rasutil" позволяют управлять GPIO пинами на Raspberry Pi,
инициализировать их, устанавливать значения и считывать значения с этих пинов.

Список самых частых методов и их описания:
GPIOInit() - Инициализирует пины GPIO на Raspberry Pi.
```python
rasutil.GPIOInit()
```
Этот метод инициализирует пины GPIO на Raspberry Pi перед использованием.

GPIOSet(pin, value) - Устанавливает значение пина GPIO на Raspberry Pi.
```python
rasutil.GPIOSet(18, 1)
```
Этот метод устанавливает значение 1 на пине GPIO 18 на Raspberry Pi.

GPIORead(pin) - Считывает значение с пина GPIO на Raspberry Pi.
```python
value = rasutil.GPIORead(12)
```
Этот метод считывает значение с пина GPIO 12 на Raspberry Pi и сохраняет его в переменную "value".

Методы "GPIOSet" и "GPIORead" позволяют управлять значениями пинов GPIO на Raspberry Pi,
устанавливая значения и считывая их соответственно. Метод "GPIOInit" необходим для инициализации пинов GPIO перед их использованием.
""",
                    "poplib": r"""
Библиотека "poplib" в Python используется для работы с протоколом почтового ящика на основе протокола POP3 (Post Office Protocol version 3).
Она позволяет получать электронные письма, удалять их, и выполнять другие операции взаимодействия с почтовым сервером.

Методы и подмодули библиотеки "poplib":

`poplib.POP3(host[, port])`: Создает объект соединения с почтовым сервером POP3 на указанном хосте и порту.
`poplib.POP3.user(username)`: Аутентифицирует пользователя на сервере, указывая имя пользователя.
`poplib.POP3.pass_(password)`: Аутентифицирует пользователя на сервере, указывая пароль.
`poplib.POP3.stat()`: Возвращает информацию о состоянии почтового ящика, включая количество сообщений и общий размер.
`poplib.POP3.list([which])`: Возвращает список всех сообщений в почтовом ящике, или информацию о конкретном сообщении, если указан параметр "which".
`poplib.POP3.retr(which)`: Получает содержимое указанного сообщения из почтового ящика.
`poplib.POP3.dele(which)`: Отмечает указанное сообщение для удаления.
`poplib.POP3.quit()`: Закрывает соединение с сервером POP3.

Наиболее часто используемые методы в библиотеке "poplib":

`poplib.POP3(host[, port])`: Создание соединения с почтовым сервером.
`poplib.POP3.user(username)` и `poplib.POP3.pass_(password)`: Аутентификация пользователя на сервере.
`poplib.POP3.stat()`: Получение информации о состоянии почтового ящика.
`poplib.POP3.list()`: Получение списка всех сообщений в почтовом ящике.
`poplib.POP3.retr(which)`: Получение содержимого конкретного сообщения.
`poplib.POP3.quit()`: Закрытие соединения с сервером POP3.

Пример использования метода `poplib.POP3(user, password)` для создания соединения с почтовым сервером:

```python
import poplib

pop_server = poplib.POP3("mail.example.com", 110)
pop_server.user("your_username")
pop_server.pass_("your_password")
```
""",
                    "mailbox": r"""
Библиотека "mailbox" в Python используется для работы с почтовыми ящиками.
Она позволяет читать и записывать электронные письма в различных форматах, таких как mbox, MMDF, babyl и др.

Таблица методов библиотеки "mailbox":

| Метод               | Краткое описание                                      |
|---------------------|-------------------------------------------------------|
| mailbox.mbox        | Позволяет работать с форматом mbox.                    |
| mailbox.Maildir     | Предоставляет доступ к Maildir-формату почтового ящика. |
| mailbox.Babyl       | Обеспечивает работу с форматом babyl.                   |
| mailbox.MMDF        | Позволяет чтение и запись писем в формате MMDF.         |
| mailbox.Mailbox     | Предоставляет общий интерфейс для работы с почтовыми ящиками в разных форматах.  |
| mailbox.MaildirMessage  | Представляет отдельное письмо в формате Maildir. |
| mailbox.MH          | Работа с письмами в формате MH.                         |

Самые часто используемые методы библиотеки "mailbox":

`add` - добавляет письмо в почтовый ящик.

```python
with mailbox.mbox("sample.mbox") as mbox:
    message = EmailMessage()
    message["Subject"] = "Hello"
    message.set_content("This is a test email")
    mbox.add(message)
```

`iterkeys` - возвращает итератор для ключей (идентификаторов) писем в почтовом ящике.


```python
with mailbox.mbox("sample.mbox") as mbox:
    for key in mbox.iterkeys():
        print(key)
```

`get_message` - возвращает письмо по ключу (идентификатору).

```python
with mailbox.mbox("sample.mbox") as mbox:
    message = mbox.get_message("12345")
    print(message["Subject"])
```

`remove` - удаляет письмо по ключу (идентификатору).

```python
with mailbox.mbox("sample.mbox") as mbox:
    mbox.remove("12345")
```
""",
                    "regcheck": r"""
Библиотека "regcheck" используется для работы с регулярными выражениями в Python.
Она предоставляет инструменты для поиска и сравнения строк, основываясь на заданных шаблонах.

Таблица методов и их краткое описание для модуля "regcheck":

Метод         | Описание
------------- | -------------
search        | Выполняет поиск заданного регулярного выражения в строке и возвращает первое совпадение.
match         | Проверяет, соответствует ли вся строка заданному регулярному выражению.
findall       | Находит все совпадения заданного регулярного выражения в строке и возвращает их в виде списка.
finditer      | Находит все совпадения заданного регулярного выражения в строке и возвращает их в виде итератора.
split         | Разделяет строку на подстроки, используя заданное регулярное выражение в качестве разделителя.
sub           | Заменяет все совпадения заданного регулярного выражения в строке указанным значением.

Список самых часто используемых методов, их краткое описание и примерный код для демонстрации их работы:

Метод      | Описание                            | Примерный код
---------- | ----------------------------------- | -------------
search     | Ищет первое совпадение в строке      | import re \n result = re.search(r"pattern", string)
findall    | Находит все совпадения в строке       | import re \n results = re.findall(r"pattern", string)
split      | Разделяет строку на подстроки         | import re \n parts = re.split(r"\s", string)
sub        | Заменяет совпадения в строке          | import re \n new_string = re.sub(r"pattern", replacement, string)
""",
                    "traitlets": r"""
Библиотека "traitlets" в Python используется для определения и использования
типизированных атрибутов (traits) и событий (events) в объектно-ориентированном программировании.
Она обеспечивает механизмы проверки типов, установки значений по умолчанию,
уведомлений об изменениях и другие функции, улучшающие модульность и гибкость кода.


Модуль: traitlets

Методы:
HasTraits(): Базовый класс, предоставляющий инфраструктуру для определения типизированных атрибутов и событий.
default(obj): Метод, возвращающий значение по умолчанию для указанного атрибута.
validate(obj, value): Метод, проверяющий значение атрибута на соответствие заданным условиям или типу.
observe(cls, handler, names=None): Метод класса, позволяющий связать обработчик события с указанными атрибутами.
link(target, name, linkname=None): Метод объекта, позволяющий установить
связь между атрибутами текущего объекта и атрибутами другого объекта.

Подмодуль: traitlets.config

Методы:
Configurable(): Базовый класс, предоставляющий функциональность для работы с конфигурационными файлами и параметрами.
load_config_file(filename): Метод, загружающий конфигурационный файл, указанный по имени.
Application: Класс, представляющий приложение, которое может быть настроено с помощью конфигурационных файлов.
Config: Класс, представляющий конфигурацию, содержащую набор параметров для настройки.


Самые часто используемые методы:
default(obj): Возвращает значение по умолчанию для указанного атрибута.

```python
value = default("attr_name")
```

validate(obj, value): Проверяет значение атрибута на соответствие заданным условиям или типу.

```python
is_valid = validate("attr_name", value)
```

observe(cls, handler, names=None): Связывает обработчик события с указанными атрибутами.

```python
observe("class_name", handler_func, ["attr_name1", "attr_name2"])
```

link(target, name, linkname=None): Устанавливает связь между атрибутами
текущего объекта и атрибутами другого объекта.

```python
link(other_object, "attr_name", "linked_attr_name")
```
""",
                    "linecache": r"""
Библиотека "linecache" в Python используется для чтения линий из файлов с исходным кодом.
Она предоставляет функции для извлечения строк из файла по их номеру.

Методы модуля "linecache" включают:
`getline(filename, lineno)`: Возвращает указанную строку из указанного файла.
`getlines(filename)`: Возвращает все строки из указанного файла в виде списка.
`clearcache()`: Очищает кэш, используемый для хранения строк файла.

   Примеры подмодулей отсутствуют.

Некоторые из самых часто используемых методов "linecache" включают:
Метод `getline(filename, lineno)` - возвращает указанную строку из указанного файла.

```python
import linecache

line = linecache.getline("file.txt", 5)
print(line)
```

Этот код выведет пятую строку из файла "file.txt".

Метод `getlines(filename)` - возвращает все строки из указанного файла в виде списка.

```python
import linecache

lines = linecache.getlines("file.txt")
for line in lines:
    print(line)
```

Этот код выведет все строки из файла "file.txt" по одной строке на каждую итерацию цикла.

Метод `clearcache()` - очищает кэш, используемый для хранения строк файла.
Это может быть полезно, если файл изменился и требуется обновить строки в кэше.

```python
import linecache

# Изменения в файле "file.txt"

linecache.clearcache()
line = linecache.getline("file.txt", 5)
print(line)
```

Этот код сначала очищает кэш, а затем возвращает пятую строку из обновленного файла "file.txt".

Примечание: Убедитесь, что файл "file.txt" существует и содержит нужные строки.
""",
                    "readline": r"""
Библиотека "readline" используется в Python для обеспечения функциональности чтения и редактирования строк в интерактивной командной оболочке.

Методы модуля "readline" и его подмодулей:

readline(): Читает строку из входного потока.
add_history(string): Добавляет строку в историю командной оболочки.
clear_history(): Очищает историю командной оболочки.
get_history_length(): Возвращает количество записей в истории командной оболочки.
set_history_length(length): Устанавливает максимальное количество записей в истории командной оболочки.
get_current_history_length(): Возвращает текущую длину истории командной оболочки.
remove_history_item(pos): Удаляет запись из истории командной оболочки по указанной позиции.
replace_history_item(pos, string): Заменяет запись в истории командной оболочки по указанной позиции новой строкой.

Наиболее часто используемые методы:

readline(): Читает строку из входного потока.

```python
import readline

input_string = readline.readline()
print("Input:", input_string)
```

add_history(string): Добавляет строку в историю командной оболочки.

```python
import readline

readline.add_history("command 1")
readline.add_history("command 2")
```

clear_history(): Очищает историю командной оболочки.

```python
import readline

readline.clear_history()
```
""",
                    "sched": r"""
Библиотека "sched" в Python используется для планирования и управления задачами в программе.
Она позволяет создавать расписания выполнения задач и контролировать их выполнение в определенные моменты времени.

Методы модуля "sched" и его подмодулей:
sched.timefunc: Устанавливает функцию, которая будет использоваться для получения времени.
sched.delayfunc: Устанавливает функцию, вызываемую перед каждым циклом планировщика.
sched.enter(delay, priority, action, argument): Планирует выполнение задачи с заданным задержкой, приоритетом, действием и аргументом.
sched.enterabs(time, priority, action, argument): Планирует выполнение задачи в определенный момент времени с указанным приоритетом, действием и аргументом.
sched.cancel(event): Отменяет выполнение задачи, связанной с указанным событием.
sched.run(): Запускает планировщик и начинает выполнение задач.

Самые часто используемые методы библиотеки "sched" и их краткие описания:
enter(delay, priority, action, argument): Планирует выполнение задачи с заданной задержкой и приоритетом.

```python
import sched
import time

def print_message():
    print("Scheduled task executed.")

scheduler = sched.scheduler(time.time, time.sleep)
scheduler.enter(5, 1, print_message, ())
scheduler.run()
```

enterabs(time, priority, action, argument): Планирует выполнение задачи в определенный момент времени с указанным приоритетом.

```python
import sched
import time

def print_message():
    print("Scheduled task executed.")

scheduler = sched.scheduler(time.time, time.sleep)
scheduler.enterabs(time.time() + 10, 1, print_message, ())
scheduler.run()
```

cancel(event): Отменяет выполнение задачи, связанной с указанным событием.

```python
import sched
import time

def print_message():
    print("Scheduled task executed.")

scheduler = sched.scheduler(time.time, time.sleep)
event = scheduler.enter(5, 1, print_message, ())
scheduler.cancel(event)
scheduler.run()
```

Пожалуйста, помните об обеспечении безопасности при использовании этой библиотеки и выполнении задач в программе.
""",
                    "packaging": r"""
Библиотека "packaging" в Python используется для работы с упаковкой и распаковкой пакетов, а также для управления метаданными пакетов.
Она предоставляет функции для создания, проверки, обновления и распаковки пакетов в формате wheel или в формате сжатого архива.

Методы модуля "packaging" и его подмодулей:

Модуль packaging.version:
parse(version_string): Парсит версию из строки и возвращает объект Version.
Version: Класс для представления версии пакета.

Модуль packaging.specifiers:
Specifier: Класс для представления спецификации версии пакета.
LegacySpecifier: Класс для представления устаревшей спецификации версии пакета.
SpecifierSet: Класс для представления набора спецификаций версий пакета.

Модуль packaging.requirements:
Requirement: Класс для представления требования к пакету.

Модуль packaging.markers:
Marker: Класс для представления условий маркера.
default_environment: Возвращает стандартное окружение.

Модуль packaging.tags:
Tag: Класс для представления метки платформы.
sys_tags(): Возвращает метки платформы для текущей системы.

Наиболее часто используемые методы в библиотеке "packaging":

parse(version_string): Парсит версию из строки и возвращает объект Version.

```python
from packaging import version

version_string = "1.2.3"
parsed_version = version.parse(version_string)
print(parsed_version)
```

SpecifierSet(specifier_string): Создает набор спецификаций версий на основе строки.

```python
from packaging.specifiers import SpecifierSet

specifier_string = ">=1.0,<=2.0"
specifier_set = SpecifierSet(specifier_string)
print(specifier_set)
```

Requirement(requirement_string): Создает требование к пакету на основе строки.

```python
from packaging.requirements import Requirement

requirement_string = "numpy>=1.0"
requirement = Requirement(requirement_string)
print(requirement)
```

Убедитесь, что у вас установлена библиотека "packaging" перед использованием этих методов.
""",
                    "nis": r"""
Библиотека "nis" в Python используется для работы с сервисом Network Information Service (NIS).
NIS предоставляет распределенную базу данных, которая используется для хранения информации о пользователях,
группах и других системных ресурсах в сети.

Методы модуля "nis":
nis.match(mapname, key): Возвращает значение, связанное с указанным ключом в указанной базе данных.
nis.cat(mapname): Возвращает все записи из указанной базы данных.
nis.maps(): Возвращает список доступных баз данных.
nis.getmapbyname(name): Возвращает содержимое базы данных с указанным именем.
nis.getmapbynumber(number): Возвращает содержимое базы данных с указанным номером.

Некоторые из самых часто используемых методов "nis" включают:
match(mapname, key): Возвращает значение, связанное с указанным ключом в указанной базе данных.

```python
import nis

value = nis.match("passwd", "john")
print(value)
```

cat(mapname): Возвращает все записи из указанной базы данных.

```python
import nis

records = nis.cat("passwd")
for record in records:
    print(record)
```

maps(): Возвращает список доступных баз данных.

```python
import nis

map_list = nis.maps()
print(map_list)
```

Это лишь некоторые из методов, доступных в библиотеке "nis".
""",
                    "notebook": r"""
Библиотека "notebook" используется для создания интерактивных блокнотов в среде Jupyter Notebook.
Она предоставляет возможность комбинировать код, текст, графики и другие элементы в одном документе,
что делает его удобным инструментом для исследования данных, прототипирования и обучения.

Методы модуля "notebook" и его подмодулей:

Модуль "notebook":
`list_notebooks()`: возвращает список всех блокнотов в текущем рабочем каталоге.
`open_notebook(path)`: открывает блокнот по указанному пути.
`create_notebook()`: создает новый блокнот.
`save_notebook(path)`: сохраняет текущий блокнот по указанному пути.
`export_notebook(path, format)`: экспортирует блокнот в указанный формат (например, HTML, PDF).

Подмодуль "cells":
`list_cells()`: возвращает список всех ячеек в текущем блокноте.
`add_code_cell()`: добавляет новую ячейку с кодом.
`add_markdown_cell()`: добавляет новую ячейку с текстом в формате Markdown.
`delete_cell(index)`: удаляет ячейку по указанному индексу.

Самые часто используемые методы:

`list_notebooks()`: возвращает список всех блокнотов в текущем рабочем каталоге.

```python
from notebook import list_notebooks

notebooks = list_notebooks()
print(notebooks)
```

`open_notebook(path)`: открывает блокнот по указанному пути.

```python
from notebook import open_notebook

notebook = open_notebook("path/to/notebook.ipynb")
print(notebook)
```

`create_notebook()`: создает новый блокнот.

```python
from notebook import create_notebook

notebook = create_notebook()
print(notebook)
```

`save_notebook(path)`: сохраняет текущий блокнот по указанному пути.

```python
from notebook import save_notebook

save_notebook("path/to/save.ipynb")
```

`list_cells()`: возвращает список всех ячеек в текущем блокноте.

```python
from notebook.cells import list_cells

cells = list_cells()
print(cells)
```

`add_code_cell()`: добавляет новую ячейку с кодом.

```python
from notebook.cells import add_code_cell

cell = add_code_cell()
print(cell)
```

`add_markdown_cell()`: добавляет новую ячейку с текстом в формате Markdown.

```python
from notebook.cells import add_markdown_cell

cell = add_markdown_cell()
print(cell)
```

`delete_cell(index)`: удаляет ячейку по указанному индексу.

```python
from notebook.cells import delete_cell

delete_cell(0)
```
""",
                    "quopri": r"""
Библиотека "quopri" в Python используется для кодирования и декодирования данных в формате Quoted-Printable.
Quoted-Printable - это способ представления непечатных или специальных символов в текстовом формате,
который используется в электронной почте и других приложениях.

Методы и подмодули библиотеки "quopri":

`quopri.encode(input, output, quotetabs=False)` - кодирует входные данные в формат Quoted-Printable и записывает результат в выходной поток.
`quopri.decode(input, output, headers=False)` - декодирует входные данные из формата Quoted-Printable и записывает результат в выходной поток.
`quopri.quote(data)` - возвращает строку, в которой данные закодированы в формате Quoted-Printable.
`quopri.unquote(data)` - возвращает строку, в которой данные декодированы из формата Quoted-Printable.
`quopri.encodestring(s)` - кодирует строку в формат Quoted-Printable и возвращает результат как строку.
`quopri.decodestring(s)` - декодирует строку из формата Quoted-Printable и возвращает результат как строку.

Самые часто используемые методы:

`quopri.encode(input, output, quotetabs=False)` - метод для кодирования данных в формат Quoted-Printable.
Можно использовать для безопасной передачи данных по электронной почте или другим каналам связи.

```python
import quopri

input_data = b"Hello, world!"
encoded_data = quopri.encode(input_data)
print(encoded_data)
```

`quopri.decode(input, output, headers=False)` - метод для декодирования данных из формата Quoted-Printable.
Полезно при работе с данными, полученными из электронной почты или других источников, где данные могут быть закодированы в этом формате.

```python
import quopri

encoded_data = b"Hello=2C=20world=21"
decoded_data = quopri.decode(encoded_data)
print(decoded_data)
```
""",
                    "mailcap": r"""
Библиотека "mailcap" в Python используется для обработки типов файлов и ассоциированных программ.


Модуль: mailcap
findmatch: Находит подходящую запись для заданного типа файла и возвращает ее.
getcaps: Возвращает все записи в файле mailcap.
getparam: Возвращает значение параметра из записи mailcap.
listmailcapfiles: Возвращает список файлов mailcap в системе.
lookup: Находит запись mailcap для заданного типа файла.
parse: Разбирает содержимое mailcap-файла и возвращает его в виде словаря.


findmatch: Находит подходящую запись для заданного типа файла и возвращает ее.

```python
import mailcap

filename = "example.txt"
type = "text/plain"

match = mailcap.findmatch(type, filename)
if match:
    command = match[0]
    params = match[1]
    # выполнение команды с использованием параметров
```

getcaps: Возвращает все записи в файле mailcap.

```python
import mailcap

caps = mailcap.getcaps()
for cap in caps:
    print(cap)
```

lookup: Находит запись mailcap для заданного типа файла.

```python
import mailcap

type = "text/plain"
lookup = mailcap.lookup(type)
if lookup:
    print(lookup)
```

Маленький код для демонстрации этих методов:
```python
import mailcap

filename = "example.txt"
type = "text/plain"

match = mailcap.findmatch(type, filename)
if match:
    command = match[0]
    params = match[1]
    # выполнение команды с использованием параметров

caps = mailcap.getcaps()
for cap in caps:
    print(cap)

lookup = mailcap.lookup(type)
if lookup:
    print(lookup)
```
""",
                    "errno": r"""
Библиотека "errno" в Python используется для обработки ошибок, связанных с системными вызовами и функциями операционной системы.
Она предоставляет доступ к кодам ошибок, которые могут возникать
при выполнении операций ввода-вывода, работы с файлами, сетью и другими системными ресурсами.

Методы и подмодули библиотеки "errno":

errno.errorcode: Возвращает словарь, ключами которого являются коды ошибок, а значениями - соответствующие им символьные имена.
errno.geterrno(): Возвращает код текущей ошибки.
errno.geterror(): Возвращает описание текущей ошибки в виде строки.
errno.strerror(errno): Возвращает описание ошибки по заданному коду ошибки.
errno.clear(): Очищает код текущей ошибки.

Самые часто используемые методы библиотеки "errno":

errno.errorcode: Возвращает словарь, где ключами являются коды ошибок, а значениями - символьные имена.
Например: {"ENOENT": "No such file or directory", "EACCES": "Permission denied"}.

```python
import errno

error_codes = errno.errorcode
print(error_codes)
```

errno.geterrno(): Возвращает код текущей ошибки. Например: 2.

```python
import errno

error_num = errno.geterrno()
print(error_num)
```

errno.geterror(): Возвращает описание текущей ошибки в виде строки. Например: "No such file or directory".

```python
import errno

error_desc = errno.geterror()
print(error_desc)
```
""",
                    "ntpath": r"""
Библиотека "ntpath" в Python используется для обработки и манипулирования путями файловой системы
с учетом специфических особенностей операционной системы Windows.

Таблица методов модуля и его подмодуля "ntpath" и их краткое описание:

Метод                                     | Описание
----------------------------------------|---------------------------------------------------
ntpath.abspath(path)                     | Возвращает абсолютный путь к указанному пути.
ntpath.basename(path)                    | Возвращает базовое имя файла или каталога из указанного пути.
ntpath.commonprefix(list)                | Возвращает наибольший общий префикс из списка путей.
ntpath.dirname(path)                     | Возвращает каталог, содержащий указанный путь.
ntpath.exists(path)                      | Проверяет, существует ли указанный путь.
ntpath.expanduser(path)                  | Заменяет в указанном пути тильду (~) на домашний каталог пользователя.
ntpath.expandvars(path)                  | Заменяет переменные окружения в указанном пути на их значения.
ntpath.isfile(path)                      | Проверяет, является ли указанный путь файлом.
ntpath.isdir(path)                       | Проверяет, является ли указанный путь каталогом.
ntpath.join(path, *paths)                | Объединяет пути с использованием разделителя.
ntpath.normpath(path)                    | Нормализует указанный путь, удаляя двойные слеши и точки.
ntpath.realpath(path)                    | Возвращает канонический абсолютный путь к указанному пути.
ntpath.relpath(path, start)              | Возвращает относительный путь от исходного пути до указанного пути.
ntpath.split(path)                       | Разделяет указанный путь на имя каталога и имя файла.

Несколько часто используемых методов "ntpath" с их кратким описанием и примерами кода:

Метод                                     | Описание                                | Пример
-----------------------------------------|-----------------------------------------|--------------------------------------------------
ntpath.basename(path)                     | Возвращает базовое имя файла или каталога из указанного пути. | dirname, filename = ntpath.split("/path/to/file.txt") print(filename) -> "file.txt"
ntpath.exists(path)                       | Проверяет, существует ли указанный путь. | if ntpath.exists("/path/to/file.txt"): print("File exists")
ntpath.join(path, *paths)                 | Объединяет пути с использованием разделителя. | full_path = ntpath.join("/path/to", "file.txt") print(full_path) -> "/path/to/file.txt"
""",
                    "locale": r"""
Библиотека "locale" в Python используется для обработки локализации и форматирования числовых,
датовых и строковых значений в соответствии с настройками локали операционной системы.

Таблица методов и их описания для модуля "locale" и его подмодулей:

Модуль "locale":
setlocale(category, locale=None): устанавливает текущую локаль для данной категории (категории определяют тип данных, например, числа, даты и др.).

Подмодуль "localeconv":
localeconv(): возвращает словарь с настройками форматирования чисел и валюты в текущей локали.

Наиболее часто используемые методы и их описание:

setlocale(category, locale=None): Этот метод позволяет установить локаль для определенной категории.
Например, setlocale(locale.LC_NUMERIC, "en_US") устанавливает локаль для чисел на английский (США).


```python
import locale

locale.setlocale(locale.LC_NUMERIC, "en_US")
formatted_number = locale.format_string("%.2f", 1234.5678)
print(formatted_number)
```
Результат: "1,234.57"

Помните, что информация о локализации и форматировании может отличаться в зависимости от операционной системы и языка установки Python.
""",
                    "gettext": r"""
Библиотека "gettext" в Python используется для локализации и перевода текстовых сообщений в программе.

# Таблица методов модуля "gettext" и его подмодулей
### Методы модуля "gettext"
bindtextdomain(domain, directory): устанавливает домен и директорию для поиска файлов перевода.
dgettext(domain, message): возвращает перевод сообщения из указанного домена.
dngettext(domain, singular, plural, n): возвращает перевод множественного сообщения на основе числа n.
gettext(message): возвращает перевод сообщения.
ngettext(singular, plural, n): возвращает перевод множественного сообщения на основе числа n.
textdomain(domain): устанавливает текущий домен перевода.

### Методы подмодуля "gettext.translation"
gettext.translation(domain, localedir=None, languages=None, fallback=False): создает объект перевода на основе заданного домена и директории локализации.
gettext.translation(""): возвращает объект перевода для текущего домена.
add_fallback(translations): добавляет объект перевода в список резервных вариантов перевода.
install(domain, localedir=None, unicode=0): устанавливает объект перевода в качестве текущего.

Самые часто используемые методы библиотеки "gettext" вместе с их кратким описанием и примером кода:

gettext(message): Возвращает перевод сообщения.

```python
import gettext
gettext.bindtextdomain("mydomain", "locale/")
gettext.textdomain("mydomain")

_ = gettext.gettext
print(_("Hello, world!"))
```

ngettext(singular, plural, n): Возвращает перевод множественного сообщения на основе числа n.

```python
import gettext
gettext.bindtextdomain("mydomain", "locale/")
gettext.textdomain("mydomain")

_ = gettext.ngettext
print(_("%d apple", "%d apples", 5) % 5)
```

dgettext(domain, message): Возвращает перевод сообщения из указанного домена.

```python
import gettext
gettext.bindtextdomain("mydomain", "locale/")
gettext.textdomain("mydomain")

_ = gettext.dgettext
print(_("mydomain", "Hello, world!"))
```
""",
                    "rfc3339_validator": r"""
Библиотека "rfc3339_validator" используется для проверки правильности формата даты и времени в соответствии со стандартом RFC 3339.

Таблица методов модуля и его подмодулей:

Метод `validate(date_string)` - проверяет правильность формата даты и времени в строке `date_string` в соответствии со стандартом RFC 3339.
Возвращает булевое значение True, если формат верен, и False в противном случае.

Список самых частых методов, их краткого описания и примерного кода:

Метод `validate(date_string)` - проверяет правильность формата даты и времени в строке `date_string` в соответствии со стандартом RFC 3339.

```python
from rfc3339_validator import validate

date_string = "2022-01-01T12:34:56Z"
if validate(date_string):
    print("Формат даты и времени верный")
else:
    print("Некорректный формат даты и времени")
```
""",
                    "netbios": r"""
"netbios" - это библиотека в Python, которая предоставляет функциональность
для работы с протоколом NetBIOS (Network Basic Input/Output System).

Таблица методов модуля "netbios" и их краткого описания:

Метод                  | Описание
-----------------------|----------------------------------------------------
nbt.getnetbiosname()   | Получает NetBIOS-имя компьютера, на котором выполняется код.
nbt.getwinsaddrs()     | Возвращает список IP-адресов машин, знающих сведения о NetBIOS-именах.
nbt.getnodetype()      | Возвращает тип узла в сети.
nbt.gethostbyname()    | Возвращает IP-адреса, связанные с указанным NetBIOS-именем.
nbt.getbcastaddrs()    | Возвращает список широковещательных адресов, связанных с NetBIOS-именами.

Список самых часто используемых методов, их краткого описания и

nbt.getnetbiosname(): Возвращает NetBIOS-имя компьютера.

```python
import netbios as nb

name = nb.getnetbiosname()
print(name)
```

nbt.getwinsaddrs(): Возвращает список IP-адресов машин, знающих сведения о NetBIOS-именах.

```python
import netbios as nb

wins_addrs = nb.getwinsaddrs()
print(wins_addrs)
```

nbt.getnodetype(): Возвращает тип узла в сети.

```python
import netbios as nb

node_type = nb.getnodetype()
print(node_type)
```
""",
                    "bz2": """
Модуль bz2 в Python предоставляет интерфейс для сжатия и распаковки данных
с использованием алгоритма BZ2 (Burrows-Wheeler).
Он позволяет работать с файлами и байтовыми объектами, обеспечивая эффективное сжатие данных.

| Метод                                                     | Описание                                                                           |
|-----------------------------------------------------------|------------------------------------------------------------------------------------|
| bz2.compress(data, compresslevel=9)                       | Сжимает данные BZ2. Можно указать уровень сжатия (1-9).                            |
| bz2.decompress(data)                                      | Распаковывает данные BZ2.                                                          |
| bz2.BZ2File(file, mode="r", buffering=0, compresslevel=9) | Создает файловый объект BZ2. Режимы: "r" (чтение), "w" (запись), "a" (добавление). |

**bz2.compress(data, compresslevel=9)** Сжимает данные BZ2.

```python
compressed_data = bz2.compress(b"Hello, World!")
print(compressed_data)
```

**bz2.decompress(data)** Распаковывает данные BZ2.

```python
decompressed_data = bz2.decompress(compressed_data)
print(decompressed_data)
```
""",
                },
            },
            "Methods": {
                "Magic methods": r"""
# Арифметические операции

| Функция                            | Пример                | Описание                                      |
|------------------------------------|-----------------------|-----------------------------------------------|
| `def __eq__(self, other) -> bool:` | self `==` other       | Равенство                                     |
| `def __ge__(self, other) -> bool:` | self `>=` other       | Больше или равен                              |
| `def __gt__(self, other) -> bool:` | self `>` other        | Больше                                        |
| `def __le__(self, other) -> bool:` | self `<=` other       | Mеньше или равен                              |
| `def __lt__(self, other) -> bool:` | self `<` other        | Меньше                                        |
| `def __ne__(self, other) -> bool:` | self `!=` other       | Не равен                                      |
| `def __or__(self, other):`         | self `|` other        | Побитовое **ИЛИ**                             |
| `def __add__(self, other):`        | self `+` other        | Сложение                                      |
| `def __and__(self, other):`        | self `&` other        | Побитовое **И**                               |
| `def __ior__(self, other):`        | self `|=` other       | Побитовое **ИЛИ** с присваиванием             |
| `def __mod__(self, other):`        | self `%` other        | Остаток от деления                            |
| `def __mul__(self, other):`        | self `*` other        | Умножение                                     |
| `def __ror__(self, other):`        | self `|` other        | Побитовое ИЛИ с обратным присваиванием        |
| `def __sub__(self, other):`        | self `-` other        | Вычитание                                     |
| `def __xor__(self, other):`        | self `^` other        | Побитовое **ИСКЛЮЧАЮЩЕЕ ИЛИ**                 |
| `def __iadd__(self, other):`       | self `+=` other       | Сложение с присваиванием                      |
| `def __iand__(self, other):`       | self `&=` other       | Побитовое **И** с присваиванием               |
| `def __idiv__(self, other):`       | self `/=` other       | Деление с присваиванием                       |
| `def __imod__(self, other):`       | self `%=` other       | Взятие остатка от деления с присваиванием     |
| `def __imul__(self, other):`       | self `*=` other       | Умножение с присваиванием                     |
| `def __ipow__(self, other):`       | self `**=` other      | Возведение в степень с присваиванием          |
| `def __isub__(self, other):`       | self `-=` other       | Вычитание с присваиванием                     |
| `def __ixor__(self, other):`       | self `^=` other       | Побитовое **ИСКЛЮЧАЮЩЕЕ ИЛИ** с присваиванием |
| `def __radd__(self, other):`       | other `+` self        | Сложение справа                               |
| `def __rand__(self, other):`       | other `&` self        | Выполняет побитовое **И** справа              |
| `def __rdiv__(self, other):`       | other `/` self        | Деление справа                                |
| `def __divmod__(self, other):`     | `divmod`(self, other) | Деление с остатком                            |
| `def __rdivmod__(self, other):`    | `divmod`(other, self) | Деление с остатком справа                     |
| `def __rmod__(self, other):`       | other `%` self        | Взятие остатка от деления справа              |
| `def __rmul__(self, other):`       | other `*` self        | Умножение справа                              |
| `def __rpow__(self, other):`       | other `**` self       | Возведение в степень справа                   |
| `def __rsub__(self, other):`       | other `-` self        | Вычитание справа                              |
| `def __rxor__(self, other):`       | other `^` self        | Побитовое **ИСКЛЮЧАЮЩЕЕ ИЛИ** справа          |
| `def __floordiv__(self, other):`   | self `//` other       | Целочисленное деление                         |
| `def __ilshift__(self, other):`    | self `<<=` other      | Побитовый сдвиг влево с присваиванием         |
| `def __imatmul__(self, other):`    | self `@=` other       | Матричное умножение с присваиванием           |
| `def __irshift__(self, other):`    | self `>>=` other      | Побитовый сдвиг вправо с присваиванием        |
| `def __itruediv__(self, other):`   | self `/=` other       | Деление с присваиванием                       |
| `def __rlshift__(self, other):`    | other `<<` self       | Побитовый сдвиг влево справа                  |
| `def __rmatmul__(self, other):`    | other `@` self        | Матричное умножение справа                    |
| `def __matmul__(self, other):`     | self `@` other        | Матричное умножение                           |
| `def __rrshift__(self, other):`    | other `>>` self       | Побитовый сдвиг вправо справа                 |
| `def __rtruediv__(self, other):`   | other `/` self        | Деление справа                                |
| `def __truediv__(self, other):`    | self `/` other        | Деление                                       |
| `def __lshift__(self, other):`     | self `<<` other       | Побитовый сдвиг влево                         |
| `def __rshift__(self, other):`     | self `>>` other       | Побитовый сдвиг вправо                        |
| `def __ifloordiv__(self, other):`  | self `//=` other      | Целочисленное деление с присваиванием         |
| `def __rfloordiv__(self, other):`  | other `//` self       | Целочисленное деление справа                  |
| `def __pos__(self):`               | `+`self               | Положительное значение объекта                |
| `def __neg__(self):`               | `-`self               | Отрицательное значение объекта                |
| `def __invert__(self):`            | `~`self               | Инвертированное значение объекта              |

# func call

| Функция                                          | Пример                          | Описание                                                                           |
|--------------------------------------------------|---------------------------------|------------------------------------------------------------------------------------|
| `def __pow__(self, power, modulo=None):`         | `pow`(self, power, modulo)      | Возведение в степень                                                               |
| `def __abs__(self):`                             | `abs`(self)                     | Абсолютное значение объекта                                                        |
| `def __hex__(self):`                             | `hex`(self)                     | Строковое представление объекта в<br>шестнадцатеричной системе счисления           |
| `def __float__(self):`                           | `float`(self)                   | Представление объекта в виде числа с плавающей запятой                             |
| `def __bytes__(self):`                           | `bytes`(self)                   | Байтовое представление объекта                                                     |
| `def __long__(self):`                            | `int`(self)                     | Длинное целочисленное представление объекта                                        |
| `def __int__(self):`                             | `int`(self)                     | Целочисленное представление объекта                                                |
| `def __bool__(self) -> bool:`                    | `bool`(self)                    | Булево значение                                                                    |
| `def __oct__(self):`                             | `oct`(self)                     | Строковое представление объекта в<br>восьмеричной системе счисления                |
| `def __len__(self):`                             | `len`(self)                     | Возвращает длину объекта                                                           |
| `def __str__(self):`                             | `str`(self)                     | Строковое представление объекта                                                    |
| `def __hash__(self):`                            | `hash`(self)                    | Хеш-значение объекта                                                               |
| `def __iter__(self):`                            | `iter`(self)                    | Итератор объекта                                                                   |
| `def __next__(self):`                            | `next`(self)                    | Следующий элемент в итерации                                                       |
| `def __round__(self, n=None):`                   | `round`(self, n)                | Округленное значение                                                               |
| `def __complex__(self):`                         | `complex`(self)                 | Комплексное представление                                                          |
| `def __reversed__(self):`                        | `reversed`(self)                | Возвращает обратный итератор объекта                                               |
| `def __unicode__(self):`                         | `unicode`(self)                 | Строковое представление объекта (`Python 2`)                                       |
| `def __instancecheck__(self, instance) -> bool:` | `isinstance`(obj, cls)          | Проверяет, является ли объект экземпляром класса                                   |
| `def __subclasscheck__(self, subclass) -> bool:` | `issubclass`(subclass, cls)     | Является ли класс подклассом другого класса                                        |
| `def __call__(self, *args, **kwargs):`           | `self(*args, **kwargs)`         | Вызывает объект как функцию                                                        |
| `def __repr__(self):`                            | `repr`(self)                    | Строковое представление объекта                                                    |
| `def __subclasshook__(cls, __subclass):`         | `issubclass`(Subclass, MyClass) | Проверяет, является ли класс подклассом другого класса                             |
| `def __dir__(self):`                             | `dir`(self)                     | Список атрибутов и методов объекта                                                 |
| `def __format__(self, format_spec):`             | {__format__}                    | Форматированную строку объекта                                                     |
| `def __cmp__(self, other) -> int:`               | `cmp`(self, other)              | Сравнивает объекты и возвращает `-1`, `0` или `1`                                  |
| `def __aiter__(self):`                           | `aiter`(self)                   | Асинхронный итератор объекта                                                       |
| `def __anext__(self):`                           | `anext`(self)                   | Возвращает следующий элемент в асинхронной итерации                                |
| `def __coerce__(self, other):`                   | `coerce`(self, other)           | Преобразует объект к общему типу с другим объектом                                 |
| `def __index__(self):`                           | `operator.index`(self)          | Целочисленное представление объекта<br>для использования в индексации              |
| `def __floor__(self):`                           | `math.floor`(self)              | Наибольшее целое число, меньшее или равное объекту                                 |
| `def __trunc__(self):`                           | `math.trunc`(self)              | Усеченное значение объекта                                                         |
| `def __ceil__(self):`                            | `math.ceil`(self)               | Наименьшее целое число, большее или равное объекту                                 |
| `def __copy__(self):`                            | `copy.copy`(self)               | Создает поверхностную копию объекта                                                |
| `def __deepcopy__(self, memodict={{}}):`         | `copy.deepcopy`(self)           | Создает глубокую копию объекта                                                     |
| `def __sizeof__(self):`                          | `sys.getsizeof`(self)           | Возвращает размер объекта в байтах                                                 |
| `def __fspath__(self):`                          | `os.fspath`(self)               | Возвращает строковое представление<br>объекта для использования в функции `fspath` |

# Контейнеры

| Функция                                   | Пример                                  | Описание                                                  |
|-------------------------------------------|-----------------------------------------|-----------------------------------------------------------|
| `def __getitem__(self, item):`            | self[item]                              | Элемент по индексу или ключу                              |
| `def __missing__(self, key):`             | self[key]                               | Вызывается при отсутствии ключа в объекте                 |
| `def __contains__(self, item) -> bool:`   | item `in` self                          | Содержится ли элемент в объекте                           |
| `def __setslice__(self, i, j, sequence):` | self[i:j] = sequence                    | Заменяет срез объекта указанной последовательностью       |
| `def __delattr__(self, item):`            | `del` self.item                         | Удаляет атрибут объекта                                   |
| `def __delitem__(self, key):`             | `del` self[key]                         | Удаляет элемент по ключу                                  |
| `def __delslice__(self, i, j):`           | `del` self[i:j]                         | Удаляет срез из объекта                                   |
| `def __get__(self, instance, owner):`     | value = self.`__get__`(instance, owner) | Возвращает значение атрибута объекта в классе-дескрипторе |

# Классы

| Функция                                 | Пример                                               | Описание                                                                         |
|-----------------------------------------|------------------------------------------------------|----------------------------------------------------------------------------------|
| `def __new__(cls, *args, **kwargs):`    | instance = MyClass(args)                             | Создает новый обьект                                                             |
| `def __init__(self):`                   | instance = MyClass(args)                             | При инициализации нового экземпляра объекта                                      |
| `def __class__(self):`                  | obj_class = obj.`__class__()`                        | Возвращает класс объекта                                                         |
| `def __del__(self):`                    | `del` self                                           | При удалении объекта                                                             |
| {__prepare__}                           | metacls.`__prepare__`(name, bases)<br><details><summary>Example</summary>{__prepare___example}</details>                   | Словарь для использования в качестве<br>пространства имен класса перед его созданием<br>Например для добавления специфической<br>логики при добавлении новых атрибутов |
| `def __delete__(self, instance):`       | `del` instance.self                                  | Удаляет атрибут объекта                                                          |
| `def __init_subclass__(cls, **kwargs):` | {__init_subclass__}                                  | Вызывается при создании подкласса                                                |
| `def __mro_entries__(self, bases):`     | {__mro_entries__}                                    | Возвращает кортеж для обновления `MRO`<br>(Method Resolution Order)              |
| `def __getinitargs__(self):`            | args = self.`__getinitargs__()`                      | Кортеж аргументов для использования при создании объекта                         |
| `def __set_name__(self, owner, name):`  | {__set_name__}                                       | Вызывается при установке имени атрибута в классе                                 |
| `def __getnewargs__(self):`             | args = self.`__getnewargs__()`                       | Возвращает аргументы для использования<br>при создании нового экземпляра объекта |
| `def __getattribute__(self, item):`     | value = self.`__getattribute__`("attr")              | Возвращает значение атрибута объекта<br>**Управляет всеми запросами атрибутов**  |
| `def __getattr__(self, item):`          | value = self.`__getattr__`("attr")                   | Вызывается при обращении<br>к несуществующему атрибуту объекта<br>**Когда `__getattribute__` не находит атрибут** |
| `def __await__(self):`                  | `await` self                                         | Возвращает объект, поддерживающий асинхронное ожидание                           |
| `def __set__(self, instance, value):`   | instance.attr = value                                | Устанавливает значение атрибута в экземпляре класса                              |
| `def __class_getitem__(cls, item):`     | item_type = MyGenericClass.`__class_getitem__`(Item) | Обобщенный тип объекта                                                           |
| `def __setattr__(self, key, value):`    | self.key = value                                     | Устанавливает значение атрибута объекта                                          |
| `def __setitem__(self, key, value):`    | self[key] = value                                    | Устанавливает значение элемента по ключу в объекте                               |

# with as

| Функция                                           | Пример                  | Описание                                                 |
|---------------------------------------------------|-------------------------|----------------------------------------------------------|
| `def __enter__(self):`                            | `with self as x:`       | Выполняет код при входе в блок `with`                    |
| `def __aenter__(self):`                           | `async with self as x:` | Вызывается при входе в асинхронный<br>контекстный блок   |
| `def __aexit__(self, exc_type, exc_val, exc_tb):` | {__aexit__}             | Вызывается при выходе из асинхронного контекстного блока | 
| `def __exit__(self, exc_type, exc_val, exc_tb):`  | {__exit__}              | Вызывается при выходе из контекстного блока              |

# Pickle

| Функция                              | Пример                                            | Описание                                                                            |
|--------------------------------------|---------------------------------------------------|-------------------------------------------------------------------------------------|
| `def __setstate__(self, state):`     | obj.`__setstate__`(state)                         | Восстанавливает состояние объекта                                                   |
| `def __reduce_ex__(self, protocol):` | `pickle.loads(pickle.dumps(self, protocol))`      | Возвращает данные для использования в процессе<br>сериализации объекта с протоколом |
| `def __getstate__(self):`            | `pickle.loads(pickle.dumps(self).__getstate__())` | Возвращает состояние объекта для использования<br>в процессе сериализации           |
| `def __reduce__(self):`              | `pickle.loads(pickle.dumps(self))`                | Возвращает данные для использования<br>в процессе сериализации объекта              |


# Примеры

## \_\_class_getitem\_\_ 

Появился в версии 3.7 и используется в основном для поддержки аннотаций типов и работы с обобщёнными типами `generics`.
Этот метод срабатывает, когда класс вызывается с использованием синтаксиса индексации `[]`.

### Обобщённые классы (Generics)
```python
class MyClass:
    def __class_getitem__(cls, item):
        print(f"Класс вызван с параметром: {{item}}")
        return cls

MyClass[int]
```

### Пример для создания обобщённых классов
`__class_getitem__` часто используется в таких библиотеках,
как `typing`, для создания обобщённых `generics` классов.

#### Пример реализации собственного Generic-класса:

```python
class MyGeneric:
    def __class_getitem__(cls, item):
        return f"{{cls.__name__}}[{{item.__name__}}]"

print(MyGeneric[int])  # MyGeneric[int]
print(MyGeneric[str])  # MyGeneric[str]
```

### Зачем нужен `__class_getitem__`?

1. **Работа с аннотациями типов.** Он упрощает создание обобщённых классов, таких как `List[int]`
или `Dict[str, int]`, поддерживая работу с типами в библиотеках, связанных с проверкой типов.
2. **Интерфейсы для собственных классов.** Если вы создаёте классы, которые должны поддерживать функциональность,
связанную с типами или шаблонами, метод `__class_getitem__` позволит вам реализовать подобную логику.
3. **Гибкость.** Он позволяет передавать классу параметры,
которые могут управлять тем, как класс себя ведёт или что возвращает.

`__class_getitem__` может работать в связке с другими магическими методами для более сложных конструкций.
Например, его можно использовать вместе с методами `__getitem__`, `__setitem__`
для создания классов, которые поддерживают индексацию и динамическое изменение поведения.

Магический метод `__class_getitem__` — это мощный инструмент для работы с обобщёнными типами и аннотациями.
С его помощью можно реализовывать гибкие и типизированные API,
которые позволяют делать код более понятным и удобным для сопровождения.
""".format(
                    __format__=to_table_code_py('"{0:{format_spec}}".format(self)'),
                    __prepare__=to_table_code_py(
                        """
class MyMeta(type):
    @classmethod
    def __prepare__(metacls, name, bases):
        return {}
""",
                    ).replace("__", "&#95;&#95;"),
                    __prepare___example=to_table_code_py(
                       '''
class CustomDict(dict):
    def __setitem__(self, key, value):
        print(f"{key!r} = {value!r}")
        super().__setitem__(key, value)

class CustomMeta(type):
    @classmethod
    def __prepare__(metacls, name, bases, custom_dict=CustomDict):
        return custom_dict()

class MyClass(metaclass=CustomMeta):
    x = 10
    y = 20


"""
"__module__" = "__main__"
"__qualname__" = "MyClass"
"x" = 10
"y" = 20
"""
'''.strip()
                    ).replace("__", "&#95;&#95;"),
                    __init_subclass__=to_table_code_py(
                        "class Subclass(Parent):\n"
                        "    pass\n"
                        "Subclass.__init_subclass__()"
                    ).replace("__", "&#95;&#95;"),
                    __mro_entries__=to_table_code_py(
                        "class MyClass(Base1, Base2, metaclass=MyMeta):\n"
                        "    pass\n"
                        "MyClass.__mro_entries__(bases)"
                    ).replace("__", "&#95;&#95;"),
                    __set_name__=to_table_code_py(
                        "class MyClass:\n"
                        "    attr = MyDescriptor()\n"
                        'MyClass.attr.__set_name__(MyClass, "attr")'
                    ).replace("__", "&#95;&#95;"),
                    __aexit__=to_table_code_py(
                        "async with self as x:\n"
                        "    pass\n"
                        "await self.__aexit__(exc_type, exc_val, exc_tb)"
                    ).replace("__", "&#95;&#95;"),
                    __exit__=to_table_code_py(
                        "with self as x:\n"
                        "    pass\n"
                        "self.__exit__(exc_type, exc_val, exc_tb)"
                    ).replace("__", "&#95;&#95;"),
                ),
                "Magic attributes": """
| Атрибут           | Описание                                                                                                      | Пример использования                                |
|-------------------|--------------------------------------------------------------------------------------------------------------|----------------------------------------------------|
| `__code__`        | Содержит объект типа `code`, представляющий байт-код функции.<br>Можно использовать для анализа и изменения.     | `func.__code__.co_varnames`                        |
| `__closure__`     | Кортеж объектов `cell`, хранящих значения переменных,<br>захваченных замыканием (если функция использует замыкания). | `func.__closure__[0].cell_contents`               |
| `__module__`      | Имя модуля, в котором определена функция.<br>Полезно для понимания контекста определения функции.                | `func.__module__`                                  |
| `__annotations__` | Словарь с аннотациями типов для аргументов функции и возвращаемого значения.                                | `func.__annotations__`                             |
| `__globals__`     | Словарь глобальных переменных, доступных функции.<br>Позволяет доступ к глобальному пространству имен.<br>Если функция func была определена в модуле module,<br>то `func.__globals__` будет ссылаться<br>на глобальный символический словарь этого модуля.           | `func.__globals__['variable_name']`                |
| `__defaults__`    | Кортеж значений по умолчанию для позиционных<br>и именованных аргументов функции (если они определены).          | `func.__defaults__`                                |
| `__kwdefaults__`  | Словарь значений по умолчанию для только ключевых аргументов функции (если они определены).                  | `func.__kwdefaults__`                              |
| `__qualname__`    | Полное имя функции, включая контексты, такие как класс или модуль, в котором она определена.                  | `func.__qualname__`                                |


# &#x5f;&#x5f;code&#x5f;&#x5f;

| Атрибут              | Описание                                                                                                                                                                                            | Пример использования                 |
|----------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------|
| `co_argcount`        | Количество аргументов, принимаемых функцией (без `*args` и `**kwargs`).                                                                                                                             | `func.__code__.co_argcount`          |
| `co_cellvars`        | Кортеж с именами переменных, которые являются локальными, но используются в замыканиях.                                                                                                             | `func.__code__.co_cellvars`          |
| `co_code`            | Сырые байт-коды, представляющие тело функции.                                                                                                                                                       | `func.__code__.co_code`              |
| `co_consts`          | Кортеж с константами, используемыми в функции (например, числа, строки).                                                                                                                            | `func.__code__.co_consts`            |
| `co_exceptiontable`  | Таблица, описывающая обработку исключений в байт-коде.<br>Содержит информацию о try/except блоках и местах, где нужно ловить исключения.                                                            | `func.__code__.co_exceptiontable`    |
| `co_filename`        | Имя файла, в котором определена функция.                                                                                                                                                            | `func.__code__.co_filename`          |
| `co_firstlineno`     | Номер первой строки, содержащей исходный код функции.                                                                                                                                               | `func.__code__.co_firstlineno`       |
| `co_flags`           | Флаги, описывающие состояние функции (например, использование генераторов).                                                                                                                         | `func.__code__.co_flags`             |
| `co_freevars`        | Кортеж с именами переменных, которые используются в функции,<br>но не являются локальными (замыкания).                                                                                              | `func.__code__.co_freevars`          |
| `co_kwonlyargcount`  | Количество ключевых-only аргументов.                                                                                                                                                                | `func.__code__.co_kwonlyargcount`    |
| `co_lines`           | Итератор, который возвращает пары `(начало строки, конец строки)`<br>для каждого блока байт-кода, позволяя точно определить,<br>какая часть кода соответствует определенным строкам исходного кода. | `list(func.__code__.co_lines())`     |
| `co_linetable`       | Байт-код таблицы, содержащей информацию о соответствии номеров строк исходному коду<br>(используется в интерпретаторе Python для трассировки).                                                      | `func.__code__.co_linetable`         |
| `co_lnotab`          | Содержит информацию для отображения байт-кодов в номера строк исходного кода.                                                                                                                       | `func.__code__.co_lnotab`            |
| `co_name`            | Имя функции.                                                                                                                                                                                        | `func.__code__.co_name`              |
| `co_names`           | Кортеж с именами всех объектов (функций, классов, переменных), используемых в функции.                                                                                                              | `func.__code__.co_names`             |
| `co_nlocals`         | Количество локальных переменных, используемых в функции.                                                                                                                                            | `func.__code__.co_nlocals`           |
| `co_positions`       | Итератор, возвращающий позиции в коде: `(start_line, start_col, end_line, end_col)`<br>для каждого выражения или инструкции в функции.<br>Это позволяет точно определить позиции в исходном коде.   | `list(func.__code__.co_positions())` |
| `co_posonlyargcount` | Количество позиционных-only аргументов.                                                                                                                                                             | `func.__code__.co_posonlyargcount`   |
| `co_qualname`        | Полное имя функции, включая контексты, такие как класс или модуль.<br>Полезно для определения квалифицированного имени метода класса или вложенной функции.                                         | `func.__code__.co_qualname`          |
| `co_stacksize`       | Размер стека, необходимый для выполнения функции.                                                                                                                                                   | `func.__code__.co_stacksize`         |
| `co_varnames`        | Кортеж с именами всех локальных переменных, включая аргументы функции.                                                                                                                              | `func.__code__.co_varnames`          |
| `replace`            | Позволяет создать новый объект code, заменив выбранные атрибуты                                                                                                                                     | `func.__code__.replace(**kwargs)`    |

### Примеры использования

#### Получение количества аргументов функции
```python
def example_func(a, b, c=10):
    return a + b + c

print(example_func.__code__.co_argcount)  # 2
```

#### Извлечение имен аргументов и локальных переменных
```python
def example_func(x, y):
    z = x + y
    return z

print(example_func.__code__.co_varnames)  # ("x", "y", "z")
```

#### Получение имени файла и строки, где определена функция
```python
def example_func():
    pass

print(example_func.__code__.co_filename)     # Имя файла, в котором определена функция
print(example_func.__code__.co_firstlineno)  # Номер первой строки
```

#### Работа с байт-кодом
```python
def example_func(a, b):
    return a + b

print(example_func.__code__.co_code)  # Сырые байт-коды
```

#### Константы, используемые в функции
```python
def example_func():
    x = 42
    return x

print(example_func.__code__.co_consts)  # (None, 42)
```

#### Проверка использования замыканий
```python
def outer_func(x):
    def inner_func(y):
        return x + y
    return inner_func

closure_func = outer_func(10)
print(closure_func.__code__.co_freevars)  # ("x",)
print(closure_func.__code__.co_cellvars)  # ()
```

### Дополнительные материалы

- `co_flags`: Этот атрибут — битовая маска, содержащая информацию о функции,
например, используется ли функция как генератор, имеет ли она `*args` или `**kwargs` и т.д.
    - Например, `0x20` указывает, что функция — генератор.
  
- `co_lnotab`: Содержит байтовую строку, которая используется для отображения байт-кодов в номера строк исходного кода.
Эта информация полезна при отладке и генерации трассировки стека.

""",
                "str": """
| Метод                                  | Описание                                                                                                           |                |
|:---------------------------------------|:-------------------------------------------------------------------------------------------------------------------|----------------|
| str.capitalize()                       | Переводит первую букву в верхний, а остальные в нижний регистр.                                                    | {capitalize}   |
| str.casefold()                         | Переводит все символы в нижний регистр                                                                             | {casefold}     |
| str.lower()                            | Переводит символы строки в нижний регистр                                                                          | {lower}        |
| str.upper()                            | Возвращает копию строки в верхнем регистре                                                                         | {upper}        |
| str.swapcase()                         | Меняет регистр всех символов на противоположный                                                                    | {swapcase}     |
| str.title()                            | Возвращает строку, где все слова начинаются с заглавной буквы,<br>а продолжаются строчными                         | {title}        |
| str.isupper()                          | `True`, если строка в верхнем регистре                                                                             | {isupper}      |
| str.islower()                          | `True`, если вся строка в нижнем регистре                                                                          | {islower}      |
| str.center(width[, fillvalue])         | Обрамляет значениями `fillvalue` строку,<br>пока длина не станет `width`                                           | {center}       |
| str.ljust(width, fillchar=" ")         | Добавляет в конец строки символ `fillchar`,<br>пока длина не станет `width`                                        | {ljust}        |
| str.rjust(width, fillchar=" ")         | Добавляет в начало строки символ `fillchar`,<br>пока длина не станет `width`                                       | {rjust}        |
| str.count(str[, start][, end]          | Считает количество подстрок `str` в выбранном промежутке строки                                                    | {count}        |
| str.encode(encoding, errors)           | Меняет кодировку строки                                                                                            | {encode}       |
| str.startswith(prefix[, start[, end]]) | `True` если строка начинается с `prefix`                                                                           | {startswith}   |
| str.endswith(suffix[, start[, end]])   | `True` если строка заканчивается на `suffix`                                                                       | {endswith}     |
| str.removeprefix(prefix: str)          | Возвращает строку без прификса `prefix`                                                                            | {removeprefix} |
| str.removesuffix(suffix: str)          | Возвращает строку без суффикса `suffix`                                                                            | {removesuffix} |
| str.expandtabs(tabsize=8)              | Увеличивает размер символов табуляции до `tabsize` пробелов                                                        | {expandtabs}   |
| str.index(str[, start[, end]])         | Возвращает индекс начала первой подстроки `str`<br>в выбранном промежутке или `ValueError`, если она не найдена    | {index}        |
| str.rindex(str[, start[, end]])        | Возвращает индекс начала последней подстроки `str`<br>в выбранном промежутке или `ValueError`, если она не найдена | {rindex}       |
| str.find(str[, start[, end]])          | Возвращает индекс начала первой подстроки `str`<br>в выбранном промежутке или `-1`, если она не найдена            | {find}         |
| str.rfind(str[, start[, end]])         | Возвращает индекс начала последней подстроки `str`<br>в выбранном промежутке или `-1`, если она не найдена         | {rfind}        |
| str.format(args, *kwargs)              | Последовательно заменяет `{{}}` в строке на свои аргументы                                                         | {format}       |
| str.format_map(dict)                   | Заменяет `{{<val>}}` в строке на `dict[<val>]`                                                                     | {format_map}   |
| str.join(iter)                         | Склеивает элементы последовательности `iter`<br>в одну строку с разделителем `str`                                 | {join}         |
| str.strip([chars])                     | Возвращает строку без пробельных символов<br>или `chars` в начале и конце                                          | {strip}        |
| str.lstrip([chars])                    | Возвращает строку без пробельных символов или `chars` в начале                                                     | {lstrip}       |
| str.rstrip([chars])                    | Возвращает строку без пробельных символов или `chars` в конце                                                      | {rstrip}       |
| str.replace(old, new)                  | Заменяет все подстроки `old` на `new`                                                                              | {replace}      |
| str.split(sep=" ", maxsplit=-1)        | Возвращает список подстрок,<br>разделенных по `sep` до `maxsplit` раз                                              | {split}        |
| str.splitlines(keepends=False)         | Разделяет строку по `\\n`.<br>Не удаляет разделители, если `keepends=True`.                                        | {splitlines}   |
| str.rsplit(sep=" ", maxsplit=-1)       | Возвращает список подстрок,<br>разделенных по sep до `maxsplit` раз (с конца)                                      | {rsplit}       |
| str.zfill(width)                       | Заполняет строку указанным числом нулей в начале                                                                   | {zfill}        |
| str.maketrans(*args)                   | Возвращает таблицу перевода для `s.translate`                                                                      | {maketrans}    |
| str.translate(table)                   | Заменяет все символы строки согласно таблице перевода                                                              | {translate}    |
| str.partition(sep)                     | Разделяет строку на три части по первому разделителю `sep`:<br>[начало, sep, конец]                                | {partition}    |
| str.rpartition()                       | Разделяет строку на три части по последнему разделителю `sep`:<br>[начало, sep, конец]                             | {rpartition}   |
| str.isalnum()                          | `True`, если строка состоит только из букв и цифр                                                                  | {isalnum}      |
| str.isalpha()                          | `True`, если строка состоит только из букв                                                                         | {isalpha}      |
| str.isdecimal()                        | `True`, если строка состоит только из цифр                                                                         | {isdecimal}    |
| str.isidentifier()                     | `True`, если строка является идентификатором<br>(`if`, `class`, `assert`)                                          | {isidentifier} |
| str.isnumeric()                        | `True`, если строка состоит только из цифр                                                                         | {isnumeric}    |
| str.isprintable()                      | `True`, если все символы строки отображаются<br>(например, `\\n`, `\\t`)                                           | {isprintable}  |
| str.isspace()                          | `True`, если строка состоит из пробелов                                                                            | {isspace}      |
| str.istitle()                          | `True`, если строка начинается с заглавной буквы,<br>а остальные — строчные                                        | {istitle}      |
| str.isascii()                          | Проверяет, состоит ли строка только из ASCII символов                                                              | {isascii}      |
| str.isdigit()                          | Проверяет, состоит ли строка только из цифр (0-9)                                                                  | {isdigit}      |

**Символы**

| Символ      | Назначение                    | Пример                 | Результат |
|:------------|:------------------------------|:-----------------------|:----------|
| `\\n`       | Перевод строки                | `"ab\\ncd"`            | ab<br>cd  |
| `\\`        | Экранирование                 | `"ab\\ncd"`            | ab\\ncd   |
| `\\a`       | Звонок                        | `"a\\aa"`              | a[BEL]a   |
| `\\b`       | Забой                         | `"ab\\ba"`             | ac        |
| `\\f`       | Перевод страницы              | `"a\\fa"`              | a[FF]a    |
| `\\r`       | Возврат каретки               | `"ab\\rcd"`            | cd        |
| `\\t`       | Горизонтальная табуляция      | `"a\\ta"`              | a a       |
| `\\v`       | Вертикальная табуляция        | `"a\\va"`              | a[VT]a    |
| `\\N{{id}}` | Символ Юникода по id          | `"\\N{{Degree Sign}}"` | °         |
| `\\uhhhh`   | 16-ричный символ Юникода      | `"\\u2030"`            | ‰         |
| `\\Uhhhh`   | 32-ичный символ Юникода       | `"\\U00000394"`        | Δ         |
| `\\xhh`     | 16-ричное значение символа    | `"\\x2A"`              | *         |
| `\\ooo`     | восьмеричное значение символа | `"\\275"`              | ½         |
| `\\0`       | символ Null                   | `"\\0"`                |           |
| `\\u00A0`   | символ неразнывного пробела   |                        |           |
""".format(
                    capitalize=to_table_code_py(
                        '>>> "capitalize".capitalize()\n"Capitalize"'
                    ),
                    casefold=to_table_code_py('>>> "CaSeFoLd".casefold()\n"casefold"'),
                    lower=to_table_code_py('>>> "lOwEr".lower()\n"lower"'),
                    upper=to_table_code_py('>>> "upper".upper()\n"UPPER"'),
                    swapcase=to_table_code_py('>>> "sWaPcAsE".swapcase()\n"SwApCaSe"'),
                    title=to_table_code_py('>>> "title title".title()\n"Title Title"'),
                    isupper=to_table_code_py(
                        '>>> "A".isupper()\nTrue\n>>> "a".isupper()\nFalse'
                    ),
                    islower=to_table_code_py(
                        '>>> "a".islower()\nTrue\n"A".islower()\nFalse'
                    ),
                    center=to_table_code_py('>>> "0".center(5, "_")\n"\\_\\_0\\_\\_"'),
                    ljust=to_table_code_py('>>> "1".ljust(5, "_")\n"1____"'),
                    rjust=to_table_code_py('>>> "1".rjust(5, "_")\n"____1"'),
                    count=to_table_code_py('>>> "12123412".count("12")\n3'),
                    encode=to_table_code_py('>>> "qwerty123".encode()\nb"qwerty123"'),
                    startswith=to_table_code_py(
                        '>>> "1234".startswith("34")\nFalse\n'
                        '>>> "1234".startswith("12")\nTrue\n'
                        '>>> "1234".startswith(("12", "89"))\nTrue'
                    ),
                    endswith=to_table_code_py(
                        '>>> "1234".endswith("12")\nFalse\n'
                        '>>> "1234".endswith("34")\nTrue\n'
                        '>>> "1234".endswith(("34", "56"))\nTrue'
                    ),
                    removeprefix=to_table_code_py('>>> "123".removeprefix("1")\n"23"'),
                    removesuffix=to_table_code_py('>>> "123".removesuffix("3")\n"12"'),
                    expandtabs=to_table_code_py('>>> "\t".expandtabs(8)\n"        "'),
                    index=to_table_code_py('>>> "1234".index("2")\n1'),
                    rindex=to_table_code_py('>>> "123427".rindex("2")\n4'),
                    find=to_table_code_py('>>> "1234".find("2")\n1'),
                    rfind=to_table_code_py('>>> "123427".rfind("2")\n4'),
                    format=to_table_code_py(
                        '>>> "{}".format("1")\n"1"\n>>> "{a}".format(a="1")\n"1"'
                    ),
                    format_map=to_table_code_py(
                        '>>> "{x} {y}".format_map(\n...     {"x": 4, "y": -5}\n... )\n"4 -5"'
                    ),
                    join=to_table_code_py('>>> " ".join(("1", "2"))\n"1 2"'),
                    strip=to_table_code_py('>>> "   1 3\t".strip()\n"1 3"'),
                    lstrip=to_table_code_py('>>> "   1 3\t".lstrip()\n"1 3\t"'),
                    rstrip=to_table_code_py('>>> "   1 3\t".rstrip()\n"   1 3"'),
                    replace=to_table_code_py(
                        '>>> "1231".replace("1", "_")\n"\\_23\\_"'
                    ),
                    split=to_table_code_py('>>> "1 3".split()\n["1", "3"]'),
                    splitlines=to_table_code_py(
                        '>>> "1 3\\n4".splitlines()\n["1 3", "4"]'
                    ),
                    rsplit=to_table_code_py('>>> "1 3".split()\n["1", "3"]'),
                    zfill=to_table_code_py('>>> "1".zfill(5)\n"00001"'),
                    maketrans="",
                    translate="",
                    partition="",
                    rpartition="",
                    isalnum="",
                    isalpha="",
                    isdecimal="",
                    isidentifier="",
                    isnumeric="",
                    isprintable="",
                    isspace=to_table_code_py(
                        '>>> " \t".isspace()\nTrue\n>>> "a".isspace()\nFalse'
                    ),
                    istitle=to_table_code_py(
                        '>>> "Aa".istitle()\nTrue\n'
                        '>>> "aA".istitle()\nFalse\n'
                        '>>> "Aa1 ".istitle()\nTrue'
                    ),
                    isascii=to_table_code_py(
                        '>>> # Состоит только из ASCII\n>>> "Hello, World!".isascii()\nTrue\n'
                        '>>> # Состоит не из ASCII\n>>> "Привет, мир!".isascii()\nFalse\n'
                        '>>> # Не содержит не-ASCII\n>>> "".isascii()\nTrue'
                    ),
                    isdigit=to_table_code_py(
                        '>>> "12345".isdigit()\nTrue\n'
                        '>>> "abc123".isdigit()\nFalse\n'
                        '>>> "123 456".isdigit()\nFalse\n'
                        '>>> "123.45".isdigit()\nFalse\n'
                        '>>> "+123".isdigit()\nFalse\n'
                        '>>> "-123".isdigit()\nFalse'
                    ),
                ),
                "int": r"""
| Метод                  | Описание                                                                                             | Пример вызова      |
|:-----------------------|:-----------------------------------------------------------------------------------------------------|:-------------------|
| int.as_integer_ratio() | Возвращает кортеж, представляющий рациональное число,<br>близкое к данному целому числу.             | {as_integer_ratio} |
| int.bit_count()        | Возвращает количество установленных битов (битов со значением 1)<br>в двоичном представлении числа.  | {bit_count}        |
| int.bit_length()       | Возвращает количество битов, необходимых для представления числа в двоичном виде.                    | {bit_length}       |
| int.conjugate()        | Возвращает сопряженное комплексное число.                                                            | {conjugate}        |
| int.denominator        | Возвращает знаменатель числа в виде рациональной дроби.                                              | {denominator}      |
| int.from_bytes()       | Преобразует байтовую последовательность в целое число,<br>используя указанный порядок байтов и знак. | {from_bytes}       |
| int.imag               | Возвращает мнимую часть комплексного числа.                                                          | {imag}             |
| int.numerator          | Возвращает числитель числа в виде рациональной дроби.                                                | {numerator}        |
| int.real               | Возвращает действительную часть комплексного числа.                                                  | {real}             |
| int.to_bytes()         | Преобразует целое число в байтовую последовательность,<br>используя указанный порядок байтов и знак. | {to_bytes}         |
""".format(
                    as_integer_ratio=to_table_code_py(">>> (10).as_integer_ratio()\n(10, 1)"),
                    bit_count=to_table_code_py(">>> (123).bit_count()\n6"),
                    bit_length=to_table_code_py(">>> (256).bit_length()\n9"),
                    conjugate=to_table_code_py(">>> (3 + 4j).conjugate()\n(3-4j)"),
                    denominator=to_table_code_py(">>> (3).denominator\n1"),
                    from_bytes=to_table_code_py(
                        '>>> int.from_bytes(\n...     b"\\x00\\x10",\n...     byteorder="big",\n...     signed=False'
                        '\n... )\n16'
                    ),
                    imag=to_table_code_py(">>> (3 + 4j).imag\n4.0"),
                    numerator=to_table_code_py(">>> (3).numerator\n3"),
                    real=to_table_code_py(">>> (3 + 4j).real\n3.0"),
                    to_bytes=to_table_code_py(
                        '>>> (1024).to_bytes(\n...     length=2,\n...     byteorder="big",\n...     signed=False\n... )'
                        '\nb"\\x04\\x00"'
                    ),
                ),
                "float": """
| Метод                  | Описание                                                                                 | Пример вызова      |
|------------------------|------------------------------------------------------------------------------------------|--------------------|
| float.as_integer_ratio | Возвращает кортеж, представляющий рациональное число,<br>близкое к данному целому числу. | {as_integer_ratio} |
| float.conjugate        | Возвращает сопряженное комплексное число.                                                | {conjugate}        |
| float.fromhex          |                                                                                          | {fromhex}          |
| float.hex              |                                                                                          | {hex}              |
| float.imag             | Возвращает мнимую часть комплексного числа.                                              | {imag}             |
| float.is_integer       |                                                                                          | {is_integer}       |
| float.real             | Возвращает действительную часть комплексного числа.                                      | {real}             |
""".format(
                    as_integer_ratio=to_table_code_py(">>> 10.5.as_integer_ratio()\n(21, 2)"),
                    conjugate=to_table_code_py(">>> 10.5.conjugate()\n10.5"),
                    fromhex=to_table_code_py('>>> float.fromhex("ff")\n255.0'),
                    hex=to_table_code_py(
                        '>>> (-0.1).hex()\n"-0x1.999999999999ap-4"\n'
                        '>>> 3.14159.hex()\n"0x1.921f9f01b866ep+1"'
                    ),
                    imag=to_table_code_py(">>> 10.5.imag\n0.0"),
                    is_integer=to_table_code_py(">>> 10.5.is_integer()\nFalse\n>>> 10.0.is_integer()\nTrue"),
                    real=to_table_code_py(">>> 10.0.real\n10.0"),
                ),
                "list": """
| Метод           |           |
|:----------------|:----------|
| list.append()   | {append}  |
| list.clear()    | {clear}   |
| list.сору()     | {сору}    |
| list.count()    | {count}   |
| list.extend([]) | {extend}  |
| list.index()    | {index}   |
| list.insert()   | {insert}  |
| list.pop()      | {pop}     |
| list.remove()   | {remove}  |
| list.reverse()  | {reverse} |
| list.sort()     | {sort}    |

""".format(
                    append=to_table_code_py(
                        ">>> l = [1, 2, 3]\n"
                        ">>> l.append(4)\n"
                        ">>> print(l)\n[1, 2, 3, 4]"
                    ),
                    clear=to_table_code_py(
                        ">>> l = [1, 2, 3]\n>>> l.clear()\n>>> print(l)\n[]"
                    ),
                    сору=to_table_code_py(
                        ">>> l = [1, 2, 3]\n"
                        ">>> l1 = l.copy()\n"
                        ">>> print(l)\n[1, 2, 3]\n"
                        ">>> l is l1\nFalse"
                    ),
                    count=to_table_code_py(">>> [1, 1, 2].count(1)\n2"),
                    extend=to_table_code_py(
                        ">>> l = [1, 2, 3]\n"
                        ">>> l.extend([4, 5])\n"
                        ">>> print(l)\n[1, 2, 3, 4, 5]"
                    ),
                    index=to_table_code_py(">>> [1, 2, 3].index(2)\n1"),
                    insert=to_table_code_py(
                        ">>> l = [1, 2, 3]\n"
                        ">>> l.insert(3, 4)\n"
                        ">>> print(l)\n[1, 2, 3, 4]"
                    ),
                    pop=to_table_code_py(
                        ">>> l = [1, 2, 3]\n"
                        ">>> l.pop(2)\n3\n"
                        ">>> print(l)\n[1, 2]"
                    ),
                    remove=to_table_code_py(
                        ">>> l = [1, 2, 3]\n"
                        ">>> l.remove(2)\n"
                        ">>> print(l)\n[1, 3]"
                    ),
                    reverse=to_table_code_py(
                        ">>> l = [1, 2, 3]\n"
                        ">>> l.reverse()\n"
                        ">>> print(l)\n[3, 2, 1]"
                    ),
                    sort=to_table_code_py(
                        ">>> l = [4, 3, 5]\n"
                        ">>> l.sort()\n"
                        ">>> print(l)\n[3, 4, 5]"
                    ),
                ),
                "tuple": """

| Метод                          | Описание                                                                                                                                                                         |
|--------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| tuple.count(x)                 | Возвращает количество элементов в кортеже, равных `x`.                                                                                                                           |
| tuple.index(x[, start[, end]]) | Возвращает индекс первого вхождения элемента `x` в кортеже.<br>Вызывает ошибку `ValueError`, если элемент не найден.<br>Можно указать диапазон поиска с помощью `start` и `end`. |

""",
                "dict": """
| Метод             | Описание                                                                              |
|:------------------|:--------------------------------------------------------------------------------------|
| dict.clear()      | Удаляет все элементы<br>{clear}                                                       |
| dict.copy()       | Возвращает поверхностную копию словаря<br>{copy}                                      |
| dict.fromkeys()   | Создает словарь из заданной последовательности<br>{fromkeys}                          |
| dict.get()        | Возвращает значение ключа<br>{get}                                                    |
| dict.pop()        | Удаляет и возвращает элемент с заданным ключом<br>{pop}                               |
| dict.popitem()    | Возвращает и удаляет последний элемент из словаря<br>{popitem}                        |
| dict.setdefault() | Возвращает значение по ключу. Если ключ отсутствует он вставляет ключ<br>{setdefault} |
| dict.update()     | Обновляет словарь указанными парами ключ-значение.<br>{update}                        |
| dict.items()      | Возвращает вид пары словаря (ключ, значение)<br>{items}                               |
| dict.keys()       | Возвращает объект просмотра всех ключей<br>{keys}                                     |
| dict.values()     | Возвращает список всех значений в словаре<br>{values}                                 |
""".format(
                    clear=to_table_code_py(
                        ">>> d = {1: 2, 3: 4}\n>>> d.clear()\n>>> print(d)\n{}"
                    ),
                    copy=to_table_code_py(
                        ">>> d = {1: 2, 3: 4}\n>>> d.copy()\n>>> print(d)\n{1: 2, 3: 4}"
                    ),
                    fromkeys=to_table_code_py(
                        '>>> print(dict.fromkeys(("key1", "key2", "key3"), 0))\n'
                        '{"key1": 0, "key2": 0, "key3": 0}'
                    ),
                    get=to_table_code_py(
                        '>>> print({"model": "Mustang", "year": 1964}.get("model"))\nMustang\n'
                        '>>> print({"model": "Mustang", "year": 1964}.get("color", "red"))\nred'
                    ),
                    pop=to_table_code_py(
                        ">>> d = {1: 2, 3: 4}\n"
                        ">>> print(d.pop(3))\n4\n"
                        ">>> print(d)\n{1: 2}"
                    ),
                    popitem=to_table_code_py(
                        ">>> d = {1: 2, 3: 4}\n"
                        ">>> print(d.popitem())\n(3, 4)\n"
                        ">>> print(d)\n{1: 2}"
                    ),
                    setdefault=to_table_code_py(
                        ">>> d = {}\n"
                        '>>> d.setdefault("k", "d")\n"d"\n'
                        '>>> d\n{"k": "d"}'
                    ),
                    update=to_table_code_py(
                        ">>> d = {1: 2, 3: 4}\n"
                        ">>> d.update({3: 5, 6: 7})\n"
                        ">>> print(d)\n{1: 2, 3: 5, 6: 7}"
                    ),
                    items=to_table_code_py(
                        ">>> d = {1: 2, 3: 4}\n"
                        ">>> print(d.items())\ndict_items([(1, 2), (3, 4)])"
                    ),
                    keys=to_table_code_py(
                        ">>> d = {1: 2, 3: 4}\n"
                        ">>> print(d.keys())\ndict_keys([1, 3])"
                    ),
                    values=to_table_code_py(
                        ">>> d = {1: 2, 3: 4}\n"
                        ">>> print(d.values())\ndict_values([2, 4])"
                    ),
                ),
                "set": r"""
| Метод                                           | Описание                                                                                                           |                                   |
|:------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------|-----------------------------------|
| set`.add`(element)                              | Добавляет элемент `element` во множество.<br>Если элемент уже присутствует, ничего не происходит.                  | {set_add}                         |
| set`.issubset`(set2)                            | Проверяет, является ли `set` подмножеством `set2`.<br>Возвращает `True`, если так, иначе `False`.                  | {set_issubset}                    |
| set`.isdisjoint`(set2)                          | Проверяет, есть ли общие элементы между `set` и `set2`.<br>Возвращает `True`, **если нет**, иначе `False`.         | {set_isdisjoint}                  |
| set`.issuperset`(set2)                          | Проверяет, является ли `set` надмножеством `set2`.<br>Возвращает `True`, если так, иначе `False`.                  | {set_issuperset}                  |
| set`.copy()`                                    | Возвращает копию множества.                                                                                        | {set_copy}                        |
| set`.union`(set2)<br>`|`                        | Возвращает новое множество,<br>содержащее все элементы из `set` и `set2`.                                          | {set_union}                       |
| set`.difference`(set2)<br>`-`                   | Возвращает новое множество,<br>содержащее элементы из `set`, которые отсутствуют в `set2`.                         | {set_difference}                  |
| set`.intersection`(set2)<br>`&`                 | Возвращает новое множество, содержащее только элементы,<br>присутствующие одновременно в `set` и `set2`.           | {set_intersection}                |
| set`.symmetric_difference`(set2)<br>`^`         | Возвращает новое множество, содержащее элементы,<br>присутствующие только в одном из `set` и `set2`.               | {set_symmetric_difference}        |
| set`.update`(set2)<br>`|=`                      | Обновляет множество, добавляя элементы из `set2`.                                                                  | {set_update}                      |
| set`.difference_update`(set2)<br>`-=`           | Обновляет множество, удаляя элементы из `set`,<br>которые присутствуют в `set2`.                                   | {set_difference_update}           |
| set`.intersection_update`(set2)<br>`&=`         | Обновляет множество, оставляя только элементы,<br>присутствующие одновременно в `set` и `set2`.                    | {set_intersection_update}         |
| set`.symmetric_difference_update`(set2)<br>`^=` | Обновляет множество, оставляя только элементы,<br>присутствующие только в одном из `set` и `set2`.                 | {set_symmetric_difference_update} |
| set`.pop()`                                     | Удаляет и возвращает произвольный элемент из множества.<br>Если множество пустое, возникает исключение `KeyError`. | {set_pop}                         |
| set`.clear()`                                   | Удаляет все элементы из множества, делая его пустым.                                                               | {set_clear}                       |
| set`.remove`(element)                           | Удаляет элемент `element` из множества.<br>Если элемент не найден, возникает исключение `KeyError`.                | {set_remove}                      |
| set`.discard`(element)                          | Удаляет элемент `element` из множества.<br>Если элемент не найден, ничего не происходит.                           | {set_discard}                     |


# frozenset

В Python «замороженный» означает, что объект не может быть изменен. Например, рассмотрим `set` и `frozenset`:

```pycon
>>> s = set((1, 2, 3))
>>> s
{{1, 2, 3}}
>>> s.add(4)
>>> s
{{1, 2, 3, 4}}
>>> fs = frozenset((1, 2, 3))
>>> fs
frozenset({{1, 2, 3}})
>>> fs.add(4)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'frozenset' object has no attribute 'add'
```
""".format(
                    set_add=to_table_code_py(
                        """
>>> s = {1, 2, 3}
>>> s.add(4)
>>> s
{1, 2, 3, 4}
>>> s.add(3)
>>> s
{1, 2, 3, 4}
"""
                    ),
                    set_issubset=to_table_code_py(
                        """
>>> {1, 2, 3}.issubset({0, 1, 2, 3, 4})
True
>>> {1, 2, 3}.issubset({0, 1, 3, 4})
False
"""
                    ),
                    set_isdisjoint=to_table_code_py(
                        """
>>> {1, 2, 3}.isdisjoint({4, 5, 6})
True
>>> {1, 2, 3}.isdisjoint({3, 4, 5})
False
"""
                    ),
                    set_issuperset=to_table_code_py(
                        """
>>> {0, 1, 2, 3, 4}.issuperset({1, 2, 3})
True
>>> {0, 1, 3, 4}.issuperset({1, 2, 3})
False
"""
                    ),
                    set_copy=to_table_code_py(
                        """
>>> first_set = {1, 2, 3}
>>> id(first_set)
...........64
>>> id(first_set.copy())
...........88
"""
                    ),
                    set_union=to_table_code_py(
                        """
>>> {1, 2} | {1, 2, 3, 4}
{1, 2, 3, 4}
>>> {1, 2}.union({1, 2, 3, 4})
{1, 2, 3, 4}
"""
                    ),
                    set_difference=to_table_code_py(
                        """
>>> {1, 2, 3, 4} - {2, 3}
{1, 4}
>>> {1, 2, 3, 4}.difference({2, 3})
{1, 4}
"""
                    ),
                    set_intersection=to_table_code_py(
                        """
>>> {1, 2, 3} & {2, 3, 4}
{2, 3}
>>> {1, 2, 3}.intersection({2, 3, 4})
{2, 3}
"""
                    ),
                    set_symmetric_difference=to_table_code_py(
                        """
>>> {1, 2, 3} ^ {3, 4, 5}
{1, 2, 4, 5}
>>> {1, 2, 3}.symmetric_difference({3, 4, 5})
{1, 2, 4, 5}
"""
                    ),
                    set_update=to_table_code_py(
                        """
>>> s1 = {1, 2, 3}
>>> s1 |= {2, 3, 4, 5}
>>> s1
{1, 2, 3, 4, 5}
>>> s1.update({4, 5, 6, 7})
>>> s1
{1, 2, 3, 4, 5, 6, 7}
"""
                    ),
                    set_difference_update=to_table_code_py(
                        """
>>> s1 = {1, 2, 3}
>>> s1 -= {3, 4, 5}
>>> s1
{1, 2}
>>> s1.difference_update({2})
>>> s1
{1}
"""
                    ),
                    set_intersection_update=to_table_code_py(
                        """
>>> s1 = {1, 2, 3}
>>> s1 &= {2, 3, 4}
>>> s1
{2, 3}
>>> s1.intersection_update({1, 2, 3, 4})
>>> s1
{2, 3}
"""
                    ),
                    set_symmetric_difference_update=to_table_code_py(
                        """
>>> s1 = {1, 2, 3}
>>> s1 ^= {3, 4, 5}
>>> s1
{1, 2, 4, 5}
>>> s1.symmetric_difference_update({4, 5, 6})
>>> s1
{1, 2, 6}
"""
                    ),
                    set_pop=to_table_code_py(
                        """
>>> {1, 2, 3}.pop()
1
"""
                    ),
                    set_clear=to_table_code_py(
                        """
>>> s = {1, 2, 3}
>>> s.clear()
>>> s
set()
"""
                    ),
                    set_remove=to_table_code_py(
                        """
>>> s = {1, 2, 3}
>>> s.remove(2)
>>> s
{1, 3}
>>> s.remove(145)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 145
"""
                    ),
                    set_discard=to_table_code_py(
                        """
>>> s = {1, 2, 3}
>>> s.discard(2)
>>> s
{1, 3}
>>> s.discard(145)
>>> s
{1, 3}
"""
                    ),
                ),
            },
            "Decorators Closure": {
                "Decorators Closure": """

## Декораторы

Специальные функции, которые позволяют модифицировать поведение других функций.
Они часто используются для добавления нового функционала к существующим функциям без изменения их кода.

```python
def cache_decorator(func):
    cache = {}
    def wrapper(*args, **kwargs):
        key = f"{args}:{kwargs}"
        if key not in cache:
            cache[key] = func(*args, **kwargs)
        return cache[key]
    return wrapper

@cache_decorator
def expensive_function(x):
    # дорогая расчетная функция
    return x**2

print(expensive_function(2))  # 4
print(expensive_function(2))  # 4 (значение берется из кеша)
print(expensive_function(3))  # 9
print(expensive_function(3))  # 9 (значение берется из кеша)
```

## closure (Замыкания)

Функции, которые ссылаются на переменные, определенные вне этой функции.
Они позволяют сохранять состояние переменных между вызовами функции.
Замыкания часто используются в Python для создания функций-генераторов,
которые возвращают новые функции с измененными параметрами.

Например, следующий код создает функцию-генератор, которая возвращает
функции, увеличивающие число на указанное значение:

```python
def make_incrementor(n):
    def incrementor(x):
        return x + n
    return incrementor

plus_3 = make_incrementor(3)
plus_5 = make_incrementor(5)

print(plus_3(10))  # 13
print(plus_5(10))  # 15
```
""",
                "dataclass": r"""
# \_\_all\_\_

| Название                   | Описание                                                                                                                                           |
|----------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| `@dataclass`               | Декоратор для автоматического создания методов класса, таких как `__init__`, `__repr__`, `__eq__`, и других.                                       |
| `field`                    | Функция для настройки полей внутри датакласса. Позволяет задать значения по умолчанию, фабрики значений, а также управлять поведением полей.       |
| `Field`                    | Класс, представляющий метаинформацию о полях датакласса. Создаётся автоматически при использовании `field()`.                                      |
| `FrozenInstanceError`      | Исключение, которое возникает при попытке изменить поле объекта неизменяемого (`frozen=True`) датакласса.                                          |
| `InitVar`                  | Специальный тип для переменных, которые используются только в `__init__` и не сохраняются как атрибуты класса.                                     |
| `KW_ONLY`                  | Специальная константа, используемая для обозначения полей, которые должны передаваться только через ключевые аргументы в `__init__`.               |
| `MISSING`                  | Значение, указывающее на отсутствие значения по умолчанию для поля, используется библиотекой автоматически.                                               |
| `fields`                   | Функция, возвращающая информацию о полях класса (список объектов `Field`).                                                                               |
| `asdict`                   | Функция, которая преобразует объект датакласса в словарь, где ключами являются имена полей, а значениями — данные этих полей.                            |
| `astuple`                  | Преобразует объект датакласса в кортеж с последовательными значениями полей.                                                                              |
| `make_dataclass`           | Функция для динамического создания нового датакласса с указанными полями и их типами.                                                                     |
| `replace`                  | Возвращает копию объекта датакласса с изменёнными значениями указанных полей.                                                                             |
| `is_dataclass`             | Функция, проверяющая, является ли объект экземпляром датакласса.                                                                                          |

# Описание

## @dataclass
Основной декоратор для объявления классов данных. Автоматически генерирует методы `__init__`, `__repr__`, `__eq__`, и другие.

```python
from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int
```
### Параметры dataclass

```python
@dataclass(
    *,
    init: bool = ...,
    repr: bool = ...,
    eq: bool = ...,
    order: bool = ...,
    unsafe_hash: bool = ...,
    frozen: bool = ...,
)
```

|               |                                                                                                                 |
|---------------|-----------------------------------------------------------------------------------------------------------------|
| `init`        | Нужно ли автоматически генерировать метод `__init__` для инициализации атрибутов класса                         |
| `repr`        | Нужно ли автоматически генерировать метод `__repr__` для вывода строкового представления объектов класса        |
| `eq`          | Нужно ли автоматически генерировать метод `__eq__` для сравнения объектов класса                                |
| `order`       | Нужно ли автоматически генерировать методы `__lt__`, `__le__`, `__gt__`, `__ge__` для сравнения объектов класса |
| `unsafe_hash` | Нужно ли автоматически генерировать метод `__hash__` для объектов класса.<br>Обычно этот аргумент следует использовать только для классов, объекты которых неизменяемы `frozen`,<br>так как изменяемые объекты могут привести к неожиданным результатам |
| `frozen`      | Нужно ли сделать объекты класса неизменяемыми `immutable`                                                       |

#### Значения по умолчанию

```python
@dataclass(
    *,
    init: bool = True,
    repr: bool = True,
    eq: bool = True,
    order: bool = True,
    unsafe_hash: bool = True,
    frozen: bool = False,
)
```

## field
Используется для более точной настройки полей.
Например, можно задать фабрику значений по умолчанию или исключить поле из конструктора.

```python
from dataclasses import dataclass, field

@dataclass
class Person:
    name: str
    age: int = field(default=18)  # Значение по умолчанию
    friends: list = field(default_factory=list)  # Фабрика для списка
```

## Field
Объект, создаваемый при использовании функции `field()`.
Содержит информацию о поле, его значении по умолчанию, фабрике значений и других метаданных.

## FrozenInstanceError
Исключение, которое генерируется, если пытаются изменить поле объекта неизменяемого датакласса.

```python
from dataclasses import dataclass, FrozenInstanceError

@dataclass(frozen=True)
class Point:
    x: int
    y: int

p = Point(1, 2)
# p.x = 10  # Вызовет FrozenInstanceError
```

## InitVar
Используется для создания переменных, которые существуют только на этапе инициализации и не сохраняются в объекте.

```python
from dataclasses import dataclass, InitVar

@dataclass
class Person:
    name: str
    age: InitVar[int]  # Не сохраняется в объекте
```

## KW_ONLY
Позволяет указать, что некоторые поля должны передаваться только как именованные аргументы при создании объекта.

```python
from dataclasses import dataclass, KW_ONLY

@dataclass
class Person:
    name: str
    KW_ONLY
    age: int
```

## MISSING
Специальное значение, используемое библиотекой `dataclasses` для обозначения отсутствия значения по умолчанию для поля.

## fields
Возвращает список полей класса в виде объектов `Field`.

```python
from dataclasses import dataclass, fields

@dataclass
class Person:
    name: str
    age: int

print(fields(Person))  # Выводит информацию о полях класса
```

## asdict
Преобразует объект датакласса в словарь.

```python
from dataclasses import dataclass, asdict

@dataclass
class Person:
    name: str
    age: int

p = Person("Alice", 30)
print(asdict(p))  # {"name": "Alice", "age": 30}
```

## astuple
Преобразует объект датакласса в кортеж.

```python
from dataclasses import astuple

print(astuple(p))  # ("Alice", 30)
```

## make_dataclass
Создаёт новый датакласс на лету с указанными полями.

```python
from dataclasses import make_dataclass

Point = make_dataclass("Point", [("x", int), ("y", int)])
p = Point(1, 2)
print(p)  # Point(x=1, y=2)
```

## replace
Возвращает новую копию объекта с изменёнными полями.

```python
from dataclasses import replace

p2 = replace(p, age=35)
print(p2)  # Person(name="Alice", age=35)
```

## is_dataclass
Проверяет, является ли объект экземпляром датакласса.

```python
from dataclasses import is_dataclass

print(is_dataclass(p))  # True
```




## \_\_post_init\_\_

Специальный метод, используемый **только в датаклассах** (аннотированных с помощью декоратора `@dataclass`).
Его основное предназначение — выполнить дополнительные действия или инициализацию после того, как автоматически сгенерированный метод `__init__` завершит свою работу.
В обычных классах этот метод не используется автоматически и его наличие не имеет смысла без использования библиотеки `dataclasses`.

Когда создается объект датакласса, Python сначала автоматически вызывает метод `__init__`, который создается на основе полей, объявленных в классе.
После этого, если в классе определен метод `__post_init__`, он будет вызван **сразу после** инициализации полей.

### Пример

```python
from dataclasses import dataclass

@dataclass
class Employee:
    name: str
    base_salary: float
    bonus_percentage: float = 0.0
    total_salary: float = 0.0

    def __post_init__(self):  # Выполняется сразу после создания объекта
        # Рассчитываем итоговую зарплату на основе бонуса
        self.total_salary = self.base_salary + (self.base_salary * self.bonus_percentage / 100)

emp = Employee(name="Alice", base_salary=1000, bonus_percentage=10)
print(emp)  # Employee(name="Alice", base_salary=1000, bonus_percentage=10, total_salary=1100.0)
```

### Особенности

1. **Модификация значений полей**: `__post_init__` часто используется для выполнения дополнительных вычислений или проверок,
требующих значений уже инициализированных полей
2. **Работа с `InitVar`**: Если в датаклассе используются поля `InitVar`, они передаются в `__post_init__`,
так как они не сохраняются как обычные атрибуты. Это полезно для временных параметров и инициализаций

### Пример с InitVar
Значение `celsius` передается в метод `__post_init__` и используется для вычисления значения поля `fahrenheit`
```python
from dataclasses import dataclass, InitVar

@dataclass
class TemperatureConverter:
    celsius: InitVar[float]
    fahrenheit: float = 0.0

    def __post_init__(self, celsius):
        # Преобразование градусов Цельсия в Фаренгейты
        self.fahrenheit = celsius * 9/5 + 32

temp = TemperatureConverter(celsius=25)
print(temp)  # TemperatureConverter(fahrenheit=77.0)
```

""",
                "property": """
```python
class Student:
    def __init__(self):
        self._score = 0

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, s):
        if 0 <= s <= 100:
            self._score = s
        else:
            raise ValueError

user1 = Student()
print(user1.score)  # 0
user1.score = 1
print(user1.score)  # 1
user1._score = 999
print(user1.score)  # 999
user1.score = 999
print(user1.score)  # ValueError
```
""",
                "cached_property": """
```python
from functools import cached_property


class Circle:
    def __init__(self, radius):
        self.radius = radius

    @cached_property
    def area(self):
        return 3.14 * self.radius ** 2


circle = Circle(10)
print(circle.area)
# Напечатает 314.0
print(circle.area)
# Вернет кешированное значение 314.0 без вычислений
```
""",
                "staticmethod": """
`@staticmethod` - это декоратор в Python, который используется для определения статического метода внутри класса. 
Статический метод - это метод, который может быть вызван на классе, а не на экземпляре класса. 
Он не имеет доступа к экземпляру класса и не может изменять его состояние.

```python
class MyClass:
    @staticmethod
    def my_static_method(arg1, arg2):
        return arg1 + arg2

print(MyClass.my_static_method(1, 2))  # 3
```

В этом примере мы определили класс `MyClass` и внутри него определили статический метод `my_static_method`. 
Этот метод принимает два аргумента `arg1` и `arg2` и возвращает их сумму. 
Затем мы вызвали этот метод на классе `MyClass`, а не на экземпляре класса.
""",
                "classmethod": """
Декоратор `@classmethod` используется для определения методов класса,
которые принимают первый аргумент в виде самого класса (обычно называемый `cls`),
а не экземпляра класса (как в случае с методами экземпляра, где первый аргумент называется `self`).

`@classmethod` позволяет вызывать метод как на экземпляре класса, так и на самом классе.

```python
class MyClass:
    @classmethod
    def foo(cls, arg):
        print(arg)


MyClass.foo(5)    # 5
MyClass().foo(6)  # 6
```
""",
                "overload": """
`@overload` - это декоратор в Python, который используется для определения перегрузки метода внутри класса. 
Перегрузка метода - это механизм, позволяющий определить несколько версий метода с разными параметрами. 
При вызове метода, интерпретатор Python выберет версию метода, которая соответствует переданным аргументам.

```python
from typing import overload

class MyClass:
    @overload
    def my_method(self, arg1: int) -> int:
        pass

    @overload
    def my_method(self, arg1: str) -> str:
        pass

    def my_method(self, arg1):
        if isinstance(arg1, int):
            return arg1 * 2
        elif isinstance(arg1, str):
            return arg1.upper()


obj = MyClass()
print(obj.my_method(2))        # 4
print(obj.my_method("hello"))  # HELLO
```
""",
                "final": """
`@final` - это аннотация (декоратор) в Python, которая указывает, что метод или свойство класса не должны переопределяться в подклассах.

Когда метод или свойство класса помечаются аннотацией `@final`, это предупреждает программистов, 
что эти элементы класса являются частью публичного интерфейса класса, который не должен изменяться в подклассах. 
Это позволяет сделать класс более простым и предсказуемым в использовании, так как гарантируется, 
что поведение не будет изменено в производных классах.


```python
from typing import final


class BaseClass:
    @final
    def some_method(self):
        pass

class DerivedClass(BaseClass):
    def some_method(self):  # Ошибка: невозможно переопределить метод
        pass
```

```python
from typing import final

@final
class FinalClass:
    pass

class AnotherClass(FinalClass):  # Ошибка: невозможно наследовать от FinalClass
    pass
```

> Декоратор `@final` является частью системы типизации Python и,
следовательно, не влияет на выполнение кода в интерпретаторе Python.
Он предназначен для статической проверки и повышения читаемости кода.
""",
            },
            "bash": {
                "Flags cmd Python": """
| Флаг                        | Описание |
|-----------------------------|----------|
| `-c`                        | Выполнить однострочный Python-код из командной строки. |
| `-m`                        | Запустить указанный Python-модуль как скрипт. |
| `-i` `—interactive`         | Запускает интерпретатор Python в интерактивном режиме после выполнения скрипта. |
| `-O` `—optimize`            | Включает режим оптимизации, который удаляет отладочную информацию и выполняет оптимизации в байт-коде.<br>Это может уменьшить размер файлов `.pyc` и улучшить производительность, но осложнить отладку. |
| `-B` `—dont-write-bytecode` | Предотвращает запись байт-кода (`.pyc` файлов) на диск. |
| `-v` `—verbose`             | Выводит подробные сообщения о том, какие модули импортируются<br>и какие файлы открываются в процессе выполнения программы. |
| `-q` `—quiet`               | Уменьшает уровень вывода, игнорируя сообщения о запуске и прочие информационные сообщения. |
| `-E` `—ignore-environment`  | Игнорировать переменные окружения,<br>которые обычно влияют на поведение Python, такие как `PYTHONPATH`. |
| `-u` `—unbuffered`          | Переключает режим не буферизованного ввода/вывода.<br>Полезно при работе с каналами и потоками данных,<br>чтобы гарантировать более немедленную обработку данных. |
| `-h` `—help`                | Выведет список всех доступных флагов и их описания. |

```
>python -h
usage: python [option] ... [-c cmd | -m mod | file | -] [arg] ...
Options (and corresponding environment variables):
-b     : issue warnings about str(bytes_instance), str(bytearray_instance)
         and comparing bytes/bytearray with str. (-bb: issue errors)
-B     : do not write .pyc files on import; also PYTHONDONTWRITEBYTECODE=x
-c cmd : program passed in as string (terminates option list)
-d     : turn on parser debugging output (for experts only, only works on
         debug builds); also PYTHONDEBUG=x
-E     : ignore PYTHON* environment variables (such as PYTHONPATH)
-h     : print this help message and exit (also -? or --help)
-i     : inspect interactively after running script; forces a prompt even
         if stdin does not appear to be a terminal; also PYTHONINSPECT=x
-I     : isolate Python from the users environment (implies -E and -s)
-m mod : run library module as a script (terminates option list)
-O     : remove assert and __debug__-dependent statements; add .opt-1 before
         .pyc extension; also PYTHONOPTIMIZE=x
-OO    : do -O changes and also discard docstrings; add .opt-2 before
         .pyc extension
-P     : do not prepend a potentially unsafe path to sys.path; also PYTHONSAFEPATH
-q     : do not print version and copyright messages on interactive startup
-s     : do not add user site directory to sys.path; also PYTHONNOUSERSITE
-S     : do not imply "import site" on initialization
-u     : force the stdout and stderr streams to be unbuffered;
         this option has no effect on stdin; also PYTHONUNBUFFERED=x
-v     : verbose (trace import statements); also PYTHONVERBOSE=x
         can be supplied multiple times to increase verbosity
-V     : print the Python version number and exit (also --version)
         when given twice, print more information about the build
-W arg : warning control; arg is action:message:category:module:lineno
         also PYTHONWARNINGS=arg
-x     : skip first line of source, allowing use of non-Unix forms of #!cmd
-X opt : set implementation-specific option
--check-hash-based-pycs always|default|never:
         control how Python invalidates hash-based .pyc files
--help-env      : print help about Python environment variables and exit
--help-xoptions : print help about implementation-specific -X options and exit
--help-all      : print complete help information and exit
Arguments:
file   : program read from script file
-      : program read from stdin (default; interactive mode if a tty)
arg ...: arguments passed to program in sys.argv[1:]
```
""",
                "Flags cmd pip": """
| Флаг                  | Описание |
|-----------------------|----------|
| `-r` `--requirements` | Установить пакеты из указанного файла зависимостей `requirements.txt`.
| `-U` `--upgrade`      | Обновить уже установленные пакеты до последней версии.
| `-e` `--editable`     | Установить пакет в режиме редактирования, что позволяет вносить изменения в код и сразу же видеть результаты.
| `-t` `--target`       | Указать путь к каталогу, в который будут установлены пакеты.
| `-f` `--find-links`   | Указать дополнительные источники для поиска пакетов (например, `URL` или путь к локальному каталогу).
| `-i` `--index-url`    | Указать `URL` для поиска пакетов в репозитории `PyPI`.
| `--no-index`          | Не использовать `PyPI` для поиска пакетов, только локальные источники.
| `--no-cache-dir`      | Не использовать кэш при установке пакетов.
| `--user`              | Установить пакеты в домашний каталог текущего пользователя.

```bash
pip install --help
```

```
Usage:
  pip install [options] <requirement specifier> [package-index-options] ...
  pip install [options] -r <requirements file> [package-index-options] ...
  pip install [options] [-e] <vcs project url> ...
  pip install [options] [-e] <local project path> ...
  pip install [options] <archive url/path> ...

Description:
  Install packages from:

  - PyPI (and other indexes) using requirement specifiers.
  - VCS project urls.
  - Local project directories.
  - Local or remote source archives.

  pip also supports installing from "requirements files", which provide
  an easy way to specify a whole environment to be installed.

Install Options:
  -r, --requirement <file>    Install from the given requirements file. This option can be used multiple times.
  -c, --constraint <file>     Constrain versions using the given constraints file. This option can be used multiple times.
  --no-deps                   Don't install package dependencies.
  --pre                       Include pre-release and development versions. By default, pip only finds stable versions.
  -e, --editable <path/url>   Install a project in editable mode (i.e. setuptools "develop mode") from a local project path or a VCS url.
  --dry-run                   Don't actually install anything, just print what would be. Can be used in combination with --ignore-installed to 'resolve'
                              the requirements.
  -t, --target <dir>          Install packages into <dir>. By default this will not replace existing files/folders in <dir>. Use --upgrade to replace
                              existing packages in <dir> with new versions.
  --platform <platform>       Only use wheels compatible with <platform>. Defaults to the platform of the running system. Use this option multiple times
                              to specify multiple platforms supported by the target interpreter.
  --python-version <python_version>
                              The Python interpreter version to use for wheel and "Requires-Python" compatibility checks. Defaults to a version derived
                              from the running interpreter. The version can be specified using up to three dot-separated integers (e.g. "3" for 3.0.0,
                              "3.7" for 3.7.0, or "3.7.3"). A major-minor version can also be given as a string without dots (e.g. "37" for 3.7.0).
  --implementation <implementation>
                              Only use wheels compatible with Python implementation <implementation>, e.g. 'pp', 'jy', 'cp',  or 'ip'. If not specified,
                              then the current interpreter implementation is used.  Use 'py' to force implementation-agnostic wheels.
  --abi <abi>                 Only use wheels compatible with Python abi <abi>, e.g. 'pypy_41'. If not specified, then the current interpreter abi tag is
                              used. Use this option multiple times to specify multiple abis supported by the target interpreter. Generally you will need
                              to specify --implementation, --platform, and --python-version when using this option.
  --user                      Install to the Python user install directory for your platform. Typically ~/.local/, or %APPDATA%\Python on Windows. (See
                              the Python documentation for site.USER_BASE for full details.)
  --root <dir>                Install everything relative to this alternate root directory.
  --prefix <dir>              Installation prefix where lib, bin and other top-level folders are placed. Note that the resulting installation may contain
                              scripts and other resources which reference the Python interpreter of pip, and not that of ``--prefix``. See also the
                              ``--python`` option if the intention is to install packages into another (possibly pip-free) environment.
  --src <dir>                 Directory to check out editable projects into. The default in a virtualenv is "<venv path>/src". The default for global
                              installs is "<current dir>/src".
  -U, --upgrade               Upgrade all specified packages to the newest available version. The handling of dependencies depends on the upgrade-strategy
                              used.
  --upgrade-strategy <upgrade_strategy>
                              Determines how dependency upgrading should be handled [default: only-if-needed]. "eager" - dependencies are upgraded
                              regardless of whether the currently installed version satisfies the requirements of the upgraded package(s). "only-if-
                              needed" -  are upgraded only when they do not satisfy the requirements of the upgraded package(s).
  --force-reinstall           Reinstall all packages even if they are already up-to-date.
  -I, --ignore-installed      Ignore the installed packages, overwriting them. This can break your system if the existing package is of a different
                              version or was installed with a different package manager!
  --ignore-requires-python    Ignore the Requires-Python information.
  --no-build-isolation        Disable isolation when building a modern source distribution. Build dependencies specified by PEP 518 must be already
                              installed if this option is used.
  --use-pep517                Use PEP 517 for building source distributions (use --no-use-pep517 to force legacy behaviour).
  --check-build-dependencies  Check the build dependencies when PEP517 is used.
  --break-system-packages     Allow pip to modify an EXTERNALLY-MANAGED Python installation
  -C, --config-settings <settings>
                              Configuration settings to be passed to the PEP 517 build backend. Settings take the form KEY=VALUE. Use multiple --config-
                              settings options to pass multiple keys to the backend.
  --global-option <options>   Extra global options to be supplied to the setup.py call before the install or bdist_wheel command.
  --compile                   Compile Python source files to bytecode
  --no-compile                Do not compile Python source files to bytecode
  --no-warn-script-location   Do not warn when installing scripts outside PATH
  --no-warn-conflicts         Do not warn about broken dependencies
  --no-binary <format_control>
                              Do not use binary packages. Can be supplied multiple times, and each time adds to the existing value. Accepts either ":all:"
                              to disable all binary packages, ":none:" to empty the set (notice the colons), or one or more package names with commas
                              between them (no colons). Note that some packages are tricky to compile and may fail to install when this option is used on
                              them.
  --only-binary <format_control>
                              Do not use source packages. Can be supplied multiple times, and each time adds to the existing value. Accepts either ":all:"
                              to disable all source packages, ":none:" to empty the set, or one or more package names with commas between them. Packages
                              without binary distributions will fail to install when this option is used on them.
  --prefer-binary             Prefer binary packages over source packages, even if the source packages are newer.
  --require-hashes            Require a hash to check each requirement against, for repeatable installs. This option is implied when any package in a
                              requirements file has a --hash option.
  --progress-bar <progress_bar>
                              Specify whether the progress bar should be used [on, off, raw] (default: on)
  --root-user-action <root_user_action>
                              Action if pip is run as a root user [warn, ignore] (default: warn)
  --report <file>             Generate a JSON file describing what pip did to install the provided requirements. Can be used in combination with --dry-run
                              and --ignore-installed to 'resolve' the requirements. When - is used as file name it writes to stdout. When writing to
                              stdout, please combine with the --quiet option to avoid mixing pip logging output with JSON output.
  --no-clean                  Don't clean up build directories.

Package Index Options:
  -i, --index-url <url>       Base URL of the Python Package Index (default https://pypi.org/simple). This should point to a repository compliant with PEP
                              503 (the simple repository API) or a local directory laid out in the same format.
  --extra-index-url <url>     Extra URLs of package indexes to use in addition to --index-url. Should follow the same rules as --index-url.
  --no-index                  Ignore package index (only looking at --find-links URLs instead).
  -f, --find-links <url>      If a URL or path to an html file, then parse for links to archives such as sdist (.tar.gz) or wheel (.whl) files. If a local
                              path or file:// URL that's a directory, then look for archives in the directory listing. Links to VCS project URLs are not
                              supported.

General Options:
  -h, --help                  Show help.
  --debug                     Let unhandled exceptions propagate outside the main subroutine, instead of logging them to stderr.
  --isolated                  Run pip in an isolated mode, ignoring environment variables and user configuration.
  --require-virtualenv        Allow pip to only run in a virtual environment; exit with an error otherwise.
  --python <python>           Run pip with the specified Python interpreter.
  -v, --verbose               Give more output. Option is additive, and can be used up to 3 times.
  -V, --version               Show version and exit.
  -q, --quiet                 Give less output. Option is additive, and can be used up to 3 times (corresponding to WARNING, ERROR, and CRITICAL logging
                              levels).
  --log <path>                Path to a verbose appending log.
  --no-input                  Disable prompting for input.
  --keyring-provider <keyring_provider>
                              Enable the credential lookup via the keyring library if user input is allowed. Specify which mechanism to use [disabled,
                              import, subprocess]. (default: disabled)
  --proxy <proxy>             Specify a proxy in the form scheme://[user:passwd@]proxy.server:port.
  --retries <retries>         Maximum number of retries each connection should attempt (default 5 times).
  --timeout <sec>             Set the socket timeout (default 15 seconds).
  --exists-action <action>    Default action when a path already exists: (s)witch, (i)gnore, (w)ipe, (b)ackup, (a)bort.
  --trusted-host <hostname>   Mark this host or host:port pair as trusted, even though it does not have valid or any HTTPS.
  --cert <path>               Path to PEM-encoded CA certificate bundle. If provided, overrides the default. See 'SSL Certificate Verification' in pip
                              documentation for more information.
  --client-cert <path>        Path to SSL client certificate, a single file containing the private key and the certificate in PEM format.
  --cache-dir <dir>           Store the cache data in <dir>.
  --no-cache-dir              Disable the cache.
  --disable-pip-version-check
                              Don't periodically check PyPI to determine whether a new version of pip is available for download. Implied with --no-index.
  --no-color                  Suppress colored output.
  --no-python-version-warning
                              Silence deprecation warnings for upcoming unsupported Pythons.
  --use-feature <feature>     Enable new functionality, that may be backward incompatible.
  --use-deprecated <feature>  Enable deprecated functionality, that will be removed in the future.
```
""",
                "venv": """
`venv` помогает избежать конфликтов между различными проектами,
предоставляя каждому из них своё собственное пространство для зависимостей.

### Создание виртуального окружения

```bash
python -m venv venv
```

### Активация окружения

- **Windows:** `venv/Scripts/activate`
- **macOS/Linux:** `source venv/bin/activate`

### Деактивация окружения

```bash
deactivate
```

### Установка пакетов в окружении из [[Languages/Python/bash/requirements.txt.md]]

```bash
pip install -r requirements.txt
```

### Удаление окружения

Просто удалите папку с виртуальным окружением `venv`.
""",
                "requirements.txt": """
Команда, которая создает список всех пакетов и их версий, 
установленных в настоящее время в среде Python.

```python
pip freeze > requirements.txt
```

Файл `requirements.txt` используется для указания зависимостей для проекта Python. 
В нем перечислены пакеты и их версии, необходимые для правильной работы проекта. 
Это упрощает настройку той же среды на другом компьютере или при развертывании приложения в производственной среде.
Когда вы запустите `pip freeze > requirements.txt`, он создаст новый файл с именем `requirements.txt`
в вашем текущем каталоге и запишет вывод `pip freeze` команды в этот файл, 
который будет содержать список всех пакетов и их версий, которые в 
настоящее время установлены в вашей среде Python, один пакет за строку.
Позже вы можете использовать 

```python
pip install -r requirements.txt
```

для установки всех пакетов и их версий, перечисленныx в файле, 
это гарантирует, что среда такая же, как та, которая 
использовалась для создания `requirements.txt` файла.

Рекомендуется включить `requirements.txt` файл в репозиторий вашего проекта, 
чтобы другие разработчики или пользователи могли легко 
настроить ту же среду и запустить проект с правильными зависимостями.

Для создания файла с библиотеками используемыми только для нужного проекта использовать 

```python
pip freeze --local > requirements.txt
```
""",
                "IPython": r"""
**Одиночный символ `%`**: Применяется для магических команд, которые действуют на одну строку в текущей ячейке.
**Двойной символ `%%`**: Применяется для ячеек с кодом, которые содержат блоки скриптов на различных языках (например, Python, Bash, Ruby).

| Команда            | Описание                                                                                    | Пример использования                                                                              |
|--------------------|---------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|
| `%%!`              | Выполняет команды оболочки в ячейке.                                                        | `%%!`<br>`echo "Hello, World!"`                                                                   |
| `%cpaste`          | Вставляет и выполняет блок кода, введённый вручную.                                         | `%cpaste`<br>`(вставить код)`<br>`--`                                                           |
| `%load`            | Загружает коды из файла в текущую ячейку.                                                   | `%load script.py`                                                                                 |
| `%pdb`             | Включает или выключает отладчик Python `pdb` при возникновении ошибок.                      | `%pdb on` или `%pdb off`                                                                          |
| `%%python2`        | Выполняет ячейку в интерпретаторе Python 2 (если установлен).                               | `%%python2`<br>`print "Hello from Python 2"`                                                      |
| `%sx`              | Выполняет команды оболочки и возвращает их результаты как список строк.                     | `output = %sx ls -l`<br>`print(output)`                                                           |
| `%%HTML`           | Отображает `HTML`-код в ячейке.                                                             | `%%HTML`<br>`<h1>Hello, World!</h1>`                                                              |
| `%ddir`            | Расширенный список атрибутов объекта.                                                       | `%ddir object_name`                                                                               |
| `%load_ext`        | Загружает расширение IPython.                                                               | `%load_ext autoreload`                                                                            |
| `%pdef`            | Показывает определение функции, включая аргументы.                                          | `%pdef function_name`                                                                             |
| `%%python3`        | Выполняет ячейку в интерпретаторе Python 3 (по умолчанию).                                  | `%%python3`<br>`print("Hello from Python 3")`                                                     |
| `%%sx`             | Выполняет команды оболочки в ячейке и возвращает их результаты как список строк.            | `%%sx`<br>`ls -l`                                                                                 |
| `%%SVG`            | Отображает `SVG`-код в ячейке.                                                              | `%%SVG`<br>`<svg>...</svg>`                                                                       |
| `%debug`           | Начинает сессию отладки в точке вызова.                                                     | `%debug`                                                                                          |
| `%loadpy`          | Загружает и выполняет файл Python.                                                          | `%loadpy script.py`                                                                               |
| `%pdoc`            | Показывает строку документации объекта.                                                     | `%pdoc function_name`                                                                             |
| `%quickref`        | Показывает краткое руководство по IPython.                                                  | `%quickref`                                                                                       |
| `%system`          | Выполняет команду оболочки.                                                                 | `%system ls -l`                                                                                   |
| `%alias`           | Создаёт псевдоним для команды оболочки.                                                     | `%alias ll ls -l`                                                                                 |
| `%%debug`          | Начинает сессию отладки в ячейке (аналогично `%debug`, но для всей ячейки).                 | `%%debug`<br>`buggy_function()`                                                                   |
| `%logoff`          | Отключает журналирование.                                                                   | `%logoff`                                                                                         |
| `%%perl`           | Выполняет код `Perl` в ячейке.                                                              | `%%perl`<br>`print "Hello from Perl\n";`                                                          |
| `%recall`          | Повторяет предыдущую команду или извлекает её по индексу из истории.                        | `%recall 42`                                                                                      |
| `%%system`         | Выполняет команды оболочки в ячейке.                                                        | `%%system`<br>`ls -l`                                                                             |
| `%alias_magic`     | Создаёт псевдоним для существующей магической команды IPython.                              | `%alias_magic t timeit`<br>`# Теперь можно использовать "t" вместо "timeit"`<br>`t my_function()` |
| `%dhist`           | Показывает историю директорий, в которых вы работали.                                       | `%dhist`                                                                                          |
| `%logon`           | Включает журналирование.                                                                    | `%logon`                                                                                          |
| `%pfile`           | Открывает и показывает содержимое файла с кодом.                                            | `%pfile my_script.py`                                                                             |
| `%rehashx`         | Пересчитывает псевдонимы для всех исполняемых файлов в `$PATH` (для использования с `%sx`). | `%rehashx`                                                                                        |
| `%tb`              | Показывает traceback (стек вызовов) от последнего исключения.                               | `%tb`                                                                                             |
| `%autoawait`       | Устанавливает функцию ожидания по умолчанию для поддержки асинхронного кода.                | `%autoawait asyncio`                                                                              |
| `%dirs`            | Показывает список директорий в стеке директорий.                                            | `%dirs`                                                                                           |
| `%logstart`        | Начинает журналирование сессии.                                                             | `%logstart`                                                                                       |
| `%pinfo`           | Показывает информацию об объекте.                                                           | `%pinfo function_name`                                                                            |
| `%reload_ext`      | Перезагружает расширение IPython.                                                           | `%reload_ext autoreload`                                                                          |
| `%time`            | Измеряет время выполнения однострочного кода.                                               | `%time my_function()`                                                                             |
| `%autocall`        | Управляет автоматическим вызовом функций в IPython.                                         | `%autocall 1`                                                                                     |
| `%doctest_mode`    | Включает/выключает режим тестирования документации `doctest`.                               | `%doctest_mode`                                                                                   |
| `%logstate`        | Показывает текущее состояние логирования.                                                   | `%logstate`                                                                                       |
| `%pinfo2`          | Показывает подробную информацию о объекте (дополненная версия `%pinfo`).                    | `%pinfo2 my_function`                                                                             |
| `%ren`             | Переименовывает переменную в среде IPython.                                                 | `%ren old_variable new_variable`                                                                  |
| `%%time`           | Измеряет время выполнения всей ячейки.                                                      | `%%time`<br>`my_function()`                                                                       |
| `%autoindent`      | Включает или выключает автоматический отступ.                                               | `%autoindent`                                                                                     |
| `%echo`            | Отображает текст или значение переменной.                                                   | `%echo "Hello, World!"`                                                                           |
| `%logstop`         | Останавливает журналирование сессии.                                                        | `%logstop`                                                                                        |
| `%pip`             | Позволяет использовать `pip` для установки пакетов изнутри IPython.                         | `%pip install numpy`                                                                              |
| `%rep`             | Повторяет и выполняет последнюю команду.                                                    | `%rep`                                                                                            |
| `%timeit`          | Измеряет время выполнения многократного запуска однострочного кода.                         | `%timeit sum(range(10000))`                                                                       |
| `%automagic`       | Включает или выключает автоматическое распознавание магических команд без префикса `%`.     | `%automagic on`                                                                                   |
| `%ed`              | Открывает редактор для редактирования строки или блока кода.                                | `%ed script.py`                                                                                   |
| `%ls`              | Список файлов и директорий.                                                                 | `%ls`                                                                                             |
| `%popd`            | Удаляет верхний каталог из стека директорий и переходит в новый верхний каталог.            | `%popd`                                                                                           |
| `%rerun`           | Повторяет последнюю команду с историей в ячейке.                                            | `%rerun`                                                                                          |
| `%%timeit`         | Измеряет время выполнения многократного запуска кода в ячейке.                              | `%%timeit`<br>`sum(range(10000))`                                                                 |
| `%%bash`           | Выполняет код `Bash` в ячейке.                                                              | `%%bash`<br>`echo "Hello from Bash"`                                                              |
| `%edit`            | Открывает редактор для редактирования строки или блока кода.                                | `%edit script.py`                                                                                 |
| `%lsmagic`         | Показывает список всех доступных магических команд.                                         | `%lsmagic`                                                                                        |
| `%pprint`          | Включает или выключает красивый вывод `pretty-printing` объектов.                           | `%pprint`                                                                                         |
| `%reset`           | Сбрасывает пространство имен IPython, удаляя все переменные и импортированные модули.       | `%reset`                                                                                          |
| `%unalias`         | Удаляет заданный псевдоним.                                                                 | `%unalias ll`                                                                                     |
| `%bookmark`        | Управление закладками для директорий.                                                       | `%bookmark mydir /path/to/directory`                                                              |
| `%env`             | Установка переменных среды или просмотр текущих переменных среды.                           | `%env PATH=/new/path`                                                                             |
| `%macro`           | Определяет макрос для последовательности команд.                                            | `%macro my_macro 1-5`<br>`print("Hello")`                                                         |
| `%precision`       | Устанавливает количество отображаемых знаков после запятой.                                 | `%precision 4`                                                                                    |
| `%reset_selective` | Сбрасывает только указанные переменные в пространстве имен IPython.                         | `%reset_selective my_variable`                                                                    |
| `%unload_ext`      | Выгружает указанное расширение IPython.                                                     | `%unload_ext autoreload`                                                                          |
| `%%capture`        | Перенаправляет вывод и ошибки в переменные.                                                 | `%%capture output`<br>`print("Hello, World!")`                                                    |
| `%%file`           | Записывает содержимое ячейки в файл.                                                        | `%%file my_script.py`<br>`print("Hello, World!")`                                                 |
| `%magic`           | Показывает справку по магическим командам.                                                  | `%magic`                                                                                          |
| `%prun`            | Выполняет код с профилированием с использованием `cProfile`.                                | `%prun my_function()`                                                                             |
| `%rmdir`           | Удаляет указанные директории.                                                               | `%rmdir directory_name`                                                                           |
| `%who`             | Показывает переменные и их типы в глобальном пространстве.                                  | `%who`                                                                                            |
| `%cd`              | Изменяет текущую рабочую директорию.                                                        | `%cd /path/to/directory`                                                                          |
| `%gui`             | Устанавливает графический интерфейс для бэкенда IPython.                                    | `%gui qt`                                                                                         |
| `%mamba`           | Запускает установку пакетов с помощью Mamba (альтернатива `pip`).                           | `%mamba install numpy`                                                                            |
| `%%prun`           | Выполняет код с профилированием с использованием `cProfile` (для всей ячейки).              | `%%prun`<br>`my_function()`                                                                       |
| `%%ruby`           | Выполняет код `Ruby` в ячейке.                                                              | `%%ruby`<br>`puts "Hello from Ruby"`                                                              |
| `%who_ls`          | Показывает имена всех переменных в глобальном пространстве в виде списка.                   | `%who_ls`                                                                                         |
| `%cls`             | Очищает консольный вывод.                                                                   | `%cls`                                                                                            |
| `%hist`            | Показывает историю ввода.                                                                   | `%hist`                                                                                           |
| `%%markdown`       | Размечает содержимое ячейки как `Markdown`.                                                 | `%%markdown`<br>`# Заголовок`<br>`**Текст**`                                                      |
| `%psearch`         | Поиск по именам символов с использованием шаблона.                                          | `%psearch *function*`                                                                             |
| `%run`             | Запускает внешний скрипт Python или IPython.                                                | `%run my_script.py`                                                                               |
| `%whos`            | Показывает все переменные в текущем пространстве имен и их типы.                            | `%whos`                                                                                           |
| `%%cmd`            | Запускает команды Windows cmd в ячейке.                                                     | `%%cmd`<br>`dir`                                                                                  |
| `%history`         | Показывает историю ввода и вывода.                                                          | `%history -n 1-10`                                                                                |
| `%matplotlib`      | Включает встроенную поддержку matplotlib.                                                   | `%matplotlib inline`                                                                              |
| `%psource`         | Показывает исходный код объекта.                                                            | `%psource my_function`                                                                            |
| `%save`            | Сохраняет ввод и вывод ячейки в файл Python.                                                | `%save my_session.py 1-5`                                                                         |
| `%%writefile`      | Записывает содержимое ячейки в файл.                                                        | `%%writefile my_file.txt`<br>`Hello, World!`                                                      |
| `%code_wrap`       | Устанавливает или отключает авто-перенос строк для вывода кода.                             | `%code_wrap on`                                                                                   |
| `%%html`           | Размечает содержимое ячейки как `HTML`.                                                     | `%%html`<br>`<h1>Hello, World!</h1>`                                                              |
| `%micromamba`      | Запускает установку пакетов с помощью Micromamba (альтернатива `pip`).                      | `%micromamba install numpy`                                                                       |
| `%pushd`           | Добавляет текущую директорию в стек и переходит в новую директорию.                         | `%pushd /path/to/directory`                                                                       |
| `%sc`              | Выполняет код, используя Subprocess.                                                        | `%sc ls -l`                                                                                       |
| `%xdel`            | Удаляет переменные и объекты из сессии IPython.                                             | `%xdel my_variable`                                                                               |
| `%%code_wrap`      | Устанавливает или отключает авто-перенос строк для вывода кода в ячейке.                    | `%%code_wrap on`                                                                                  |
| `%%javascript`     | Выполняет JavaScript код в ячейке (для Jupyter Notebook).                                   | `%%javascript`<br>`console.log("Hello, World!")`                                                  |
| `%mkdir`           | Создает новую директорию.                                                                   | `%mkdir new_directory`                                                                            |
| `%pwd`             | Выводит текущую рабочую директорию.                                                         | `%pwd`                                                                                            |
| `%%script`         | Запускает ячейку с указанным интерпретатором (`bash`, `python`, `ruby`, etc).               | `%%script bash`<br>`ls -l`                                                                        |
| `%xmode`           | Устанавливает уровень подробности трассировки для ошибок.                                   | `%xmode Verbose`                                                                                  |
| `%colors`          | Устанавливает цветовую схему для вывода в IPython.                                          | `%colors Linux`                                                                                   |
| `%%js`             | Выполняет `JavaScript` код в ячейке (для Jupyter Notebook).                                 | `%%js`<br>`console.log("Hello, World!")`                                                          |
| `%notebook`        | Запускает скрипт Python как блокнот Jupyter.                                                | `%notebook script.py`                                                                             |
| `%pycat`           | Показывает содержимое скрипта Python.                                                       | `%pycat script.py`                                                                                |
| `%set_env`         | Устанавливает переменные среды для текущей сессии IPython.                                  | `%set_env PATH=/new/path`                                                                         |
| `%conda`           | Взаимодействует с conda для управления окружением и пакетами.                               | `%conda install numpy`                                                                            |
| `%killbgscripts`   | Останавливает все фоновые процессы выполнения скриптов.                                     | `%killbgscripts`                                                                                  |
| `%page`            | Отображает содержимое объекта с поддержкой постраничного просмотра.                         | `%page large_object`                                                                              |
| `%pylab`           | Загружает `matplotlib` и numpy для интерактивной работы в IPython.                          | `%pylab`                                                                                          |
| `%%sh`             | Выполняет команды `Shell` (sh) в ячейке.                                                    | `%%sh`<br>`ls -l`                                                                                 |
| `%config`          | Конфигурирует IPython и его расширения.                                                     | `%config IPCompleter.greedy=True`                                                                 |
| `%%latex`          | Размечает содержимое ячейки как `LaTeX`.                                                    | `%%latex`<br>`\begin{equation}`<br>`E = mc^2`<br>`\end{equation}`                                 |
| `%paste`           | Вставляет и выполняет блок кода, считанный из буфера обмена.                                | `%paste`                                                                                          |
| `%%pypy`           | Выполняет код Python с использованием интерпретатора `PyPy`.                                | `%%pypy`<br>`print("Hello, PyPy!")`                                                               |
| `%store`           | Сохраняет переменные в файл между сеансами IPython.                                         | `%store my_variable`                                                                              |
| `%copy`            | Копирует файлы между локальной файловой системой и файловой системой `Jupyter Notebook`.    | `%copy my_file.txt another_directory/`                                                            |
| `%ldir`            | Список файлов и директорий в локальной файловой системе.                                    | `%ldir`                                                                                           |
| `%pastebin`        | Отправляет содержимое ячейки на `Pastebin` и возвращает `URL`.                              | `%pastebin`                                                                                       |
| `%%python`         | Выполняет код Python в ячейке.                                                              | `%%python`<br>`print("Hello, Python!")`                                                           |
| `%%svg`            | Размечает содержимое ячейки как `SVG` (Scalable Vector Graphics).                           | `%%svg`<br>`<svg height="100" width="100"> ... </svg>`                                            |

""",
                "File formats": """
# Основные форматы файлов

| Формат файла | Описание                                                                                                                                                                   |
|--------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `.py`        | Основной исходный файл Python. Интерпретируются Python напрямую                                                                                                            |
| `.pyi`       | Файлы с аннотациями типов (типовыми подсказками). Используются для статического анализа кода и проверки типов                                                              |
| `.pyc`       | Скомпилированные файлы Python.<br>Генерируются автоматически при импорте `.py` файлов.<br>Эти файлы содержат байт-код, который интерпретируется виртуальной машиной Python |
| `.pyo`       | **Устаревший** формат для скомпилированных файлов с оптимизацией.<br>В новых версиях Python не используется, заменён на `.pyc` с флагом оптимизации                        |
| `.pyw`       | Аналог `.py`, но используется для запуска Python-скриптов на Windows без открытия консольного окна                                                                         |
| `.pyz`       | Сжатые архивы, содержащие Python-программу в формате `ZIP`.<br>Используются для упрощённого распространения и запуска Python-программ                                      |
| `.pyd`       | Файлы расширений Python для `Windows` (аналог `.so` на Linux).<br>Это динамически загружаемые библиотеки, написанные на `C` или `C++` и используемые в Python              |
| `.pxd`       | Заголовочные файлы для `Cython`, аналог `.h` файлов в `C`/`C++`.<br>Используются для объявления C-функций и структур, которые могут быть использованы в Cython-коде        |
| `.pyx`       | Исходные файлы для Cython, расширение Python.<br>Эти файлы компилируются в C-код и могут использоваться для повышения производительности Python-программ                   |

# .py
Содержат исходный код на языке Python
Они могут включать определения функций, классов, переменных и другие конструкции, поддерживаемые Python
Эти файлы интерпретируются напрямую интерпретатором Python

```python@script.py
# script.py
def hello_world():
    print("Hello, World!")
```

Этот файл можно запустить командой `python script.py` в командной строке

# .pyi
Используются для добавления аннотаций типов к Python-коду
Эти файлы позволяют статическим анализаторам кода (например, `MyPy`)
проверять корректность типов без выполнения самого кода

```python@module.pyi
# module.pyi
def hello_world() -> None: ...
```

Этот файл используется только для типизации и не выполняется непосредственно

# .pyc
Содержат скомпилированный байт-код Python, который создаётся автоматически при импорте `.py` файлов
Этот байт-код интерпретируется виртуальной машиной Python и ускоряет выполнение программы

Когда вы импортируете модуль `import script`, Python автоматически создаёт файл `script.pyc` в директории `__pycache__`.

# .pyo
Использовались в старых версиях Python (до `3.5`) для хранения скомпилированного байт-кода с включенной оптимизацией
В новых версиях Python этот формат заменён на `.pyc` с флагом оптимизации

# .pyw
Аналогичны `.py`, но предназначены для запуска скриптов на `Windows` без открытия консольного окна
Обычно используются для создания графических приложений на Python

```python@script.pyw
# script.pyw
import tkinter as tk

root = tk.Tk()
label = tk.Label(root, text="Hello, World!")
label.pack()
root.mainloop()
```
Запуск `script.pyw` на Windows не откроет консольное окно

# .pyz
ZIP-архивы, которые могут содержать Python-программы
Они позволяют упаковать несколько модулей и пакетов в один файл для удобства распространения и выполнения

Вы можете создать `.pyz` файл с помощью утилиты [[Languages/Python/Libraries/Python/zipapp.md]]

```bash
python -m zipapp my_app -o my_app.pyz
```

Запуск `python my_app.pyz` выполнит программу, упакованную в архив

# .pyd
Динамически загружаемые библиотеки (`DLL`),
написанные на `C` или `C++` и используемые как модули Python
Они позволяют использовать высокопроизводительный код, написанный на других языках

Вы можете создать `.pyd` файл, используя компилятор `C` или `C++` с поддержкой `Python API`

# .pxd
Используются в `Cython` для объявления C-функций и структур, которые будут использоваться в Cython-коде
Они аналогичны `.h` файлам в `C`/`C++`
```cython@header.pxd
# header.pxd
cdef extern from "math.h":
    double sin(double x)
```

# .pyx
Содержат исходный код на Cython, который представляет собой надстройку над Python,
позволяющую компилировать код в `C` для повышения производительности.

```cython@module.pyx
# module.pyx
def sin_cos(double x):
    return sin(x), cos(x)
```

Этот файл можно скомпилировать в `C` и подключить как модуль в Python.
""",
            },
            "Generators and lists": {
                "for in list comprehension": """
```python
list_of_tuples = [(1, 2), (3, 4), (5, 6)]
result_list = [
    item
    for tpl in list_of_tuples
    for item in tpl
]
print(result_list)
[1, 2, 3, 4, 5, 6]
```
```python
list_of_tuples = [(1, 2), (3, 4), (5, 6)]
result_list = []
for tpl in list_of_tuples:
    for item in tpl:
        result_list.append(item)

print(result_list)
[1, 2, 3, 4, 5, 6]
```
""",
                "yield from": """
# yield from

Это выражение, которое позволяет делегировать выполнение
генератора другому генератору, который называется **подгенератором**. 
Это означает, что когда генератор встречает выражение `yield from` с указанием **подгенератора**,
он передает управление этому **подгенератору**, 
который затем возвращает значения генерируемых им элементов непосредственно в генератор-делегат.

Кроме того, `yield from` позволяет пропустить передачу через промежуточный уровень вложенности. 
Это означает, что когда подгенератор завершает свою работу, управление передается автоматически обратно генератору-делегату. 
Это может быть полезно в случаях, когда вы хотите объединить несколько генераторов вместе,
чтобы создать новый генератор, который генерирует элементы из каждого из них.

Вот пример, который демонстрирует использование yield from:

```python
def generator1():
    yield "A"
    yield "B"
    yield "C"

def generator2():
    yield "D"
    yield from generator1()
    yield "E"
    yield "F"

[letter for letter in generator2()]
# ["D", "A", "B", "C", "E", "F"]
```

Здесь `generator2` создает новый генератор, используя `yield from` 
для вызова генератора `generator1` и объединения его с другими элементами, которые генерирует `generator2`. 
Когда `generator1` завершает свою работу, управление автоматически возвращается обратно в `generator2`,
который продолжает генерировать свои элементы.
""",
                "Multiplication of lists": """
```pycon
>>> a = [[]]*3
>>> for x in a:
...     print(id(x))
...
3276075832448
3276075832448
3276075832448
>>> a[1].append(1)
>>> a
[[1], [1], [1]]
>>>
>>> b = [[] for _ in range(3)]
>>> for x in b:
...     print(id(x))
...
3276075828928
3276075828992
3276075828864
>>> b[1].append(1)
>>> b
[[], [1], []]
>>>
>>> c = [[]]
>>> print(id(c[0]))
3276075894784
>>> for x in (c + c):
...     print(id(x))
...
3276075894784
3276075894784
>>>
>>> d = ((),)*3
>>> for x in d:
...     print(id(d))
...
3276075830656
3276075830656
3276075830656
```
""",
            },
            "Built-in": {
                "Built-in functions": r"""

## slice

```python
print([1, 2, 3, 4, 5][1:4])  # [2, 3, 4]
print([1, 2, 3, 4, 5][slice(1, 4)])  # [2, 3, 4]
```

## frozenset
Неизменяемый тип данных, представляющий собой неупорядоченное множество уникальных элементов.

```python
print(frozenset([1, 2, 2, 3, 4]))  # frozenset({1, 2, 3, 4})
```

## memoryview
Доступ к буферу памяти объекта без копирования его данных.

```pycon
>>> mv = memoryview(bytearray("ABC", "UTF-8"))
>>> mv[0]           # доступ к нулевому индексу представления памяти
65
>>> bytes(mv[0:2])  # создать байт из представления памяти
b"AB"
>>> list(mv[0:3])   # создать список из представления памяти
[65, 66, 67]
```

## hasattr
Для проверки наличия атрибута (метода или свойства) у объекта.

```python
class MyClass:
    def __init__(self):
        self.my_attr = 42

my_obj = MyClass()
print(hasattr(my_obj, "my_attr"))  # True
print(hasattr(my_obj, "non_existent_attr"))  # False
```

## reversed
Для переворачивания последовательности (sequence).

```python
my_list = [1, 2, 3, 4, 5]
reversed_list = reversed(my_list)
print(list(reversed_list))  # [5, 4, 3, 2, 1]
```

## &#95;&#95;import&#95;&#95;
Для импорта модуля во время выполнения программы.

```python
math = __import__("math")
print(math.pi)  # 3.141592653589793
```

## staticmethod
Для создания метода класса, который не принимает первый аргумент self (или cls для методов класса).

```python
class MyClass:
    @staticmethod
    def my_static_method():
        print("This is a static method")

MyClass.my_static_method()  # This is a static method
```

## setattr
Для установки значения атрибута объекта.

```python
class MyClass:
    def __init__(self):
        self.my_attr = 42

my_obj = MyClass()
setattr(my_obj, "my_attr", 43)
print(my_obj.my_attr)  # 43
```

## property
Для создания свойства объекта, которое можно читать и записывать, как обычный атрибут.

```python
class MyClass:
    def __init__(self):
        self._my_attr = 42

    @property
    def my_attr(self):
        return self._my_attr

    @my_attr.setter
    def my_attr(self, value):
        self._my_attr
```

## object
Базовый класс, от которого наследуются все остальные классы в Python.

```python
class MyClass(object):
    pass
```

## locals
Для получения словаря с локальными переменными в текущем контексте выполнения.

```python
def my_func():
    a = 1
    b = 2
    print(locals())

my_func()  # {"a": 1, "b": 2}
```

## globals
Для получения словаря с глобальными переменными в текущем модуле.

```python
my_var = 42
print(globals())  # {"__name__": "__main__", "__doc__": None, "__package__": None, "my_var": 42, ...}
```

## getattr
Для получения значения атрибута объекта по его имени.

```python
class MyClass:
    def __init__(self):
        self.my_attr = 42

print(getattr(MyClass(), "my_attr"))  # 42
```

## complex
Для создания комплексного числа.

```python
print(complex(1, 2))  # (1+2j)
```

## compile
Для компиляции строки с кодом Python в объект-код.

```python
exec(compile('print("Hello, world!")', "<string>", "exec"))  # Hello, world!
```

## bytearray
Изменяемый тип данных, представляющий собой массив байтов.
Последовательность целых чисел в диапазоне `0 ≤ X < 256`

Параметр **source** можно использовать для начальной инициализации массива:
Если source является строкой, вы также должны указать кодировку encoding и опционально **errors**
Если source является целым числом, массив будет иметь размер **source** и инициализирован байтами со значением `0`
Если source является объектом, то он должен поддерживать интерфейс буфера.
Для инициализации массива байт будет использован буфер, предназначенный для чтения.
Если **source** является итерируемым объектом, его элементами должны быть целыми числами в диапазоне `0 ≤ X < 256`.
Этими числами и будет инициализирован массив.
Если **source** не передан, вернет пустой **bytearray**

```pycon
>>> bytearray("Привет, Python!", "UTF-8")  
bytearray(b"\xd0\x9f\xd1\x80\xd0\xb8\xd0\xb2\xd0\xb5\xd1\x82, Python!")
>>> bytearray(5)
bytearray(b"\x00\x00\x00\x00\x00")
>>> bytearray([1, 2, 3])
bytearray(b"\x01\x02\x03")
```

## abs
Получения абсолютного значения числа.

```python
print(abs(-42))  # 42
```

## bin
Получения двоичного представления числа.

```python
print(bin(42))  # 0b101010
```

## bytes
Неизменяемый тип данных, представляющий собой массив байтов.

```python
print(bytes([1, 2, 3, 4, 5]))  # b"\x01\x02\x03\x04\x05"
```

## callable
Является ли объект вызываемым (т.е. функцией или методом).

```python
def my_func():
    pass

class MyClass:
    def my_method(self):
        pass

print(callable(my_func))  # True
print(callable(MyClass().my_method))  # True
print(callable(42))  # False
```

## chr
Получение символа Unicode по его коду.

```python
print(chr(97))  # "a"
```

## classmethod
Создание метода класса. Этот метод может быть вызван без создания экземпляра класса.

```python
class MyClass:
    my_class_attr = 42

    @classmethod
    def my_class_method(cls):
        print(cls.my_class_attr)

MyClass.my_class_method()  # 42
```

## delattr
Удаление атрибута объекта.

```python
class MyClass:
    my_attr = 42

my_obj = MyClass()
delattr(my_obj, "my_attr")
print(hasattr(my_obj, "my_attr"))  # False
```

## dir
Получение списка всех атрибутов объекта.

```python
print(dir([1, 2, 3]))  # ["__add__", "__class__", "__contains__", ...]
```

## divmod
Получения частного и остатка от деления двух чисел.

```python
print(divmod(42, 5))  # (8, 2)
```

## filter
Фильтрация элементов последовательности с помощью функции.

```python
print(list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5])))  # [2, 4]
```

## oct
Получение восьмеричного представления числа.

```python
print(oct(42))  # 0o52
```

## nonlocal
Объявление переменной из внешней области видимости внутри функции.

```python
def my_func():
    my_var = 42
    def inner_func():
        nonlocal my_var
        my_var = 43
    inner_func()
    print(my_var)

my_func()  # 43
```
""",
                "Exception": """
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


EncodingWarning
EnvironmentError
IOError
WindowsError
```

""",
                "ExceptionGroup": """
ExceptionGroup в Python появился в версии 3.11
Позволяет объединять несколько исключений в одно


### Пример 1: Создание ExceptionGroup

```python
try:
    raise ExceptionGroup("Ошибка выполнения операций", [
        ValueError("Некорректное значение"),
        TypeError("Неверный тип данных"),
        KeyError("Ключ не найден")
    ])
except ExceptionGroup as eg:
    print(f"Произошло {len(eg.exceptions)} исключений:")
    for exc in eg.exceptions:
        print(f"- {exc.__class__.__name__}: {exc}")
```

<details>
<summary>output</summary>

```
Произошло 3 исключений:
- ValueError: Некорректное значение
- TypeError: Неверный тип данных
- KeyError: 'Ключ не найден'
```

</details>

### Пример 2: Обработка отдельных исключений внутри группы

```python
try:
    raise ExceptionGroup("Ошибка выполнения операций", [
        ValueError("Некорректное значение"),
        TypeError("Неверный тип данных"),
        KeyError("Ключ не найден")
    ])
except* ValueError as v_errors:
    for error in v_errors:
        print(f"Обработан ValueError: {error}")
except* TypeError as t_errors:
    for error in t_errors:
        print(f"Обработан TypeError: {error}")
```

<details>
<summary>output</summary>

```
  | ExceptionGroup:  (3 sub-exceptions)
  +-+---------------- 1 ----------------
    | Exception Group Traceback (most recent call last):
    |   File "<stdin>", line 2, in <module>
    | ExceptionGroup: Ошибка выполнения операций (1 sub-exception)
    +-+---------------- 1 ----------------
      | ValueError: Некорректное значение
      +------------------------------------
    |
    | During handling of the above exception, another exception occurred:
    |
    | Traceback (most recent call last):
    |   File "<stdin>", line 8, in <module>
    | TypeError: 'ExceptionGroup' object is not iterable
    +---------------- 2 ----------------
    | Exception Group Traceback (most recent call last):
    |   File "<stdin>", line 2, in <module>
    | ExceptionGroup: Ошибка выполнения операций (1 sub-exception)
    +-+---------------- 1 ----------------
      | TypeError: Неверный тип данных
      +------------------------------------
    |
    | During handling of the above exception, another exception occurred:
    |
    | Traceback (most recent call last):
    |   File "<stdin>", line 11, in <module>
    | TypeError: 'ExceptionGroup' object is not iterable
    +---------------- 3 ----------------
    | Exception Group Traceback (most recent call last):
    |   File "<stdin>", line 2, in <module>
    | ExceptionGroup: Ошибка выполнения операций (1 sub-exception)
    +-+---------------- 1 ----------------
      | KeyError: 'Ключ не найден'
      +------------------------------------
```

</details>


### Пример 3: Вложенные ExceptionGroup

```python
try:
    raise ExceptionGroup("Основная группа", [
        ExceptionGroup("Первая подгруппа", [
            ValueError("Некорректное значение"),
            KeyError("Ключ не найден")
        ]),
        TypeError("Неверный тип данных")
    ])
except ExceptionGroup as eg:
    print(f"Основная группа исключений: {eg}")
    for exc in eg.exceptions:
        print(f"- {exc}")
```

<details>
<summary>output</summary>

```
Основная группа исключений: Основная группа (2 sub-exceptions)
- Первая подгруппа (2 sub-exceptions)
- Неверный тип данных
```

</details>

### Пример 4: Комбинирование и повторное создание ExceptionGroup

```python
def function_that_raises():
    errors = []
    try:
        raise ValueError("Первый ValueError")
    except ValueError as e:
        errors.append(e)

    try:
        raise TypeError("Первый TypeError")
    except TypeError as e:
        errors.append(e)

    if errors:
        raise ExceptionGroup("Группа исключений в функции", errors)

try:
    function_that_raises()
except ExceptionGroup as eg:
    print(f"Обработан ExceptionGroup: {eg}")
    for exc in eg.exceptions:
        print(f"- {exc}")
```
<details>
<summary>output</summary>

```
Обработан ExceptionGroup: Группа исключений в функции (2 sub-exceptions)
- Первый ValueError
- Первый TypeError
```

</details>
""",
                "metaclass": '''
**Метаклассы** в Python — это классы, которые создают другие классы.
Они определяют, как классы будут создаваться и как будут вести себя в процессе их создания.

Метакласс — это класс, который наследует от `type`. Он управляет созданием и поведением других классов.
`type` — встроенный метакласс, который является метаклассом для всех классов в Python.

```python
class MyMeta(type):
    def __new__(cls, name, bases, dct):
        print(f"Creating class {name}")
        return super().__new__(cls, name, bases, dct)


class MyClass(metaclass=MyMeta):
   pass


obj = MyClass()  # При создании класса MyClass вызовется MyMeta.__new__
```

`__new__(cls, name, bases, dct)` — создаёт новый класс.

- `name` — имя создаваемого класса.
- `bases` — кортеж базовых классов.
- `dct` — словарь, содержащий атрибуты класса.

`__init__(cls, name, bases, dct)` — инициализирует созданный класс.
Можно использовать для добавления атрибутов или методов.


### Пример метакласса с изменением поведения

```python
class AddHelloMeta(type):
    """
    Автоматически добавляет метод hello
    """
    def __new__(cls, name, bases, dct):
        dct["hello"] = lambda self: "Hello, world!"
        return super().__new__(cls, name, bases, dct)


class MyClass(metaclass=AddHelloMeta):
   pass


obj = MyClass()
print(obj.hello())  # Hello, world!
```


### Пример [[General/Паттерны%20проектирования/Порождающие%20паттерны/Singleton%20(Одиночка).md]] с использованием метакласса

```python
class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class Singleton(metaclass=SingletonMeta):
    pass


a = Singleton()
b = Singleton()
print(a is b)  # True
```
''',
            },
            "operator precedence": """
Приоритетность операторов от высокой до самой низкой.

| Операторы                                                    | Применение                                 |
|--------------------------------------------------------------|--------------------------------------------|
| `{}` `()`                                                    | Скобки (объединение)                       |
| `f(args)`                                                    | Вызов функции                              |
| `x[index:index]`                                             | Срез                                       |
| `x[index]`                                                   | Получение по индексу                       |
| `x.attribute`                                                | Ссылка на атрибут                          |
| `**`                                                         | Возведение в степень                       |
| `~x` `+x` `-x`                                               | Положительное, отрицательное число         |
| `*` `/` `//` `%`                                             | Умножение, деление, остаток                |
| `+` `—`                                                      | Сложение, вычитание                        |
| `<<` `>>`                                                    | Сдвиг влево/вправо                         |
| `&`                                                          | Побитовое **И**                            |
| `^`                                                          | Побитовое **ИЛИ** **НЕ**                   |
| `|`                                                          | Побитовое **ИЛИ**                          |
| `in` `not in` `is` `is not` `<` `<=` `>` `>=` `<>` `!=` `==` | Сравнение, принадлежность, тождественность |
| `not`                                                        | Булево **НЕ**                              |
| `and`                                                        | Булево **И**                               |
| `or`                                                         | Булево **ИЛИ**                             |
| `lambda`                                                     | Лямбда-выражение                           |

""",
            "fstrings": """
# F-Strings

**F-строки** - это новый способ форматирования строк в Python 3.6 и выше. 
Они позволяют встраивать выражения Python внутри строк посредством указания их в `{}` внутри строки, заключенной в `f`.


> replacement_field ::=  "{" [field_name] ["!" conversion] [":" format_spec] "}"
>
> field_name        ::=  arg_name ("." attribute_name | "[" element_index "]")*
> arg_name          ::=  [identifier | digit+]
> attribute_name    ::=  identifier
> element_index     ::=  digit+ | index_string
> index_string      ::=  <любой исходный символ, кроме "]"> +
> 
> conversion        ::=  "r" | "s" | "a"
> 
> format_spec       ::=  [[fill]align][sign][#][0][width][grouping_option][.precision][type]
> fill              ::=  <any character>
> align             ::=  "<" | ">" | "=" | "^"
> sign              ::=  "+" | "-" | " "
> width             ::=  digit+
> grouping_option   ::=  "_" | ","
> precision         ::=  digit+
> type              ::=  "b" | "c" | "d" | "e" | "E" | "f" | "F" | "g" | "G" | "n" | "o" | "s" | "x" | "X" | "%"

## Field_name

Выражение формы `".name"` выбирает именованный атрибут с помощью `getattr()`
Выражение формы `"[index]"` выполняет поиск по индексу с использованием `getitem()`


## Conversion

Вызывает приведение типа перед форматированием

| conversion |         |
|:----------:|---------|
| `!s`       | str()   |
| `!r`       | repr()  |
| `!a`       | ascii() |
| `!e`       | **Python 3.12** |


## Format_spec

Содержит спецификацию того, как должно быть представлено значение,
Включая такие детали, как ширина поля, выравнивание, заполнение, десятичная точность и т. д.
Каждый тип значения может определять свой собственный **мини-язык форматирования** или интерпретацию `format_spec`.

### Fill

Невозможно использовать литеральную фигурную скобку `{` или `}` в качестве символа `fill`
в форматированном строковом литерале или при использовании метода `str.format()`.
<details>
    <summary><b>Однако можно вставить фигурную скобку с вложенным полем замены.</b></summary>
```pycon
>>> f"{1:}>20}"
  File "<stdin>", line 1
    f"{1:}>20}"
               ^
SyntaxError: f-string: single '}' is not allowed
>>> f"{1:}}>20}"
  File "<stdin>", line 1
    f"{1:}}>20}"
                ^
SyntaxError: f-string: single '}' is not allowed
>>> f"{1:{'}'}>20}"
"}}}}}}}}}}}}}}}}}}}1"```
</details>
Это ограничение не влияет на функцию `format()`.


### Align

| Вариант        | Значение |
|:--------------:|----------|
| **`<`**        | Выравнивает поле по левому краю в доступном пространстве<br>**По умолчанию для большинства объектов** |
| **`>`**        | Принудительно выравнивает поле по правому краю в доступном пространстве<br>**По умолчанию для чисел** |
| **`^`**        | Центрирует поле в доступном пространстве |


### Sign

Действителен только для числовых типов.

| Вариант        | Значение |
|:--------------:|----------|
| **`+`**          | Указывает, что знак должен использоваться как для положительных, так и для отрицательных чисел.                                                                                                                                                                                                                       |
| **`-`**          | Указывает, что знак следует использовать только для отрицательных чисел<br>**Поведение по умолчанию**.                                                                                                                                                                                                                 |
| **`=`**          | Принудительно размещает заполнение после знака (если есть), но перед цифрами.<br>Это используется для печати полей в форме `+000000120`.<br>Этот параметр выравнивания действителен только для числовых типов.<br>Он становится значением по умолчанию для чисел, когда `0` непосредственно предшествует ширине поля. |
| **__Пробел__** | Указывает, что ведущий пробел должен использоваться на положительных числах, а знак минус на отрицательных числах.                                                                                                                                                                                                    |


### &#x23;

**#** - Приводит к использованию **альтернативной формы** для преобразования.
    Альтернативная форма определяется по-разному для разных типов.
    Этот параметр действителен только для **целых**, **плавающих** и **сложных** типов.
    Для целых чисел, когда используется **двоичный**, **восьмеричный** или **шестнадцатеричный** вывод,
    эта опция добавляет соответствующий префикс `0b`, `0o`, `0x` или `0X` к выходному значению.<br>
    Для чисел с **плавающей запятой** и **сложных** альтернативная форма приводит к тому, что результат
    преобразования всегда содержит символ десятичной точки, **даже если за ним не следуют цифры**.
    Обычно символ десятичной точки появляется в результате этих преобразований только в том случае, если за ним следует цифра.
    **Кроме того, для преобразований `g` и `G` конечные нули не удаляются из результата.**


### 0

**,** - Сигнализирует об использовании запятой для разделителя тысяч.
    Для разделителя с учётом языкового стандарта использовать вместо него целочисленный тип представления `n`
**_** - Сигнализирует об использовании подчеркивания для разделителя тысяч для типов представления с плавающей запятой
    и для целочисленного типа представления `d`.
    Для целочисленных типов представления `b`, `o`, `x` и `X` символы подчеркивания вставляются каждые 4 цифры.
    Для других типов представлений указание этой опции является ошибкой.


### Width

Десятичное целое число, определяющее минимальную общую ширину поля,
включая любые префиксы, разделители и другие символы форматирования.
Если не указан, то ширина поля будет определяться содержимым.

Если явное выравнивание не задано, то перед полем `width` нулевым `0` символом
включается знаковое заполнение нулями для числовых типов.
Это эквивалентно `fill` символу `0` с типом alignment `=`.

Точность представляет собой десятичное целое число , указывающее, сколько цифр должно отображаться после десятичной 
точки для типов представления `f` и `F`, или до и после десятичной точки для типов представления `g` или `G`. 
Для типов строкового представления поле указывает максимальный размер поля, другими словами, сколько символов 
будет использовано из содержимого поля. Точность не допускается для целочисленных типов представления .


### Precision

Десятичное число, указывающее, сколько цифр должно отображаться после десятичной точки
для значения с плавающей запятой, отформатированного с помощью `f` и `F`,
или до и после десятичной точки для значения с плавающей запятой, отформатированного с помощью `g` или `G`.
Для нечисловых типов поле указывает максимальный размер поля — другими словами,
сколько символов будет использовано из содержимого поля.
`precision` не допускается для целочисленных значений.


### Type

Определяет, как данные должны быть представлены.

#### 1. Доступные типы представления строк

| Тип   | Значение |
|:-----:|----------|
| `s` | Формат строки. Это тип по умолчанию для строк, и его можно опустить. |
| None  | То же, что `s`. |


#### 2. Доступные типы целочисленного представления

| Тип   | Значение |
|:-----:|----------|
| **`b`** | Двоичный формат |
| **`c`** | Преобразует целое число в соответствующий символ Юникода перед печатью |
| **`d`** | Десятичное целое число |
| **`o`** | Восьмеричный формат |
| **`x`** | Шестнадцатеричный формат. Использует строчные буквы для цифр выше `9` |
| **`X`** | Шестнадцатеричный формат. Использует прописные буквы для цифр выше `9` |
| **`n`** | Число. Это то же самое, что и `d`, за исключением того,<br>что для вставки соответствующих символов-разделителей чисел он использует текущую настройку локали. |
| None  | То же, что `d` |

#### 3. Доступные типы представления для `float` и `Decimal` значений

| Тип      | Значение |
|:--------:|----------|
| **`e`**    | Научная нотация.<br>Для заданной точности `p` форматирует число в **экспоненциальном представлении** с буквой «`e`», отделяющей **`p` цифр коэффициента** от экспоненты.<br>Коэффициент состоит из одной цифры перед и после десятичной точки, всего `p + 1` значащих цифр.<br>Если точность не указана, используется точность **6 цифр** после десятичной точки для `float`<br>и отображаются все цифры коэффициентов для `Decimal`.<br>Если после десятичной точки нет цифр, десятичная точка также удаляется,<br>если не используется опция `#` |
| **`E`**    | Научная нотация.<br>То же, что и `e`, за исключением того, что в качестве символа-разделителя используется заглавная буква «`E`» |
| **`f`**    | Запись с фиксированной точкой.<br>Для заданной точности `p` форматирует число как десятичное с точностью `p` цифр после десятичной точки.<br>Если точность не указана, используется точность **6 цифр** после десятичной точки для `float`<br>и используется точность, достаточно большая для отображения всех цифр коэффициентов для `Decimal`.<br>Если после десятичной точки нет цифр, десятичная точка также удаляется,<br>если не используется опция `#` |
| **`F`**    | Представление с фиксированной точкой.<br>То же, что и `f`, но преобразует `nan` в `NAN` и `inf` в `INF` |
| **`g`**    | Общий формат.<br>Для заданной точности `p >= 1` округляет число до `p` значащих цифр и затем форматирует результат либо в формате с фиксированной точкой,<br>либо в научном представлении, в зависимости от его величины.<br><br>Точные правила следующие: предположим, что результат отформатирован с типом представления `e` и `p-1` точности, будет с exp экспонентой.<br>Затем, если `m <= exp < p`, где `m` равно `-4` для `floats` и `-6` для `Decimals`,<br>число форматируется с типом представления `f` и точностью `p-1-exp`.<br>В противном случае номер форматируется с помощью `e` типа представления и `p-1` точности.<br>В обоих случаях из значащего удаляются незначительные конечные нули, а десятичная точка также удаляется, если после неё нет оставшихся цифр,<br>если не используется опция `#`.<br><br>Без указания точности использует точность **`6` значащих цифр** для `float`.<br>Для `Decimal` коэффициент результата формируется из цифр коэффициента значения;<br>экспоненциальная нотация используется для значений, меньших, чем `1e-6` по абсолютной величине, и значений,<br>в которых разряд наименее значащей цифры больше 1, а в противном случае используется нотация с фиксированной точкой.<br><br>Положительные и отрицательные бесконечности, положительный и отрицательный ноль и `nan`,<br>форматируются как `inf`, `-inf`, `0`, `-0` и `nan` соответственно, независимо от точности |
| **`G`**    | Общий формат.<br>То же, что и `g`, за исключением переключения на `E`, если число становится слишком большим.<br>Представления бесконечности и `NaN` также в верхнем регистре. |
| **`n`**    | Номер.<br>Это то же самое, что и `g`, за исключением того, что он использует текущую настройку локали<br>для вставки соответствующих символов разделителя чисел. |
| **`%`**    | Процент.<br>**Умножает число на `100` и отображает в фиксированном `f` формате**, за которым следует знак процента. |
| **None** | Для `float` это то же самое, что и для `g`,<br>за исключением того, что когда для форматирования результата используется запись с фиксированной точкой,<br>она всегда включает как минимум одну цифру после десятичной точки.<br>Используемая точность настолько велика, насколько это необходимо для точного представления заданного значения.<br><br>Для Decimal это то же самое, что `g` или `G` в зависимости от значения `context.capitals` для текущего десятичного контекста.<br><br>Общий эффект заключается в том, чтобы соответствовать выходным данным `str()`, измененному другими модификаторами формата. |


Примеры простых форматных строк:
```python
"Сначала посчитай до {0}"         # Ссылки на первый позиционный аргумент
"Принеси мне {}"                  # Неявно ссылается на первый позиционный аргумент
"От {} до {}"                     # То же, что "От {0} до {1}"
"Мой квест {name}"                # Ссылка на ключевой аргумент «name»
"Масса в тоннах {0.weight}"       # атрибут «weight» первого позиционного аргумента
"Уничтожено единиц: {players[0]}" # Первый элемент ключевого аргумента «players».

"Гарольд умный {0!s}"             # Сначала вызывает str() для первого аргумента
"Принесите святую {name!r}"       # Сначала вызывает repr() для первого аргумента
"Больше {!a}"                     # Сначала вызывает ascii() для первого аргумента
```


Доступ к аргументам по позиции:

```pycon
>>> "{0}, {1}, {2}".format("a", "b", "c")
"a, b, c"
>>> "{}, {}, {}".format("a", "b", "c")  # 3.1+ python version only
"a, b, c"
>>> "{2}, {1}, {0}".format("a", "b", "c")
"c, b, a"
>>> "{2}, {1}, {0}".format(*"abc")      # unpacking argument sequence
"c, b, a"
>>> "{0}{1}{0}".format("abra", "cad")   # arguments indices can be repeated
"abracadabra"
```

Доступ к аргументам по имени:

```pycon
>>> "Coordinates: {latitude}, {longitude}".format(latitude="37.24N", longitude="-115.81W")
"Coordinates: 37.24N, -115.81W"
>>> coord = {"latitude": "37.24N", "longitude": "-115.81W"}
>>> "Coordinates: {latitude}, {longitude}".format(**coord)
"Coordinates: 37.24N, -115.81W"
```

Доступ к атрибутам аргументов:

```pycon
>>> c = 3-5j
>>> (
...     "The complex number {0} is formed from the real part {0.real} "
...     "and the imaginary part {0.imag}."
... ).format(c)
"The complex number 3-5j is formed from the real part 3.0 and the imaginary part -5.0."
```
```pycon
>>> class Point:
...     def __init__(self, x, y):
...         self.x, self.y = x, y
...     def __str__(self):
...         return "Point({self.x}, {self.y})".format(self=self)
...
>>> str(Point(4, 2))
"Point(4, 2)"
```

Доступ к элементам аргументов:

```pycon
>>> "X: {0[0]};  Y: {0[1]}".format((3, 5))
"X: 3;  Y: 5"
```
Замена `%s` и `%r`:
```pycon
>>> "repr() shows quotes: {!r}; str() doesn't: {!s}".format("test1", "test2")
"repr() shows quotes: 'test1'; str() doesn't: test2"
```

Выравнивание текста и указание ширины:

```pycon
>>> "{:<30}".format("left aligned")
"left aligned                  "
>>> "{:>30}".format("right aligned")
"                 right aligned"
>>> "{:^30}".format("centered")
"           centered           "
>>> "{:*^30}".format("centered")  # use "*" as a fill char
"***********centered***********"
```

Замена `%+f`, `%-f`, и и указание знака: `%` `f`

```pycon
>>> "{:+f}; {:+f}".format(3.14, -3.14)  # show it always
"+3.140000; -3.140000"
>>> "{: f}; {: f}".format(3.14, -3.14)  # show a space for positive numbers
" 3.140000; -3.140000"
>>> "{:-f}; {:-f}".format(3.14, -3.14)  # show only the minus -- same as "{:f}; {:f}"
"3.140000; -3.140000"
>>> 
>>> "{:-.2f}; {:-.2f}".format(3.14, -3.14)
"3.14; -3.14"
```

Замена `%x` и `%o` преобразование значения в разные базы:

```pycon
>>> # format also supports binary numbers
>>> "int: {0:d};  hex: {0:x};  oct: {0:o};  bin: {0:b}".format(42)
"int: 42;  hex: 2a;  oct: 52;  bin: 101010"
>>> # with 0x, 0o, or 0b as prefix:
>>> "int: {0:d};  hex: {0:#x};  oct: {0:#o};  bin: {0:#b}".format(42)
"int: 42;  hex: 0x2a;  oct: 0o52;  bin: 0b101010"
```

Использование запятой или подчёркивания в качестве разделителя тысяч:

```pycon
>>> "{:,}".format(1234567890)
"1,234,567,890"
>>> "{:_}".format(1234567890)
"1_234_567_890"
```

Выражение процента:

```pycon
>>> points, total = 19, 22
>>> "Correct answers: {:.2%}".format(points/total)
"Correct answers: 86.36%"
```

Использование форматирования для конкретного типа:

```pycon
>>> from datetime import datetime
>>> "{:%Y-%m-%d %H:%M:%S}".format(datetime(2010, 7, 4, 12, 15, 58))
"2010-07-04 12:15:58"
```

Вложенные аргументы и более сложные примеры:

```pycon
>>> for align, text in zip("<^>", ["left", "center", "right"]):
...    "{0:{fill}{align}16}".format(text, fill=align, align=align)
...
"left<<<<<<<<<<<<"
"^^^^^center^^^^^"
">>>>>>>>>>>right"
>>> octets = [192, 168, 0, 1]
>>> "{:02X}{:02X}{:02X}{:02X}".format(*octets)
"C0A80001"
>>> int(_, 16)
3232235521
>>> width = 5
>>> for num in range(5,12): 
...     for base in "dXob":
...         print("{0:{width}{base}}".format(num, base=base, width=width), end=" ")
...     print()
... 
    5     5     5   101
    6     6     6   110
    7     7     7   111
    8     8    10  1000
    9     9    11  1001
   10     A    12  1010
   11     B    13  1011
```

Форматирование чисел:
Для вывода количества знаков после запятой можно использовать флаг f:

```pycon
>>> f"pi {22 / 7:.2f}"
"pi 3.14"
```

Форматирование строк:

```pycon
>>> name = "Name"
>>> f"{name.upper():<10}"  # выравнивается в лево на 10 символов
"NAME      "
>>> f"{name.upper():>10}"  # выравнивается в право на 10 символов
"      NAME"
>>> f"{name.upper():^10}"  # выравнивается по центру шириной 10 символов
"   NAME   "
>>> f"{22 / 7:>10.2f}"     # выравнивает в право на 10 и оставляет два знака после точки
"      3.14"
```

Форматирование строк может быть улучшено с помощью флагов:

```pycon
>>> f"{name.upper():=^10}"  # centered with 10 characters width and filled with "="
"===NAME==="
```

```python
>>> class Person:
...     def __format__(self, format_spec):
...         return "Person Object"
... 
>>> p = Person()
>>> print(f"{p}")
Person Object
```

```pycon
>>> import string
>>> class PluralFormatter(string.Formatter):
...     def format_field(self, value, format_spec):
...         if format_spec.startswith("plural,"):
...             words = format_spec.split(",")
...             if value == 1:
...                 return words[1]
...             else:
...                 return words[2]
...         else:
...             return super().format_field(value, format_spec)
...
>>> fmt = PluralFormatter()
>>> msg = "{0} {0:plural,bottle,bottles} on the wall"
>>> for bottle_count in (99, 3, 2, 1, 0):
...     print(fmt.format(msg, bottle_count))
... 
99 bottles on the wall
3 bottles on the wall
2 bottles on the wall
1 bottle on the wall
0 bottles on the wall
```

Взято из [https://digitology.tech/docs/python_3/library/string.html](https://digitology.tech/docs/python_3/library/string.html)

# % strings

|    |                                               |
|:--:|:----------------------------------------------|
| %s | Строковое представление.                      |
| %d | Целое число.                                  |
| %f | Число с плавающей точкой.                     |
| %x | Шестнадцатеричное представление целого числа. |
| %o | Восьмеричное представление целого числа.      |

""",
            "mro": """
# Method resolution order | Порядок разрешения методов

Позволяет Питону выяснить, из какого класса-предка нужно вызывать метод,
если он не обнаружен непосредственно в классе-потомке при множественном наследовании.

Решает проблему **«ромбовидной структуры»** («diamond diagram»).

```python
\U00002800 object
   /   \\
  A     B
   \\   /
     C
```

**Линеаризация класса** - это список из самого класса и всех его предков (родителей и прародителей)
в котором по порядку слева направо будет производиться поиск метода.

**Монотонность** — это свойство, которое требует соблюдения в линеаризации класса-потомка
того же порядка следования классов-прародителей, что и в линеаризации класса-родителя.

**Порядок локального старшинства** — это свойство, которое требует соблюдения в линеаризации класса-потомка
того же порядка следования классов-родителей, что и в его объявлении.

Для решения проблемы ромбовидной структуры линеаризация должна быть **монотонной**.


# Алгоритм порядка разрешения методов C3.

Для достижения указанных выше целей в Питоне используется алгоритм **C3**.

`[C1, C2, … CN]` – список из элементов `C1`, `C2`, … `CN`. Соответственно, `[С]` — список из одного элемента `C`.
`L[C]` – линеаризация класса `C`. Важно помнить, что любая линеаризация есть список по определению.
`merge(L[C1], L[C2], …, L[CN])` – объединение элементов линеаризаций `L[C1]`, `L[C2]`, …, `L[CN]` в список с помощью некоторого алгоритма.
По сути, этот алгоритм должен упорядочить все классы из `L[C1]`, `L[C2]`, …, `L[CN]` и исключить дублирование классов в итоговом списке.


Алгоритм C3 представляет из себя набор следующих правил:

- Линеаризация класса `C` есть одноэлементный список из самого класса `C` плюс объединение линеаризаций его родителей и списка всех его родителей.
  В условных обозначениях это можно записать как `L[C] = [C] + merge(L[C1], L[C2], …, L[CN], [C1, C2, …, CN])`,
  если класс `C` был объявлен как `class C(C1, C2, …, CN)`.
  Надо отметить, что каждая линеаризация `L[CX]` начинается с класса `CX`,
  который был дополнительно приписан в конец списка объединения как непосредственный родитель класса `C`.
  Зачем это сделано станет ясно далее.
- Объединение линеаризаций происходит следующим образом:
    1. Берётся нулевой элемент из первой линеаризации `L[C1][0]`.
    2. Этот элемент ищется во всех других линеаризациях (от `L[C2]` до `L[CN]`).
    3. Если этот элемент найден где-то вне начала списка
       (`L[CK][X] == L[C1][0]`, `X != 0`; по сути это значит, что `L[C1][0]` является чьйм-то предком),
       то алгоритм переходит к первому шагу, беря в качестве нулевого элемент из следующей линеаризации (`L[C2][0]`).
    4. Если элемент нигде не найден в позиции отличной от нулевой, то он добавляется в конец итогового списка линеаризации
       и удаляется из всех рассматриваемых списков (от `L[C1]` до` L[CN]`; один и тот же класс не может встречаться в итоговом списке дважды).
       Если после удаления элемента остались пустые списки — они исключаются из объединения.
       После этого алгоритм повторяется с самого начала (от нового элемента L[C1][0]), если он есть.
       Если его нет — объединение закончено.
    5. Если алгоритм дошёл до последнего элемента `L[CN]`,
       но ни один из нулевых элементов не удовлетворяет правилам, то линеаризация не возможна.

[https://habr.com/ru/articles/62203/](https://habr.com/ru/articles/62203/)
""",
        },
        "RegExp": {
            "RegExp": r"""
Регуля́рные выраже́ния — формальный язык, используемый в компьютерных программах, 
работающих с текстом, для поиска и осуществления манипуляций с подстроками в тексте, 
основанный на использовании метасимволов. 
Для поиска используется строка-образец, состоящая из символов и 
метасимволов и задающая правило поиска.


# Обозначения

|        |                                                                                   |
|--------|-----------------------------------------------------------------------------------|
| `.`    | Один любой символ, кроме новой строки `\n`.                                       |
| `\d`   | Любая цифра ≈`[0-9]`                                                               |
| `\D`   | Любой символ, кроме цифры ≈`[^0-9]`                                               |
| `\s`   | Любой пробельный символ (пробел, табуляция, конец строки и т.п.) ≈`[ \f\n\r\t\v]` |
| `\S`   | Любой не пробельный символ                                                        |
| `\w`   | Любая буква (то, что может быть частью слова), а также цифры и `_`                |
| `\W`   | Любая не-буква, не-цифра и не подчёркивание                                       |
| `[ ]`  | Один из символов в скобках, а также любой символ из диапазона `a-z` `0-9`<br>Буква `ё` не включается в общий диапазон букв!<br>Если нужен минус, его нужно указать последним или первым<br>Внутри скобок нужно экранировать только `]` и `\` |
| `[^ ]` | Любой символ, кроме перечисленных                                                |
| `^`    | Начало всего текста или начало строчки текста, если `flags=re.MULTILINE`          |
| `$`    | Конец всего текста или конец строчки текста, если `flags=re.MULTILINE`            |
| `\A`   | Строго начало всего текста                                                        |
| `\Z`   | Строго конец всего текста                                                         |
| `\b`   | Начало или конец слова (слева пусто или не-буква, справа буква и наоборот)        |
| `\B`   | Не граница слова: либо и слева, и справа буквы, либо и слева, и справа НЕ буквы   |


# Квантификаторы

Квантификатор — специальный ограничитель, который указывает количество возможных повторений символа,
группы символов или класса символов, находящихся в регулярном выражении перед ним.

|                                                  |                                            |
|--------------------------------------------------|--------------------------------------------|
| `{{n}}`                                          | Ровно `n` повторений                       |
| `{{m,n}}`                                        | От `m` до `n` повторений включительно      |
| `{{m,}}`                                         | Не менее `m` повторений                    |
| `{{,n}}`                                         | Не более `n` повторений                    |
| `?`                                              | Ноль или одно вхождение, синоним `{{0,1}}` |
| `*`                                              | Ноль или более, синоним `{{0,}}`           |
| `+`                                              | Одно или более, синоним `{{1,}}`           |
| `*?` `+?` `??`<br>`{{m,n}}?` `{{,n}}?` `{{m,}}?` | По умолчанию квантификаторы жадные — захватывают максимально возможное число символов.<br>Добавление `?` делает их ленивыми, они захватывают минимально возможное число символов. |


# Условные выражения

| Условное выражение |                                                                          | Регулярка            | Соответствие                                                                                                                                                                                                                                               |
|--------------------|--------------------------------------------------------------------------|----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `(?=.)`            | Позитивный просмотр вперёд                                               | `Людовик(?=XVI)`     | ЛюдовикXV, =={{background-color: #999999}}Людовик==XVI, =={{background-color: #999999}}Людовик==XVIII, ЛюдовикLXVII, ЛюдовикXXL                                                                |
| `(?!.)`            | Негативный просмотр вперёд                                               | `Людовик(?!XVI)`     | =={{background-color: #999999}}Людовик==XV, ЛюдовикXVI, ЛюдовикXVIII, =={{background-color: #999999}}Людовик==LXVII, =={{background-color: #999999}}Людовик==XXL |
| `(?<=.)`           | Позитивный просмотр назад<br>**Длина шаблона должна быть фиксированной** | `(?<=Сергей )Иванов` | Сергей =={{background-color: #999999}}Иванов==, Игорь Иванов                                                                                                                                                                 |
| `(?<!.)`           | Негативный просмотр назад                                                | `(?<!Сергей )Иванов` | Сергей Иванов, Игорь =={{background-color: #999999}}Иванов==                                                                                                                                                                 |

## Выполнить операции в зависимости от того, была ли захвачена определенная группа.

Формат условного выражения:

```regexp
(?(condition)true-regex|false-regex)
```

- `condition`: Условие, которое проверяется. Обычно это номер группы захвата (например, `1` для первой группы).
- `true-regex`: Регулярное выражение, которое применяется, если условие истинно.
- `false-regex`: Регулярное выражение, которое применяется, если условие ложно (опционально).

### Примеры условных выражений

#### Проверка наличия захваченной группы

```regexp
(a)?(?(1)b|c)
```

- `a` — необязательная группа.
- `b` — применяется, если `a` присутствует (т.е., если группа 1 захвачена).
- `c` — применяется, если `a` отсутствует (т.е., если группа 1 не захвачена).

Совпадение: `ab` или `c`.

#### Условные выражения с несколькими группами

```regexp
(a)(?(1)b|c)(d)?
```

- `a` — первая группа.
- Если группа 1 захвачена, проверяется `b`.
- Если группа 1 не захвачена, проверяется `c`.
- `d` — необязательная группа, которая захватывается, если предыдущий шаблон совпал.

Совпадение: `abd` или `cd` или `ab` или `c`.


# Группы захвата

| Группа захвата      | Название                                                                                | Регулярка                   | Соответствие                                                                                            |
|---------------------|-----------------------------------------------------------------------------------------|-----------------------------|---------------------------------------------------------------------------------------------------------|
| `(?:pattern)`       | Незахватывающая группа                                                                  | `(?:abc|def)`               | 123 =={{background-color: #999999}}abc== 456                              |
| `(pattern)`         | Неименованная группа захвата                                                            | `(123)`                     | 0=={{background-color: #999999}}123==4<br>{unnamed_capture_group}               |
| `\1`                | Неименованная обратная ссылка<br>Позволяет ссылаться на ранее захваченные группы<br>по номеру порядка их появления в регулярном выражении |  `(\d+)-\1`                  | 1 =={{background-color: #999999}}1-1== =={{background-color: #999999}}123-123== |
| `(?P<name>pattern)` | Именованная группа захвата                                                              | `My name is (?P<name>\w+)`  | My name is =={{background-color: #999999}}John==<br>{named_capture_group} |
| `(?P=name)`         | Именованная обратная ссылка<br>Позволяет ссылаться на ранее захваченные группы по имени | `(?P<word>\w+)\s+(?P=word)` | =={{background-color: #999999}}hello hello==                              |


# Другое

| Паттерн                                   | Название | Регулярка |   |
|-------------------------------------------|----------|-----------|---|
| `(?>pattern)`                             | Атомарная группа<br>Захватывает подстроку<br>и запрещает бэктрекинг*<br>внутри этой группы,<br>если остальная часть<br>шаблона не совпала. | `(?>\d{{3}})\d`<br>Эта конструкция сначала пытается<br>сопоставить `\d{{3}}`, а затем `\d`.<br>Если первое выражение не совпадает,<br>оно не пытается вернуться назад. | =={{background-color: #999999}}1234== |
| `(?R)` или `(?0)`                         | Рекурсивный шаблон<br>Вставляет текущее регулярное<br>выражение внутрь самого себя. | `\((?:[^()]+|(?R))*\)`<br>Это регулярное выражение<br>сопоставляет сбалансированные скобки.<br>`re.error: unknown extension ?R at position 13` | =={{background-color: #999999}}(a(b)c)== |
| `(?P<name1>pattern1|(?P<name2>pattern2))` | Условные выражения<br>с именованными группами |  | {conditional_expressions_with_named_groups} |


# Флаги

[https://docs.python.org/3/library/re.html#flags](https://docs.python.org/3/library/re.html#flags)

|                           |        |        |
|---------------------------|--------|--------|
| `re.A`<br>`re.ASCII`      | `(?a)` | По умолчанию `\w`, `\W`, `\b`, `\B`, `\d`, `\D`, `\s`, `\S` соответствуют все юникодные<br>символы с соответствующим качеством. Ускоряет работу, если все соответствия лежат внутри ASCII. |
| `re.I`<br>`re.IGNORECASE` | `(?i)` | Не различать заглавные и маленькие буквы. Работает медленнее, но иногда удобно |
| `re.M`<br>`re.MULTILINE`  | `(?m)` | Специальные символы `^` и `$` соответствуют началу и концу каждой строки |
| `re.S`<br>`re.DOTALL`     | `(?s)` | По умолчанию символ `\n` конца строки не подходит под точку. С этим флагом точка — вообще любой символ |
| `re.X`<br>`re.VERBOSE`    | `(?x)` | Пробелы внутри шаблона игнорируются, за исключением случаев,<br>когда они находятся в классе символов, или когда им предшествует неэкранированная<br>обратная косая черта, или внутри токенов,<br>таких как `*?`, `(?:` или `(?P<...>`. Например, и не допускаются.<br>{VERBOSE} |
| `re.L`<br>`re.LOCALE`     | `(?L)` | Сделать `\w`, `\W`, `\b`, \Bи соответствие без учета регистра зависимым от текущей локали.<br>Этот флаг можно использовать только с шаблонами байтов. |
| `re.U`<br>`re.UNICODE`    |        | В Python 3 символы Unicode сопоставляются по умолчанию для `str` шаблонов.<br>Поэтому этот флаг является избыточным, **не имеет никакого эффекта**<br>и сохраняется только для обратной совместимости. |
| `re.DEBUG`                |        | Отображение отладочной информации о скомпилированном выражении. |
| `re.NOFLAG`               |        | С версии 3.11. |

## Использование модификаторов

Можно объединять в одну группу: `(?i-sm)` (включает режим `i` и выключает режимы `s` и `m`)
Если требуется только в пределах группы, то шаблон после двоеточия.
Например, `(?-i)(?i:A)bc` найдёт `abc` и `Abc`, но не `ABC`.


# Команды

| Метод                                                                                                                                                                                                                                 | Описание                                                         |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------|
| re.match(    <br>&nbsp;&nbsp;&nbsp;&nbsp;pattern: str,<br>&nbsp;&nbsp;&nbsp;&nbsp;string: str,                      <br>&nbsp;&nbsp;&nbsp;&nbsp;flags: int \| RegexFlag = 0                             <br>) -> Match[str] \| None   | Ищет совпадение в начале строки.                                 |
| re.search(   <br>&nbsp;&nbsp;&nbsp;&nbsp;pattern: str,<br>&nbsp;&nbsp;&nbsp;&nbsp;string: str,                      <br>&nbsp;&nbsp;&nbsp;&nbsp;flags: int \| RegexFlag = 0                             <br>) -> Match[str] \| None   | Ищет первое совпадение в строке.                                 |
| re.findall(  <br>&nbsp;&nbsp;&nbsp;&nbsp;pattern: str,<br>&nbsp;&nbsp;&nbsp;&nbsp;string: str,                      <br>&nbsp;&nbsp;&nbsp;&nbsp;flags: int \| RegexFlag = 0                             <br>) -> list                 | Возвращает список всех непересекающихся совпадений в строке.     |
| re.finditer( <br>&nbsp;&nbsp;&nbsp;&nbsp;pattern: str,<br>&nbsp;&nbsp;&nbsp;&nbsp;string: str,                      <br>&nbsp;&nbsp;&nbsp;&nbsp;flags: int \| RegexFlag = 0                             <br>) -> Iterator[Match[str]] | Возвращает итератор по всем совпадениям в строке.                |
| re.sub(      <br>&nbsp;&nbsp;&nbsp;&nbsp;pattern: str,<br>&nbsp;&nbsp;&nbsp;&nbsp;repl: str \| (Match[str]) -> str, <br>&nbsp;&nbsp;&nbsp;&nbsp;string: str, count: int = 0, flags: int \| RegexFlag = 0<br>) -> str                  | Заменяет совпадения в строке на указанный текст.                 |
| re.subn(     <br>&nbsp;&nbsp;&nbsp;&nbsp;pattern: str,<br>&nbsp;&nbsp;&nbsp;&nbsp;repl: str \| (Match[str]) -> str, <br>&nbsp;&nbsp;&nbsp;&nbsp;string: str, count: int = 0, flags: int \| RegexFlag = 0<br>) -> tuple[str, int]      | То же, что и `re.sub()`, но также возвращает количество замен.   |
| re.split(    <br>&nbsp;&nbsp;&nbsp;&nbsp;pattern: str,<br>&nbsp;&nbsp;&nbsp;&nbsp;string: str,                      <br>&nbsp;&nbsp;&nbsp;&nbsp;maxsplit: int = 0, flags: int \| RegexFlag = 0          <br>) -> list[str]            | Разбивает строку по шаблону и возвращает список строк.           |
| re.fullmatch(<br>&nbsp;&nbsp;&nbsp;&nbsp;pattern: str,<br>&nbsp;&nbsp;&nbsp;&nbsp;string: str,                      <br>&nbsp;&nbsp;&nbsp;&nbsp;flags: int \| RegexFlag = 0                             <br>) -> Match[str] \| None   | Проверяет, полностью ли строка соответствует шаблону.            |
| re.compile(  <br>&nbsp;&nbsp;&nbsp;&nbsp;pattern: str,<br>&nbsp;&nbsp;&nbsp;&nbsp;flags: int \| RegexFlag = 0       <br>) -> Pattern[AnyStr]                                                                                          | Компилирует регулярное выражение в объект регулярного выражения. |

| Метод                                                                                                                                                                                                     | Описание                                                       |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------|
| re.compile(...).match(    <br>&nbsp;&nbsp;&nbsp;&nbsp;string: str,                      <br>&nbsp;&nbsp;&nbsp;&nbsp;flags: int \| RegexFlag = 0                             <br>) -> Match[str] \| None   | Ищет совпадение в начале строки.                               |
| re.compile(...).search(   <br>&nbsp;&nbsp;&nbsp;&nbsp;string: str,                      <br>&nbsp;&nbsp;&nbsp;&nbsp;flags: int \| RegexFlag = 0                             <br>) -> Match[str] \| None   | Ищет первое совпадение в строке.                               |
| re.compile(...).findall(  <br>&nbsp;&nbsp;&nbsp;&nbsp;string: str,                      <br>&nbsp;&nbsp;&nbsp;&nbsp;flags: int \| RegexFlag = 0                             <br>) -> list                 | Возвращает список всех непересекающихся совпадений в строке.   |
| re.compile(...).finditer( <br>&nbsp;&nbsp;&nbsp;&nbsp;string: str,                      <br>&nbsp;&nbsp;&nbsp;&nbsp;flags: int \| RegexFlag = 0                             <br>) -> Iterator[Match[str]] | Возвращает итератор по всем совпадениям в строке.              |
| re.compile(...).sub(      <br>&nbsp;&nbsp;&nbsp;&nbsp;repl: str \| (Match[str]) -> str, <br>&nbsp;&nbsp;&nbsp;&nbsp;string: str, count: int = 0, flags: int \| RegexFlag = 0<br>) -> str                  | Заменяет совпадения в строке на указанный текст.               |
| re.compile(...).subn(     <br>&nbsp;&nbsp;&nbsp;&nbsp;repl: str \| (Match[str]) -> str, <br>&nbsp;&nbsp;&nbsp;&nbsp;string: str, count: int = 0, flags: int \| RegexFlag = 0<br>) -> tuple[str, int]      | То же, что и `re.compile(...).sub()`, но также возвращает количество замен. |
| re.compile(...).split(    <br>&nbsp;&nbsp;&nbsp;&nbsp;string: str,                      <br>&nbsp;&nbsp;&nbsp;&nbsp;maxsplit: int = 0, flags: int \| RegexFlag = 0          <br>) -> list[str]            | Разбивает строку по шаблону и возвращает список строк.         |
| re.compile(...).fullmatch(<br>&nbsp;&nbsp;&nbsp;&nbsp;string: str,                      <br>&nbsp;&nbsp;&nbsp;&nbsp;flags: int \| RegexFlag = 0                             <br>) -> Match[str] \| None   | Проверяет, полностью ли строка соответствует шаблону.          |


<br>

```python
>>> import re
>>> def func(m):
...     return f"[censored({{len(m[0])}})]"
...
>>> text = "Некоторые хорошие слова подозрительны: хор, хоровод, хороводоводовед."
>>> print(re.sub(r"\b[хХxX]\w*", func, text))
Некоторые [censored(7)] слова подозрительны: [censored(3)], [censored(7)], [censored(15)].
```


# Примеры

### Номер кредитки

```regexp
[0-9]{{13,16}}
```

### ICQ

```regexp
([1-9])+(?:-?\d){{4,}}
```

### Набор из букв и цифр (латиница)

```regexp
^[a-zA-Z0-9]+$
```

### Набор из букв и цифр (латиница + кириллица)

```regexp
^[а-яА-ЯёЁa-zA-Z0-9]+$
```

### Домен (например seo-zona.ru)

```regexp
^([a-zA-Z0-9]([a-zA-Z0-9\-]{{0,61}}[a-zA-Z0-9])?\.)+[a-zA-Z]{{2,6}}$
```

### IPv4

```regexp
((25[0-5]|2[0-4]\d|[01]?\d\d?)\.){{3}}(25[0-5]|2[0-4]\d|[01]?\d\d?)
```

### IPv6

```regexp
((^|:)([0-9a-fA-F]{{0,4}})){{1,8}}$
```

### Имя пользователя (с ограничением 2-20 символов,<br>которыми могут быть буквы и цифры, первый символ обязательно буква)

```regexp
^[a-zA-Z][a-zA-Z0-9-_\.]{{1,20}}$
```

### Дата в формате YYYY-MM-DD

```regexp
[0-9]{{4}}-(0[1-9]|1[012])-(0[1-9]|1[0-9]|2[0-9]|3[01])
```

### Дата в формате `DD/MM/YYYY`

```regexp
(0[1-9]|[12][0-9]|3[01])[- /.](0[1-9]|1[012])[- /.](19|20)\d\d
```

### Целые числа и числа с плавающей точкой (разделитель точка)

```regexp
\-?\d+(\.\d{{0,}})?
```

### UUID

```regexp
^[0-9A-Fa-f]{{8}}\-[0-9A-Fa-f]{{4}}\-[0-9A-Fa-f]{{4}}\-[0-9A-Fa-f]{{4}}\-[0-9A-Fa-f]{{12}}$
```

### Широта или долгота

```regexp
-?\d{{1,3}}\.\d+
```

## Пример атомарной группы

Возьмем выражение `(?>a|ab)c` и строку `abc`:

1. Сначала регулярное выражение пытается сопоставить `a` внутри атомарной группы `(?>a|ab)`.
2. После успешного совпадения с `a`, атомарная группа блокируется, и больше не возвращается назад, даже если дальнейшие совпадения не удаются.
3. Затем выражение пытается сопоставить `c`, что не удается, потому что следующий символ `b`.
4. В обычной группе регулярное выражение вернулось бы назад, чтобы попробовать сопоставить `ab` вместо `a`.<br>Но так как группа атомарная, бэктрекинг не происходит, и регулярное выражение не находит совпадения.

### Пример кода

```pycon
>>> import re
>>> simple_group = re.compile(r"(a|ab)c")
>>> atomic_group = re.compile(r"(?>a|ab)c")
>>> print(simple_group.search("abc").group())  # Обычная группа
abc
>>> print(atomic_group.search("abc"))  # Атомарная группа
None
>>> print(atomic_group.search("ac").group())
ac
```


# Бэктрекинг

**Бэктрекинг (backtracking)** — это процесс возврата назад по строке для поиска альтернативных путей совпадения,
если текущий путь не приводит к успешному совпадению.
Регулярные выражения могут исследовать разные комбинации символов и паттернов, чтобы найти подходящее совпадение.

## Пример бэктрекинга

Рассмотрим регулярное выражение `a(b|c)*d` и строку `abbbd`:

1. Начало сопоставления с `a` — успех.
2. Далее идет `(b|c)*`, которое может захватить любое количество `b` или `c`. Сначала регулярное выражение захватывает все `b`: `abbb`.
3. Теперь шаблон пытается сопоставить `d` после `abbb`. Строка заканчивается на `d`, и совпадение успешно завершается.

Теперь возьмем строку `abbcd`:

1. Начало сопоставления с `a` — успех.
2. Далее идет `(b|c)*`, которое снова захватывает все `b`: `abb`.
3. Теперь шаблон пытается сопоставить `d` после `abb`. Это неудача, потому что следующий символ `c`.
4. Регулярное выражение возвращается (бэктрекинг) к последнему совпавшему `b`, теперь пробует совпадение с `c`: `abbc`.
5. Теперь шаблон пытается сопоставить `d` после `abbc`. Строка заканчивается на `d`, и совпадение успешно завершается.

# Особенности в разных языках

## Java

### && ^
`[\w&&[^_]]` - Любой символ, подходящий под `\w`, кроме `_`.



""".format(
                unnamed_capture_group=to_table_code_py(
                    'm = re.compile(r"0(123)4").match("01234")\n'
                    'm.group(1)  # 123\n'
                    'm[1]        # 123\n'
                    'm.group(0)  # 01234\n'
                    'm[0]        # 01234\n'
                    'm.group()   # 01234'
                ),
                named_capture_group=to_table_code_py(
                    'm = re.compile(r"My name is (?P<name>\\w+)") \\\n'
                    '.match("My name is John")\n'
                    'm.group("name")  # John\n'
                    'm["name"]        # John'
                ),
                conditional_expressions_with_named_groups=to_table_code_py(
                    """
>>> re.compile(
>>>     r"(?P<name1>pattern1\\|"
>>>     r"(?P<name2>pattern2))"
>>> ).match(
>>>     "pattern2"
>>> ).groupdict()
{
    "name1": "pattern2",
    "name2": "pattern2",
}
""".strip(),
                ),
                VERBOSE=to_table_code_py(
                    '''
a = re.compile(
   r"""
\\d +  # the integral part
\\\\.    # the decimal point
\\d *  # some fractional digits
""",
   re.X,
)
b = re.compile(r"\\d+.\\d*")

# Wrong!
c = re.compile(
   r"""(?s)
\\d +  # the integral part
\\\\.    # the decimal point
\\d *  # some fractional digits
"""
)
'''.strip(),
                ),
            ),
            "images": r"""
![regexp.png](Languages/RegExp/regexp.png)
![to template.png](Languages/RegExp/to template.png)
![lookaround.png](Languages/RegExp/lookaround.png)
""",
        },
        "Java": {
            "java": {
                "util": {
                    "Scanner": """
```java
import java.util.Scanner;
```
```java
Scanner input = new Scanner(System.in);
System.out.print(">>> ");
System.out.println(input.nextLine());  // text
```
""",
                    "Arrays": """
```java
import java.util.Arrays;
```

```java
int[] nums = { 1, 2, 3, 5 };
System.out.println(Arrays.toString(nums));
```

`Arrays.copyOf` - копирует один массив в другой.

```java
int[] arr = new int[] { 1, 2, 3, 5 };
int[] some_new = Arrays.copyOf(arr, arr.length);
```

`Arrays.sort` - сортировка массива.

```java
int[] numbers = new int[] { 1, 7, 3, 5, 2, 6, 4 };

Arrays.sort(numbers);
```
""",
                    "LinkedList": """
```java
import java.util.LinkedList;

public class LinkedListExample {
    public static void main(String[] args) {
        LinkedList<String> list = new LinkedList<>();
        list.add("Red");
        list.add("Green");
        list.add("Blue");

        for (String color : list) {
            System.out.println(color);
        }
    }
}
```
""",
                    "ArrayList": """
```java
import java.util.ArrayList;

public class ArrayListExample {
    public static void main(String[] args) {
        ArrayList<String> list = new ArrayList<>();
        list.add("Apple");
        list.add("Banana");
        list.add("Cherry");

        for (String fruit : list) {
            System.out.println(fruit);
        }
    }
}
```
""",
                    "HashSet": """
```java
import java.util.HashSet;

public class HashSetExample {
    public static void main(String[] args) {
        HashSet<String> set = new HashSet<>();
        set.add("Dog");
        set.add("Cat");
        set.add("Bird");

        for (String animal : set) {
            System.out.println(animal);
        }
    }
}
```
""",
                    "HashMap": """
```java
import java.util.HashMap;

public class HashMapExample {
    public static void main(String[] args) {
        HashMap<String, Integer> map = new HashMap<>();
        map.put("Alice", 30);
        map.put("Bob", 25);
        map.put("Charlie", 35);

        for (String name : map.keySet()) {
            System.out.println(name + ": " + map.get(name));
        }
    }
}
```
""",
                },
                "math": {
                    "BigInteger и BigDecimal": """

""",
                },
            },
            "Built-in": {
                "String": """
# Особенности
- **Неизменяемость (immutable)**: После создания строка не может быть изменена.
Все операции, которые, казалось бы, изменяют строку, возвращают новый объект `String`.
- **Пул строк**: При создании строк литералами Java сохраняет их в специальный пул строк, что помогает экономить память.

```java
String s1 = "Hello";
String s2 = new String("World");
```

# Методы

| Метод                                                    | Описание                                                                | Пример использования  |
|----------------------------------------------------------|-------------------------------------------------------------------------|-----------------------|
| `charAt(int index)`                                      | Возвращает символ по указанному индексу.                                | {charAt}              |
| `length()`                                               | Возвращает длину строки.                                                | {length}              |
| `concat(String str)`                                     | Склеивает две строки, возвращает новую строку.                          | {concat}              |
| `contains(CharSequence)`                                 | Проверяет, содержит ли строка<br>указанную последовательность символов. | {contains}            |
| `equals(Object obj)`                                     | Проверяет строки на равенство.                                          | {equals}              |
| `equalsIgnoreCase(String str)`                           | Проверяет строки на равенство, игнорируя регистр символов.              | {equalsIgnoreCase}    |
| `startsWith(String prefix)`                              | Проверяет, начинается ли строка с указанного префикса.                  | {startsWith}          |
| `endsWith(String suffix)`                                | Проверяет, заканчивается ли строка указанным суффиксом.                 | {endsWith}            |
| `indexOf(String str)`                                    | Возвращает индекс первого вхождения подстроки.                          | {indexOf}             |
| `lastIndexOf(String str)`                                | Возвращает индекс последнего вхождения подстроки.                       | {lastIndexOf}         |
| `substring`<br>(int beginIndex)                              | Возвращает подстроку, начиная с указанного индекса.                     | {substring}           |
| `substring`<br>(int beginIndex, int endIndex)                | Возвращает подстроку с указанного<br>начала до конца (не включая).      | {substring_2}         |
| `toLowerCase()`                                          | Возвращает новую строку, переведенную в нижний регистр.                 | {toLowerCase}         |
| `toUpperCase()`                                          | Возвращает новую строку, переведенную в верхний регистр.                | {toUpperCase}         |
| `trim()`                                                 | Удаляет начальные и конечные пробелы.                                   | {trim}                |
| `replace`<br>(char oldChar, char newChar)                    | Заменяет все вхождения одного символа на другой.                        | {replace}             |
| `replace`<br>(CharSequence target,<br>CharSequence replacement) | Заменяет все вхождения одной<br>последовательности символов на другую.  | {replace_2}           |
| `split(String regex)`                                    | Разделяет строку по указанному регулярному выражению.                   | {split}               |
| `matches(String regex)`                                  | Проверяет, соответствует ли строка регулярному выражению.               | {matches}             |
| `isEmpty()`                                              | Проверяет, пуста ли строка (имеет длину 0).                             | {isEmpty}             |
| `intern()`                                               | Возвращает строку из пула строк или добавляет её туда.                  | {intern}              |
| `toCharArray()`                                          | Преобразует строку в массив символов.                                   | {toCharArray}         |
| `compareTo(String anotherString)`                        | Сравнивает строки лексикографически.                                    | {compareTo}           |
| `compareToIgnoreCase(String str)`                        | Лексикографическое сравнение<br>строк без учета регистра.               | {compareToIgnoreCase} |
| `format(String format, Object... args)`                  | Возвращает отформатированную<br>строку на основе переданных аргументов. | {format}              |
| `join`<br>(CharSequence delimiter,<br>CharSequence... elements) | Объединяет элементы в строку с указанным разделителем.                  | {join}                |

# Примеры использования

1. **Склеивание строк:**
```java
String s1 = "Hello";
String s2 = "World";
String result = s1.concat(" ").concat(s2);  // "Hello World"
```

2. **Получение подстроки:**
```java
String s = "Hello World";
String sub = s.substring(6);  // "World"
```

3. **Замена символов:**
```java
String s = "apple";
String replaced = s.replace('p', 'b');  // "abble"
```

4. **Разделение строки:**
```java
String s = "a,b,c";
String[] parts = s.split(",");  // ["a", "b", "c"]
```

5. **Проверка содержания строки:**
```java
String s = "Hello";
boolean contains = s.contains("ell");  // true
```

6. **Форматирование строки:**
```java
String formatted = String.format("Name: %s, Age: %d", "Alice", 30);
System.out.println(formatted);  // "Name: Alice, Age: 30"
```

""".format(
                    charAt=to_table_code_java('char c = "Hello".charAt(1);\n// \'e\''),
                    length=to_table_code_java('int len = "Hello".length();\n// 5'),
                    concat=to_table_code_java('String s = "Hello".concat(" World");\n// "Hello World"'),
                    contains=to_table_code_java('boolean b = "Hello".contains("ll");\n// true'),
                    equals=to_table_code_java('boolean b = "Hello".equals("hello");\n// false'),
                    equalsIgnoreCase=to_table_code_java('boolean b = "Hello".equalsIgnoreCase("hello");\n// true'),
                    startsWith=to_table_code_java('boolean b = "Hello".startsWith("He");\n// true'),
                    endsWith=to_table_code_java('boolean b = "Hello".endsWith("lo");\n// true'),
                    indexOf=to_table_code_java('int idx = "Hello".indexOf("l");\n// 2'),
                    lastIndexOf=to_table_code_java('int idx = "Hello".lastIndexOf("l");\n// 3'),
                    substring=to_table_code_java('String sub = "Hello".substring(2);\n// "llo"'),
                    substring_2=to_table_code_java('String sub = "Hello".substring(1, 4);\n// "ell"'),
                    toLowerCase=to_table_code_java('String s = "HELLO".toLowerCase();\n// "hello"'),
                    toUpperCase=to_table_code_java('String s = "hello".toUpperCase();\n// "HELLO"'),
                    trim=to_table_code_java('String s = "  Hello  ".trim();\n// "Hello"'),
                    replace=to_table_code_java('String s = "Hello".replace(\'l\', \'p\');\n// "Heppo"'),
                    replace_2=to_table_code_java('String s = "Hello".replace("ll", "yy");\n// "Heyyo"'),
                    split=to_table_code_java('String[] arr = "a,b,c".split(",");\nArrays.toString("a,b,c".split(","))\n[a, b, c]'),
                    matches=to_table_code_java('boolean b = "abc".matches("[a-z]+");\n// true'),
                    isEmpty=to_table_code_java('boolean b = "".isEmpty();\n// true'),
                    intern=to_table_code_java('String s = "Hello".intern();\n// "Hello"'),
                    toCharArray=to_table_code_java('char[] arr = "Hello".toCharArray();\n// "Hello"'),
                    compareTo=to_table_code_java('int cmp = "abc".compareTo("abd");\n// -1'),
                    compareToIgnoreCase=to_table_code_java('int cmp = "abc".compareToIgnoreCase("ABC");\n// 0'),
                    format=to_table_code_java('String s = String.format("Hello %s", "World");\n// "Hello World"'),
                    join=to_table_code_java('String s = String.join(", ", "a", "b", "c");\n// "a, b, c"'),
                ),
                "Integer": """

""",
                "Character": """
```java
int x = 65535;
System.out.println(Character.charCount(x)); // 1
x = 65536;
System.out.println(Character.charCount(x)); // 2
```
""",
                "StringBuilder от StringBuffer": """

StringBuffer synchronized // заставляет ждать остальные потоки
""",
            },
            "Core": {
                "Запуск": {
                    "Запуск": """
Независимо от того, какую операционную систему вы используете, **Linux**, **Mac** или **Windows**,
если на вашем компьютере установлен **JDK** **(Java Development Kit)**,
вы можете в консоли набрать следующие команды чтобы скомпилировать и запустить программу:

`javac` или `javac.exe` компилятор
`java`  или `java.exe`  запускалка

Эти файлы лежат в папке `bin` вашего **JDK**.

Рассмотрим на примере. Cоздадим файл с названием `Main.java`.

```java
public class Main {
    public static void main(String[] args) {
        System.out.println("Hello, World!");
    }
}
```

Для того, чтобы скомпилировать его нужно набрать в консоли команду `javac`
и в качестве параметра передать имя нашего файла:

```bash
javac Main.java
```

Эта команда вызовет компилятор, который создаст файл `Main.class`,
содержащий скомпилированный код нашей `java` программы.

Чтобы запустить ее, нужно ввести команду `java` с именем класса (не файла!) в качестве параметра:

```bash
java Main // так правильно

java Main.class // так неправильно
```

# .jar

```bash
jar cf main.jar Main.class
```
""",
                    "Аргументы": """
# Аргументы

В главном классе нашей программы есть метод public static void main(...), который в качестве аргумента принимает массив String[] args.
Массив строк в качестве аргумента можно передать в программу при запуске из командной строки.
Любой массив в Java имеет переменную длину, это число элементов в этом массиве.
Добавим такой код в класс Main.java:

```java
public class Main {
    public static void main(String[] args) {
        for (int i = 0; i < args.length; i++) {
            System.out.println(args[i]);
        }
    }
}
```

И чтобы скомпилировать и запустить программу с аргументами, пишем в консоль:

```bash
javac Main.java
java Main arg0 arg1 arg2

```
""",
                },
                "Типы данных": """
|           |                          |          |                                                                    |
|-----------|--------------------------|----------|--------------------------------------------------------------------|
| `byte`    | Число                    | 1 байт   | -128<br>127<br>`2**7`                                              |
| `short`   | Число                    | 2 байта  | -32 768<br>32 767<br>`2**15`                                       |
| `int`     | Число                    | 4 байта  | -2 147 483 648<br>2 147 483 647<br>`2**31`                         |
| `long`    | Число                    | 8 байтов | –9 223 372 036 854 775 808<br>9 223 372 036 854 775 807<br>`2**63` |
| `float`   | Число с плавающей точкой | 4 байта  | -3.4\\*1038<br>3.4\\*1038                                          |
| `double`  | Число с плавающей точкой | 8 байтов | ±4.9\\*10-324<br>±1.8\\*10308                                      |
| `boolean` | `true` или `false`       | 1 байт   |                                                                    |
| `char`    | Один символ `'a'`        | 2 байта  |                                                                    |
| `String`  | Текст `"Text"`           |          |                                                                    |

String – не примитив

```java
double d = 4.5;
d = 3.0;
float f = (float) 4.5;
f = 4.5f; // (f – более короткий способ объявить float)
```

```java
char c = 'g';
String s1 = new String("Who let the dogs out?");
String s2 = "Who who who who!";
String s3 = s1 + s2;
// В Java нет перегрузки операторов!
// Оператор + определен только для строк,
// вы никогда не увидите его с другими объектами, только с примитивами.
int num = 5;
String s = "I have " + num + " cookies";
```
""",
                "Логические операторы": """
`||` **ИЛИ**
`&&` **И**
`!` **НЕ**

# ==

Сравнивает **ссылки** на объекты, если используется с объектами.
Для примитивных типов данных (`int`, `char`, `boolean`, и т. д.) сравнивает **значения**.


# equals

Определён в классе `Object`, и сравнивает **содержимое** объектов.
Стандартная реализация `equals()` в классе `Object` сравнивает **ссылки**,
но многие классы (например, `String`, `Integer`, и т. д.) переопределяют этот метод для сравнения значений.

# switch case

```java
int x = 23;
switch (x) {
    case 1:
        System.out.print ("Переменная равна 1");
        break;
    case 56:
        System.out.print ("Переменная равна 56");
        break;
    default:
        System.out.print("Что-то другое");
}
```
""",
                "Циклы": """
# for

```java
for (int i = 0; i < 3; i++) {} // Цикл будет работать 3 раза
```
1. Выполняется один раз, когда мы входим в цикл.
2. Проверяет логическое условие.
В первый раз запускается сразу после первой секции,
и выполняется каждый раз, пока условие верно, вызывая третью секцию.
3. Выполняется каждый раз при выполнении цикла.


# while
```java
while (condition) {}
```


# do while

Всегда выполнит по крайне мере одно действие

```java
do {

} while(condition);
```

# foreach

```java
int[] arr = {1, 2, 3, 4};
for (int el : arr) {
    System.out.println(el);
}
```
==
```java
int[] arr = {1, 2, 3, 4};
for (int i = 0; i < arr.length; i++) {
    int el = arr[i];
    System.out.println(el);
}
```

# break and continue

**break** останавливает цикл и переходит к оператору, следующему за ним.
**continue** остановит текущую итерацию и переместится в следующую.
""",
                "Массив (Array)": """

- **`Массив (array)`** — это структура данных фиксированного размера
- **`Список (list)`** — это интерфейс в Java, который представляет динамическую структуру данных, размер которой может изменяться.


```java
int numbers[];
numbers = new int[10];

int[] nums = new int[4];
nums[0] = 1;

int[] nums2 = new int[] { 1, 2, 3, 5 };
int[] nums3 = { 1, 2, 3, 5 };

System.out.println(Arrays.toString(nums3));
System.out.println(nums3.length);

System.out.println(Arrays.toString(new int[] { 1, 2, 3, 5 }));
System.out.println(new int[] { 1, 2, 3, 5 }.length);
```

# Вывод значений

Для вывода всех значений массива используйте метод `Arrays.toString()`, преобразующий массив в строку.

```java
import java.util.Arrays;
```
```java
System.out.println(Arrays.toString(arr));
```

Или напишите цикл, выводящий последовательно элементы массива.

```java
for(int i=0; i<arr.length; i++) {
    System.out.println(arr[i]);
}
// Или
for (int el : arr) {
    System.out.println(el);
}
```

# Многомерный массив

```java
int[][] x = { { 0, 1, 2 }, { 3, 4, 5 } };
```

# Стандартные коллекции

![collections.jpg](Languages/Java/collections.jpg)


## Основные коллекции
Помимо главного интерфейса Collection есть три других главных формата:

- `List` - коллекция для создания массивов данных, где индексами являются числа (0, 1, 2 и так далее);
- `Set` - тоже самое что `List`, вот только в `Set` нельзя установить повторяющиеся элементы;
- `Map` - коллекция для создания массивов данных, где индексами являются ключи ("one", "2", "three" и так далее).


```java
import java.util.LinkedList;
import java.util.ArrayList;


public class Main {
    public static void main(String[] args) {
        ArrayList<Float> numbers = new ArrayList<>(1);  // 1 (initialCapacity) можно не указывать
        LinkedList<String> names = new LinkedList<>();
    }
}
```

- `add()` - добавление элемента в конец массива;
- `remove()` - удаление элемента из массива по его индексу;
- `clear()` - очистка всего массива;
- `size()` - получение размера массива (количество элементов);
- `addFirst()` - добавление элемента в начало массива;
- `addLast()` - добавление элемента в конец;
- `clone()` - выполняет клонирование массива;
- `get()` - возвращает элемент по индексу;
- `getFirst()` - возвращает первый элемент в массиве;
- `getLast()` - возвращает последний элемент в массиве;
- `set(index, element)` - меняет значение элемента по индексу.


```java
List<Object> items = new ArrayList<>();
items.add("Hello");
items.add(42);
items.add(3.14);
items.add(0, 3.14);
items.add(2, 3.14);

System.out.println(items.get(0));
// System.out.println(items.get(-1)); // Index -1 out of bounds for length 5
System.out.println(items.size());
for (Object item : items) {
    System.out.println(item);
}
```
```output
5
3.14
Hello
3.14
42
3.14
```
""",
                "try, catch, finally": """
```java
public class ExceptionExample {
    public static void main(String[] args) {
        try {
            int result = 10 / 0;  // Это вызовет ArithmeticException
        } catch (ArithmeticException e) {
            System.out.println("Ошибка деления на ноль: " + e.getMessage());
        } finally {
            System.out.println("Блок finally выполняется всегда.");
        }
    }
}
```

# try-with-resources

```java
try (BufferedReader reader = new BufferedReader(new FileReader("file.txt"))) {
    String line;
    while ((line = reader.readLine()) != null) {
        System.out.println(line);
    }
} catch (IOException e) {
    e.printStackTrace();
}
```

## Без круглых скобочек

```java
BufferedReader reader = null;
try {
    reader = new BufferedReader(new FileReader("file.txt"));
    String line;
    while ((line = reader.readLine()) != null) {
        System.out.println(line);
    }
} catch (IOException e) {
    e.printStackTrace();
} finally {
    if (reader != null) {
        try {
            reader.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
```
""",
                "Исключения": """
В языке Java все исключения являются объектами и могут быть вызваны не только системой,
но и создаваться самим разработчиком.
Исключения делятся на несколько классов, которые имеют общего предка — класс `Throwable`.
Его потомками являются подклассы `Exception` и `Error`.
Исключения (**`Exceptions`**) являются результатом проблем в программе, которые в принципе решаемы и предсказуемы.
Например, произошло деление на ноль в целых числах.

Ошибки (**`Errors`**) представляют собой более серьёзные проблемы, которые, согласно спецификации `Java`,
не следует пытаться обрабатывать в собственной программе, поскольку они связаны с проблемами уровня `JVM`.
Например, исключения такого рода возникают, если закончилась память, доступная виртуальной машине.

В Java все исключения делятся на три типа: **контролируемые исключения** (**`checked`**)
и **неконтролируемые исключения** (**`unchecked`**), к которым относятся ошибки (**`Errors`**)
и исключения времени выполнения (**`RuntimeExceptions`**, потомок класса **`Exception`**).

Контролируемые исключения представляют собой ошибки, которые можно и нужно обрабатывать в программе,
к этому типу относятся все потомки класса **`Exception`** (кроме **`RuntimeException`**).

```java
// CustomException.java
public class CustomException extends Exception {
    public CustomException(String message) {
        super(message);
    }
}

// CustomExceptionExample.java
public class CustomExceptionExample {
    public static void main(String[] args) {
        try {
            throw new CustomException("Это собственное исключение!");
        } catch (CustomException e) {
            System.out.println("Поймано исключение: " + e.getMessage());
        }
    }
}
```
""",
                "Лямбда-выражения": """
```java
(parameters) -> expression
```
```java
import java.util.Arrays;
import java.util.List;

public class LambdaExample {
    public static void main(String[] args) {
        List<String> list = Arrays.asList("Apple", "Banana", "Cherry");

        // Использование лямбда-выражения для вывода элементов списка
        list.forEach(item -> System.out.println(item));
    }
}
```
```java
List<String> list = Arrays.asList("Apple", "Banana", "Cherry");
list.forEach(System.out::println);
```
""",
                "Method reference": """
# :: method reference

Указание на метод без его вызова.
""",
                "Пакеты": """
```java
package some_name;
```
```java
import java.util.Arrays;
```
```java
import java.util.*;
```
""",
                "Генерики": """
### Параметризованные типы

```java
import java.util.ArrayList;
import java.util.List;

public class GenericsExample {
    public static void main(String[] args) {
        List<String> list = new ArrayList<>();
        list.add("Hello");
        list.add("World");

        for (String item : list) {
            System.out.println(item);
        }
    }
}
```

### Ограничения генериков

```java
// Ограничение по типу
public class BoundedGenericsExample {
    public static <T extends Number> void printNumber(T number) {
        System.out.println(number);
    }

    public static void main(String[] args) {
        printNumber(10);         // Integer
        printNumber(10.5);       // Double
        // printNumber("Hello"); // Ошибка компиляции
    }
}
```

### Использование нескольких ограничений

```java
// Класс с несколькими ограничениями
public class MultipleBoundsExample {
    public static <T extends Number & Comparable<T>> void printComparable(T value) {
        System.out.println(value);
    }

    public static void main(String[] args) {
        printComparable(10);   // Integer
        printComparable(10.5); // Double
    }
}
```
""",
                "Аргументы": """
Все аргументы в отличии от [[Languages/Python/]] позиционные.

Может принимать неограниченное количество аргументов одного типа.
```java
public class Main {{
    public static void printNumbers(int... numbers) {{
        for (int number : numbers) {{
            System.out.print(number + " ");
        }}
        System.out.println();
    }}

    public static void main(String[] args) {{
        printNumbers(1, 2, 3, 4, 5);

        int[] numbersArray = {{1, 2, 3, 4, 5}};
        printNumbers(numbersArray);
    }}
}}
```

<div style="width:max-content;">{output}</div>
""".format(output=to_table_code_java("1 2 3 4 5\n1 2 3 4 5")),
            },
            "Классы": {
                "Объекты, конструкторы": """
Этот класс определяет точку с координатами `X` и `Y`.
```java
class Point {
    int x;
    int y;
}
```
```java
Point p = new Point();
```

Конструктор имеет то же самое имя, что и класс, в котором он определен, а также не имеет типа возвращаемого значения.

```java
class Point {
    int x;
    int y;

    Point(int x, int y) {
        this.x = x;
        this.y = y;
    }
}
```
```java
Point p = new Point(4, 1);
```

Мы можете определить более чем один конструктор, так что объект класса `Point` может быть создан несколькими способами.
Ключевое слово `this` мы можем использовать в качестве ссылки на текущий объект.

```java
class Point {
    int x;
    int y;

    Point() {
        this(0, 0);
    }

    Point(int x, int y) {
        this.x = x;
        this.y = y;
    }
}
```
```java
Point p = new Point();
Point p = new Point(4, 1);
```

```java
Point p = new Point();
p.x = 3;
p.y = 6;
```
""",
                "Модификатор доступа": """
|             |                                                                                          |
|-------------|------------------------------------------------------------------------------------------|
| `default`   | `public` внутри `package`                                                                |
| `public`    | Доступен из другого класса                                                               |
| `private`   | Доступен только внутри класса                                                            |
| `protected` | Доступен внутри класса и классов наследников                                             |
| `abstract`  | Запрещает создавать экземпляры класса. Несовместим с `final` и `static`.                 |
| `final`     | Запрещает изменять значение или иметь наследников для классов. Несовместим с `abstract`. |
| `static`    | Статичный метод                                                                          |
""",
                "Методы": {
                    "Методы": """
```java
public class Main {{
    public static void foo() {{
        // ...
    }}
}}
```

|        |                                                                                                                              |
|--------|------------------------------------------------------------------------------------------------------------------------------|
| static | Метод принадлежит классу, а не конкретному экземпляру класса.<br>Мы можем вызвать этот метод из другого класса так: {static} |

**void** значит, что этот метод не возвращает значение.
Методы могут возвращать значение в Java и оно должно быть определено при объявлении метода.

Пример объявления метода, возвращающего значение типа `int` – сумму двух своих параметров типа `int`:

```java
int sum(int a, int b){{
      int x;
      x = a + b;
      return x;
}}
```

При вызове метода, например, `sum(5, 3)`, параметры `5` и `3` передаются в метод, как значения соответственно `a` и `b`,
и оператор вызова метода `sum(5, 3)` – заменяется значением, возвращаемым методом (8).

В отличие от языка C, в котором тип параметра, задаваемого при вызове, приводится к типу параметра в объявлении функции,
тип задаваемого параметра в Java должен строго соответствовать типу параметра в объявлении метода,
поэтому вызов метода `sum(1.5, 8)` приведет к ошибке при компиляции программы.


```java
class Point {{
    ... // Наш код ранее
    void printPoint() {{
        System.out.println("(" + x + "," + y + ")");
    }}

    Point center(Point other) {{
        // Возвращает центр между этой и другой точками
        // Заметьте, мы используем целое число, поэтому не получим точное значение
        return new Point((x + other.x) / 2, (y + other.y) / 2);
    }}
}}
```
""".format(
                        static=to_table_code_java("Main.foo()")
                    ),
                    "Не статические методы": """
# Не статические методы

Не статические методы в Java используются чаще, чем статические методы.
Эти методы могут принадлежать любому объекту, экземпляру класса, а не всему классу.

Не статические методы могут получать доступ и изменять поля объекта.

```java
public class Student {
    private String name;
    public String getName() {
        return name;
    }
    public void setName(String name) {
        this.name = name;
    }
}
```

Вызов методов требует экземпляра класса Student.

```java
Student s = new Student();
s.setName("Danielle");
String name = s.getName();

Student.setName("Bob"); // Не будет работать!
Student.getName(); // Не будет работать!
```
""",
                    "Перегруженные методы": """
# Перегруженные методы

В языке Java в пределах одного класса можно определить два или более методов,
которые совместно используют одно и то же имя, но имеют разное количество параметров.
Когда это имеет место, методы называют перегруженными,
а о процессе говорят как о перегрузке метода **method overloading**.

Когда метод вызывается, то по количеству параметров и/или их типам среда выполнения Java определяет,
какую именно версию перегруженного метода надо вызывать
(тип возвращаемого значения во внимание не принимается, хотя, в принципе,
он тоже может отличаться у разных версий перегруженных методов).

Например метод

```java
double sum(double a, double b) {
     double x;
     x = a + b;
     return x;
}
```

вместе с объявленным ранее методом `int sum(int a, int b)`
составляют пару перегруженных методов и при вызове `sum(5, 8)` будет вызван первый метод,
а при вызове `sum(5.0, 8.0)` будет вызван второй метод.

По умолчанию метод, как и переменная, доступен только классам в том же пакете (наборе классов), что и исходный класс.
Если перед возвращаемым типом задан модификатор доступа `public`, то метод является глобальным и доступен любым объектам,
а модификатор `private` означает, что метод доступен в том классе, в котором он был объявлен,
т.е. метод инкапсулирован в данном классе.
""",
                    "Переопределение методов": """
# Переопределение методов

Кроме перегрузки существует также замещение, или переопределение методов (англ. overriding).
Замещение происходит, когда класс потомок (подкласс) определяет некоторый метод,
который уже есть в родительском классе (суперклассе), таким образом новый метод заменяет метод суперкласса.
У нового метода подкласса должны быть те же параметры или сигнатура, тип возвращаемого результата,
что и у метода родительского класса.

```java
public class Thought {
    public void message() {
        System.out.println("Я себя чувствую как стрекоза, попавшая в параллельную вселенную.");
    }
}

public class Advice extends Thought {
    @Override  // Аннотация @Override с Java 5 является необязательной, но весьма полезной
    public void message() {
        System.out.println("Внимание: Даты в календаре ближе, чем кажутся.");
    }
}
```

Класс `Thought` представляет собой суперкласс и обеспечивает вызов метода `message()`.
Подкласс, называемый `Advice`, наследует каждый метод класса `Thought`.
Однако, класс `Advice` переопределяет метод `message()`, замещая функционал, описанный в классе `Thought`.

В Java, когда подкласс содержит метод, переопределяющий метод суперкласса,
то он может помимо своего метода вызывать и метод суперкласса при помощи ключевого слова `super`.

Например, нижеследующий вариант выводит оба сообщения при вызове метода подкласса:

```java
public class Advice extends Thought {
    @Override
    public void message() {
        System.out.println("Внимание: Даты в календаре ближе, чем кажутся.");
        super.message(); // Вызов версии метода родительского класса
    }
}
```

Существуют методы, которые подкласс не может переопределять.
Например, в Java метод, объявленный с ключевым словом `final`, не может быть переопределён.
Методы, объявленные как `private` или `static` не могут быть переопределены,
поскольку это соответствует неявному использованию `final`.
""",
                    "Абстрактные методы": """
public abstract void name();
""",
                },
                "Наследование": """
Наследование в Java позволяет повторно использовать код одного класса в другом классе,
то есть вы можете унаследовать новый класс от уже существующего класса.

Главный наследуемый класс в Java называют родительским классам, или суперклассом.
Наследующий класс называют дочерним классом, или подклассом.
Подкласс наследует все поля и свойства суперкласса,
а также может иметь свои поля и свойства, отсутствующие в классе-родителе.

Пример наследования
Рассмотрим класс под названием Shape (Форма).
Shape является базовым классом, от которого наследуются другие формы, таких как прямоугольник, квадрат, круг и т.д.

```java
public class Shape {
    public double area () {
        return 0;   
    }
}
```

Поскольку это просто общая «форма», метод  вычисления площади area() будет возвращать ноль.
Чтобы узнать площадь конкретной фигуры, нужно создать подкласс, унаследованный от класса Shape, и в нем переопределить метод area().

От класса Shape  наследуется класс Circle, который тоже представляет собой форму.

```java
class Circle extends Shape { // ключевое слово "extends" означает наследование

    private static final double PI = Math.PI; // константа
    private double diameter; // любое число, представляющее диаметр этого круга

    public Circle(double diameter) { // конструктор
        this.diameter = diameter;
    }

    public double area() {
        double radius = diameter / 2.0;
        return PI * radius * radius;
    }
}
```

Метод area() базового класса наследуется классом Circle и становится доступен в нем, но нам нужно переопределить метод area()
в классе Circle, таким образом, чтобы он вычислял площадь круга.

Преимущество использования наследования в том, что вы можете написать код,
который можно применить к ряду классов, расширяющих более общий класс.

Создадим  класс Main, и в нем напишем метод, который вычисляет большую площадь двух фигур:

```java
public class Main {
    public static void main(String[] args) {
        Shape s1 = new Circle (5.0);
        Shape s2 = new Rectangle (5.0, 4.0);
        Shape larger = getLargerShape(s1,s2);

        System.out.println("The area of the larger shape is: "+larger.area());
    }

    public static Shape getLargerShape(Shape s1, Shape s2) {
        if(s1.area() > s2.area())
            return s1;
        else
            return s2;
    }
}
```

Как вы можете видеть, метод getLargerShape() не требует указания определенного типа фигуры для его двух параметров.
В качестве параметров для этого метода можно использовать экземпляр любого класса, который наследует тип Shape.
Можно использовать экземпляр класса круг, прямоугольник, треугольник, трапеция, и т.д. – до тех пор, как они наследуют класс формы.
""",
                "Анонимный класс": """
```java
Тип имя = new Тип() {
    // переписываем методы
};
```
""",
                "interface": """
```java
public interface InterfaceName {
    
}
```
```java
public interface InterfaceName extends Interface2Name, Interface3Name {
    
}
```
```java
public class ClassName implements InterfaceName, Interface2Name {
    
}
```

- Методы `public abstract`
- Поля `public final static`


### Example

```java
public interface ILights {
    boolean isOn = false;
    void setLight (boolean set);
}
```

```java
interface MyInterface {
    int MY_CONSTANT = 10;

    default void defaultMethod(String argument) {
        System.out.println("Value of argument: " + argument);
        System.out.println("Value of MY_CONSTANT: " + MY_CONSTANT);
    }
}

class MyClass implements MyInterface {}

public class Main {
    public static void main(String[] args) {
        MyClass myObject = new MyClass();
        myObject.defaultMethod("Text");
        // Value of argument: Text
        // Value of MY_CONSTANT: 10
    }
}
```
""",
                "abstract class": """
`abstract` методы не могут быть `static`

Может иметь конструктор
""",
            },
            "IO": """
## File

```java
import java.io.File;
import java.io.IOException;

public class FileExample {
    public static void main(String[] args) {
        try {
            File file = new File("example.txt");
            if (file.createNewFile()) {
                System.out.println("Файл создан: " + file.getName());
            } else {
                System.out.println("Файл уже существует.");
            }
        } catch (IOException e) {
            System.out.println("Произошла ошибка: " + e.getMessage());
        }
    }
}
```


## BufferedReader

```java
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class BufferedReaderExample {
    public static void main(String[] args) {
        try (BufferedReader br = new BufferedReader(new FileReader("example.txt"))) {
            String line;
            while ((line = br.readLine()) != null) {
                System.out.println(line);
            }
        } catch (IOException e) {
            System.out.println("Произошла ошибка: " + e.getMessage());
        }
    }
}
```


## FileWriter

```java
import java.io.FileWriter;
import java.io.IOException;

public class FileWriterExample {
    public static void main(String[] args) {
        try (FileWriter fw = new FileWriter("example.txt")) {
            fw.write("Hello, world!");
        } catch (IOException e) {
            System.out.println("Произошла ошибка: " + e.getMessage());
        }
    }
}
```
""",
            "Snippets": {
                "snippet 1": """
```java
import java.util.function.Consumer;

class Example {
    int print = 1;
    // String print = "qwe"; // Variable 'print' is already defined in the scope

    public void print(int x) {
        System.out.println(x);
    }
    public void print(String x) {
        System.out.println(x);
    }
}

public class Main {
    public static void main(String[] args) {
        Example example = new Example();
        System.out.println(example.print);
        example.print(23);
        example.print("qwerty");

        int Int = example.print;
        System.out.println(Int);

        Consumer<Integer> printInt = example::print;
        printInt.accept(23);

        Consumer<String> printString = example::print;
        printString.accept("qwerty");
    }
}
```
"""
            },
        },
        "SQL": {
            "SQLite3": {
                "Date And Time Format": """
copied from [https://www.sqlite.org/lang_datefunc.html](https://www.sqlite.org/lang_datefunc.html)

## Overview
SQLite supports seven scalar date and time functions as follows:

1. `date(time-value, modifier, modifier, ...)`  `YYYY-MM-DD`
2. `time(time-value, modifier, modifier, ...)`  `HH:MM:SS` or as `HH:MM:SS.SSS`
3. `datetime(time-value, modifier, modifier, ...)`  `YYYY-MM-DD HH:MM:SS` or as `YYYY-MM-DD HH:MM:SS.SSS`
4. `julianday(time-value, modifier, modifier, ...)`  - the fractional number of days since noon in Greenwich on November 24, 4714 B.C.
5. `unixepoch(time-value, modifier, modifier, ...)`  unix timestamp
6. `strftime(format, time-value, modifier, modifier, ...)`
7. `timediff(time-value, time-value)`

|      |                                                             |
|------|-------------------------------------------------------------|
| `%d` | day of month: `01-31`                                       |
| `%e` | day of month without leading zero: `1-31`                   |
| `%f` | fractional seconds: SS.SSS                                  |
| `%F` | ISO 8601 date: `YYYY-MM-DD`                                 |
| `%G` | ISO 8601 year corresponding to `%V`                         |
| `%g` | 2-digit ISO 8601 year corresponding to `%V`                 |
| `%H` | hour: `00-24`                                               |
| `%I` | hour for 12-hour clock: `01-12`                             |
| `%j` | day of year: `001-366`                                      |
| `%J` | Julian day number (fractional)                              |
| `%k` | hour without leading zero: `0-24`                           |
| `%l` | %I without leading zero: `1-12`                             |
| `%m` | month: `01-12`                                              |
| `%M` | minute: `00-59`                                             |
| `%p` | `AM` or `PM` depending on the hour                          |
| `%P` | `am` or `pm` depending on the hour                          |
| `%R` | ISO 8601 time: `HH:MM`                                      |
| `%s` | seconds since `1970-01-01`                                  |
| `%S` | seconds: `00-59`                                            |
| `%T` | ISO 8601 time: `HH:MM:SS`                                   |
| `%U` | week of year (`00-53`) - week 01 starts on the first Sunday |
| `%u` | day of week `1-7` with Monday==1                            |
| `%V` | ISO 8601 week of year                                       |
| `%w` | day of week `0-6` with Sunday==0                            |
| `%W` | week of year (`00-53`) - week 01 starts on the first Monday |
| `%Y` | year: `0000-9999`                                           |
| `%%` | `%`                                                         |

| Function         | Equivalent `strftime()`             |
|------------------|-------------------------------------|
| `date(...)`      | `strftime('%F', ...)`               |
| `time(...)`      | `strftime('%T', ...)`               |
| `datetime(...)`  | `strftime('%F %T', ...)`            |
| `julianday(...)` | `CAST(strftime('%J', ...) as REAL)` |
| `unixepoch(...)` | `CAST(strftime('%s', ...) as INT)`  |

```sql
SELECT timediff('2023-02-15','2023-03-15');
```

## Time Values
A time-value can be in any of the following formats shown below.
The value is usually a string, though it can be an integer or floating point number in the case of format 12.

1. `YYYY-MM-DD`
2. `YYYY-MM-DD HH:MM`
3. `YYYY-MM-DD HH:MM:SS`
4. `YYYY-MM-DD HH:MM:SS.SSS`
5. `YYYY-MM-DDTHH:MM`
6. `YYYY-MM-DDTHH:MM:SS`
7. `YYYY-MM-DDTHH:MM:SS.SSS`
8. `HH:MM`
9. `HH:MM:SS`
10. `HH:MM:SS.SSS`
11. `now`
12. `DDDDDDDDDD`


## Modifiers
For all date/time functions other than `timediff()`, the time-value argument can be followed by zero or more modifiers that alter date and/or time.
Each modifier is a transformation that is applied to the time-value to its left.
Modifiers are applied from left to right; order is important.
The available modifiers are as follows.

1. `NNN days`
2. `NNN hours`
3. `NNN minutes`
4. `NNN seconds`
5. `NNN months`
6. `NNN years`
7. `±HH:MM`
8. `±HH:MM:SS`
9. `±HH:MM:SS.SSS`
10. `±YYYY-MM-DD`
11. `±YYYY-MM-DD HH:MM`
12. `±YYYY-MM-DD HH:MM:SS`
13. `±YYYY-MM-DD HH:MM:SS.SSS`
14. `ceiling`
15. `floor`
16. `start of month`
17. `start of year`
18. `start of day`
19. `weekday N`
20. `unixepoch`
21. `julianday`
22. `auto`
23. `localtime`
24. `utc`
25. `subsec`
26. `subsecond`

""",
                "Разное": """
# Индексирование базы данных

Процесс создания специальной структуры данных, которая позволяет быстро находить нужные записи в базе данных.
Индексы могут быть созданы для отдельных полей или сочетаний полей в таблице базы данных.
Как правило, индексы упорядочивают записи в базе данных по определенному полю или полям,
что позволяет быстро находить нужные записи путем поиска в упорядоченном списке.
Индексы также могут улучшить производительность базы данных при выполнении
различных операций, таких как сортировка и группировка данных.


# AVERAGE (функция среднего)

Функция, которая вычисляет среднее значение выборки данных.
Она работает так: суммирует все значения в выборке и делит результат на количество значений.
Например, если у нас есть таблица с четырьмя строками и одним столбцом, содержащим числа `10`, `20`, `30` и `40`,
то среднее значение будет равно `25`.
Это можно посчитать, суммируя все числа `(10 + 20 + 30 + 40)`
и деля полученный результат `100` на количество чисел `4`, что даст `25`.


# Оконные функции

Функции баз данных, которые выполняют операции над наборами данных, называемыми "окнами".
Окна - это наборы строк в таблице, которые определяются каким-либо критерием
(например, временным интервалом, порядковым номером и т. д.).
Оконные функции позволяют совершать различные операции над этими наборами строк,
например, вычислять агрегатные функции (среднее, сумма, минимум и т. д.),
применять фильтры и группировки, выполнять ранжирование.
Оконные функции обычно используются с оператором `OVER`,
который определяет окно данных, над которыми будут выполняться операции.
Например, чтобы вычислить среднее значение поля `Зарплата` для каждой строки в таблице, можно использовать следующий запрос:

{okonnie_func}

В этом примере функция `AVERAGE` вычисляет среднее значение поля `Зарплата` для каждой группы строк


# PARTITION BY

Это часть оконных функций в базах данных, который используется для разбиения
набора строк на группы, называемые "партициями".Каждая партиция - это набор строк
с общими свойствами, определяемыми критерием, указанным в `PARTITION BY`
Может использоваться совместно с другими операторами,
такими как `ORDER BY` и `ROWS`/`RANGE`, чтобы определить окно данных более точно.
Например, чтобы вычислить среднее значение поля "Зарплата" для каждого отдела,
но учитывая только последние 3 месяца, можно использовать следующий запрос:
{partition_by}
В этом примере функция `AVERAGE` будет вычислять среднее значение поля `Зарплата`
для каждой партиции (то есть для каждого отдела), учитывая только строки,
упорядоченные по полю `Месяц` и относящиеся к
последним 3 месяцам (включая текущий).


# PRECEDING

Это часть оконных функций в базах данных, который используется для определения окна данных
в терминах количества строк, находящихся до текущей строки.
Например, чтобы вычислить сумму последних 3 строк в таблице, можно использовать следующий запрос:

{preceding}

В этом примере функция `SUM` будет вычислять сумму значений поля `Value` для каждой строки,
учитывая только строки, упорядоченные по полю `Id` и находящиеся до текущей строки на 2 строки (включая текущую).
Оператор `PRECEDING` может использоваться совместно с другими операторами, такими как `PARTITION BY` и `RANGE`,
чтобы определить окно данных более точно.

""".format(
                    okonnie_func=to_table_code_sql(
                        "SELECT AVERAGE(Salary)\n"
                        "  OVER (PARTITION BY Department)\n"
                        "  FROM Employees;"
                    ),
                    partition_by=to_table_code_sql(
                        "SELECT AVERAGE(Salary)\n"
                        "  OVER (\n"
                        "       PARTITION BY Department\n"
                        "       ORDER BY Month\n"
                        "       ROWS BETWEEN 2 PRECEDING AND CURRENT ROW\n"
                        "  )\n"
                        "FROM Employees;"
                    ),
                    preceding=to_table_code_sql(
                        "SELECT SUM(Value)\n"
                        "  OVER (\n"
                        "           ORDER BY Id\n"
                        "           ROWS BETWEEN 2\n"
                        "           PRECEDING AND CURRENT ROW\n"
                        "       )\n"
                        "  FROM Table;"
                    ),
                ),
                "JOIN": """
|                                                    |                                                                                                                                                                                                                                                                                                                      |
|----------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| JOIN                                               | Используется для соединения двух таблиц в одну.<br>Существует ряд различных видов JOIN, каждый из которых имеет свои особенности<br>и применяется в зависимости от ситуации.<br>INNER JOIN, LEFT JOIN, RIGHT JOIN, FULL OUTER JOIN,<br>CROSS JOIN, NATURAL JOIN, UNION JOIN, STRAIGHT_JOIN, OUTER APPLY, CROSS APPLY |
| INNER JOIN - это самый распространенный вид JOIN   | Соединяет две таблицы по совпадающим значениям определенных полей.<br>Результатом является таблица, содержащая только те строки,<br>которые совпадают по заданным полям.                                                                                                                                             |
| LEFT JOIN аналогичен INNER JOIN                    | Результирующая таблица содержит все строки из левой (первой) таблицы,<br>даже если они не совпадают по заданным полям со второй таблицей.<br>Несовпадающие строки заполняются нулевыми значениями                                                                                                                    |
| RIGHT JOIN аналог LEFT JOIN                        | Результирующая таблица содержит все строки из правой (второй) таблицы,<br>даже если они не совпадают по заданным полям с первой таблицей.<br>Несовпадающие строки заполняются нулевыми значениями.                                                                                                                   |
| FULL OUTER JOIN комбинация LEFT JOIN и RIGHT JOIN. | Результирующая таблица содержит все строки из обоих таблиц,<br>даже если они не совпадают по заданным полям.<br>Несовпадающие строки заполняются нулевыми значениями.                                                                                                                                                |
| CROSS JOIN                                         | Cоединяет все строки из первой таблицы со всеми строками из второй таблицы,<br>создавая картежи, удовлетворяющие условию соединения.<br>Таким образом, CROSS JOIN не учитывает совпадающие<br>значения в таблицах и создает все возможные картежи.                                                                   |

```sql
SELECT * FROM Table1
FULL OUTER JOIN Table2
ON Table1.Field1 = Table2.Field1;
```

```sql
SELECT * FROM Table1
CROSS JOIN Table2;
```
""",
                "Операторы": """Операторы:
SELECT - используется для извлечения данных из базы данных. 
         Он может быть использован с другими операторами, такими как FROM, WHERE и GROUP BY, 
         чтобы определить, какие данные должны быть извлечены, из каких таблиц и с какими условиями.
         - SELECT - какие колонки данных вы хотите извлечь.
         - FROM - из какой таблицы нужно извлечь данные.
         - WHERE - условие, которое должны соответствовать строки, чтобы быть включенными в результат.
         - GROUP BY - какие колонки нужно использовать для группировки результата.
         - HAVING - для фильтрации групп результата запроса. Он похож на оператор WHERE, 
                    но он используется с оператором GROUP BY и применяется только к группам, а не к отдельным строкам.
         - ORDER BY - какие колонки нужно использовать для сортировки результата, 
                      а также порядок сортировки (по возрастанию или убыванию (ASC|DESC))
         - JOIN - используется для соединения двух таблиц в базе данных. 
                  Он может быть использован с различными типами JOIN, такими как INNER JOIN, LEFT JOIN и RIGHT JOIN, 
                  чтобы определить, какие строки из обеих таблиц должны быть соединены.
         SELECT column1, column2, ...
         FROM     __table_name
         WHERE    __condition
         GROUP BY __column
         HAVING   __condition
         ORDER BY __column ASC|DESC;

JOIN - это оператор SQL, который используется для соединения двух или более таблиц в базе данных. 
       Он позволяет вам извлекать данные из разных таблиц и объединять их в одном результате.
       Существует разные типы JOIN, которые используются в зависимости от требуемого результата. Основные типы JOIN это:
       INNER JOIN - этот тип JOIN возвращает строки, которые содержатся в обоих таблицах.
       OUTER JOIN - этот тип JOIN возвращает все строки из обоих таблиц, даже если они не совпадают. 
                    Существует два вида внешних JOIN: LEFT JOIN и RIGHT JOIN.
       CROSS JOIN - этот тип JOIN используется для создания картежного произведения двух таблиц. 
                    Он возвращает все возможные комбинации строк из двух таблиц, даже если у них нет совпадений.
       SELECT column1, column2, ... FROM table1 CROSS JOIN table2;

FULL OUTER JOIN - используется для соединения двух таблиц. 
                  Он возвращает все строки из обеих таблиц, даже если у них нет совпадений. 
                  Если соответствующих строк нет в одной из таблиц, то в качестве значений используются NULL.
                  SELECT column1, column2, ... FROM table1 FULL OUTER JOIN table2 ON table1.column = table2.column;

INSERT - используется для вставки новых строк в таблицу базы данных. 
         Он может быть использован с VALUES и SELECT, DEFAULT VALUES и SET, 
         чтобы определить, какие данные нужно вставить и откуда их взять.

UPDATE - используется для обновления существующих строк в таблице базы данных. 
         Он может быть использован с оператором SET, чтобы указать, какие значения должны быть обновлены, 
         и с оператором WHERE, чтобы указать, какие строки должны быть обновлены.
         UPDATE table_name SET column1 = value1, column2 = value2, ... WHERE condition;

DELETE - используется для удаления строк из таблицы базы данных. 
         Он может быть использован с оператором WHERE, чтобы указать, какие строки должны быть удалены. 
         Если оператор WHERE не указан, то будут удалены все строки из таблицы. 
         DELETE FROM table_name WHERE condition;

CREATE - используется для создания объектов в базе данных, таких как таблицы, индексы, представления, триггеры и т. д. 
         Он может быть использован с TABLE, INDEX, VIEW, TRIGGER, чтобы указать, какой тип объекта нужно создать.
         CREATE object_type object_name (column1 datatype, column2 datatype, ...);

DROP - используется для удаления объектов из базы данных, таких как таблицы, индексы, представления, триггеры и т. д. 
       Он может быть использован c TABLE, INDEX, VIEW, TRIGGER, чтобы указать, какой тип объекта нужно удалить. 
       DROP object_type object_name;

ALTER - используется для изменения структуры существующих объектов в базе данных, 
        таких как таблицы, индексы, представления, триггеры и т. д. 
        Он может быть использован с ADD, DROP, MODIFY, ALTER, чтобы указать, какое изменение нужно внести.
        ALTER object_type object_name action;
        Например, чтобы добавить столбец email к таблице customers, вы можете использовать следующий запрос:
        ALTER TABLE customers ADD email VARCHAR(255);
        Или, чтобы удалить столбец age из таблицы customers, вы можете использовать следующий запрос:
        ALTER TABLE customers DROP age;

TRUNCATE - используется для удаления всех строк из таблицы базы данных. 
           Он отличается от оператора DELETE, тем что он удаляет все строки из таблицы без проверки условий, 
           а также очищает данные страниц таблицы, что позволяет сократить время выполнения и уменьшить размер таблицы.  
           TRUNCATE TABLE table_name;
           (Обратите внимание, что оператор TRUNCATE не может быть отменен, поэтому используйте его с осторожностью.)

WHERE - это оператор SQL, который используется для фильтрации строк в результате запроса. 
        Он может быть использован с операторами SELECT, UPDATE, DELETE и другими, 
        чтобы указать, какие строки должны быть включены в результат или изменены.
        SELECT column1, column2, ...
        FROM table_name
        WHERE condition;

AND - это логическое условие, используется в операторе WHERE в SQL для соединения нескольких условий. 
      Оно возвращает TRUE только в том случае, если все условия равны TRUE.
      SELECT column1, column2, ... FROM table_name WHERE condition1 AND condition2 AND ...;

OR - это логическое условие, используется в операторе WHERE в SQL для соединения нескольких условий. 
     Оно возвращает TRUE, если хотя бы одно из условий равно TRUE. 
     SELECT column1, column2, ... FROM table_name WHERE condition1 OR condition2 OR ...;

NOT - это логическое условие, используется в операторе WHERE в SQL для инвертирования условия. 
      Оно возвращает TRUE, если условие равно FALSE, и наоборот. SELECT column1, column2, ... 
      FROM table_name WHERE NOT condition;
      Обратите внимание, что условие NOT может быть использовано совместно с другими логическими условиями, 
      такими как AND и OR. Например: 
      SELECT * FROM customers WHERE NOT (name = 'John' OR age > 30);

BETWEEN - используется в операторе WHERE для указания диапазона значений. 
          Он возвращает TRUE, если значение равно либо больше начального значения, но меньше конечного значения. 
          SELECT column1, column2, ... FROM table_name WHERE column BETWEEN value1 AND value2;

IN - это оператор SQL, который используется в операторе WHERE для указания набора значений. 
     Он возвращает TRUE, если значение равно любому из указанных значений.
        SELECT column1, column2, ... FROM table_name WHERE column IN (value1, value2, ...);
        Обратите внимание, что условие IN может быть использовано совместно с другими логическими условиями, такими как AND и OR. Например:
        SELECT * FROM customers WHERE (name IN ('John', 'Alice') AND age > 30) OR city = 'New York';

BETWEEN - используется для указания диапазона значений, которые должны соответствовать условию в запросе SQL. 
          эквивалентен использованию оператора ">=" и "<=".
          SELECT * FROM products WHERE price BETWEEN 10 AND 20;

IN - используется для указания списка значений, которые должны соответствовать условию в запросе SQL. 
     используется в качестве альтернативы оператору BETWEEN.
     SELECT * FROM employees WHERE salary IN (40000, 41000, 42000, 43000, 44000, 45000);

LIKE - используется для указания условия совпадения данных с определенным шаблоном. 
       принимает в качестве аргумента строку с специальными символами, которые обозначают любые символы или любое количество символов.
       SELECT * FROM customers WHERE email LIKE 'm%';
       % - соответствует любому количеству символов
       _ - соответствует любому одному символу
       [] - указывает диапазон символов, которые могут совпасть с шаблоном. Например, [a-z] соответствует любому одному символу от a до z.
       [^] - указывает диапазон символов, которые не могут совпасть с шаблоном. Например, [^a-z] соответствует любому символу, кроме a-z.

REGEXP - используется для указания условия совпадения данных с определенным регулярным выражением. 
         Регулярные выражения - это специальный язык, который используется для описания шаблона строки. 
         Они позволяют создавать более сложные условия совпадения, чем может позволить LIKE.
         SELECT * FROM customers WHERE email REGEXP 'gmail';

LIMIT - это оператор SQL, который используется для ограничения количества строк, возвращаемых запросом. 
        Он может быть использован с операторами SELECT, UPDATE и DELETE.
           SELECT column1, column2, ... FROM table_name LIMIT number;
           Например, чтобы выбрать только первые 10 клиентов, вы можете использовать следующий запрос:
           SELECT * FROM customers LIMIT 10;
           Вы также можете указать начальное положение и количество строк, которые должны быть возвращены, указав эти значения в операторе LIMIT. Например:
           SELECT * FROM customers LIMIT 5, 10;

ORDER BY - это оператор SQL, который используется для сортировки результатов запроса. 
           Он может быть использован с операторами SELECT, UPDATE и DELETE.
              SELECT column1, column2, ... FROM table_name ORDER BY column1, column2, ... ASC|DESC;
              Например, чтобы отсортировать всех клиентов по имени в алфавитном порядке, вы можете использовать следующий запрос:
              SELECT * FROM customers ORDER BY name;

GROUP BY - это оператор SQL, который используется для группировки результатов запроса по указанному столбцу. 
           Он обычно используется совместно с функциями агрегации, такими как SUM, AVG, COUNT, MAX и MIN.
           SELECT column1, column2, ... FROM table_name GROUP BY column1, column2, ...;

HAVING - это оператор SQL, который используется для фильтрации групп результатов запроса. 
         Он аналогичен оператору WHERE, но указывается после GROUP BY и применяется только к группам, а не к отдельным строкам.
         SELECT column1, column2, ... FROM table_name GROUP BY column1, column2, ... HAVING condition;

UNION - это оператор SQL, который используется для объединения результатов двух или более запросов. 
        Он возвращает уникальные строки из всех запросов.
        SELECT column1, column2, ... FROM table1 UNION SELECT column1, column2, ... FROM table2;
        Например, чтобы объединить результаты двух запросов и вернуть уникальные имена клиентов, вы можете использовать следующий запрос:
        SELECT name FROM customers1 UNION SELECT name FROM customers2;
        Вы также можете использовать оператор UNION ALL, чтобы вернуть все строки,

DISTINCT - убирает дубликаты из результата выборки. (Возвращает уникальные значения)
           может использоваться с различными типами данных.
           SELECT DISTINCT customer FROM sales;

INTERSECT - это оператор SQL, который используется для выбора строк, которые содержатся в обоих результатах двух 
            или более запросов. Он возвращает только уникальные строки, которые присутствуют во всех запросах.
            SELECT column1, column2, ... FROM table1 INTERSECT SELECT column1, column2, ... FROM table2;
            Например, чтобы выбрать те имена клиентов, которые содержатся в обоих таблицах, вы можете использовать следующий запрос:
            SELECT name FROM customers1 INTERSECT SELECT name FROM customers2;
            Обратите внимание, что оператор INTERSECT не поддерживается во всех СУБД. 
            Вместо этого вы можете использовать вложенный запрос с IN или EXISTS.

EXCEPT - это оператор SQL, который используется для выбора строк, которые содержатся в первом запросе, 
         но не содержатся во втором. Он возвращает только уникальные строки, которые присутствуют в первом запросе, но отсутствуют во втором.
         SELECT column1, column2, ... FROM table1 EXCEPT SELECT column1, column2, ... FROM table2;
         Например, чтобы выбрать те имена клиентов, которые содержатся в первой таблице, но не содержатся во второй, вы можете использовать следующий запрос:
         SELECT name FROM customers1 EXCEPT SELECT name FROM customers2;
         Обратите внимание, что оператор EXCEPT не поддерживается во всех СУБД. Вместо этого вы можете использовать вложенный запрос с NOT IN или NOT EXISTS.

MATCH - используется для указания условия совпадения данных с определенным столбцом или набором столбцов в таблице. 
        используется совместно с оператором AGAINST, который указывает, что ищется.
        SELECT * FROM articles WHERE MATCH(tags) AGAINST('SQL');

USING - это оператор SQL, который используется в соединениях JOIN для указания столбца, который используется для соединения таблиц. 
        Он позволяет вам определить условие соединения с помощью одного столбца, который имеется в обеих таблицах.
        SELECT column1, column2, ... FROM table1 JOIN table2 USING (column);
        Например, чтобы соединить таблицы customers и orders по столбцу customer_id, вы можете использовать следующий запрос:
        SELECT customers.name, orders.order_id FROM customers JOIN orders USING (customer_id);
        Обратите внимание, что оператор USING не поддерживается во всех СУБД.
        Вместо этого вы можете использовать ON с условием table1.column = table2.column для соединения таблиц.

FOR - это оператор SQL, который используется для задания условий в выражении SELECT. 
      Он позволяет вам задать условие, которое должно быть выполнено для каждой строки результата запроса. 
      Оператор FOR может использоваться только с оператором SELECT и только в конце запроса. 
      Он может использоваться для указания типа блокировки, которую нужно установить на строки, выбранные в результате запроса. 
      Существует два основных типа блокировок, которые можно установить с помощью оператора FOR: 
      FOR UPDATE и FOR SHARE. 
      Оператор FOR UPDATE устанавливает блокировку на строку, которая не может быть изменена или удалена другими транзакциями, 
      пока текущая транзакция не будет завершена.""",
                "Функции": """
Функции:

|           |                                                                                                                                                                                                                                                                                                                                                |
|-----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| MAX       | Возвращает максимальное значение из списка аргументов.<br>может использоваться с числовыми и дата/время типами данных.<br>`SELECT MAX(amount) FROM sales;`                                                                                                                                                                                     |
| MIN       | Возвращает минимальное значение из списка аргументов.<br>может использоваться с числовыми и дата/время типами данных.<br>`SELECT MIN(amount) FROM sales;`                                                                                                                                                                                      |
| SUM       | Возвращает сумму аргументов.<br>может использоваться только с числовыми типами данных.<br>`SELECT SUM(amount) FROM sales;`                                                                                                                                                                                                                     |
| AVG       | Возвращает среднее арифметическое аргументов.<br>может использоваться только с числовыми типами данных.<br>`SELECT AVG(amount) FROM sales;`                                                                                                                                                                                                    |
| COUNT     | Возвращает количество аргументов.<br>может использоваться с различными типами данных.<br>`SELECT COUNT(amount) FROM sales;`                                                                                                                                                                                                                    |
| CONCAT    | Соединяет строки.<br>может использоваться с типом данных строка.<br>`SELECT CONCAT(first_name, ' ', last_name) as full_name FROM customers;`                                                                                                                                                                                                   |
| UPPER     | Преобразует строку в верхний регистр.<br>может использоваться с типом данных строка.<br>`SELECT UPPER(first_name) as first_name, UPPER(last_name) as last_name FROM customers;`                                                                                                                                                                |
| LOWER     | Преобразует строку в нижний регистр.<br>может использоваться с типом данных строка.<br>`SELECT LOWER(first_name) as first_name, LOWER(last_name) as last_name FROM customers;`                                                                                                                                                                 |
| SUBSTR    | Извлекает подстроку из строки. (столбец, первый символ, количество символов)<br>может использоваться с типом данных строка.<br>`SELECT SUBSTR(phone, 1, 3) as area_code FROM customers;`                                                                                                                                                       |
| TRIM      | Удаляет пробелы из начала и конца строки.<br>может использоваться с типом данных строка.<br>`SELECT TRIM(first_name) as first_name, last_name FROM customers;`                                                                                                                                                                                 |
| LENGTH    | Возвращает количество символов в строке.<br>может использоваться с типом данных строка.<br>`SELECT first_name, LENGTH(first_name) as name_length FROM customers;`                                                                                                                                                                              |
| ROUND     | Округляет число до указанной точности. (столбец, кол-во знаков после запятой)<br>может использоваться с типом данных число.<br>`SELECT product, ROUND(price, 2) as price FROM sales;`                                                                                                                                                          |
| DATE      | Преобразует строку в формат даты. (хз проверить на питоне надо)<br>может использоваться с типом данных строка и возвращает тип данных дата.<br>`SELECT DATE(order_date) as order_date, product, price FROM orders;`                                                                                                                            |
| TIME      | Преобразует строку в формат времени. (хз проверить на питоне надо)<br>может использоваться с типом данных строка и возвращает тип данных время.<br>`SELECT TIME(meeting_time) as meeting_time, topic FROM meetings;`                                                                                                                           |
| DATETIME  | Преобразует строку в формат даты и времени.<br>может использоваться с типом данных строка и возвращает тип данных дата/время.<br>`SELECT DATETIME(event_date_time) as event_date_time, event_name FROM events;`                                                                                                                                |
| TIMESTAMP | Преобразует строку в формат времени с меткой времени (timestamp). <br>может использоваться с типом данных строка и возвращает тип данных timestamp.<br>`SELECT TIMESTAMP(log_timestamp) as log_timestamp, log_message FROM logs;`                                                                                                              |
| NOW       | Возвращает текущую дату и время.<br>не требует аргументов и возвращает тип данных timestamp.<br>`INSERT INTO orders (order_date, product, price) VALUES (NOW(), 'Shoes', 59.99);`                                                                                                                                                              |
| COALESCE  | Принимает неограниченное количество аргументов и возвращает первый ненулевой аргумент (???)<br>может использоваться с типами данных число, строка, дата/время и возвращает тип данных, соответствующий первому ненулевому аргументу.<br>`SELECT first_name, last_name, COALESCE(email, '') as email, COALESCE(phone, '') as phone FROM users;` |
| ISNULL    | Проверяет, является ли значение нулевым (NULL).<br>принимает один аргумент и возвращает логическое значение true, если аргумент равен NULL, и false, если аргумент не равен NULL.<br>`SELECT first_name, last_name, position FROM employees WHERE ISNULL(bonus);`                                                                              |
| IFNULL    | Проверяет, является ли значение нулевым (NULL).<br>принимает два аргумента и возвращает первый аргумент, если он не равен NULL, и второй аргумент, если первый равен NULL.<br>`SELECT name, price, IFNULL(description, 'No description') as description FROM products;`                                                                        |

CASE - позволяет условно выполнять различные действия в запросе SQL. 
       состоит из секций WHEN, THEN и ELSE, где WHEN указывает условие, 
       THEN - действие, которое нужно выполнить при выполнении условия, 
       а ELSE - действие, которое нужно выполнить, если условие не выполнено.
       SELECT position, salary,
       CASE
       WHEN salary > 40000 THEN 'High salary'
       WHEN salary BETWEEN 30000 AND 40000 THEN 'Average salary'
       ELSE 'Low salary'
       END as salary_level
       FROM employees;

IIF (IF ELSE) - позволяет условно выполнять различные действия в запросе SQL. 
                принимает три аргумента: логическое выражение, возвращаемое значение при истинном условии и возвращаемое значение при ложном условии.
```sql
SELECT name, price, IIF(quantity > 0, 'In stock', 'Out of stock') as stock_status FROM products;
```

ROW_NUMBER - используется для нумерации строк в результирующем наборе данных. 
             используется совместно с оператором ORDER BY для сортировки строк по определенному критерию.
```sql
SELECT ROW_NUMBER() OVER (ORDER BY quantity) as row_num, product_name, quantity, price FROM sales;
```

RANK - используется для нумерации строк в результирующем наборе данных. 
       используется совместно с оператором ORDER BY для сортировки строк по определенному критерию.
       (Отличие RANK от ROW_NUMBER заключается в том, что RANK нумерует строки с учетом их значений. 
        Например, если у нас есть несколько строк с одинаковым значением, то RANK будет устанавливать им ранг 
        с учетом этого одинакового значения, а не просто нумеровать их в порядке возрастания.)
       (Обратите внимание, что если бы у нас были строки с одинаковым значением количества, то они бы получили одинаковый ранг.)
```sql
SELECT RANK() OVER (ORDER BY quantity) as row_num, product_name, quantity, price FROM sales;
```

DENSE_RANK - используется для нумерации строк в результирующем наборе данных. 
             используется совместно с оператором ORDER BY для сортировки строк по определенному критерию.
             (Отличие DENSE_RANK от RANK заключается в том, что DENSE_RANK нумерует строки с учетом их значений, 
              но не оставляет промежутки между рангами. Таким образом, если у нас есть несколько строк с одинаковым значением, 
              то DENSE_RANK будет устанавливать им ранг с учетом этого одинакового значения, но не оставляет промежутки между рангами.)
             (Обратите внимание, что если бы у нас были строки с одинаковым значением количества, то они бы получили одинаковый ранг.
              Отличие от RANK заключается в том, что DENSE_RANK не оставляет промежутки между рангами.)
```sql
SELECT DENSE_RANK() OVER (ORDER BY quantity) as row_num, product_name, quantity, price FROM sales;
```

NTILE - используется для разбиения результирующего набора данных на равные части. 
        используется совместно с оператором ORDER BY для сортировки строк по определенному критерию.
        (разбить эту таблицу на 3 равные части и пронумеровать каждую строку с учетом ее нахождения в этой части)
```sql
SELECT NTILE(3) OVER (ORDER BY quantity) as group_num, product_name, quantity, price FROM sales;
```

LAG - используется для получения значения из предыдущей строки результирующего набора данных. 
      используется для сравнения значений в разных строках или для вычисления разницы между значениями.
      (получить таблицу с колонкой, содержащей разницу между ценой текущей строки и ценой предыдущей строки.)
```sql
SELECT product_name, price, LAG(price, 1) OVER (ORDER BY date) as prev_price, price - LAG(price, 1) OVER (ORDER BY date) as price_diff FROM sales;
```

LEAD - используется для получения значения из следующей строки результирующего набора данных. 
       используется для сравнения значений в разных строках или для вычисления разницы между значениями.
       SELECT product_name, price, LEAD(price, 1) OVER (ORDER BY date) as next_price, price - LEAD(price, 1) OVER (ORDER BY date) as price_diff FROM sales;
       (получить таблицу с колонкой, содержащей разницу между ценой текущей строки и ценой следующей строки.)

EXPLAIN - используется для анализа плана выполнения запроса. 
          возвращает таблицу с информацией о том, как база данных планирует выполнить запрос, включая информацию о том, 
          какие таблицы и столбцы будут использоваться, какие индексы будут использоваться, и как будут объединяться таблицы.
          EXPLAIN SELECT * FROM sales WHERE price > 200;
          (Мы хотим анализировать план выполнения запроса на выборку всех строк таблицы "sales" с ценой больше 200.)


EXPLAIN ANALYZE - расширение функции EXPLAIN, включает в себя дополнительную информацию о времени выполнения каждого этапа плана выполнения запроса. 
                  Эта информация может быть полезна при оптимизации запросов и изучении причин медленного выполнения.
                  EXPLAIN ANALYZE SELECT * FROM sales WHERE price > 200;
                  (Каждая строка таблицы описывает один этап плана и содержит следующие столбцы:
                   Номер этапа
                   Тип этапа (поиск, сортировка, табулирование и т.п.)
                   Таблицы, на которые распространяется действие этапа
                   Количество строк, которое будет обработано на этом этапе
                   Время выполнения этапа)
                  (Например, таблица может выглядеть следующим образом:
                   Seq.    Type    Table    Rows    Time
                   1    scan    sales    3        0.001
                   2    sort            3        0.002
                   3    limit            3        0.002)
                  (Основное отличие между EXPLAIN и EXPLAIN ANALYZE заключается в том, что EXPLAIN ANALYZE не только выводит информацию о плане выполнения запроса, 
                   но и РЕАЛЬНО выполняет запрос и возвращает результат. Это позволяет получить более точную информацию о времени выполнения каждого этапа, 
                   так как используется реальное время выполнения, а не оценочные данные, которые могут быть предоставлены функцией EXPLAIN. 
                   Также EXPLAIN ANALYZE может показать дополнительную информацию, такую как количество сканированных строк, общее время выполнения запроса и т.п.)

ABS (абсолютное значение) - возвращает абсолютное значение указанного числа. ABS(-5) = 5, ABS(3) = 3

ACOS (арккосинус) - возвращает арккосинус указанного числа. Арккосинус - это угол, косинус которого равен указанному числу. 
                    Функция ACOS может принимать любое число в диапазоне от -1 до 1, включительно, и возвращает угол в радианах.
                    ACOS(0.5) = 1.0471975511966, ACOS(-1) = 3.14159265358979

ASIN (арксинус) - возвращает арксинус указанного числа. 
                  Арксинус - это угол, синус которого равен указанному числу. 
                  Функция ASIN может принимать любое число в диапазоне от -1 до 1, включительно, и возвращает угол в радианах.
                  ASIN(0.5) = 0.52359877559829
                  ASIN(-1) = -1.5707963267949
                  Функция ASIN может быть использована для вычисления угла в треугольнике, если известны два катета и гипотенуза. Для этого нужно воспользоваться теоремой синусов.

ATAN (арктангенс) - возвращает арктангенс указанного числа. 
                    Арктангенс - это угол, тангенс которого равен указанному числу. 
                    Функция ATAN может принимать любое число и возвращает угол в радианах.
                    ATAN(1) = 0.78539816339745
                    ATAN(-2) = -1.10714871779409
                    Функция ATAN может быть использована для вычисления угла в треугольнике, если известны два катета и гипотенуза. Для этого нужно воспользоваться теоремой тангенсов.
                    (Пример использования функции ATAN в SQL запросе:
                     SELECT ATAN(2) as atan FROM DUAL;
                     Этот запрос выполнится и вернет арктангенс числа 2, то есть 1.10714871779409.
                     Также функция ATAN может быть использована в качестве условия в WHERE клаузе, например:
                     SELECT * FROM points WHERE ATAN(y/x) > 0.5;
                     В этом запросе будут выбраны точки, у которых угол между осью X и вектором из начала координат до точки больше 0.5 радиан.)

ATAN2 (арктангенс 2) - возвращает арктангенс указанной точки (y, x). 
                       Арктангенс - это угол, тангенс которого равен указанной точке. 
                       Функция ATAN2 принимает два аргумента - y и x, и возвращает угол в радианах.
                       ATAN2(1, 1) = 0.78539816339745
                       ATAN2(-2, 2) = -0.78539816339745
                       Функция ATAN2 может быть использована для вычисления угла в треугольнике, если известны два катета и гипотенуза. 
                       Для этого нужно воспользоваться теоремой тангенсов.
                       (Отличие между функциями ATAN и ATAN2 в том, что ATAN принимает только один аргумент - тангенс угла, 
                        в то время как ATAN2 принимает два аргумента - координаты точки в декартовой системе координат. 
                        Это позволяет ATAN2 вычислять угол даже если одна из координат равна нулю, чего не может сделать функция ATAN.)

CEIL (от ceiling)   возвращает наименьшее целое число, которое больше или равно переданному значению. CEIL(3.14) вернет 4, а CEIL(-3.14) вернет -3.
COS                 возвращает косинус угла в градусах. COS(угол в градусах) COS(45) result 0.7071067811865475
COT                 возвращает котангенс угла в радианах. Котангенс угла равен обратному тангенсу угла. COT(угол в радианах) COT(PI() / 4) result 1
                    функция COT работает так же, как и функция SIN и TAN, но ожидает угол в радианах.

DEGREES             преобразует радианы в градусы. DEGREES(выражение_вычисляется_как_радианы) DEGREES(PI()) result 180
EXP                 возвращает экспоненту (е в степени) заданного числа. EXP(выражение_вычисляется_как_число) EXP(2) result 7.38905609893065
                    число e (естественный логарифм) равно 2.718281828459045. EXP(2) эквивалентно e^2 = 7.38905609893065.
FLOOR               возвращает наибольшее целое число, которое меньше или равно переданному значению. FLOOR(выражение_вычисляется_как_число) FLOOR(3.14) result 3
                    FLOOR отличается от CEIL тем, что возвращает наибольшее целое число, которое меньше или равно переданному значению, 
                    в то время как CEIL возвращает наименьшее целое число, которое больше или равно переданному значению.

LN                  возвращает натуральный логарифм (по основанию e) заданного числа. LN(выражение_вычисляется_как_число) LN(2)сresult 0.693147180559945
                    число e (естественный логарифм) равно 2.718281828459045. LN(2) эквивалентно ln(2) = 0.693147180559945.

LOG                 возвращает логарифм заданного числа по заданному основанию. LOG(выражение_вычисляется_как_число, основание_логарифма) LOG(100, 10) result 2
                    работает так же, как и функция LN, но позволяет задавать основание логарифма. LOG(100, 10) эквивалентно log10(100) = 2.

LOG10               возвращает десятичный логарифм числа. LOG10(выражение, которое вычисляется как число) LOG10(100) result 2
                    всегда возвращает положительное число. Если входное число 0 или отрицательно, то результатом будет NULL.

MOD                 возвращает остаток от деления одного числа на другое. MOD(10, 3) result 1
                    всегда возвращает положительное число. Если второе число равно 0, то результатом будет NULL.

PI                  возвращает значение математической константы Пи (3.14159265358979323846)  PI() result 3.141592653589793
POWER               возвращает результат возведения числа в степень. POWER(основание_степени, показатель_степени) POWER(2, 3) result 8  эквивалентно выражению 2^3 = 8.
RADIANS             преобразует градусы в радианы. RADIANS(угол в градусах)  угол в 180 градусов равен PI радианам (3.141592653589793)
RAND                которая возвращает случайное число в диапазоне от 0 до 1. RAND()  Результат: 0.5298371105
SIGN                возвращает 1, 0 или -1 в зависимости от того, положительное, нулевое или отрицательное число соответственно.SIGN(выражение, которое вычисляется как число)
SIN                 возвращает синус угла в радианах. SIN(угол в радианах)
SQRT                возвращает квадратный корень числа. всегда возвращает неотрицательный квадратный корень. 
                    Если вы хотите вернуть квадратный корень с отрицательным числом, то результатом будет NULL.

TAN                 возвращает тангенс угла в радианах. TAN(угол в радианах)


[https://www.sqlite.org/json1.html#jex](https://www.sqlite.org/json1.html#jex)

| Функция / Оператор                    | Описание                                                                                    | Пример использования                                                                 |
|---------------------------------------|---------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|
| JSON(json)                            | Преобразует строку в формат JSON.                                                           | JSON('{"name": "John", "age": 30}')<br>{"name":"John","age":30}                      |
| JSONB(json)                           | `JSON`, но в бинарном формате<br>для более эффективного доступа.                            | JSONB('{"name": "John", "age": 30}')                                                 |
| JSON_ARRAY(value1, value2, ...)       | Создает JSON массив из переданных аргументов.                                               | JSON_ARRAY('apple', 'banana', 'cherry')<br>["apple","banana","cherry"]               |
| JSONB_ARRAY(value1, value2, ...)      | `JSON_ARRAY`, но в бинарном формате.                                                        | JSONB_ARRAY('apple', 'banana', 'cherry')                                             |
| JSON_ARRAY_LENGTH(json, [path])       | Возвращает количество элементов<br>в массиве.                                               | JSON_ARRAY_LENGTH('["apple", "banana", "cherry"]')<br>3<br>JSON_ARRAY_LENGTH('["apple", "banana", "cherry"]', '$')<br>3<br>JSON_ARRAY_LENGTH('{"fruits": ["apple", "banana", "cherry"]}', '$.fruits')<br>3      |
| JSON_ERROR_POSITION(json)             | Возвращает позицию ошибки в JSON строке,<br>если JSON недействителен.                       | JSON_ERROR_POSITION('{"name": "John", "age": 30,}')                                  |
| JSON_EXTRACT(json, path, ...)         | Извлекает значение по заданному пути.                                                       | JSON_EXTRACT('{"name": "John", "age": 30}', '$.name')<br>John                        |
| JSONB_EXTRACT(json, path, ...)        | `JSON_EXTRACT`, но работает с бинарными JSON данными.                                       | JSONB_EXTRACT('{"name": "John", "age": 30}', '$.name')                               |
| json -> path                          | Извлекает значение по заданному пути<br>`JSON_EXTRACT`.                                     | '{"name": "John", "age": 30}' -> '$.name'<br>John                                    |
| json ->> path                         | Извлекает значение по заданному пути<br>и преобразует его в текст<br>`JSON_EXTRACT`.        | '{"name": "John", "age": 30}' ->> '$.name'<br>John                                   |
| JSON_INSERT(json, path, value, ...)   | Вставляет новое значение по заданному пути.                                                 | JSON_INSERT('{"name": "John"}', '$.age', 30)<br>{"name":"John","age":30}             |
| JSONB_INSERT(json, path, value, ...)  | `JSON_INSERT`, но с бинарными JSON данными.                                                 | JSONB_INSERT('{"name": "John"}', '$.age', 30)                                        |
| JSON_OBJECT(label1, value1, ...)      | Создает JSON объект из пар "ключ-значение".                                                 | JSON_OBJECT('name', 'John', 'age', 30)<br>{"name":"John","age":30}                   |
| JSONB_OBJECT(label1, value1, ...)     | `JSON_OBJECT`, но в бинарном формате.                                                       | JSONB_OBJECT('name', 'John', 'age', 30)                                              |
| JSON_PATCH(json1, json2)              | Объединяет два JSON<br>значения из второго документа<br>перезаписывают значения из первого. | JSON_PATCH('{"name": "John"}', '{"age": 30}')<br>{"name":"John","age":30}            |
| JSONB_PATCH(json1, json2)             | `JSON_PATCH`, но с бинарными JSON данными.                                                  | JSONB_PATCH('{"name": "John"}', '{"age": 30}')                                       |
| JSON_PRETTY(json)                     | Форматирует JSON для более удобного чтения.                                                 | JSON_PRETTY('{"name": "John", "age": 30}')                                           |
| JSON_REMOVE(json, path, ...)          | Удаляет значение по заданному пути.                                                         | JSON_REMOVE('{"name": "John", "age": 30}', '$.age')<br>{"name":"John"}               |
| JSONB_REMOVE(json, path, ...)         | `JSON_REMOVE`, но с бинарными JSON данными.                                                 | JSONB_REMOVE('{"name": "John", "age": 30}', '$.age')                                 |
| JSON_REPLACE(json, path, value, ...)  | Заменяет значение в JSON документе<br>по заданному пути (если путь существует).             | JSON_REPLACE('{"name": "John", "age": 30}', '$.age', 31)<br>{"name":"John","age":31} |
| JSONB_REPLACE(json, path, value ,...) | `JSON_REPLACE`, но с бинарными JSON данными.                                                | JSONB_REPLACE('{"name": "John", "age": 30}', '$.age', 31)                            |
| JSON_SET(json, path, value, ...)      | Устанавливает значение по заданному пути.                                                   | JSON_SET('{"name": "John", "age": 30}', '$.age', 31)<br>{"name":"John","age":31}     |
| JSONB_SET(json, path, value, ...)     | `JSON_SET`, но с бинарными JSON данными.                                                    | JSONB_SET('{"name": "John", "age": 30}', '$.age', 31)                                |
| JSON_TYPE(json, [path])               | Возвращает тип значения<br>по заданному пути в JSON документе.                              | JSON_TYPE('{"name": "John", "age": 30}')<br>object<br>JSON_TYPE('{"name": "John", "age": 30}', '$')<br>object<br>JSON_TYPE('{"name": "John", "age": 30}', '$.name')<br>text                           |
| JSON_VALID(json)                      | Проверяет, является ли строка<br>допустимым JSON документом.                                | JSON_VALID('{"name": "John", "age": 30}')<br>1                                       |
| JSON_VALID(json, flags)               | `JSON_VALID`, но с флагами для проверки.                                                    | JSON_VALID('{"name": "John", "age": 30}', 0)                                         |
| JSON_QUOTE(value)                     | Кавычит значение для включения в JSON документ.                                             | JSON_QUOTE('John')<br>"John"                                                         |

""",
            },
            "PostgreSQL": {
                "Типы данных": """
# Числовые типы

| Имя              | Размер     | Описание                                  | Диапазон                                              |
|------------------|------------|-------------------------------------------|-------------------------------------------------------|
| smallint         | 2 байта    | Целое в небольшом диапазоне               | -32768 .. +32767                                      |
| integer          | 4 байта    | Типичный выбор для целых чисел            | -2147483648 .. +2147483647                            |
| bigint           | 8 байт     | Целое в большом диапазоне                 | -9223372036854775808 .. 9223372036854775807           |
| decimal          | переменный | Вещественное число с указанной точностью  | до 131072 цифр до десятичной точки и до 16383 — после |
| numeric          | переменный | Вещественное число с указанной точностью  | до 131072 цифр до десятичной точки и до 16383 — после |
| real             | 4 байта    | Вещественное число с переменной точностью | точность в пределах 6 десятичных цифр                 |
| double precision | 8 байт     | Вещественное число с переменной точностью | точность в пределах 15 десятичных цифр                |
| smallserial      | 2 байта    | Небольшое целое с автоувеличением         | 1 .. 32767                                            |
| serial           | 4 байта    | Целое с автоувеличением                   | 1 .. 2147483647                                       |
| bigserial        | 8 байт     | Большое целое с автоувеличением           | 1 .. 9223372036854775807                              |

`numeric` стоит использовать для различных "денежных" вещей, где недопустимо "потерять копейку на округлениях":

```sql
SELECT 3.1415926::real;
--     3.1415925 - чуток потеряли
SELECT 3.1415926::numeric;
--     3.1415926 - а тут все четко
```

`serial`-псевдотипы (аналог `AUTO_INCREMENT / IDENTITY` из других СУБД),
Позволяют определить поля с автоматически формируемым возрастающим значением "по умолчанию": `1, 2, 3, ...`

Нет `unsigned` - все числовые типы знаковые, поэтому "честно" положить диапазон `[0x00000000..0xFFFFFFFF]` в `integer` не получится,
только со смещением "наполовину"

# Символьные типы

| Имя                                 | Описание                                               |
|-------------------------------------|--------------------------------------------------------|
| character varying(n), varchar(n)    | Строка ограниченной переменной длины                   |
| character(n), char(n), bpchar(n)    | Строка фиксированной длины, дополненная пробелами      |
| bpchar                              | Строка неограниченной переменной длины с удалением пробелов |
| text                                | Строка неограниченной переменной длины                 |

Указание ограничения длины не дает никаких бонусов.
За исключением случаев, когда вам действительно требуется ограничить длину записываемого в поле
Например, для 2-буквенного кода страны.

# Типы даты/времени

[Дата и время](https://postgrespro.ru/docs/postgresql/16/datatype-datetime) в `PostgreSQL`, технически, хранятся как целочисленные,
со значением от [POSTGRES_EPOCH](https://github.com/postgres/postgres/blob/871fe4917e1e92304bdcc2ab779de7416492c6de/src/include/datatype/timestamp.h#L235)(01.01.2000) в соответствующих единицах (микросекундах или сутках):

| Имя                                 | Размер  | Описание                               | Наименьшее значение | Наибольшее значение | Точность       |
|-------------------------------------|---------|----------------------------------------|---------------------|---------------------|----------------|
| timestamp [(p)] [without time zone] | 8 байт  | Дата и время (без часового пояса)      | 4713 до н. э.       | 294276 н. э.        | 1 микросекунда |
| timestamp [(p)] with time zone      | 8 байт  | Дата и время (с часовым поясом)        | 4713 до н. э.       | 294276 н. э.        | 1 микросекунда |
| date                                | 4 байта | Дата (без времени суток)               | 4713 до н. э.       | 5874897 н. э.       | 1 день         |
| time [(p)] [without time zone]      | 8 байт  | Время суток (без даты)                 | 00:00:00            | 24:00:00            | 1 микросекунда |
| time [(p)] with time zone           | 12 байт | Время дня (без даты), с часовым поясом | 00:00:00+1559       | 24:00:00-1559       | 1 микросекунда |
| interval [ поля ] [(p)]             | 16 байт | Временной интервал                     | -178000000 лет      | 178000000 лет       | 1 микросекунда |

В этом их отличие от некоторых других СУБД, где  может храниться как текстовая строка.

Арифметические операции как над числами над `timestamp` тоже допустимы, в том числе преобразование к Unix time (время от `01.01.1970`)

```sql
SELECT '2024-01-01'::date - 1;
-- 2023-12-31 - за день до
SELECT '2024-01-01'::date - 8 * '1 hour'::interval;
-- 2023-12-31 16:00:00 - за 8 часов до
SELECT extract(epoch from '2024-01-01'::timestamp);
-- 1704067200 - превратили timestamp в double precision
SELECT '1970-01-01 00:00:00'::timestamp + 1704067200 * '1 second'::interval;
-- 2024-01-01 00:00:00 - ... и обратно
```

Во временном значении можно использовать часовой пояс `with time zone`
или указывать сохраняемую точность (`timestamp(0)` означает хранение "до секунд").

# Логический тип

| Имя     | Размер | Описание                   |
|---------|--------|----------------------------|
| boolean | 1 байт | Состояние: истина или ложь |

Он может принимать значения `TRUE`/`FALSE` и `NULL`, равно как и любой другой тип.


# Специальные типы данных

Помимо базовых типов, "из коробки" `PostgreSQL` предоставляет массу других, более специализированных, типов:

- двоичные данные
- перечисления
- геометрические
- сетевые адреса
- битовые строки
- вектора текстового поиска
- UUID
- XML
- JSON
- массивы
- диапазоны

Например, всякие картографические сервисы любят использовать [геометрические типы](https://postgrespro.ru/docs/postgresql/16/datatype-geometric) данных с расширением `PostGIS`,
а слабоструктурированные данные можно хранить в [JSON](https://postgrespro.ru/docs/postgresql/16/datatype-json), причем ничуть не хуже какой-нибудь `MongoDB`,
а идентификаторы в распределенных системах - в [UUID](https://postgrespro.ru/docs/postgresql/16/datatype-uuid).

Если вдруг и этих типов вам окажется мало – можно [создать свой](https://postgrespro.ru/docs/postgresql/16/sql-createtype) и работать с ним как с любым другим полем.
Главное, правильно его описать, задать соответствующие функции ввода-вывода, хранения и обработки.

Вообще, PostgreSQL очень хорошо расширяем, поэтому `EXTENSION`'ы, которые для него можно найти и подключить,
составляют достаточно весомую часть его преимуществ по отношению к другим СУБД.


""",
                "pg_hba.conf": r"""
```bash
notepad "C:\Program Files\PostgreSQL\16\data\pg_hba.conf"
```

```bash
net stop postgresql-x64-16
net start postgresql-x64-16
```

# Запись может быть сделана в одном из семи форматов

> local      база  пользователь  метод-аутентификации  [параметры-аутентификации]
> host       база  пользователь  адрес  метод-аутентификации  [параметры-аутентификации]
> hostssl    база  пользователь  адрес  метод-аутентификации  [параметры-аутентификации]
> hostnossl  база  пользователь  адрес  метод-аутентификации  [параметры-аутентификации]
> host       база  пользователь  IP-адрес  IP-маска  метод-аутентификации  [параметры-аутентификации]
> hostssl    база  пользователь  IP-адрес  IP-маска  метод-аутентификации  [параметры-аутентификации]
> hostnossl  база  пользователь  IP-адрес  IP-маска  метод-аутентификации  [параметры-аутентификации]


|                          |        |
|--------------------------|--------|
| local                    | Unix-сокеты                                                             |
| host                     | Подключения по `TCP/IP`. С `SSL` и без `SSL`.                           |
| hostssl                  | Подключения по `TCP/IP` с применением шифрования `SSL`.                 |
| hostnossl                | Противоположен `hostssl`. Подключения по `TCP/IP` без шифрования `SSL`. |
| база                     | - `all` - все базы данных<br>- `sameuser` - имя запрашиваемой базы данных совпадает с именем запрашиваемого пользователя<br>- `samerole` - запрашиваемый пользователь должен быть членом роли с таким же именем, как и у запрашиваемой базы данных.<br>  (`samegroup` — это устаревший, но допустимый вариант значения `samerole`.)<br>  Суперпользователи не становятся членами роли автоматически из-за `samerole`,<br>  а только если они являются явными членами роли, прямо или косвенно, и не только из-за того, что они суперпользователи.<br>- `replication` - если запрашивается подключение для физической репликации (для таких подключений не выбирается какая-то конкретная база данных).<br>Любое другое значение воспринимается как имя определённой базы `Postgres Pro`.<br>Несколько имён баз данных можно указать, разделяя их запятыми.<br>Файл, содержащий имена баз данных, можно указать, поставив знак `@` в начале его имени. |
| пользователь             | - `all` - все пользователи.<br>  Имя группы начинается с `+`.<br>  (В `Postgres Pro` нет никакой разницы между пользователем и группой; знак + означает «совпадение любых ролей,<br>   которые прямо или косвенно являются членами роли», тогда как имя без знака `+` является подходящим только для этой конкретной роли.)<br>  Суперпользователь рассматривается как член роли, только если он явно является членом этой роли, прямо или косвенно,<br>  а не только потому, что он является суперпользователем.<br>Несколько имён пользователей можно указать, разделяя их запятыми.<br>Файл, содержащий имена пользователей, можно указать, поставив знак `@` в начале его имени. |
| адрес                    | ip/mask<br>- `all` - любой IP-адрес<br>- `samehost` - любые IP-адреса данного сервера- <br>- `samenet` - любой адрес любой подсети, к которой сервер подключён напрямую<br><br>Имени, начинающееся с точки `.`, соответствует суффиксу актуального имени узла.<br>Так, `.example.com` будет соответствовать `foo.example.com` (а не только `example.com`).<br>Это поле применимо только к записям `host`, `hostssl` и `hostnossl`. |
| метод-аутентификации     | - `trust` - Разрешает безусловное подключение.<br>  Этот метод позволяет тому, кто может подключиться к серверу с базой данных `Postgres Pro`,<br>  войти под любым желаемым пользователем `Postgres Pro` без введения пароля и без какой-либо другой аутентификации. [Подробности](https://postgrespro.ru/docs/postgrespro/10/auth-methods#AUTH-TRUST)<br>- `reject` - Отклоняет подключение безусловно.<br>  Полезна для «фильтрации» некоторых серверов группы, например, строка `reject` может отклонить попытку подключения одного компьютера,<br>  при этом следующая строка позволяет подключиться остальным компьютерам в той же сети.<br>- `scram-sha-256` Проверяет пароль пользователя, производя аутентификацию `SCRAM-SHA-256`. [Подробности](https://postgrespro.ru/docs/postgrespro/10/auth-methods#AUTH-PASSWORD)<br>- `md5` Проверяет пароль пользователя, производя аутентификацию `SCRAM-SHA-256` или `MD5`. [Подробности](https://postgrespro.ru/docs/postgrespro/10/auth-methods#AUTH-PASSWORD)<br>- `password` Требует для аутентификации введения клиентом незашифрованного пароля.<br>  Поскольку пароль посылается простым текстом через сеть, такой способ не стоит использовать, если сеть не вызывает доверия. [Подробности](https://postgrespro.ru/docs/postgrespro/10/auth-methods#AUTH-PASSWORD)<br>- `gss` Для аутентификации пользователя использует `GSSAPI`. Этот способ доступен только для подключений по `TCP/IP`. [Подробности](https://postgrespro.ru/docs/postgrespro/10/auth-methods#GSSAPI-AUTH)<br>- `sspi` Для аутентификации пользователя использует `SSPI`. Способ доступен только для `Windows`. [Подробности](https://postgrespro.ru/docs/postgrespro/10/auth-methods#SSPI-AUTH)<br>- `ident` Получает имя пользователя операционной системы клиента, связываясь с сервером `Ident`,<br>  и проверяет, соответствует ли оно имени пользователя базы данных.<br>  Аутентификация ident может использоваться только для подключений по `TCP/IP`.<br>  Для локальных подключений применяется аутентификация peer. [Подробности](https://postgrespro.ru/docs/postgrespro/10/auth-methods#AUTH-IDENT)<br>- `peer` Получает имя пользователя операционной системы клиента из операционной системы и проверяет,<br>  соответствует ли оно имени пользователя запрашиваемой базы данных.<br>  Доступно только для локальных подключений. [Подробности](https://postgrespro.ru/docs/postgrespro/10/auth-methods#AUTH-PEER)<br>- `ldap` Проводит аутентификацию, используя сервер `LDAP`. [Подробности](https://postgrespro.ru/docs/postgrespro/10/auth-methods#AUTH-LDAP)<br>- `radius` Проводит аутентификацию, используя сервер `RADIUS`. [Подробности](https://postgrespro.ru/docs/postgrespro/10/auth-methods#AUTH-RADIUS)<br>- `cert` Проводит аутентификацию, используя клиентский сертификат `SSL`. [Подробности](https://postgrespro.ru/docs/postgrespro/10/auth-methods#AUTH-CERT)<br>- `pam` Проводит аутентификацию, используя службу подключаемых модулей аутентификации `PAM`, предоставляемую операционной системой. [Подробности](https://postgrespro.ru/docs/postgrespro/10/auth-methods#AUTH-PAM)<br>- `bsd` Проводит аутентификацию, используя службу аутентификации `BSD`, предоставляемую операционной системой. [Подробности](https://postgrespro.ru/docs/postgrespro/10/auth-methods#AUTH-BSD) |
| параметры-аутентификации | `имя=значение`<br>`clientcert` можно задать в любой записи hostssl.<br>Если он равен `1`, клиент должен представить подходящий (доверенный) сертификат `SSL`,<br>в дополнение к другим требованиям метода проверки подлинности. |




> Удалённое соединение по `TCP/IP` невозможно, если сервер запущен без определения соответствующих значений
> для параметра конфигурации `listen_addresses`, поскольку по умолчанию система принимает подключения по `TCP/IP`
> только для локального адреса замыкания `localhost`.

[https://postgrespro.ru/docs/postgrespro/10/auth-pg-hba-conf](https://postgrespro.ru/docs/postgrespro/10/auth-pg-hba-conf)
""",
                "CREATE": """
```sql
CREATE ACCESS METHOD
CREATE AGGREGATE
CREATE CAST
CREATE COLLATION
CREATE CONVERSION
CREATE DATABASE -- Создание базы данных
CREATE DOMAIN
CREATE EVENT TRIGGER
CREATE EXTENSION
CREATE FOREIGN DATA WRAPPER
CREATE FOREIGN TABLE
CREATE FUNCTION
CREATE GROUP
CREATE INDEX
CREATE LANGUAGE
CREATE MATERIALIZED VIEW
CREATE OPERATOR
CREATE OPERATOR CLASS
CREATE OPERATOR FAMILY
CREATE POLICY
CREATE PROCEDURE
CREATE PUBLICATION
CREATE ROLE -- Роли базы данных
CREATE RULE
CREATE SCHEMA
CREATE SEQUENCE
CREATE SERVER
CREATE STATISTICS
CREATE SUBSCRIPTION
CREATE TABLE -- Создание таблицы
CREATE TABLE AS
CREATE TABLESPACE -- Табличные пространства
CREATE TEXT SEARCH CONFIGURATION
CREATE TEXT SEARCH DICTIONARY
CREATE TEXT SEARCH PARSER
CREATE TEXT SEARCH TEMPLATE
CREATE TRANSFORM
CREATE TRIGGER
CREATE TYPE
CREATE USER
CREATE USER MAPPING
CREATE VIEW
```

```sql
CREATE DATABASE tst;

CREATE TABLE tbl(
    k integer,  -- Имя поля Тип поля
    v text
);
```

```sql
'st''r'  -- это строка с одинарным апострофом
E'st\\'r' -- ... и это – она же
$$st'r$$ -- ... и даже вот это
$abcd$st'r$abcd$
```

[https://habr.com/ru/companies/tensor/articles/779698/](https://habr.com/ru/companies/tensor/articles/779698/)
""",
                "Картинки": """
![distinct.png](Languages/SQL/PostgreSQL/distinct.png)
![is_distinct.png](Languages/SQL/PostgreSQL/is_distinct.png)
""",
            },
            "Картинки": r"""
![sql.png](Languages/SQL/sql.png)
![chshpart1.jpg](Languages/SQL/chshpart1.jpg)
![chshpart2.jpg](Languages/SQL/chshpart2.jpg)
""",
        },
        "Dockerfile": {
            "Dockerfile": """Dockerfile
FROM:    Определяет базовый образ, на основе которого будет создан ваш образ контейнера. 
         Здесь мы используем образ `Python 3.9` на основе `slim-версии Debian`.

WORKDIR: Устанавливает рабочую директорию внутри контейнера, где будут выполняться команды.

COPY:    Копирует файлы из текущей директории на вашем компьютере внутрь контейнера.

RUN:     Выполняет команды внутри контейнера для установки зависимостей, указанных в файле `requirements.txt`.

CMD:     Определяет команду, которая будет запущена при запуске контейнера. 
         Здесь мы указываем запуск основного скрипта `main.py`.

```Dockerfile@Dockerfile
FROM python:3.9-slim-buster

WORKDIR /app

COPY requirements.txt .

RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python3", "main.py"]
```


```Dockerfile
ENV BOT_TOKEN=""
```

![docker.png](Languages/Dockerfile/docker.png)
""",
            "RUN mkdir -p": r"""
Команда `mkdir` используется для создания новой директории.

Флаг `/p` позволяет создать директорию и ее родительские директории, если они еще не существуют. 
Например:

```Dockerfile
RUN mkdir C:\app\data\logs /p
```

Если же использовать команду `RUN mkdir C:\app\data\logs` 
и директория `C:\app\data` еще не существует, то команда `mkdir` вернет ошибку.
""",
        },
        "JavaScript": {
            "Списки": """
```js
let myArray = [1, 2, 3, 4, 5];
console.log(myArray.length); // Outputs 5
```

 or == ||
and == &&

```js
let list = ["apple", "banana", "orange"];
let textToCheck = "banana";

if (list.includes(textToCheck)) {
    console.log("Text exists in the list");
} else {
    console.log("Text does not exist in the list");
}
```
""",
            "for": """
Цикл for в JavaScript используется для выполнения одного 
или нескольких операторов многократно, пока условие в цикле истинно. 
Синтаксис цикла for выглядит следующим образом:

```js
for (initialization; condition; final-expression) {
   statement(s)
}
```

initialization     выполняется один раз перед началом цикла 
                   и обычно используется для инициализации счетчика цикла.
condition          условие, которое проверяется перед каждой итерацией цикла. 
                   Если условие истинно, то тело цикла выполняется, иначе цикл завершается.
final-expression   выполняется после каждой итерации цикла 
                   и обычно используется для изменения счетчика цикла.
statement(s)       один или несколько операторов, которые выполняются в теле цикла.

```js
for (let i = 0; i < 5; i++) {
   console.log(i);
}
```

Цикл по списку

```js
var myArray = [1, 2, 3, 4, 5];
for (var i = 0; i < myArray.length; i++) {
  console.log(myArray[i]);
}
```

или

```js
var myArray = [1, 2, 3, 4, 5];
for (const element of myArray) {
  console.log(element);
}
```
""",
            "handlebar": """Пробел ! " # % & ' ( ) * + , . / ; < = > @ [ \ ] ^ ` { | } ~

""",
            "Переменные": """в JavaScript можно создать глобальную переменную, которая будет доступна 
во всем скрипте, даже после завершения функции. Для этого нужно просто объявить переменную
вне функции, без использования ключевого слова `var`, `let` или `const`.

```js
// Глобальная переменная
let myGlobalVariable = "Hello, World!";

function myFunction() {
  // Использование глобальной переменной
  console.log(myGlobalVariable);
}

myFunction(); // "Hello, World!"
console.log(myGlobalVariable); // "Hello, World!"
```

Однако, использование глобальных переменных может приводить к проблемам 
с организацией кода и конфликтам имен, поэтому рекомендуется использовать их с осторожностью.
""",
            "Ключевые слова для объявления переменных и констант": """
| **Ключевое слово** | **Описание**                                                                              | **Область видимости**        | **Повторное объявление**     | **Повторное присвоение**                                                    |
|--------------------|-------------------------------------------------------------------------------------------|------------------------------|------------------------------|-----------------------------------------------------------------------------|
| `var`              | Объявляет переменную.<br>Поддерживает функции и глобальную область видимости.             | Функциональная<br>Глобальная | **Можно** переопределять  | **Можно** повторно присвоить                                             |
| `let`              | Объявляет переменную с блочной областью видимости.                                        | Блочная                      | **Можно** переопределять  | **Можно** повторно присвоить                                             |
| `const`            | Объявляет константу с блочной областью видимости.                                         | Блочная                      | **Нельзя** переопределять | Значение **нельзя** изменить<br>(но объект или массив могут изменяться). |
| `class`            | Объявляет класс.<br>Поддерживает блочную область видимости.                               | Блочная                      | **Нельзя** переопределять | **Нельзя** повторно присваивать класс                                    |
| `function`         | Объявляет функцию.<br>Поддерживает функциональную область видимости.                      | Функциональная               | **Можно** переопределять  | **Можно** повторно присвоить                                             |
| `let` (в циклах)   | Используется для объявления переменной,<br>которая уникальна в каждой итерации цикла.     | Блочная                      | **Можно** переопределять  | **Можно** повторно присвоить                                             |
| `var` (в циклах)   | Переменная в цикле `var` не уникальна<br>для каждой итерации, что может вызвать проблемы. | Функциональная               | **Можно** переопределять  | **Можно** повторно присвоить                                             |

### Примеры использования

#### `var`

```javascript
function exampleVar() {
    if (true) {
        var x = 1; // `x` доступна в функции
    }
    console.log(x); // 1
}
```

#### `let`

```javascript
function exampleLet() {
    if (true) {
        let y = 1; // `y` доступна только в блоке
    }
    console.log(y); // Ошибка: y is not defined
}
```

#### `const`

```javascript
function exampleConst() {
    const z = 2;
    z = 3; // Ошибка: Assignment to constant variable
}
```

#### `class`

```javascript
class Person {
    constructor(name) {
        this.name = name;
    }

    greet() {
        console.log(`Hello, my name is ${this.name}`);
    }
}

const person = new Person("Alice");
person.greet(); // Hello, my name is Alice
```

#### `function`

```javascript
function greet(name) {
    console.log(`Hello, ${name}`);
}

greet("Bob"); // Hello, Bob
```

### Функциональная область видимости

Переменная объявленная с помощью `var` и функции доступна в пределах функции, где она была объявлена,
или глобально, если объявлена вне функции.

### Блочная область видимости

Переменные и константы, объявленные с помощью `let`, `const`, и классов,
доступны только в блоке, где они были объявлены.
""",
        },
        "CSS": {
            "css-text": {
                "Backgrounds": """
# Backgrounds

```css
background
background-image
background-position
background-size
background-repeat
background-attachment
background-origin
background-clip
background-color
background-image

url | Gradients | none

background-position
 top left   |   top center  |   top right
center left | center center | center right
bottom left | bottom center | bottom right

x-% y-%
X-pos y-pos

background-size
length
%
auto | cover | contain

background-repeat
repeat | repeat-x | repeat-y | no-repeat

background-attachment
scroll | fixed | local

background-origin
border-box | padding-box | content-box

background-clip
border-box | padding-box | content-box | no-clip

background-color
color
transparent
```
""",
                "Border": """
# Border

```css
border
border-width
border-style
border-color

border-width
thin | medium | thick | length

border-style
none | hidden | dotted
dashed | solid | double
groove | ridge | inset | outset

border-color
color

border-left
border-left-width
border-style
border-color
border-left-style
border-style
border-left-color
border-color

border-left-width
thin | medium | thick length

border-right
border-right-width
border-style
border-color

border-right-style
border-style
border-right-color
border-color

border-right-width
thin | medium | thick | length

border-top
border-top-width
border-style
border-color
border-top-style
border-style







border-top-color
border-color

border-top-width
thin | medium | thick | length

border-bottom
border-bottom-width
border-style
border-color

border-bottom-color
border-color

border-bottom-style
border-style

border-break
border-width
border-style
color
close

box-shadow
inset | | [ length, length, length, length | | <color> ]
none

border-collapse
collapse | separate

border-image
image
[ number / % border-width stretch | repeat | round ] none

border-radius
border-radius
border-top-right-radius
border-bottom-right-radius
border-bottom-left-radius
border-top-left-radius
border-top-right-radius
length
border-bottom-left-radius
length
border-bottom-right-radius
length
```
""",
                "table": """
# Table

```css
border-collapse
collapse | separate

empty-cells
show | hide

border-spacing
length length

table-layout
auto | fixed

caption-side
top | bottom | left | right
```
""",
                "boxmodel": """
# Box Model

```css
float
left | right | none

height
auto
length
%

max-height
none
length
%

max-width
none
length
%

min-height
none
length
%

width
auto
%
length

margin-top
margin-right
margin-bottom
margin-left

margin-bottom
auto
length
%

margin-left
auto
height
%

margin-right
auto
height
%

margin-top
auto
length
max-width





padding
padding-top
padding-right
padding-bottom
padding-left

podding-bottom
length
%

padding-left
length
%

padding-right
length
%

padding-top
length
%

display
none | inline | block | inline-block
list-item | run-in | compact | table
inline-table | table-row-group | table-header-group
table-footer-group | table-row | table-column-group
table-column | table-cell | table-caption | ruby
ruby-base | ruby-text | ruby-base-group | ruby-text-group
inline-flex | inline-grid | contents

overflow
visible | hidden | scroll
auto | no-display | no-content
overflow-x
overflow-y

overflow-style
auto | marquee-line | marqueeblock

overflow-x
visible | hidden | scroll
auto | no-display | no-content

rotation
angle

rotation-point
position (paired value off-set)

visibility
visible | hidden | collapse
clear
left | right | both | none
```
""",
                "font": """
# Font

```css
font
font-style
font-variant
font-weight
font-size/line-height
font-family
caption | icon | menu | messagebox
small-caption | status-bar

font-size-adjust
none | inherit
number

font-family
serif | sans-serif | monospace
cursive | fantasy } system-vi | emoji
math | fangsong
inherit | initial | unset

font-style
normal | italic | oblique
inherit

font-variant
normal | small-caps | inherit

font-size
xx-small | x-small | small
medium | large | x-large | xxlarge
smalller | larger

inherit
length
%

font-weight
normal | bold | bolder | lighter
100 | 200 | 300 | 400 | 500
600 | 700 | 800 | 900 | inherit
```
""",
                "text": """
# Text

```css
direction
ltr | rtl | inherit

hanging-punctuation
none | [ start | end | endedge ]

letter-spacing
normal
length
%

text-outline
none
color
length

unicode-bidi
normal | embed | bidi-override

white-space
normal | pre | nowrap | pre-wrap | pre-line

white-space-collapse
preserve | collapse | preserve-breaks | discard

punctuation-trim
none | [start | end | adjacent ]

text-align
start | end | left | right | center | justify

text-align-last
start | end | left | right | center | justify

text-decoration
none | underline | overline | line-through | blink

text-shadow
none
color
length

word-break
normal | keep-all | loose | break-strict | break-all

word-wrap
normal
nowrap

text-emphasis
none | [ [ accent | dot | circle | disc | [ before | after ] ? ]

text-indent
length
%

text-justify
auto | inter-word | interideograph
inter-cluster | distribute | kashida | tibetan

text-transform
none | capitalize | uppercase | lowercase

text-wrap
normal | unrestricted | none | suppress

word-spacing
normal
length
%
```
""",
                "color_angles_time_frequency": """
# Color

```css
color
inherit
color

opacity
inherit
number
```

# Angles

```css
deg - degrees
grad - grads
rad - radians
turn - turns
```

# Time

```css
ms - milli-seconds
s - seconds
```

# Frequency

```css
Hz - heriz
kHz - kilo-hertz
```
""",
                "animations": """
# Animations

```css
animations
animation-name
animation duration
animation-timing-function
animation-delay
animation-iteration-count
animation-direction

animation-name
none | IDENT
animation-duration
time

animation-timing-function
ease | linear | ease-in | ease-out
ease-in-out | cubic-Bezier
(number, number, number, number)

animation-delay
Time

animation-iteration-count
inherit
number

animation-direction
normal | alternate

animation-play-state
running | paused
```
""",
                "speech": """
# Speech

```css
cue
cue-before
cue-after

cue before
url [ silent | x-soft | soft | medium
loud | x-loud | none | inherit ]
number
%

cue-after
url [ silent | x-soft | soft | medium
loud | x-loud | none | inherit ]
number
%

mark
mark-before
mark after

mark-before
string

mark-alter
string

voice-pitch-range
x-low | low | medium | high
xhigh | inherit
number

voice-stress
strong | moderate | none
reduced | inherit

voice-volume
silent | x soft | sofi | medium
loud | x-loud | inherit
number
%

pause
pause-before
pause-after

pause-before
none | x-weak | weak | medium
strong | x-strong | inherit
time

pause after
none | x-weak | weak | medium
strong | x-strong | inherit
time

phonemes
string

voice-duration
time

voice-family
inherit | [ <specific-voice, age,
generic-voice, number> ]

voice-rate
x-slow | slow | medium | fast
x-fast | inherit

voice-pitch
x-low | low | medium | high
x-high | inherit
number
%

caption-side
top | bottom | left | right

rest
rest-before
rest-alter

rest-before
none | x-weak | weak | medium
strong
| x-strong | inherit
time

rest after
none | x-weak | weak | medium
x-strong | inherit

speak
none | normal | spell-out | digits | literal-punctuation | no-punctuation | inherit-number
```
""",
                "transitions": """
# Transitions

```css
transitions
transition-property
transitions-duration
transitions-timing-function
transitions-delay

transitions-delay
time

transitions-duration
time

transitions-property
none | all

transition-timing-function
ease | linear | ease-in | ease-out
ease-in-out | cubic-Bezier
(number, number, number, number)
```
""",
                "ui": """""",
                "column": """""",
                "list and markers": """""",
                "absolute measurement": """""",
                "pseudo element": """""",
                "pseudo class": """""",
                "colors": """""",
                "outlin": """""",
                "relative measurement": """""",
            },
            "css-img": r"""

![                  background.png](Languages/CSS/background.png)
![                      border.png](Languages/CSS/border.png)
![                       table.png](Languages/CSS/table.png)
![                    boxmodel.png](Languages/CSS/boxmodel.png)
![                        font.png](Languages/CSS/font.png)
![                        text.png](Languages/CSS/text.png)
![ color_angles_time_frequency.png](Languages/CSS/color_angles_time_frequency.png)
![                  animations.png](Languages/CSS/animations.png)
![                      speech.png](Languages/CSS/speech.png)
![                 transitions.png](Languages/CSS/transitions.png)
![                          ui.png](Languages/CSS/ui.png)
![                      column.png](Languages/CSS/column.png)
![            list and markers.png](Languages/CSS/list and markers.png)
![        absolute measurement.png](Languages/CSS/absolute measurement.png)
![              pseudo element.png](Languages/CSS/pseudo element.png)
![                pseudo class.png](Languages/CSS/pseudo class.png)
![                      colors.png](Languages/CSS/colors.png)
![                     outline.png](Languages/CSS/outline.png)
![        relative measurement.png](Languages/CSS/relative measurement.png)

![              selector types.png](Languages/selector types.png)
![             2d 3d transform.png](Languages/2d 3d transform.png)
![           generated content.png](Languages/generated content.png)
![                   hyperlink.png](Languages/hyperlink.png)
![                 positioning.png](Languages/positioning.png)
![                    line box.png](Languages/line box.png)
![                 paged media.png](Languages/paged media.png)
""",
            "Селекторы": r"""
![selectors.png](Languages/CSS/css_selectors.png)
""",
            "Единицы измерения": """
| **Единица измерения**     | **Символ**  | **Тип**       | **Описание**                                                                        |
|---------------------------|-------------|---------------|-------------------------------------------------------------------------------------|
| Пиксели                   | `px`        | Абсолютная    | Определяет размер в пикселях.                                                       |
| Проценты                  | `%`         | Относительная | Определяет размер относительно размера родительского элемента.                      |
| Эм                        | `em`        | Относительная | Определяет размер относительно размера шрифта родительского элемента.               |
| Корень Эм                 | `rem`       | Относительная | Определяет размер относительно размера шрифта корневого элемента `<html>`.          |
| Вьюпорт Ширина            | `vw`        | Относительная | Определяет размер относительно ширины вьюпорта (1% от ширины окна).                 |
| Вьюпорт Высота            | `vh`        | Относительная | Определяет размер относительно высоты вьюпорта (1% от высоты окна).                 |
| Вьюпорт Ширина (Минимум)  | `vmin`      | Относительная | Определяет размер относительно минимального значения ширины или высоты вьюпорта.    |
| Вьюпорт Высота (Максимум) | `vmax`      | Относительная | Определяет размер относительно максимального значения ширины или высоты вьюпорта.   |
| Пункт                     | `pt`        | Абсолютная    | Определяет размер в пунктах (1/72 дюйма).                                           |
| Пиксель (Для мониторов)   | `dpi`       | Абсолютная    | Определяет размер в зависимости от плотности пикселей монитора (dots per inch).     |
| Пиксель (Для экранов)     | `dppx`      | Абсолютная    | Определяет размер в зависимости от плотности пикселей экрана (dots per pixel).      |
| Мм                        | `mm`        | Абсолютная    | Определяет размер в миллиметрах.                                                    |
| См                        | `cm`        | Абсолютная    | Определяет размер в сантиметрах.                                                    |
| Инч                       | `in`        | Абсолютная    | Определяет размер в дюймах (1 дюйм = 2.54 см).                                      |

### Примеры использования

```css
/* Размер в пикселях */
.box {
  width: 200px;
  height: 100px;
}

/* Размер в процентах */
.container {
  width: 80%;
}

/* Размер в эм */
.text {
  font-size: 2em; /* Размер шрифта в 2 раза больше размера шрифта родительского элемента */
}

/* Размер в корень эм */
.heading {
  font-size: 1.5rem; /* Размер шрифта в 1.5 раза больше размера шрифта корневого элемента */
}

/* Размер в вьюпорт ширины */
.full-width {
  width: 100vw; /* 100% ширины вьюпорта */
}

/* Размер в вьюпорт высоты */
.full-height {
  height: 100vh; /* 100% высоты вьюпорта */
}

/* Размер в миллиметрах */
.card {
  width: 100mm;
  height: 50mm;
}
```

Вьюпорт (viewport) - это видимая область веб-страницы на экране устройства.

![css_units.png](Languages/CSS/css_units.png)
""",
            "Переносы строк": """

[https://developer.mozilla.org/ru/docs/Web/CSS/white-space](https://developer.mozilla.org/ru/docs/Web/CSS/white-space)

Чтобы контролировать переносы строк в тексте с помощью CSS, можно использовать следующие свойства:

1. **`white-space`** — управляет переносами и пробелами.
2. **`word-break`** — управляет разбиением слов на части, если они не помещаются в одну строку.
3. **`overflow-wrap`** — управляет тем, как браузер должен переносить длинные слова, которые не умещаются в контейнер.

### Примеры

1. **Запретить переносы строк:**

Если вы хотите полностью запретить переносы строк (включая пробелы) и отображать текст в одной строке:

```css
.no-break {
  white-space: nowrap;
}
```

2. **Разрешить перенос строк только по пробелам:**

Для переноса строк только по пробелам, без разбиения слов:

```css
.break-by-space {
  white-space: normal;
  word-break: normal;
  overflow-wrap: normal;
}
```

3. **Разрешить перенос слов, если они не помещаются:**

Если слово слишком длинное и не помещается в строке, браузер может перенести его на следующую строку:

```css
.break-words {
  word-break: break-word;
  overflow-wrap: break-word;
}
```

4. **Разрешить перенос строки на любых символах (агрессивный перенос):**

Перенос строки может произойти на любом символе, если слово не помещается:

```css
.strict-break {
  word-break: break-all;
}
```
""",
        },
        "HTML": {
            "Теги": r"""
![tags1.png](Languages/HTML/tags1.png)
![tags2.png](Languages/HTML/tags2.png)
""",
            "Символы и экранирование": r"""
![html_character1.png](Languages/HTML/html_character1.png)
![html_character1.png](Languages/HTML/html_character1.png)
""",
            "tag input": """
```html
<input type="text" id="">
```

```html
<input type="password" id="">
```

```html
<input type="radio" id="">
```

```html
<input type="checkbox" id="">
```

```html
<input type="submit" id="">
```

```html
<input type="reset" id="">
```

```html
<input type="button" id="">
```

```html
<input type="file" id="">
```

```html
<input type="hidden" id="">
```

```html
<input type="image" id="">
```

```html
<input type="number" id="">
```

```html
<input type="range" id="">
```

```html
<input type="search" id="">
```

```html
<input type="email" id="">
```

```html
<input type="tel" id="">
```

```html
<input type="url" id="">
```

```html
<input type="date" id="">
```

```html
<input type="time" id="">
```

```html
<input type="week" id="">
```

```html
<input type="month" id="">
```

```html
<input type="color" id="">
```
""",
            "tag a": """
[https://www.w3schools.com/tags/tag_a.asp](https://www.w3schools.com/tags/tag_a.asp)

| Attribute        | Value           | Description |
|------------------|-----------------|-------------|
| `download`       | filename        | [download](https://www.w3schools.com/tags/att_a_download.asp)  |
| `href`           | URL             | [href](https://www.w3schools.com/tags/att_a_href.asp)          |
| `hreflang`       | language_code   | [hreflang](https://www.w3schools.com/tags/att_a_hreflang.asp)  |
| `media`          | media_query     | [media](https://www.w3schools.com/tags/att_a_media.asp)        |
| `ping`           | list_of_URLs    | Указывает разделенный пробелами список URL-адресов,<br>на которые при переходе по ссылке браузером (в фоновом режиме)<br>будут отправлены post запросы с body ping.<br>Обычно используется для отслеживания. [ping](https://www.w3schools.com/tags/att_a_ping.asp) |
| `referrerpolicy` | `no-referrer`<br>`no-referrer-when-downgrade`<br>`origin`<br>`origin-when-cross-origin`<br>`same-origin`<br>`strict-origin-when-cross-origin`<br>unsafe-url | Указывает, какую информацию о реферере следует отправлять со ссылкой [referrerpolicy](https://www.w3schools.com/tags/att_a_referrepolicy.asp) |
| `rel`            | `alternate`<br>`author`<br>`bookmark`<br>`external`<br>`help`<br>`license`<br>`next`<br>`nofollow`<br>`noreferrer`<br>`noopener`<br>`prev`<br>`search`<br>`tag` | Определяет связь между текущим документом и связанным документом. [rel](https://www.w3schools.com/tags/att_a_rel.asp) |
| `target`         | `_blank`<br>`_parent`<br>`_self`<br>`_top` | [target](https://www.w3schools.com/tags/att_a_target.asp)           |
| `type`           | media_type      | Specifies the media type of the linked document [type](https://www.w3schools.com/tags/att_a_type.asp) |


# target

| Value       | Description                                                                                      |
|-------------|--------------------------------------------------------------------------------------------------|
| `_blank`    | Открывает связанный документ в новом окне или вкладке                                            |
| `_self`     | Открывает связанный документ в том же фрейме, в котором он был нажат (это значение по умолчанию) |
| `_parent`   | Открывает связанный документ в родительском фрейме                                               |
| `_top`      | Открывает связанный документ во всем теле окна                                                   |
| `framename` | Открывает связанный документ в именованном iframe                                                |



            """,
            "Xpath": {
                "Link": """
Шпаргалка взята с сайта [https://devhints.io/xpath](https://devhints.io/xpath)
""",
                "Selectors": """
# Descendant selectors

|              |           |    |
|--------------|-----------|----|
| h1           | //h1      | ?  |
| div p        | //div//p  | ?  |
| ul > li      | //ul/li   | ?  |
| ul > li > a  | //ul/li/a |    |
| div > *      | //div/*   |    |
| :root        | /         | ?  |
| :root > body | /body     |    |

# Attribute selectors

|                      |                                    |    |
|----------------------|------------------------------------|----|
| #id                  | //*[@id="id"]                      | ?  |
| .class               | //*[@class="class"] …kinda         |    |
| input[type="submit"] | //input[@type="submit"]            |    |
| a#abc[for="xyz"]     | //a[@id="abc"][@for="xyz"]         | ?  |
| a[rel]               | //a[@rel]                          |    |
| a[href^='/']         | //a[starts-with(@href, '/')]       | ?  |
| a[href$='pdf']       | //a[ends-with(@href, '.pdf')]      |    |
| a[href*='://']       | //a[contains(@href, '://')]        |    |
| a[rel~='help']       | //a[contains(@rel, 'help')] …kinda |    |

# Order selectors

|                        |                         |    |
|------------------------|-------------------------|----|
| ul > li:first-of-type  | //ul/li[1]              | ?  |
| ul > li:nth-of-type(2) | //ul/li[2]              |    |
| ul > li:last-of-type   | //ul/li[last()]         |    |
| li#id:first-of-type    | //li[1][@id="id"]       | ?  |
| a:first-child          | //*[1][name()="a"]      |    |
| a:last-child           | //*[last()][name()="a"] |    |

# Siblings

|          |                                    |    |
|----------|------------------------------------|----|
| h1 ~ ul  | //h1/following-sibling::ul         | ?  |
| h1 + ul  | //h1/following-sibling::ul[1]      |    |
| h1 ~ #id | //h1/following-sibling::[@id="id"] |    |


# jQuery

|                            |                                |    |
|----------------------------|--------------------------------|----|
| $('ul > li').parent()      | //ul/li/..                     | ?  |
| $('li').closest('section') | //li/ancestor-or-self::section |    |
| $('a').attr('href')        | //a/@href                      | ?  |
| $('span').text()           | //span/text()                  |    |

# Other things

|                         |                                 |    |
|-------------------------|---------------------------------|----|
| h1:not([id])            | //h1[not(@id)]                  | ?  |
| Text match              | //button[text()="Submit"]       | ?  |
| Text match (substring)  | //button[contains(text(),"Go")] |    |
| Arithmetic              | //product[@price > 2.50]        |    |
| Has children            | //ul[*]                         |    |
| Has children (specific) | //ul[li]                        |    |
| Or logic                | //a[@name or @href]             | ?  |
| Union (joins results)   | //a | //div                     | ?  |

# Class check

|                                                                     |
|---------------------------------------------------------------------|
| //div[contains(concat(' ',normalize-space(@class),' '),' foobar ')] |

Xpath doesn’t have the “check if part of space-separated list” operator, so this is the workaround (source).
""",
                "Expressions": """
# Steps and axes

|         |      |      |               |
|---------|------|------|---------------|
| //      | ul   | /    | a[@id='link'] |
| Axis    | Step | Axis | Step          |


# Prefixes

| Prefix | Example             | What     |
|--------|---------------------|----------|
| //     | //hr[@class='edge'] | Anywhere |
| ./     | ./a                 | Relative |
| /      | /html/body/div      | Root     |

Begin your expression with any of these.



# Axes

| Axis | Example           | What       |
|------|-------------------|------------|
| /    | //ul/li/a         | Child      |
| //   | //[@id="list"]//a | Descendant |

Separate your steps with /. Use two (//) if you don’t want to select direct children.


# Steps

```bash
//div
//div[@name='box']
//[@id='link']
```

A step may have an element name (div) and predicates ([...]). Both are optional. They can also be these other things:

```bash
//a/text()     #=> "Go home"
//a/@href      #=> "index.html"
//a/*          #=> All a's child elements
```
""",
                "Predicates": """
# Predicates

```bash
//div[true()]
//div[@class="head"]
//div[@class="head"][@id="top"]
```

Restricts a nodeset only if some condition is true. They can be chained.

# Operators

```bash
# Comparison
//a[@id = "xyz"]
//a[@id != "xyz"]
//a[@price > 25]
```

```bash
# Logic (and/or)
//div[@id="head" and position()=2]
//div[(x and y) or not(z)]
```

Use comparison and logic operators to make conditionals.

# Using nodes

```bash
# Use them inside functions
//ul[count(li) > 2]
//ul[count(li[@class='hide']) > 0]
```

```bash
# This returns `<ul>` that has a `<li>` child
//ul[li]
```

You can use nodes inside predicates.

# Indexing

```bash
//a[1]                  # first <a>
//a[last()]             # last <a>
//ol/li[2]              # second <li>
//ol/li[position()=2]   # same as above
//ol/li[position()>1]   # :not(:first-of-type)
```

Use [] with a number, or last() or position().

# Chaining order

```bash
a[1][@href='/']
a[@href='/'][1]
```

Order is significant, these two are different.

# Nesting predicates

```bash
//section[.//h1[@id='hi']]
```
This returns &lt;section> if it has an &lt;h1> descendant with id='hi'.
""",
                "Functions": """
# Node functions

```bash
name()                     # //[starts-with(name(), 'h')]
text()                     # //button[text()="Submit"]
                           # //button/text()
lang(str)
namespace-uri()
```

```bash
count()                    # //table[count(tr)=1]
position()                 # //ol/li[position()=2]
```

# Boolean functions

```bash
not(expr)                  # button[not(starts-with(text(),"Submit"))]
```

# String functions

```bash
contains()                 # font[contains(@class,"head")]
starts-with()              # font[starts-with(@class,"head")]
ends-with()                # font[ends-with(@class,"head")]
```

```bash
concat(x,y)
substring(str, start, len)
substring-before("01/02", "/")  #=> 01
substring-after("01/02", "/")   #=> 02
translate()
normalize-space()
string-length()
```

# Type conversion

```bash
string()
number()
boolean()
```
""",
                "Axes": """
# Using axes

```bash
//ul/li                       # ul > li
//ul/child::li                # ul > li (same)
//ul/following-sibling::li    # ul ~ li
//ul/descendant-or-self::li   # ul li
//ul/ancestor-or-self::li     # $('ul').closest('li')
```

Steps of an expression are separated by /, usually used to pick child nodes.
That’s not always true: you can specify a different “axis” with ::.

|      |      |          |      |
|------|------|----------|------|
| //   | ul   | /child:: | li   |
| Axis | Step | Axis     | Step |

# Child axis

```bash
# both the same
//ul/li/a
//child::ul/child::li/child::a
```

child:: is the default axis. This makes //a/b/c work.

```bash
# both the same
# this works because `child::li` is truthy, so the predicate succeeds
//ul[li]
//ul[child::li]
```

```bash
# both the same
//ul[count(li) > 2]
//ul[count(child::li) > 2]
```



# Descendant-or-self axis

```bash
# both the same
//div//h4
//div/descendant-or-self::h4
```

// is short for the descendant-or-self:: axis.

```bash
# both the same
//ul//[last()]
//ul/descendant-or-self::[last()]
```

# Other axes

| Axis               | Abbrev  | Notes                                        |
|--------------------|---------|----------------------------------------------|
| ancestor           |         |                                              |
| ancestor-or-self   |         |                                              |
| attribute          | @       |  @href is short for attribute::href          |
| child              |         |  div is short for child::div                 |
| descendant         |         |                                              |
| descendant-or-self | //      | // is short for /descendant-or-self::node()/ |
| namespace          |         |                                              |
| self               | .       |  . is short for self::node()                 |
| parent             | ..      | .. is short for parent::node()               |
| following          |         |                                              |
| following-sibling  |         |                                              |
| preceding          |         |                                              |
| preceding-sibling  |         |                                              |
| There are other axes you can use.

# Unions

//a | //span
Use | to join two expressions.
""",
                "More examples": """
# Examples

```bash
//*                 # all elements
count(//*)          # count all elements
(//h1)[1]/text()    # text of the first h1 heading
//li[span]          # find a <li> with an <span> inside it
                    # ...expands to //li[child::span]
//ul/li/..          # use .. to select a parent
```


# Find a parent

```bash
//section[h1[@id='section-name']]
```

Finds a &lt;section> that directly contains h1#section-name

```bash
//section[//h1[@id='section-name']]
```

Finds a &lt;section> that contains h1#section-name.
(Same as above, but uses descendant-or-self instead of child)

# Closest

```bash
./ancestor-or-self::[@class="box"]
```

Works like jQuery’s $().closest('.box').

# Attributes

```bash
//item[@price > 2*@discount]
```

Finds &lt;item> and check its attributes
""",
            },
        },
        "Cpp": {
            r"Типы данных": """
# Целые числа

|                    |                                                                                                                      |
|--------------------|----------------------------------------------------------------------------------------------------------------------|
| short int          | предназначен для хранения целых чисел.<br>Диапазон чисел от -32 768 до 32 767;                                       |
| unsigned short int | предназначен для хранения целых положительных чисел.<br>Диапазон чисел от 0 до 65 535;                               |
| int                | предназначен для хранения целых чисел.<br>Диапазон чисел от -2 147 483 648 до 2 147 483 647;                         |
| unsigned int       | предназначен для хранения целых положительных чисел.<br>Диапазон чисел от 0 до 4 294 967 295;                        |
| long int           | предназначен для хранения целых чисел.<br>Диапазон чисел от –9 223 372 036 854 775 808 до 9 223 372 036 854 775 807; |
| unsigned long int  | предназначен для хранения целых положительных чисел.<br>Диапазон чисел от 0 до 18 446 744 073 709 551 615.           |

Разница между типами заключается только в диапазоне чисел, который можно записать в переменную. 
Также не используйте большие типы данных по типу long int, если число маленькое, 
так как чем больше диапазон, тем больше памяти требуется компьютеру на конкретную переменную.

# Числа с точкой

|                      |                                                                                           |
|----------------------|-------------------------------------------------------------------------------------------|
| float                | Для создания чисел с плавающей точкой.<br>Диапазон чисел от от -3.4*1038 до 3.4*1038;     |
| double<br>long float | Для создания чисел с плавающей точкой.<br>Диапазон чисел от от ±4.9*10-324 до ±1.8*10308. |

# Прочие типы данных

|      |                                                                                                |
|------|------------------------------------------------------------------------------------------------|
| bool | Логический тип данных. Предназначен для записи истинного (true) или ложного (false) значения;  |
| char | Тип данных для работы с символами. Позволяет поместить в одинарных кавычках какой-либо символ. |

Для создания переменной необходимо указать тип данных и назвать её.
Также можно сразу же добавить к ней значение:

```cpp
int a = 0; // Добавление значения сразу
float c; // Создание переменной без значения
short int b, y = 342; // Создание нескольких переменных
```

Для вызова переменной вы можете обратиться к ней по имени.
Получение данных
Для получения данных от пользователя необходимо воспользоваться командой cin:

```cpp
cin >> some_value;
```

Таким образом введенные пользователем данные будут помещены в переменную с названием «some_value».

```cpp
char c = '1';    // символ
bool b = true;   // логическая переменная, принимает значения false и true
int i = 42;      // целое число (занимает, как правило, 4 байта)
short int i = 17;            // короткое целое (занимает 2 байта)
long li = 12321321312;       // длинное целое (как правило, 8 байт)
long long lli = 12321321312; // длинное целое (как правило, 16 байт)
float f = 2.71828;           // дробное число с плавающей запятой (4 байта)
double d = 3.141592;         // дробное число двойной точности (8 байт)
long double ld = 1e15;       // длинное дробное (как правило, 16 байт)
```

```cpp
std::cout << "char: " << sizeof(char) << "\\n";                 //  1
std::cout << "bool: " << sizeof(bool) << "\\n";                 //  1
std::cout << "short int: " << sizeof(short int) << "\\n";       //  2 (по стандарту >= 2)
std::cout << "int: " << sizeof(int) << "\\n";                   //  4 (по стандарту >= 2)
std::cout << "long int: " << sizeof(long int) << "\\n";         //  8 (по стандарту >= 4)
std::cout << "long long int: " << sizeof(long long) << "\\n";   //  8 (по стандарту >= 8)
std::cout << "float: " << sizeof(float) << "\\n";               //  4
std::cout << "double: " << sizeof(double) << "\\n";             //  8
std::cout << "long double: " << sizeof(long double) << "\\n";   // 16
```

Приведённые выше примеры вывода оператора sizeof верны для 64-битных архитектур, которые на сегодняшний день распространены повсеместно. 
Однако если бы мы скомпилировали и запустили такую программу на компьютере с 32-битной архитектурой, то получили бы другие результаты. 
Например, sizeof(long int) стал бы равен 4, в то время как на современных компьютерах мы получили бы 8. 
Также бывают встраиваемые системы, под которые тоже можно писать на С++. Там битность архитектуры может быть ещё меньше, чем 32.

В заголовочном файле cstdint стандартной библиотеки имеются целочисленные типы с фиксированным размером:

int8_t / uint8_t
int16_t / uint16_t
int32_t / uint32_t
int64_t / uint64_t
Число в имени типа означает количество бит, используемых для хранения в памяти. 
Например, int32_t содержит 32 бита (4 байта) и часто соответствует типу int. 
Если система не поддерживает какой-то тип, то программа с ним просто не скомпилируется.

Арифметические операции
Бинарные операции +, - и * работают для чисел стандартным образом. 
Результат операции деления /, применённой к целым числам, всегда округляется в сторону нуля. 
Таким образом, для положительных чисел операция / возвращает неполное частное. 
Остаток от деления целых чисел можно получить с помощью операции %.

```cpp
int main() {
    int a = 7, b = 3;
    int q = a / b;  // 2
    int r = a % b;  // 1
}
```

Если при делении нужно получить обычное частное, то один из аргументов нужно привести
к вещественному типу (например, double) с помощью оператора static_cast:

```cpp
int main() {
    int a = 6, b = 4;
    double q = static_cast<double>(a) / b;  // 1.5
}
```

Можно было бы написать чуть более кратко: double q = a * 1.0 / b;. 
Тогда преобразование аргументов произошло бы неявно.

Арифметические операции над символами,
а также сравнение символов друг с другом — это фактически операциинад их ASCII-кодами:

```cpp
#include <iostream>

int main() {
    char c = 'A';
    c += 25;  // увеличиваем ASCII-код символа на 25
    std::cout << c << "\\n";  // Z
}
```
""",
            "if-else,switch-case": r"""
&& (И)
|| (ИЛИ)
! (НЕ)

Если необходимо проверить несколько условий в одном операторе, 
то можно воспользоваться логическим «и» или же логическим «или»:

```cpp
if (a != b && a > b) {
    // Код будет выполнен, если и первое, и второе условие
    // окажутся верными
}

if (a < b || a == b) {
    // Код будет выполнен, если или первое, или второе условие
    // окажется верным
}
```

Тернарная операция
Это сокращенная форма if else. Записывается следующим образом:

```cpp
int x = 90, a = 8;
int res = x < a ? (x + a) : (x - a);
cout << res << endl;
```

Проверяем: если “x” будет меньше “а”, то в переменную res устанавливаем их сумму, иначе – их разницу. 

Конструкция switch
Конструкция case обладает более удобным форматом для проверки множественных условий на совпадение значения. 
В конструкцию записывается переменная, что проверяется, а также значения на которые происходит проверка.

Пример оператора:

```cpp
int x = 23;
switch (x) { // Проверяем переменную x
    case 1: // Если переменная будет равна 1, то здесь сработает код
        // Может быть множество строк, а не только одна
        cout << "Переменная равна 1" << endl;
        break; // Указываем конец для кода для этой проверки
    case 56: // Если переменная будет равна 56, то здесь сработает код
        // Может быть множество строк, а не только одна
        cout << "Переменная равна 56" << endl;
        break; // Указываем конец для кода для этой проверки
        // По аналогии таких проверок может быть множество
        // Также можно добавить проверку, которая сработает в случае
        // если все остальные проверки не сработают
    default:
        cout << "Что-то другое" << endl;
        break; // Можно и не ставить, так как это последние условие
}
```


Операторы && и || ведут себя лениво: если первого аргумента уже достаточно для ответа, то второй аргумент вычисляться не будет. 
Например, в выражении condition1 && condition2 второе условие не вычисляется, если первое ложно.



Сравнение чисел с плавающей точкой
Рассмотрим программу, которая проверяет равенство 0.1 + 0.2 == 0.3:

```cpp
#include <iostream>

int main() {
    double x = 0.1, y = 0.2;
    if (x + y == 0.3) {
        std::cout << "EQUAL ";
    } else {
        std::cout << "NOT EQUAL ";
    }

    std::cout << x + y << "\n";
}
```

Логично было бы предположить, что программа выведет EQUAL 0.3, потому что . 
Однако программа напечатает NOT EQUAL 0.3. 
Данная «ошибка вычисления» встречается в большинстве современных языков программирования и обусловлена погрешностью представления этих чисел. 
Если повысить число знаков дробной части в выводе, мы увидим, что 0.1 + 0.2 == 0.30000000000000004.

Поскольку операции над числами с плавающей точкой могут содержать погрешность, обычное сравнение через == некорректно. 
Поэтому правильнее сравнивать модуль разности величин с некой допустимой для нас погрешностью. 
Модуль дробного числа можно получить с помощью функции std::abs из заголовочного файла cmath. 
Исходную программу можно было бы переписать так:

```cpp
#include <cmath>
#include <iostream>

int main() {
    double delta = 0.000001;

    double x = 0.1, y = 0.2;
    double sum = x + y;

    if (std::abs(sum - 0.3) < delta) {
        std::cout << "EQUAL ";
    } else {
        std::cout << "NOT EQUAL ";
    }

    std::cout << sum << "\n";
}
// Теперь программа выведет EQUAL 0.3.
```
""",
            "rand": """Случайные числа
Для генерации случайных чисел необходимо использовать метод rand(). Чтобы создать случайное число в диапазоне от 1 до 20 потребуется следующий код:

```cpp
int num = 1 + rand() % 20;
```

При использовании такого кода число будет генерироваться случайны образом, но всегда будет неизменным. 
Чтобы каждый раз при запуске программы выводилось новое случайное число необходимо использовать библиотеку: 
#include <time.h>. 
После её подключения в функции main пропишите команду: srand(time(NULL));


Пример реализации:

```cpp
#include <iostream>
#include <time.h>
using namespace std; 

int main() {
    setlocale(LC_ALL, "Russian"); // Русская локализация консоли
    srand(time(NULL)); // Генерирует случайное число, используя текущую дату как параметр
    cout << 1 + rand() % 20 << endl;
    cout << 1 + rand() % 20 << endl;

    cin.get();
    return 0; 
}
```

Функции для строк
Для работы со строками необходимо подключить библиотеку #include <string>. 


Для получения целой строки от пользователя используйте функцию «getline(cin, value)». 
В функции параметр value является названием переменной, в которую будет записано значение от пользователя.
""",
            "Циклы": """Цикл For
В цикле for все условия записываются в одном месте, что очень удобно во многих случаях. 
Стандартная запись такого цикла выглядит следующим образом:

```cpp
for (int i = 0; i < 10; i++)
    cout << i << endl;
```

В объявлении цикла записывается следующее: переменная цикла, её начальное значение и диапазон. 
В примере выше будут выведены числа от 0 до 10.

Если в теле цикла всего одна строка кода, то фигурные скобки можно пропустить и не записывать их.

Цикл While
Суть цикла while не особо отличается от цикла for. Единственное отличие заключается в способе записи цикла. 
В while необходимо прописать лишь условие, а все остальные параметры записываются вне цикла:

```cpp
int i = 1; // Создание переменной
while (i <= 10) { // Здесь только условие
    cout << i << endl;
    i++; // Увеличение переменной
}
```

Цикл Do While
Цикл схож с циклом while по форме написания, но при этом работает немного по-другому. 
Цикл do..while будет выполнен один раз сто процентов, а дальше проверит условие и если оно верно, то цикл будет выполняться дальше:

```cpp
int x = 13;
do {
    x--;
    cout << i << endl;
} while (x > 10);
```

Как видно из примера, цикл изначально неверный, но это не мешает ему сработать один раз.
Операторы для работы в циклах
Существует два основных оператора для работы в циклах:

Оператор break - служит для выхода из цикла полностью;
Оператор continue - пропускает лишь одну итерацию и не выходит из цикла.
""",
            "try-catch": """Реализации конструкции try catch
Для добавления отслеживания ошибок можно прописать следующий код:

```cpp
try { // В блоке try мы пытаемся выполнить какой-либо код
    if (variable == 0) // Проверяем делитель на ноль
        throw 277; // Запускаем исключение и передаем в него параметр

    cout << something / variable << endl; 
} catch(int i) { // Здесь отлавливаем переданную ошибку
    cout << "Нам очень повезло!" << endl;
    cout << "Нам удалось избежать ошибки с индексом " << i << " - на 0 делить нельзя!";
}
```

В коде выше представлен очень простой пример использования исключений. 
Не обращайте внимание на его простоту, так как главное это рассмотреть общую конструкцию блока try catch.

При использовании такой конструкции, какая бы ошибка не получилась в ходе программы 
сама программа работать не перестанет и пользователь не получить плохой опыт в её использовании.

Если необходимо отследить несколько классов с ошибками, то можно добавить несколько 
блоков catch. Все они добавляются друг под другом точно также как в условных операторах. 
""",
            "Массивы": """Массивы позволяют хранить большой объем информации в одном месте. В языке C++ можно найти несколько основных типов массивов. 

Одномерный массив
Чтобы создать массив необходимо указать тип данных, прописать название и поставить квадратные скобки. 
Это очень схоже с созданием обычных переменных, но здесь после названию идут ещё квадратные скобки.

В массивах отсчет начинается с 0, поэтому первый элемент по индексу будет равен 0, второй - 1 и так далее.

Примеры создания массива:

```cpp
char stroka[2]; // Создание пустого массива
int[] numbers; // Будет считаться ошибкой

int nums[4];
nums[0] = 1; // Добавление элементов в массив из 4 элементов

int nums2[] = { 1, 2, 3, 5 }; // Присвоение всех значений сразу
```

Работать с элементами массива можно точно как с переменными. Мы можем их выводить или же устанавливать для них новые значения.

Многомерный массив
Многомерный массив - это массив, в котором каждый элемент является другим массивом. 
На практике очень редко используются массивы с более чем третим уровнем вложенности. 
То есть массивы, в которых все элементы являются другими массивами 
и в котором все элементы также другие массивы встречаются очень и очень редко на практике.



Мы не будем изучать подобные массивы, так как принцип их построения 
точно такой же как при работе с двумерными массивами.

Для создания двумерных массивов необходимо использовать двойные квадратные скобки после названия. 
Выглядит такой массив как матрица, а записывается следующим образом:

```cpp
int x[3][3] = { { 0, 34, 2 }, { 3, 4, 5 } };
cout << x[0][1]; // 34

// Можно их сразу не присваивать
char symbols[5][2];
symbols [0][1] = 'A';
```

Мы видим, что элементы первого массива являются другими массивами. 
Чтобы выбрать какой-либо объект используйте ту же структуру что и для одномерных массивов, 
вот только теперь указывайте индекс как первого массива, так и второго:

```cpp
x[0][1] = 1; // Вместо 34 теперь будет 1
```
""",
            "Указатели": """Каждая переменная или объект хранит данные в определенной ячейке в памяти компьютера. 
Каждый раз, создавая новую переменную, мы создаем новую ячейку в памяти, с новым значением для неё. 
Чем больше ячеек, тем больше компьютерной памяти будет занято.


Адрес в памяти компьютера это число, к которому мы можем получить доступ. 
Указатель - это тот же адрес в памяти, по которому мы получаем переменную и по итогу её значение.

Чтобы работать с указателями необходимо воспользоваться двумя специальными символами: & и *.

```cpp
int t = 237; // Простая переменная
int *p; // Создание указателя, который принимает лишь адрес другой переменной
p = &t; // Устанавливаем адрес нашей первой переменной
```

Переменные t и p будут равны числу 237, так как оба ссылаются на одну ячейку. 
Сам же компьютер на вычислении обеих переменных потратит меньше усилий, ведь обе переменные ссылаются на одно и то же.

Ссылки в C++
Ссылки и указатели схожи между собой, так как оба в качестве значения имеют лишь адрес некого объекта.

Указатель хранит адрес ячейки и если мы захотим изменить значение этой ячейки, то нам придется выполнить операцию «разыменования»:

```cpp
float some = 391; // Простая переменная
float *u = &some; // Указатель на переменную
*u = 98; // Изменение значения переменной
```

В ссылках такого понятия нет, так как меняя ссылку вы автоматически меняете и переменную. 
Ссылки напрямую ссылаются к переменной, поэтому их синтаксис проще:

```cpp
char symbol = 'A'; // Простая переменная
char &ref = symbol; // Создание ссылки на переменную
// Поскольку мы ссылаемся на переменную, то можем её использовать
// как отдельно взятую переменную
cout << ref << endl; // Вывод символа "А"
ref = 'C'; // Изменение на символ "C"
```

Использование ссылок и указателей оправдано в случае передачи данных в функции или же в объекты. 
Также данные технологии отлично подойдут для передачи большого объема данных в ходе программы.
""",
            "Динамические массивы": """Динамическое выделение памяти очень удобно, так как за счёт выделения 
памяти мы резервируем место под данные в каком-либо объекте.

В C++ за выделение и удаление памяти отвечают операторы new и delete соответсвенно. 
Они служат для создания не только динамических массивов, но также для выделения памяти под объекты и даже простые переменные.

```cpp
// Операция выделения памяти (new)
float *val = new float; // Можно выделять память под любые типы данных
// здесь val это указатель на участок памяти типа float 
// new служит операцией выделения этой памяти
// delete необходим для высвобождения памяти
delete val;
```

Динамический массив использует ту же конструкцию. Здесь также применяются операторы new и delete:

```cpp
char *symbols = new char [25]; // выделение памяти под массив
// Также необходимо освободить память,
// когда массив уже не нужен
delete [] symbols;
```
""",
            "Символы и строки": """Создание строкового объекта было невозможным в языке Си. 
Для создании строки использовался массив символов - char arr[]. 
В языке C++ все было упрощено и для создания строк появился новый отдельный объект. 
Вместе с объектом появились и новые функции для обработки строк. 

Вместе с тем не стоит забывать, что строки до сих пор являются массивом символов, 
а это означает, что с каждым символом можно работать по отдельности, будто это элемент одного общего массива.

Работа со строками не отличается от работы с массивами. 
Вот только для записи целой строки мы можем воспользоваться специальной функцией gets(). 

С недавних пор более предпочтительно использовать метод gets_s(), что более защищен и позволяет выполнить получения строки от пользователя. 

Язык C++ спокойно может работать с кириллицей, при условие что вы подключите обработку символов кириллицы. 
Для корректной работы необходимо подключить библиотеку «clocale», а также в метода main воспользоваться функцией setlocale:

```cpp
#include <clocale>

using namespace std; 

int main() {
    // Установка поддержки кириллицы
    setlocale(LC_CTYPE, "rus");

    return 0; 
}
```

python

```python
x = "2"
y = "4"
z = int(x + y + y)
print(z+6)  # 250
```

C++

```cpp
#include <iostream>
#include <string>
using namespace std;

int main() {
    string x = "2";
    string y = "4";
    int z = stoi(x + y + y);
    cout << z + 6 << endl; // 250
    return 0;
}
```

stoi() - это функция стандартной библиотеки C++, которая используется для преобразования строки 
(например, содержащей текстовое представление числа) в целое число (int). 
Функция std::stoi() возвращает полученное целое число.

python

```python
x = 2
y = 4
z = str(x + y + y)
print(f"f({z})")  # f(10)
```

С++

```cpp
#include <iostream>
#include <string>
using namespace std;

int main() {
    int x = 2;
    int y = 4;
    string z = to_string(x + y + y);
    cout << "f(" << z << ")" << endl; // f(10)
    return 0;
}
```
""",
            "Структуры данных": """Структуры служат для описания небольшого объекта, у которого нет большого количества переменных и функций.

Использование структур удобно, так как они имеют ряд преимуществ:
занимают меньше памяти, поэтому использование их облегчает нагрузку на процессор;
имеют простой синтаксис;
имеют лишь переменные, функции и конструкторы;
на их основе можно создавать объекты.

Получается, что благодаря структурам, можно с легкостью создавать небольшие объекты с маленьким количеством информации. 
Такие объекты могут описывать реальные объекты из жизни: объект книги, объект автомобиль, объект дерево и тому подобное.

Для создания структуры используйте синтаксис: struct NAME {}. 
На основе одной структуры можно создавать неограниченное количество объектов, 
которые будут иметь одинаковые названия переменных и функций, но при этом значения у всех объектов будут разными.
""",
            "Перечисления (Enum)": """За счёт перечислений вы можете указать список элементов для выбора и далее в программе можете пользоваться данным списком.
Перечисления служат для удобства программистов, так как особой функциональности они не несут. 
Представим, что у вас большая программа со множеством массивов данных, которые человек попросту не способен запомнить. 
По причине неспособности все запомнить вы можете создать перечисление, что будет хранить список со всеми доступными значениями и названиями.

Создав такой список вы можете обращаться к нему и выбирать подходящий для вас вариант.

Для создания перечислений используйте пропишите слово enum, назовите его и укажите инициализацию всех вариантов.


Обьяснение от ChatGPT:

Перечисления (Enum) - это специальный тип данных в C++, который позволяет определять именованные константы. 
Это полезно, когда вы хотите указать набор допустимых значений для переменной.

Определение перечисления выглядит так:

```cpp
enum Color {
  RED,
  GREEN,
  BLUE
};
```

В этом примере мы определили перечисление Color, которое содержит три константы: RED, GREEN и BLUE. 
Эти константы могут использоваться в качестве значений для переменных типа Color.

По умолчанию каждая константа присваивается значение равным ее позиции в перечислении, начиная с нуля. 
Однако, вы также можете явно указать значение для каждой константы:

```cpp
enum Color {
  RED = 1,
  GREEN = 2,
  BLUE = 4
};
```

В этом примере мы явно указали значение для каждой константы в перечислении.
""",
            "Работа с файлами": """Многие языки программирования предоставляют классы для работы с файлами и директориями проекта. 
Язык C++ обладает множеством классов для записи и чтения данных из файлов.

Работа с файлами
При работе с файлами всегда необходимо помнить две вещи:

Перед началом работы с файлом его необходимо открыть;
После завершения работы с файлом его необходимо закрыть.

Если файл не открыт или же неверно открыт, то вы не можете полноценно работать с его содержимым. 

С закрытием все проще, но и коварнее. Если вы не закроете файл, то программа будет работать верно, 
тем не менее, чем больше будет открытых файлов, тем больше программа будет перегружена и в какой-то момент она просто зависнет или выключиться.

Исключения и файлы
Поскольку не всегда известно будет ли файл в проекте или на компьютере пользователя, 
то всегда лучше открывать файлы за счёт использования исключений. 
Выполняйте открытие файлов в блоке try catch и тем самым вы обезопасите себя от любых непредвиденных обстоятельств.

Запись данных в файл
При записи данных в файл его изначально необходимо открыть. Для этого в языке C++ используется класс ofstream:

```cpp
// Создание/открытие файла "examples.txt"
ofstream itproger_file("examples.txt");
// Можно было использовать метод open
// ofstream itproger_file;
// itproger_file.open("examples.txt");
// но первая запись короче, поэтому стоит использовать её
if (itproger_file.is_open()) { // Проверяем открыт ли файл
    itproger_file << "Simple text"; // Записываем текст в файл
    itproger_file.close(); // Всегда необходимо закрывать файл
} else // Если файл не удалось открыть, тогда выдаем ошибку
    cout << "Error!" << endl;
```

Таким образом мы можем открыть файл и поместить в него любую информацию.

При открытии файла можно указать режим открытия. Существуют несколько режимов и все они представлены на фото ниже:

Константа         Описание
ios_base::in      открыть файл для чтения
ios base::out     открыть файл для записи
ios base::ate     при открытии переместить указатель в конец файла
ios_base::app     открыть файл для записи в конец файла
ios_base::trunc   удалить содержимое файла, если он существует
ios_base::binary  открытие файла в двоичном режиме

Режим необходимо прописывать в качестве второго параметра при открытии файла:

```cpp
#include <iostream>
#include <fstream>

using namespace std; 

int main() {
    // Открываем файл для записи в него текста
    ofstream file("test.txt", ios_base::out);
    if (file.is_open()) { // Проверяем открыт ли сам файл
        file << "Simple world"; // Записываем текст в начало файла
        textFile.close(); // Закрываем файл
    }

    cin.get();
    return 0; 
}
```

Чтение данных из файла
Для чтения данных файл необходимо также изначально открыть и в конце закрыть. 
Чтобы прочесть содержимое файла используется класс ifstream:

```cpp
#include <iostream>
#include <fstream>

using namespace std; 

int main() {
    // здесь будет храниться промежуточный текст,
    // который мы будем считывать из файла
    char temp[100];
    ifstream some_file("test.txt"); // открываем файл для чтения

    // считываем лишь первое слово и помещаем в переменную temp
    some_file >> temp;
    cout << temp << endl; // выводим эту переменную

    // Считываем определенное количество символов - 100
    // и записываем их в нашу переменную
    some_file.getline(temp, 100);
    some_file.close(); // Закрываем файл
    cout << temp << endl; // Отображаем переменную temp

    cin.get();
    return 0; 
}
```
""",
            "Функции": """Функции можно назвать небольшими подпрограммами, куда можно вынести повторяющийся код и обращаться к нему, когда это будет нужно. 
Функции значительно облегчают построение программ, так как нам не надо копировать 
однотипный код множество раз, а можно просто воспользоваться одной общей функцией.

Многие путают функции и методы и не понимают отличий между ними. 
На самом деле отличий нет, так как что методы, что функции являются одним и тем же. 
Функции что записаны вне классов называют функциями, а функции что записаны внутри классов называются методами. 
Поскольку C++ это не объектно ориентированный язык, то лучше говорить функции, хотя это не имеет никакого значения.

Точно такая же ситуация обстоит с переменным. В классах переменные называются полями, а вне классов - переменными.

Для создания функций необходимо указать возвращаемый тип данных, указать название и параметры.
В случае когда функция ничего не возвращает, то указывается тип данных void.

Все функции необходимо записывать перед созданием функции main().
В таком случае при вызове функций у вас не будет появляются ошибок.

Также функции можно лишь объявить перед функцией «main», а после неё прописать.

Создание функции
На основе всех данных наша функция будет выглядеть следующим образом

```cpp
void test () {
    cout << "Вывод чего-либо в консоль" << endl;
}
```

Функция выше не принимает никаких параметров и ничего не возвращает.
Она просто пишет слово в консоль. Давайте разнообразим функцию и добавим параметр

```cpp
void test (char symbol) {
    cout << symbol << endl;
}
```

Теперь функция принимает параметр, который будет отображен в консоли.

Также было бы логично прописать описание функции перед функцией «main»:

```cpp
void test (char symbol);
```

Если функция должна что-либо вернуть, то прописываем тип данных который будет возвращен.
Для возвращения данных используем ключевое слово return:

```cpp
double test (double some_number) {
    some_number *= 2;
    return some_number;
}
```
""",
            "Перегрузка функций": """С перегрузкой методов мы уже ни раз сталкивались, хотя ни разу их не создавали вручную. 
Пришло время это исправить.

Что такое перегрузка методов?
За счёт перегрузки методов мы можем создать множество методов, что будут принимать разное количество 
параметров или разный тип данных и при этом будут иметь одно и то же имя.

Отличным примером является функция «rand». В неё мы можем передавать различные типы данных, 
но при этом выполнение функции происходит без каких-либо ошибок. 
Так происходит из-за того, что в функция «rand» имеет множество перегрузок на разные типы данных. 

Как создать перегрузку?
Чтобы создать перегрузку необходимо прописать метод с тем же именем, 
но при этом указать либо другое количество принимаемых параметров, либо другие типы данных для принимаемых параметров.

Пример:

```cpp
void getInfo(char some) {
    cout << some << "!";
}

int getInfo(int a, int b) {
    return a + b;
}
```

Теперь при вызове метода компилятор будет понимать какие параметры были переданы и в зависимости от этого будут вызываться разные методы.
""",
            "Математические операции": """функции: pow(), ceil(), abs(), floor(), sin(), cos() идр
В языке C++ существует библиотека cmath, которая позволяет использовать множество встроенных математических функций.

После подключения библиотеки вы можете использовать функции для получения синуса, косинуса, квадратного корня и многого другого.

Помимо сложных вычислений в языке C++ можно выполнять все математические операции. Это такие операции, как:
вычитание - z = y - x;
сложение - z = y + x;
умножение - z = y * x;
деление - z = y / x (на ноль делить нельзя);
остаток при делении - z = y % x;
Если операция проходит над одной и той же переменной, то можно запись сократить:

z = z + 20;
z += 20; // Эта запись аналогична той, что находиться выше
Если нам необходимо увеличить или уменьшить число на 1, то мы можем прописать ++ и -- соответсвенно:

z = 10;
z += 1;
z++; // Аналогично тому, что прописано выше
""",
            "(Введение в ООП) Классы и объекты": """На начальном этапе ООП – это тёмный лес, в котором многое непонятно и слишком усложнено. 
На самом деле всё вовсе не так. Предлагаем абстрагироваться от специфических (непонятных) определений и познакомиться с ООП простыми словами. 

ООП простыми словами
Поскольку на примере все усвоить гораздо проще, то давайте за пример возьмем робота, которого постараемся описать за счёт классов в ООП.

Класс в случае с роботом – это его чертёж. Экземпляром класса (объектом) называет целый робот, который создан точно по чертежу.

Наследование – это добавление полезных опций к чертежу робота. 
К примеру, берем стандартный чертёж робота и дорисуем к нему лазеры, крылья и броню. 
Все эти дорисовки мы сделаем в классе наследнике, основной функционал которого взят из родительского класса.

Полиморфизм – это общий функционал для всех роботов и не важно что каждый робот может очень сильно отличаться друг от друга. 
К примеру, в главном классе мы указываем возможность передвижения для всех последующих роботов. 
Далее в классе наследнике мы можем дополнительно указать возможность левитации для робота, в другом же классе укажем возможность передвижения по воде и так далее. 
Получается, что есть общий функционал что записан в главном чертеже, но его можно переписать для каждого последующего робота (для каждого наследника).

А инкапсуляция является для нас бронёй, защищающей робота. 
Под пластырем брони находятся уязвимые элементы, вроде проводов и микросхем. После прикрытия брешей с помощью брони (protected или private), 
робот полностью защищён от внешних вмешательств. По сути, мы делаем доступ ко всем полям лишь за счёт методов, тем самым прямой доступ к полю будет закрыт.

У всех классов методы могут отличаться, как и поля с конструкторами. 
Каждый класс позволяет создавать любое количество разных объектов, все из них имеют собственные характеристики.

Создание классов
Для создания класса необходимо прописать ключевое слово class и далее название для класса. 
Общепринято начинать названия классов с буквы в верхнем регистре, но если этого не сделать, то ошибки не будет.

В любом классе можно создавать поля (переменные), методы (функции), а также конструкторы.

Создав новый класс и поместив туда какую-либо информацию мы можем создавать на основе него новые объекты. 
Объекты будут иметь доступ ко всем характеристикам класса, которые отмечены модификатором public.

Существует три модификатора доступа:

public - данные будут видны повсюду, как в классе, так и вне его;
protected - данные будут видны только в классе, где они были созданы, а также в классах наследниках;
private - данные будут видны только в классе, где они были созданы.
Пример простого класса приведен ниже:

```cpp
class Book {
public:
    int pages;
    char name;
    float weight;

    void getInfoBook () {
        cout << "В книге " << name << " находиться " << pages << " страниц. " << endl;
        cout << "При этом она весит " << weight << endl;
    } 
};
```

На основе такого класса мы можем создать множество объектов. 
Каждый объект в данном случае будет представлять из себя конкретную книжку. 
Для каждого объекта мы можем указать уникальные данные: количество страниц, название книги и её вес.

Чтобы создать объект нам потребуется следующий код:

```cpp
Book sherlock_holms; // Создание объекта
sherlock_holms.getInfoBook(); // Вызов метода класса
Такой код можно прописать и в одной строке кода. Мы для наглядности разбили код в две строки.
```

Чтобы брать данные из класса через объект необходимо ставить точку и указывать имя переменной или функции, которую мы хотим взять.
""",
            "Конструкторы и деструкторы": """Конструктор класса очень удобен и по своему виду схож с обыкновенными функциями. 
За счёт конструктора мы можем установить значения для объекта сразу при его создании.

Конструктор должен иметь одинаковое название с классом.

```cpp
class Book {
private:
    int pages;
    float weight;
public: 
    char name;

    void getInfoBook () {
        cout << "В книге " << name << " находиться " << pages << " страниц. " << endl;
        cout << "При этом она весит " << weight << endl;
    } 

    Book (int _pages, float _weight) {
        pages = _pages;
        weight = _weight;
    }

    Book (int _pages, float _weight, char _name) {
        pages = _pages;
        weight = _weight;
        name = _name;
    }
};
```

В одном классе может быть сразу несколько конструкторов. 
Создав несколько конструкторов мы можем передавать разное количество параметров при создании объекта.

Компилятор сам определяет какой конструктор необходимо использовать в зависимости от передаваемых параметров и их типов данных. 

В коде выше переменные идут с модификатором доступа private. 
Дело в том, что все переменные лучше делать либо private, либо protected. 
Доступ к переменным должен осуществляться только за счёт методов и конструкторов. Доступ к полям напрямую должен быть закрыт.

Дополнительно создадим два объекта и выведем информацию:

```cpp
int main() {
    Book sherlock_holms(460, 1.7f); // Используем 1 конструктор
    sherlock_holms.name = 'S'; // Устанавливаем вручную значение для name
    sherlock_holms.getInfoBook ();

    Book green_mile(750, 2.8f, 'G'); // Используем второй конструктор
    green_mile.getInfoBook ();

    return 0;
}
```

Поскольку переменная name имеет public модификатор доступа, то мы можем ссылаться к ней отдельно. 
Лучше так не делать и для неё тоже установить модификатор private.

Также конструктор может не принимать параметров. 
В таком случае при создании объекта ничего не надо дополнительно передавать.

Деструкторы
Деструкторы работают в обратную сторону от конструкторов. 
Конструктор вызывается при создании объекта, а деструктор при удалении.

Пример создания деструктора:

```cpp
class Some {
public:
    ~Some () {
        cout << "Работа с объектом завершена.";
    }
};
```

Исходный код

Конструкторы и деструкторы

```cpp
using namespace std;

class Auto {
private:
    int year, month, day;
public:
    Auto () {
        year = 2000;
        month = 12;
        day = 31;

        get();
        cout << endl;
    }

    Auto (int date_year, int date_month, int date_day) {
        year = date_year;
        month = date_month;
        day = date_day;

        get();
        cout << endl;
    }

    void message () {
        cout << "Class is working!" << endl;
    }

    void set (int date_year, int date_month, int date_day) {
        year = date_year;
        month = date_month;
        day = date_day;
    }

    void get () {
        cout << "Year of this auto is - " << year << ", month is - " << month << ", day is - " << day << endl;
    }

    ~Auto () {
        cout << "Class is not working" << endl;
    }
};

int main(int argc, const char * argv[]) {

    Auto shkoda (2015, 2, 13);
    shkoda.message();
    shkoda.set(2005, 11, 23);
    shkoda.get();

    Auto bmw;
    bmw.set(2012, 1, 11);
    bmw.get();

    cin.get();
    return 0;
}
```
""",
            "20 Дружественные функции": """Дружественная функция - это функция, что имеет доступ к полям и методам класса, при этом сама функция может быть создана вне класса. 

Для создания дружественной функции необходимо прописать обыкновенную функцию вне классов 
и далее для классов что будут работать с этой функцией объявить её, указав имя, а также поставив слово friend перед типом данных функции.

После создания такой функции вы сможете через неё управлять всеми данными во всех классах, 
что указали функции её как дружественную. Доступ будет даже к тем полям, у которых модификатор доступа стоит как private или protected.
""",
            "Дружественные классы": """Дружественные классы по своей работе схожи с дружественными функциями. 
Единственное отличие заключается в объединение не просто функций, а целых классов.

Благодаря дружественному свойству мы можем указать несколько классов, что будут связаны между собой. 
Это позволит брать данные через объект сразу из нескольких классов.

За счёт этого мы может точно описать логику для различных персонажей в игре или для окон в приложении. 
Все они могут быть записаны в разных классах, но при этом каждый сможет иметь доступ друг к другу.

Пример создания дружественного класса:

```cpp
class Auto;
class Motorcycle {
    friend class Auto;
private: 
    bool isStillWorking = true;
};

class Auto {
public:
    void CrashDTP(Auto &moto) {
        moto.isStillWorking = false;
        cout << "Motorcycle is currently not working!";
    }
};
```

Из примера видно, что для дружественных классов используется схожая структура что для дружественных функций.

Перед объявление класса Motorcycle указывается существование класса Auto: class Auto. 
Далее мы делаем класс Auto дружественным и для этого используем ключевое слово friend.
""",
            "Указатель this": """За счёт указателя this мы можем точно указать откуда берутся данные. 
При работе с данными внутри одного класса часто необходимо обратить к полям или методом самого класса. 
Чтобы не возникало конфликтов имен можно использовать указать «this».

Пример работы:

```cpp
class Some {
private
    int test;

public:
    void set (int test) {
        this->test = test;
    }
};
```

При использовании указателя данный код не вызовит ошибок и все обработается корректно.


Обьяснение от ChatGPT:

this - это указатель на текущий объект внутри метода класса. 
Он используется для обращения к полям и методам текущего объекта.

Например, если у вас есть класс Person, и вы хотите использовать поле name текущего 
объекта внутри метода printName, то вы можете сделать это следующим образом:

```cpp
class Person {
  public:
    string name;
    void printName() {
      cout << this->name << endl;
    }
};
```

В этом примере this указывает на текущий объект класса Person, 
и мы можем использовать его, чтобы достучаться до поля name и вывести его на экран.
""",
            "Наследование классов (ООП)": """Наследование является одним из ключевых понятий ООП. 
За счёт наследования можно создать один общий класс (класс родитель) и создать множество других классов (классы наследники), 
что будут наследовать все поля, методы и конструкторы из главного класса.

За чем использовать наследование?
Предположим что у нас есть один большой класс «Транспорт». В классе описываются базовые характеристики для всех транспортных средств:

поля: скорость, вес, запас хода и тому подобное;
методы: получение информации из полей, установка новых значений;
конструктор: пустой и по установке всех полей.


На основе класса мы спокойно можем создать объект легковой машины, объект грузовика, объект самолета и так далее. 
У всех объектов будут одинаковые характеристики и методы. 

Мы явно понимаем, что у объекта машина и самолёт будут разные поля и характеристики. Как можно поступить:

Можно создать два отдельных класса: «Car» и «Airplane». 
В каждом классе будут все методы, поля и конструкторы повторно переписанные из класса «Транспорт», 
а также будут новые методы, что важны только для конкретного класса;
Можно создать два класса наследника: «Car» и «Airplane». 
Оба класса будут наследовать всё от класса «Транспорт» и при этом будут содержать свои дополнительные функции. 
Таким образом повторения кода не будет и код станет меньше и чище.


Создание классов наследников
Для создания класса наследника требуется создать класс и указать наследование от главного класса.

Пример класса наследника:

```cpp
class Transport {
protected:
    float speed;
};

class Auto : public Transport {
private:
    int wheels;

public:
    Auto (float speed, int wheels) {
        this->speed = speed;
        this->wheels = wheels;
        cout << "Speed is: " << speed << ", model is - " << wheels << endl;
    }
};

int main() {
    Auto bmw(301.2, 4);
    Auto mercedes(270, 4);

    return 0;
}
```

Как вы можете заметить, у нас есть одна общая переменная speed. 
Поскольку модификатор доступа у неё protected, то доступ к переменной мы имеем 
внутри класса Transport, а также внутри всех классов наследников.

Для создания наследования мы прописали ключевое слово : после имени класса и указали какой класс будет родительским.
""",
            "Шаблоны функций (template)": """Шаблоны функций, а также шаблоны классов в языке C++ это мощные технологии, 
что позволяют создавать шаблонные конструкции и далее при передачи данных передавать как значения, так и типы данных.

Для создания шаблонной функции необходимо использовать ключевое слово template, 
а также в угловых скобках необходимо указывать принимаемый тип данных. 
Можно принимать один или несколько типов данных. 

Пример создания шаблонной функции:
```cpp
template <typename Type1> // Указываем что это шаблон функции
// Принимаем параметр value и его тип данных мы получим
// также в качестве передаваемого параметра - Type1
void funct (Type1 *value) {
    cout << value; // Просто выводим это значение
}
```

Для передачи нескольких типов данных стоит прописать следующее:

```cpp
// Здесь мы получаем сразу два типа данных
template <typename Type1, typename Type2>
void funct (Type1 *value, Type2 *newValue) {
    // Мы можем использовать передаваемые типы в самой функции
    Type1 someNew;
    cout << newValue; // Просто выводим значение
}
```

Для вызова шаблонной функции пропишите следующее:

```cpp
// Вызов функции с одним параметром
funct<double>(value);
// Вызов с несколькими параметрами
funct<char, double>(value, oneMoreValue);
```

Шаблоны функций

```cpp
#include <iostream>

using namespace std;

template <typename T1, typename T2>
T2 printArr (const T1 * array, int i) {
    int count = 0;
    for (int j = 0; j < i; j++) {
        cout << array[j] << " ";
        count++;
    }
    cout << endl;
    return count;
}

int main(int argc, const char * argv[]) {

    const int iSize = 3, fSize = 2, dSize = 3, cSize = 5;

    int i_arr[iSize] = {23, 45, 78};
    float f_arr[fSize] = {12.2, 67.5};
    double d_arr[dSize] = {3.345, 7.567, 9.023};
    char c_arr[cSize] = {"HI!!"};

    cout << "Массив с типом данных int: ";
    cout << "Количество элементов: " << printArr<int, int>(i_arr, iSize) << endl;
    cout << "Массив с типом данных float: ";
    cout << "Количество элементов: " << printArr<float, int>(f_arr, fSize) << endl;
    cout << "Массив с типом данных double: ";
    cout << "Количество элементов: " << printArr<double, int>(d_arr, dSize) << endl;
    cout << "Массив с типом данных char: ";
    cout << "Количество элементов: " << printArr<char, int>(c_arr, cSize) << endl;

    cin.get();
    return 0;
}
```



Обьяснение от ChatGPT:

Шаблоны функций и классов в C++ - это механизм, который позволяет создавать 
универсальные классы и функции, которые могут работать с разными типами данных. 
Вместо того, чтобы создавать отдельную функцию или класс для каждого типа данных, 
вы можете определить шаблон, который может использоваться с разными типами данных.

Определение шаблона функции выглядит так:

```cpp
template <typename T>
T max(T a, T b) {
  return (a > b) ? a : b;
}
```

В этом примере T является параметром шаблона, который может быть любым типом данных. 
Когда вы вызываете функцию max с разными типами данных, компилятор создает специализированную 
версию функции для каждого типа данных, с которым вы вызываете эту функцию.
""",
            "Шаблоны классов": """Шаблоны классов работают по тому же принципу что и шаблоны функций. 
Разница заключается в том, что шаблоны классов описывают шаблонную структура класса, а не функции.

Для создания шаблона класса используйте ключевое слово template. Пример реализации шаблонного класса

```cpp
template <class SomeType>
class Test {
private:
    SomeType value;
public: 
    SomeType setElement(SomeType value) {
        this->value = value;
        return value;
    }
};
```

При создании объекта на основе шаблонного класса необходимо передать не только значения, но также тип данных.

```cpp
Test<float> newObject;
newObject.setElement(2.6);
```
""",
            "end": """В ходе видео курса мы изучили основные моменты в языке C++. 
Язык C++ состоит из множества библиотек, которые расширяют его функционал и добавляют новые возможности. 
Изучить все библиотеки невозможно, а главное не нужно.

Вам необходимо выбрать определённую сферу, в которой хотите работать и тогда уже изучать специализированные библиотеки для вашей сферы. 
К примеру, если вы хотите создавать программы под Windows, то можно изучить работу с программой QT.

На закрепление знаний вы можете просмотреть большой видео урок по изучению C++ за час! 
Также вы можете перейти на страницу с этим видео и получить дополнительные домашние задания и готовый код.

Программа обучения
Также хотим отметить, что если вас интересует более углубленное изучение самого языка и его фреймворков, 
то предлагаем вашему внимаю наш полный курс по изучению C++. 
За курс вы изучите язык C++, научитесь работать с библиотекой STL, 
базами данных, многопоточностью и научитесь строить приложения при помощи WinForms и QT.
""",
            "ChatGPT": """
## Me:
Можешь переписать этот код на C++?

```python
a = [0, 1, "привет", "мир"]
print(a[2], a[3])
```
----------------------------------------------------------------

## ChatGPT:
Да, я могу переписать этот код на C++:

```cpp
#include <iostream>
#include <vector>

int main() {
    std::vector<std::string> a = { "0", "1", "привет", "мир" };
    std::cout << a[2] << " " << a[3] << std::endl;
    return 0;
}
```

Здесь я использовал std::vector, чтобы создать массив строк, 
поскольку C++ не поддерживает нетипизированные массивы.
""",
            "Разное": r"""
[https://metanit.com/cpp/tutorial/](https://metanit.com/cpp/tutorial/)

Вывод в консоль

```cpp
cout << "Hello World!\n";
```

Функция вывода

```cpp
template <typename T>
void print(T args) {cout << args << "\n";}
print("text1", "text2");
```

Русский язык в консоли

```cpp
int main() {SetConsoleCP(1251); SetConsoleOutputCP(1251);
```

Параметры для функции main
```cpp
int main (int argc, char *argv[]) {}
```

многострочный комментарий

```cpp
/* многострочный комментарий */
```

Автоподстановка типа

```cpp
auto number = 5;
```

Подобие mach/case в Python

```cpp
int x = 2;
switch (x) {
    case 1:
        std::cout << "x = 1" << "\n";
        break;
    case 2:
        std::cout << "x = 2" << "\n";
        break;
    case 3:
        std::cout << "x = 3" << "\n";
        break;
    default:
        std::cout << "x is undefined" << "\n";
        break;
    }
```

Позволяет сократить определение простейших условных конструкций if и имеет следующую форму:
[первый_операнд - условие] ? [второй_операнд] : [третий_операнд]
                                if true             if false
```cpp
int result = sign == '+' ? x + y : x - y;
```

&& (конъюнкция, логическое умножение)
Возвращает true, если оба операнда не равны false.
Возвращает false, если хотя бы один операнд равен false.

```cpp
bool a = true;
bool b = false;
bool c = a && b;    // false
bool d = a && true; // true
```

|| (дизъюнкция, логическое сложение)
Возвращает true, если хотя бы один операнд равен true.
Возвращает false, если оба операнда равны false.

```cpp
bool a = true;
bool b = false;
bool c = a || b;        // true
bool d = b || false;    // false
```
""",
            "Операции над числами": r"""Префиксный инкремент. Увеличивает значение переменной на единицу и 
полученный результат используется как значение выражения ++x

```cpp
int a = 8; int b = ++a;
std::cout << a << "\n"; // 9
std::cout << b << "\n"; // 9
```

Постфиксный инкремент. Увеличивает значение переменной на единицу, 
но значением выражения x++ будет то, которое было до увеличения на единицу

```cpp
int a = 8; int b = a++;
std::cout << a << "\n"; // 9
std::cout << b << "\n"; // 8
```

Префиксный декремент. Уменьшает значение переменной на единицу, и полученное значение используется как значение выражения

```cpp
int a = 8; int b = --a;
std::cout << a << "\n"; // 7
std::cout << b << "\n"; // 7
```

Постфиксный декремент. Уменьшает значение переменной на единицу, но значением выражения x-- будет то, которое было до уменьшения на единицу

```cpp
int a = 8; int b = a--;
std::cout << a << "\n"; // 7
std::cout << b << "\n"; // 8
```
""",
            "for while": r"""Цикл for
for (начальные_условия;  условие_для_выполнения_цикла; изменение_параметров_цикла) {}

```cpp
for(int i = 1; i < 10; i++) {}
```

Но можно и так

```cpp
int i = 1;
for (; i < 10;) {
    std::cout << i << " * " << i << " = " << i * i << std::endl;
    i++;
}
```

Этот цикл применим к контейнерам разной природы (массивам, векторам, спискам и т. д.).
Пока рассмотрим его на примере строк. 
Цикл позволяет удобно проитерироваться по символам строки, не используя индексов. 
В этом примере мы считываем строку и печатаем отдельно все символы строки и их ASCII-коды:

```cpp
#include <iostream>
#include <string>

int main() {
    std::string line;
    std::getline(std::cin, line);
    for (char symbol : line) {
        std::cout << symbol << "\t" << static_cast<int>(symbol) << "\n";
    }
}
```
""",
            "Массив": r"""Массив
тип_переменной название_массива [длина_массива]

```cpp
int numbers[4];
int numbers[4] = {1,2,3,4};
int numbers[4] = {1, 2, 3, 4, 5, 6}; //ОШИБКА!
int numbers[] = {1, 2, 3, 4, 5, 6};
char s1[] = {'h', 'e', 'l', 'l', 'o'}; длинна 5
char s2[] = "world"; длинна 6! (добавляется '\0')
//Нельзя присвоить одному массиву другой массив
int nums1[] = {1,2,3,4,5};
int nums2[] = nums1;    // ошибка
nums2 = nums1;          // ошибка
```

Перебор массива

```cpp
#include <iostream>
int main() {
    int numbers[4] = { 1,2,3,4 };
    int size = sizeof(numbers) / sizeof(numbers[0]);
    for (int i = 0; i < size; i++)
        std::cout << numbers[i] << std::endl;
    return 0;
}
```

Или цикл for специально для массивов

```cpp
#include <iostream>
int main() {
    int numbers[4] = { 1,2,3,4 };
    for (int number : numbers)              //(или можно спользовать auto number)
        std::cout << number << std::endl;

    return 0;
}
```
""",
            "Строка": """Строки
```cpp
#include <string>
std::string s1;                  // пустая строка
std::string s2 = "hello";        // hello
std::string s3("welcome");       // welcome
std::string s4(5, 'h');          // hhhhh
std::string s5 = s2;             // hello

string s1 = "hello";
s1.size() == 5                   // true
s1.empty()                       // false
```

Изменение строки

```cpp
std::string hello = "Hello";
char c = hello[1];               // e
hello[0] = 'M';
std::cout << hello << std::endl; // Mello
```

Форматирование строк

```cpp
string text1 = "text1";
string text2 = "text2";
int number = 12345;
string out = text1 + " " + to_string(number) + " " + text2;
cout << out << endl;
```

Получить полный ввод подобие input()

```cpp
get_line(cin, out)
```

Выберет только первое слово из введённых (подобие text.split()[0] в Python)

```cpp
cin >> out
```
""",
            "Указатели2": """Указатели
& и *

```cpp
int count = 100
m = &count; //m получает адрес count
m == например 2000
q = *m; //q получает значение по адресу m
q == 100

m = &count;
```

Это адрес внутреннего местоположения переменной в компьютере.
С самим значением переменной ничего не делается.
Оператор & можно запомнить как «взятие адреса».
Поэтому вышеупомянутый оператор присваивания можно прочитать как «m получает адрес count».

Для лучшего понимания данного присваивания предположим, 
что переменная count находится по адресу 2000. 
Также предположим, что count имеет значение 100. 
После данного присваивания m будет содержать 2000. 

Оператор*, дополняющий &. Это унарный оператор, возвращающий значение переменной по указанному адресу.
Например: если m содержит адрес переменной count, то

```cpp
q = *m;
```

Следуя вышеприведенному примеру, q получит значение 100, 
поскольку 100 хранилось по адресу 2000 - адресу, находящемуся в переменной m.
Операция* может быть запомнена как «по адресу».
В данном случае оператор можно прочитать как «q получает значение по адресу m».
""",
        },
        "Bash": {
            "help": """
# Работа с файлами

|         |   |
|---------|---|
| COPY    | Копирование одного или нескольких файлов в другое место.
| DEL     | Удаление одного или нескольких файлов.
| REN     | Переименовывает файлы.
| RENAME  | Переименовывает файлы.
| REPLACE | Заменяет файлы.
| TYPE    | Отображает содержимое текстовых файлов.
| XCOPY   | Копирует файлы и деревья папок.


# Работа с папками
|       |   |
|-------|---|
| DIR   | Вывод списка файлов и подпапок из указанной папки.
| RD    | Удаляет каталог.
| RMDIR | Удаляет каталог.


# Для получения сведений об определенной команде наберите HELP <имя команды>
|             |   |
|-------------|---|
| CD          | Вывод имени либо смена текущей папки.
| ECHO        | Отображает сообщения и переключает режим отображения команд на экране.
| CLS         | Очистка экрана.
| CMD         | Запуск еще одного интерпретатора командных строк Windows.
| COLOR       | Установка цветов переднего плана и фона, используемых по умолчанию.
|             |
| ASSOC       | Вывод либо изменение сопоставлений по расширениям имен файлов.
| ATTRIB      | Отображение и изменение атрибутов файлов.
| BREAK       | Включение и выключение режима обработки комбинации клавиш CTRL+C.
| BCDEDIT     | Задает свойства в базе данных загрузки для управления начальной загрузкой.
| CACLS       | Отображение и редактирование списков управления доступом (ACL) к файлам.
| CALL        | Вызов одного пакетного файла из другого.
| CHCP        | Вывод либо установка активной кодовой страницы.
| CHDIR       | Вывод имени либо смена текущей папки.
| CHKDSK      | Проверка диска и вывод статистики.
| CHKNTFS     | Отображение или изменение выполнения проверки диска во время загрузки.
| COMP        | Сравнение содержимого двух файлов или двух наборов файлов.
| COMPACT     | Отображение и изменение сжатия файлов в разделах NTFS.
| CONVERT     | Преобразует тома FAT в NTFS. Вы не можете преобразовать текущий диск.
| DATE        | Вывод либо установка текущей даты.
| DISKPART    | Отображает или настраивает свойства раздела диска.
| DOSKEY      | Редактирует командные строки, повторно вызывает команды Windows и создает макросы.
| DRIVERQUERY | Отображает текущее состояние и свойства драйвера устройства.
| ENDLOCAL    | Завершает локализацию изменений среды для пакетного файла.
| ERASE       | Удаляет один или несколько файлов.
| EXIT        | Завершает работу программы CMD.EXE (интерпретатора командных строк).
| FC          | Сравнивает два файла или два набора файлов и отображает различия между ними.
| FIND        | Ищет текстовую строку в одном или нескольких файлах.
| FINDSTR     | Ищет строки в файлах.
| FOR         | Запускает указанную команду для каждого из файлов в наборе.
| FORMAT      | Форматирует диск для работы с Windows.
| FSUTIL      | Отображает или настраивает свойства файловой системы.
| FTYPE       | Отображает либо изменяет типы файлов, используемые при сопоставлении по расширениям имен файлов.
| GOTO        | Направляет интерпретатор команд Windows в отмеченную строку пакетной программы.
| GPRESULT    | Отображает информацию о групповой политике для компьютера или пользователя.
| GRAFTABL    | Позволяет Windows отображать расширенный набор символов в графическом режиме.
| HELP        | Выводит справочную информацию о командах Windows.
| ICACLS      | Отображает, изменяет, архивирует или восстанавливает списки ACL для файлов и каталогов.
| IF          | Выполняет условную обработку в пакетных программах.
| LABEL       | Создает, изменяет или удаляет метки тома для дисков.
| MD          | Создает каталог.
| MKDIR       | Создает каталог.
| MKLINK      | Создает символьные ссылки и жесткие связи
| MODE        | Настраивает системные устройства.
| MORE        | Последовательно отображает данные по частям размером в один экран.
| MOVE        | Перемещает один или несколько файлов из одного каталога в другой.
| OPENFILES   | Отображает файлы, открытые для файлового ресурса удаленными пользователями.
| PATH        | Отображает или устанавливает путь поиска исполняемых файлов.
| PAUSE       | Приостанавливает выполнение пакетного файла и выводит сообщение.
| POPD        | Восстанавливает предыдущее значение текущего каталога, сохраненное с помощью команды PUSHD.
| PRINT       | Выводит на печать содержимое текстового файла.
| PROMPT      | Изменяет командную строку Windows.
| PUSHD       | Сохраняет текущий каталог, затем изменяет его.
| RECOVER     | Восстанавливает данные, которые можно прочитать, с плохого или поврежденного диска.
| REM         | Записывает комментарии в пакетные файлы или файл CONFIG.SYS.
| ROBOCOPY    | Улучшенная служебная программа копирования файлов и деревьев папок
| SET         | Показывает, устанавливает или удаляет переменные среды Windows.
| SETLOCAL    | Начинает локализацию изменений среды в пакетном файле.
| SC          | Отображает или настраивает службы (фоновые процессы).
| SCHTASKS    | Выполняет команды и запускает программы на компьютере по расписанию.
| SHIFT       | Изменяет положение заменяемых параметров в пакетных файлах.
| SHUTDOWN    | Позволяет локально или удаленно завершить работу компьютера.
| SORT        | Сортирует ввод.
| START       | Выполняет указанную программу или команду в отдельном окне.
| SUBST       | Связывает путь с именем диска.
| SYSTEMINFO  | Отображает сведения о свойствах и конфигурации определенного компьютера.
| TASKLIST    | Отображает все выполняемые задачи, включая службы.
| TASKKILL    | Прекращение или остановка процесса либо приложения.
| TIME        | Отображает или устанавливает системное время.
| TITLE       | Назначает заголовок окна для сеанса CMD.EXE.
| TREE        | Графически отображает структуру каталогов диска или пути.
| VER         | Отображает сведения о версии Windows.
| VERIFY      | Устанавливает режим проверки в Windows правильности записи файлов на диск.
| VOL         | Отображает метку и серийный номер тома для диска.
| WMIC        | Отображает сведения об инструментарии WMI в интерактивной командной оболочке.
""",
            "Переменные окружения": """
```bash
set MY_VAR="my_value"
```

Чтобы удалить переменную окружения через командную строку (cmd) в Windows, 
можно использовать команду `setx` с параметром `/m`, где `/m` указывает, что переменная должна быть удалена из системной области.

Например, чтобы удалить переменную `MY_VAR`, можно выполнить следующую команду в `cmd`:

```bash
setx MY_VAR /m
```

После выполнения этой команды переменная `MY_VAR` будет удалена из системной области. 
Обратите внимание, что эта команда не удалит переменную из текущей области видимости командной строки, 
поэтому если вы хотите удалить переменную только из текущей сессии cmd, вы можете использовать команду `set`:

```bash
set MY_VAR=
```

Эта команда устанавливает значение переменной `MY_VAR` в пустую строку, что эквивалентно её удалению.


Если вы хотите удалить переменную окружения только временно, в рамках текущей сессии cmd, то можно использовать команду `set` с параметром `/u`, который 


Чтобы получить значение переменной, можно использовать команду `echo` с параметром `%variable_name%`, 
где `variable_name` - это имя переменной, значение которой нужно получить. 
Например, чтобы получить значение переменной `MY_VAR`, можно выполнить следующую команду в `cmd`:

```bash
echo %MY_VAR%
```

После выполнения этой команды в консоль будет выведено значение переменной `MY_VAR`, если она определена.

Чтобы сохранить значение переменной в файле, можно использовать оператор перенаправления вывода `>` или `>>`. 
Например, чтобы сохранить значение переменной `MY_VAR` в файл `my_file.txt`, можно выполнить следующую команду:

```bash
echo %MY_VAR% > my_file.txt
```

После выполнения этой команды значение переменной `MY_VAR` будет записано в файл `my_file.txt`, 
и если файл не существовал, то он будет создан. 
Если нужно добавить значение переменной в конец файла, а не перезаписать его, можно использовать оператор `>>` вместо `>`:

```bash
echo %MY_VAR% >> my_file.txt
```

Это добавит значение переменной в конец файла `my_file.txt`, если файл уже существует. 
Если файл не существует, то он будет создан и в него будет записано значение переменной.
""",
        },
        "LaTex": {
            "Элементы": r"""

## Пробелы
```LaTex
\quad - Большой пробел
\! - Сдвинуть назад
"\ " - Маленький пробел
```

## Матрица
```LaTex
\begin{bmatrix}
{}&{}\\
{}&{}
\end{bmatrix}
```

## Система уравнений
```LaTex
\begin{cases}
{}\\
{}
\end{cases}
```

## Дробь
```LaTex
\frac{}{}
```

## Форматирование текста
```LaTex
\underline{} - нижнее подчёркивание
\textbf{} - жирный текст
```

## Символы
```LaTex
\Delta - Треугольничек
\dots - ...
\сdot - Точка умножений
\lambda - Лямбда
\ne - !=
\approx - ≈

\left? - Левая скобка
\right? - Правая скобка
```
"""
        },
        "Go": {
            "devhints.io": """
[Go cheatsheet](?Other/Links.md#go)
""",
        },
    },
    "Other": {
        "File formats": {
            "JSON": r"""
# JSON - JavaScript Object Notation

Tекстовый формат обмена данными, который основан на синтаксисе JavaScript.
Он используется для хранения и обмена структурированными данными и часто используется
в веб-приложениях для обмена данными между клиентом и сервером.

```json
{
    "name": "John Smith",
    "age": 30,
    "city": "New York"
}
```

```python
import json


config = {"BOT": {"bot_name": "", "token": ""}}

with open("config.json", "w", encoding="UTF-8") as file:
    file.write(json.dumps(config, indent=4, ensure_ascii=False))
    # json.dump(config, file, indent=4, ensure_ascii=False)

with open("config.json", "r", encoding="UTF-8") as file:
    config = json.load(file)
    # config = json.loads(file.read())

print(config)
```

# JSONL

```python
{"name": "Alice Jones", "age": 25, "city": "Los Angeles"}
{"name": "John Smith", "age": 30, "city": "New York"}
{"name": "Bob Johnson", "age": 40, "city": "Chicago"}
```

```python
import json


config = [
    {"name": "Alice Jones", "age": 25, "city": "Los Angeles"},
    {"name": "John Smith", "age": 30, "city": "New York"},
    {"name": "Bob Johnson", "age": 40, "city": "Chicago"},
]

with open("test.jsonl", "a", encoding="UTF-8") as file:
    file.writelines([str(line) + "\n" for line in config])

with open("config.jsonl", "r", encoding="UTF-8") as file:
    for line in file:
        print(json.loads(line))
```

[[Other/File formats/TinyDB (json).md]]
""",
            "YAML": """
# YAML - Ain't Markup Language

Формат файлов, который используется для хранения и обмена неструктурированными и структурированными
данными. Например он популярен в файлах настройки приложений, описание конфигураций и т.д.
`YAML` использует отступы и специальные символы для обозначения структуры данных.
Он также поддерживает множество типов данных, включая строки, числа, логические значения и массивы.

```yaml
name: John Smith
age: 30
city: New York
```

```python
import yaml  # pip install yaml


config = {"BOT": {"bot_name": "", "token": ""}}

with open("config.yaml", "w", encoding="utf-8") as file:
    file.write(yaml.safe_dump(config, sort_keys=False, allow_unicode=True, indent=4))

with open("config.yaml", "r", encoding="utf-8") as file:
    config = yaml.safe_load(file.read())

print(config)
```
""",
            "TOML": """
# TOML - Tom's Obvious, Minimal Language

формат конфигурационных файлов, который был разработан
для использования в проектах, написанных на языке программирования `Rust`.

TOML файлы имеют структуру ключ-значение, где ключи и значения
разделены знаком `=`, и используют синтаксис, похожий на язык программирования `INI`.

```toml
[package]
name = "example"
version = "1.0.0"
authors = ["John Doe <john@example.com>"]
```

```python
import toml  # pip install toml


config = {"BOT": {"bot_name": "", "token": ""}}

with open("config.toml", "w", encoding="UTF-8") as file:
    file.write(toml.dumps(config))
    # toml.dump(config, file)

with open("config.toml", "r", encoding="UTF-8") as file:
    config = toml.load(file)
    # config = toml.loads(file.read())

print(config)
```
""",
            "INI": """
# INI (Initialization)

формат конфигурационных файлов, который используется 
для хранения настроек приложений и операционных систем. 
Он был разработан в `Windows` и стал широко используемым 
форматом для хранения конфигурационных данных в различных программных продуктах.

```ini
[Section1]
key1 = value1
key2 = value2

[Section2]
key3 = value3
key4 = value4
```

```python
# config = configparser.ConfigParser()
# config["BOT"] = {"bot_name": "", "token": ""}

import configparser


config = {"BOT": {"bot_name": "", "token": ""}}
config_ini = configparser.ConfigParser()

for key, value in config.items():
    config_ini[key] = value

with open("config.ini", "w") as file:
    config_ini.write(file)

config_ini = configparser.ConfigParser()
config_ini.read("config.ini")
print(config)
```
""",
            "XML": """
# XML - eXtensible Markup Language

Расширяемый язык разметки, который используется для хранения и обмена структурированными данными.
Он использует теги для определения структуры данных и может быть использован для хранения
всех видов данных, включая текст, изображения и мультимедиа.
`XML` широко используется в Интернете для хранения и обмена данными между веб-сервисами и приложениями.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<note>
<to>Tove</to>
<from>Jani</from>
<heading>Reminder</heading>
<body>Don't forget me this weekend!</body>
</note>
```

```python
# config = ET.Element("config")
# bot = ET.SubElement(config, "BOT")
# ET.SubElement(bot, "bot_name").text = ""
# ET.SubElement(bot, "token").text = ""
# tree = ET.ElementTree(config)

import xml.etree.ElementTree as xml

def dict_to_xml(dct, root_node=None):
    if root_node is None:
        root_node = xml.Element("root")
    for key, value in dct.items():
        node = xml.SubElement(root_node, key)
        if isinstance(value, dict):
            dict_to_xml(value, node)
        else:
            node.text = str(value)
    return root_node

def xml_to_dict(root):
    from collections import defaultdict
    dct = {root.tag: {} if root.attrib else None}
    children = list(root)
    if children:
        dd = defaultdict(list)
        for dc in map(xml_to_dict, children):
            for k, v in dc.items():
                dd[k].append(v)
        dct = {root.tag: {k: v[0] if len(v) == 1 else v for k, v in dd.items()}}
    if root.attrib:
        dct[root.tag].update(("@" + k, v) for k, v in root.attrib.items())
    if root.text:
        text = root.text.strip()
        if children or root.attrib:
            if text:
                dct[root.tag]["#text"] = text
        else:
            dct[root.tag] = text
    return dct

config = {"BOT": {"bot_name": "", "token": ""}}
config = dict_to_xml(config)
tree = xml.ElementTree(config)

with open("config.xml", "wb") as file:
    tree.write(file, encoding="utf-8", xml_declaration=True)

with open("config.xml", "r") as file:
    tree = xml.parse(file)

root = tree.getroot()
config = xml_to_dict(root)
print(config)
```
""",
            "CSV": """
# CSV - Comma Separated Values

Текстовый формат файла, который используется для хранения табличных данных.
Каждая строка файла содержит одну запись, а значения в этой записи разделены запятыми.

```csv
Name,Age,City
John Smith,30,New York
Jane Doe,25,Chicago
```

```python
import csv


data = [
    ("Name", "Age"),
    ("Alice", 25),
    ("Bob", 30),
    ("Charlie", 35),
]

with open("data.csv", "w", newline="", encoding="UTF-8") as file:
    csv.writer(file).writerows(data)

with open("data.csv", "r", encoding="UTF-8") as file:
    print(list(csv.reader(file)))
```
""",
            "SQLite3 to CSV": '''
```python
import sqlite3
import csv

def SQL(query: str, params: tuple | dict = None, commit: bool = False, column_names: bool = False):
    """Выполняет SQL запрос"""
    with sqlite3.connect(r"database.sqlite") as connection:
        cursor = connection.cursor()
        cursor.execute(query, params)
        if commit: connection.commit()
        result = cursor.fetchall()
        if column_names and getattr(cursor, "description"):
            column_names_data = [column[0] for column in cursor.description] or None
            result = column_names_data + result
    return result

data = SQL("SELECT * FROM table_name;")

with open("data.csv", "w", newline="", encoding="UTF-8") as file:
    writer = csv.writer(file)
    writer.writerows(data)

with open("data.csv", "r", encoding="UTF-8") as file:
    reader = csv.reader(file)
    column_names = next(reader)
    SQL(
        f"""
CREATE TABLE table_name (
    {', '.join([f"{column} TEXT" for column in column_names])}
);
""",
        commit=True,
    )
    for row in reader:
        SQL(
            f"""
INSERT INTO table_name (
    {', '.join(column_names)}
)
VALUES (
    {', '.join([f'"{column}"' for column in row])}
)
""",
            commit=True,
        );
```
''',
            "Vedis db": """
```python
from vedis import Vedis
db = Vedis(":mem:")  # Create an in-memory database.
db = Vedis("Dict.vedis")
with db.transaction():
    db["key"] = "value"
    db.rollback()  # Undo changes.
    db.commit()
print(db["key"])
```

[https://vedis-python.readthedocs.io/en/latest/quickstart.html](https://vedis-python.readthedocs.io/en/latest/quickstart.html)

Пример использования в боте
[https://mastergroosha.github.io/telegram-tutorial/docs/lesson_11/](https://mastergroosha.github.io/telegram-tutorial/docs/lesson_11/)
""",
            "TinyDB (json)": """
```bash
pip install tinydb
```

```python
from tinydb import TinyDB, Query


db = TinyDB("db.json")
users_table = db.table("users")
user_id = users_table.insert({"name": "John", "age": 25})
all_users = users_table.all()

# Получение записи по условию (например, по имени)
user_query = Query()
john_data = users_table.search(user_query.name == "John")

# Изменение данных в записи по условию (например, по имени)
users_table.update({"age": 26}, user_query.name == "John")

# Удаление записи по условию (например, по имени)
users_table.remove(user_query.name == "John")
```

[[Other/File formats/JSON.md]]
""",
        },
        "Code examples": {
            "Пирамида граф": """
Нахождение пути с максимальной суммой по "пирамиде"

```python
graph = [
    [75],
    [95, 64],
    [17, 47, 82],
    [18, 35, 87, 10],
    [20,  4, 82, 47, 65],
    [19,  1, 23, 75,  3, 34],
    [88,  2, 77, 73,  7, 63, 67],
    [99, 65,  4, 28,  6, 16, 70, 92],
    [41, 41, 26, 56, 83, 40, 80, 70, 33],
    [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
    [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
    [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
    [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
    [63, 66,  4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
    [ 4, 62, 98, 27, 23,  9, 70, 98, 73, 93, 38, 53, 60,  4, 23],
]

# Cоздаем пустой словарь для хранения сумм каждого узла.
sums = {}
for i in range(len(graph)):
    for j in range(len(graph[i])):
        sums[(i, j)] = graph[i][j]

# Проходимся по каждому узлу в пирамиде и вычисляем сумму каждого узла
# Начинаем с последней строки пирамиды и движемся вверх
for i in range(len(graph)-2, -1, -1):
    for j in range(len(graph[i])):
        sums[(i, j)] += max(sums[(i+1, j)], sums[(i+1, j+1)])

# Step 3
max_sum_path = sums[(0, 0)]

# Step 4
i, j = 0, 0
path = [graph[0][0]]
while i < len(graph) - 1:
    left_sum = sums[(i+1, j)]
    right_sum = sums[(i+1, j+1)]
    if left_sum > right_sum:
        i += 1
    else:
        i += 1
        j += 1
    path.append(graph[i][j])

print(sum(path))
```

```python
def max_sum_path(graph):
    n = len(graph)
    # Инициализируем максимальную сумму первого элемента
    max_sum = graph[0][0]
    for i in range(1, n):
        # Проходим по строкам и столбцам "ниже" текущего элемента
        for j in range(i + 1):
            if j == 0: # Если элемент находится на краю графа, то соседи существуют только с одной стороны
                graph[i][j] += graph[i - 1][j]
            elif j == i: # Если элемент находится на краю графа, то соседи существуют только с одной стороны
                graph[i][j] += graph[i - 1][j - 1]
            else: # В остальных случаях элемент имеет двух соседей
                graph[i][j] += max(graph[i - 1][j - 1], graph[i - 1][j])
            # Обновляем максимальную сумму
            max_sum = max(max_sum, graph[i][j])
    return max_sum

# Пример использования функции
graph = [[45], [23, 78], [12, 26, 51]]
print("Максимальная сумма пути в графе:", max_sum_path(graph))
```

```python
def longest_slide_down(p):
    res = p.pop()
    while p:
        tmp = p.pop()
        res = [tmp[i] + max(res[i],res[i+1]) for i in range(len(tmp))] 
    return res.pop()
```


# Обьяснение
Если граф будет равен

```python
graph = [
        [45], 
      [23, 78], 
    [12, 26, 51]]
```
""",
            "Определитель матрицы": """
```python@matrix.py
class Matrix:
    def __init__(self, matrix: list[list[int]]):
        self.matrix = matrix

    def get_minor(self, i: int, j: int) -> list[list[int]]:
        result = [
            list(row[:j] + row[j+1:])
            for row_index, row in enumerate(self.matrix) 
            if row_index != i
        ]
        return result

    def det(self):
        n = len(self.matrix)
        if len({len(row) for row in self.matrix}) > 1 and n != x[0]:
            raise ValueError("")

        if n == 1:
            return self.matrix[0][0]

        elif n == 2:
            return (
                self.matrix[0][0] * self.matrix[1][1]
            ) - (
                self.matrix[0][1] * self.matrix[1][0]
            )
        elif n == 3:
            return (
                self.matrix[0][0] * self.matrix[1][1] * self.matrix[2][2]
            ) + (
                self.matrix[0][1] * self.matrix[1][2] * self.matrix[2][0]
            ) + (
                self.matrix[0][2] * self.matrix[1][0] * self.matrix[2][1]
            ) - (
                self.matrix[0][2] * self.matrix[1][1] * self.matrix[2][0]
            ) - (
                self.matrix[0][0] * self.matrix[1][2] * self.matrix[2][1]
            ) - (
                self.matrix[0][1] * self.matrix[1][0] * self.matrix[2][2]
            )

        else:
            result = []
            i = 0
            for j, x in enumerate(self.matrix[0]):
                minor = self.get_minor(i, j)
                result.append(x * ((-1)**(i+1 + j+1)) * Matrix(minor).det())
            return sum(result)
```

```python@test_matrix_1.py
from matrix import Matrix

m = [
    [1, 5, 7, 4, 9],
    [4, 7, 8, 3, 4],
    [9, 3, 5, 2, 8],
    [9, 3, 6, 3, 1],
    [5, 9, 1, 4, 2]
]

print(Matrix(m).det())
```

```python@test_matrix_2.py
from numpy import linalg
m = [
    [1, 5, 7, 4, 9],
    [4, 7, 8, 3, 4],
    [9, 3, 5, 2, 8],
    [9, 3, 6, 3, 1],
    [5, 9, 1, 4, 2]
]
print(linalg.det(m))
```
""",
            "Минимальное максимальное число матрицы cpp": r"""
```cpp@maxminmatrix.cpp
#include <iostream>
#include <vector>
#include <time.h>
#include <iomanip>

using namespace std;

int main() {
    int rows = 3;
    int cols = 4;
    srand(time(NULL));
    vector<vector<int>> matrix(rows, vector<int>(cols, 0));
    for (int i = 0; i < rows; ++i) {
        cout << "|";
        for (int j = 0; j < cols; ++j) {
            int number = 1 + rand() % 999;
            matrix[i][j] = number;
            cout << " " << setw(3) << setfill(" ") << number << " |";
        }
        cout << "\n";
    }
    int max = 0;
    int min = 999;
    for (auto r : matrix) {
        for (auto c : r) {
            if (c > max) max = c;
            if (c < min) min = c;
        }
    }
    cout << "max = " << max << "\n" << "min = " << min << "\n";
    return 0;
}
```
""",
            "str - int": """
```python
chr_digit = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]


def number_to_string(number):
    if number == 0:
        return "0"
    sign = "-" if number < 0 else ""
    number = abs(number)
    digits = []
    while number > 0:
        digit = number % 10
        digits.append(chr_digit[digit])
        number //= 10
    digits.reverse()
    return sign + "".join(digits)


def string_to_number(string):
    if string == "0":
        return 0
    sign = 1
    if string[0] == "-":
        sign = -1
        string = string[1:]
    number = 0
    for char in string:
        digit = chr_digit.index(char)
        number = number * 10 + digit
    return sign * number
```
```pycon
>>> print(number_to_string(12345))
"12345"
>>> print(string_to_number("12345"))
12345
```
""",
            "fib": """
```python
def fib(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b
```
```pycon
>>> print(list(fib(10)))
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
```
""",
            "converters": '''
```python
def sqrt(x, p: int = 2):
    return pow(x, (1 / p))
```
```python
def rgb_to_hex(r: int, g: int, b: int) -> str:
    return "#{:02x}{:02x}{:02x}".format(r, g, b).upper()

def hex_to_rgb(h: str) -> tuple[int, int, int]:
    return tuple(int(h.lstrip("#")[i:i + 2], 16) for i in (0, 2, 4))
```
```pycon
>>> rgb_to_hex(164, 73, 211)
"#A449D3"
>>> hex_to_rgb("#A449D3")
(164, 73, 211)
```
```python
def html_escape(text):
    return "".join(f"&#{ord(char)};" for char in text)
```
```python
def tg_color(chat_id: int):
    """
    0x6FB9F0 Синий
    0xFFD67E Оранжевый
    0xCB86DB Фиолетовый
    0x8EEE98 Зелёный
    0xFF93B2 Розовый
    0xFB6F5F Красный
    """
    return {0: "К", 1: "О", 2: "Ф", 3: "З", 4: "Г", 5: "С", 6: "Р"}[abs(chat_id) % 7]
```
```python
def unicode(text):
    return "".join(fr"\\U{ord(char):0>8x}" for char in text)
```
''',
            "quicksort": """
```python
def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)


quicksortL = lambda array: (
    array
    if len(array) < 2 else
    (
        lambda pivot, less, greater: quicksortL(less) + [pivot] + quicksortL(greater)
    )(
        **(
            lambda pivot, temp_arr: {
                "pivot": pivot,
                "less": [i for i in temp_arr if i <= pivot],
                "greater": [i for i in temp_arr if i > pivot]
            }
        )(array[0], array[1:])
    )
)
```
```pycon
>>> print(quicksort([10, 5, 2, 3]))
[2, 3, 5, 10]
```
""",
            "download telegram emoji": """
```python
import logging

import requests
from requests.exceptions import MissingSchema


def download_emoji(emoji: str) -> bool:
    emoji_name = "-".join(str(hex(ord(c)))[2:] for c in emoji)
    print(emoji_name)
    link = f"https://web.telegram.org/a/img-apple-64/{emoji_name}.png"
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/120.0.0.0 Safari/537.36 Edg/113.0.1774.42"
        )
    }
    try:
        with open(f"emojis/{emoji_name}.png", "wb") as file:
            file.write(requests.get(link, headers=headers).content)
        return True
    except MissingSchema as e:
        logging.error(f"{e}")
    except ConnectionError:
        logging.error("404")
    return False
```
""",
            "js YouTube": """
# изменение скорости воспроизведения на ютубе
```javascript
javascript:document.getElementsByClassName("video-stream html5-main-video")[0].playbackRate = 2.5;
```
""",
            "словарь обращение через точку": """
# Словарь обращение через точку

```python
class Dict:
    def __init__(self, d: dict):
        self.d = d

    def __getattr__(self, item: str):
        return self.__class__(self.d.get(item))

    def __setattr__(self, name, value):
        if name == 'd':
            super().__setattr__(name, value)
        else:
            self.d[name] = value

    def __repr__(self):
        return __repr__(self.d)
```
""",
        },
        "Minecraft": {
            "Color": """
| color name   |                                                                         | color | chat | hex code  | rgb           | motd       | decimal    |
|--------------|-------------------------------------------------------------------------|:-----:|:----:|-----------|---------------|------------|------------|
| dark_red     | <div style="background-color: #AA0000;width: 50px;height: 15px;"></div> | `&4`  | `§4` | #`AA0000` | `170 0 0`     | `\\u00A74` | `11141120` |
| red          | <div style="background-color: #FE5555;width: 50px;height: 15px;"></div> | `&c`  | `§c` | #`FF5555` | `255 85 85`   | `\\u00A7c` | `16733525` |
| gold         | <div style="background-color: #FFAA00;width: 50px;height: 15px;"></div> | `&6`  | `§6` | #`FFAA00` | `255 170 0`   | `\\u00A76` | `16755200` |
| yellow       | <div style="background-color: #FFFF55;width: 50px;height: 15px;"></div> | `&e`  | `§e` | #`FFFF55` | `255 255 85`  | `\\u00A7e` | `16777045` |
| green        | <div style="background-color: #55FF55;width: 50px;height: 15px;"></div> | `&a`  | `§a` | #`55FF55` | `0 170 0`     | `\\u00A7a` | `5635925`  |
| dark_green   | <div style="background-color: #00AA00;width: 50px;height: 15px;"></div> | `&2`  | `§2` | #`00AA00` | `85 255 85`   | `\\u00A72` | `43520`    |
| aqua         | <div style="background-color: #55FFFF;width: 50px;height: 15px;"></div> | `&b`  | `§b` | #`55FFFF` | `85 255 255`  | `\\u00A7b` | `5636095`  |
| dark_aqua    | <div style="background-color: #00AAAA;width: 50px;height: 15px;"></div> | `&3`  | `§3` | #`00AAAA` | `0 170 170`   | `\\u00A73` | `43690`    |
| blue         | <div style="background-color: #5555FF;width: 50px;height: 15px;"></div> | `&9`  | `§9` | #`5555FF` | `0 0 170`     | `\\u00A79` | `5592575`  |
| dark_blue    | <div style="background-color: #0000AA;width: 50px;height: 15px;"></div> | `&1`  | `§1` | #`0000AA` | `85 85 255`   | `\\u00A71` | `170`      |
| light_purple | <div style="background-color: #FF55FF;width: 50px;height: 15px;"></div> | `&d`  | `§d` | #`FF55FF` | `255 85 255`  | `\\u00A7d` | `16733695` |
| dark_purple  | <div style="background-color: #AA00AA;width: 50px;height: 15px;"></div> | `&5`  | `§5` | #`AA00AA` | `170 0 170`   | `\\u00A75` | `11141290` |
| white        | <div style="background-color: #FFFFFF;width: 50px;height: 15px;"></div> | `&f`  | `§f` | #`FFFFFF` | `255 255 255` | `\\u00A7f` | `16777215` |
| gray         | <div style="background-color: #AAAAAA;width: 50px;height: 15px;"></div> | `&7`  | `§7` | #`AAAAAA` | `170 170 170` | `\\u00A77` | `11184810` |
| dark_gray    | <div style="background-color: #555555;width: 50px;height: 15px;"></div> | `&8`  | `§8` | #`555555` | `85 85 85`    | `\\u00A78` | `5592405`  |
| black        | <div style="background-color: #000000;width: 50px;height: 15px;"></div> | `&0`  | `§0` | #`000000` | `0 0 0`       | `\\u00A70` | `0`        |

|            |    |
|------------|----|
| color name | string code, mostly used banner and items
| chat       | start with the `§` character, used for chat, books and signs
| motd       | Used in the server config for setting message of the day
| hex code   | paint color and web css colors
| decimal    | used for nbt data tags, setting potion and leather armour colors

| style         | chat   | motd       |
|---------------|--------|------------|
| Obfuscated    | `§k`   | `\\u00A7k` |
| Bold          | `§l`   | `\\u00A7l` |
| Strikethrough | `§m`   | `\\u00A7m` |
| Underline     | `§n`   | `\\u00A7n` |
| Italic        | `§o`   | `\\u00A7o` |
| Reset         | `§r`   | `\\u00A7r` |                       
""",
        },
        "Alt Symbols": """

| Символ | Код  |
|-------:|:-----|
| `§`    | 21   |
| `…`    | 0133 |
| `¹`    | 0185 |
| `²`    | 0178 |
| `³`    | 0179 |

""",
        "Links": """
# Python

| Описание                                | Ссылка |
|:----------------------------------------|:-------|
| Дорожная карта                          | [https://roadmap.sh/python](https://roadmap.sh/python) [https://roadmap.sh/backend](https://roadmap.sh/backend) [https://roadmap.sh/roadmaps](https://roadmap.sh/roadmaps) |
| Sorting Algorithms                      | [https://www.tutorialspoint.com/python_data_structure/python_sorting_algorithms.htm](https://www.tutorialspoint.com/python_data_structure/python_sorting_algorithms.htm)<br>[https://realpython.com/sorting-algorithms-python/](https://realpython.com/sorting-algorithms-python/) |
| логирование                             | [https://habr.com/ru/companies/wunderfund/articles/683880/](https://habr.com/ru/companies/wunderfund/articles/683880/) |
| re                                      | [https://www.exlab.net/files/tools/sheets/regexp/regexp.pdf](https://www.exlab.net/files/tools/sheets/regexp/regexp.pdf)<br>[https://www.exlab.net/files/tools/sheets/regexp/regexp.png](https://www.exlab.net/files/tools/sheets/regexp/regexp.png) |
| Recursive Regular Expressions           | [http://www.rexegg.com/regex-recursion.html](http://www.rexegg.com/regex-recursion.html) |
| Магические методы                       | [https://habr.com/ru/post/186608/](https://habr.com/ru/post/186608/) |
| Unit Tests                              | [https://machinelearningmastery.com/a-gentle-introduction-to-unit-testing-in-python/](https://machinelearningmastery.com/a-gentle-introduction-to-unit-testing-in-python/) |
| Асинхронность                           | [https://habr.com/ru/articles/421625/](https://habr.com/ru/articles/421625/) |
| Лексический анализ. Документация Python | [https://digitology.tech/docs/python_3/reference/lexical_analysis.html#grammar-token-conversion](https://digitology.tech/docs/python_3/reference/lexical_analysis.html#grammar-token-conversion) |
| string                                  | [https://digitology.tech/docs/python_3/library/string.html](https://digitology.tech/docs/python_3/library/string.html) |


# Python Другое

|                                       |                                                                             |
|:--------------------------------------|:----------------------------------------------------------------------------|
| Алгоритм генерации судоку             | [https://habr.com/ru/articles/192102/](https://habr.com/ru/articles/192102/)<br>[https://habr.com/ru/post/249899/](https://habr.com/ru/post/249899/)<br>[https://www.cs.mcgill.ca/~aassaf9/python/algorithm_x.html](https://www.cs.mcgill.ca/~aassaf9/python/algorithm_x.html) |
| Компиляторы и трансляторы кода Python | [https://egorovegor.ru/python-compiler-and-translator/](https://egorovegor.ru/python-compiler-and-translator/)<br>[https://medium.com/doctolib/understanding-and-fixing-n-1-query-30623109fe89](https://medium.com/doctolib/understanding-and-fixing-n-1-query-30623109fe89) |
| N + 1 query                           |                                                                             |


# C++

|                |                                                                  |
|----------------|------------------------------------------------------------------|
| Дорожная карта | [https://habr.com/ru/specials/726724/](https://habr.com/ru/specials/726724/)<br>[https://practicum.yandex.ru/blog/yazyk-c-plus-dlya-chego-nuzhen/](https://practicum.yandex.ru/blog/yazyk-c-plus-dlya-chego-nuzhen/)<br>[https://en.cppreference.com/w/](https://en.cppreference.com/w/)                                   |


# Go

|               |                                                  |
|---------------|--------------------------------------------------|
| Go cheatsheet | [https://devhints.io/go](https://devhints.io/go) |


# GIT GitHub

|                               |                                      |
|-------------------------------|--------------------------------------|
| Git и Github. Простые рецепты | [https://habr.com/ru/articles/273897/](https://habr.com/ru/articles/273897/) |
| Книга                         | [https://git-scm.com/book/ru/v2](https://git-scm.com/book/ru/v2)       |


# HTML

|             |                                                            |
|-------------|------------------------------------------------------------|
| SVG         | [https://flowbite.com/icons/](https://flowbite.com/icons/) |
| codepen.io  | [https://codepen.io/](https://codepen.io/)                 |
| svgrepo.com | [https://www.svgrepo.com/](https://www.svgrepo.com/)       |


# General

|       |          |
|-------|----------|
| Управляющие символы | [https://ru.wikipedia.org/wiki/Управляющие_символы](https://ru.wikipedia.org/wiki/Управляющие_символы) |
| Каретная нотация    | [https://ru.wikipedia.org/wiki/Каретная_нотация](https://ru.wikipedia.org/wiki/Каретная_нотация)       |
| Па́ттерны проектирования<br>Design Patterns | [https://ru.wikipedia.org/wiki/Design_Patterns](https://ru.wikipedia.org/wiki/Design_Patterns) |

# Downloads

|                  |   |
|------------------|---|
| Python           | [https://www.python.org/downloads/](https://www.python.org/downloads/)<br>[https://github.com/python/cpython](https://github.com/python/cpython) |
| Java             | [https://www.oracle.com/java/technologies/downloads/#java](https://www.oracle.com/java/technologies/downloads/#java) |
| GIT              | [https://git-scm.com/downloads](https://git-scm.com/downloads) |
| PyCharm          | [https://www.jetbrains.com/pycharm/download/](https://www.jetbrains.com/pycharm/download/) |
| IntelliJ IDEA    | [https://www.jetbrains.com/idea/download/](https://www.jetbrains.com/idea/download/)<br>[https://github.com/JetBrains/intellij-community](https://github.com/JetBrains/intellij-community) |
| Docker           | [https://www.docker.com/get-started/](https://www.docker.com/get-started/)<br>[https://github.com/docker/for-win](https://github.com/docker/for-win) |
| DBeaver          | [https://dbeaver.io/download/](https://dbeaver.io/download/)<br>[https://github.com/dbeaver/dbeaver](https://github.com/dbeaver/dbeaver) |
| Windows Terminal | [https://apps.microsoft.com/detail/9n0dx20hk701](https://apps.microsoft.com/detail/9n0dx20hk701)<br>[https://github.com/microsoft/terminal](https://github.com/microsoft/terminal) |
| DevToys          | [https://devtoys.app/](https://devtoys.app/)<br>[https://github.com/DevToys-app/DevToys](https://github.com/DevToys-app/DevToys) |
| SQLiteStudio     | [https://sqlitestudio.pl/](https://sqlitestudio.pl/)<br>[https://github.com/pawelsalawa/sqlitestudio](https://github.com/pawelsalawa/sqlitestudio) |

""",
        "TODO": """
# TODO

1. Перенести `metadata.json` в `cheatsheet`.
2. Добавлять `SVG` с помощью `JavaScript` для уменьшения размера `index.html`.
3. Искать подходящую библиотеку для `Markdown`.
4. Оглавление. Окошко с текстовыми `h` тегами из текущей шпаргалки, прокручивает до видимости при нажатии. 
5. Подсвечивать нажатую кнопку постоянно, а не `:active`.
6. Сделать ссылку на шпаргалку как всплывашка при наведении на ссылку.
7. Сделать поисковые фишки как в [[General/Google Search.md]].
8. История поиска

Поменять в метадате color на classList

<!--
- Параметр поиска `s` в `URL`
    - ?path
    - ?path&s=query
    - ?path\\#anchor
    - ?s=query
    - ?s=query\\#anchor
    - \\#anchor
    - ?path&s=query\\#anchor
-->
""",
        "Markdown": r"""

\*Italic\* - *Italic*
\_Italic\_ - _Italic_

\*\*Bold\*\* - **Bold**
\_\_Bold\_\_ - __Bold__

\*\*\*Bold & Italic\*\*\* - ***Bold & Italic***
\_\_\_Bold & Italic\_\_\_ - ___Bold & Italic___
\*\*\_Bold & Italic\_\*\* - **_Bold & Italic_**
\_\*\*Bold & Italic\*\*\_ - _**Bold & Italic**_

\`text\` - `text`

\|\|text\|\| - ||text||

&#x7e;&#x7e;text&#x7e;&#x7e; - ~~text~~

&#x3d;&#x3d;mark&#x3d;&#x3d; - ==mark==

&#x3d;&#x3d;{color:red;background-color:inherit;}mark&#x3d;&#x3d; - =={color:red;background-color:inherit;}mark==

```pre
code
```

````pre
```pre
code
```
````

`````pre
````pre
```pre
code
```
````
`````

```table
| c1 | c2 |
|----|----|
| v1 | v2 |
| v3 | v4 |
```

| c1 | c2 |
|----|----|
| v1 | v2 |
| v3 | v4 |

```table
|    |    |
|----|----|
| v1 | v2 |
| v3 | v4 |
```

|    |    |
|----|----|
| v1 | v2 |
| v3 | v4 |

<!--
> blockquote
>> blockquote
>>> blockquote
> blockquote
-->
""",
    },
    "Shortcuts": {
        "link-1": "Languages/Python/fstrings.md",
        "link-2": "Languages/RegExp/RegExp.md",
        "Java": {
            "link-3": "Languages/Java/",
            "link-4": "Languages/Java/Классы/",
        },
    },
}
