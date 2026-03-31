from flask import Flask, jsonify
import subprocess
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return "Trivy Security Scanner Demo"

@app.route('/health')
def health():
    return jsonify({"status": "healthy"})

@app.route('/scan-info')
def scan_info():
    return jsonify({
        "app": "Trivy Demo",
        "scan_commands": [
            "trivy image <image-name>",
            "trivy image --severity CRITICAL,HIGH <image>",
            "trivy config .",
            "trivy fs ."
        ],
        "docs": "https://trivy.dev/"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
