"""Generate Markov text from text files."""

from random import choice

def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """
    read_file = open(file_path).read()

    return read_file

# def split_text(input):
#     """Takes string and splits into list."""

#     input = input.split()
#     input.append(None)

#     return input

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

    text_string = text_string.split()
    text_string.append(None)

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


def make_text(chains):
    """Return text from chains."""

    words = []

    random_key = choice(list(chains.keys()))
    word_key = [random_key[0], random_key[1]]
    next_word = choice(chains[random_key])
    
    while next_word is not None:
        random_key = (random_key[1], next_word)
        words.append(next_word)
        next_word = choice(chains[random_key])
 
    return " ".join(words)


def execute_functions(file_name):
    input_path = file_name

    # Open the file and turn it into one long string
    input_text = open_and_read_file(input_path)
    
    # Get a Markov chain
    chains = make_chains(input_text)
    
    # Produce random text
    random_text = make_text(chains)

    print(random_text)

execute_functions('gettysburg.txt')