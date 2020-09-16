# -*- coding: utf-8 -*-
'''
One Away: There are three types of edits that can be performed on strings: 
insert a character, remove a character, or replace a character.
Given two strings, write a function to check if they are one edit (or zero edits) away.
EXAMPLE
pale, ple -> true
pales, pale -> true pale
bale -> true pale
bake -> false
'''

def oneAway(word1, word2):
    if (word1 == word2):
        return True
    if (abs(len(word1) - len(word2)) > 1):
        return False
    if (abs(len(word1) - len(word2)) == 1):
        # insertion or removal
        charCountMap = {}
        for c in list(word1):
            if (c in charCountMap):
                charCountMap[c] = charCountMap[c] + 1
            else:
                charCountMap[c] = 1

        for c in list(word2):
            if (charCountMap.get(c)):
                charCountMap[c] = charCountMap[c] - 1
        return sum(charCountMap.values()) == 1
    if (len(word1) == len(word2)):
        word1AsList = list(word1)
        word1AsList.sort()
        word2AsList = list(word2)
        word2AsList.sort()
        foundDiff = False
        for i, c in enumerate(word1AsList, start = 0):
            if foundDiff and word1AsList[i] != word2AsList[i]:
                return False
            if word1AsList[i] != word2AsList[i]:
                foundDiff = True
        return True
    return False
            
print(oneAway('cake','cak'))
print(oneAway('cake','cakc'))
print(oneAway('gain','rock'))
print(oneAway('o','omgg'))

        
        

