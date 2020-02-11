#!/usr/bin/env python
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

# read input line by line from input.txt
#   on each line, run the tests and then write/append to output.txt

# Types of brackets:
#     ()
#     []
#     {}
#     < >
#     (* *)
# The combination `(*)` should be interpreted as `(*` followed by `)`.
# `(*` and `*)`count as one for the error space


# change the input string into a list of single characters
# need to include whitespace.

# iterate through that list and merge the (* and *) elements

# make a "stack" list of all brackets, going left to right in the string

# if a bracket is a left symbol, add it to the list.

# if a bracket is a right symbol, compare it to the last item in the list.
# it must be the complement.  If it is, delete the bracket from the list.
# if it is not the complement, we have an error.  proceed to finding the
# location of the error.

# finding error location:
# make a counter for the merged (* array to show what character we are
# currently evaluating

# write output to output.txt - line by line
#
# The output is a textfile named `output.txt`.
# Each line contains the result of the check of the corresponding
# inputline, that is ‘YES’ (in upper case), if the expression is OK,
# and (if it is not OK) ‘NO’ followed by a space and the
# position of the error.


def is_nested(line):
    line = make_formatted_line(line)
    print (line)
    return "Hello"
    """Validate a single input line for correct nesting"""


def make_formatted_line(line):
    line = [character for character in line]
    formatted_line = []
    skip = False
    for character_index in range(0, len(line)):
        if skip is True:
            skip = False
            continue
        if character_index == len(line)-1:
            formatted_line += [(line[character_index])]
        elif line[character_index] != "(" and line[character_index] != "*":
            formatted_line += [(line[character_index])]
        elif line[character_index] == "(" and line[character_index + 1] == "*":
            skip = True
            formatted_line += [("(*")]
        elif line[character_index] == "(" and line[character_index + 1] != "*":
            formatted_line += [(line[character_index])]
        elif line[character_index] == "*" and line[character_index + 1] == ")":
            skip = True
            formatted_line += [("*)")]
        elif line[character_index] == "*" and line[character_index + 1] != ")":
            formatted_line += [(line[character_index])]
        else:
            print ("I goofed up somewhere in the parsing of the line.")
    return formatted_line

    print (line)


def main(args):
    with open('input.txt', 'r') as input_file:
        with open('output.txt', 'w') as output_file:
            for line in input_file:
                line_validation = is_nested(line)
                output_file.write(line_validation + "\n")
                print(line_validation + "\n")


if __name__ == '__main__':
    main(sys.argv[1:])
