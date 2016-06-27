#!/usr/bin/env python

import re
import os
import sys
import argparse


DESCRIPTION = 'A script to rename batches of files using regexes.'


# Command line arguments
def construct_parser(parser):
    # Positional arguments
    parser.add_argument('match_regex',
        type=str,
        help='The regex to use for matching files.')
    
    parser.add_argument('rename_regex',
        type=str,
        help='The regex to use for renaming files.')
    
    parser.add_argument('files',
        type=str,
        nargs='+',
        help='The files to rename.')
    
    # Optional arguments
    parser.add_argument('-f', '--full',
        type=int,
        help='Only rename files that the regex fully matches.')


def mvr(argv):
    parser = argparse.ArgumentParser(description=DESCRIPTION)
    construct_parser(parser)
    args = parser.parse_args(sys.argv[1:])
    
    new_files = []
    
    if args.full:
        args.match_regex = re.sub('^{0}$'.format(args.match_regex))
    
    for f in args.files:
        new_files.append(
            re.sub(args.match_regex, args.rename_regex, f)
        )
    
    
    # Check for collisions
    test_set = set(new_files)
    if len(new_files) > len(test_set):
        print('Collision exists in new file names. Aborting...')
        exit(1)
    
    # Rename the files
    for old, new in zip(args.files, new_files):
        if old == new:
            continue
        
        print('"{0}" => "{1}"'.format(old, new))
        os.rename(old, new)

# Main method
if __name__ == '__main__':
    mvr(sys.argv[1:])
