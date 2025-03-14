import requests
from bs4 import BeautifulSoup
from .models import Book, Genre, session

def parse_books():
    base_url = "https://books.toscrape.com"
    response = requests.get(base_url)
    soup = BeautifulSoup(response.text, 'html.parser')

    categories = soup.find('ul', class_='nav nav-list').find_all('a')

    for category in categories:
        genre_name = category.text.strip()
        genre_url = base_url + "/" + category['href']

        genre = Genre(name=genre_name)
        session.add(genre)
        session.commit()

        response = requests.get(genre_url)
        soup = BeautifulSoup(response.text, 'html.parser')

        books = soup.find_all('article', class_='product_pod')

        for book in books:
            title = book.h3.a['title']
            price = book.find('p', class_='price_color').text
            rating = book.p['class'][1]

            book_obj = Book(title=title, price=price, rating=rating, genre_id=genre.id)
            session.add(book_obj)
        session.commit()
