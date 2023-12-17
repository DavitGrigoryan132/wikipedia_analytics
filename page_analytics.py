import json
import pandas as pd
from page_content import PageContent


class PageAnalytics:
    """Analyzes the content of a web page and provides various analytics."""

    def __init__(self, page_content: PageContent):
        """Initialize PageAnalytics with the provided PageContent.

        Args:
            page_content (PageContent): The PageContent object containing the content to be analyzed.
        """
        self.page_content = page_content
        self.top_10_frequently_words = None
        self.top_10_frequently_cleared_words = None
        self.median_length = None
        self.mean_length = None
        self.top_10_longest_words = None
        self.mean_length_sentence = None
        self.median_length_sentence = None
        self.longest_word = None
        self.json = None

    def make_analytics(self):
        """Perform analytics on the content of the web page."""
        words_df = pd.DataFrame(self.page_content.words, columns=['Word'])

        self.__find_10_frequently_words(words_df)
        self.__find_10_frequently_cleared_words()

        words_df["Length"] = words_df["Word"].apply(lambda x: len(x))
        self.median_length = words_df["Length"].median()
        self.mean_length = words_df["Length"].mean()

        self.top_10_longest_words = words_df.sort_values("Length", ascending=False).head(10)

        sentences_df = pd.DataFrame(self.page_content.sentences, columns=["Sentence"])
        sentences_df["Length"] = sentences_df["Sentence"].apply(lambda x: len(x))
        self.median_length_sentence = sentences_df["Length"].median()
        self.mean_length_sentence = sentences_df["Length"].mean()

        self.longest_word = words_df.sort_values("Length", ascending=False).iloc[0]["Word"]

    @staticmethod
    def __remove_prefix_suffix(word):
        """Remove common prefixes and suffixes from a word.

        Args:
            word (str): The word to be processed.

        Returns:
            str: The word after removing common prefixes and suffixes.
        """
        prefixes = ['un', 'pre', 're']
        suffixes = ['ing', 'ed', 'ly']

        for prefix in prefixes:
            if word.startswith(prefix):
                word = word[len(prefix):]

        for suffix in suffixes:
            if word.endswith(suffix):
                word = word[:-len(suffix)]

        return word

    def __find_10_frequently_words(self, words_df):
        """Find the top 10 frequently occurring words.

        Args:
            words_df (pd.DataFrame): DataFrame containing words.

        Returns:
            None
        """
        word_counts = words_df['Word'].value_counts()
        self.top_10_frequently_words = word_counts.head(10).reset_index()

    def __find_10_frequently_cleared_words(self):
        """Find the top 10 frequently occurring cleared words.

        Returns:
            None
        """
        cleared_words = [self.__remove_prefix_suffix(word) for word in self.page_content.words]
        cleared_words_df = pd.DataFrame(cleared_words, columns=['Word'])
        self.top_10_frequently_cleared_words = cleared_words_df['Word'].value_counts().head(10).reset_index()

    def save_to_json(self, filename: str):
        """Save analytics results to a JSON file.

        Args:
            filename (str): The name of the JSON file.

        Returns:
            None
        """
        self.json = {"top_10_frequently_words": self.top_10_frequently_words["count"].values.tolist(),
                     "top_10_frequently_cleared_words": self.top_10_frequently_cleared_words['count'].values.tolist(),
                     "median_length": self.median_length,
                     "mean_length": self.mean_length,
                     "top_10_longest_words": self.top_10_longest_words["Word"].to_list(),
                     "mean_length_sentence": self.mean_length_sentence,
                     "median_length_sentence": self.median_length_sentence,
                     "longest_word": self.longest_word
                     }

        with open(filename, "w") as f:
            json.dump(self.json, f)
