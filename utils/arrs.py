"""Функции для работы с массивами"""


def get(array, index, default=None):
    """
    Извлекает из списка значение по указанному индексу, если индекс существует.
    Если индекс не существует, возвращает значение по умолчанию.
    Функция работает только с неотрицательными индексами.
    :param array: Исходный список.
    :param index: Индекс извлекаемого элемента.
    :param default: Значение по-умолчанию.
    :return: Значение по индексу или значение по-умолчанию.
    """
    if index < 0:
        return default

    return array[index]


def my_slice(coll, start=0, end=None):
    """
    Возвращает новый массив, содержащий копию части исходного массива.
    :param coll: Исходный список.
    :param start: Индекс, по которому начинается извлечение. Если индекс отрицательный,
    start указывает смещение от конца списка. По умолчанию равен нулю.
    :param end: Индекс, по которому заканчивается извлечение (не включая элемент с индексом end).
    Если индекс отрицательный, end указывает смещение от конца списка. По умолчанию равен длине исходного списка.
    :return: Массив элементов
    """
    length = len(coll)

    if length == 0:
        return []

    normalized_end = length if end is None else end

    normalized_start = start

    if normalized_start < 0:
        if normalized_start < -length:
            normalized_start = 0
        else:
            normalized_start += length

    return coll[normalized_start:normalized_end]
