#!/usr/bin/python3

"""
This module contains a function that converts a Markdown file to HTML.
It parses Markdown headings and generates corresponding HTML.
"""
import sys
import os.path
import re
import hashlib

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('Usage: ./markdown2html.py README.md README.html',
              file=sys.stderr)
        exit(1)

    if not os.path.isfile(sys.argv[1]):
        print('Missing {}'.format(sys.argv[1]), file=sys.stderr)
        exit(1)

    with open(sys.argv[1]) as f:
        with open(sys.argv[2], 'w') as md_ml:
            ulist, olist, p_tag = False, False, False

            for text in f:
                text = text.replace('**', '<b>', 1)
                text = text.replace('**', '</b>', 1)
                text = text.replace('__', '<em>', 1)
                text = text.replace('__', '</em>', 1)

                md5 = re.findall(r'\[\[.+?\]\]', text)
                md5_inside = re.findall(r'\[\[(.+?)\]\]', text)
                if md5:
                    text = text.replace(md5[0], hashlib.md5(
                        md5_inside[0].encode()).hexdigest())

                rm_c = re.findall(r'\(\(.+?\)\)', text)
                rm_cs = re.findall(r'\(\((.+?)\)\)', text)
                if rm_c:
                    rm_cs = ''.join(
                        c for c in rm_cs[0] if c not in 'Cc')
                    text = text.replace(rm_c[0], rm_cs)

                text_len = len(text)
                headers = text.lstrip('#')
                h_levels = text_len - len(headers)
                ul = text.lstrip('-')
                ul_number = text_len - len(ul)
                ol = text.lstrip('*')
                ol_number = text_len - len(ol)

                if 1 <= h_levels <= 6:
                    text = '<h{}>'.format(
                        h_levels) + headers.strip() + '</h{}>\n'.format(
                        h_levels)

                if ul_number:
                    if not ulist:
                        md_ml.write('<ul>\n')
                        ulist = True
                    text = '<li>' + ul.strip() + '</li>\n'
                if ulist and not ul_number:
                    md_ml.write('</ul>\n')
                    ulist = False

                if ol_number:
                    if not olist:
                        md_ml.write('<ol>\n')
                        olist = True
                    text = '<li>' + ol.strip() + '</li>\n'
                if olist and not ol_number:
                    md_ml.write('</ol>\n')
                    olist = False

                if not (h_levels or ulist or olist):
                    if not p_tag and text_len > 1:
                        md_ml.write('<p>\n')
                        p_tag = True
                    elif text_len > 1:
                        md_ml.write('<br/>\n')
                    elif p_tag:
                        md_ml.write('</p>\n')
                        p_tag = False

                if text_len > 1:
                    md_ml.write(text)

            if ulist:
                md_ml.write('</ul>\n')
            if olist:
                md_ml.write('</ol>\n')
            if p_tag:
                md_ml.write('</p>\n')
    exit(0)
