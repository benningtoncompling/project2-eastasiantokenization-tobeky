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
    if line in dictionary:
        return line + " "
    if len(line) == 1:
        return line + " "
    else:
        new_line = line[:-1]
        return max_match(new_line, dictionary)


# paulina helped me bang out this bit, but then we realized it was the same as what I had originally
# sentence = []
# def max_match(line, dictionary):
#     if line in dictionary and line != "":
#         word = line
#         print(word)
#         if len(line) != len(word):
#             remainder = line[len(word):]
#         else:
#             remainder = ""
#         if remainder == "":
#             sentence.append(word)
#             return
#         sentence.append(word)
#         return word + " " + max_match(remainder, dictionary)
#     if len(line) == 1:
#         sentence.append(line)
#         return str(line) + " "
#     elif len(line) > 1:
#         new_line = line[:-1]
#         return max_match(new_line, dictionary)

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
