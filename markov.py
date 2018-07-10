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

    whole_text = text_string.split()
    # for loop to go through text and group into tuples
    for i in range(len(whole_text)-2):

        following_word = whole_text[i + 2]
        chain_tuple = (whole_text[i], whole_text[i + 1])

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
    words = ['Would', 'you']

    #Look at tuple (would you)- randomly pick next word from list
    #Look at tuple (you- next) -randomly pick
    #(first word, link)
    #next work is random from list

    #first_tuple = chains[("Would", "you")]
    #next_word = choice(first_tuple)
    word1 = words[0]
    word2 = words[1]

    for word in chains:
        key = (word1, word2)

        # if key == ('Sam', 'I'):
        if key == ('them,', 'Sam'):
            break

        else:
            next_word = choice(chains[key])
            words.append(next_word)
            word1 = word2
            word2 = next_word

    words.extend(["I", "am?"])
    #     # if key in chains:
    #     #     next_word = choice(chains[key])
    #     #     words.append(next_word)
    #     #     word1 = word2
    #     #     word2 = next_word

    #     # else:
    #     #     words.extend("I", "am?")


    # for key, value in chains:

    return " ".join(words)


input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print (random_text)
