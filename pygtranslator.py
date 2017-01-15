pyg = 'ay'# This is the final ay which is a string. This goes at the end of the original word.

original = raw_input('Enter a word:')
# This is where the user enters a word he/she likes

if len(original) > 0 and original.isalpha():
    # This checks if there is a word and if the whole thing is a string.
    # If there is another data type isalpha function returns false.
    print original
    word = original.lower() #makes the original a lower case
    first = word[0] #puts the first letter into the variable "first"
    new_word = word[1:len(word)] + first + pyg
    # puts the word from 1 index to the last and adds first and pyg (concatenation)
    print new_word
else:
    print 'empty'
