#!/usr/bin/python3
"""
This module contains a function that converts a Markdown file to HTML.
It parses Markdown headings and generates corresponding HTML.
"""

import sys
import os
import re


def markdown2html():
    """
    Convert a Markdown file to HTML.
    """
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html",
              file=sys.stderr)
        exit(1)

    markdown_file = sys.argv[1]
    if not os.path.exists(markdown_file):
        print(f"Missing {markdown_file}", file=sys.stderr)
        exit(1)

    with open(markdown_file, 'r') as f:
        lines = f.readlines()

    html_lines = []
    for line in lines:
        match = re.match(r'(#{1,6})\s(.*)', line)
        if match:
            level = len(match.group(1))
            content = match.group(2)
            html_lines.append(f'<h{level}>{content}</h{level}>')


if __name__ == "__main__":
    markdown2html()
