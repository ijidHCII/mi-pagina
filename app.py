import os
from flask import Flask, send_from_directory

BASE = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__)

@app.route("/")
def home():
    return send_from_directory(BASE, "index.html")

@app.route("/pdf/<nombre>")
def serve_pdf(nombre):
    pdf_folder = os.path.join(BASE, "pdfs")
    return send_from_directory(pdf_folder, nombre, mimetype="application/pdf")

if __name__ == "__main__":
    app.run(debug=True)

