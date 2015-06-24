# Alphabetical substrings: WAP for printing longest substring of s with letters in alphabetical order
# Test values for variable 's' is provided by edX  
# 
# Example: 
# s = 'azcbobobegghakl'
# ----- Output -----
#   Longest substring in alphabetical order is: beggh
#

alphabets = 'abcdefghijklmnopqrstuvwxyz'
sub_string = ""
longest_string = ""

for char in s:
    temp_index = alphabets.index(char)
    sub_string_length = len(sub_string)
    longest_string_length = len(longest_string)

    if sub_string_length != 0:
        # compare if the index of current alphabet in the word is greater than the index of last alphabet in the given string 's'
        if temp_index >= alphabets.index(sub_string[sub_string_length - 1]):
            sub_string += char
            if longest_string_length < sub_string_length:
                longest_string = sub_string
        else:
            if longest_string_length < sub_string_length:
                longest_string = sub_string
            sub_string = char
    else:
        sub_string += char

print "Longest substring in alphabetical order is: " + longest_string  
