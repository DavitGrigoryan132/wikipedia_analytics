class UrlError(Exception):
    """Custom exception class for URL-related errors."""

    def __init__(self, url):
        """Initialize UrlError with the given URL.

        Args:
            url (str): The URL that caused the error.
        """
        self.url = url
        super().__init__()

    def __str__(self):
        """Return a string representation of the error."""
        return f"Url error: {self.url}"
