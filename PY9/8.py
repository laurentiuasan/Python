"""
Write a function that recursively scrolls a directory and displays those files whose name matches a regular expression
 given as a parameter or contains a string that matches the same expression.
 Files that satisfy both conditions will be prefixed with ">>"
"""
import re
import os


def display_files(path, regex):
    answer = []
    try:
        for root, directories, files in os.walk(path):
            for file in files:
                file_path = os.path.join(root, file)
                in_name = re.match(regex, file)
                file_contains = re.match(regex, open(file_path, "r").read())
                if in_name and file_contains:
                    answer.append(">>" + file_path)
                elif in_name or file_contains:
                    answer.append(file_path)
    except Exception as e:
        print(e)

    return answer


if __name__ == '__main__':
    check_string = r"\d+"
    print(display_files("C:\\Users\\laula\\Desktop\\Python\\PY9", check_string))
