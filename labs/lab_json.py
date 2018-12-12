#!/usr/bin/env python3
# *-* coding:utf-8 *-*

import argparse
import json

import yaml

"""
:mod:`lab_json` -- JSON to YAML and back again
=========================================

LAB_JSON Learning Objective: Learn to navigate a JSON file and convert to a
                             python object.
::

 a. Create a script that expects 3 command line arguments: -j or -y, json_filename, yaml_filename
    The first argument is -j or -y based on whether to convert from JSON to YAML (-j) or
    YAML to JSON (-y)
    The second argument is the name of the json file to parse or save to
    The third argument is the name of the yaml file to parse or save to

 b. Based on the -y/-j selection, parse the contents of the input file using the appropriate
    library.

 c. Using the other library, save the parsed object to the output filename

 d. Test your script using the json and yml files in the data directory.

 e. If you have time, create your own JSON and YAML files and translate between the formats.

"""


def get_args():
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-j", action="store_true", dest="from_json")
    group.add_argument("-y", action="store_false", dest="from_json")
    parser.add_argument("json_filename")
    parser.add_argument("yaml_filename")
    args = parser.parse_args()
    return args


def get_file_handlers(from_json):
    return {
        True: (json.loads, lambda x: yaml.dump(x, default_flow_style=False)),
        False: (yaml.load, json.dumps),
    }[from_json]


def main():
    args = get_args()
    deserialize, serialize = get_file_handlers(args.from_json)
    if args.from_json:
        in_file, out_file = args.json_filename, args.yaml_filename
    else:
        in_file, out_file = args.yaml_filename, args.json_filename

    with open(in_file) as f:
        data = deserialize(f.read())

    with open(out_file, 'w') as f:
        f.write(serialize(data))


if __name__ == "__main__":
    main()
