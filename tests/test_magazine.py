import pytest
from lib.models.magazine import Magazine
from lib.models.author import Author
from lib.models.article import Article

def test_magazine_creation_and_save():
    mag = Magazine("Nature Insights", "Environment")
    mag.save()
    fetched = Magazine.find_by_id(mag.id)
    assert fetched.name == "Nature Insights"
    assert fetched.category == "Environment"

def test_magazine_articles():
    mag = Magazine("Innovate Now", "Technology")
    mag.save()
    author = Author("Elon Musk")
    author.save()
    Article("Mars Colonization Plans", author.id, mag.id).save()
    Article("The Future of AI", author.id, mag.id).save()

    articles = mag.articles()
    titles = [a["title"] for a in articles]
    assert "Mars Colonization Plans" in titles
    assert "The Future of AI" in titles

def test_magazine_contributors():
    mag = Magazine("Creative Minds", "Art & Culture")
    mag.save()
    a1 = Author("Frida Kahlo")
    a2 = Author("Pablo Picasso")
    a1.save()
    a2.save()
    Article("Surrealism in Painting", a1.id, mag.id).save()
    Article("Cubism Explained", a2.id, mag.id).save()

    contributors = mag.contributors()
    names = [c["name"] for c in contributors]
    assert "Frida Kahlo" in names
    assert "Pablo Picasso" in names
