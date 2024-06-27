from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.json.get('data')
    g = 9.81  # Asumiendo la gravedad constante en m/s^2

    constants = []
    for item in data:
        p = item['pressure']
        rho = item['density']
        v = item['velocity']
        y = item['height']
        
        constant = p + (0.5 * rho * v ** 2) + (rho * g * y)
        constants.append(constant)

    return jsonify({'constants': constants})

if __name__ == '__main__':
    app.run(debug=True)
