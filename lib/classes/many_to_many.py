class Article:
    _all = []  # Class variable to hold all instances of Article

    def __init__(self, author, magazine, title):
        if not isinstance(author, Author):
            raise ValueError("Author must be an instance of Author.")
        if not isinstance(magazine, Magazine):
            raise ValueError("Magazine must be an instance of Magazine.")
        if not isinstance(title, str) or not (5 <= len(title) <= 50):
            raise ValueError("Title must be a string between 5 and 50 characters.")
        self.author = author
        self.magazine = magazine
        self._title = title
        Article._all.append(self)  # Add the instance to the class variable

    @property
    def title(self):
        return self._title  # Add property for title to enforce immutability

    @title.setter
    def title(self, value):
        raise AttributeError("title is immutable")  # Add setter to enforce immutability


class Author:
    def __init__(self, name):
        if not isinstance(name, str) or len(name) <= 0:
            raise ValueError("Name must be a non-empty string.")
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
        magazines = list(set(article.magazine for article in self.articles()))
        return magazines if magazines else []  # Change from None to an empty list

    def add_article(self, magazine, title):
        if not isinstance(magazine, Magazine):
            raise ValueError("The magazine must be an instance of Magazine.")
        if not isinstance(title, str) or not (5 <= len(title) <= 50):
            raise ValueError("Title must be a string between 5 and 50 characters.")
        return Article(self, magazine, title)

    def topic_areas(self):
        categories = list(set(magazine.category for magazine in self.magazines()))
        return categories if categories else []  # Change from None to an empty list


class Magazine:
    def __init__(self, name, category):
        if not isinstance(name, str) or not (2 <= len(name) <= 16):
            raise ValueError("Name must be a string between 2 and 16 characters.")
        self._name = name
        if not isinstance(category, str) or len(category) <= 0:
            raise ValueError("Category must be a non-empty string.")
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
        authors = list(set(article.author for article in self.articles()))
        return authors if authors else None

    def article_titles(self):
        titles = [article.title for article in self.articles()]
        return titles if titles else None

    def contributing_authors(self):
        author_count = {}
        for article in self.articles():
            author_count[article.author] = author_count.get(article.author, 0) + 1
        top_authors = [author for author, count in author_count.items() if count > 2]
        return top_authors if top_authors else None
