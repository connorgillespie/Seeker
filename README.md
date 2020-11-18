# Seeker
## About
Seeker was designed to help users find files with ease. After constantly losing files, I finally decided to create a simple, efficent script to help releviate the issue.

## Installation
To install the necessary packages for the script, please run the following command inside the directory containing the script's files.
> pip install -r requirements.txt

## Inputs
### File
The file input is used to find any file by an extension or filename. 

For example, if you were wishing to search for the file test.txt, you would enter the following.
> test.txt

The ASCII character * can be replaced within the input to symbolize a wildcard. A wildcard can be used to subsitute for zero or more characters within a string.

For example, if you are trying to display all .txt files within a directory, you would enter the following.
> *.txt

### Path
The path input is used to specify a directory to search. 

For example, if you were wishing to search for a file within the C directory, you would enter the following.
> C:/

*Note the script will automatically search all subdirectories within the inputted path.*

## Upcoming
[] Add Linux Support
[] Add Wildcard Directories
