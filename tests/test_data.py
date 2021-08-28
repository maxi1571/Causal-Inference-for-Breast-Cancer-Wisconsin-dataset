from pathlib import Path
import pandas as pd
import unittest
import sys
sys.path.append("../")
class Test_file(unittest.TestCase):
    def file_exists(self):
        path = Path('../data/data.csv')
        assert path.is_file()


    def test_diagnosis_col(self):
        df = pd.read_csv("data/data.csv")
        assert df['diagnosis'].isin(["B","M"]).all() == True
       
if(__name__ == '__main__'):
    unittest.main()
    