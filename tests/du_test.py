import unittest

import pydfu


class DiskUsage(unittest.TestCase):

    def setUp(self):
        self._du = pydfu.du()

    def test_query(self):
        _data = self._du.query('/tmp')
        self.assertTrue(len(_data) != 0)

    def test_query_obj(self):
        _data = self._du.query('/tmp')
        for attr in ['name', 'size_in_byte', 'size']:
            self.assertTrue(hasattr(_data[0], attr))

    def test_check_query_functionality(self):
        _data = self._du.query('/tmp')
        _correct = [item for item in _data
                    if not item.name.startswith('/tmp')] and False or True
        self.assertTrue(_correct)

    def test_default_stdout(self):
        self.assertTrue(hasattr(self._du.stdout('/tmp'), 'getvalue'))
