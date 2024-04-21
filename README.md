# Pattern Search Tool

This Python script is designed to search for a specific pattern recursively within files in a directory.
Usage

## Features:

#### Efficient Search: 
Utilizes multi-threading to concurrently search through multiple files, enhancing search speed and performance.

#### Flexible Pattern Matching: 
Employs regular expressions to allow for versatile pattern matching, enabling users to specify complex search criteria.

#### Automatic Encoding Detection: 
Detects file encodings to ensure seamless processing of text files encoded in various formats, enhancing compatibility.

Install the required libraries using pip:
`pip install chardet`

Run the script providing the pattern to search for and optionally the directory to search in:

`python search_pattern.py <pattern> [<directory>]`

- <pattern>: The pattern to search for in the files. (multi words simply needs quotes) 
- [<directory>] (optional): The directory to search in. If not provided, the current directory will be searched.

### Interactive Mode

Alternatively, you can run the script in interactive mode by adding the --interactive flag:

`python search_pattern.py --interactive`
`Enter pattern: example`
`Enter directory (press Enter for current directory): /path/to/directory`

In interactive mode, you will be prompted to enter the pattern and the directory to search in.  The script does not store searches history therefore enhancing privacy. 

*Note: Auto-complete for directories is not supported in interactive mode in this current version of the script.
*
### Example running CLI, not interactive

Search for the pattern "example" in the current directory:

`python search_pattern.py example`

Search for a multi-word pattern in the Documents directory:

`python search_pattern.py 'My important idea' Documents`
