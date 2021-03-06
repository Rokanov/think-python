#                                                                      #
# ----------------------Chapter 12: Tuples---------------------------- #
#                                                                      #

# TODO: Memoize ex 12.4. solution

# 12.1. Write a function called most_frequent that takes a string and prints
# the letters in decreasing order of frequency. Find text samples from several
# different languages and see how letter frequency varies between languages.


def handle_text(s):
    '''Text handling: removes symbols from a string and sets to lower-case

    s: string

    returns: string
    '''
    symbols = ' -”“!?‘’,.;:\\\n\'«»'
    for symbol in symbols:
        if symbol in s:
            s = s.replace(symbol, '')
    s = s.lower()
    return s


def histogram(s):
    '''Takes a string and returns histogram of frequencies

    s: String

    returns: dictionary mapping letter:frequency
    '''
    d = dict()
    for c in s:
        d[c] = d.get(c, 0)
        d[c] += 1
    return d


def most_frequent(s):
    '''Takes a string and prints the letters in decreasing order of frequency.
    Includes rudimentary special character handling.

    s: String

    returns: None
    '''
    s = handle_text(s)
    d = histogram(s)

    if len(d) > 26:
        print(' More than 26 characters counted')

    # Reverse dictionary and store as a list of tuples where first value is
    # frequency and second is letter
    t = []
    for letter, freq in d.items():
        t.append((freq, letter))

    # Sort tuples in list from highest to lowest frequency
    t = sorted(t, reverse=True)

    # Unpack tuples, printing letter then frequency
    for freq, letter in t:
        print('  {0}: {1}'.format(letter, freq))


def ex12_1():
    print('Basic String:')
    string = 'ab  cd dda'
    most_frequent(string)

    print('The Golden Bird:')
    fin = open('resources/goldenbird.txt', encoding='UTF-8')
    s = ''
    for line in fin:
        s += line

    most_frequent(s)

    print('Wolves against Mustangs (Czech)')
    fin = open('resources/czech.txt', encoding='UTF-8')
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
    fin = open('resources/words.txt')
    word_list = []
    for line in fin:
        word = line.strip()
        word_list.append(word)
    return word_list


