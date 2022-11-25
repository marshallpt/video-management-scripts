import argparse
import shutil
import re
from datetime import datetime as dt


def output_name(file_name):
    """Parse the original name and return a modified one."""
    file_list = file_name.split('.')
    new_file_name = "".join(file_list[0:-1]) + f"_italics_fixed.{file_list[-1]}"

    return new_file_name

def parse_file(input_file, output_file):
    pattern = r"<\/i>( {0,2}.{1} {0,2})<i>|<i>( {0,2}.{1} {0,2})<\/i>"

    with open(input_file, mode="r") as input:
        with open(output_file, mode="w", encoding="UTF-8") as output:
            for line in input:
                match = re.search(pattern,line)
                match_iter = re.finditer(pattern,line)
                if not match:
                    output.write(line)
                else:
                    match_body = line[match.start():match.end()]

                    beginning = line[:match.start()]
                    middle = match_body.replace('<i>',"").replace('</i>',"").strip()
                    end = line[match.end():]
                    new_line = beginning + middle + end
                    print("-------------------------------------")
                    # print(f"Modifying : {line}With: {beginning=} {middle=} {end=}")
                    print(f"Modifying : {line}With: {new_line}")
                    output.write(new_line)

def main():
    parser = argparse.ArgumentParser(description="Simulation L1 cache.",
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    
    parser.add_argument("file_name", default="example.srt", nargs='?', 
                        help="Subtitle file name to parse.")
    args = parser.parse_args()

    file_name = output_name(args.file_name)
    parse_file(input_file=args.file_name, output_file=file_name)


if __name__ == '__main__':
    main()
