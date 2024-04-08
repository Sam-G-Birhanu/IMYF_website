from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS



app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:0000@localhost/user'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(100), nullable=False)
    fathername = db.Column(db.String(100), nullable=False)
    dob = db.Column(db.String(20), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    age_group = db.Column(db.String(10), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    examCenter = db.Column(db.String(100), nullable=False)
@app.route('/api/generate_pdf', methods=['OPTIONS'])
def handle_options():
    return '', 200, {
        'Access-Control-Allow-Origin': 'http://localhost:4200',
        'Access-Control-Allow-Methods': 'POST',
        'Access-Control-Allow-Headers': 'Content-Type'
    }
    
# Route to handle user registration
@app.route('/register', methods=['POST'])
def register_user():
    data = request.get_json()
    new_user = User(
        fullname=data['fullname'],
        fathername=data['fathername'],
        dob=data['dob'],
        age=data['age'],
        age_group=data['age_group'],
        email=data['email'],
        examCenter=data['examCenter']
    )
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User registered successfully'})

if __name__ == '__main__':
    # Create the database tables based on the defined models
    db.create_all()
    # Run the Flask application
    app.run(debug=True)