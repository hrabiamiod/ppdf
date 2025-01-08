from flask import Flask
from datetime import datetime
import time

app = Flask(__name__)

@app.route('/')
def hello():
    # Pobierz aktualny czas
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Aktualna godzina</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
                background-color: #f4f4f9;
            }
            #clock {
                font-size: 2em;
                color: #333;
            }
        </style>
    </head>
    <body>
        <div id="clock"></div>
        <script>
            function updateClock() {
                const now = new Date();
                const hours = String(now.getHours()).padStart(2, '0');
                const minutes = String(now.getMinutes()).padStart(2, '0');
                const seconds = String(now.getSeconds()).padStart(2, '0');
                document.getElementById('clock').textContent = `${hours}:${minutes}:${seconds}`;
            }

            // Uruchamianie funkcji co 1 sekundę
            setInterval(updateClock, 1000);

            // Natychmiastowe wyświetlenie godziny po załadowaniu stronyaaa
            updateClock();
        </script>
    </body>
    </html>
    """

if __name__ == '__main__':
    # Uruchamiamy Flask na porcie 5000
    app.run(host='0.0.0.0', port=5000)
