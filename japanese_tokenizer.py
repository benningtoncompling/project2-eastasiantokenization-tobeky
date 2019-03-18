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


# attempt number one
# def max_match(line, dictionary):
#     if line in dictionary:
#         #word = line
#         #line = line[len(word):]
#         #return word + " " + max_match(line, dictionary)
#         for line in lines:
#             sentence = line
#             while len(sentence) > 1:
#                 word = max_match(line, dictionary)
#                 sentence = sentence[len(word):]
#             return word + max_match(sentence, dictionary)
#     if len(line) == 1:
#         return line + " "
#     else:
#         new_line = line[:-1]
#         return max_match(new_line, dictionary)


# attempt number two
# def max_match(lines, dictionary):
#     for line in lines:
#         if line in dictionary:
#             sentence = line
#             word = max_match(line, dictionary)
#             sentence = sentence[len(word):]
#             return word + max_match(sentence, dictionary)
#         if len(line) == 1:
#             return line + " "
#         else:
#             new_line = line[:-1]
#             return max_match(new_line, dictionary)


result = open("out.txt", "w")
for line in lines:
    result.write(max_match(lines, dictionary))
    result.write("\n")
result.close()


#   Sources:
#   thanks as always to Sophia for putting up with me/emotional support
#   kelsey & I worked together on this a bit
#   thank you Justin for help!
#   making the txt files into lines: https://stackoverflow.com/questions/14676265/how-to-read-a-text-file-into-a-list-or-an-array-with-python/27046171
#   inspiration: https://www.youtube.com/watch?v=ABGiqizwCso