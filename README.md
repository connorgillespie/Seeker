# Seeker
## About
Seeker was designed to help users find files with ease. After constantly losing files, I finally decided to create a simple, efficent script to help releviate the issue.

## Installation
### Windows
Download the zip from github [https://github.com/connorgillespie/Seeker/archive/main.zip](here).

Unzip the files using 7zip or Winrar.

Open the Seeker-main folder and double click the seeker.py file. 

### Linux
Press CTRL+ALT+T to open a new terminal. 

Execute the following command to download the zip.
> wget https://github.com/connorgillespie/Seeker/archive/main.zip

Execute the following command to unzip the files.
> unzip main.zip

Execute the following command to remove the zip.
> rm main.zip

Execute the following command to start the script.
>  python3 Seeker-main/seeker.py

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

Additionally, if you were wishing to search the Linux home directory, you would enter the following.
> /home

*Note the script will automatically search all subdirectories within the inputted path.*
