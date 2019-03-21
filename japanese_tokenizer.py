#!/usr/bin/env python3

import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

japanese_dictionary = open("japanese_wordlist.txt", "r")
dictionary = japanese_dictionary.read().split("\n")
japanese_dictionary.close()

text = open("in.txt", "r")
lines = text.read().split("\n")
text.close()


def max_match(line, dictionary):
    case = line
    spaced_line = " "
    while case not in dictionary and len(case) > 1:
        case = case[:-1]

    if len(case) == 0:
        return spaced_line

    if case in dictionary or len(case) == 1:
        spaced_line += case + " "
        new_case = line[len(case):]
        spaced_line += max_match(new_case, dictionary)
        return spaced_line


result = open("out.txt", "w")
for line in lines:
    output = max_match(line, dictionary)
    result.write(str(output))
    result.write("\n")
result.close()


#   Sources:
#   thanks as always to Sophia for putting up with me/emotional support
#   kelsey & I worked together on this a bit
#   paulina also helped!!
#   thank you Justin for help!
#   making the txt files into lines: https://stackoverflow.com/questions/14676265/how-to-read-a-text-file-into-a-list-or-an-array-with-python/27046171
#   inspiration: https://www.youtube.com/watch?v=ABGiqizwCso
