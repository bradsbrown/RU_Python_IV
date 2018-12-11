#!/usr/bin/env python3
# *-* coding:utf-8 *-*

import subprocess

from helpers import print_step

"""

:mod:`lab_subprocess` -- subprocess module
============================================

LAB subprocess Learning Objective: Familiarization with subprocess

::

 a. Use the subprocess run function to run "ls -l" and print the output.

 b. Do the same as a), but don't print anything to the screen.

 c. Do the same as a), but run the command "/bogus/command". What happens?

 d. Use subprocess run function to run "du -h" and output stdout to a pipe. Read the pipe
    and print the output.

 e. Create a new function commander() which takes in a list of commands to execute
    (as strings) on the arg list, then runs them sequentially printing stdout.

"""

def run_print(cmd):
    proc = subprocess.run(cmd.split())


def run_no_print(cmd):
    subprocess.run(cmd.split(), stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


def run_return_out(cmd):
    proc = subprocess.run(cmd.split(), stdout=subprocess.PIPE)
    return proc.stdout.decode()


def commander(*commands):
    for command in commands:
        run_print(command)


COMMANDS = [
    'ls -al',
    'df -h',
    'mount',
    'who',
    'whoami'
]


def main():
    # Step a
    print_step("A")
    run_print('ls -l')

    # Step b
    print_step("B")
    run_no_print('ls -l')

    # Step c
    print_step("C")
    try:
        run_no_print('/bogus/command')
    except OSError as e:
        print('(error occured)')
        print(e)

    # Step d
    print_step("D")
    print(run_return_out('du -h'))

    # Step e
    print_step("E")
    commander(*COMMANDS)


if __name__ == "__main__":
    main()
