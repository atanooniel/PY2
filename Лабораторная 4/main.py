import doctest


class DndWeapon:
    """
    Класс описывает поведение объекта "Оружие" для настольной игры ДнД
    """
    def __init__(self, name: str, cost: int, dmg: int) -> None:
        """
        Инициализация объекта "Оружие ДнД"
        :param name: Имя оружия (может быть изменено)
        :param cost: Цена оружия в игровом магазине (параметр постоянен после создания объекта)
        :param dmg: Урон оружия (параметр постоянен после создания объекта)

        Пример:
        >>> rock = DndWeapon('Камень', 1, 2) #инициализация экземпляра класса
        """
        # ToDo блок проверок
        self.name = name
        self._cost = cost
        self._dmg = dmg

    @property
    def cost(self) -> int:  # инкапсуляция атрибута через свойства, read-only
        return self._cost

    @property
    def dmg(self) -> int:  # инкапсуляция атрибута через свойства, read-only
        return self._dmg

    def __str__(self) -> str:
        """
        :return: Строковое представление основных переменных объекта
        """
        return f'Оружие ДнД: {self.name}, урон {self.dmg}, цена {self.cost}'

    def __repr__(self) -> str:
        """
        :return: Валидная строка для инициализации идентичного объекта
        """
        return f'{self.__class__.__name__}({self.name!r}, {self.cost}, {self.dmg})'

    def weapon_damage(self, armor: int) -> int:
        """
        Метод расчета урона оружия по заданной цели
        :param armor: Показатель брони цели
        :return: Урон, достигший цели

        Пример:
        >>> rock = DndWeapon('Камень', 1, 2)
        >>> rock.weapon_damage(10)
        """
        ...

    def weapon_battle_stats(self) -> str:
        """
        Метод, возвращающий боевые характеристики оружия
        :return: Строковое представление боевых характеристик оружия

        Пример:
        >>> rock = DndWeapon('Камень', 1, 2)
        >>> rock.weapon_battle_stats()
        """
        ...


class DndRangeWeapon(DndWeapon):
    """
    Класс описывает поведение объекта "Дальнобойное оружие персонажа в ДнД"
    """

    def __init__(self, name: str, cost: int, dmg: int, distance: int) -> None:
        """
        Инициализация объекта "Дальнобойное оружие ДнД"
        :param name: Имя оружия (может быть изменено)
        :param cost: Цена оружия в игровом магазине (параметр постоянен после создания объекта)
        :param dmg: Урон оружия (параметр постоянен после создания объекта)
        :param distance: Максимальная дальность стрельбы (параметр постоянен после создания объекта)

        Пример:
        >>> bow = DndRangeWeapon('Лук', 15, 5, 100)
        """
        # ToDo блок проверок
        super().__init__(name, cost, dmg)
        self._distance = distance

    @property
    def distance(self) -> int:
        return self._distance  # инкапсуляция атрибута через свойства, read-only

    def __repr__(self) -> str:  # метод перегружен
        """
        :return: Валидная строка для инициализации идентичного объекта
        Метод перегружен ввиду расширенного списка атрибутов
        """
        return f'{self.__class__.__name__}({self.name!r}, {self.cost}, {self.dmg}, {self.distance})'

    def hit_check(self, target_distance: int) -> bool:
        """
        Метод, проверяющий попадание в цель
        :param target_distance: Дистанция до цели стрельбы
        :return: True при попадании, False при промахе

        Пример:
        >>> bow = DndRangeWeapon('Лук', 15, 5, 100)
        >>> bow.hit_check(90)
        """
        ...

    def weapon_battle_stats(self) -> str:
        """
        Метод, возвращающий боевые характеристики оружия
        Перегруженный метод родительского класса, т.к. дистанция также входит в боевые характеристики
        :return: Строковое представление боевых характеристик оружия

        Пример:
        >>> bow = DndRangeWeapon('Лук', 15, 5, 100)
        >>> bow.weapon_battle_stats()
        """
        ...


class DndMeleeWeapon(DndWeapon):
    """
    Класс описывает поведение объекта "Оружие ближнего боя персонажа в ДнД"
    """

    def __init__(self, name: str, cost: int, dmg: int, melee_type: str) -> None:
        """
        Инициализация объекта "Оружие ближнего боя ДнД"
        :param name: Имя оружия (может быть изменено)
        :param cost: Цена оружия в игровом магазине (параметр постоянен после создания объекта)
        :param dmg: Урон оружия (параметр постоянен после создания объекта)
        :param melee_type: Тип оружия (параметр постоянен после создания объекта)

        Пример:
        >>> sword = DndMeleeWeapon('Меч', 20, 7, 'одноручный')
        """
        # ToDo блок проверок
        super().__init__(name, cost, dmg)
        self._melee_type = melee_type

    @property
    def melee_type(self) -> str:  # инкапсуляция атрибута через свойства, read-only
        return self._melee_type

    def __repr__(self) -> str:  # метод перегружен
        """
        :return: Валидная строка для инициализации идентичного объекта
        Метод перегружен ввиду расширенного списка атрибутов
        """
        return f'{self.__class__.__name__}({self.name!r}, {self.cost}, {self.dmg}, {self.melee_type!r})'


if __name__ == "__main__":
    doctest.testmod()
    pass
