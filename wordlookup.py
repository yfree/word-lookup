#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
from lxml import etree

api_key = 'FILL ME OUT'
api_url = 'http://www.dictionaryapi.com/api/v1/references/collegiate/xml/'

def parse_args():
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('words', nargs='+', help="Words to look up.")
    return arg_parser.parse_args()

def word_lookup(word):
    request_url = api_url + word + '?key=' + api_key
    try:
        doc = etree.parse(request_url)
    except IOError:
        print 'Failed to connect to API.'
        return
    except etree.XMLSyntaxError:
        print 'Invalid XML response when looking up "' + word + '".'
        return
    entries = doc.xpath('//entry_list/entry')
    suggestions = doc.xpath('//entry_list/suggestion')
    if entries:
        print '\n\tInput: ' + word
        for entry in entries:
            print '========================='
            print entry.find('ew').text
            for definition in entry.xpath('def/dt'):
                etree.strip_tags(definition,"*")
                print '=> ' + definition.text.replace(':','', 1)
        print '========================='
    elif suggestions:
        print 'The word "' + word + '" isn\'t in the dictionary.\nSuggestions:'
        for suggestion in suggestions:
            print suggestion.text
    else:
        print 'No results found for "' + word + '".'

def main():
    args = parse_args()
    for word in args.words:
        word_lookup(word)

if __name__ == "__main__":
    main()
