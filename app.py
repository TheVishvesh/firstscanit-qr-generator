from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
import io
import base64
from qr_generator import generate_artistic_qr, generate_svg_qr

app = Flask(__name__)
CORS(app)

@app.route('/health')
def health():
    return jsonify({'status':'ok'})

@app.route('/api/generate', methods=['POST'])
def generate_qr():
    data = request.json.get('data')
    style = request.json.get('style', 'geometric')
    size = int(request.json.get('size', 300))
    fmt = request.json.get('format', 'png')

    buf = io.BytesIO()
    if fmt == 'svg':
        generate_svg_qr(data, style, buf)
        buf.seek(0)
        return send_file(buf, mimetype='image/svg+xml')
    else:
        generate_artistic_qr(data, style, size // 10, buf)
        buf.seek(0)
        img64 = base64.b64encode(buf.getvalue()).decode()
        return jsonify({'image': f'data:image/png;base64,{img64}', 'success': True})

if __name__ == "__main__":
    app.run(debug=True, port=5000)
