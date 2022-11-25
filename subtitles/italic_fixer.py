import argparse
import shutil
import re
from datetime import datetime as dt


def output_name(file_name):
    """Parse the original name and return a modified one."""
    file_list = file_name.split('.')
    new_file_name = "".join(file_list[0:-1]) + f"_italics_fixed.{file_list[-1]}"

    return new_file_name

def fix_middle(line, count):
    pattern = r"<\/i>( {0,2}.{1} {0,2})<i>|<i>( {0,2}.{1} {0,2})<\/i>"
    match = re.search(pattern,line)
    while match:
        count +=1
        match_body = line[match.start():match.end()]

        beginning = line[:match.start()]
        middle = match_body.replace('<i>',"").replace('</i>',"").strip()
        end = line[match.end():]
        line = beginning + middle + end
        match = re.search(pattern,line)
        # print(f"Modifying : {line}With: {beginning=} {middle=} {end=}")
    return line, count

def fix_beginning(line, count):
    pattern = r"^(.){1,4}<i>"
    match = re.search(pattern,line)
    while match:
        count +=1
        beginning = '<i>'
        middle = line[:match.end()-3]
        end = line[match.end():]
        line = beginning + middle + end
        match = re.search(pattern,line)
    return line, count

def parse_file(input_file, output_file):
    with open(input_file, mode="r") as input:
        with open(output_file, mode="w", encoding="UTF-8") as output:
            for line in input:
                count = 0
                old_line = line
                line, count = fix_middle(line, count)
                # line, count = fix_beginning(line, count)
                if count != 0:
                    print("-------------------------------------")
                    print(f"""{'Modifying' : <15}: {old_line : >30}"""
                          f"""{f'With ({count} fixes)': <15}: {line : >30}""")
                output.write(line)
                    

def main():
    parser = argparse.ArgumentParser(description="Simulation L1 cache.",
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    
    parser.add_argument("file_name", default="example.srt", nargs='?', 
                        help="Subtitle file name to parse.")
    parser.add_argument("-o", "--output_file",
                        help="Output file name.")
    args = parser.parse_args()
    
    if args.output_file is not None:
        file_name = args.output_file
    else:
        file_name = output_name(args.file_name)
    parse_file(input_file=args.file_name, output_file=file_name)


if __name__ == '__main__':
    main()
