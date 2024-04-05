import os
import pytest

from csv_compare.compare import compare


filename1 = os.path.join(os.getcwd(), "tests", "test_files", "file1.csv")
filename2 = os.path.join(os.getcwd(), "tests", "test_files", "file2.csv")
filename3 = os.path.join(os.getcwd(), "tests", "test_files", "file3.csv")

def test_compare_equal(filename1=filename1, filename2=filename2):
    assert compare(filename1, filename2)

def test_compare_no_file(filename1=filename1, filename2=""):
    with pytest.raises(FileNotFoundError):
        compare(filename1, filename2)

def test_compare_not_equal(filename1=filename1, filename2=filename3):
    assert compare(filename1, filename2) is False
