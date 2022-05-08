import os
import re


def sort_by_modified_date(entry):
    """Return time file was modified."""
    return os.path.getmtime(entry)


def parse_file_list(file_list, extensions):
    """
    Sort file list by date modified and return list only containing passed extensions.

    :param file_list: list of files in the cwd
    :param extensions: list of desired file extensions in new file_list
    :return: sorted & pruned file_list
    """
    new_list = []
    file_list.sort(key=sort_by_modified_date)

    for entry in file_list:
        for x in extensions:
            regex_compare = f"\.{x}$"
            match = re.search(regex_compare, entry.name)
            if match is not None:
                new_list.append(entry)

    return new_list


def generate_avs_file(proj_name, file_list):
    """
    Generate an AviSynth file with the passed project name and file list.

    :param proj_name: string : file name
    :param file_list: DirEntry list : list of files to add to the AviSynth file
    :return: no return value
    """
    avs_file = open(f"{proj_name}.avs", "w+")
    count = 0

    for entry in file_list:
        print(f"{entry}, {os.path.getmtime(entry)}")
        if count != 0:
            avs_file.write('  ++ \\\n')
        avs_line = f'FFmpegSource2("{entry.path}", atrack = -1)'
        avs_file.write(avs_line)
        count += 1
    avs_file.close()


def generate_bat_file(proj_name):
    """
    Generate a .bat file to use ffmpeg to encode the generated proj_name.avs file with DVD settings

    :param proj_name: string : name of .avs file to point new .bat file to
    :return: no return value
    """
    batch_file = open(f"{proj_name}.bat", "w+")
    batch_line = f'ffmpeg -i {proj_name}.avs -target ntsc-dvd -r 29.97 -s 720x480 -aspect 16:9 -b:v 8000k ' \
                 f'{proj_name}.mpeg \npause'
    batch_file.write(batch_line)
    batch_file.close()


def main():
    """Generate an AviSynth script to concatenate all video files in cwd, as well as a .bat file
    to encode it for DVD via ffmpeg."""
    cwd = os.getcwd()
    split_path = cwd.split('\\')
    file_list = list(os.scandir(cwd))

    extensions = ['MOD', 'mpg']
    proj_name = split_path[-1]
    file_list = parse_file_list(file_list=file_list, extensions=extensions)

    print(f"Operating path: {cwd}\nFiles found: ")
    generate_avs_file(proj_name=proj_name, file_list=file_list)
    generate_bat_file(proj_name=proj_name)


if __name__ == '__main__':
    main()
