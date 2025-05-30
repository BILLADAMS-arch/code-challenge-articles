from lib.models.author import Author
from lib.models.magazine import Magazine
from lib.models.article import Article

def test_author_creation_and_articles():
    author = Author("Arundhati Roy")
    author.save()
    magazine = Magazine("Voices of Asia", "Culture")
    magazine.save()
    article = Article("The God of Small Things Revisited", author.id, magazine.id)
    article.save()

    articles = author.articles()
    assert any(a["title"] == "The God of Small Things Revisited" for a in articles)

def test_author_magazines():
    author = Author("Neil Gaiman")
    author.save()
    m1 = Magazine("Fantasy World", "Fantasy")
    m2 = Magazine("Graphic Novels Monthly", "Comics")
    m1.save()
    m2.save()
    Article("Coraline and Beyond", author.id, m1.id).save()
    Article("The Sandman Chronicles", author.id, m2.id).save()
    mags = author.magazines()
    assert len(mags) == 2
