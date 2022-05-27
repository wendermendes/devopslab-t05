from flask import Flask

app = Flask(__name__)
app.config['WTF_CSRF_ENABLED'] = True

@app.route("/")
def pagina_inicial():
    return "Hello Word, this is my personalized message, By: Wender Oliveira."

if __name__ == '__main__':
    app.run()