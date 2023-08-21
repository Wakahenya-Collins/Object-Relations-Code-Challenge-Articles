import pytest
from ..magazine.author import Author
from ..magazine.article import Article
from ..magazine.magazine import Magazine

# Test Author class
def test_author_creation():
    author = Author("John Doe")
    assert author.name() == "John Doe"

def test_author_add_article():
    author = Author("John Doe")
    magazine = Magazine("Tech Magazine", "Technology")
    article = author.add_article(magazine, "Python Programming")
    assert article.author() == author
    assert article.magazine() == magazine
    assert article.title() == "Python Programming"

# Test Article class
def test_article_creation():
    author = Author("John Doe")
    magazine = Magazine("Tech Magazine", "Technology")
    article = Article(author, magazine, "Python Programming")
    assert article.author() == author
    assert article.magazine() == magazine
    assert article.title() == "Python Programming"

# Test Magazine class
def test_magazine_creation():
    magazine = Magazine("Tech Magazine", "Technology")
    assert magazine.name() == "Tech Magazine"
    assert magazine.category() == "Technology"

def test_magazine_add_contributor():
    magazine = Magazine("Tech Magazine", "Technology")
    author = Author("John Doe")
    magazine.add_contributor(author)
    assert author in magazine.contributors()

def test_magazine_find_by_name():
    magazine = Magazine("Tech Magazine", "Technology")
    found_magazine = Magazine.find_by_name("Tech Magazine")
    assert found_magazine == magazine

def test_magazine_article_titles():
    author = Author("John Doe")
    magazine = Magazine("Tech Magazine", "Technology")
    author.add_article(magazine, "Python Programming")
    author.add_article(magazine, "Web Development")
    assert magazine.article_titles() == ["Python Programming", "Web Development"]

# Run the tests
if __name__ == "__main__":
    pytest.main()
