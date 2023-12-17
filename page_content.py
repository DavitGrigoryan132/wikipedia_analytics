class PageContent:
    """Represents the content of a web page, including sentences and words."""

    def __init__(self):
        """Initialize PageContent with empty sentences and words."""
        self._sentences = None
        self._words = None

    @property
    def sentences(self):
        """Property method to get the list of sentences in the web page content.

        Returns:
            list[str]: List of sentences.
        """
        return self._sentences

    @sentences.setter
    def sentences(self, new_value):
        """Setter method to set the list of sentences in the web page content.

        Args:
            new_value (list[str]): The new list of sentences to set.
        """
        self._sentences = new_value

    @property
    def words(self):
        """Property method to get the list of words in the web page content.

        Returns:
            list[str]: List of words.
        """
        return self._words

    @words.setter
    def words(self, new_value):
        """Setter method to set the list of words in the web page content.

        Args:
            new_value (list[str]): The new list of words to set.
        """
        self._words = new_value
