class Article:
    _all = []  # Class variable to hold all instances of Article

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self._title = title  # Change title to a private attribute
        Article._all.append(self)  # Add the instance to the class variable

    @property
    def title(self):
        return self._title  # Add property for title to enforce immutability

    @title.setter
    def title(self, value):
        raise AttributeError("title is immutable")  # Add setter to enforce immutability

        
class Author:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        raise AttributeError("name is immutable")

    def articles(self):
        return [article for article in Article._all if article.author == self]

    def magazines(self):
        return list(set(article.magazine for article in self.articles()))

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        categories = list(set(magazine.category for magazine in self.magazines()))
        return categories if categories else None

class Magazine:
    def __init__(self, name, category):
        self._name = name
        self._category = category

    @property
    def name(self):
        return self._name  # Add property for name to allow access

    @name.setter
    def name(self, value):
        raise AttributeError("name is immutable")  # Add setter to enforce immutability

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not value:
            raise ValueError("Category must be a non-empty string")
        self._category = value

    def articles(self):
        return [article for article in Article._all if article.magazine == self]

    def contributors(self):
        return list(set(article.author for article in self.articles()))

    def article_titles(self):
        titles = [article.title for article in self.articles()]
        return titles if titles else None

    def contributing_authors(self):
        author_count = {}
        for article in self.articles():
            author_count[article.author] = author_count.get(article.author, 0) + 1
        top_authors = [author for author, count in author_count.items() if count > 2]
        return top_authors if top_authors else None
