def punctuate2(sentence, phrase_type):
    """
    Create a punctuated sentence from a string. Defaults to an ordinary
    sentence with a full stop.

    sentence: string, the phrase that is to have punctuation added
    phrase_type: string, defines what kind of sentence to create. 
                "exclamation", "question" and "aside" are known values
    """
    if phrase_type == "exclamation":
        return sentence + "!"
    elif phrase_type == "question":
        return sentence + "?"
    elif phrase_type == "aside":
        return "(" + sentence + ")"
    else:
        return sentence + "."

punctuate2()
