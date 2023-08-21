class Magazine:
    _all = []

    def __init__(self, name, category):
        self._name = name
        self._category = category
        self._contributors = []
        self._all.append(self)

    def name(self):
        return self._name

    def category(self):
        return self._category

    def add_contributor(self, author):
        self._contributors.append(author)

    def contributors(self):
        return self._contributors

    def contributing_authors(self):
        return [author for author in self._contributors if len(author.articles()) > 2]
    
    @classmethod
    def all(cls):
        return cls._all
    
    @classmethod
    def article_titles(cls):
         return [article.title() for magazine in cls._all for author in magazine._contributors for article in author._articles]


    @classmethod
    def find_by_name(cls, name):
        for magazine in cls._all:
            if magazine.name() == name:
                return magazine
    
    