from flask import Flask, render_template, request
import urllib.request
import webbrowser

app = Flask(__name__, template_folder=r'./templates') # Relative path to reach the templates folder

@app.route('/')
@app.route('/luhn/')
def hello():
    return render_template('luhn.html')

if __name__ == "__main__":
    webbrowser.open_new("http://localhost:8080/luhn/")
    app.run('localhost', 8080, True, use_reloader=False)