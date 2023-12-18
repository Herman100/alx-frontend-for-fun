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

    output_file = sys.argv[2]

    with open(markdown_file, 'r') as md_file:
        markdown_content = md_file.read()

    html_content = convert_headings(markdown_content)
    html_content = convert_lists(html_content)
    html_content = convert_ordered_lists(html_content)

    with open(output_file, 'w') as html_file:
        html_file.write(html_content)


def convert_headings(markdown_content):
    """
    Convert Markdown headings to HTML.
    """
    headings = [
        (r'###### (.*)', r'<h6>\1</h6>'),
        (r'##### (.*)', r'<h5>\1</h5>'),
        (r'#### (.*)', r'<h4>\1</h4>'),
        (r'### (.*)', r'<h3>\1</h3>'),
        (r'## (.*)', r'<h2>\1</h2>'),
        (r'# (.*)', r'<h1>\1</h1>')
    ]

    for markdown_pattern, html_replace in headings:
        markdown_content = re.sub(markdown_pattern,
                                  html_replace, markdown_content)

    return markdown_content


def convert_lists(markdown_content):
    """
    Convert Markdown unordered lists to HTML.
    """
    html_content = re.sub(r'^(?!\s*$)(?:- (.+)$\n?)+', r'<ul>\n\g<0></ul>',
                          markdown_content, flags=re.MULTILINE)
    html_content = re.sub(r'^- (.+)$', r'<li>\1</li>',
                          html_content, flags=re.MULTILINE)

    return html_content


def convert_ordered_lists(markdown_content):
    """
    Convert Markdown ordered lists to HTML.
    """
    html_content = re.sub(r'^(?!\s*$)(?:\* (.+)$\n?)+', r'<ol>\n\g<0></ol>',
                          markdown_content, flags=re.MULTILINE)
    html_content = re.sub(r'^\* (.+)$', r'<li>\1</li>',
                          html_content, flags=re.MULTILINE)

    return html_content


if __name__ == "__main__":
    markdown2html()
