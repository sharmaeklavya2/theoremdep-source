#!/usr/bin/env python3

from __future__ import print_function

import sys
import os
import argparse


TEMPLATE = """{
    "deps": [
    ],
    "metadata": {
        "type": "theorem",
        "title": "",
        "description": ""
    },
    "document": {
        "type": "include",
        "path": "$path$"
    }
}
"""


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('path')
    args = parser.parse_args()
    path = args.path

    if path.startswith('nodes'):
        path = path[5:]
    if path.endswith('.json'):
        path = path[:-5]
    if path.startswith('/'):
        path = path[1:]

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    json_path = os.path.relpath(os.path.join(BASE_DIR, 'nodes', path + '.json'))
    md_path = '/{}.md'.format(path)
    md_path2 = os.path.relpath(os.path.join(BASE_DIR, 'includes', path + '.md'))

    if os.path.exists(json_path):
        print('File', repr(json_path), 'already exists.', file=sys.stderr)
        sys.exit(1)

    with open(json_path, 'w') as fp:
        fp.write(TEMPLATE.replace('$path$', md_path))
    with open(md_path2, 'a') as fp:
        pass


if __name__ == '__main__':
    main()
