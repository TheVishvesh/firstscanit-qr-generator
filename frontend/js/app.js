const API_URL = 'https://qr-generator-backend-b65c.onrender.com';

document.getElementById('qrForm').addEventListener('submit', async function(e) {
    e.preventDefault();
    const btn = e.target.querySelector('button');
    btn.innerText = "Generating...";
    btn.disabled = true;
    
    const data = document.getElementById('qrData').value;
    const style = document.getElementById('style').value;
    const size = document.getElementById('size').value;
    
    try {
        console.log("Sending request to:", `${API_URL}/api/generate`);
        
        const res = await fetch(`${API_URL}/api/generate`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Accept': 'application/json'
            },
            body: JSON.stringify({ data, style, size })
        });
        
        console.log("Response status:", res.status);
        
        const result = await res.json();
        
        if (result.success) {
            document.getElementById('output').innerHTML = `<img src="${result.image}" alt="QR Code">`;
        } else {
            alert("Error: " + (result.error || "Failed to generate"));
        }
    } catch (err) {
        console.error("Fetch error:", err);
        alert("Network Error: Check console for details. " + err.message);
    } finally {
        btn.innerText = "Generate QR";
        btn.disabled = false;
    }
});
