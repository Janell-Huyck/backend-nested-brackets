#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Module docstring: Determines if brackets in strings are properly nested

Reads a series of strings in lines from input.txt.  Evaluates each
line to determine if the brackets in it are properly nested.  Acceptable
brackets are: () [] {} <> and (* *). (*) is read as (* followed by ).
Writes to output.txt either YES or NO followed by the index of where the
error is at.  (* and *) are counted as one character for error
indexing purposes.

This program from the third week of the third quarter at Kenzie Academy,
where Python is first being introduced.
"""
__author__ = "Janell.Huyck"

import sys
if sys.version_info[0] >= 3:
    raise Exception("This program requires python2 interpreter")


def is_nested(line):
    l_paren_vals = ["(*", "(", "[", "{", "<"]
    r_paren_vals = ["*)", ")", "]", "}", ">"]
    left_stack = []
    index = 0

    while line:
        token = line[0]
        index += 1
        for paren in l_paren_vals:
            if line.startswith(paren):
                token = paren
                left_stack.append(token)
                break
        for paren in r_paren_vals:
            if line.startswith(paren):
                token = paren
                if len(left_stack) == 0:
                    return "NO " + str(index)
                if r_paren_vals.index(paren) ==\
                        l_paren_vals.index(left_stack[-1]):
                    left_stack.pop()
                    break
                else:
                    return "NO " + str(index)
        line = line[len(token):]

    if len(left_stack) == 0:
        return "YES"
    else:
        return "NO " + str(index)


def main(args):
    with open('input.txt', 'r') as input_file:
        with open('output.txt', 'w') as output_file:
            for line in input_file:
                line_validation = is_nested(line)
                output_file.write(line_validation + "\n")
                print(line_validation)


if __name__ == '__main__':
    main(sys.argv[1:])
