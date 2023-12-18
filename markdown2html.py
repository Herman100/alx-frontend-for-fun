#!/usr/bin/python3

"""
This module contains a function that converts a Markdown file to HTML.
It parses Markdown headings and generates corresponding HTML.
"""
import sys
import os.path
import re
import hashlib

def usage_error():
    """Prints usage error message and exits."""
    print('Usage: ./markdown2html.py README.md README.html', file=sys.stderr)
    exit(1)

def file_error(file_path):
    """Prints file error message and exits."""
    print(f'Missing {file_path}', file=sys.stderr)
    exit(1)

def replace_syntax(line):
    """Replaces Markdown syntax with HTML tags."""
    line = line.replace('**', '<b>', 1)
    line = line.replace('**', '</b>', 1)
    line = line.replace('__', '<em>', 1)
    line = line.replace('__', '</em>', 1)
    return line

def md5_replacement(line):
    """Replaces MD5 syntax with hashed values."""
    md5 = re.findall(r'\[\[.+?\]\]', line)
    md5_inside = re.findall(r'\[\[(.+?)\]\]', line)
    if md5:
        line = line.replace(md5[0], hashlib.md5(md5_inside[0].encode()).hexdigest())
    return line

def remove_letter_c(line):
    """Removes 'C' or 'c' within double parenthesis."""
    remove_letter_c = re.findall(r'\(\(.+?\)\)', line)
    remove_c_more = re.findall(r'\(\((.+?)\)\)', line)
    if remove_letter_c:
        remove_c_more = ''.join(c for c in remove_c_more[0] if c not in 'Cc')
        line = line.replace(remove_letter_c[0], remove_c_more)
    return line

def convert_to_html(input_file, output_file):
    """Converts Markdown content to HTML."""
    with open(input_file) as read:
        with open(output_file, 'w') as html:
            unordered_start, ordered_start, paragraph = False, False, False
            for line in read:
                line = replace_syntax(line)
                line = md5_replacement(line)
                line = remove_letter_c(line)

                length = len(line)
                headings = line.lstrip('#')
                heading_num = length - len(headings)
                unordered = line.lstrip('-')
                unordered_num = length - len(unordered)
                ordered = line.lstrip('*')
                ordered_num = length - len(ordered)

                # ... (rest of the code remains the same)

if __name__ == '__main__':
    if len(sys.argv) < 3:
        usage_error()

    if not os.path.isfile(sys.argv[1]):
        file_error(sys.argv[1])

    convert_to_html(sys.argv[1], sys.argv[2])
    exit(0)

