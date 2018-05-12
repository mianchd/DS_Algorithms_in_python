# -*- coding: utf-8 -*-

"""
Showing frequency of words in a Sentence
"""
sentence = "busy people usually cannot meet other busy people"
word_list = sentence.split(" ")

output_dict = {}
for word in word_list:
    output_dict[word] =  0
# output_dict = dict((element, 0) for element in word_list)
    
for word in word_list:
    output_dict[word] = output_dict[word] + 1



"""
Write a code to check whether given string is palindrome or not?
"""
string1 = 'this is not a palindrome'
string2 = 'A Santa Lived As a Devil At NASA'
string3 = 'Doc, Note: I Dissent. A Fast Never Prevents A Fatness. I Diet On Cod.'

testString = 'jumamuj'
testString == testString[::-1]
testString == ''.join(reversed(testString))

import re
def isPalindrome(w):
  
    w = re.sub(r'\W+', '', w).lower()
    matches = 0
    for i in range(len(w)):
        if w[i] == w[len(w)-1-i]:
            matches += 1
    if matches == len(w):
        return True
    else:
        return False

isPalindrome(string1)
isPalindrome(string2)
isPalindrome(string3)


"""
Write a program to sort numbers in place using quick sort?
"""

"""
How do you find middle element of a linked list in single pass?
"""

"""
In an array 1-100 numbers are stored, one number is missing how do you find it?
"""
