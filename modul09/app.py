
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return """
    <html>
    <head><title>Modul 07 - ACR Demo</title></head>
    <body style="font-family:Arial; padding:40px; background:#0078d4; color:white;">
        <h1>Azure Container Registry Demo</h1>
        <p>Dieses Image wurde erfolgreich aus der Azure Container Registry geladen!</p>
        <hr>
        <p><strong>Modul 07</strong> – Image Build &amp; Push zur ACR</p>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)