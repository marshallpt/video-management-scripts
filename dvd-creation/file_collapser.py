import os
import re


def main():
    """
    Recursively searches sub-directors of cwd and moves all files matching extensions into cwd.

    :return:
    """
    cwd = os.getcwd()
    extensions = ['MOD', 'mpg']

    for root, dirs, files in os.walk(cwd):
        if root is not cwd:
            print(f"{root} {dirs} {files}")
            for name in files:
                for ext in extensions:
                    regex_compare = rf"\.{ext}$"
                    match = re.search(regex_compare, name)
                    if match is not None:
                        curr = os.path.join(root, name)
                        new = os.path.join(cwd, name)
                        print(f"Current: {curr} New: {new}")
                        os.rename(curr, new)


if __name__ == '__main__':
    main()
