import argparse
import sys

def parse_args():
    """Simple program to shuffle text paragraphs (big files too)
    :return: argument parser instance
    """

    parser = argparse.ArgumentParser(
        prog="Simple program to shuffle text paragraphs",
        description="Randomly shuffle paragraphs in input file")

    parser.add_argument('--input_file', nargs='?', default='paragraphs.txt',
                        help='input text file')
    parser.add_argument('--output_file', nargs='?', default=None,
                        help='output file, use stdout if not provided')

    return parser.parse_args()