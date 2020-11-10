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


![OSDgif](https://user-images.githubusercontent.com/44411777/93946180-9171b200-fd06-11ea-90fe-06c34cbee5c5.gif)




Feel free to play with codes, if you have a crazy idea, then pull request :)

# Scope

Create a command-line tool to check links status codes in python.

# How It Works

Using the power of the library click we can add decorators to our functions. This allows us to simplify the command line arguments.
For example, "-v" or "--version" using the click object we can create a simple version_option decorator.
We check the status code of each URL we requested and display the data in color.

```sh
$ python main.py check-urls https://telescope.cdot.systems/posts
```

How to format your code.
```sh
$ python main.py format-code
```

How to lint your code.
```sh
$ python main.py lint-code
```



# Optional Features Include:

1. Option -h or --help will return the help page.
2. Option -v or --version will return the current version information.
3. option -i or --ignore the program will ignore the given urls.

# Coming soon!
Any ideas are welcome!
