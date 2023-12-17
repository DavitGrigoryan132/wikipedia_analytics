class PageContent:
    def __init__(self):
        self._sentences = None
        self._words = None

    @property
    def sentences(self):
        return self._sentences

    @sentences.setter
    def sentences(self, new_value):
        self._sentences = new_value

    @property
    def words(self):
        return self._words

    @words.setter
    def words(self, new_value):
        self._words = new_value
