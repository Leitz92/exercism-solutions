def is_pangram(sentence):
    """
    Check if a given sentence is a pangram. A pangram is a sentence that contains all the letters of the alphabet.

    :param sentence: str - the input sentence
    :return: bool - True if the sentence is a pangram, False otherwise
    """
    # Convert the sentence to lowercase and remove spaces
    sentence = sentence.lower().replace(" ", "")
    # Check if all the letters of the alphabet are present in the sentence
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for char in alphabet:
        if char not in sentence:
            return False
    return True