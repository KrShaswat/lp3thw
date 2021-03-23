# break_words fucntion breaks the sentence when it finds a ' ' space and saves the run letters in list
def break_words(stuff):
    """This function will break up words for us"""
    words = stuff.split(' ')
    return words
# sort_words sorts the break_words alphabatically using sorted() fucntion
def sort_words(words):
    """Sorts the words."""
    return sorted(words)
# print first word is with pop method which pops the indexed from the list
def print_first_word(words):
    """Prints the first word after popping it off."""
    word = words.pop(0)
    print(word)
# pops last string to index last index we use negative -1
def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1)
    print(word)
# sort snetence is with the break_sentence command and returns sorted result
def sort_sentence(sentence):
    """Takes in full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)
# uses both print last and first function
def print_first_and_last(sentence):
    """Print the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)
# print first and last sorted
def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)