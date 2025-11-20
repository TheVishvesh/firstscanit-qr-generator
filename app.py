from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
import io
import base64
from qr_generator import generate_artistic_qr

app = Flask(__name__)
# Enable CORS for all domains and routes
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/')
def home():
    return "FirstScanIt QR API is Running!"

@app.route('/health')
def health():
    return jsonify({'status': 'healthy'}), 200

@app.route('/api/generate', methods=['POST'])
def generate_qr():
    try:
        data = request.json.get('data')
        style = request.json.get('style', 'geometric')
        size = int(request.json.get('size', 300))
        
        # Generate QR
        buffer = io.BytesIO()
        generate_artistic_qr(data, style, size // 10, buffer)
        buffer.seek(0)
        
        # Return base64 image
        img_base64 = base64.b64encode(buffer.getvalue()).decode()
        return jsonify({
            'success': True,
            'image': f'data:image/png;base64,{img_base64}'
        })
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'success': False, 'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
