"""Test of utils.py"""

import pytest

import config
import utils

def test_list_of_file_regex():
    assert utils.list_of_file_regex(config.config_store) == [
        "Asia\sProd.*",
        "NA\sProd.*",
        "NA\sPreview.*"
    ]

def test_list_of_file_regex_fail():
   assert utils.list_of_file_regex(config.bad_config) == 'missing config'


def test_file_directory_construct():
    directory = "fake/directory"
    _file = "fake.csv"
    
    assert utils.file_directory_construct(directory, _file) == "fake/directory/fake.csv"


def test_read_file():
    _file = "store/test_files/Engineering_Test_Files/NA Prod.csv"
    assert utils.read_file(_file) == [
        {'Source IP': '1.1.1.1', 'Count': '2', 'Events / Second': '0'},
        {'Source IP': '1.1.1.1', 'Count': '9028', 'Events / Second': '0'},
        {'Source IP': '2.2.2.2', 'Count': '158852820', 'Events / Second': '1839'},
        {'Source IP': '3.3.3.3', 'Count': '1028682', 'Events / Second': '12'}
    ]


def test_file_match():
    assert utils.file_match("Asia\sProd.*", "Asia Prod.csv") == "Asia Prod.csv"
