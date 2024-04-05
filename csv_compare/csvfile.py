import os
from pandas import read_csv, DataFrame


class CSVFile:

    def __init__(self, filepath: str):
        if not os.path.exists(filepath):
            raise FileNotFoundError
        self.filename = filepath

    def read(self) -> "DataFrame":
        return read_csv(self.filename)
