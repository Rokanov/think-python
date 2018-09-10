#                                                                      #
# ----------------------Chapter 12: Tuples---------------------------- #
#                                                                      #

# 12.1. Write a function called most_frequent that takes a string and prints
# the letters in decreasing order of frequency. Find text samples from several
# different languages and see how letter frequency varies between languages.

def most_frequent(s):
    '''Takes a string and prints the letters in decreasing order of frequency.
    Includes rudimentary special character handling.

    s: String

    returns: None
    '''
    chars = ' -”“!?‘’,.;:\\\n\'«»'
    for symbol in chars:
        if symbol in s:
            s = s.replace(symbol, '')
    s = s.lower()

    d = {}
    for letter in s:
        d.setdefault(letter, 0)
        d[letter] += 1
    
    if len(d) > 26:
        print(' More than 26 characters counted')

    t = []
    for key, value in d.items():
        t.append((value, key))
    t = sorted(t, reverse=True)
    
    for freq, letter in t:
        print('  {0}: {1}'.format(letter, freq))
    
def ex12_1():
    print('Basic String:')
    string = 'ab  cd dda'
    most_frequent(string)

    print('The Golden Bird:')
    fin = open('goldenbird.txt', encoding='UTF-8')
    s = ''
    for line in fin:
        s += line

    most_frequent(s)

    print('Wolves against Mustangs (Czech)')
    fin = open('czech.txt', encoding='UTF-8')
    s = ''
    for line in fin:
        s += line

    most_frequent(s)

# 12.2. a) Write a program that reads a word list from a file and prints
# all the sets of words that are anagrams.
# 
# Here is an example of what the output might look like:
#	
#	['deltas', 'desalt', 'lasted', 'salted', 'slated', 'staled']
#	['retainers', 'ternaries']
#	['generating', 'greatening']
#	['resmelts', 'smelters', 'termless']
#	
# Hint: you might want to build a dictionary that maps from a collection of 
# letters to a list of words that can be spelled with those letters. 
# The question is, how can you represent the collection of letters in a 
# way that can be used as a key? 
# 
# b) Modify the previous program so that it prints the longest list of 
# anagrams first, followed by the second longest, and so on.
# 
# c) In Scrabble a “bingo” is when you play all seven tiles in your rack, 
# along with a letter on the board, to form an eight-letter word. What 
# collection of 8 letters forms the most possible bingos? Hint: there are seven.


def build_word_list():
    '''Build word list from file words.txt

    Returns: list of strings
    '''
    fin = open('words.txt')
    word_list = []
    for line in fin:
        word = line.strip()
        word_list.append(word)
    return word_list


def print_anagrams(word_list):
    '''Reads word list and prints all sets of words that are anagrams from
    longest set to shortest

    word_list: list of strings
    '''
    # Create dictionary with tuple of each word as key and anagrams as values
    d = dict()
    for word in word_list:
        t = tuple(sorted(word))
        d.setdefault(t, []).append(word)

    # Create a new dict with tuple of anagram words as keys and length 
    # (amount of words) as values
    anagram_dict = dict()
    for k in d:
        if len(d[k]) > 1:
            anagram_dict[tuple(d[k])] = len(d[k])
    
    # Reverse the dictionary so length is first and save to a list, sorting
    # by number of words in list
    anagram_list = []
    for key, value in anagram_dict.items():
        anagram_list.append((value, key))    
    anagram_list = sorted(anagram_list, reverse = True)

    # Print the words as a list, longest first
    for length, words in anagram_list:
        print(list(words))
    

# word_list = ['deltas', 'desalt', 'lasted', 'salted', 'slated', 'staled']
word_list = build_word_list()
print_anagrams(word_list)




# 12.3. Two words form a “metathesis pair” if you can transform one into the 
# other by swapping two letters; for example, “converse” and “conserve”. 
# Write a program that finds all of the metathesis pairs in the dictionary.
# Hint: don’t test all pairs of words, and don’t test all possible swaps.








# 12.4. What is the longest English word, that remains a valid English word, 
# as you remove its letters one at a time? Now, letters can be removed from 
# either end, or the middle, but you can’t rearrange any of the letters. 
# Every time you drop a letter, you wind up with another English word. 
# If you do that, you’re eventually going to wind up with one letter and 
# that too is going to be an English word—one that’s found in the dictionary. 
# I want to know what’s the longest word and how many letters does it have? 
# I’m going to give you a little modest example: Sprite. Ok? You start off 
# with sprite, you take a letter off, one from the interior of the word, 
# take the r away, and we’re left with the word spite, then we take the 
# e off the end, we’re left with spit, we take the s off, we’re left with 
# pit, it, and I.
# 
# Write a program to find all words that can be reduced in this way, 
# and then find the longest one. This exercise is a little more challenging
# than most, so here are some suggestions:
#
#	1. You might want to write a function that takes a word and computes
#       a list of all the words that can be formed by removing one letter. 
#       These are the “children” of the word. 
#	2. Recursively, a word is reducible if any of its children are reducible. 
#       As a base case, you can consider the empty string reducible. 
#	3. The wordlist I provided, words.txt, doesn’t contain single letter words. 
#       So you might want to add “I”, “a”, and the empty string.
#   4. To improve the performance of your program, you might want to memoize 
#       the words that are known to be reducible. 




# Run exercise solutions
# ex12_1()