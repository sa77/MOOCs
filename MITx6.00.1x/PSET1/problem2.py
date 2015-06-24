# Counting bob: WAP for counting number of times the string 'bob' appears in string s
# Test values for variable 's' is provided by edX  
# 
# Example: s = 'azcbobobegghakl'
# ----- Output -----
#   Number of times bob occurs is: 2
#

length = len(s)
start = 0
count = 0

while length != 0:
    if 'bob' in s[start:start + 3]:
        count += 1
    start += 1
    length -= 1

print "Number of times bob occurs is: " + str(count)


