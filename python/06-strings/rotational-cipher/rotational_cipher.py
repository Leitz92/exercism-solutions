def rotate(text, key):
    """
    Rotate a given text by a given key.

    :param text: str - the input text to cipher
    :param key: int - the number of positions to rotate the text
    :return: str - the rotated text
    """
    rotated_text = ""
    for char in text:
        # Check if the character is a letter
        if char.isalpha() and char.islower():
            # Calculate the new position of the letter in the alphabet
            new_position = (ord(char) - ord("a") + key) % 26 + ord("a")
            # Add the rotated letter to the result
            rotated_text += chr(new_position)
        elif char.isalpha() and char.isupper():
            # Calculate the new position of the letter in the alphabet
            new_position = (ord(char) - ord("A") + key) % 26 + ord("A")
            # Add the rotated letter to the result
            rotated_text += chr(new_position)
        else:
            # Add non-letter characters
            rotated_text += char
    return rotated_text