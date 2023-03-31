from collections import deque


class CustomDict:
    def __init__(self):
        self._data = {}
        self._history = deque(maxlen=10)

    def __setitem__(self, key, value):
        self._data[key] = value
        self._history.append(key)

    def __getitem__(self, key):
        return self._data[key]

    def get_history(self):
        return self._history

my_dict = CustomDict()

try:
    while True:
        new_key = input('Specify the key: ')
        new_value = input('Add the value: ')
        my_dict[new_key] = new_value
except EOFError:
    print('\n', list(my_dict.get_history()))