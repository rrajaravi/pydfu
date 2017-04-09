from subprocess import Popen, PIPE

from .fs import Fs

# create fs objects


def get_fs():
    cmd = ['df']
    p = Popen(cmd, stdin=PIPE, stdout=PIPE)
    p.wait()
    out, err = p.communicate()
    data = []
    out = isinstance(out, bytes) and out.decode('utf-8') or out

    for _line in out.splitlines()[1:]:
        if _line:
            _data = _line.split()
            data.append(Fs(_data))
    return data


class Df:

    def __init__(self):
        self._items = get_fs()
        self.opeartions = Fs.checkers

    def __len__(self):
        return len(self._items)

    def __getitem__(self, item):
        return self._items[item]

    def find_by_path(self, path):
        return filter(lambda f: getattr(f, 'path') == path,
                      self._items)

    def find_by_name(self, name):
        return filter(lambda f: getattr(f, 'name') == name,
                      self._items)

    def find(self, *args, **kwargs):
        result = []
        for _item in self._items:
            fail = False
            for k, v in kwargs.items():
                r = getattr(_item, self.opeartions[k])(v)
                if not r:
                    fail = True

            if fail is False:
                result.append(_item)

        return result

    def query(self, *args, **kwargs):
        return self.find(*args, **kwargs)

    def query_one(self, *args, **kwargs):
        _result_lst = self.find(*args, **kwargs)
        return _result_lst and _result_lst[0] or None
