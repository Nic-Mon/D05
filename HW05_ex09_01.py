#!/usr/bin/env python3
# HW05_ex09_01.py

# Write a program that reads words.txt and prints only the
# words with more than 20 characters (not counting whitespace).
##############################################################################
# Imports

# Body
def print_long_words(filename):
	words_file = open(filename, 'r')
	for line in words_file:
		if(len(line) > 20):
			print(line, end='')

##############################################################################
def main():
    print_long_words('words.txt')

if __name__ == '__main__':
    main()
