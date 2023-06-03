import os
import re

def find_uuids(text):
    uuid_pattern = r'[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}'
    uuids = re.findall(uuid_pattern, text, re.I)
    return uuids

def print_uuids_in_file(filename):
    with open(filename, 'r') as file:
        for line_number, line in enumerate(file, start=1):
            uuids = find_uuids(line)
            for uuid in uuids:
                print(f'Line {line_number}: {uuid}')

filePath = os.path.join(os.getcwd(), '26.json')
print_uuids_in_file(filePath)
