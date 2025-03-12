from flask import Flask, request, jsonify
from app.models import Book, Genre, session

app = Flask(__name__)

@app.route('/books', methods=['GET'])
def get_books():
    genre_name = request.args.get('genre')
    rating_value = request.args.get('rating')

    query = session.query(Book)

    if genre_name:
        genre = session.query(Genre).filter_by(name=genre_name).first()
        if genre:
            query = query.filter_by(genre_id=genre.id)

    if rating_value:
        query = query.filter_by(rating=rating_value)

    books = query.all()
    result = []

    for book in books:
        result.append({
            'title': book.title,
            'price': book.price,
            'rating': book.rating,
            'genre': session.query(Genre).filter_by(id=book.genre_id).first().name
        })

    return jsonify(result)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
