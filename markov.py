"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """
    read_file = open(file_path).read()
    return read_file

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

    whole_text = text_string.split(" ")
    print(whole_text)

    # i = 0
    # while i < 100:
    # # for word in text_string:
    #     #key =chain is tuple of i (n, i n+1)
    #     #value = following word in a list
    #     #dictionaryname[key] = value
    #     # i = 0
    #     print(text_string[i])
    #     chain = (text_string[i], text_string[i + 1])
    #     print(chains)
    #     print(chain)

    #     possible_following_words = []

    #     chains[chain] = possible_following_words.append(text_string[i+2]) 
    #     break

    # return chains

#print(make_chains(open_and_read_file('green-eggs.txt')))

def make_text(chains):
    """Return text from chains."""

    words = []

    # your code goes here

    return " ".join(words)


# input_path = "green-eggs.txt"

# # Open the file and turn it into one long string
# input_text = open_and_read_file(input_path)

# # Get a Markov chain
# chains = make_chains(input_text)

# # Produce random text
# random_text = make_text(chains)

# print (random_text)
