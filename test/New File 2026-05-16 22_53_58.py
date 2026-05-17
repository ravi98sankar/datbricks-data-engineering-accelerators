def are_anagrams(str1, str2):
    return sorted(str1.replace(" ", "").lower()) == sorted(str2.replace(" ", "").lower())

# Example usage:
word1 = "listen"
word2 = "silent"
result = are_anagrams(word1, word2)

# added a second comment at the end

#added a new comment to check
