import pytest
from lib.models.article import Article
from lib.models.author import Author
from lib.models.magazine import Magazine

def test_article_creation_and_save():
    author = Author("Isabel Allende")
    magazine = Magazine("World Stories", "Literature")
    author.save()
    magazine.save()

    article = Article("The House of the Spirits Revisited", author.id, magazine.id)
    article.save()

    assert article.id is not None

def test_article_belongs_to_author_and_magazine():
    author = Author("Haruki Murakami")
    magazine = Magazine("Modern Tales", "Fiction")
    author.save()
    magazine.save()

    article = Article("Kafka on the Shore: A Study", author.id, magazine.id)
    article.save()

    assert article.author_id == author.id
    assert article.magazine_id == magazine.id
