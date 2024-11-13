from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Izinkan akses CORS untuk pengembangan

@app.route('/data', methods=['GET'])
def get_data():
    data = {
        "suhumax": 36,
        "suhumin": 21,
        "suhurata": 28.35,
        "nilai_suhu_max_humid_max": [
            {
                "idx": 101,
                "suhu": 36,
                "humid": 36,
                "kecerahan": 25,
                "timestamp": "2010-09-18 07:23:48"
            },
            {
                "idx": 226,
                "suhu": 36,
                "humid": 36,
                "kecerahan": 27,
                "timestamp": "2011-05-02 12:29:34"
            }
        ],
        "month_year_max": [
            {
                "month_year": "9-2010"
            },
            {
                "month_year": "5-2011"
            }
        ]
    }
    return jsonify(data)

# Endpoint untuk menghidangkan file HTML dari folder frontend
@app.route('/')
def serve_frontend():
    return send_from_directory('frontend', 'index.html')

@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory('frontend', path)

if __name__ == '__main__':
    app.run(debug=True)
