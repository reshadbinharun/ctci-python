'''
Check Permutation: Given two strings, write a method to decide if one is a permutation of the
other.
'''

def checkPermutation(word1, word2):
    word1AsList = list(word1)
    word2AsList = list(word2)
    word1AsList.sort()
    word2AsList.sort()
    return word1AsList == word2AsList

# test cases
print(checkPermutation("cat", "cta"))
print(checkPermutation("cat", "dog"))