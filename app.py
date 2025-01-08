from flask import Flask
from datetime import datetime
import time

app = Flask(__name__)

@app.route('/')
def hello():
    # Pobierz aktualny czas
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"""
    <html>
      <head>
        <meta http-equiv="refresh" content="1">
        <!-- Powoduje automatyczne odświeżanie strony co 1s, aby czas się aktualizował -->
      </head>
      <body style="font-family: sans-serif;">
        <h1>Witaj na mojej stronie! Teraz jest po update 2</h1>
        <h3>Aktualny czas: {now}</h3>
      </body>
    </html>
    """

if __name__ == '__main__':
    # Uruchamiamy Flask na porcie 5000
    app.run(host='0.0.0.0', port=5000)