def print_anagrams(word_list, n=2):
    '''Reads word list and prints all sets of words that are anagrams from
    longest set to shortest

    word_list: list of strings
    n: minimum number of words that form anagrams (Default: 2)
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
        # Find bingo solution. 8 letters giving 7 words
        if len(d[k]) == 7 and len(k) == 8:
            bingo = k
            bingo_words = d[k]
        if len(d[k]) >= n:
            anagram_dict[tuple(d[k])] = len(d[k])

    # Reverse the dictionary so length is first and save to a list, sorting
    # by number of words in list
    anagram_list = []
    for key, value in anagram_dict.items():
        anagram_list.append((value, key))
    anagram_list = sorted(anagram_list, reverse=True)

    # Print the words as a list, longest first
    for length, words in anagram_list:
        print(list(words))

    print('Collection of letters with most bingos:', bingo)
    print('Possible words:', bingo_words)


def ex12_2():
    # word_list = ['deltas', 'desalt', 'lasted', 'salted', 'slated', 'staled']
    word_list = build_word_list()
    print_anagrams(word_list, 6)


# 12.3. Two words form a “metathesis pair” if you can transform one into the
# other by swapping two letters; for example, “converse” and “conserve”.
# Write a program that finds all of the metathesis pairs in the dictionary.
# Hint: don’t test all pairs of words, and don’t test all possible swaps.


def build_word_dict():
    '''Build a dictionary of words with word length as keys and list of words as
    values.

    returns: dictionary of int:list of strings
    '''
    fin = open('resources/words.txt')

    word_dict = dict()
    for line in fin:
        word = line.strip()
        i = len(word)
        word_dict.setdefault(i, []).append(word)

    return word_dict


def is_metathesis(word1, word2):
    '''Compares two words and returns True if they are a 'metathesis pair'
    (If can transform one into the other by swapping two letters)

    word1, word2: string

    returns: bool
    '''
    # Skip same word and words not of same length
    if word1 == word2 or len(word1) != len(word2):
        return False

    # Only proceed with words containing exact same set of letters
    if sorted(tuple(word1)) != sorted(tuple(word2)):
        return False

    # If passes preconditions, must be metathesis pair
    return True


def build_metathesis_dict():
    '''Build a dictionary of metathesis pairs. Uses length of words as keys
    and saves solutions as tuples within a list.

    returns: dictionary of int:list of tuple of strings
    '''
    metadict_all = dict()
    metathesis_dict = dict()
    word_dict = build_word_dict()

    for i in word_dict:
        for word1 in word_dict[i]:
            word1_tuple = tuple(sorted(tuple(word1)))
            metadict_all.setdefault(word1_tuple, []).append(word1)

    for t in metadict_all:
        if len(metadict_all[t]) > 1:
            key = len(metadict_all[t][0])
            metathesis_dict.setdefault(key, []).append(tuple(metadict_all[t]))

    return metathesis_dict


def ex12_3():
    '''Run solution to metathesis pair exercise
    '''
    print('Original method using is_metathesis:',
        is_metathesis('converse', 'conserve'))
    print()

    meta_dict = build_metathesis_dict()

    keys_list = []
    for key, value in meta_dict.items():
        keys_list.append(key)
    keys_list.sort()

    while True:
        print('Display metathesis pairs of which length?')
        print(' Possible lengths are:{0}'.format(keys_list))
        print(' (Type "quit" to exit)\n')
        inp = input(' > ')
        try:
            if inp == 'quit':
                break
            elif int(inp) in keys_list:
                print()
                for t in meta_dict[int(inp)]:
                    print(t)
                print()
            else:
                print("Error: Key doesn't exist, try a different number\n")
        except:
            print("Error: Please type int\n")



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


def build_word_dict():
    '''Generate word dictionary with strings as keys

    returns: dict with str as keys
    '''
    fin = open('resources/words.txt')
    word_dict = dict()
    for line in fin:
        word = line.strip()
        word_dict.setdefault(word, 0)
    return word_dict


def trim_word_dict(word_dict):
    '''For reducible testing, removes all words not containing a or i
    
    word_dict: dict with strings as keys

    returns: dict with strings as keys
    '''
    temp_word_dict = dict()
    for key in word_dict:
        if 'a' in key or 'i' in key:
            temp_word_dict.setdefault(key, 0)
    return temp_word_dict


def get_children(word):
    '''Generate a list of "reduced" children from a word.
    
    word: string

    returns: list    
    '''
    children = list()

    for i in range(len(word)):
        child = word[:i] + word[i+1:]
        # print(child)
        children.append(child)
    # print(children)
    return children


def validate_word(word):
    '''Check if a word is real.
    
    word: string

    returns: bool
    '''
    return word in word_dict


def check_word(word, verbose=False):
    '''Recursively check if a word and all children are reducible. Optional
    logging to show steps
    
    word: string
    verbose: bool
    
    returns: bool
    '''
    # Recusion calls and word checking
    
    # Base case. Reduces down to empty string
    if word == '':
        return True

    children = get_children(word)
    if verbose == True:
        print('  Children:', children)
    for child in children:
        if child == '':
            return True
        if validate_word(child):
            if verbose == True:
                print('  Valid child:', child)
                return check_word(child, verbose=True)
            else:
                return check_word(child)
    return False

    
def ex12_4():

    # Build word dict and trim words without i or a. Use global so don't
    # have to pass word_dict to all functions
    global word_dict
    word_dict = build_word_dict()
    word_dict = trim_word_dict(word_dict)

    # Run basic tests
    print('Empty string, True:', check_word(''))
    print('Sprite, True:', check_word('sprite'))
    print('Assvogel, False:', check_word('assvogel'))

    # Find reducible all words
    reducible_dict = dict()
    for word in word_dict:
        if check_word(word):
            reducible_dict[word] = 0

    # Find longest reducible word or words
    longest_so_far = str()
    longest_list = list()
    for word in reducible_dict:
        if len(word) > len(longest_so_far):
            longest_so_far = word
            longest_list = [word]
        elif len(word) == len(longest_so_far):
            longest_list.append(word)

    # Print longest word and show steps to prove it's reducible
    print('Longest reducible word(s):', longest_list)
    for word in longest_list:
        print(check_word(word, verbose=True))


# Run exercise solutions
# ex12_1()
# ex12_2()
# ex12_3()
ex12_4()
