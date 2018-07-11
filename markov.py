"""Generate Markov text from text files."""

from random import choice

def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """
    read_file = open(file_path).read()
    return read_file

def split_text(input):
    """Takes string and splits into list."""

    return input.split()

def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']
        
        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}

    # for loop to go through text and group into tuples
    for i in range(len(text_string)-2):

        following_word = text_string[i + 2]
        chain_tuple = (text_string[i], text_string[i + 1])

    # conditional statement to check for chain_tuple in keys of dictionary
        # if new entry, it'll add a list containing a following word
        if chain_tuple not in chains.keys():
            chains[chain_tuple] = [following_word]
        # if not new entry, append the following word to the value
        else:
            chains[chain_tuple].append(following_word)

    return chains


def make_text(chains, list_words):
    """Return text from chains."""
    words = []

    first_words = list_words[0:2]
    words.extend(first_words)
    
    last_tuple = list_words[-3:-1]
    last_tuple = tuple(last_tuple)

    word1 = words[0]
    word2 = words[1]

    for word in chains:
        key = tuple((word1, word2))

        if key == last_tuple:
            break

        else:
            next_word = choice(chains[key])
            words.append(next_word)
            word1 = word2
            word2 = next_word

    # words.append(last_tuple)
    # #     # if key in chains:
    # #     #     next_word = choice(chains[key])
    # #     #     words.append(next_word)
    # #     #     word1 = word2
    # #     #     word2 = next_word

    # #     # else:
    # #     #     words.extend("I", "am?")


    # # # for key, value in chains:

    # return " ".join(words)



def execute_functions(file_name):
    input_path = file_name

    # Open the file and turn it into one long string
    input_text = open_and_read_file(input_path)

    # Input is string, splits text into list of strings
    whole_text = split_text(input_text)

    # Get a Markov chain
    chains = make_chains(input_text)

    # Produce random text
    random_text = make_text(chains, whole_text)

    # print (random_text)

execute_functions('green-eggs.txt')