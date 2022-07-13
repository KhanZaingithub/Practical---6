def countoccurence(str,word):
    wordlist = list(str.split())
    return wordlist.count(word)

str = " This program checks the occurence of the word "    
word1 = "the"
print(countoccurence(str,word1))
