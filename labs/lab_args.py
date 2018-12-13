#!/usr/bin/env python3
# *-* coding:utf-8 *-*

"""

:mod:`lab_args` -- Arguing with the functions
=========================================

LAB_ARGS Learning Objective: Learn to modify, receive, and work with arguments to function.
::

 a. Create a function that accepts any number of positional arguments and
    keyword arguments and prints the argument values out to the screen.

 b. Create a function that takes in any number of positional arguments, turns
    those arguments into keyword arguments using "arg#" for the keyword names,
    and calls the print function you wrote in a.

 c. Write a validation function that takes in a variable number of positional
    arguments.  Validate that all the arguments passed in are integers and are
    greater than 0.  If the arguments validate, call the print function, if an
    argument doesn't validate raise a ValueError.

"""


def print_args(*args, **kwargs):
    if args:
        print("Arg values are:\n\t" + '\n\t'.join([f"{x}" for x in args]))
    if kwargs:
        print("Kwarg values are:\n\t" + "\n\t".join([f"{k}: {v}" for k, v in kwargs.items()]))


def key_the_pos(*args):
    print_args(**{f"arg{i}": v for i, v in enumerate(args)})


def _is_pos_int(value):
    return isinstance(value, int) and value > 0


def validate_the_pos(*args):
    if not all([_is_pos_int(x) for x in args]):
        raise ValueError(f"Not all args were integers greater than zero: {args}")
    print_args(*args)


def test_validate_failure(*args):
    try:
        validate_the_pos(*args)
    except ValueError as e:
        print(f"Expected ValueError was raised: {e}")
    else:
        print(f"Oops! These args should have raised a ValueError: {args}")


if __name__ == "__main__":
    validate_the_pos(3, 5, 6, 7, 1, 12)
    test_validate_failure("a", 3, 5, 6)
    test_validate_failure(1, 2, 3, -5)
