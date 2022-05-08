import os


def generate_avs_file(proj_name, file_list):
    """
    Generate an AviSynth file with the passed project name and file list.

    :param proj_name: string : file name
    :param file_list: DirEntry list : list of files to add to the AviSynth file
    :return: no return value
    """
    extension = '.mpg'
    ignored_extension = '.ffindex'
    avs_name = proj_name + '.avs'

    avs_file = open(avs_name, "w+")

    count = 0

    for entry in file_list:
        if entry.name.find(extension) != -1 and entry.name.find(ignored_extension) == -1:
            print(entry, end='')
            print(os.path.getmtime(entry))
            if count != 0:
                avs_file.write('  ++ \\\n')
            avs_line = f'FFmpegSource2("{entry.path}", atrack = -1)'
            avs_file.write(avs_line)
            count += 1
    avs_file.close()
    file_list.close()


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
    """Use the current working directory to generate a project name and file list, and then generate
    a .avs and .bat file."""
    working_directory = os.getcwd()
    split_path = working_directory.split('\\')
    file_list = os.scandir(working_directory)
    print(f"Operating path: {working_directory}\nFiles found: ")

    project_name = split_path[-1]
    generate_avs_file(proj_name=project_name, file_list=file_list)
    generate_bat_file(proj_name=project_name)


if __name__ == '__main__':
    main()
