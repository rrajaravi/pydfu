import unittest

import pydfu


class DiskFree(unittest.TestCase):
    def get_df(self):
        df = pydfu.df()
        self.assertIsInstance(
            df, pydfu.fs.Fs, msg="return data type is correct")

    def test_query_particulars(self):
        df = pydfu.df()
        fs = df[0]
        map(lambda attr: self.assertTrue(hasattr(fs, attr)),
            ['name', 'size', 'used', 'avail', 'use', 'path']
            )

    def test_conditional_query(self):
        df = pydfu.df()
        fs = df.query_one(path='/')
        self.assertTrue(fs.path == '/')

        fs = df.query(size='>10g')
        self.assertTrue(isinstance(fs, list))

        fs = df.query_one(use='>100%')
        self.assertIsNone(fs, msg="success: invalid query returned none")

        fs = df.query_one(use='<100%')
        self.assertTrue(fs.use < 100)

        fs = df.query(size='>1000000000g')
        self.assertTrue(fs == [])

        fs = df.query_one(size='>10g', use='<50%')
        if fs:
            # cross check
            self.assertTrue(fs.check_size('>10g')
                            and fs.check_use('<50%') and True)


class Scanner(unittest.TestCase):

    def test_run_scanner(self):
        print('running')
