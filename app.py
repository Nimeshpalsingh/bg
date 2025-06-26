from flask import Flask, request, send_file
from rembg import remove
import io
import os  # 🔥 Port env ke liye use hoga

app = Flask(__name__)

@app.route('/')
def index():
    return '✅ Background Remover API running!'

@app.route('/remove-bg', methods=['POST'])
def remove_bg():
    if 'image' not in request.files:
        return "No image found", 400
    img = request.files['image']
    result = remove(img.read())
    return send_file(io.BytesIO(result), mimetype='image/png')

# ✅ Only needed for local testing (optional)
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # 🔥 Render se port milega
    app.run(host='0.0.0.0', port=port)        # 🔥 Har jagah se accessible
