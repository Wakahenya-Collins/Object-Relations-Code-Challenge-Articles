from magazine.author import Author
from magazine.article import Article 
from magazine.magazine import Magazine 

def main():
    # Creating authors
    author1 = Author("John mbugua")
    author2 = Author("Jane mwongeli")

    # Creating magazines
    magazine1 = Magazine("Tech Magazine", "Technology")
    magazine2 = Magazine("Science Journal", "Science")

    # Adding articles and associating them with authors and magazines
    author1.add_article(magazine1, "Python Programming")
    author1.add_article(magazine2, "Quantum Mechanics")
    author1.add_article(magazine1, "Robotics")
    author1.add_article(magazine1, "AI integration")
    author2.add_article(magazine1, "AI and Ethics")

    # Displaying authors and their contributions
    print("Authors and their contributions:")
    for author in Author.all():
        print(f"{author.name()}: {', '.join([article.title() for article in author.articles()])}")

    # Displaying magazines and their contributors
    print("\nMagazines and their contributors:")
    for magazine in Magazine.all():
        print(f"{magazine.name()} ({magazine.category()}): {', '.join([contributor.name() for contributor in magazine.contributors()])}")

    # Finding a magazine by name
    found_magazine = Magazine.find_by_name("Tech Magazine")
    if found_magazine:
        print(f"\nFound magazine: {found_magazine.name()}")
    else:
        print("\nMagazine not found.")

    # Displaying article titles for all magazines
    print("\nArticle titles for all magazines:")
    for magazine in Magazine.all():
        article_titles = [article.title() for author in magazine.contributors() for article in author.articles()]
        print(f"{magazine.name()}: {', '.join(article_titles)}")

    ## Displaying authors who have written more than 2 articles for each magazine
    print("\nAuthors contributing more than 2 articles for each magazine:")
    for magazine in Magazine.all():
        print(f"{magazine.name()} ({magazine.category()}):", end=" ")
        contributing_authors = []

        for author in magazine.contributors():
            if len(author.articles()) > 2:
                contributing_authors.append(author.name())

        if contributing_authors:
            print(", ".join(contributing_authors))
        else:
            print("None")

if __name__ == "__main__":
    main()
