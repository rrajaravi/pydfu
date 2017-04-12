from __future__ import print_function
import os
import math
import sys
import six
from collections import namedtuple

if six.PY2:
    from cStringIO import StringIO
else:
    if sys.version_info.minor <= 3:
        from StringIO import StringIO
    else:
        from io import StringIO

FileObj = namedtuple('FileObj', 'name size_in_byte size_in_h size')
DirObj = namedtuple('DirObj', 'name size_in_byte size_in_h size')


class DiskUsage(object):
    def __init__(self):
        self.db = []
        self.path = None
        self.recursive = False
        self.human_readable = False
        self.total_size = 0
        self.total_size_in_h = 0
        self.total_size_in_byte = 0
        self.stdout_write = False

    @staticmethod
    def convert_size(size_bytes):
        if size_bytes is 0:
            return '0B'
        size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
        i = int(math.floor(math.log(size_bytes, 1024)))
        p = math.pow(1024, i)
        s = round(size_bytes / p, 2)
        return '%s %s' % (s, size_name[i])

    def get_size(self):
        _total_size = 0
        for root, dirs, files in os.walk(self.path):
            for name in files:
                file_name = os.path.join(root, name)
                size = os.stat(file_name).st_size
                size_in_h = self.convert_size(size)
                _total_size += size

                self.db.append(FileObj(
                    name=file_name,
                    size_in_byte=size,
                    size_in_h=size_in_h,
                    size=self.human_readable and size_in_h or size)
                )

            for _dir in dirs:
                abs_dir = os.path.join(root, _dir)
                size = os.stat(abs_dir).st_size
                size_in_h = self.convert_size(size)
                _total_size += size
                self.db.append(DirObj(
                    name=abs_dir,
                    size_in_byte=size,
                    size_in_h=size_in_h,
                    size=self.human_readable and size_in_h or size)
                )

        self.total_size_in_byte = _total_size
        self.total_size_in_h = self.convert_size(_total_size)
        self.total_size = self.human_readable and self.total_size_in_h or \
            self.total_size_in_byte

    def query(self, path, **kwargs):
        self.parse(path, **kwargs)
        self.get_size()
        return self.db

    def parse(self, path, **kwargs):
        self.path = path
        self.stdout_write = kwargs.get('write', self.stdout_write)
        self.recursive = kwargs.get('recursive', self.recursive)
        self.human_readable = kwargs.get('h', self.human_readable)

    def stdout(self, path, **kwargs):
        buffer = StringIO()
        self.parse(path, **kwargs)
        self.get_size()
        for item in self.db:
            buffer.write(str(item.size).ljust(10) + item.name + '\n')
        buffer.write("\nTotal Size: " + str(self.total_size))

        if self.stdout_write:
            print(buffer.getvalue())
            buffer.close()
        else:
            return buffer

    def __getitem__(self, item):
        _find = [x for x in self.db if x.name == item]
        return _find and _find[0] or None

    def __len__(self):
        len(self.db)
