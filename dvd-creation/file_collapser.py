import os
import re


def main():
    """
    Recursively searches sub-directors of cwd and moves all files matching extensions into cwd.

    :return:
    """
    cwd = os.getcwd()
    extensions = ['MOD', 'mpg']

    # Looking for sub-directories, not our cwd
    for root, dirs, files in os.walk(cwd):
        if root is not cwd:
            for name in files:
                # Checking to see if it's a file we care about
                for ext in extensions:
                    regex_compare = rf"\.{ext}$"
                    match = re.search(regex_compare, name)
                    # If the file has an extension we're looking for
                    if match is not None:
                        curr = os.path.join(root, name)
                        new = os.path.join(cwd, name)
                        print(f"Current: {curr} New: {new}")

                        count = 0
                        while True:
                            # Attempt to rename the file
                            try:
                                os.rename(curr, new)
                            # If a file with that name already exists, append a number to it
                            except FileExistsError:
                                count += 1
                                old_name = name
                                name_split = name.split('.')
                                new_name = ""
                                for x in range(0, len(name_split)-1):
                                    # Accounting for the fact that some file names may contain `.`
                                    if x is len(name_split)-2:
                                        new_name += name_split[x]
                                    else:
                                        new_name += f"{name_split[x]}."
                                new_name += f"_{count}.{name_split[-1]}"
                                new = os.path.join(cwd, new_name)
                            # Rename has succeeded, exit the loop
                            else:
                                break


if __name__ == '__main__':
    main()
