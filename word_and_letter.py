

'''Write a function lettersIndex(word,letter) that takes in two arguments word and letter. If this letter is in the word it returns the index of the letter in the word., else it returns -1.(Do not use in, do use while loop)



Example:
lettersIndex('Hello','h') 
    Index: 0
lettersIndex('Computer','m')
    Index: 2
    
    '''

#code:
def remove_special_chars(thisString):
    return(''.join(e for e in thisString if e.isalnum()))

def lettersIndex(word,letter):

    count = 0
    letters = []
    letters.extend(word)
    while count < len(letters):
        thisLetter = letters[count]
        thisLetter = thisLetter.lower()
        if thisLetter == letter:
            return(count)
        count += 1

word = input()
word = remove_special_chars(word)
letter = input()
letter = remove_special_chars(letter)

placement = lettersIndex(word,letter)

print("Index:",placement)

