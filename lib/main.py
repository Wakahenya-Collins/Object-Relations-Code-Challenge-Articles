import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


from magazine.author import Author
from magazine.article import Article
from magazine.magazine import Magazine

def main():
    # Creating authors
    author1 = Author("JM Kariuki")
    author2 = Author("Ken Walibora")

    # Creating magazines
    magazine1 = Magazine("Tech Magazine", "Technology")
    magazine2 = Magazine("Science Journal", "Science")

    # Adding articles and associating them with authors and magazines
    author1.add_article(magazine1, "Python Programming")
    author1.add_article(magazine2, "Quantum Mechanics")
    author2.add_article(magazine1, "AI and Ethics")

    # Accessing magazine contributors
    print(f"Contributors for {magazine1.name()}: {', '.join([contributor.name() for contributor in magazine1.contributors()])}")
    print(f"Contributors for {magazine2.name()}: {', '.join([contributor.name() for contributor in magazine2.contributors()])}")

    # Finding a magazine by name
    found_magazine = Magazine.find_by_name("Tech Magazine")
    if found_magazine:
        print(f"Found magazine: {found_magazine.name()}")
    else:
        print("Magazine not found.")

    # Accessing article titles for all magazines
    print("Article titles for all magazines:", Magazine.article_titles())

    # Iterating over authors and their articles
    for author in Author.all():
        for article in author.articles():
            for magazine in Magazine.all():
                if article.magazine() == magazine:
                    articles.append(article.title())

    # Printing authors contributing more than 2 articles for a magazine
    for magazine in Magazine.all():
        contributing_authors = magazine.contributing_authors()
        if contributing_authors:
            authors = [author.name() for author in contributing_authors]
            if len(authors) > 2:
                print(f"Authors contributing more than 2 articles for {magazine.name()}: {', '.join(authors)}")

if __name__ == "__main__":
    main()
