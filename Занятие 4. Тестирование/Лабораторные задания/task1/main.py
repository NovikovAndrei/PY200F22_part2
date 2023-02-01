class Pets:
    """Класс питомцы"""
    counter = 0

    def __init__(self, kind: str, breed: str, name: str, age: int):
        """
        Инициализация класса питомцы
        :param kind: Вид
        :param breed: Порода
        :param name: Кличка
        :param age: Возраст
        """
        self._kind = kind
        self._breed = breed
        self.is_valid_kind_breed(self.kind, self.breed)
        self.name = name
        self.age = age
        Pets.__count()
        self.__add_to_registr()

    @staticmethod
    def __count():
        """Счетчик созданных экземпляров"""
        Pets.counter += 1

    @property
    def kind(self) -> str:
        """
        Установка Вида
        :return: Вид питомца
        """
        return self._kind

    @property
    def breed(self):
        """
        Установка породы
        :return: Порода
        """
        return self._breed

    @classmethod
    def is_valid_kind_breed(cls, kind: str, breed: str) -> str:
        """
        Проверка валидности породы
        :param kind: вид
        :param breed: порода
        :return: валидна порода или нет
        """
        if not isinstance(kind, str):
            raise TypeError("Вид может быть только типа str")
        if not isinstance(breed, str):
            raise TypeError("Порода может быть только типа str")
        cls._kind = kind
        cls._breed = breed
        return "Вид и порода валидны"

    @property
    def name(self) -> str:
        """
        Возвращает кличку
        :return: кличка
        """
        return self._name

    @name.setter
    def name(self, val: str):
        """
        Установка клички
        :param val: значение для установки
        :return: кличка
        """
        if not isinstance(val, str):
            raise TypeError("Имя может быть только типа str")
        self._name = val

    @property
    def age(self) -> int:
        """
        Возвращает возраст
        :return: возраст
        """
        return self._age

    @age.setter
    def age(self, val: int):
        """
        Установка возраста
        :param val: значение для установки
        :return: возраст
        """
        if not isinstance(val, int):
            raise TypeError("возраст может быть только типа целым числом")
        if val < 1:
            raise ValueError("Возраст должен быть больше нуля")
        self._age = val

    def __add_to_registr(self):
        """Добавление в реестр"""
        with open("registr.txt", "a", encoding="utf8") as f:
            f.writelines(f"\t Питомец №{Pets.counter}\n"
                         f"{self.__str__()}\n")

    @staticmethod
    def print_registr():
        """Вывод файла регистра"""
        with open("registr.txt", "r", encoding="utf8") as f:
            print(f.read())

    def __repr__(self):
        return f"{__class__.__name__}(kind={self._kind!r}, breed={self._breed!r}, name={self.name!r}, age={self.age})"

    def __str__(self):
        return f"Вид: {self._kind}, порода: {self._breed!r}, кличка: {self.name!r}, возраст: {self.age}"


class Cat(Pets):
    """Класс кошки"""

    def __init__(self, breed: str, name: str, age: int, affectionateness: str, kind: str = "Кот"):
        """
        Подготовка к инициализации класса кошки
        :param breed: Порода
        :param name: Кличка
        :param age: возраст
        :param affectionateness: ласковость
        :param kind: Вид (по-умолчанию "кот")
        """
        super().__init__(kind, breed, name, age)
        self.affectionateness = affectionateness

    @property
    def affectionateness(self) -> str:
        """
        Возвращает атрибут ласковость
        :return: ласковость
        """
        return self._affectionateness

    @affectionateness.setter
    def affectionateness(self, val):
        """
        Установка атрибута ласковость
        :param val: значение атрибута ласковость
        :return: ласковость
        """
        if not isinstance(val, str):
            raise TypeError("Может быть только типа str")
        if val not in ("низкая", "средняя", "высокая"):
            raise ValueError('Ласковость может быть только: "низкая", "средняя", "высокая"')
        self._affectionateness = val

    def __repr__(self):
        return f"{__class__.__name__}(breed={self._breed!r}, " \
               f"name={self.name!r}, age={self.age}, affectionateness={self.affectionateness})"

    def __str__(self):
        return f"{super().__str__()}"


class Dog(Pets):
    def __init__(self, breed: str, name: str, age: int, security_qualities: str, kind: str = "Собака"):
        super().__init__(kind, breed, name, age)
        self.security_qualities = security_qualities

    @property
    def security_qualities(self) -> str:
        """
        Возвращает атрибут охранные качества
        :return: охранные качества
        """
        return self._security_qualities

    @security_qualities.setter
    def security_qualities(self, val):
        """
        Установка атрибута охранные качества
        :param val: значение атрибута охранные качества
        :return: охранные качества
        """
        if not isinstance(val, str):
            raise TypeError("Может быть только типа str")
        if val not in ("низкий", "средний", "высокий"):
            raise ValueError('Уровень охранных качеств может быть только: "низкий", "средний", "высокий"')
        self._security_qualities = val

    def __repr__(self):
        return f"{__class__.__name__}(breed={self._breed!r}, " \
               f"name={self.name!r}, age={self.age}, security_qualities={self.security_qualities})"

    def __str__(self):
        return f"{super().__str__()}"


if __name__ == "__main__":
    # Write your solution here
    pet = Pets("cat", "maincoon", "hulk", 10)
    # print(pet.name)
    # pet.name = "123"
    # print(pet.name)
    # print(Pets.is_valid_kind_breed("1", "1234"))
    # print(Pets.counter)
    pet2 = Pets("asd", "asdff", "ddd", 33)
    # print(Pets.counter)
    pet3 = Pets("asd", "asdff", "ddd", 333)
    # print(Pets.counter)
    # print(pet)
    cat1 = Cat("maincoon", "jerry", 11, "высокая")
    # print(cat1)
    dog1 = Dog("Пит", "кратос", 2, "средний")
    print(dog1)
    print(dog1.security_qualities)

