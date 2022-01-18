# Ex 5.11
# Create a list of alphabet letters that can be iterated over

ALPHABET = 'abcdefghijklmnopqrstuvwxyz'

def summarize_letters(string):
    #Initializing a empty dictionary
    character_counter = {}
    #converting all the characters to lowercase
    string_lower = string.lower()
    for i in string_lower:
        #checking if the charter presents in the dictionery then increase it by one and also to check if the character is alphabetic
        if i in character_counter and i.isalpha():
            character_counter[i] = character_counter[i]+1
        #checking if the character not present in the dictionary then assign 1
        if i not in character_counter and i.isalpha():
            character_counter[i] = 1
    #converting the dictionary to list of tuples
    list_of_tuples = [(k, v) for k, v in character_counter.items()]
    return list_of_tuples

#initializing a string of characters in alphabets
alphabets = 'a b b b b B A c e f g d h i j k  B l m M n o p q r s P t u v w x y z'
print(summarize_letters(alphabets))

#importing the string module
import string
#pulling all the alphabets
alphabet = set(string.ascii_lowercase)
#checking if our hardcoded string has all the alphabets
if set(alphabets.lower()) >= alphabet:
    print('The string ' +alphabets+' has all the letters in the alphabet ')
    
    
    