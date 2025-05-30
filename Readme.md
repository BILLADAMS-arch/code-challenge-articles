## Phase 3 Code Challenge: Articles
## Overview
This project builds a content publishing platform using plain Python classes and raw SQL (without an ORM like SQLAlchemy). It manages relationships among authors, articles, and magazines, allowing flexible database interactions through direct SQL queries. The system models the following relationships:

One author can write multiple articles

A magazine can feature multiple articles

Each article is linked to one author and one magazine

This results in a many-to-many relationship between authors and magazines through the articles they share.

## Layout
code-challenge-articles/
├── Pipfile
├── Pipfile.lock
├── .gitignore
├── README.md
├── articles.db
├── lib/
│   ├── __init__.py
│   ├── debug.py
│   ├── db/
│   │   ├── __init__.py
│   │   ├── connection.py
│   │   ├── schema.sql
│   │   └── seed.py
│   └── models/
│       ├── __init__.py
│       ├── author.py
│       ├── magazine.py
│       └── article.py
├── scripts/
│   └── setup_db.py
└── tests/
    ├── __init__.py
    ├── test_author.py
    ├── test_article.py
    └── test_magazine.py

## Setup Guide
1. Clone the Repository
git clone https://github.com/BILLADAMS-arch/code-challenge-articles
cd code-challenge-articles

2. Install Dependencies with Pipenv
Ensure that you have pipenv installed. Then, run:
pipenv install
pipenv shell

3. Set Up the Database
Run the following script to initialize the database and load sample data:
python -m scripts.setup_db
This will execute the schema and seed files to prepare the articles.db SQLite database.

## How to Run Tests
To run the unit tests for the models, use:
pytest
This will execute all test cases in the tests/ directory, covering Author, Article, and Magazine functionality.

 ## Key Capabilities

Assign articles to authors and magazines

Retrieve all magazines for which an author has written

Manage database transactions with basic validations

Integrate raw SQL queries into Python classes

Create and update authors, magazines, and articles

List all authors who have contributed to a magazine

Retrieve all articles written by a specific author

## Technology Stack
Python 3.8 or higher

SQLite (via built-in sqlite3 module)

Pipenv for dependency and virtual environment management

Pytest for unit testing

Development Tools

## Debugging
You can explore the database and models interactively using the debug script:

python lib/debug.py

This launches an interactive Python shell preloaded with model access and database connection helpers.

