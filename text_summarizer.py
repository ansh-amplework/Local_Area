import re
import numpy as np
from text_reader import textreader
def text_summarizer(filepath,count):
    key_words = textreader(filepath)
    with open("summary.txt","w") as summary_file, open(filepath,"r") as main_file:
            content = main_file.read()
            sentences = re.split(r'\.',content)
            for sentence in sentences:
                match_words_count = 0
                for word,freq in key_words.items():
                      if word in sentence.lower() and freq >= count:
                           match_words_count += 1
                
                if match_words_count >= 3:
                     summary_file.write(sentence + ".")
    print(key_words)
if __name__ == "__main__":
    filepath = input("Enter the filepath of the file: ")
    text_summarizer(filepath,3)  # Example file path
    # print("Text summarizer is ready to use.")