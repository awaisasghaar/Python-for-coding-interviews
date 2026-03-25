import pytest
from functions import sheet, percentage

def test_integer_sheet():
    subjects = {'Maths': 88, 'Computer Science': 52, 'English': 65}
    assert sheet, subjects['Maths'] == 88
    assert sheet, subjects['Computer Science'] == 52
    assert sheet, subjects['English'] == 65

def test_percentage():
    assert percentage(230) == 'Grade B+ (Pass)'
    assert percentage(143) == 'Fail'




