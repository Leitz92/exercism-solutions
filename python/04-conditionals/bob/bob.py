def response(hey_bob):
    # Clean the string at beggining and ending of white spaces
    hey_bob = hey_bob.strip()
    # Check if the string is empty
    if len(hey_bob) == 0:
        return "Fine. Be that way!"
    # Check if yell a question (all uppercase and ending with a question mark)
    elif hey_bob.isupper() and hey_bob[-1] == "?":
        return "Calm down, I know what I'm doing!"
    # Check if is a question, come here because the previous one was more restrictive
    elif hey_bob[-1] == "?":
        return "Sure."
    # Check if is all uppercase
    elif hey_bob.isupper():
        return "Whoa, chill out!"
    # Anything else
    else:
        return "Whatever."
