word1 = input("Enter a string: ")
word2 = input("Enter a second string: ")

def isAnagram(s1, s2):
    s1 = sorted(s1)
    s2 = sorted(s2)
    if s1 == s2:
       print("This is an anagram")
    else:
       print("This is not an anagram")

isAnagram(word1, word2)