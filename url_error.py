class UrlError(Exception):
    def __init__(self, url):
        self.url = url
        super().__init__()

    def __str__(self):
        return f"Url error: {self.url}"
