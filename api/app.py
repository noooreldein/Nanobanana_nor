import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

MY_OWNER = "@n_7_3_a"
MY_CHANNEL = "https://t.me/n_7_3_a_2"
MY_NAME = "Noor"

ORIGINAL_API = "http://de3.bot-hosting.net:21007/kilwa-nanobanana-pro"

@app.route('/')
def home():
    return jsonify({"status": "running", "api": "NanoBanana Pro by Noor"})

@app.route('/generate', methods=['GET'])
def generate():
    text = request.args.get('text', '')
    if not text:
        return jsonify({"status": "error", "message": "استخدم ?text=وصف الصورة"}), 400

    try:
        resp = requests.get(ORIGINAL_API, params={'text': text}, timeout=15)
        resp.raise_for_status()
        data = resp.json()
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

    data['owner'] = MY_OWNER
    data['channel'] = MY_CHANNEL
    data['developer'] = MY_NAME

    return jsonify(data)
