from flask import Flask, render_template, request, jsonify
from tyrageosaure import tyrageosaure

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/tirage', methods=['POST'])
def tirage():
    participants = request.json.get('participants', [])
    if len(participants) < 2:
        return jsonify({'error': 'Il faut au moins 2 participants!'}), 400
    
    result = tyrageosaure(participants)
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)
