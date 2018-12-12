#!/usr/bin/env python3
# *-* coding:utf-8 *-*

import yaml

"""

:mod:`lab_yaml` -- YAML Parsing
=========================================

LAB_YAML Learning Objective: Learn to parse a YAML file using the PyYAML library
                             and use the information.
::

 a. Load the data/widget.yml file using the PyYAML library.

 b. Change the value for the width and height of the window element to be 1/2 their current value.
    Change the size of the text element to be 1/4 it's current value.
    Change the image alignment element to 'justified'.

 c. Save your updated object to widget_updated.yaml using the PyYAML library.

"""

YAML_SOURCE_PATH = 'data/widget.yml'
YAML_TARGET_PATH = 'data/widget_updated.yml'


def read_yaml(path):
    with open(path) as f:
        return yaml.load(f.read())


def write_yaml(data, path):
    with open(path, 'w') as f:
        f.write(yaml.dump(data, default_flow_style=False))


def main():
    data = read_yaml(YAML_SOURCE_PATH)

    widget = data['widget']
    widget['window']['height'] //= 2
    widget['window']['width'] //= 2
    widget['text']['size'] //= 4
    widget['image']['alignment'] = 'justified'

    write_yaml(data, YAML_TARGET_PATH)


if __name__ == '__main__':
    main()
