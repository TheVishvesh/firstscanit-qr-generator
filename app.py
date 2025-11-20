from flask import Flask, request, jsonify
from flask_cors import CORS
import io
import base64
from qr_generator import generate_artistic_qr

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*", "methods": ["GET", "POST", "OPTIONS"], "allow_headers": ["Content-Type"]}})

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
    response.headers.add('Access-Control-Allow-Methods', 'GET,POST,OPTIONS')
    return response

@app.route('/')
def home():
    return "FirstScanIt QR API is Running!"

@app.route('/health')
def health():
    return jsonify({'status': 'healthy'}), 200

@app.route('/api/generate', methods=['POST', 'OPTIONS'])
def generate_qr():
    if request.method == 'OPTIONS':
        return '', 204
        
    try:
        data = request.json.get('data')
        style = request.json.get('style', 'geometric')
        size = int(request.json.get('size', 300))
        
        if not data:
            return jsonify({'success': False, 'error': 'No data provided'}), 400
        
        buffer = io.BytesIO()
        generate_artistic_qr(data, style, size // 10, buffer)
        buffer.seek(0)
        
        img_base64 = base64.b64encode(buffer.getvalue()).decode()
        
        return jsonify({
            'success': True,
            'image': f'data:image/png;base64,{img_base64}',
            'style': style,
            'size': size
        }), 200
        
    except Exception as e:
        print(f"Error generating QR: {e}")
        return jsonify({'success': False, 'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
