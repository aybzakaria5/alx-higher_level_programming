#!/usr/bin/python3

def text_indentation(text):
    """
    This function adds two new lines after each occurrence of '.', '?', and ':'

    Args:
        text (str): The input text.

    Raises:
        TypeError: If the input is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    punctuation = ('.', '?', ':')
    none_found = True
    start = 0

    for i, char in enumerate(text):
        if char in punctuation:
            none_found = False
            substring = text[start:i + 1].strip()
            print(f"{substring}\n\n", end="")

            if i + 1 < len(text):
                start = i + 1

    if none_found and start != len(text) - 1:
        print(text[start:].strip(), end="")
