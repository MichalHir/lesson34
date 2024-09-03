from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

# Create an instance of the Flask class
app = Flask(__name__)

# Configure the SQLAlchemy Database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pets.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Define the Pet model
class Pet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    image = db.Column(db.String(200), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age,
            'image': self.image
        }

# Create the database and tables
with app.app_context():
    db.create_all()

# Pet list
@app.route('/pets/', methods=['GET'])
def pets_list():
    pets = Pet.query.all()
    return jsonify([pet.to_dict() for pet in pets])

@app.route('/pets/', methods=['POST'])
def add_pet():
    data = request.get_json()
    new_pet = Pet(
        name=data['name'],
        age=data['age'],
        image=data['image']
    )
    db.session.add(new_pet)
    db.session.commit()
    return jsonify({'result': 'added successfully'}), 201

@app.route('/pets/<int:id>/', methods=['GET'])
def single_pet(id):
    pet = Pet.query.get(id)
    if pet:
        return jsonify(pet.to_dict())
    return jsonify({'result': 'Pet not found'}), 404

@app.route('/pets/<int:id>', methods=['DELETE'])
def delete_pet(id):
    pet = Pet.query.get(id)
    if pet:
        db.session.delete(pet)
        db.session.commit()
        return jsonify({'result': 'Pet deleted successfully'}), 200
    return jsonify({'result': 'Pet not found'}), 404

@app.route('/pets/<int:id>', methods=['PUT'])
def update_pet(id):
    pet = Pet.query.get(id)
    if pet:
        data = request.get_json()
        pet.name = data.get('name', pet.name)
        pet.age = data.get('age', pet.age)
        pet.image = data.get('image', pet.image)
        db.session.commit()
        return jsonify({'result': 'Pet updated successfully'}), 200
    return jsonify({'result': 'Pet not found'}), 404

# Run the app only if this script is executed (not imported)
if __name__ == '__main__':
    app.run(debug=True)
