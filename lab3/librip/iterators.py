# Итератор для удаления дубликатов
import itertools
class Unique(object):
    def __init__(self, items, **kwargs):
        self.unique=[]
        if isinstance(items, list):
            self.items=iter(items)
        else: items
        self.ignore_case=False
        self.ignore_case=kwargs.get('ignore_case', False)
        self.upp=[]

        # Нужно реализовать конструктор
        # В качестве ключевого аргумента, конструктор должен принимать bool-параметр ignore_case,
        # в зависимости от значения которого будут считаться одинаковые строки в разном регистре
        # Например: ignore_case = True, Aбв и АБВ разные строки
        #           ignore_case = False, Aбв и АБВ одинаковые строки, одна из них удалится
        # По-умолчанию ignore_case = False

    def __next__(self):
        # Нужно реализовать __next__
        while True:
            try:
                current=next(self.items)
                if isinstance(current, str) and self.ignore_case is True:
                    value=current.upper()
                    if value not in self.upp:
                        self.upp.append(value)
                    if value!=self.upp[-1]:
                        elem=current
                    elem=current.upper()
                else:
                    elem=current
                if not elem in self.unique:
                    self.unique.append(elem)
                    return current
            except Exception:
                raise StopIteration

    def __iter__(self):
        return self

def Sorted(mass):
    module=[]
    for x in mass:
        abs(x).append(module)
    sorted(module)


