# search_pattern.py Pattern Search Tool

This Python script is designed to search for a specific pattern recursively within files in a directory.


#### Features:

- *Efficient Search*: Utilizes multi-threading to concurrently search through multiple files, enhancing search speed and performance.

- *Flexible Pattern Matching*: Employs regular expressions to allow for versatile pattern matching, enabling users to specify complex search criteria.

- *Automatic Encoding Detection*: Detects file encodings to ensure seamless processing of text files encoded in various formats, enhancing compatibility.

------------
## Installation

Install the required libraries using pip:
`pip install chardet`

`git clone https://github.com/TheyCallMeLinux/search_pattern.py.git && cd search_pattern.py`


## Usage

`python search_pattern.py <pattern> [<directory>]`

- <pattern>: The pattern to search for in the files.
- [<directory>] (optional): The directory to search in. If not provided, the current directory will be searched.

### Interactive Mode

Alternatively, you can run the script in interactive mode by adding the `--interactive` flag. In interactive mode, you will be prompted to enter the pattern and the directory to search in.  The script does not store searches history therefore enhancing privacy. 

In your favorite terminal type:

`python search_pattern.py --interactive`
 then press enter
 
`Enter pattern: example of search` 
Enter your sentence or word, then press Enter

`Enter directory (press Enter for current directory): /path/to/directory`
Enter the search path and or press Enter to select current working directory



*Note: Auto-complete for directories is not supported in interactive mode in this current version of the script.
*
### Example running CLI, not interactive

Search for the pattern "example" in the current directory:

`python search_pattern.py example`

Search for a multi word pattern "My Awesome Theme" in the user's Downloads directory:

`python search_pattern.py 'My Awesome Theme' ~/Downloads`

------------


### Todo

-i, --ignore-case: Perform case-insensitive search.
-r, --recursive: Recursively search within subdirectories.
-h, --help: Display the help message and exit.

### Contributing

Contributions are welcome! If you find any bugs or have suggestions for improvements, feel free to open an issue or create a pull request.

### Provided As Is

This script is provided as is, without any warranty or guarantee. Use at your own risk.

### License

This project is licensed under the MIT License - see the [MIT](https://opensource.org/license/mit "MIT") license for details.

### Acknowledgments

This script was developed by TheyCallMeLinux.

