import doctest


class Bulb:
    """
    Класс описывает поведение объекта лампочки
    """

    def __init__(self, light_status: bool):
        """
        Создание и подготовка к работе объекта "Лампочка"

        :param light_status: Статус лампочки: горит - True, не горит - False

        :raise TypeError если light_status передан в типе данных, отличном от bool

        Пример:
        >>> lamp = Bulb(True) # инициализация экземпляра класса
        """
        if not isinstance(light_status, bool):
            raise TypeError("Статус лампочки должен быть типа bool")
        self.light_status = light_status

    def is_light_on(self) -> bool:
        """
        Функция проверяет статус лампочки (горит / не горит)

        :return: Статус лампочки (горит / не горит)

        Пример:
        >>> lamp = Bulb(True)
        >>> lamp.is_light_on()
        """
        ...

    def turn_on_off(self) -> None:
        """
        Функция изменяет статус лампочки на противоположный (имитация кнопки включения / выключения)

        Пример:
        >>> lamp = Bulb(True)
        >>> lamp.turn_on_off()
        """
        ...


class DNDLevelTracker:
    """
    Трекер уровня и полученного опыта для настольной игры ДнД
    """

    def __init__(self, current_exp: int, lvl: int):
        """
        Создание и подготовка к работе объекта "Трекер уровня персонажа ДнД"

        :param current_exp: Текущий опыт персонажа на момент создания
        :param lvl: Текущий уровень персонажа на момент создания

        :raise TypeError если current_exp или lvl переданы в формате, отличном от int
        :raise ValueError если стартовый уровень или опыт отрицательные

        >>> Aragorn = DNDLevelTracker(100, 4)
        """
        if not isinstance(current_exp, int):
            raise TypeError("Старотовый опыт должен быть в целочисленном формате")
        if current_exp < 0:
            raise ValueError("Опыт должен быть положительным или нулевым")
        self.current_exp = current_exp

        if not isinstance(lvl, int):
            raise TypeError("Уровень персонажа должен быть целочисленным")
        if lvl < 0:
            raise ValueError("Стартовый уровень должен быть положительным или нулевым")
        self.lvl = lvl

    def gain_exp(self, exp: int) -> [int]:
        """
        Функция которая добавляет полученный опыт к соданному персонажу.
        Поднимает уровень персонажа при достижении неообходимого опыта

        :param exp: Полученный опыт
        :return: Значение текущего опыта и уровеня

        :raise TypeError если exp передан в формате, отличном от int

        >>> Aragorn = DNDLevelTracker(100, 4)
        >>> Aragorn.gain_exp(50)
        """
        if not isinstance(exp, int):
            raise TypeError("Получаемый опыт должен быть в целочисленном формате")
        if exp < 0:
            raise ValueError("Получаемый опыт должен быть положительным числом")
        ...

    def lvl_check(self) -> [int]:
        """
        Функция которая выводит информацию по текущему опыту и уровню персонажа

        :return: Значение текущего опыта и уровеня

        >>> Aragorn = DNDLevelTracker(100, 4)
        >>> Aragorn.lvl_check()
        """
        ...


class CameraMemory:
    """
    Класс описывает поведение памяти фотаппарата при съемке
    """

    def __init__(self, model: str, max_memory: int, busy_memory: int):
        """
        Создание и подготовка к работе объекта "Память фотоаппарата"

        :param model: Модель фотоаппарата в формате str
        :param max_memory: Максимально доступная память фотоаппарата, в байтах
        :param busy_memory: Занятая память фотоаппарата, в байтах

        :raise TypeError при несоответсвии типов передаваемых данных
        :raise ValueError при передаче не положительной max_memory, при отрицательной busy_memory
        :raise ValueError если занятая память больше максимальной памяти

        >>> nikon_d3100 = CameraMemory('Nikon D3100', 8589934592, 1073741824)
        """
        if not isinstance(model, str):
            raise TypeError("Модель фотаппарата должна быть типа str")
        self.model = model

        if not isinstance(max_memory, int):
            raise TypeError("Максимальная память фотаппарата должна быть типа int")
        if max_memory <= 0:
            raise ValueError("Максимальная память фотаппарата должна быть больше 0 байт")
        self.max_memory = max_memory

        if not isinstance(busy_memory, int):
            raise TypeError("Занятая память фотаппарата должна быть типа int")
        if busy_memory < 0:
            raise ValueError("Занятая память фотаппарата не может быть отрицательной")
        if busy_memory > max_memory:
            raise ValueError("Занятая память не должна быть больше максимальной памяти фотоаппарата")
        self.busy_memory = busy_memory

    def take_pict(self, pict_size: int) -> None:
        """
        Снятие фотографии, добавление фотографии в память фотоаппарата

        :param pict_size: Размер сохраняемой фотографии, в байтах

        :raise TypeError при несоответсвии типов передаваемых данных
        :raise ValueError при не положительном значении размера фотографии

        >>> nikon_d3100 = CameraMemory('Nikon D3100', 8589934592, 1073741824)
        >>> nikon_d3100.take_pict(20971520)
        """
        if not isinstance(pict_size, int):
            raise TypeError("Размер фотографии должен быть типа int")
        if pict_size <= 0:
            raise ValueError("Размер фотографии должен быть больше 0 байт")
        ...

    def delete_picts(self, memory_to_delete: int) -> None:
        """
        Функция удаления заданног объема занятой памяти

        :param memory_to_delete: Размер очищаемой памяти, в байтах

        :raise TypeError при несоответсвии типов передаваемых данных
        :raise ValueError при отрицательном размере удаляемых файлов
        :raise ValueError если удаляемый размер файлов больше, чем занятый объем памяти фотоаппарата

        >>> nikon_d3100 = CameraMemory('Nikon D3100', 8589934592, 1073741824)
        >>> nikon_d3100.delete_picts(10485760)
        """
        if not isinstance(memory_to_delete, int):
            raise TypeError("Размер удаляемых файлов должен быть типа int")
        if memory_to_delete < 0:
            raise ValueError("Размер удаляемых файлов не может быть отрицательным")
        if memory_to_delete > self.busy_memory:
            raise ValueError("Размер удаляемых файлов не может быть больше объема занятой памяти")
        ...

    def free_memory(self) -> int:
        """
        Функция отображает объем свободной памяти

        :return: Объем свободной памяти, в байтах

        >>> nikon_d3100 = CameraMemory('Nikon D3100', 8589934592, 1073741824)
        >>> nikon_d3100.free_memory()
        """
        ...


if __name__ == "__main__":
    doctest.testmod()
    pass
