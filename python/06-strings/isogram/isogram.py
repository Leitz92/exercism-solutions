def is_isogram(string):
    """
    Determine if a given string is an isogram. An isogram is a word or phrase without a repeating letter.

    :param string: str - the input string
    :return: bool - True if the string is an isogram, False otherwise
    """
    # Remove spaces and convert to lowercase
    string = string.replace(" ", "").lower()
    # Check if all the characters in the string are different without consider special characters
    characters = ""
    for char in string:
        if char in characters and not char.isalpha():
            characters += char
        elif char not in characters:
            characters += char
        else:
            return False
    if len(characters) == len(string):
        return True