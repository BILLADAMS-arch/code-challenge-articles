from lib.models.author import Author
from lib.models.magazine import Magazine
from lib.models.article import Article

def seed_data():
    a1 = Author("Toni Morrison")
    a1.save()
    a2 = Author("Gabriel García Márquez")
    a2.save()
    a3 = Author("Chimamanda Ngozi Adichie")
    a3.save()

    m1 = Magazine("Global Literature", "Culture")
    m2 = Magazine("Modern Politics", "Politics")
    m3 = Magazine("Science Monthly", "Science")
    m1.save()
    m2.save()
    m3.save()

    Article("Beloved and Memory", a1.id, m1.id).save()
    Article("Magical Realism Explained", a2.id, m1.id).save()
    Article("The Danger of a Single Story", a3.id, m2.id).save()
    Article("Political Narratives in Africa", a3.id, m2.id).save()
    Article("The Future of Genetic Engineering", a2.id, m3.id).save()

    print("Seeding complete.")

if __name__ == "__main__":
    seed_data()
