import os
import pytest
from csv_compare.csvfile import CSVFile


def test_no_file():
    filepath = "toto"

    with pytest.raises(FileNotFoundError):
        file = CSVFile(filepath)


filename = os.path.join(os.getcwd(), "tests", "test_files", "file1.csv")


def test_read(filename=filename):
    file = CSVFile(filename)

    assert file.read() is not None
