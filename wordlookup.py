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
    key = '?key=' + api_key
    request_url = api_url + word + key
    doc = etree.parse(request_url)
    # these tags are meant to manipulate the text output and should be stripped while retaining their contents
    etree.strip_tags(doc,'note', 'sup', 'inf', 'it', 'sc', 'rom', 'bold', 'bit',
                                'isc', 'd_link', 'i_link', 'dx_ety', 'dx_def','un','ca','dx')
    suggestions = doc.xpath('//entry_list/suggestion')
    entries = doc.xpath('//entry_list/entry')
    
    if suggestions:
        print 'The word "' + word + '" isn\'t in the dictionary.\nSuggestions:'
        for suggestion in suggestions:
            print suggestion.text
    elif entries:
        for entry in entries:
            print '========================='
            print entry.find('ew').text
            for definition in entry.xpath('def/dt | def/dt/sx'):
                try:
                    filtered_definition = definition.text.replace(':','')
                except AttributeError:
                    print "Unfiltered formatting tag found in definition field:"
                    undef_tags = definition.getchildren()
                    for undef_tag in undef_tags:
                        print undef_tag.tag + ' '
                    exit(1)

                if filtered_definition:
                    print '=> ' + filtered_definition
    else:
        print 'No results found.'

def main():
    args = parse_args()
    for word in args.words:
        word_lookup(word)

if __name__ == "__main__":
    main()
