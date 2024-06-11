
from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

places = [
    {'name': 'Burj Khalifa', 'description': 'The tallest building in the world.'},
    {'name': 'Dubai Mall', 'description': 'The largest shopping mall in the world.'},
    {'name': 'Palm Jumeirah', 'description': 'An artificial archipelago in the shape of a palm tree.'},
    {'name': 'Dubai Fountain', 'description': 'A large choreographed fountain in front of the Burj Khalifa.'},
    {'name': 'Dubai Marina', 'description': 'A waterfront neighborhood with luxury yachts and apartments.'},
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/places')
def places():
    return render_template('places.html', places=places)

@app.route('/plan')
def plan():
    return render_template('plan.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/api/get_places')
def get_places():
    return jsonify(places)

@app.route('/api/create_plan', methods=['POST'])
def create_plan():
    data = request.get_json()
    plan = {'name': data['name'], 'places': [random.choice(places) for _ in range(int(data['num_places']))]}
    return jsonify(plan)

@app.route('/api/send_email', methods=['POST'])
def send_email():
    data = request.get_json()
    # Placeholder function to simulate sending an email
    print(f"Sending email to {data['email']}: {data['message']}")
    return jsonify({'success': True})

if __name__ == '__main__':
    app.run(debug=True)
