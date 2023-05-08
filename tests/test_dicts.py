from utils import dicts


def test_get_val():
    assert dicts.get_val({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}, 'd', 'git') == 4
    assert dicts.get_val({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}, 't', 'git') == "git"
    assert dicts.get_val({}, 'a', 'git') == "git"
