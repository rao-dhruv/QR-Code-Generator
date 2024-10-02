from flask import Flask, request, send_file
import pyqrcode
import os

app = Flask(__name__)

@app.route('/generate_qr', methods=['POST'])
def generate_qr():
    link = request.json.get('link')
    qrcode = pyqrcode.create(link)
    qrcode_file = "qr_code.png"
    qrcode.png(qrcode_file, scale=5)

    return send_file(qrcode_file, mimetype='image/png')

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
