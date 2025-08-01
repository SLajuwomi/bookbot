# BookBot
BookBot is my first [Boot.dev](https://www.boot.dev) project!

## Description
BookBot is a simple Python project that analyzes the contents of classic books. It counts words and characters, then prints a summary report.

## Features
- Counts total words in a book
- Counts and sorts character frequency (case-insensitive)
- Outputs a formatted report to the console

## Usage
Run BookBot from the command line, providing the path to a book file:

```bash
python3 main.py books/frankenstein.txt
```

Replace `books/frankenstein.txt` with the path to any `.txt` file you want to analyze.

## Project Structure
- `main.py` — Main entry point and report generator
- `stats.py` — Functions for word and character counting
- `books/` — Folder containing sample book files

## Example Output
```
============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
Found 75000 total words
--------- Character Count -------
a: 5000
b: 3000
# ...
============= END ===============
```