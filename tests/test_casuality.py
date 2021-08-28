from pathlib import Path
import unittest

class Test_region_selector(unittest.TestCase):
    def file_exists(self):
        path = Path('./data/data.csv')
        assert path.is_file()
       
if(__name__ == '__main__'):
    unittest.main()