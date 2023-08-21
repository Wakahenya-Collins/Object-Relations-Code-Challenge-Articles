# class Author:
#     def __init__(self, name):
#         self.name = name
#         self.article = []
    
#     #method to add article // write articles

# def write_article(self, title, magazine):
    

class Article:
    _all = []

    def __init__(self, author, magazine, title):
        self._author = author
        self._magazine = magazine
        self._title = title
        self._all.append(self)

    def title(self):
        return self._title

    def author(self):
        return self._author

    def magazine(self):
        return self._magazine

    @classmethod
    def all(cls):
        return cls._all
   