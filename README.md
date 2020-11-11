# OSD_A1_Tool
Creating a command-line tool to consider if urls are good, bad, or unknown.

# Introduction

My name is Paul, welcome to my Open Source Development Repo.

During the next 12 weeks I will be completeing a series of blog posts documenting my experience in the Open Source community. 
You can find my blog [here](https://osd600.blogspot.com/).

# Instructions

Download Virtualenv: pip3 install Virtualenv 
Create Virtualenv: virtualenv .
Enter virtual environment: source bin/activate

How to run 
```
$ python main.py https://telescope.cdot.systems/posts
```

NOTE: This project will only works with Python version 3.7 and above.
# Init Release:

Command Line Interface


![gif](https://user-images.githubusercontent.com/44411777/98872293-4a6d8680-2444-11eb-9cf2-3a2f2941bb60.gif)




Feel free to play with codes, if you have a crazy idea, then pull request :)

# Scope

Create a command-line tool to check links status codes in python.

# How It Works

Using the power of the library click we can add decorators to our functions. This allows us to simplify the command line arguments.
For example, "-v" or "--version" using the click object we can create a simple version_option decorator.
We check the status code of each URL we requested and display the data in color.


# Optional Features Include:

1. Option -h or --help will return the help page.
2. Option -v or --version will return the current version information.
3. option -i or --ignore the program will ignore the given urls.


# Commands

1. check-urls   Check urls retrieved from ENDPOINT.
2. format-code  Format our python scripts
3. lint-code    Format our python scripts
4. print-urls   Prints the urls on terminal

### check-urls function

This function is the main functionality of the program.
```sh
$ python main.py check-urls https://telescope.cdot.systems/posts
```

### format-code function

This function will format your code for you!
```sh
$ python main.py format-code
```
### lint-code function

This function will lint your code for you!
```sh
$ python main.py lint-code
```

# Coming soon!
Any ideas are welcome!
