import json
import pandas as pd

from page_content import PageContent


class PageAnalytics:
    def __init__(self, page_content: PageContent):
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
        words_df = pd.DataFrame(self.page_content.words, columns=['Word'])

        self.__find_10_frequently_words(words_df)
        self.__find_10_frequently_cleared_words()

        words_df["Length"] = words_df["Word"].apply(lambda x: len(x))
        self.median_length = words_df["Length"].median()
        self.mean_length = words_df["Length"].mean()

        self.top_10_longest_words = words_df["Length"].sort_values(ascending=False).head(10)

        sentences_df = pd.DataFrame(self.page_content.sentences, columns=["Sentence"])
        sentences_df["Length"] = sentences_df["Word"].apply(lambda x: len(x))
        self.median_length_sentence = sentences_df["Length"].median()
        self.mean_length_sentence = sentences_df["Length"].mean()

        self.longest_word = sentences_df["Length"].sort_values(ascending=False).iloc[0]

    @staticmethod
    def __remove_prefix_suffix(word):
        prefixes = ['un', 'pre', 're']
        suffixes = ['ing', 'ed', 'ly']

        word = None

        for prefix in prefixes:
            if word.startswith(prefix):
                word = word[len(prefix):]

        for suffix in suffixes:
            if word.endswith(suffix):
                word = word[:-len(suffix)]

        return word

    def __find_10_frequently_words(self, words_df):
        word_counts = words_df['Word'].value_counts()
        self.top_10_frequently_words = word_counts.head(10).reset_index()

    def __find_10_frequently_cleared_words(self):
        cleared_words = [self.__remove_prefix_suffix(word) for word in self.page_content.words]
        cleared_words_df = pd.DataFrame(cleared_words, columns=['Word'])
        self.top_10_frequently_cleared_words = cleared_words_df['Word'].value_counts().head(10).reset_index()

    def save_to_json(self, filename: str):
        self.json = {"top_10_frequently_words": self.top_10_frequently_words["count"].values,
                     "top_10_frequently_cleared_words": self.top_10_frequently_cleared_words['count'].values,
                     "median_length": self.median_length,
                     "mean_length": self.mean_length,
                     "top_10_longest_words": self.top_10_longest_words["Word"].to_list(),
                     "mean_length_sentence": self.mean_length_sentence,
                     "median_length_sentence": self.median_length_sentence,
                     "longest_word": self.longest_word}

        with open(filename, "w") as f:
            json.dump(self.json, f)
