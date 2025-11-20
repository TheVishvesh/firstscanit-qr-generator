const API_URL = 'https://qr-generator-backend-b65c.onrender.com';

let currentQRImage = null;

document.getElementById('qrForm').addEventListener('submit', async function(e) {
    e.preventDefault();
    
    const data = document.getElementById('qrData').value;
    const style = document.getElementById('style').value;
    const size = document.getElementById('size').value;
    
    // Show loading, hide output and errors
    document.getElementById('loading').style.display = 'block';
    document.getElementById('output').style.display = 'none';
    document.getElementById('error').style.display = 'none';
    
    console.log('Generating QR code...');
    console.log('API URL:', API_URL);
    console.log('Data:', data, 'Style:', style, 'Size:', size);
    
    try {
        const response = await fetch(`${API_URL}/api/generate`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Accept': 'application/json'
            },
            body: JSON.stringify({ data, style, size })
        });
        
        console.log('Response status:', response.status);
        
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        
        const result = await response.json();
        console.log('Result:', result);
        
        if (result.success) {
            document.getElementById('qrDisplay').innerHTML = 
                `<img src="${result.image}" alt="Generated QR Code" style="max-width:100%; border-radius:10px; box-shadow:0 4px 15px rgba(0,0,0,0.1);">`;
            document.getElementById('output').style.display = 'block';
            currentQRImage = result.image;
        } else {
            throw new Error(result.error || 'Failed to generate QR code');
        }
    } catch (error) {
        console.error('Error:', error);
        document.getElementById('errorMessage').textContent = error.message;
        document.getElementById('error').style.display = 'block';
    } finally {
        document.getElementById('loading').style.display = 'none';
    }
});

function downloadQR() {
    if (!currentQRImage) {
        alert('No QR code to download');
        return;
    }
    
    const link = document.createElement('a');
    link.download = 'firstscanit-qr-code.png';
    link.href = currentQRImage;
    link.click();
}
