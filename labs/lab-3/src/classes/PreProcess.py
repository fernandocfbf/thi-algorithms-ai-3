from bs4 import BeautifulSoup
import re
import string
import nltk
from nltk.stem import WordNetLemmatizer

class PreProcess():
    def lower_case(self, text):
        return text.lower()
    
    def remove_tags(self, text):
        res = BeautifulSoup(text).get_text()
        res = re.sub(r"http\S+", "", res)
        return res
    
    def remove_punctuation(self, text):
        text_transformed = text.translate(str.maketrans('', '', string.punctuation))
        text = text_transformed
        return text

    def lemmatization(self, text):
        lemmatizer = WordNetLemmatizer()
        return " ".join([lemmatizer.lemmatize(w) for w in nltk.word_tokenize(text)])
    
    def apply(self, text):
        text = self.lower_case(text)
        text = self.remove_tags(text)
        text = self.remove_punctuation(text)
        text = self.lemmatization(text)
        return text
