'''
Is Unique: Implement an algorithm to determine 
if a string has all unique characters. 
What if you cannot use additional data structures?
'''
# implementation with additional data structure
def isUnique(input):
    allChars = set()
    for c in input:
        if c not in allChars:
            allChars.add(c)
    return len(allChars) == len(input)

# implementation without additional data structure
def isUniqueLean(input):
    for i in range(0, len(input) - 1):
        for j in range(i + 1, len(input) - 1):
            if input[i] == input[j]:
                return False
    return True

# Test cases
print(isUnique("sammie")) 
print(isUnique("sSamie")) 

print(isUniqueLean("sammie")) 
print(isUniqueLean("sSamie")) 