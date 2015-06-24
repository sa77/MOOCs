# Counting vowels: WAP for counting vowels in a given string 's'
# Test values for variable 's' is provided by edX  
# 
# Example: s = 'elephant'
# ----- Output -----
#   Number of vowels: 3
#

count = 0 
for char in s:
    if char in ['a', 'e', 'i', 'o', 'u']:
        count += 1
print "Number of vowels: " + str(count)



