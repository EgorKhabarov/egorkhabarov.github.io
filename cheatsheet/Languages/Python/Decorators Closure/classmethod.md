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
