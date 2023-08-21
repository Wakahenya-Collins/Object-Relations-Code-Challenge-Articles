from .article import Article
# from magazine import Magazine

class Author:
    _all = []

    def __init__(self, name):
        self._name = name
        self._articles = []

    def name(self):
        return self._name

    def articles(self):
        return self._articles

    def magazines(self):
        return list({article.magazine() for article in self._articles})

    def add_article(self, magazine, title):
        article = Article(self, magazine, title)
        self._articles.append(article)
        magazine.add_contributor(self)
        return article

    def topic_areas(self):
        topic_areas = {article.magazine().category() for article in self._articles}
        return list(topic_areas)

    @classmethod
    def all(cls):
        return cls._all
