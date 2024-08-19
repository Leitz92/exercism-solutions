VOWELS = {"a", "e", "i", "o", "u"}
VOWELS_Y = {"a", "e", "i", "o", "u", "y"}
SPECIALS = {"xr", "yt"}

def translate(text):
    """
    Translate given text from English to Pig Latin.

    :param text: str - input text in English
    :return: str - translated text in Pig Latin
    """
    piggyfied = []

    for word in text.split():
        if word[0] in VOWELS or word[0:2] in SPECIALS:
            piggyfied.append(word + "ay")
        else:
            for position in range(1, len(word)):
                if word[position] in VOWELS_Y:
                    position += 1 if word[position] == 'u' and word[position - 1] == "q" else 0
                    piggyfied.append(word[position:] + word[:position] + "ay")
                    break

    return " ".join(piggyfied)
