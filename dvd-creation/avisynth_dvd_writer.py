"""AviSynth DVD Writer

Concatenates a single video file for each date footage was recorded by creating a .avs file for
each and generating a .bat file to encode them all via FFMPEG for DVD delivery.

    * modified_date - returns date file was modified
    * parse_file_list - sorts & filters file list and splits into sub-lists based on date modified
    * generate_avs_file - concatenates passed files into .avs file for each day
    * generate_bat_file - generates .bat file to ffmpeg encode all generated .avs files
"""
import datetime
import os
import re
import time


def modified_date(entry):
    """Return time file was modified."""
    return os.path.getmtime(entry)


def parse_file_list(file_list, extensions):
    """
    Sort file list by date modified, remove files not matching extensions, and sort into sub-lists
    each containing a separate modified date.

    :param file_list: list of files in the cwd
    :param extensions: list of desired file extensions in new file_list
    :return: list of DirEntry lists: each sub-list containing unique file modification date, index 0
    in each being a string of the date they were modified
    """
    trimmed_list = []
    file_list.sort(key=modified_date)

    for entry in file_list:
        for ext in extensions:
            regex_compare = rf"\.{ext}$"
            match = re.search(regex_compare, entry.name)
            if match is not None:
                trimmed_list.append(entry)

    new_list = []

    for entry in trimmed_list:
        timestamp = os.path.getmtime(entry)
        date = datetime.datetime.fromtimestamp(timestamp)
        date_recorded = f"{date.month}-{date.day}-{date.year}"

        index = len(new_list) - 1

        # If the new_list is entirely empty
        if index == -1:
            new_list.append([date_recorded])
            new_list[index+1].append(entry)

        # If the date is already added
        elif new_list[index][0] == date_recorded:
            new_list[index].append(entry)

        # If the date is new
        else:
            print("-------------------------------------------------------------")
            new_list.append([date_recorded])
            new_list[index+1].append(entry)

        print(f"{entry}, {date_recorded}, {time.ctime(timestamp)}")

    return new_list


def generate_avs_file(file_list):
    """
    Generate AviSynth files for each sublist in file_list.

    :param file_list: list of DirEntry lists : each sub-list containing unique file modification
    date, index 0 in each being a string of the date they were modified
    :return: no return value
    """
    for sublist in file_list:
        with open(f"{sublist[0]}.avs", mode="w", encoding="UTF-8") as avs_file:

            for entry in range(1, len(sublist)):
                if entry != 1:
                    avs_file.write('  ++ \\\n')
                avs_line = f'FFmpegSource2("{sublist[entry].path}", atrack = -1)'
                avs_file.write(avs_line)
        avs_file.close()


def generate_bat_file(file_list):
    """
    Generate a .bat file to use ffmpeg to encode all generated .avs files with DVD settings.

    :param file_list: list of DirEntry lists : each sub-list containing unique file modification
    date, index 0 in each being a string of the date they were modified
    :return: no return value
    """
    with open(f"encode_me.bat", mode="w", encoding="UTF-8") as batch_file:
        for entry in file_list:
            batch_line = f'ffmpeg -i {entry[0]}.avs -target ntsc-dvd -r 29.97 -s 720x480 ' \
                         f'-aspect 16:9 -b:v 8000k {entry[0]}.mpeg\n'
            batch_file.write(batch_line)
        batch_file.write('pause')
    batch_file.close()


def main():
    """Generate AviSynth scripts to concatenate each day's video files in cwd and a .bat file
    to encode them all for for DVD via ffmpeg."""
    cwd = os.getcwd()
    file_list = list(os.scandir(cwd))

    extensions = ['MOD', 'mpg']
    print(f"Operating path: {cwd}\nFiles found: ")
    file_list = parse_file_list(file_list=file_list, extensions=extensions)

    generate_avs_file(file_list=file_list)
    generate_bat_file(file_list=file_list)


if __name__ == '__main__':
    main()
