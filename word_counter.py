import re

def word_counter(text):
    """
    Counts the number of words in the given text.
    """
    stop_words = re.compile(r"\b(?:the|is|are|a|an|of|to|in|on|at|for|with|by|and|or|but|if|then|so|that|this|it|as|be|from|was|were|has|have|had|how|can|also|like|who|the|and|of|to|in|for|as|with|by|which|while)\b", re.IGNORECASE)
    sentence = re.split(r'[.!?]+|\s+', text.strip())
    words_frequency = dict()
    for words in sentence:
        if not stop_words.match(words):
            words = words.lower()
            if words in words_frequency:
                words_frequency[words] += 1
            else:
                words_frequency[words] = 1
    return words_frequency