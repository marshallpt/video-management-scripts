import argparse
import shutil
import re
from datetime import datetime as dt


def make_new_file(file_name):
    """Make a copy of the original file and return the path to it."""
    file_list = file_name.split('.')
    new_file_name = "".join(file_list[0:-1]) + f"_fixed_italics.{file_list[-1]}"

    shutil.copy(file_name, new_file_name)
    return new_file_name

def parse_file(input_file, output_file):
     with open(input_file, mode="r") as input:
            with open(output_file, mode="w", encoding="UTF-8") as output:
                for line in input:
                    output.write(line)

def main():
    parser = argparse.ArgumentParser(description="Simulation L1 cache.",
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    
    parser.add_argument("file_name", default="example.srt", nargs='?', 
                        help="Subtitle file name to parse.")
    args = parser.parse_args()

    file_name = make_new_file(args.file_name)
    parse_file(input_file=file_name, output_file="burgah.srt")


if __name__ == '__main__':
    main()
