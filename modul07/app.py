from flask import Flask, jsonify
import os
import pwd

app = Flask(__name__)

@app.route('/')
def hello():
    try:
        current_user = pwd.getpwuid(os.getuid()).pw_name
    except:
        current_user = f"UID {os.getuid()}"
    
    return f"Running as user: {current_user}"

@app.route('/health')
def health():
    return jsonify({"status": "healthy"})

@app.route('/security-info')
def security_info():
    try:
        current_user = pwd.getpwuid(os.getuid()).pw_name
    except:
        current_user = f"UID {os.getuid()}"
    
    return jsonify({
        "user": current_user,
        "uid": os.getuid(),
        "gid": os.getgid(),
        "is_root": os.getuid() == 0,
        "recommendation": "Container should NOT run as root!"
    })

@app.route('/test-write')
def test_write():
    """Testet ob in /etc geschrieben werden kann (sollte fehlschlagen)"""
    try:
        with open('/etc/test-file', 'w') as f:
            f.write('test')
        return jsonify({"error": "SECURITY ISSUE: Could write to /etc!"})
    except PermissionError:
        return jsonify({"status": "OK - Cannot write to /etc (as expected)"})

if __name__ == '__main__':
    # Port 8080 für non-privileged User
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)
