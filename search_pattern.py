import os
import re
import sys
import chardet
from multiprocessing import Pool

# Compile regex pattern outside the loop
pattern = re.compile(sys.argv[1])

def detect_encoding(file_path):
    with open(file_path, 'rb') as f:
        rawdata = f.read(1024)  # Read the first 1024 bytes for encoding detection
    return chardet.detect(rawdata)['encoding']

def search_file(args):
    file_path, compiled_pattern = args
    found = False
    encoding = detect_encoding(file_path)
    if encoding:
        try:
            with open(file_path, 'r', encoding=encoding) as f:
                for line_number, line in enumerate(f, start=1):
                    if compiled_pattern.search(line):  # Use compiled regex pattern
                        print(f"{file_path}:{line_number}:{line.strip()}")
                        found = True
        except UnicodeDecodeError:
            pass
        except OSError:
            print(f"Could not open/read file: {file_path}")
    return found

def search_pattern(directory, compiled_pattern):
    found = False
    files_to_search = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            files_to_search.append((file_path, compiled_pattern))

    with Pool() as pool:
        results = pool.map(search_file, files_to_search)
        found = any(results)

    if not found:
        print("No matching lines found.")

if __name__ == "__main__":
    # Check if user provided a pattern
    if len(sys.argv) < 2:
        print("Usage: python search_pattern.py <pattern> [<dir>]")
        sys.exit(1)

    pattern_arg = sys.argv[1]

    # Check if directory is provided
    if len(sys.argv) == 3:
        directory_arg = sys.argv[2]
    else:
        directory_arg = '.'

    # Store the compiled regex pattern
    pattern = re.compile(pattern_arg)

    # Search for the pattern recursively in the specified directory or current directory if not specified
    search_pattern(directory_arg, pattern)
