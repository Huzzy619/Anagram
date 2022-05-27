# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True
from collections import Counter


def find_anagram(word, anagram):
    # [assignment] Add your code here
    if Counter(word) == Counter(anagram):
        print(f"{word} & {anagram} are anagrams")
        return True
    else:
        print(f"{word} & {anagram} are not anagrams")
        return False


find_anagram("listen", "silent")

find_anagram("switch", "stitch")
