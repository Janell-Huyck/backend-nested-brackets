#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Module docstring: Determines if brackets in strings are properly nested

Reads a series of strings in lines from input.txt.  Evaluates each
line to determine if the brackets in it are properly nested.  Acceptable
brackets are: () [] {} <> and (* *). (*) is read as (* followed by ).
Writes to output.txt either YES or NO followed by the length of the
string prior to the error.  (* and *) are counted as one character for this.

This program from the third week of the third quarter at Kenzie Academy,
where Python is first being introduced.
"""
__author__ = "Janell.Huyck with help from madarp"

import sys
if sys.version_info[0] >= 3:
    raise Exception("This program requires python2 interpreter")

l_paren_vals = ["(*", "(", "[", "{", "<"]
r_paren_vals = ["*)", ")", "]", "}", ">"]


def check_bracket_nesting(line):
    left_stack = []
    count = 1

    def check_left_parentheses(token, left_stack):
        if not line:
            return token
        for paren in l_paren_vals:
            if line.startswith(paren):
                token = paren
                left_stack.append(token)
                break
        return token

    def check_right_parentheses(token):
        if not line:
            return token
        for paren in r_paren_vals:
            if line.startswith(paren):
                token = paren
                if not left_stack or l_paren_vals.index(left_stack.pop()) !=\
                        r_paren_vals.index(paren):
                    return "NO"
                break
        return token

    while line:
        token = line[0]
        token = check_left_parentheses(token, left_stack)
        token = check_right_parentheses(token)
        if token == "NO":
            return "NO " + str(count)
        count += 1
        line = line[len(token):]

    if not left_stack:
        return "YES"
    else:
        return "NO " + str(count - 1)


def main(args):
    with open('input.txt', 'r') as input_file:
        with open('output.txt', 'w') as output_file:
            for line in input_file:
                line_validation = check_bracket_nesting(line)
                output_file.write(line_validation + "\n")
                print(line_validation)


if __name__ == '__main__':
    main(sys.argv[1:])
