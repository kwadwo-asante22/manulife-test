"""main"""

import csv

from config import config_store
from config import COMBINED_CSV
from config import FILE_DIRECTORY
from message import sample_message
import utils


def main():
    combined_csv_content = [records for records in gather()]

    keys = combined_csv_content[0].keys()

    with open(COMBINED_CSV, 'w', newline='') as output_file:
       dict_writer = csv.DictWriter(output_file, keys)
       dict_writer.writeheader()
       dict_writer.writerows(combined_csv_content)

def worker():
    """Convert the acquired file into a generator."""
    
    # Collect all the regular expressions represent a file
    # within the configuration store
    list_file_regex = utils.list_of_file_regex(config_store)

    # Check to see if the file exists within the message
    file_exist = utils.file_match(list_file_regex, sample_message['file_name'])

    environment = (' ').join(file_exist.split('.')[0].split(' ')[:2])

    if file_exist:
        incoming_file = utils.read_file(utils.file_directory_construct(
            FILE_DIRECTORY, sample_message['file_name']
        ))

    for inp in incoming_file:
        yield {
            'Source IP': inp['Source IP'],
            'Environment': environment
        }

def gather():
    """Combine the generated acquisition file and the current combined file."""

    _file = [record for record in worker()]

    # Get combined file
    combined_file = utils.read_file(COMBINED_CSV)

    combine = combined_file + _file
    
    # Using a generator because currently file is bound to grow
    # memory saver
    for records in combine:
        yield {
            'Source IP': records['Source IP'],
            'Environment': records['Environment']
        }

main()
