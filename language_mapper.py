#!/usr/bin/python3

"""mapper.py"""

import json
import sys

for line in sys.stdin:
    line = line.strip()
    json_file = json.loads(line)
    for repo in json_file.values():
        language = repo['language']
        if language is None:
            continue
        print(language.replace(' ',''), 1)