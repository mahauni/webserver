from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__)

@app.route('/form')
def index():
    return render_template("index.html",
    data = [{'hair': 'Encaracolado'}, {'hair': 'Longo'}, {'hair': 'Curto'}, {'hair': 'Tijela'}])

@app.route('/postend', methods=['POST', 'GET'])
def postend():
    nome = request.form['nome']
    email = request.form['email']
    car = request.form.get('hair')
    print(nome)
    print(email)
    print(str(car))
    return render_template("postend.html")

@app.route('/')
def initial():
    return render_template('initial.html')

if __name__ == "__main__":
    app.run(debug=True)