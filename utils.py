"""Utility"""

import re
import csv
from typing import Any, Dict, List, Union


def list_of_file_regex(_config: Dict[str, Any]) -> Union[List[str], str]:
    """read the config and parse details"""
    if _config:
        return [items["file_regex"] for items in _config.get("data")]
    else:
        return 'missing config'


def file_match(regex: List[str], _file: str) -> str:
    """Find the targeted file(s)"""
    for file_regex in regex:
        if re.search(file_regex, _file) :
            return _file


# in reality there will be a function to check if file exists 
def file_directory_construct(file_directory: str, _file: str) -> bool:
    """check if the file exists"""
    directory = [file_directory, _file]
    return "/".join(directory)


def read_file(file: str) -> Dict[str, Any]:
    """Read file as a dcitionary"""
    with open(file, mode='r', encoding='utf-8-sig') as f:
        reader = csv.reader(f)
        headers = next(reader)
        return [dict(zip(headers, row)) for row in reader]
