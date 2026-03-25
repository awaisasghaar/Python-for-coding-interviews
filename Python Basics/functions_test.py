import pytest
from functions import sheet, percentage, total_subject_marks

def test_integer_sheet():
    subjects = {'Maths': 88, 'Computer Science': 52, 'English': 65}
    assert sheet, subjects['Maths'] == 88
    assert sheet, subjects['Computer Science'] == 52
    assert sheet, subjects['English'] == 65

def test_percentage():
    assert percentage(230) == 'Grade B+ (Pass)'
    assert percentage(143) == 'Fail'
    assert percentage(250) == 'Grade A (Pass)'

def test_total_subject_marks():
    subjects = {'Maths': 88, 'Computer Science': 52, 'English': 65}
    assert total_subject_marks(subjects) == 205

def test_total_subject_marks_zaro():
    subjects = {'Maths': 0, 'Computer Science': 0, 'English': 0}
    assert total_subject_marks(subjects) == 0








