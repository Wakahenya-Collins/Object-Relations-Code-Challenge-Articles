import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import unittest
from magazine.author import Author
from magazine.article import Article
from magazine.magazine import Magazine

class TestArticles(unittest.TestCase):
    def setUp(self):
        self.author1 = Author("John Doe")
        self.author2 = Author("Jane Smith")

        self.magazine1 = Magazine("Tech Magazine", "Technology")
        self.magazine2 = Magazine("Science Journal", "Science")

        self.author1.add_article(self.magazine1, "Python Programming")
        self.author2.add_article(self.magazine2, "Quantum Mechanics")

    def test_author_name(self):
        self.assertEqual(self.author1.name(), "John Doe")

    def test_author_articles(self):
        self.assertEqual(len(self.author1.articles()), 1)
        self.assertEqual(len(self.author2.articles()), 1)


class TestMagazines(unittest.TestCase):
    def setUp(self):
        self.author1 = Author("John Doe")
        self.magazine1 = Magazine("Tech Magazine", "Technology")
        self.magazine2 = Magazine("Science Journal", "Science")

        self.author1.add_article(self.magazine1, "Python Programming")

    def test_magazine_name(self):
        self.assertEqual(self.magazine1.name(), "Tech Magazine")

    def test_magazine_category(self):
        self.assertEqual(self.magazine1.category(), "Technology")


if __name__ == "__main__":
    unittest.main()
