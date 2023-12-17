import string

from page_content import PageContent
from raw_page import RawPage


class Extractor:
    def __init__(self):
        pass

    @staticmethod
    def extract_sentences(raw_page: RawPage, page_content: PageContent):
        page_content.sentences = [sentence for sentence in raw_page.data.replace("\n", ".").split(".") if
                                  len(sentence) > 0]

    @staticmethod
    def extract_words(raw_page: RawPage, page_content: PageContent):
        text = raw_page.data.replace("\n", ".")

        translator = str.maketrans("", "", string.punctuation)
        cleaned_string = text.translate(translator)

        page_content.words = [word.lower() for word in cleaned_string.split(" ") if len(word) > 0]
