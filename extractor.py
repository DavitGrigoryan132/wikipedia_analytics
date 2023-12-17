import string
from page_content import PageContent
from raw_page import RawPage


class Extractor:
    """Extracts sentences and words from raw web page content."""

    def __init__(self):
        """Initialize the Extractor."""
        pass

    @staticmethod
    def extract_sentences(raw_page: RawPage, page_content: PageContent):
        """Extract sentences from raw web page content and update the PageContent object.

        Args:
            raw_page (RawPage): The RawPage object representing the web page.
            page_content (PageContent): The PageContent object to be updated.
        """
        page_content.sentences = Extractor.__get_list_of_sentences(raw_page.data)

    @staticmethod
    def extract_words(raw_page: RawPage, page_content: PageContent):
        """Extract words from raw web page content and update the PageContent object.

        Args:
            raw_page (RawPage): The RawPage object representing the web page.
            page_content (PageContent): The PageContent object to be updated.
        """
        sentences = Extractor.__get_list_of_sentences(raw_page.data)

        words = []

        for sentence in sentences:
            translator = str.maketrans(string.punctuation, ' ' * len(string.punctuation))
            cleaned_string = sentence.translate(translator)
            cleaned_string = cleaned_string.replace('\xa0', ' ')
            words += cleaned_string.split(" ")

        page_content.words = [word.lower() for word in words if len(word) > 0]

    @staticmethod
    def __get_list_of_sentences(text: str):
        """Private method to split text into a list of sentences.

        Args:
            text (str): The text to be split into sentences.

        Returns:
            list[str]: List of sentences.
        """
        return [sentence for sentence in text.replace("\n", ".").split(".") if len(sentence) > 0]
