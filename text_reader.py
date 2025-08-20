from word_counter import word_counter
import numpy as np
def textreader(filepath):
    """
    Reads text from a file and passes it to the text summarizer.
    """
    total_words_frequency = dict()
    with open(filepath, "r",newline="") as file:
        while True:
            content = file.readline()
            if not content:
                break
            else:
                total_words_frequency.update(word_counter(content))
    # max_word = max(total_words_frequency,key = total_words_frequency.values())
    # print("Total words frequency:", total_words_frequency)
    counts = list(total_words_frequency.values())
    mean, std = np.mean(counts), np.std(counts)
    threshold = mean + std
    filtered_words = {}
    if "" in total_words_frequency:
            del total_words_frequency[""]
    for word,freq in total_words_frequency.items():
        if freq > threshold:
            filtered_words.update({word: freq})
    return filtered_words