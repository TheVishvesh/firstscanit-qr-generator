const API_URL = 'https://firstscanit-qr-api.onrender.com';

document.getElementById('qrForm').addEventListener('submit', async function (e) {
    e.preventDefault();
    const data = document.getElementById('qrData').value;
    const style = document.getElementById('style').value;
    const size = document.getElementById('size').value;
    const res = await fetch(`${API_URL}/api/generate`, {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({data, style, size, format: 'png'})
    });
    const result = await res.json();
    if (result.success) {
        document.getElementById('output').innerHTML = `<img src="${result.image}" alt="QR">`;
    } else {
        document.getElementById('output').innerText = "Failed to generate QR";
    }
});
