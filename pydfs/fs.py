import re


class Fs:

    checkers = {'name': 'check_name',
                'size': 'check_size',
                'used': 'check_used',
                'avail': 'check_avail',
                'use': 'check_use',
                'path': 'check_path',
                }

    def __init__(self, data):
        if len(data) != 6:
            raise RuntimeError("Invalid df output")

        self.name = data[0]
        self.size = data[1]
        self.used = data[2]
        self.avail = data[3]
        self.use = int(data[4][:-1])
        self.path = data[5]

    def convert(self, size, scheme):
        scheme = scheme.lower()
        if scheme == 'g':
            return 1024 * 1024 * size
        elif scheme == 'm':
            return 1024 * size
        elif scheme == 'k':
            return size

    def check_use(self, use):
        _condition, _use = None, '=='

        re_obj = re.search(r'([=<>==]*)([0-9]+)', use)
        if re_obj:
            _condition = re_obj.group(1) or _condition
            _use = re_obj.group(2) or _use

        else:
            raise RuntimeError('Invalid value provided for use= : ', use)

        return eval("%s %s %s" % (self.use, _condition, _use))

    def check_name(self, name):
        return self.name == name

    def check_path(self, path):
        return self.path == path

    def check_used(self, used):
        return self.check_use(used)

    def check_size(self, size):
        _size, _condition, _scheme = float(0), '==', 'k'

        re_obj = re.search(r'([=<>==]*)([0-9]+)(.)', size)
        if re_obj:
            _condition = re_obj.group(1) or _condition
            _size = int(re_obj.group(2)) or _size
            _scheme = re_obj.group(3) or _scheme
        else:
            raise RuntimeError('Invalide value provided for size= : ', size)

        _size = self.convert(_size, _scheme)
        return eval("%s %s %s" % (self.size, _condition, _size))

    def for_print(self):
        return [self.name, self.size, self.used, self.avail,
                str(self.use) + '%', self.path]

    def __repr__(self):
        return self.path
