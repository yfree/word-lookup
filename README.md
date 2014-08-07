# Word Lookup
A command line tool for looking up quick word definitions

## Overview
This tool uses the Merriam-Webster Dictionary API to look up words in their collegiate dictionary. Output is displayed in the terminal.
Sign up for your free API key at [Merriam-Webster's Dictionary API](http://dictionaryapi.com/).

## Usage

```bash
$ ./wordlookup cat
```
```bash
$ ./wordlookup cat dog mouse
```
The following is considered two seperate words to look up:
```bash
$ ./wordlookup guinea pig
```
Try this instead for a multi-word unit:
```bash 
$ ./wordlookup "guinea pig"
```
