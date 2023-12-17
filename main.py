from page_analytics import PageAnalytics
from page_content import PageContent
from raw_page import RawPage
from extractor import Extractor


def get_analytics(urls: list[str]):
    """Get analytics for a list of URLs.

    Args:
        urls (list[str]): List of URLs to analyze.

    Returns:
        list[PageAnalytics]: List of PageAnalytics objects containing analytics for each URL.
    """
    urls_analytics = []
    for url in urls:
        raw_page = RawPage(url)
        page_content = PageContent()

        Extractor.extract_words(raw_page, page_content)
        Extractor.extract_sentences(raw_page, page_content)

        page_analytics = PageAnalytics(page_content)
        page_analytics.make_analytics()

        urls_analytics.append(page_analytics)
    return urls_analytics


def get_longest_sentence(pages_analytics: list[PageAnalytics]):
    """Get the longest sentence among a list of PageAnalytics.

    Args:
        pages_analytics (list[PageAnalytics]): List of PageAnalytics objects.

    Returns:
        str: The longest sentence.
    """
    longest_sentence = ""
    for page in pages_analytics:
        sentence = max(page.page_content.sentences, key=len)
        if len(longest_sentence) < len(sentence):
            longest_sentence = sentence
    return longest_sentence


def get_longest_word(pages_analytics: list[PageAnalytics]):
    """Get the longest word among a list of PageAnalytics.

    Args:
        pages_analytics (list[PageAnalytics]): List of PageAnalytics objects.

    Returns:
        str: The longest word.
    """
    longest_word = ""
    for page in pages_analytics:
        word = page.longest_word
        if len(longest_word) < len(word):
            longest_word = word
    return longest_word


def get_page_with_more_sentences(pages_analytics: list[PageAnalytics]):
    """Get the PageAnalytics object with the most sentences.

    Args:
        pages_analytics (list[PageAnalytics]): List of PageAnalytics objects.

    Returns:
        PageAnalytics: The PageAnalytics object with the most sentences.
    """
    page_with_more_sentences = pages_analytics[0]
    for page in pages_analytics[1:]:
        if len(page.page_content.sentences) > len(page_with_more_sentences.page_content.sentences):
            page_with_more_sentences = page
    return page_with_more_sentences


def get_page_with_more_words(pages_analytics: list[PageAnalytics]):
    """Get the PageAnalytics object with the most words.

    Args:
        pages_analytics (list[PageAnalytics]): List of PageAnalytics objects.

    Returns:
        PageAnalytics: The PageAnalytics object with the most words.
    """
    page_with_more_words = pages_analytics[0]
    for page in pages_analytics[1:]:
        if len(page.page_content.words) > len(page_with_more_words.page_content.words):
            page_with_more_words = page
    return page_with_more_words


# Example usage:
analytics = get_analytics(["https://en.wikipedia.org/wiki/Joseph-Louis_Lagrange",
                           "https://en.wikipedia.org/wiki/Augustin-Louis_Cauchy",
                           "https://en.wikipedia.org/wiki/Gottfried_Wilhelm_Leibniz"])

print(get_longest_sentence(analytics))
print(get_longest_word(analytics))

most_words_page = get_page_with_more_words(analytics)
most_sentence_page = get_page_with_more_sentences(analytics)

for i, url_analytics in enumerate(analytics):
    url_analytics.save_to_json(f"analytics_{i}.json")
