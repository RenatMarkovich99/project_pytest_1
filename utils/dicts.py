def get_val(collection, key, default='git'):
    """Возвращает значение из словаря по переданному ключу,
    если ключ существует.
    В ином случае возвращает значение default
    :param collection: Исходный словарь.
    :param key: Ключ.
    :param default: Значение по-умолчанию.
    :return: Значение по индексу или значение по-умолчанию.
    """
    if key in collection:
        return collection[key]
    else:
        return default
