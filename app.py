from flask import Flask, request, send_file, jsonify, render_template
import pyqrcode
from PIL import Image

app = Flask(__name__)

# Route to serve the HTML form
@app.route('/')
def home():
    return render_template('index.html')

# Defining an endpoint to generate the QR code
@app.route('/generate_qr', methods=['POST'])
def generate_qr():
    try:
        data = request.get_json()
        link = data['link']

        qrcode = pyqrcode.create(link)
        qrcode_file = "qr_code.png"
        qrcode.png(qrcode_file, scale=5)

        return send_file(qrcode_file, mimetype='image/png')

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
