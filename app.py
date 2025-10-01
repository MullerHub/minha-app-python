from flask import Flask, render_template
import os

app = Flask(__name__)

# Cor de fundo padrão é verde
BACKGROUND_COLOR = os.environ.get('APP_COLOR', 'green')

@app.route("/")
def main():
    return render_template('index.html', color=BACKGROUND_COLOR)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
