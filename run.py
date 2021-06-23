from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    desc = db.Column(db.String(500))

    def __repr__(self):
        return f'{self.name} - {self.desc}'

@app.route('/')
def home():
    return "Working demo"

@app.route('/books')
def get_books():
    data = Book.query.order_by(Book.id.desc()).all()
    output = []
    for item in data:
        row = {"name":item.name, "desc":item.desc}
        output.append(row)
    return {"books":output,"total_books":len(output)}

@app.route('/books/<id>')
def get_book(id):
    data = Book.query.get_or_404(id)
    output = [{"name":data.name, "desc":data.desc}]
    return {"books":output,"total_books":len(output)}

@app.route('/books', methods=['POST'])
def add_book():
    data = Book(name=request.json['name'],desc=request.json['desc'])
    db.session.add(data)
    db.session.commit()
    return { "id":data.id }

@app.route('/books/update', methods=['POST'])
def update_book():
    data = Book.query.filter(Book.id == request.json['id']).first()
    if data:
        data.name = request.json['name']
        data.desc = request.json['desc']
        db.session.commit()
        return { 'message' : 'success' }
    else:
        return { "message" : "error, id not found"}

if __name__ == "__main__":
    app.run(debug=True)
