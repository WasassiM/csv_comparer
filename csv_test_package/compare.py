from csv_test_package.csvfile import CSVFile


def compare(filename1: str, filename2: str) -> bool:
    file1 = CSVFile(filename1)
    file2 = CSVFile(filename2)

    return file1.read().equals(file2.read())
