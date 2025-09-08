def is_anagram(word1, word2):
    w1 = word1.replace(" ", "").lower()
    w2 = word2.replace(" ", "").lower()
    return sorted(w1) == sorted(w2)
a=input()
b=input()
print(is_anagram(a,b)) 
