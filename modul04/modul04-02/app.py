from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return f"Docker Scout Demo - Python {os.sys.version}"

@app.route('/health')
def health():
    return jsonify({"status": "healthy"})

@app.route('/info')
def info():
    return jsonify({
        "app": "Docker Scout Demo",
        "python_version": os.sys.version,
        "scan_status": "check with: docker scout cves <image>"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
