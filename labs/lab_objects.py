#!/usr/bin/env python3
# *-* coding:utf-8 *-*

"""

:mod:`lab_objects` -- Objects in Python
=========================================

LAB Objects Learning Objective: Explore objects in Python and how everything in Python
                                is an object.

a. Fill in the series of functions below that determine the characteristics of an object.

b. Write a print_object_flags function that uses the is_* functions to find the characteristics
   of the passed in object and print the characteristics (flags).

"""

from pathlib import Path


def _check_attrs(obj, *attrs):
    return all([hasattr(obj, f"__{x}__") for x in attrs])


def is_callable(obj):
    """ returns True if the object is callable """
    return _check_attrs(obj, 'call')


def is_with(obj):
    """ returns True if the object can be used in a "with" context """
    return _check_attrs(obj, 'enter', 'exit')


def is_math(obj):
    """ returns True if the object supports +, -, /, and * """
    return _check_attrs(obj, 'add', 'sub', 'mul', 'truediv')


def is_iterable(obj):
    """ returns True if the object is iterable """
    return _check_attrs(obj, 'iter')


FLAGS_TO_CHECK = {
    "callable": is_callable,
    "with": is_with,
    "math": is_math,
    "iterable": is_iterable,
}


def print_object_flags(obj):
    """ assess the object for various characteristics and print them """
    obj_name = obj.__class__.__name__
    print(
        f'"{obj_name}" Object Properties:\n\t'
        + "\n\t".join(f"{k}: {f(obj)}" for k, f in FLAGS_TO_CHECK.items())
    )


if __name__ == "__main__":
    print_object_flags(1)
    print_object_flags("abc")
    print_object_flags(print_object_flags)
    print_object_flags([1, 2, 3])
    test_file_path = "test.file.deleteme"
    print_object_flags(open(test_file_path, "w"))
    Path(test_file_path).unlink()
