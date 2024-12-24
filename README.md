# SCOURGIFY #

Solution for CS50's Introduction to Programming with Python , Problem Set 6, on File I/O

Program:

    Expects the user to provide two command-line arguments:
        the name of an existing CSV file to read as input, whose columns are assumed to be, in order, name and house, and
        the name of a new CSV to write as output, whose columns should be, in order, first, last, and house.
    Converts that input to that output, splitting each name into a first name and last name. Assume that each student will have both a first name and last name.

    If the user does not provide exactly two command-line arguments, or if the first cannot be read, the program should exit via sys.exit with an error message.

# Prerequisite #

Clone repo:
```bash
    git clone https://github.com/GakuruAlex/scourgify.git
```

Execute:
```bash
    cd scourgify
```
Create virtual environment
```bash
    python3 -m venv envname
```

Activate environment
```bash
    source envname/bin/activate
```

Then execute the follolwing to install dependencies:
```bash
    pip install -r requirements.txt
```

# Usage #

Execute:
```bash
    python3 scourgify.py
```