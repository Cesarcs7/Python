#Challenge
#Using the Python language, have the function LongestWord(sen) take the sen parameter being passed and return the largest word in the string.
#If there are two or more words that are the same length, return the first word from the string with that length.
#Ignore punctuation and assume sen will not be empty. 

def LongestWord(sen):
    
    words = sen.split()
    longest = ''
    
    for val in words:
        
        if len(val) > len(longest):
            longest = val
        
    return longest
      
print(LongestWord(input()))  