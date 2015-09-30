from random import choice


def open_and_read_file(file_path):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here
    contents = open(file_path).read()
    return contents

def make_chains(text_string):
    """Takes input text as string; returns dictionary of markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:




        >>> make_chains("hi there mary hi there juanita")
        {('hi', 'there'): ['mary', 'juanita'], ('there', 'mary'): ['hi'], ('mary', 'hi': ['there']}
    """         

    chains = {}
    contents = text_string.split()
    for i in range(len(contents)-2):

        # make a tuple with current word and next word
        current_key = (contents[i],contents[ i + 1 ])
        # define a variable called third_word for the word you need to add
        third_word = contents[i + 2]
        
        # if the key is not in the dictionary yet, add it, with the value [third_word]
        if current_key not in chains:
            chains[current_key] = [] #[third_word] it can also be this and the next line can be deleted

        # if the key is already in the dictionary, append the third_word to that key's value 
        # (which should already be a list)
        chains[current_key].append(third_word)


    # your code goes here
    return chains
    #return chains


def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""

    new_key = choice(chains.keys())
    text=" "
    while new_key in chains:
        list_of_valid_following_words = chains[new_key]
        word = choice(list_of_valid_following_words) #sting
        new_key = (new_key[1], word) #tuple
        text=text + new_key[1] + " " + word + " "
                                                             
    return text
    # your code goes hereprint text


input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)
# print chains
# Produce random text
random_text = make_text(chains)

print random_text
