# -*- coding: utf-8 -*-
'''
Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palin­ drome.
A palindrome is a word or phrase that is the same forwards and backwards.
A permutation is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.
EXAMPLE
Input: Tact Coa
Output: True (permutations: "taco cat", "atco eta", etc.)
'''

from itertools import permutations # using python power-up

def isPalindrome(word):
    if len(word) == 1:
        return True
    left, right = 0, len(word) - 1
    while (left != right and abs(left - right) > 1):
        if word[left] == word[right]:
            left += 1
            right -= 1
        else:
            return False
    return True        

'''
This method can be written to not use power-up
'''
def generatePermuations(input):
    return permutations(input)


def isPalindromePermutation(input):
    for combo in generatePermuations(input.replace(" ", "")):
        if (isPalindrome(combo)):
            return True
    return False

print(isPalindromePermutation('tacocat'))
print(isPalindromePermutation('taco cat'))
