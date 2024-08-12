"""Functions for creating, transforming, and adding prefixes to strings."""


def add_prefix_un(word):
    """Take the given word and add the 'un' prefix.

    :param word: str - containing the root word.
    :return: str - of root word prepended with 'un'.
    """
    return "un"+word


def make_word_groups(vocab_words):
    """Transform a list containing a prefix and words into a string with the prefix followed by the words with prefix prepended.

    :param vocab_words: list - of vocabulary words with prefix in first index.
    :return: str - of prefix followed by vocabulary words with
            prefix applied.

    This function takes a `vocab_words` list and returns a string
    with the prefix and the words with prefix applied, separated
     by ' :: '.

    For example: list('en', 'close', 'joy', 'lighten'),
    produces the following string: 'en :: enclose :: enjoy :: enlighten'.
    """
    # Extract the prefix from the first element
    prefix = vocab_words[0]

    # Initialize a list to store the results
    prefixed_words = []

    # Add the prefix itself to the list
    prefixed_words.append(prefix)

    # Loop through the remaining words and add the prefix to each word
    for word in vocab_words[1:]:
        prefixed_words.append(prefix + word)

    # Advanced mode
    # prefixed_words = [prefix] + [prefix + word for word in vocab_words[1:]]

    # Join the list into a single string with ' :: ' as the separator
    return " :: ".join(prefixed_words)


def remove_suffix_ness(word):
    """Remove the suffix from the word while keeping spelling in mind.

    :param word: str - of word to remove suffix from.
    :return: str - of word with suffix removed & spelling adjusted.

    For example: "heaviness" becomes "heavy", but "sadness" becomes "sad".
    """
    # We assume all the words coming are ended with 'ness'
    base_word = word[:-4] # Remove the 'ness' suffix
    if base_word.endswith("i"):
        return base_word[:-1] + "y" # Change the 'i' to a 'y'
    return base_word


def adjective_to_verb(sentence, index):
    """Change the adjective within the sentence to a verb.

    :param sentence: str - that uses the word in sentence.
    :param index: int - index of the word to remove and transform.
    :return: str - word that changes the extracted adjective to a verb.

    For example, ("It got dark as the sun set.", 2) becomes "darken".
    """

    # Convert the string into a list of all words
    word_list = sentence.split()

    # Get the clean word
    adjective = word_list[index].strip('.,?!¿¡')

    # Convert the adjective to verb
    return adjective + "en"

    





