#!/usr/bin/env python3
# *-* coding:utf-8 *-*

import argparse
import multiprocessing
import queue
import sys
import threading
import time

from helpers import file_to_list

"""

:mod:`lab_multi` -- Investigate multiprocessing / multithreading
=========================================

LAB_multi Learning Objective: Learn to use the multiprocessing and multithreading modules
                              to perform parallel tasks.
::

 a. Create set of three functions that perform the following tasks:
    1. Capitalize all strings that come through and pass them along
    2. Count the number of characters in the string and pass along the string and the count as a
       a tuple (string, count).
    3. Check to see if the count is the largest seen so far.  If so, send along a tuple with
       (string, count, True), else send (string, count, False)

 b. Spawn each of those functions into processes (multiprocessing) and wire them together
    with interprocess communications (queues).

 c. Run the entire data/dictionary2.txt file through your processing engine, one word at a time.

 d. In the main process, monitor the results coming from the last stage in the processing engine.
    After all the words have been processed, print the longest word that went through the engine.

 e. If you complete the above tasks, go back and do the same tasks using threads (threading).  Don't
    delete your multiprocessing code, just add the threading code.

"""

SOURCE_FILE_PATH = "data/dictionary2.txt"


def capitalize(in_q, out_q):
    while True:
        item = in_q.get()
        out_q.put(item.capitalize())
        in_q.task_done()


def count(in_q, out_q):
    while True:
        string = in_q.get()
        out_q.put((string, len(string)))
        in_q.task_done()


def find_largest(in_q, out_q):
    highest_len = 0
    while True:
        string, count = in_q.get()
        is_largest = False
        if count > highest_len:
            is_largest = True
            highest_len = count
        out_q.put((string, count, is_largest))
        in_q.task_done()


def get_args():
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument(
        "--threads", action="store_true", help="Use threads instead of processes"
    )
    group.add_argument(
        "--both",
        action="store_true",
        help="Run threads and processes, and display times",
    )
    args = parser.parse_args()
    return args


def get_q_and_runner(use_threads):
    return {
        True: (queue.Queue, threading.Thread),
        False: (multiprocessing.JoinableQueue, multiprocessing.Process),
    }[use_threads]


def start_proc(runner, target, in_q, out_q):
    proc = runner(target=target, args=[in_q, out_q])
    proc.daemon = True
    proc.start()
    return proc


def main(use_threads=False):
    print("Running with {}!".format({True: "threads", False: "processes"}[use_threads]))
    start_time = time.time()
    q, runner = get_q_and_runner(use_threads)
    # Initialize the queues
    start_q = q()
    cap_q = q()
    count_q = q()
    largest_q = q()

    # Initialize the processes
    capitalize_proc = start_proc(runner, capitalize, start_q, cap_q)
    count_proc = start_proc(runner, count, cap_q, count_q)
    largest_proc = start_proc(runner, find_largest, count_q, largest_q)
    spinup_time = time.time()
    print(f"Spinup time of {spinup_time - start_time} seconds")

    # fill the starting queue
    words = file_to_list(SOURCE_FILE_PATH)
    for word in words:
        start_q.put(word)
    data_load_time = time.time()
    print(f"Data load time of {data_load_time - spinup_time} seconds")

    # collect the final results and print
    largest = (None, 0, True)
    for _ in range(len(words)):
        word, length, is_largest = largest_q.get()
        if is_largest:
            largest = (word, length, is_largest)
    word, length, _ = largest
    print(f'The largest word, at {length} characters, is "{word}"!')
    print(f"Processing time of {time.time() - data_load_time} seconds")
    print(f"Completed in {time.time() - start_time} seconds.")


if __name__ == "__main__":
    args = get_args()
    if not args.both:
        main(use_threads=args.threads)
    else:
        main(use_threads=True)
        print("\n\n")
        main()
