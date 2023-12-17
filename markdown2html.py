#!/usr/bin/python3
"""
This module contains a function that converts a Markdown file to HTML.
"""

import sys
import os


def markdown2html():
    """
    Convert a Markdown file to HTML.
    """
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        exit(1)

    markdown_file = sys.argv[1]
    if not os.path.exists(markdown_file):
        print(f"Missing {markdown_file}", file=sys.stderr)
        exit(1)

    # Your code to convert markdown to html goes here


if __name__ == "__main__":
    markdown2html()
